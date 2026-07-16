#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"
TESTS = ROOT / "tests"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validator(name):
    schema = load(SCHEMAS / name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)

def validate(name, instance):
    errors = sorted(validator(name).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        raise AssertionError("; ".join(e.message for e in errors))

def positive_tests():
    passed = []

    high = load(EXAMPLES / "context-demand-high-consequence.json")
    low = load(EXAMPLES / "context-demand-reversible-draft.json")
    validate("context-demand-profile.schema.json", high)
    validate("context-demand-profile.schema.json", low)

    pd1 = load(EXAMPLES / "PD1-TOKEN-RICH-STANDING-POOR.json")
    validate("standing-coverage-assessment.schema.json", pd1["standing_assessment"])
    validate("context-capacity-profile.schema.json", pd1["capacity_profile"])
    validate("stop-escalation-decision.schema.json", pd1["stop_decision"])
    assert pd1["token_count"] > 100000
    assert pd1["capacity_profile"]["dimensions"]["standing_coverage"] == "insufficient"
    assert pd1["stop_decision"]["decision"] == "pause"
    assert pd1["capacity_profile"]["composite_score_is_governing"] is False
    passed.append("PD-1 token-rich but standing-poor")

    pd2 = load(EXAMPLES / "PD2-SMALL-CONTEXT-ADEQUATE.json")
    validate("context-capacity-profile.schema.json", pd2["capacity_profile"])
    validate("stop-escalation-decision.schema.json", pd2["decision"])
    assert len(pd2["context_items"]) == 3
    assert pd2["capacity_profile"]["overall_outcome"] == "adequate_for_narrower_action"
    assert pd2["decision"]["decision"] == "continue_with_conditions"
    passed.append("PD-2 small context adequate")

    pd3 = load(EXAMPLES / "PD3-PRIVACY-PRESERVING-CAPACITY.json")
    validate("context-capacity-profile.schema.json", pd3["prior_profile"])
    validate("context-capacity-profile.schema.json", pd3["new_profile"])
    assert pd3["prior_profile"]["dimensions"]["privacy_capacity"] == "degraded"
    assert pd3["new_profile"]["dimensions"]["privacy_capacity"] == "adequate"
    assert pd3["protected_omission"]["withheld"]
    passed.append("PD-3 privacy-preserving capacity")

    pd4 = load(EXAMPLES / "PD4-OVERLOAD-AUTHORITY-DEGRADATION.json")
    validate("overload-event.schema.json", pd4["overload"])
    validate("authority-degradation-record.schema.json", pd4["degradation"])
    assert pd4["degradation"]["prior_authority"] == "execute"
    assert pd4["degradation"]["current_authority"] == "recommend"
    assert pd4["degradation"]["tool_enforcement"]["execution_disabled"] is True
    passed.append("PD-4 authority degradation")

    pd5 = load(EXAMPLES / "PD5-MISSING-CORRECTION-STOP.json")
    validate("context-capacity-profile.schema.json", pd5["capacity_profile"])
    validate("stop-escalation-decision.schema.json", pd5["decision"])
    assert pd5["retrieval_included"] is False
    assert pd5["decision"]["decision"] == "stop"
    passed.append("PD-5 missing correction stop")

    pd6 = load(EXAMPLES / "PD6-PARTICIPANT-LOAD-STAGING.json")
    validate("participant-load-record.schema.json", pd6["participant_load"])
    assert pd6["participant_load"]["status"] == "overloaded"
    assert pd6["participant_load"]["silence_is_consent"] is False
    assert pd6["decision"]["rights_preserved"]
    passed.append("PD-6 participant-load staging")

    pd7 = load(EXAMPLES / "PD7-COMPETENT-ESCALATION.json")
    validate("escalation-record.schema.json", pd7["escalation"])
    assert pd7["escalation"]["target_competence_verified"] is True
    assert pd7["escalation"]["return_path"]
    assert pd7["escalation"]["context_withheld"]
    passed.append("PD-7 competent escalation")

    pd8 = load(EXAMPLES / "PD8-CONTEXT-RECONSTITUTION-RECOVERY.json")
    validate("context-capacity-profile.schema.json", pd8["new_capacity_profile"])
    validate("context-reconstitution-record.schema.json", pd8["reconstitution"])
    validate("capacity-debt-record.schema.json", pd8["remaining_capacity_debt"])
    assert pd8["reconstitution"]["restored_authority"] == "recommend"
    assert pd8["reconstitution"]["status"] == "partially_restored"
    assert pd8["remaining_capacity_debt"]["status"] == "open"
    passed.append("PD-8 context reconstitution")

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-token-count-sufficiency": lambda: x["token_count"] > 0 and not x["standing_review"] and x["declared_adequate"],
        "NC-2-fluent-authority-persistence": lambda: x["capacity_failed"] and x["fluent_output"] and x["execution_authority_retained"],
        "NC-3-privacy-as-deficit": lambda: x["valid_omission_proof"] and x["unnecessary_disclosure_requested"],
        "NC-4-participant-burden-blindness": lambda: x["participant_overloaded"] and x["full_review_required"] and x["silence_treated_as_agreement"],
        "NC-5-missing-correction": lambda: x["active_correction_exists"] and not x["retrieved"] and x["action_continues"],
        "NC-6-composite-score-concealment": lambda: x["composite_score"] > 0.9 and x["stop_capacity"] == "insufficient" and x["declared_adequate"],
        "NC-7-escalation-by-hierarchy-only": lambda: x["target_higher_status"] and not x["competence_verified"] and x["return_path"] is None,
        "NC-8-no-decision-without-cost-bearer": lambda: x["decision"] == "pause" and not x["cost_bearers"],
        "NC-9-capacity-debt-erasure": lambda: x["external_gap_exists"] and x["action_succeeded"] and not x["debt_recorded"],
        "NC-10-authority-restoration-without-reconstitution": lambda: x["restored_authority"] == "execute" and not x["new_context"] and not x["review"],
        "NC-11-small-context-rejection": lambda: x["action_class"] == "reversible_draft" and x["minimum_context_present"] and x["blocked_for_incomplete_full_field"],
        "NC-12-overload-without-degradation": lambda: x["overload_detected"] and not x["tool_authority_changed"] and x["execution_enabled"]
    }
    return checks[name]()

def main():
    schema_files = sorted(SCHEMAS.glob("*.json"))
    for path in schema_files:
        Draft202012Validator.check_schema(load(path))

    positive = positive_tests()
    fixtures = load(TESTS / "negative-conformance-fixtures.json")
    negative = []
    for name, fixture in fixtures.items():
        if not negative_detected(name, fixture):
            raise AssertionError(f"{name} was not detected")
        negative.append(name)

    result = {
        "schemas_checked": len(schema_files),
        "schema_errors": 0,
        "positive_demonstrations_passed": len(positive),
        "positive_demonstrations": positive,
        "negative_cases_detected": len(negative),
        "negative_cases": negative,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
