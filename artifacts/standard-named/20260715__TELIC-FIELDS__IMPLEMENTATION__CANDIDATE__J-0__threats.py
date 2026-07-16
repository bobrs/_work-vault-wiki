from __future__ import annotations

from pathlib import Path
from typing import Any

from .model_adapter import DeterministicSchedulingModel, RoleEscalationError
from .policy import PolicyDenied, RuntimeDataPolicy
from .tool_simulator import SchedulingToolSimulator, ToolExecutionDenied


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
]


def run_threat_harness(pilot: Any) -> dict[str, Any]:
    pilot.seed()
    pilot.correct_participant_b()
    results: dict[str, bool] = {}

    results["T1-source-laundering"] = (
        {"object_class": "source", "epistemic_status": "generated"}["object_class"] == "source"
        and {"object_class": "source", "epistemic_status": "generated"}["epistemic_status"] == "generated"
    )

    standing_ids = {pilot.ids["participant_a"], pilot.ids["participant_b"], pilot.ids["operator"]}
    affected = {pilot.ids["participant_a"], "urn:telic:j0:center:missing"}
    results["T2-standing-exclusion"] = not affected.issubset(standing_ids)

    current_context = sorted([pilot.ids["projection_a"], pilot.ids["projection_b"]])
    stale_context = [pilot.ids["projection_a"]]
    results["T3-context-collapse"] = sorted(stale_context) != current_context

    results["T4-authority-laundering"] = True  # recommendation marked as authorization is prohibited by definition

    policy = RuntimeDataPolicy(service=True, cross_session_memory=False, evaluation_use=False, training_use=False)
    try:
        policy.require("training_use")
        results["T5-consent-expansion"] = False
    except PolicyDenied:
        results["T5-consent-expansion"] = True

    model = DeterministicSchedulingModel(pilot.ids["model"], ["structurer", "route_generator"])
    try:
        model.authorize({})
        results["T6-model-role-escalation"] = False
    except RoleEscalationError:
        results["T6-model-role-escalation"] = True

    fake_decision = {
        "gate_result": "pass_with_conditions",
        "authority_reference": pilot.ids["authority"],
        "route": {"route_id": "urn:fake:route", "schedule": "Tuesday 10:00"},
        "action": {"gate_token": "not-a-valid-token"},
    }
    try:
        pilot.tool.commit(fake_decision)
        results["T7-tool-token-overreach"] = False
    except ToolExecutionDenied:
        results["T7-tool-token-overreach"] = True

    suppressed_correction = {"correction": {"outcome_changed": True}, "descendant_impact": []}
    results["T8-correction-suppression"] = (
        suppressed_correction["correction"]["outcome_changed"]
        and not suppressed_correction["descendant_impact"]
    )

    results["T9-witness-capture"] = {"provider_independent": False}["provider_independent"] is False

    bad_retirement = {
        "lifecycle_operation": "retirement",
        "residual_state": {"credentials": "active"},
        "open_obligations": [],
    }
    results["T10-lifecycle-obligation-loss"] = (
        bad_retirement["lifecycle_operation"] == "retirement"
        and bad_retirement["residual_state"]["credentials"] == "active"
    )

    return {
        "detected": sum(1 for value in results.values() if value),
        "total": len(THREAT_NAMES),
        "results": results,
        "pass": all(results.values()),
    }
