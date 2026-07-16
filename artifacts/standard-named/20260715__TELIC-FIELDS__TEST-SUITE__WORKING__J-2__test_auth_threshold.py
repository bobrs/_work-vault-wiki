from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j2.auth import AuthenticationError, RoleIdentityRegistry
from telic_j2.threshold import ThresholdCustody


class AuthThresholdTests(unittest.TestCase):
    def test_role_assertion_and_replay_rejection(self):
        with tempfile.TemporaryDirectory() as name:
            reg = RoleIdentityRegistry(Path(name)/"identities")
            reg.register("alice", ["participant"])
            assertion = reg.issue(actor_id="alice", role="participant", operation="correct", session_id="s1", subject="p1", nonce="n1")
            verified = reg.verify(assertion, required_role="participant", required_operation="correct", session_id="s1", consume_nonce=True)
            self.assertEqual(verified["actor_id"], "alice")
            with self.assertRaises(AuthenticationError):
                reg.verify(assertion, required_role="participant", required_operation="correct", session_id="s1", consume_nonce=True)

    def test_threshold_requires_distinct_approvals(self):
        with tempfile.TemporaryDirectory() as name:
            custody = ThresholdCustody(Path(name), {"a":"operator","b":"privacy","c":"verifier"}, threshold=2)
            digest = "a"*64
            one = custody.approve(custodian_id="a", release_id="r1", manifest_digest=digest, approved_at="2026-07-15T00:00:00Z")
            self.assertFalse(custody.verify_threshold([one], release_id="r1", manifest_digest=digest)["valid"])
            two = custody.approve(custodian_id="c", release_id="r1", manifest_digest=digest, approved_at="2026-07-15T00:00:00Z")
            result = custody.verify_threshold([one,two], release_id="r1", manifest_digest=digest)
            self.assertTrue(result["valid"])
            self.assertEqual(result["valid_custodians"], ["a","c"])


if __name__ == "__main__":
    unittest.main()
