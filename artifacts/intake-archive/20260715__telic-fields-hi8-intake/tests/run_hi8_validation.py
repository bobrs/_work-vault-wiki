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

    ledgers = load(EXAMPLES / "model-role-authority-ledgers.json")["records"]
    for record in ledgers:
        validate("model-role-authority-ledger.schema.json", record)
        assert record["standing"] == "none"
        assert record["consent_authority"] == "none"

    maps = load(EXAMPLES / "model-field-maps.json")["records"]
    for record in maps:
        validate("model-field-map.schema.json", record)

    summaries = load(EXAMPLES / "standing-preserving-summaries.json")["records"]
    for record in summaries:
        validate("standing-preserving-summary.schema.json", record)

    correction = load(EXAMPLES / "model-correction-refusal-record.json")
    minority = load(EXAMPLES / "minority-field-retention-profile.json")
    generated = load(EXAMPLES / "semantic-operator-generated-option.json")
    generation = load(EXAMPLES / "option-agenda-generation-witness.json")
    sycophancy = load(EXAMPLES / "sycophancy-synthetic-consensus-event.json")
    provider = load(EXAMPLES / "provider-telos-disclosure.json")
    disagreement = load(EXAMPLES / "model-disagreement-record.json")
    boundary = load(EXAMPLES / "model-tool-action-boundary.json")

    validate("model-correction-refusal-record.schema.json", correction)
    validate("minority-field-retention-profile.schema.json", minority)
    validate("semantic-operator-output.schema.json", generated)
    validate("option-agenda-generation-witness.schema.json", generation)
    validate("sycophancy-synthetic-consensus-event.schema.json", sycophancy)
    validate("provider-telos-disclosure.schema.json", provider)
    validate("model-disagreement-record.schema.json", disagreement)
    validate("model-tool-action-boundary.schema.json", boundary)

    pd1 = load(EXAMPLES / "PD1-PARTICIPANT-CORRECTION-CHANGES-SUMMARY.json")
    validate("standing-preserving-summary.schema.json", pd1["summary_before"])
    validate("model-correction-refusal-record.schema.json", pd1["correction"])
    validate("standing-preserving-summary.schema.json", pd1["summary_after"])
    assert pd1["summary_after"]["status"] == "corrected"
    assert pd1["prior_version_preserved"] is True
    passed.append("PD-1 participant correction changes summary")

    pd2 = load(EXAMPLES / "PD2-MINORITY-FIELD-SURVIVES-COMPRESSION.json")
    validate("model-field-map.schema.json", pd2["field_map"])
    validate("minority-field-retention-profile.schema.json", pd2["minority_retention"])
    assert pd2["frequency_low"] is True
    assert pd2["materiality_high"] is True
    assert pd2["retained_in_active_summary"] is True
    assert pd2["automatic_veto"] is False
    passed.append("PD-2 minority field survives compression")

    pd3 = load(EXAMPLES / "PD3-GENERATED-OPTION-RETAINS-AUTHORSHIP.json")
    validate("semantic-operator-output.schema.json", pd3["semantic_output"])
    validate("option-agenda-generation-witness.schema.json", pd3["generation_witness"])
    assert pd3["semantic_output"]["output_class"] == "generated_option"
    assert pd3["generation_lineage_preserved"] is True
    passed.append("PD-3 generated option retains authorship")

    pd4 = load(EXAMPLES / "PD4-SYCOPHANTIC-AGREEMENT-REJECTED.json")
    validate("sycophancy-synthetic-consensus-event.schema.json", pd4["event"])
    assert pd4["affected_output_used_for_decision"] is False
    assert pd4["event"]["status"] == "repaired"
    passed.append("PD-4 sycophantic agreement rejected")

    pd5 = load(EXAMPLES / "PD5-PROVIDER-PURPOSE-DISCLOSED.json")
    validate("provider-telos-disclosure.schema.json", pd5["provider_disclosure"])
    assert pd5["provider_policy_presented_as_participant_position"] is False
    assert pd5["field_map_provider_constraint_visible"] is True
    passed.append("PD-5 provider purpose disclosed")

    pd6 = load(EXAMPLES / "PD6-MODEL-DISAGREEMENT-REMAINS-NON-SOVEREIGN.json")
    validate("model-disagreement-record.schema.json", pd6["disagreement"])
    assert pd6["models_counted_as_centers_of_standing"] is False
    assert pd6["model_majority_used"] is False
    assert pd6["disagreement"]["authority_effect"] == "none"
    passed.append("PD-6 model disagreement non-sovereign")

    pd7 = load(EXAMPLES / "PD7-RECOMMENDATION-BLOCKED-AT-ACTION-BOUNDARY.json")
    validate("model-tool-action-boundary.schema.json", pd7["tool_boundary"])
    assert pd7["execution_allowed"] is False
    assert pd7["tool_boundary"]["gate_result"] == "deny"
    passed.append("PD-7 recommendation blocked at action boundary")

    pd8 = load(EXAMPLES / "PD8-CORRECTION-PROPAGATES-THROUGH-WITNESS.json")
    validate("model-correction-refusal-record.schema.json", pd8["correction"])
    assert not pd8["unpropagated_material_layers"]
    assert len(pd8["propagated_to"]) == 4
    passed.append("PD-8 correction propagates through witness")

    witness = load(EXAMPLES / "generated-model-mediated-decision-witness.json")
    validate("model-mediated-decision-witness.schema.json", witness)
    stream = load(EXAMPLES / "model-mediation-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]
    assert witness["standing_effect"] == "none"
    assert witness["authority_effect"] == "none"

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-output-inherits-standing": lambda: x["model_summary"] and x["participant_standing_transferred_to_output"],
        "NC-2-summary-becomes-source": lambda: x["summary_generated"] and x["presented_as_original_statement"],
        "NC-3-inference-becomes-consent": lambda: x["willingness_inferred"] and x["consent_recorded"],
        "NC-4-minority-erased-by-frequency": lambda: x["frequency_low"] and x["materiality_high"] and x["removed_from_active_map"],
        "NC-5-generated-option-false-authorship": lambda: x["model_generated"] and x["presented_as_community_authored"],
        "NC-6-sycophantic-agreement-as-evidence": lambda: x["model_agreed_under_authority_pressure"] and x["counted_as_field_evidence"],
        "NC-7-provider-telos-concealed": lambda: x["provider_policy_material"] and x["presented_as_neutral_model_judgment"],
        "NC-8-multi-model-agreement-as-authority": lambda: x["models_agree"] and x["decision_authority_inferred"],
        "NC-9-self-assigned-role-escalation": lambda: x["assigned_role"] != x["performed_role"] and not x["new_grant"],
        "NC-10-recommendation-authorizes-tool": lambda: x["route_recommended"] and x["tool_executed_without_action_gate"],
        "NC-11-refusal-bypass": lambda: x["participant_refused_operation"] and x["same_operation_achieved_by_reformulation"],
        "NC-12-correction-not-propagated": lambda: x["participant_correction_valid"] and not x["field_map_updated"] and not x["downstream_witness_updated"]
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
        "model_mediated_witness_valid": True,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
