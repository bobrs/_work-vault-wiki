from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j2.delivery_queue import DurableDeliveryQueue, SimulatedNetworkTimeout
from telic_j2.policy import AuthorizationPolicyRegistry
from telic_j2.policy_migration import PolicyMigrationManager


class QueuePolicyMigrationTests(unittest.TestCase):
    def test_timeout_after_apply_is_exactly_once(self):
        with tempfile.TemporaryDirectory() as name:
            queue = DurableDeliveryQueue(Path(name)/"queue.sqlite3")
            calls=[]
            def handler(payload):
                calls.append(payload["value"])
                return {"applied":payload["value"]}
            queue.enqueue(message_id="m1",dedupe_key="d1",sequence_no=1,payload={"value":7})
            with self.assertRaises(SimulatedNetworkTimeout):
                queue.process_one(handler,fault="timeout_after_apply")
            result=queue.process_one(handler)
            self.assertTrue(result["deduplicated"])
            self.assertEqual(calls,[7])
            self.assertEqual(queue.effect_count(),1)

    def test_policy_migration_rolls_back(self):
        registry=AuthorizationPolicyRegistry()
        registry.publish(version=2,purpose="bounded",allowed_operations=["prepare tool request"],prohibited_operations=["training reuse"],required_checks=["authority"])
        manager=PolicyMigrationManager(registry)
        failed=manager.attempt(version=3,purpose="bad",allowed_operations=["prepare tool request","training reuse"],prohibited_operations=[],required_checks=["authority"],validation=lambda p:(False,["training reuse"] if "training reuse" in p["allowed_operations"] else []))
        self.assertEqual(failed["status"],"rolled_back")
        self.assertEqual(registry.active()["version"],2)
        passed=manager.attempt(version=4,purpose="good",allowed_operations=["prepare tool request"],prohibited_operations=["training reuse"],required_checks=["authority"],validation=lambda p:(True,[]))
        self.assertTrue(passed["validation_passed"])
        self.assertEqual(registry.active()["version"],4)


if __name__ == "__main__":
    unittest.main()
