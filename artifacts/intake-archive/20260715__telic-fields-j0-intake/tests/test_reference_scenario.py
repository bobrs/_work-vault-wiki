from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j0.scenario import ReferencePilot
from telic_j0.witness import verify_export


ROOT = Path(__file__).resolve().parents[1]


class ReferenceScenarioTests(unittest.TestCase):
    def test_full_scenario_and_independent_export(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            workdir = Path(name) / "run"
            export = Path(name) / "witness.zip"
            pilot = ReferencePilot(workdir, ROOT / "schemas")
            result = pilot.run_full(export)
            proofs = result["witness"]["proofs"]
            self.assertTrue(all(proofs.values()))
            self.assertEqual(result["status"]["step"], "retired")
            self.assertFalse(result["status"]["tool_credential_active"])
            verified = verify_export(export)
            self.assertTrue(verified["valid"], verified["errors"])
            self.assertGreaterEqual(verified["events_verified"], 10)
            self.assertGreaterEqual(verified["records_validated"], 10)

    def test_participant_correction_changes_protected_status(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            pilot = ReferencePilot(Path(name), ROOT / "schemas")
            pilot.seed()
            pilot.summarize()
            before = pilot.store.get_object(pilot.ids["projection_b"])["record"]
            self.assertFalse(before["protected_status"]["protected"])
            pilot.correct_participant_b()
            after = pilot.store.get_object(pilot.ids["projection_b"])["record"]
            self.assertTrue(after["protected_status"]["protected"])
            self.assertIn("required_window", after["content_or_reference"])

    def test_external_gate_blocks_morning_route(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            pilot = ReferencePilot(Path(name), ROOT / "schemas")
            result = pilot.plan_and_gate()
            blocked = [item for item in result["decisions"] if item["gate_result"] == "deny"]
            allowed = [item for item in result["decisions"] if item["gate_result"] == "pass_with_conditions"]
            self.assertEqual(len(blocked), 1)
            self.assertEqual(len(allowed), 1)
            self.assertIn("protected_conditions", blocked[0]["review"]["failed_checks"])


if __name__ == "__main__":
    unittest.main()
