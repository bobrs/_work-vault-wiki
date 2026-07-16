from __future__ import annotations

from typing import Any

from .canonical import canonical_json, sha256_text, utc_now
from .ids import urn


class StaleContextError(RuntimeError):
    pass


def build_context_revision(
    *,
    context_seed: str,
    revision: int,
    source_objects: list[dict[str, Any]],
    correction_event_ids: list[str],
    status: str = "active",
) -> dict[str, Any]:
    object_ids = sorted(str(item["id"]) for item in source_objects)
    hashes = {str(item["id"]): sha256_text(canonical_json(item)) for item in source_objects}
    payload = {
        "context_seed": context_seed,
        "revision": revision,
        "source_object_ids": object_ids,
        "source_hashes": hashes,
        "correction_event_ids": sorted(correction_event_ids),
    }
    return {
        "context_id": urn("context", context_seed),
        "revision": revision,
        "source_object_ids": object_ids,
        "source_hashes": hashes,
        "correction_event_ids": sorted(correction_event_ids),
        "fingerprint": sha256_text(canonical_json(payload)),
        "created_at": utc_now(),
        "status": status,
    }


def require_current_context(route: dict[str, Any], current: dict[str, Any]) -> None:
    if route.get("context_fingerprint") != current.get("fingerprint"):
        raise StaleContextError("Route was generated from a stale context revision")
    if int(route.get("context_revision", -1)) != int(current.get("revision", -2)):
        raise StaleContextError("Route context revision does not match active context")
