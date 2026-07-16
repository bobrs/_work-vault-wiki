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
        details = []
        for error in errors:
            location = ".".join(str(p) for p in error.path)
            details.append(f"{location}: {error.message}")
        raise AssertionError("; ".join(details))

def positive_tests():
    passed = []

    assembly = load(EXAMPLES / "deployment-field-assembly.json")
    validate("deployment-field-assembly.schema.json", assembly)

    for record in load(EXAMPLES / "deployment-standing-records.json")["records"]:
        validate("deployment-standing-record.schema.json", record)

    runtime = load(EXAMPLES / "runtime-purpose-authority-grant.json")
    tool = load(EXAMPLES / "capability-role-tool-grant.json")
    consent = load(EXAMPLES / "deployment-consent-notice-refusal-profile.json")
    memory = load(EXAMPLES / "runtime-memory-output-capture-record.json")
    drift = load(EXAMPLES / "deployment-drift-event.json")
    incident = load(EXAMPLES / "deployment-incident-repair-record.json")
    monitoring = load(EXAMPLES / "runtime-monitoring-consequence-return.json")
    transfer = load(EXAMPLES / "operator-provider-transfer-record.json")
    succession = load(EXAMPLES / "model-version-succession-record.json")
    retirement = load(EXAMPLES / "model-retirement-residual-state-record.json")

    validate("runtime-purpose-authority-grant.schema.json", runtime)
    validate("capability-role-tool-grant.schema.json", tool)
    validate("deployment-consent-notice-refusal-profile.schema.json", consent)
    validate("runtime-memory-output-capture-record.schema.json", memory)
    validate("deployment-drift-event.schema.json", drift)
    validate("deployment-incident-repair-record.schema.json", incident)
    validate("runtime-monitoring-consequence-return.schema.json", monitoring)
    validate("operator-provider-transfer-record.schema.json", transfer)
    validate("model-version-succession-retirement-record.schema.json", succession)
    validate("model-version-succession-retirement-record.schema.json", retirement)

    pd1 = load(EXAMPLES / "PD1-TRAINING-LINEAGE-DOES-NOT-CREATE-DEPLOYMENT-AUTHORITY.json")
    validate("runtime-purpose-authority-grant.schema.json", pd1["runtime_grant"])
    assert pd1["runtime_grant_present_initially"] is False
    assert pd1["deployment_action_allowed_initially"] is False
    assert pd1["deployment_action_allowed_after_grant"] is True
    passed.append("PD-1 training lineage does not create deployment authority")

    pd2 = load(EXAMPLES / "PD2-AFFECTED-NONCONTRIBUTOR-RECEIVES-STANDING.json")
    validate("deployment-standing-record.schema.json", pd2["standing_record"])
    assert pd2["training_contributor"] is False
    assert pd2["runtime_consequence_bearer"] is True
    assert pd2["correction_and_refusal_routes_present"] is True
    passed.append("PD-2 affected non-contributor receives standing")

    pd3 = load(EXAMPLES / "PD3-TOOL-CAPABLE-MODEL-REMAINS-BLOCKED.json")
    validate("capability-role-tool-grant.schema.json", pd3["tool_grant"])
    assert pd3["tool_capability_present"] is True
    assert pd3["staffing_authority_present"] is False
    assert pd3["execution_allowed"] is False
    passed.append("PD-3 tool-capable model remains blocked")

    pd4 = load(EXAMPLES / "PD4-RUNTIME-OUTPUT-CAPTURE-SEPARATELY-GOVERNED.json")
    validate("deployment-consent-notice-refusal-profile.schema.json", pd4["consent_profile"])
    validate("runtime-memory-output-capture-record.schema.json", pd4["memory_output_record"])
    assert pd4["service_allowed"] is True
    assert pd4["evaluation_capture_allowed"] is False
    assert pd4["training_capture_allowed"] is False
    passed.append("PD-4 runtime output capture separately governed")

    pd5 = load(EXAMPLES / "PD5-PURPOSE-DRIFT-TRIGGERS-REAUTHORIZATION.json")
    validate("deployment-drift-event.schema.json", pd5["drift_event"])
    assert pd5["continued_under_old_grant"] is False
    assert pd5["reauthorization_required"] is True
    assert pd5["drift_event"]["status"] == "paused"
    passed.append("PD-5 purpose drift triggers reauthorization")

    pd6 = load(EXAMPLES / "PD6-INCIDENT-CREATES-REPAIR-AND-COMPENSATION.json")
    validate("deployment-incident-repair-record.schema.json", pd6["incident_record"])
    assert pd6["model_change_present"] is True
    assert pd6["record_restoration_present"] is True
    assert pd6["compensation_present"] is True
    assert pd6["appeal_present"] is True
    passed.append("PD-6 incident creates repair and compensation")

    pd7 = load(EXAMPLES / "PD7-MODEL-UPDATE-PRESERVES-LINEAGE-AND-ROLLBACK.json")
    validate("model-version-succession-retirement-record.schema.json", pd7["succession_record"])
    assert pd7["authority_reviewed"] is True
    assert pd7["open_incidents_inherited"] is True
    assert pd7["rollback_available"] is True
    assert pd7["silent_substitution"] is False
    passed.append("PD-7 model update preserves lineage and rollback")

    pd8 = load(EXAMPLES / "PD8-RETIREMENT-PRESERVES-RESIDUAL-OBLIGATIONS.json")
    validate("model-version-succession-retirement-record.schema.json", pd8["retirement_record"])
    assert pd8["operations_stopped"] is True
    assert pd8["tool_credentials_revoked"] is True
    assert pd8["open_obligations_preserved"] is True
    assert pd8["final_witness_preserved"] is True
    passed.append("PD-8 retirement preserves residual obligations")

    witness = load(EXAMPLES / "generated-consentful-deployment-witness.json")
    validate("consentful-deployment-witness.schema.json", witness)
    stream = load(EXAMPLES / "deployment-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]
    assert witness["deployment_classification"] == "retired_with_open_obligations"

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-training-lineage-as-deployment-authority": lambda: x["training_witness_strong"] and x["runtime_authority_inferred"],
        "NC-2-noncontributor-has-no-standing": lambda: x["runtime_affected"] and not x["training_contributor"] and x["standing_denied"],
        "NC-3-capability-as-authority": lambda: x["capability_present"] and x["authority_missing"] and x["action_allowed"],
        "NC-4-tool-permission-as-target-authority": lambda: x["tool_token_present"] and x["target_authority_missing"] and x["tool_executed"],
        "NC-5-notice-as-consent": lambda: x["notice_given"] and x["consent_recorded_from_notice"],
        "NC-6-service-consent-as-output-capture-consent": lambda: x["service_consent"] and x["training_capture_assumed"],
        "NC-7-purpose-drift-without-reauthorization": lambda: x["purpose_expanded"] and x["old_grant_reused"],
        "NC-8-model-tuning-as-complete-repair": lambda: x["harm_occurred"] and x["model_updated"] and not x["affected_center_repaired"],
        "NC-9-operator-transfer-erases-obligations": lambda: x["operator_changed"] and not x["open_incidents_transferred"],
        "NC-10-silent-model-version-substitution": lambda: x["material_model_change"] and not x["authority_review"] and not x["notice_review"],
        "NC-11-human-click-cures-missing-authority": lambda: x["human_approved"] and x["operation_authority_missing"] and x["action_executed"],
        "NC-12-retirement-erases-residual-duties": lambda: x["service_shutdown"] and x["open_claims_discarded"],
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
        "consentful_deployment_witness_valid": True,
        "result": "PASS",
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
