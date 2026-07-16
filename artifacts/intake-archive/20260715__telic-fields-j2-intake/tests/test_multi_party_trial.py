from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j2.trial import ReleaseCandidateTrial
from telic_j2.witness import verify_export


class MultiPartyTrialTests(unittest.TestCase):
    def test_full_trial(self):
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as name:
            work=Path(name)/"work"
            export=Path(name)/"witness.zip"
            trial=ReleaseCandidateTrial(work,root/"schemas")
            result=trial.run_full(export)
            proofs=result["witness"]["proofs"]
            for key in ["failed_gate","valid_action","correction_propagation","policy_rollback","queue_exactly_once","authenticated_roles","multi_party_correction","retirement_revocation"]:
                self.assertTrue(proofs[key],key)
            self.assertFalse(result["witness"]["review_status"]["external_human_review_complete"])
            self.assertEqual(result["witness"]["active_policy"]["version"],4)
            verified=verify_export(export)
            self.assertTrue(verified["valid"],verified["errors"])


if __name__ == "__main__":
    unittest.main()
