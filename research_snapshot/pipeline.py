"""Deterministic collection, normalization, validation, and snapshot comparison."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REQUIRED_REQUEST_FIELDS = {"question", "as_of", "mode", "sources"}
REQUIRED_OBSERVATION_FIELDS = {
    "entity",
    "metric",
    "value",
    "unit",
    "observed_at",
    "source_id",
}
ALLOWED_MODES = {"lookup", "explain", "analyze", "deep_research"}
# deep_research was originally set to 18 to match the kospi-semiconductor-bottom-harness
# headcount. docs/personal-market-research-agent-architecture.md's own migration goal is
# to shrink that fixed 18-person call down to a task-selected pool of 4-7 experts, so the
# ceiling here now reflects that target instead of the pre-refactor number.
MODE_MAX_AGENTS = {"lookup": 0, "explain": 1, "analyze": 3, "deep_research": 7}


class SnapshotError(ValueError):
    """Raised when a request or source violates the snapshot contract."""


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_request(request: dict[str, Any]) -> None:
    missing = REQUIRED_REQUEST_FIELDS - request.keys()
    if missing:
        raise SnapshotError(f"request missing required fields: {sorted(missing)}")
    if request["mode"] not in ALLOWED_MODES:
        raise SnapshotError(f"unsupported mode: {request['mode']}")
    if not isinstance(request["sources"], list) or not request["sources"]:
        raise SnapshotError("request.sources must be a non-empty list")
    budget = request.get("agent_budget", {"max_agents": 0, "max_rounds": 0})
    if not isinstance(budget, dict):
        raise SnapshotError("request.agent_budget must be an object")
    max_agents = budget.get("max_agents", 0)
    max_rounds = budget.get("max_rounds", 0)
    if not isinstance(max_agents, int) or max_agents < 0:
        raise SnapshotError("agent_budget.max_agents must be a non-negative integer")
    if not isinstance(max_rounds, int) or max_rounds < 0:
        raise SnapshotError("agent_budget.max_rounds must be a non-negative integer")
    if max_agents > MODE_MAX_AGENTS[request["mode"]]:
        raise SnapshotError(
            f"mode {request['mode']} allows at most {MODE_MAX_AGENTS[request['mode']]} agents"
        )
    source_ids = [source.get("id") for source in request["sources"]]
    if any(not source_id for source_id in source_ids) or len(source_ids) != len(set(source_ids)):
        raise SnapshotError("every source requires a unique non-empty id")
    dynamic_sources = [
        source for source in request["sources"] if source.get("type", "").startswith("generated_")
    ]
    if dynamic_sources and not request.get("allow_dynamic_collectors", False):
        raise SnapshotError(
            "generated collectors require request.allow_dynamic_collectors=true"
        )


def _run_generated_collector(source: dict[str, Any], target: Path) -> dict[str, Any]:
    """Run an explicitly approved agent-authored collector without a shell."""

    collector = source.get("collector")
    if not isinstance(collector, dict):
        raise SnapshotError(f"source {source.get('id')} requires collector configuration")
    command = collector.get("command")
    if (
        not isinstance(command, list)
        or not command
        or any(not isinstance(part, str) or not part for part in command)
    ):
        raise SnapshotError(f"source {source.get('id')} collector.command must be a string array")
    timeout = collector.get("timeout_seconds", 60)
    if not isinstance(timeout, int) or not 1 <= timeout <= 600:
        raise SnapshotError("collector.timeout_seconds must be between 1 and 600")

    env_names = collector.get("env", [])
    if not isinstance(env_names, list) or any(not isinstance(name, str) for name in env_names):
        raise SnapshotError("collector.env must be an array of environment variable names")
    missing_env = [name for name in env_names if name not in os.environ]
    if missing_env:
        raise SnapshotError(f"collector missing environment variables: {sorted(missing_env)}")
    inherited_names = ("PATH", "HOME", "LANG", "LC_ALL", "SYSTEMROOT", "TMPDIR")
    environment = {name: os.environ[name] for name in inherited_names if name in os.environ}
    environment.update({name: os.environ[name] for name in env_names})
    artifact_dir = target.parent / f"{source['id']}.artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    environment["RESEARCH_RAW_DIR"] = str(artifact_dir.resolve())

    cwd = Path(collector.get("cwd", ".")).resolve()
    if not cwd.is_dir():
        raise SnapshotError(f"collector working directory not found: {cwd}")
    code_paths = collector.get("code_paths", [])
    if not isinstance(code_paths, list) or any(not isinstance(item, str) for item in code_paths):
        raise SnapshotError("collector.code_paths must be an array of paths")
    code_hashes = []
    for item in code_paths:
        code_path = (cwd / item).resolve()
        if not code_path.is_file():
            raise SnapshotError(f"collector code path not found: {code_path}")
        code_hashes.append({"path": str(code_path), "sha256": _sha256(code_path)})
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SnapshotError(f"collector {source['id']} could not run: {error}") from error

    stderr_path = target.with_suffix(target.suffix + ".stderr.log")
    stderr_path.write_bytes(completed.stderr)
    if completed.returncode != 0:
        raise SnapshotError(
            f"collector {source['id']} exited with {completed.returncode}; see {stderr_path}"
        )
    if not completed.stdout:
        raise SnapshotError(f"collector {source['id']} returned no data on stdout")
    target.write_bytes(completed.stdout)

    artifact_hashes = [
        {"path": str(path), "sha256": _sha256(path)}
        for path in sorted(artifact_dir.rglob("*"))
        if path.is_file()
    ]

    return {
        "command": command,
        "cwd": str(cwd),
        "timeout_seconds": timeout,
        "stderr_path": str(stderr_path),
        "code_hashes": code_hashes,
        "artifact_hashes": artifact_hashes,
    }


def _collect_source(source: dict[str, Any], raw_dir: Path) -> tuple[Path, dict[str, Any] | None]:
    source_type = source.get("type")
    location = source.get("location")
    if source_type not in {
        "local_csv", "local_json", "http_csv", "http_json", "generated_csv", "generated_json"
    }:
        raise SnapshotError(f"unsupported source type for {source.get('id')}: {source_type}")
    if not location and not source_type.startswith("generated_"):
        raise SnapshotError(f"source {source.get('id')} is missing location")

    suffix = ".csv" if source_type.endswith("csv") else ".json"
    target = raw_dir / f"{source['id']}{suffix}"
    target.parent.mkdir(parents=True, exist_ok=True)
    collector_manifest = None
    if source_type.startswith("generated_"):
        collector_manifest = _run_generated_collector(source, target)
    elif source_type.startswith("local_"):
        origin = Path(location)
        if not origin.is_file():
            raise SnapshotError(f"local source not found: {origin}")
        shutil.copy2(origin, target)
    else:
        request = urllib.request.Request(
            location,
            headers={"User-Agent": "research-snapshot/1.0 contact=local-user"},
        )
        with urllib.request.urlopen(request, timeout=30) as response, target.open("wb") as output:
            shutil.copyfileobj(response, output)
    return target, collector_manifest


def _records(path: Path) -> list[dict[str, Any]]:
    if path.suffix == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as stream:
            return list(csv.DictReader(stream))
    value = _read_json(path)
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and isinstance(value.get("records"), list):
        return value["records"]
    raise SnapshotError(f"JSON source must be a list or contain records[]: {path}")


def _coerce_value(value: Any, value_type: str) -> Any:
    if value_type == "number":
        return float(str(value).replace(",", ""))
    if value_type == "integer":
        return int(str(value).replace(",", ""))
    return value


def _normalize(
    source: dict[str, Any], records: Iterable[dict[str, Any]]
) -> list[dict[str, Any]]:
    mapping = source.get("field_map", {})
    constants = source.get("constants", {})
    value_type = source.get("value_type", "number")
    output: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        observation: dict[str, Any] = {}
        for field in REQUIRED_OBSERVATION_FIELDS:
            if field == "source_id":
                observation[field] = source["id"]
            elif field in constants:
                observation[field] = constants[field]
            elif field in mapping and mapping[field] in record:
                observation[field] = record[mapping[field]]
        missing = REQUIRED_OBSERVATION_FIELDS - observation.keys()
        if missing:
            raise SnapshotError(
                f"source {source['id']} row {index} missing normalized fields: {sorted(missing)}"
            )
        observation["value"] = _coerce_value(observation["value"], value_type)
        observation["published_at"] = constants.get("published_at")
        observation["provider"] = source.get("provider")
        observation["publisher"] = source.get("publisher")
        observation["source_family"] = source.get("source_family", source["id"])
        observation["evidence_grade"] = source.get("evidence_grade", "C")
        observation["directly_observed"] = source.get("directly_observed", True)
        observation["row_number"] = index
        output.append(observation)
    return output


def _validation_checks(
    request: dict[str, Any], observations: list[dict[str, Any]], source_manifest: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    keys = [
        (item["entity"], item["metric"], item["observed_at"], item["source_id"])
        for item in observations
    ]
    return [
        {"check_id": "request.mode", "passed": request["mode"] in ALLOWED_MODES},
        {"check_id": "sources.collected", "passed": len(source_manifest) == len(request["sources"])},
        {"check_id": "observations.non_empty", "passed": bool(observations)},
        {
            "check_id": "observations.required_fields",
            "passed": all(REQUIRED_OBSERVATION_FIELDS <= item.keys() for item in observations),
        },
        {"check_id": "observations.unique", "passed": len(keys) == len(set(keys))},
        {
            "check_id": "sources.sha256",
            "passed": all(len(item["sha256"]) == 64 for item in source_manifest),
        },
    ]


def build_snapshot(request_path: Path | str, run_dir: Path | str) -> dict[str, Any]:
    """Build one immutable-style research snapshot from declarative sources."""

    request_path = Path(request_path)
    run_dir = Path(run_dir)
    request = _read_json(request_path)
    _validate_request(request)
    if run_dir.exists() and any(run_dir.iterdir()):
        raise SnapshotError(f"run directory must be empty: {run_dir}")
    raw_dir = run_dir / "raw"
    normalized_dir = run_dir / "normalized"
    evidence_dir = run_dir / "evidence"
    validation_dir = run_dir / "validation"
    for directory in (raw_dir, normalized_dir, evidence_dir, validation_dir):
        directory.mkdir(parents=True, exist_ok=True)

    shutil.copy2(request_path, run_dir / "request.json")
    observations: list[dict[str, Any]] = []
    source_manifest: list[dict[str, Any]] = []
    for source in request["sources"]:
        raw_path, collector_manifest = _collect_source(source, raw_dir)
        source_observations = _normalize(source, _records(raw_path))
        observations.extend(source_observations)
        source_manifest.append(
            {
                "id": source["id"],
                "type": source["type"],
                "raw_path": str(raw_path.relative_to(run_dir)),
                "sha256": _sha256(raw_path),
                "record_count": len(source_observations),
                "provider": source.get("provider"),
                "publisher": source.get("publisher"),
                "source_family": source.get("source_family", source["id"]),
                "evidence_grade": source.get("evidence_grade", "C"),
                "collector": collector_manifest,
            }
        )

    observations.sort(
        key=lambda item: (
            item["entity"],
            item["metric"],
            item["observed_at"],
            item["source_id"],
        )
    )
    observation_path = normalized_dir / "observations.jsonl"
    observation_path.write_text(
        "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in observations),
        encoding="utf-8",
    )
    checks = _validation_checks(request, observations, source_manifest)
    status = "PASS" if all(check["passed"] for check in checks) else "FAIL"
    validation = {"status": status, "checks": checks, "observation_count": len(observations)}
    _write_json(validation_dir / "validation_report.json", validation)

    evidence_pack = {
        "question": request["question"],
        "as_of": request["as_of"],
        "mode": request["mode"],
        "status": "ready_for_agents" if status == "PASS" else "blocked",
        "observations": observations,
        "source_families": sorted({item["source_family"] for item in source_manifest}),
        "missing_data": request.get("missing_data", []),
        "agent_budget": request.get("agent_budget", {"max_agents": 0, "max_rounds": 0}),
    }
    _write_json(evidence_dir / "evidence_pack.json", evidence_pack)
    manifest = {
        "schema_version": "1.0",
        "run_id": request.get("run_id", run_dir.name),
        "question": request["question"],
        "as_of": request["as_of"],
        "mode": request["mode"],
        "built_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "sources": source_manifest,
        "artifacts": {
            "observations": str(observation_path.relative_to(run_dir)),
            "evidence_pack": "evidence/evidence_pack.json",
            "validation": "validation/validation_report.json",
        },
    }
    _write_json(run_dir / "run_manifest.json", manifest)
    return {"status": status, "run_dir": str(run_dir), "observations": len(observations)}


def _load_observations(run_dir: Path) -> dict[tuple[str, str, str, str], dict[str, Any]]:
    path = run_dir / "normalized/observations.jsonl"
    if not path.is_file():
        raise SnapshotError(f"completed snapshot missing observations: {path}")
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        item = json.loads(line)
        key = (item["entity"], item["metric"], item["observed_at"], item["source_family"])
        result[key] = item
    return result


def compare_snapshots(before: Path | str, after: Path | str) -> dict[str, Any]:
    """Return deterministic additions, removals, and value changes between snapshots."""

    before_items = _load_observations(Path(before))
    after_items = _load_observations(Path(after))
    before_keys, after_keys = set(before_items), set(after_items)
    added = [after_items[key] for key in sorted(after_keys - before_keys)]
    removed = [before_items[key] for key in sorted(before_keys - after_keys)]
    changed = [
        {"before": before_items[key], "after": after_items[key]}
        for key in sorted(before_keys & after_keys)
        if before_items[key]["value"] != after_items[key]["value"]
    ]
    return {"status": "PASS", "added": added, "removed": removed, "changed": changed}
