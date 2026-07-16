from __future__ import annotations

import copy
from typing import Any

from .canonical import canonical_json, sha256_text, utc_now
from .ids import urn


PRIVATE_KEYS = {"content_or_reference", "consent_relation", "consent_basis", "correction_route"}


def create_default_profiles(participant_id: str) -> list[dict[str, Any]]:
    common = {
        "valid_time":{"from":utc_now(),"to":None},
        "status":"active",
    }
    return [
        {
            "profile_id":urn("disclosure-profile", "public"),
            "audience":"public",
            "included_families":["route-gate-action-consequence","event-witness-contest-repair","lifecycle-transfer-residual"],
            "included_object_ids":[],
            "redaction_rules":["remove direct source content","remove participant consent detail","replace private records with commitments"],
            "commitment_rules":["commit every omitted object by canonical SHA-256"],
            "purpose":"public verification of action, consequence, correction, and retirement",
            **common,
        },
        {
            "profile_id":urn("disclosure-profile", f"participant:{participant_id}"),
            "audience":"participant",
            "included_families":["center-standing","source-projection-context","route-gate-action-consequence","event-witness-contest-repair","lifecycle-transfer-residual"],
            "included_object_ids":[participant_id],
            "redaction_rules":["hide other participants direct source content"],
            "commitment_rules":["commit omitted other-participant objects"],
            "purpose":"participant review and correction",
            **common,
        },
        {
            "profile_id":urn("disclosure-profile", "operator"),
            "audience":"operator",
            "included_families":["center-standing","source-projection-context","purpose-authority-role","route-gate-action-consequence","event-witness-contest-repair","lifecycle-transfer-residual","authorization-policy","context-revision","correction-reachability","tool-transaction"],
            "included_object_ids":[],
            "redaction_rules":["remove data not required for scheduling operation"],
            "commitment_rules":["commit omitted records"],
            "purpose":"operate and review the bounded scheduling pilot",
            **common,
        },
        {
            "profile_id":urn("disclosure-profile", "verifier"),
            "audience":"verifier",
            "included_families":["*"],
            "included_object_ids":[],
            "redaction_rules":[],
            "commitment_rules":["commit all records"],
            "purpose":"independent full-scope verification",
            **common,
        },
    ]


def redact_record(record: dict[str, Any], *, audience: str, participant_id: str | None = None) -> dict[str, Any]:
    result = copy.deepcopy(record)
    center = result.get("center") or result.get("id")
    if audience == "verifier":
        return result
    if audience == "public":
        for key in list(result):
            if key in PRIVATE_KEYS:
                result[key] = {"redacted":True,"commitment":sha256_text(canonical_json(record[key]))}
        if result.get("object_class") == "source":
            result["content_or_reference"] = {"redacted":True,"commitment":sha256_text(canonical_json(record.get("content_or_reference")))}
    elif audience == "participant" and participant_id is not None:
        if center not in {participant_id, None} and result.get("object_class") in {"source","projection"}:
            if "content_or_reference" in result:
                result["content_or_reference"] = {"redacted":True,"commitment":sha256_text(canonical_json(record["content_or_reference"]))}
    return result


def build_selective_view(
    *,
    profile: dict[str, Any],
    objects: list[dict[str, Any]],
    participant_id: str | None = None,
) -> dict[str, Any]:
    audience = profile["audience"]
    include_all = "*" in profile["included_families"]
    visible = []
    commitments = []
    for item in objects:
        family = item["family"]
        record = item["record"]
        object_id = item["object_id"]
        permitted = include_all or family in profile["included_families"] or object_id in profile["included_object_ids"]
        if permitted:
            visible.append({"family":family,"object_id":object_id,"record":redact_record(record,audience=audience,participant_id=participant_id)})
        else:
            commitments.append({"object_id":object_id,"family":family,"commitment":item["object_hash"]})
    return {
        "view_id":urn("selective-view", profile["profile_id"]),
        "profile":profile,
        "visible_records":visible,
        "omitted_commitments":commitments,
        "record_count":len(visible),
        "omitted_count":len(commitments),
        "generated_at":utc_now(),
    }
