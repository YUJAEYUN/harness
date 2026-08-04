import json
import tempfile
import unittest
from pathlib import Path

from research_snapshot.pipeline import SnapshotError, build_snapshot, compare_snapshots


class ResearchSnapshotTests(unittest.TestCase):
    def _request(self, root: Path, value: int, observed_at: str = "2026-12-31") -> Path:
        source = root / "source.csv"
        source.write_text(
            "company,metric,value,unit,observed_at\n"
            f"Alphabet,capital_expenditure,{value},USD_billion,{observed_at}\n",
            encoding="utf-8",
        )
        request = {
            "question": "CAPEX direction?",
            "as_of": "2026-08-04",
            "mode": "analyze",
            "agent_budget": {"max_agents": 2, "max_rounds": 1},
            "sources": [{
                "id": "capex",
                "type": "local_csv",
                "location": str(source),
                "provider": "official-ir",
                "publisher": "Alphabet",
                "source_family": "alphabet-ir",
                "evidence_grade": "A",
                "field_map": {
                    "entity": "company",
                    "metric": "metric",
                    "value": "value",
                    "unit": "unit",
                    "observed_at": "observed_at",
                },
            }],
        }
        path = root / "request.json"
        path.write_text(json.dumps(request), encoding="utf-8")
        return path

    def test_build_creates_validated_evidence_pack(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = build_snapshot(self._request(root, 200), root / "run")
            self.assertEqual("PASS", result["status"])
            pack = json.loads((root / "run/evidence/evidence_pack.json").read_text())
            self.assertEqual("ready_for_agents", pack["status"])
            self.assertEqual(200.0, pack["observations"][0]["value"])
            self.assertEqual({"max_agents": 2, "max_rounds": 1}, pack["agent_budget"])
            manifest = json.loads((root / "run/run_manifest.json").read_text())
            self.assertEqual(64, len(manifest["sources"][0]["sha256"]))

    def test_duplicate_observations_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request_path = self._request(root, 200)
            source = root / "source.csv"
            source.write_text(source.read_text() + "Alphabet,capital_expenditure,201,USD_billion,2026-12-31\n")
            result = build_snapshot(request_path, root / "run")
            self.assertEqual("FAIL", result["status"])
            report = json.loads((root / "run/validation/validation_report.json").read_text())
            failed = {item["check_id"] for item in report["checks"] if not item["passed"]}
            self.assertIn("observations.unique", failed)

    def test_snapshot_diff_reports_changed_values(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            before_root, after_root = root / "before-input", root / "after-input"
            before_root.mkdir()
            after_root.mkdir()
            build_snapshot(self._request(before_root, 200), root / "before")
            build_snapshot(self._request(after_root, 225), root / "after")
            result = compare_snapshots(root / "before", root / "after")
            self.assertEqual("PASS", result["status"])
            self.assertEqual(1, len(result["changed"]))
            self.assertEqual(200.0, result["changed"][0]["before"]["value"])
            self.assertEqual(225.0, result["changed"][0]["after"]["value"])

    def test_invalid_mode_is_rejected_before_collection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request_path = self._request(root, 200)
            request = json.loads(request_path.read_text())
            request["mode"] = "always_spawn_everyone"
            request_path.write_text(json.dumps(request))
            with self.assertRaises(SnapshotError):
                build_snapshot(request_path, root / "run")

    def test_mode_budget_is_enforced_before_collection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request_path = self._request(root, 200)
            request = json.loads(request_path.read_text())
            request["mode"] = "explain"
            request["agent_budget"] = {"max_agents": 2, "max_rounds": 1}
            request_path.write_text(json.dumps(request))
            with self.assertRaisesRegex(SnapshotError, "allows at most 1 agents"):
                build_snapshot(request_path, root / "run")


if __name__ == "__main__":
    unittest.main()
