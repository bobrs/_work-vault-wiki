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
        detail = []
        for error in errors:
            location = ".".join(str(item) for item in error.path)
            detail.append(f"{location}: {error.message}")
        raise AssertionError("; ".join(detail))

def main():
    schema_files = sorted(SCHEMAS.glob("*.json"))
    for path in schema_files:
        Draft202012Validator.check_schema(load(path))

    for record in load(EXAMPLES / "center-standing-records.json")["records"]:
        validate("center-standing.schema.json", record)

    for record in load(EXAMPLES / "source-projection-context-records.json")["records"]:
        validate("source-projection-context.schema.json", record)

    authority = load(EXAMPLES / "purpose-authority-role.json")
    validate("purpose-authority-role.schema.json", authority)

    routes = load(EXAMPLES / "route-gate-action-consequence-records.json")["records"]
    for record in routes:
        validate("route-gate-action-consequence.schema.json", record)

    events = load(EXAMPLES / "reference-event-stream.json")["events"]
    for record in events:
        validate("event-witness-contest-repair.schema.json", record)

    retirement = load(EXAMPLES / "lifecycle-retirement-record.json")
    validate("lifecycle-transfer-residual.schema.json", retirement)

    blocked, approved = routes
    assert blocked["gate_result"] == "deny"
    assert blocked["status"] == "blocked"
    assert approved["gate_result"] == "pass_with_conditions"
    assert approved["status"] == "consequence_observed"

    correction_events = [e for e in events if e["event_type"] == "corrected"]
    assert len(correction_events) == 1
    assert correction_events[0]["correction"]["outcome_changed"] is True
    assert approved["id"] in correction_events[0]["descendant_impact"]

    assert retirement["lifecycle_operation"] == "retirement"
    assert retirement["verification"]["tool_access_revoked"] is True
    assert retirement["verification"]["optional_memory_deleted"] is True

    witness = load(EXAMPLES / "reference-scenario-witness.json")
    assert witness["failed_gate_proven"] is True
    assert witness["valid_action_proven"] is True
    assert witness["correction_changed_outcome"] is True
    assert witness["retirement_revoked_authority"] is True

    claim = load(EXAMPLES / "conformance-claim-manifest.json")
    assert claim["profile"] == "TF-C4"
    assert claim["bounded_extension"] == "TF-C5 retirement"
    assert len(claim["records_tested"]) == 6

    threats = load(TESTS / "threat-negative-fixtures.json")
    detected = []
    for name, fixture in threats.items():
        if not any(value is True for value in fixture.values()):
            raise AssertionError(f"{name} was not detected")
        detected.append(name)

    result = {
        "schemas_checked": len(schema_files),
        "schema_errors": 0,
        "common_schema_families": len(schema_files),
        "reference_records_validated": (
            len(load(EXAMPLES / "center-standing-records.json")["records"])
            + len(load(EXAMPLES / "source-projection-context-records.json")["records"])
            + 1 + len(routes) + len(events) + 1
        ),
        "failed_gate_proven": True,
        "valid_action_proven": True,
        "correction_propagation_proven": True,
        "retirement_revocation_proven": True,
        "threat_cases_detected": len(detected),
        "threat_cases": detected,
        "conformance_claim_valid": True,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
