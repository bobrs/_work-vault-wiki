from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j0.event_store import EventConflictError, EventStore


class EventStoreTests(unittest.TestCase):
    def test_idempotent_replay_and_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            store = EventStore(Path(name) / "events.sqlite3")
            event = {
                "event_id": "urn:test:event:1",
                "event_type": "observed",
                "subject": "urn:test:subject:1",
                "actor": "urn:test:actor:1",
                "valid_time": "2026-07-15T00:00:00Z",
                "recorded_time": "2026-07-15T00:00:00Z",
                "source_references": [],
                "authority_reference": None,
                "scope": {},
                "prior_state": None,
                "new_state": {"value": 1},
                "affected_centers": [],
                "descendant_impact": [],
                "contest": None,
                "correction": None,
                "repair": None,
                "witness": {},
                "status": "active",
            }
            first = store.append_event(event)
            second = store.append_event(event)
            self.assertFalse(first["idempotent_replay"])
            self.assertTrue(second["idempotent_replay"])
            changed = dict(event)
            changed["new_state"] = {"value": 2}
            with self.assertRaises(EventConflictError):
                store.append_event(changed)
            self.assertTrue(store.verify_chain()[0])

    def test_tamper_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            store = EventStore(Path(name) / "events.sqlite3")
            event = {
                "event_id": "urn:test:event:2",
                "event_type": "observed",
                "subject": "urn:test:subject:2",
                "actor": "urn:test:actor:2",
                "valid_time": "2026-07-15T00:00:00Z",
                "recorded_time": "2026-07-15T00:00:00Z",
                "source_references": [],
                "authority_reference": None,
                "scope": {},
                "prior_state": None,
                "new_state": {"value": 1},
                "affected_centers": [],
                "descendant_impact": [],
                "contest": None,
                "correction": None,
                "repair": None,
                "witness": {},
                "status": "active",
            }
            store.append_event(event)
            store._conn.execute("UPDATE events SET event_json = ? WHERE event_id = ?", ('{"tampered":true}', event["event_id"]))
            store._conn.commit()
            valid, errors = store.verify_chain()
            self.assertFalse(valid)
            self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
