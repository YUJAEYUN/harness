#!/usr/bin/env python3
"""Fail-closed validation gate for the KOSPI semiconductor bottom harness."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    evidence: str


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _float(value: str, label: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label}: numeric value required, got {value!r}") from exc
    if not math.isfinite(number):
        raise ValueError(f"{label}: finite value required, got {value!r}")
    return number


def _percentile_inc(values: Sequence[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def _weak_percentile(values: Sequence[float], target: float) -> float:
    return 100.0 * sum(value <= target for value in values) / len(values)


def _close(actual: float, expected: float, tolerance: float = 0.011) -> bool:
    return abs(actual - expected) <= tolerance


def _append(checks: List[Check], check_id: str, condition: bool, evidence: str) -> None:
    checks.append(Check(check_id, bool(condition), evidence))


def _validate_input(
    root: Path, name: str, spec: Mapping[str, Any], checks: List[Check]
) -> Tuple[List[str], List[Dict[str, str]]]:
    path = root / str(spec["path"])
    _append(checks, f"input.{name}.exists", path.is_file(), str(spec["path"]))
    if not path.is_file():
        return [], []

    digest = _sha256(path)
    _append(
        checks,
        f"input.{name}.sha256",
        digest == spec["sha256"],
        f"expected={spec['sha256']} actual={digest}",
    )
    columns, rows = _read_csv(path)
    missing = sorted(set(spec["required_columns"]) - set(columns))
    _append(checks, f"input.{name}.columns", not missing, f"missing={missing}")
    return columns, rows


def validate(root: Path, contract_path: Path) -> Dict[str, Any]:
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    checks: List[Check] = []

    _, price_rows = _validate_input(root, "price", contract["inputs"]["price"], checks)
    _, valuation_rows = _validate_input(root, "valuation", contract["inputs"]["valuation"], checks)

    if price_rows and valuation_rows:
        expected_rows = int(contract["dataset"]["row_count"])
        _append(checks, "dataset.price.row_count", len(price_rows) == expected_rows, f"actual={len(price_rows)}")
        _append(checks, "dataset.valuation.row_count", len(valuation_rows) == expected_rows, f"actual={len(valuation_rows)}")

        price_dates = [row["date"] for row in price_rows]
        valuation_dates = [row["date"] for row in valuation_rows]
        _append(checks, "dataset.price.unique_dates", len(price_dates) == len(set(price_dates)), f"rows={len(price_dates)} unique={len(set(price_dates))}")
        _append(checks, "dataset.valuation.unique_dates", len(valuation_dates) == len(set(valuation_dates)), f"rows={len(valuation_dates)} unique={len(set(valuation_dates))}")
        _append(checks, "dataset.dates.aligned", price_dates == valuation_dates, "price and valuation dates must match in the same order")
        _append(checks, "dataset.dates.ascending", price_dates == sorted(price_dates), "dates must be ascending")
        _append(checks, "dataset.start_date", price_dates[0] == contract["dataset"]["start_date"], f"actual={price_dates[0]}")
        _append(checks, "dataset.end_date", price_dates[-1] == contract["dataset"]["end_date"], f"actual={price_dates[-1]}")

        mismatched_closes = [
            p["date"] for p, v in zip(price_rows, valuation_rows)
            if not _close(_float(p["close"], p["date"]), _float(v["close"], v["date"]))
        ]
        _append(checks, "dataset.close.aligned", not mismatched_closes, f"mismatches={mismatched_closes[:5]}")

        valuation_by_date = {row["date"]: row for row in valuation_rows}
        price_by_date = {row["date"]: row for row in price_rows}
        for date, expected in contract["representative_observations"].items():
            if date not in price_by_date or date not in valuation_by_date:
                _append(checks, f"observation.{date}.exists", False, "date missing")
                continue
            actual = {
                "close": _float(price_by_date[date]["close"], f"{date}.close"),
                "per": _float(valuation_by_date[date]["per"], f"{date}.per"),
                "pbr": _float(valuation_by_date[date]["pbr"], f"{date}.pbr"),
            }
            for metric, expected_value in expected.items():
                _append(
                    checks,
                    f"observation.{date}.{metric}",
                    _close(actual[metric], float(expected_value)),
                    f"expected={expected_value} actual={actual[metric]}",
                )

        series: Dict[str, List[float]] = {}
        for metric in ("per", "pbr"):
            values = [_float(row[metric], f"{row['date']}.{metric}") for row in valuation_rows if row[metric] != ""]
            series[metric] = values
            missing_count = len(valuation_rows) - len(values)
            allowed_missing = int(contract["dataset"]["allowed_missing"].get(metric, 0))
            _append(checks, f"distribution.{metric}.missing", missing_count == allowed_missing, f"expected={allowed_missing} actual={missing_count}")
            calculated = {
                "min": min(values),
                "p10": _percentile_inc(values, 0.10),
                "median": _percentile_inc(values, 0.50),
                "p90": _percentile_inc(values, 0.90),
            }
            for statistic, expected_value in contract["distribution_checks"][metric].items():
                _append(
                    checks,
                    f"distribution.{metric}.{statistic}",
                    _close(calculated[statistic], float(expected_value)),
                    f"expected={expected_value} actual={calculated[statistic]:.4f}",
                )

        for date, expected in contract["percentile_checks"].items():
            row = valuation_by_date[date]
            for metric in ("per", "pbr"):
                target = _float(row[metric], f"{date}.{metric}")
                actual = round(_weak_percentile(series[metric], target), 1)
                expected_value = float(expected[f"{metric}_weak_pct"])
                _append(checks, f"percentile.{date}.{metric}", actual == expected_value, f"expected={expected_value:.1f} actual={actual:.1f}")

    for relative_path, required_phrases in contract["artifacts"].items():
        path = root / relative_path
        _append(checks, f"artifact.{relative_path}.exists", path.is_file(), relative_path)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for index, phrase in enumerate(required_phrases, start=1):
            _append(checks, f"artifact.{relative_path}.phrase_{index}", phrase in text, phrase)

    ic_path = root / "_workspace/kospi-bottom/03_ic_memo.md"
    if ic_path.is_file():
        ic_text = ic_path.read_text(encoding="utf-8")
        latest = ic_text.split("## LEGACY 감사기록 시작", 1)[0]
        _append(checks, "control.ic.latest_three_conditional", latest.count("| **CONDITIONAL** |") == 3, f"actual={latest.count('| **CONDITIONAL** |')}")
        _append(checks, "control.ic.latest_no_pass_grade", "| **PASS** |" not in latest, "latest IC must not issue PASS")
        withdrawn_probability_phrases = ("낙관 35%", "비관A 40%", "비관B 20%", "35%·40%·20%")
        present = [phrase for phrase in withdrawn_probability_phrases if phrase in latest]
        _append(checks, "control.ic.latest_no_withdrawn_probability", not present, f"present={present}")

    failed = [check for check in checks if not check.passed]
    return {
        "contract_version": contract["contract_version"],
        "contract_as_of": contract["as_of"],
        "validated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS" if not failed else "FAIL",
        "summary": {"passed": len(checks) - len(failed), "failed": len(failed), "total": len(checks)},
        "checks": [asdict(check) for check in checks],
    }


def _default_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=_default_root())
    parser.add_argument("--contract", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)

    root = args.root.resolve()
    contract_path = args.contract or root / ".claude/skills/kospi-semiconductor-bottom-harness/references/run-contract.json"
    report = validate(root, contract_path.resolve())
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        report_path = args.report if args.report.is_absolute() else root / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(output, encoding="utf-8")
    print(f"{report['status']}: {report['summary']['passed']}/{report['summary']['total']} checks passed")
    for check in report["checks"]:
        if not check["passed"]:
            print(f"FAIL {check['check_id']}: {check['evidence']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
