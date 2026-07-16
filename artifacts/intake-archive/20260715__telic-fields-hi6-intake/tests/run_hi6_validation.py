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

    trace = load(EXAMPLES / "trace-hazard-marker.json")
    state = load(EXAMPLES / "memory-state-hazard.json")
    grant = load(EXAMPLES / "retrieval-authority-maintenance.json")
    validate("durable-trace-record.schema.json", trace)
    validate("memory-state-record.schema.json", state)
    validate("retrieval-authority-grant.schema.json", grant)

    pd1 = load(EXAMPLES / "PD1-USEFUL-TRAIL-WITHOUT-FIELD-RECONSTRUCTION.json")
    validate("durable-trace-record.schema.json", pd1["durable_trace"])
    validate("memory-state-record.schema.json", pd1["memory_state"])
    validate("retrieval-authority-grant.schema.json", pd1["retrieval_grant"])
    assert pd1["later_uptake"]["source_event_recreated"] is False
    assert pd1["durable_trace"]["integrity"]["complete_field_preserved"] is False
    passed.append("PD-1 useful trail without field reconstruction")

    pd2 = load(EXAMPLES / "PD2-SOURCE-AND-INFERENCE-REMAIN-DISTINCT.json")
    validate("memory-assertion-record.schema.json", pd2["source_assertion"])
    validate("memory-assertion-record.schema.json", pd2["model_inference"])
    assert pd2["source_assertion"]["assertion_class"] == "direct_source_statement"
    assert pd2["model_inference"]["assertion_class"] == "model_inference"
    assert pd2["collapsed_into_one_fact"] is False
    passed.append("PD-2 source and inference distinct")

    pd3 = load(EXAMPLES / "PD3-CORRECTION-PROPAGATES-INTO-ACTIVE-RETRIEVAL.json")
    validate("memory-assertion-record.schema.json", pd3["prior_assertion"])
    validate("memory-assertion-record.schema.json", pd3["correction_assertion"])
    validate("memory-state-record.schema.json", pd3["prior_memory_state"])
    validate("memory-state-record.schema.json", pd3["correction_memory_state"])
    assert pd3["correction_memory_state"]["eligible_for_action"] is True
    assert pd3["prior_memory_state"]["eligible_for_action"] is False
    assert pd3["retrieval_order"][0] == pd3["correction_assertion"]["assertion_id"]
    assert pd3["historical_version_preserved"] is True
    passed.append("PD-3 correction changes active retrieval")

    pd4 = load(EXAMPLES / "PD4-ARCHIVAL-MEMORY-INELIGIBLE-FOR-ACTION.json")
    validate("memory-state-record.schema.json", pd4["memory_state"])
    assert pd4["memory_state"]["state"] == "archival"
    assert pd4["historical_question"]["retrieved"] is True
    assert pd4["current_decision"]["retrieved_as_authority"] is False
    passed.append("PD-4 archival memory ineligible for action")

    pd5 = load(EXAMPLES / "PD5-SALIENCE-DECAY-WITHOUT-WITNESS-DELETION.json")
    validate("salience-decay-record.schema.json", pd5["salience"])
    assert pd5["ordinary_retrieval"] is False
    assert pd5["archival_witness_available"] is True
    assert pd5["trace_deleted"] is False
    assert pd5["salience"]["action_authority_effect"] == "none"
    passed.append("PD-5 salience decay without deletion")

    pd6 = load(EXAMPLES / "PD6-PROTECTED-FORGETTING.json")
    validate("forgetting-release-record.schema.json", pd6["forgetting_release"])
    assert pd6["active_retrieval"] is False
    assert pd6["training_use"] is False
    assert pd6["content_in_deletion_witness"] is False
    assert pd6["known_gap_preserved"] is True
    passed.append("PD-6 protected forgetting")

    pd7 = load(EXAMPLES / "PD7-STIGMERGIC-COORDINATION.json")
    validate("trace-link-coordination-record.schema.json", pd7["coordination"])
    assert pd7["coordination"]["central_controller"] is None
    assert pd7["central_command_required"] is False
    assert pd7["outer_purpose_presumed_legitimate"] is False
    passed.append("PD-7 stigmergic coordination")

    pd8 = load(EXAMPLES / "PD8-STALE-MEMORY-BREACH-AND-REPAIR.json")
    validate("memory-contamination-event.schema.json", pd8["contamination_event"])
    assert pd8["stale_trace"]["eligible_for_action"] is False
    assert pd8["current_trace"]["eligible_for_action"] is True
    assert pd8["prior_witness_preserved"] is True
    passed.append("PD-8 stale memory repair")

    envelope = load(EXAMPLES / "model-session-memory-envelope.json")
    transfer = load(EXAMPLES / "cross-loop-memory-transfer.json")
    validate("model-session-memory-envelope.schema.json", envelope)
    validate("cross-loop-memory-transfer.schema.json", transfer)
    assert envelope["correction_priority"] is True
    assert envelope["cross_user"]["allowed"] is False
    assert transfer["transformations"]

    witness = load(EXAMPLES / "generated-semantic-trail-witness.json")
    validate("semantic-trail-witness.schema.json", witness)
    stream = load(EXAMPLES / "semantic-trail-event-stream.json")["events"]
    for event in stream:
        validate("semantic-trail-event.schema.json", event)
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-trace-as-full-field": lambda: x["record_exists"] and x["claimed_complete_person_or_event"],
        "NC-2-retrieval-as-authority": lambda: x["retrieval_allowed"] and not x["action_authority"] and x["action_taken"],
        "NC-3-inference-laundering": lambda: x["model_inference_repeated"] and x["relabelled_direct_source"],
        "NC-4-archival-action": lambda: x["memory_state"] == "archival" and x["used_for_current_action"],
        "NC-5-correction-burial": lambda: x["active_correction_exists"] and x["corrected_trace_ranked_first"],
        "NC-6-salience-as-legitimacy": lambda: x["retrieval_frequency_high"] and x["authority_inferred"],
        "NC-7-decay-as-deletion": lambda: x["salience_below_threshold"] and x["historical_witness_deleted"],
        "NC-8-release-without-descendants": lambda: x["trace_released"] and x["known_derivatives_continue_use"] and not x["descendant_review"],
        "NC-9-total-retention-as-integrity": lambda: x["everything_retained"] and x["integrity_claimed_from_retention_alone"],
        "NC-10-stigmergic-trace-as-neutral": lambda: x["shared_trace_coordinates"] and x["outer_purpose_assumed_legitimate"],
        "NC-11-cross-loop-transformation-concealment": lambda: x["summary_transferred"] and x["presented_as_untransformed_source"],
        "NC-12-model-continuity-inflation": lambda: x["memory_envelope_limited"] and x["model_claims_relationship_beyond_envelope"]
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
        "semantic_trail_witness_valid": True,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
