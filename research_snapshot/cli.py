"""Command-line interface for the static research snapshot runtime."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .pipeline import build_snapshot, compare_snapshots


def _load_dotenv(path: Path) -> None:
    """Populate missing os.environ entries from a KEY=VALUE .env file.

    Never overrides a variable already set in the real environment, so an
    explicit `export` still wins over the file. Intentionally minimal (no
    quoting/escaping rules beyond stripping surrounding quotes) to avoid a
    third-party dependency for a single local secrets file.
    """

    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="research-snapshot",
        description="Build deterministic evidence packs before invoking AI analysts.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    build = commands.add_parser("build", help="Build and validate one static snapshot")
    build.add_argument("--request", type=Path, required=True, help="Research request JSON")
    build.add_argument("--run-dir", type=Path, required=True, help="Snapshot output directory")

    diff = commands.add_parser("diff", help="Compare two completed snapshots")
    diff.add_argument("--before", type=Path, required=True)
    diff.add_argument("--after", type=Path, required=True)
    diff.add_argument("--output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    _load_dotenv(Path.cwd() / ".env")
    args = _parser().parse_args(argv)
    if args.command == "build":
        result = build_snapshot(args.request, args.run_dir)
    else:
        result = compare_snapshots(args.before, args.after)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1
