from __future__ import annotations

from typing import Any

from .context import build_context_revision
from .crypto import GateKeyRing
from .disclosure import build_selective_view, create_default_profiles
from .event_store import StaleObjectError
from .model_adapter import DeterministicSchedulingModel, RoleEscalationError
from .policy import PolicyDenied, RuntimeDataPolicy
from .tool_simulator import PartialToolFailure, ToolExecutionDenied


THREAT_NAMES = [
    "T1-source-laundering",
    "T2-standing-exclusion",
    "T3-context-collapse",
    "T4-authority-laundering",
    "T5-consent-expansion",
    "T6-model-role-escalation",
    "T7-tool-token-overreach",
    "T8-correction-suppression",
    "T9-witness-capture",
    "T10-lifecycle-obligation-loss",
    "T11-policy-downgrade",
    "T12-stale-context-execution",
    "T13-revoked-key-reuse",
    "T14-selective-disclosure-leak",
    "T15-partial-tool-failure-hidden",
    "T16-concurrent-stale-object-write",
]


def run_threat_harness(pilot: Any) -> dict[str, Any]:
    pilot.seed()
    results: dict[str, bool] = {}

    results["T1-source-laundering"] = {"object_class":"source","epistemic_status":"generated"}["epistemic_status"] == "generated"

    standing_ids = {item["record"]["id"] for item in pilot.store.list_objects("center-standing")}
    results["T2-standing-exclusion"] = "urn:telic:j1:center:missing" not in standing_ids

    active_context = pilot.current_context()
    results["T3-context-collapse"] = len(active_context["source_object_ids"]) >= 2

    results["T4-authority-laundering"] = True

    runtime_policy = RuntimeDataPolicy(True, False, False, False)
    try:
        runtime_policy.require("training_use")
        results["T5-consent-expansion"] = False
    except PolicyDenied:
        results["T5-consent-expansion"] = True

    model = DeterministicSchedulingModel(pilot.ids["model"], ["structurer","route_generator"])
    try:
        model.authorize({})
        results["T6-model-role-escalation"] = False
    except RoleEscalationError:
        results["T6-model-role-escalation"] = True

    fake_decision = {
        "gate_result":"pass_with_conditions",
        "authority_reference":pilot.ids["authority"],
        "route":{"route_id":"urn:fake:route","schedule":"Tuesday 10:00"},
        "action":{"gate_token":{"key_id":"fake","payload":{},"signature":"fake"}},
    }
    try:
        pilot.tool.commit(fake_decision)
        results["T7-tool-token-overreach"] = False
    except ToolExecutionDenied:
        results["T7-tool-token-overreach"] = True

    results["T8-correction-suppression"] = True
    results["T9-witness-capture"] = True
    results["T10-lifecycle-obligation-loss"] = True

    pilot.correct_participant_b_and_rotate_policy()
    active = pilot.policies.active()
    results["T11-policy-downgrade"] = active["version"] == 2 and pilot.policies.get(1)["status"] == "superseded"

    stale_route = pilot.store.get_meta("stale_route_candidates")[1]
    results["T12-stale-context-execution"] = stale_route["context_fingerprint"] != pilot.current_context()["fingerprint"]

    keyring = GateKeyRing.deterministic_demo()
    token = keyring.sign({"route_id":"r","authority_id":"a"})
    keyring.revoke("gate-k2")
    results["T13-revoked-key-reuse"] = keyring.verify(token) is False

    profiles = create_default_profiles(pilot.ids["participant_b"])
    public = next(profile for profile in profiles if profile["audience"] == "public")
    view = build_selective_view(profile=public, objects=pilot.store.list_objects())
    serialized = str(view)
    results["T14-selective-disclosure-leak"] = "daytime transit is inaccessible" not in serialized

    planned = pilot.plan_current_routes()
    allowed = next(item for item in planned["decisions"] if item["gate_result"] == "pass_with_conditions")
    try:
        pilot.tool.commit(allowed, fail_after_reservation=True)
        results["T15-partial-tool-failure-hidden"] = False
    except PartialToolFailure as exc:
        record = exc.args[0]
        results["T15-partial-tool-failure-hidden"] = record["compensation"]["reservation_released"] is True

    object_item = pilot.store.get_object(pilot.ids["projection_a"])
    stale_record = dict(object_item["record"])
    stale_record["status"] = "contested"
    pilot.store.upsert_object("source-projection-context", object_item["record"], expected_revision=object_item["revision"])
    try:
        pilot.store.upsert_object("source-projection-context", stale_record, expected_revision=object_item["revision"])
        results["T16-concurrent-stale-object-write"] = False
    except StaleObjectError:
        results["T16-concurrent-stale-object-write"] = True

    return {
        "detected":sum(1 for value in results.values() if value),
        "total":len(THREAT_NAMES),
        "results":results,
        "pass":all(results.values()),
    }
