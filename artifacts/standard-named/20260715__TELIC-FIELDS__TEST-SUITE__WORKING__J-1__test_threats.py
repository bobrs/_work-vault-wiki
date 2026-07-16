from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j1.scenario import ReferencePilot
from telic_j1.threats import THREAT_NAMES, run_threat_harness

ROOT = Path(__file__).resolve().parents[1]


class ThreatHarnessTests(unittest.TestCase):
    def test_all_sixteen_threats_detected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            pilot = ReferencePilot(Path(name), ROOT/"schemas")
            result = run_threat_harness(pilot)
            self.assertTrue(result["pass"])
            self.assertEqual(result["detected"], len(THREAT_NAMES))
