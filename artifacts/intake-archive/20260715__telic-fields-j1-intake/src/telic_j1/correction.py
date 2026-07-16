from __future__ import annotations

from typing import Any

from .canonical import utc_now
from .ids import urn


class CorrectionReachabilityEngine:
    def __init__(self, store: Any):
        self.store = store

    def report(
        self,
        *,
        correction_event_id: str,
        origin_object_id: str,
        updated_descendants: list[str],
        blocked_descendants: list[str] | None = None,
        unreachable_descendants: list[str] | None = None,
    ) -> dict[str, Any]:
        known = sorted({edge["descendant_id"] for edge in self.store.descendants(origin_object_id)})
        updated = sorted(set(updated_descendants))
        blocked = sorted(set(blocked_descendants or []))
        unreachable = sorted(set(unreachable_descendants or []))
        complete = set(known).issubset(set(updated) | set(blocked) | set(unreachable)) and not unreachable and not blocked
        status = "complete" if complete else ("blocked" if blocked else "partial")
        return {
            "report_id":urn("correction-reachability", correction_event_id),
            "correction_event_id":correction_event_id,
            "origin_object_id":origin_object_id,
            "known_descendants":known,
            "updated_descendants":updated,
            "blocked_descendants":blocked,
            "unreachable_descendants":unreachable,
            "complete_for_scope":complete,
            "generated_at":utc_now(),
            "status":status,
        }
