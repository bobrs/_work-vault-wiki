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

    centers = load(EXAMPLES / "temporal-centers.json")["records"]
    for record in centers:
        validate("temporal-center-reference.schema.json", record)
    assert centers[1]["representation_status"] == "projected"
    assert centers[1]["consent_state"] == "not_available"

    personal_continuity = load(EXAMPLES / "continuity-personal.json")
    validate("continuity-relation.schema.json", personal_continuity)

    pd1 = load(EXAMPLES / "PD1-PRESENT-ACTION-PRESERVES-LATER-OPTION.json")
    validate("future-standing-assessment.schema.json", pd1["future_standing_assessment"])
    validate("irreversibility-option-profile.schema.json", pd1["irreversibility_profile"])
    assert pd1["future_standing_assessment"]["future_consent"] == "not_available"
    assert pd1["selected_route"]["permanent_enrollment"] is False
    passed.append("PD-1 present action preserves later option")

    pd2 = load(EXAMPLES / "PD2-VALID-COMMITMENT-BINDS-WITHIN-SCOPE.json")
    validate("commitment-record.schema.json", pd2["commitment"])
    assert pd2["commitment"]["status"] == "active"
    assert pd2["gate"]["result"] == "decline_optional_work"
    passed.append("PD-2 valid commitment binds within scope")

    pd3 = load(EXAMPLES / "PD3-CHANGED-CONDITIONS-TRIGGER-REVIEW.json")
    validate("commitment-record.schema.json", pd3["commitment_before"])
    validate("commitment-record.schema.json", pd3["commitment_current"])
    validate("commitment-review-release.schema.json", pd3["review"])
    assert pd3["commitment_current"]["status"] == "due_for_review"
    assert pd3["review"]["review_result"] == "narrow"
    passed.append("PD-3 changed conditions trigger review")

    pd4 = load(EXAMPLES / "PD4-STALE-PROJECTION-LOSES-AUTHORITY.json")
    validate("temporal-state-change-event.schema.json", pd4["state_change_event"])
    assert pd4["projection"]["current_status"] == "stale"
    assert pd4["new_action_attempt"]["allowed"] is False
    assert pd4["historical_visibility"] is True
    passed.append("PD-4 stale projection loses authority")

    pd5 = load(EXAMPLES / "PD5-CONSENT-EXPIRES-WITHOUT-ERASING-WITNESS.json")
    validate("temporal-consent-authority.schema.json", pd5["consent"])
    validate("temporal-state-change-event.schema.json", pd5["expiry_event"])
    assert pd5["historical_use"]["authorized"] is True
    assert pd5["new_use"]["authorized"] is False
    passed.append("PD-5 expired consent preserves witness")

    pd6 = load(EXAMPLES / "PD6-FUTURE-STANDING-BLOCKS-IRREVERSIBLE-ACTION.json")
    validate("future-standing-assessment.schema.json", pd6["future_standing_assessment"])
    validate("irreversibility-option-profile.schema.json", pd6["irreversibility_profile"])
    assert pd6["future_standing_assessment"]["status"] == "material_future_standing_missing"
    assert pd6["irreversibility_profile"]["reversibility"] == "irreversible"
    assert pd6["gate"]["result"] == "pause"
    passed.append("PD-6 future standing blocks irreversible action")

    pd7 = load(EXAMPLES / "PD7-SUCCESSOR-INHERITS-OBLIGATIONS-NOT-UNLIMITED-AUTHORITY.json")
    validate("continuity-relation.schema.json", pd7["continuity"])
    validate("succession-obligation-record.schema.json", pd7["succession"])
    assert pd7["succession"]["obligations_transferred"]
    assert pd7["succession"]["authority_not_transferred"]
    passed.append("PD-7 successor obligations separated from authority")

    pd8 = load(EXAMPLES / "PD8-TEMPORAL-BREACH-REPAIR-AND-RELEASE.json")
    validate("temporal-breach-repair.schema.json", pd8["breach_repair"])
    validate("commitment-review-release.schema.json", pd8["commitment_review_release"])
    assert pd8["breach_repair"]["prior_witness_preserved"] is True
    assert pd8["commitment_review_release"]["review_result"] == "release"
    passed.append("PD-8 temporal breach repair and release")

    witness = load(EXAMPLES / "generated-temporal-decision-witness.json")
    validate("temporal-decision-witness.schema.json", witness)
    stream = load(EXAMPLES / "temporal-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [e["event_id"] for e in stream]

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-future-standing-as-consent": lambda: x["representation"] == "projected" and x["consent"] == "active",
        "NC-2-persistence-as-legitimacy": lambda: x["record_exists"] and not x["validity_review"] and x["treated_active"],
        "NC-3-permanent-commitment-sovereignty": lambda: x["binds_now"] and x["scope"] is None and x["review"] is None and x["release"] is None,
        "NC-4-historical-rewrite": lambda: x["later_correction"] and not x["prior_governing_version_preserved"],
        "NC-5-expired-consent-reuse": lambda: x["consent_state"] == "expired" and x["new_use_authorized"],
        "NC-6-stale-projection-action": lambda: x["projection_state"] == "stale" and x["used_as_current_direct_evidence"],
        "NC-7-asset-only-succession": lambda: x["assets_claimed"] and not x["attached_obligations_recorded"],
        "NC-8-unlimited-successor-authority": lambda: x["all_predecessor_authority_inherited"] and not x["operation_reviewed"],
        "NC-9-irreversible-closure-without-standing": lambda: x["irreversible"] and x["future_standing_missing"] and x["action_proceeds"],
        "NC-10-present-erasure": lambda: x["speculative_future_interest"] and x["urgent_present_standing"] and x["present_automatically_overridden"],
        "NC-11-release-as-erasure": lambda: x["commitment_released"] and x["past_consequence_deleted"] and x["valid_reliance_erased"],
        "NC-12-repair-as-forced-continuation": lambda: x["dissolution_legitimate"] and x["repair_requires_loop_continue"]
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
        "temporal_witness_valid": True,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
