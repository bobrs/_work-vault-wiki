from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j1.crypto import GateKeyRing
from telic_j1.scenario import ReferencePilot

ROOT = Path(__file__).resolve().parents[1]


class PolicyKeyContextTests(unittest.TestCase):
    def test_stale_context_and_policy_version_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            pilot = ReferencePilot(Path(name), ROOT/"schemas")
            stale = pilot.demonstrate_stale_rejection()
            self.assertEqual(stale["gate_result"], "deny")
            self.assertFalse(stale["gate_dimensions"]["context_current"])
            self.assertEqual(pilot.policies.active()["version"], 2)
            self.assertEqual(pilot.policies.get(1)["status"], "superseded")

    def test_revoked_key_cannot_verify_token(self) -> None:
        keyring = GateKeyRing.deterministic_demo()
        token = keyring.sign({"route_id":"r"})
        self.assertTrue(keyring.verify(token))
        keyring.revoke("gate-k2")
        self.assertFalse(keyring.verify(token))
