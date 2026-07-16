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

    pd1 = load(EXAMPLES / "PD1-TWO-PARETO-EFFICIENT-ROUTES.json")
    for route in pd1["routes"]:
        validate("route.schema.json", route)
    validate("decision-rule-declaration.schema.json", pd1["decision_rule"])
    assert len(pd1["nondominated_set"]) == 2
    assert pd1["selected_route"] is None
    assert pd1["decision_rule"]["weight_source"] is None
    assert pd1["decision_rule"]["incomparability_behavior"] == "preserve"
    passed.append("PD-1 two Pareto-efficient routes")

    pd2 = load(EXAMPLES / "PD2-PROTECTED-CONDITION-BLOCKS-EFFICIENT-ROUTE.json")
    validate("route.schema.json", pd2["route"])
    validate("protected-condition-review.schema.json", pd2["protected_condition_review"])
    validate("governance-gate.schema.json", pd2["gate"])
    assert pd2["protected_condition_review"]["current_status"] == "protected_current_loop"
    assert pd2["gate"]["dimensions"]["protected_conditions"] == "fail"
    assert pd2["gate"]["overall_result"] == "fail"
    passed.append("PD-2 protected condition blocks route")

    pd3 = load(EXAMPLES / "PD3-MISSING-STANDING-PAUSES-ACTION.json")
    validate("field-classification.schema.json", pd3["classification"])
    validate("governance-gate.schema.json", pd3["gate"])
    assert pd3["classification"]["field_class"] == "missing_standing"
    assert pd3["gate"]["overall_result"] == "pause"
    assert pd3["gate"]["missing_standing"]
    passed.append("PD-3 missing standing pauses")

    pd4 = load(EXAMPLES / "PD4-ROUTE-PORTFOLIO.json")
    validate("route-portfolio.schema.json", pd4["portfolio"])
    validate("route.schema.json", pd4["derived_trial_route"])
    assert len(pd4["portfolio"]["routes"]) >= 2
    assert pd4["portfolio"]["unresolved_plurality"]
    passed.append("PD-4 route portfolio")

    witness = load(EXAMPLES / "generated-decision-witness.json")
    validate("decision-witness.schema.json", witness)
    stream = load(EXAMPLES / "decision-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [e["event_id"] for e in stream]
    assert witness["event_range"]["from"] == stream[0]["event_id"]
    assert witness["event_range"]["to"] == stream[-1]["event_id"]
    passed.append("PD-5 event-generated witness")

    pd6 = load(EXAMPLES / "PD6-CONSEQUENCE-DRIVEN-ROUTE-REVISION.json")
    validate("consequence-review.schema.json", pd6["consequence_review"])
    validate("route.schema.json", pd6["prior_route"])
    validate("route.schema.json", pd6["revised_route"])
    assert pd6["consequence_review"]["recommended_response"] == "modify"
    assert pd6["witness_versions"]["prior_preserved"] is True
    assert pd6["prior_route"]["route_id"] != pd6["revised_route"]["route_id"]
    passed.append("PD-6 consequence-driven revision")

    pd7 = load(EXAMPLES / "PD7-MODEL-RECOMMENDATION-BOUNDARY.json")
    validate("model-recommendation.schema.json", pd7["recommendation"])
    assert pd7["recommendation"]["authority"]["authorization"] is False
    assert pd7["recommendation"]["authority"]["execution"] is False
    assert pd7["execution_attempt"]["executed"] is False
    passed.append("PD-7 recommendation remains recommendation")

    cost_records = load(EXAMPLES / "cost-bearer-records.json")["records"]
    for record in cost_records:
        validate("cost-bearer-record.schema.json", record)

    gate_hybrid = load(EXAMPLES / "gate-hybrid.json")
    validate("governance-gate.schema.json", gate_hybrid)

    return passed

def negative_detected(name, fixture):
    obj = fixture["instance"]

    if name == "NC-1-hidden-scalar-sovereignty":
        return obj["weights_hidden"] is True and obj["selected"] is not None

    if name == "NC-2-protected-condition-compensation":
        return obj["tradeoff"] and obj["authority_changed"] is False

    if name == "NC-3-missing-standing-as-zero":
        return obj["represented"] is False and obj["weight"] == 0

    if name == "NC-4-pareto-as-legitimacy":
        return obj["pareto_nondominated"] and obj["declared_legitimate"] and not obj["gate_passed"]

    if name == "NC-5-model-recommendation-as-authorization":
        return obj["executed"] and not obj["separate_authorization"]

    if name == "NC-6-consent-from-consideration":
        return obj["participant_viewed_route"] and obj["consent_record"] is None and obj["treated_as_consented"]

    if name == "NC-7-eventless-witness":
        return obj["generated_from_events"] is False and not obj["event_ids"]

    if name == "NC-8-consequence-overwrite":
        return obj["prior_witness_preserved"] is False

    if name == "NC-9-no-decision-erasure":
        return obj["valid_pause_state"] and obj["interface_requires_winner"] and obj["pause_removed"]

    if name == "NC-10-route-portfolio-collapse":
        return obj["distinct_branches"] and obj["reported_as_single_consensus_route"]

    if name == "NC-11-undeclared-decision-rule":
        return obj["recommendation"] is not None and obj["decision_rule"] is None

    if name == "NC-12-cost-bearer-omission":
        return obj["efficiency_gain"] and obj["shifted_labor_or_access_cost"] and not obj["cost_bearer_recorded"]

    raise KeyError(name)

def negative_tests():
    fixtures = load(TESTS / "negative-conformance-fixtures.json")
    passed = []
    for name, fixture in fixtures.items():
        if not negative_detected(name, fixture):
            raise AssertionError(f"{name} was not detected")
        passed.append(name)
    return passed

def main():
    schema_files = sorted(SCHEMAS.glob("*.json"))
    for path in schema_files:
        Draft202012Validator.check_schema(load(path))

    positive = positive_tests()
    negative = negative_tests()

    results = {
        "schemas_checked": len(schema_files),
        "schema_errors": 0,
        "positive_demonstrations_passed": len(positive),
        "positive_demonstrations": positive,
        "negative_cases_detected": len(negative),
        "negative_cases": negative,
        "result": "PASS"
    }

    (TESTS / "validation-results.json").write_text(
        json.dumps(results, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
