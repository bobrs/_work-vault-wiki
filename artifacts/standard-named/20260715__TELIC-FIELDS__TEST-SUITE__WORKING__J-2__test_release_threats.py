from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j2.release_threats import RELEASE_THREAT_NAMES, run_release_threat_harness
from telic_j2.trial import ReleaseCandidateTrial


class ReleaseThreatHarnessTests(unittest.TestCase):
    def test_all_release_threats_detected(self):
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as name:
            trial=ReleaseCandidateTrial(Path(name)/"work",root/"schemas")
            result=run_release_threat_harness(trial)
            self.assertEqual(result["total"],len(RELEASE_THREAT_NAMES))
            self.assertEqual(result["detected"],len(RELEASE_THREAT_NAMES))
            self.assertTrue(result["pass"])


if __name__ == "__main__":
    unittest.main()
