"""Command-line interface for the static research snapshot runtime."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import build_snapshot, compare_snapshots


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
