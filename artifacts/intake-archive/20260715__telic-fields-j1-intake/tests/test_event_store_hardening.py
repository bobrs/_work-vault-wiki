from __future__ import annotations

import tempfile
import threading
import unittest
from pathlib import Path

from telic_j1.event_store import EventStore, StaleObjectError


def event(event_id: str) -> dict:
    return {
        "event_id":event_id,"event_type":"observed","subject":"urn:test:subject","actor":"urn:test:actor",
        "valid_time":"2026-07-15T00:00:00Z","recorded_time":"2026-07-15T00:00:00Z",
        "source_references":[],"authority_reference":None,"scope":{},"prior_state":None,"new_state":{"id":event_id},
        "affected_centers":[],"descendant_impact":[],"contest":None,"correction":None,"repair":None,"witness":{},"status":"active",
    }


class EventStoreHardeningTests(unittest.TestCase):
    def test_concurrent_appends_serialize_into_valid_chain(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            db = Path(name)/"events.sqlite3"
            initializer = EventStore(db)
            initializer.close()
            barrier = threading.Barrier(5)
            failures = []
            def worker(index: int) -> None:
                try:
                    store = EventStore(db)
                    barrier.wait()
                    store.append_event(event(f"urn:test:event:{index}"))
                    store.close()
                except Exception as exc:
                    failures.append(exc)
            threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
            for thread in threads: thread.start()
            for thread in threads: thread.join()
            self.assertFalse(failures, failures)
            store = EventStore(db)
            self.assertEqual(len(store.list_events()), 5)
            self.assertTrue(store.verify_chain()[0])

    def test_stale_object_revision_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            store = EventStore(Path(name)/"objects.sqlite3")
            record = {"id":"urn:test:object","status":"active"}
            revision = store.upsert_object("test", record)
            store.upsert_object("test", {"id":"urn:test:object","status":"corrected"}, expected_revision=revision)
            with self.assertRaises(StaleObjectError):
                store.upsert_object("test", {"id":"urn:test:object","status":"contested"}, expected_revision=revision)
