import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".claude/skills/kospi-semiconductor-bottom-harness/scripts/validate_run.py"
SPEC = importlib.util.spec_from_file_location("validate_run", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class HarnessValidationTests(unittest.TestCase):
    def test_repository_snapshot_passes_contract(self):
        contract = ROOT / ".claude/skills/kospi-semiconductor-bottom-harness/references/run-contract.json"
        report = VALIDATOR.validate(ROOT, contract)
        self.assertEqual("PASS", report["status"], [c for c in report["checks"] if not c["passed"]])
        self.assertGreaterEqual(report["summary"]["total"], 50)

    def test_tampered_raw_input_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            temp_root = Path(temporary)
            source = ROOT / "_workspace/kospi-bottom/00_input/krx_kospi_price_daily_2007_2026.csv"
            target = temp_root / "_workspace/kospi-bottom/00_input/krx_kospi_price_daily_2007_2026.csv"
            target.parent.mkdir(parents=True)
            shutil.copy2(source, target)
            text = target.read_text(encoding="utf-8-sig").replace("2007-01-02,1435.26", "2007-01-02,1435.27", 1)
            target.write_text(text, encoding="utf-8")

            contract_data = json.loads((ROOT / ".claude/skills/kospi-semiconductor-bottom-harness/references/run-contract.json").read_text(encoding="utf-8"))
            contract_data["inputs"]["valuation"]["path"] = str(ROOT / contract_data["inputs"]["valuation"]["path"])
            contract_data["artifacts"] = {}
            contract = temp_root / "contract.json"
            contract.write_text(json.dumps(contract_data), encoding="utf-8")

            report = VALIDATOR.validate(temp_root, contract)
            failed_ids = {check["check_id"] for check in report["checks"] if not check["passed"]}
            self.assertEqual("FAIL", report["status"])
            self.assertIn("input.price.sha256", failed_ids)


if __name__ == "__main__":
    unittest.main()
