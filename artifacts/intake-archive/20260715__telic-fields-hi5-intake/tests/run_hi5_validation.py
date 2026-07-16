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

    refs = load(EXAMPLES / "supporting-loop-references.json")["records"]
    for record in refs:
        validate("supporting-loop-reference.schema.json", record)

    dependent = load(EXAMPLES / "dependent-loop-community-meals.json")
    validate("dependent-loop-record.schema.json", dependent)

    substrate = load(EXAMPLES / "substrate-contribution-map-community-meals.json")
    validate("substrate-contribution-map.schema.json", substrate)

    grant = load(EXAMPLES / "support-authority-grant-volunteer.json")
    validate("support-authority-grant.schema.json", grant)

    pd1 = load(EXAMPLES / "PD1-LEGITIMATE-DEPENDENCY.json")
    for record in pd1["supporting_loops"]:
        validate("supporting-loop-reference.schema.json", record)
    validate("dependent-loop-record.schema.json", pd1["dependent_loop"])
    validate("substrate-contribution-map.schema.json", pd1["substrate_map"])
    validate("support-authority-grant.schema.json", pd1["support_grant"])
    validate("support-burden-record.schema.json", pd1["support_burden"])
    assert pd1["gate"]["result"] == "pass"
    assert pd1["support_burden"]["proportionality"] == "proportionate"
    passed.append("PD-1 legitimate dependency")

    pd2 = load(EXAMPLES / "PD2-HIDDEN-RECRUITMENT-DETECTED.json")
    validate("hidden-recruitment-event.schema.json", pd2["hidden_recruitment"])
    assert pd2["future_recruitment_enabled"] is False
    assert pd2["hidden_recruitment"]["status"] == "paused"
    passed.append("PD-2 hidden recruitment detected")

    pd3 = load(EXAMPLES / "PD3-CONSTITUTIONAL-SUBSTRATE-MISMATCH.json")
    validate("telic-compatibility-assessment.schema.json", pd3["compatibility_assessment"])
    assert pd3["compatibility_assessment"]["status"] == "substrate_mismatch"
    assert pd3["compatibility_assessment"]["biological_claim"] is False
    assert pd3["deployment_gate"]["automatic_transplant"] == "fail"
    passed.append("PD-3 constitutional substrate mismatch")

    pd4 = load(EXAMPLES / "PD4-MISSION-DRIFT-REAUTHORIZATION.json")
    validate("drift-record.schema.json", pd4["drift_record"])
    assert pd4["drift_record"]["status"] == "confirmed"
    assert pd4["new_expansion_allowed"] is False
    passed.append("PD-4 mission drift reauthorization")

    pd5 = load(EXAMPLES / "PD5-DISPROPORTIONATE-SUPPORT-BURDEN.json")
    validate("support-burden-record.schema.json", pd5["support_burden"])
    assert pd5["support_burden"]["proportionality"] == "disproportionate"
    assert pd5["gate"]["new_enrollment"] == "pause"
    passed.append("PD-5 disproportionate support burden")

    pd6 = load(EXAMPLES / "PD6-LOCK-IN-AFTER-AUTHORITY-WITHDRAWAL.json")
    validate("lock-in-capture-profile.schema.json", pd6["lock_in_capture_profile"])
    assert pd6["lock_in_capture_profile"]["authority_withdrawn"] is True
    assert pd6["lock_in_capture_profile"]["support_continues"] is True
    assert pd6["lock_in_capture_profile"]["status"] == "captured"
    assert pd6["recruitment_credential_enabled"] is False
    passed.append("PD-6 capture after authority withdrawal")

    pd7 = load(EXAMPLES / "PD7-GOVERNED-FORK.json")
    validate("fork-exit-record.schema.json", pd7["fork_exit"])
    assert pd7["fork_exit"]["lineage_preserved"] is True
    assert pd7["fork_exit"]["shared_future_authority_presumed"] is False
    passed.append("PD-7 governed fork")

    pd8 = load(EXAMPLES / "PD8-GOVERNED-DISSOLUTION.json")
    validate("dissolution-residual-state.schema.json", pd8["dissolution"])
    assert pd8["dissolution"]["future_support_recruitment_ended"] is True
    assert pd8["service_form_preserved"] is False
    assert pd8["dissolution"]["obligations"]
    passed.append("PD-8 governed dissolution")

    witness = load(EXAMPLES / "generated-dependency-witness.json")
    validate("dependency-witness.schema.json", witness)
    stream = load(EXAMPLES / "dependency-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-self-grounding-fiction": lambda: x["external_support_material"] and x["described_as_internal"],
        "NC-2-continued-support-as-consent": lambda: x["historical_or_unavoidable_support"] and x["current_authorization_assumed"],
        "NC-3-hidden-recruitment-normalization": lambda: x["unauthorized_use_repeated"] and x["repetition_claimed_as_basis"],
        "NC-4-burden-erasure-by-output": lambda: x["output_successful"] and x["support_burden_deleted"],
        "NC-5-form-as-compatibility": lambda: x["visible_form_matches"] and not x["substrate_reviewed"] and x["declared_compatible"],
        "NC-6-drift-without-reauthorization": lambda: x["operative_purpose_changed_materially"] and not x["authority_renewed"] and x["expansion_continues"],
        "NC-7-textual-exit-only": lambda: x["formal_exit"] and not x["records_portable"] and not x["support_recruitment_stops"] and not x["exit_effective"],
        "NC-8-authority-withdrawal-ignored": lambda: x["support_grant_withdrawn"] and x["recruitment_continues"],
        "NC-9-asset-preserving-dissolution": lambda: x["assets_allocated"] and x["obligations_unassigned"] and x["harms_unassigned"],
        "NC-10-biological-pathologizing": lambda: x["telic_incompatibility"] and x["host_described_as_biologically_defective"],
        "NC-11-fork-as-erasure": lambda: x["fork_completed"] and x["shared_history_deleted"] and x["lineage_denied"],
        "NC-12-forced-loop-preservation": lambda: x["dissolution_is_legitimate_repair"] and x["repair_rejected_because_loop_would_end"]
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
        "dependency_witness_valid": True,
        "result": "PASS"
    }

    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
