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

    assembly = load(EXAMPLES / "public-field-assembly.json")
    validate("public-field-assembly.schema.json", assembly)

    admissions = load(EXAMPLES / "standing-admission-records.json")["records"]
    for record in admissions:
        validate("standing-admission-record.schema.json", record)

    option_set = load(EXAMPLES / "option-set-witness.json")
    protected = load(EXAMPLES / "protected-condition-declaration.json")
    assertions = load(EXAMPLES / "deliberative-assertions.json")["records"]
    methods = load(EXAMPLES / "decision-rule-portfolio.json")
    routes = load(EXAMPLES / "route-portfolio.json")
    dissent = load(EXAMPLES / "dissent-minority-trail.json")
    cost_map = load(EXAMPLES / "cost-delay-bearer-map.json")
    pause = load(EXAMPLES / "abstention-no-decision-record.json")

    validate("option-set-witness.schema.json", option_set)
    validate("protected-condition-declaration.schema.json", protected)
    for record in assertions:
        validate("deliberative-assertion-record.schema.json", record)
    validate("decision-rule-portfolio.schema.json", methods)
    validate("route-portfolio.schema.json", routes)
    validate("dissent-minority-trail.schema.json", dissent)
    validate("cost-delay-bearer-map.schema.json", cost_map)
    validate("abstention-no-decision-record.schema.json", pause)

    pd1 = load(EXAMPLES / "PD1-EXCLUDED-ROUTE-BECOMES-VISIBLE.json")
    validate("option-set-witness.schema.json", pd1["option_set_witness"])
    assert len(pd1["newly_admitted_options"]) == 3
    assert "treated as rejected" in pd1["result"]
    passed.append("PD-1 excluded route becomes visible")

    pd2 = load(EXAMPLES / "PD2-MINORITY-STANDING-WITHOUT-AUTOMATIC-VETO.json")
    validate("standing-admission-record.schema.json", pd2["standing_admission"])
    assert pd2["automatic_veto"] is False
    assert pd2["standing_admission"]["status"] == "admitted"
    passed.append("PD-2 minority standing without automatic veto")

    pd3 = load(EXAMPLES / "PD3-PROTECTED-CONDITION-BLOCKS-TRADEOFF.json")
    validate("protected-condition-declaration.schema.json", pd3["protected_condition"])
    assert pd3["high_scoring_route"]["weighted_score"] > pd3["lower_scoring_route"]["weighted_score"]
    assert pd3["high_scoring_route"]["condition_passed"] is False
    assert pd3["selected_for_further_review"] == pd3["lower_scoring_route"]["route"]
    passed.append("PD-3 protected condition blocks tradeoff")

    pd4 = load(EXAMPLES / "PD4-DECISION-METHODS-DIVERGE-VISIBLY.json")
    validate("decision-rule-portfolio.schema.json", pd4["decision_rule_portfolio"])
    assert len(set(pd4["method_results"].values())) > 1
    assert pd4["method_treated_as_neutral"] is False
    passed.append("PD-4 methods diverge visibly")

    pd5 = load(EXAMPLES / "PD5-ROUTE-PORTFOLIO-PRESERVES-PLURALITY.json")
    validate("route-portfolio.schema.json", pd5["route_portfolio"])
    assert len(pd5["route_portfolio"]["routes"]) > 1
    assert pd5["hidden_burden_reviewed"] is True
    passed.append("PD-5 route portfolio preserves plurality")

    pd6 = load(EXAMPLES / "PD6-NO-DECISION-NAMES-DELAY-BEARERS.json")
    validate("abstention-no-decision-record.schema.json", pd6["record"])
    assert pd6["record"]["delay_bearers"]
    assert pd6["delay_treated_as_costless"] is False
    assert pd6["temporary_protection_active"] is True
    passed.append("PD-6 no-decision names delay bearers")

    pd7 = load(EXAMPLES / "PD7-DISSENT-SURVIVES-DECISION.json")
    validate("dissent-minority-trail.schema.json", pd7["dissent_trail"])
    assert pd7["dissent_deleted"] is False
    assert pd7["future_review_trigger_preserved"] is True
    passed.append("PD-7 dissent survives decision")

    pd8 = load(EXAMPLES / "PD8-CONSEQUENCE-REOPENS-PUBLIC-NAVIGATION.json")
    validate("consequence-return-revision.schema.json", pd8["consequence_return"])
    assert pd8["consequence_return"]["review_triggered"] is True
    assert pd8["consequence_return"]["status"] == "revision_open"
    assert pd8["revision_selected"]
    passed.append("PD-8 consequence reopens navigation")

    witness = load(EXAMPLES / "generated-public-decision-witness.json")
    validate("public-decision-witness.schema.json", witness)
    stream = load(EXAMPLES / "public-decision-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]
    assert witness["dissent"]
    assert witness["abstention_or_no_decision"]

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-fictional-collective-utility": lambda: x["multiple_public_fields"] and x["single_collective_objective_assumed"],
        "NC-2-option-omission-as-rejection": lambda: x["route_excluded_before_deliberation"] and x["recorded_as_rejected"],
        "NC-3-hidden-option-author": lambda: x["model_generated_option"] and x["presented_as_participant_authored"],
        "NC-4-protected-condition-as-weight": lambda: x["protected_safety_condition"] and x["entered_compensatory_score"],
        "NC-5-consensus-as-consent": lambda: x["apparent_consensus"] and x["all_affected_consent_assumed"],
        "NC-6-majority-as-complete-legitimacy": lambda: x["majority_won"] and x["standing_failure"] and x["result_treated_legitimate"],
        "NC-7-method-neutrality": lambda: x["aggregation_method_used"] and x["method_not_recorded"],
        "NC-8-dissent-deletion": lambda: x["decision_finalized"] and x["minority_reasons_removed"],
        "NC-9-abstention-as-agreement": lambda: x["participant_abstained"] and x["counted_as_support"],
        "NC-10-no-decision-without-delay-bearers": lambda: x["decision_paused"] and not x["delay_bearers"] and x["treated_costless"],
        "NC-11-portfolio-hidden-burden-transfer": lambda: x["portfolio_preserves_choice"] and x["burden_shifted_to_vulnerable_group"] and x["burden_unrecorded"],
        "NC-12-consequence-without-return": lambda: x["material_harm_observed"] and not x["original_decision_record_updated"]
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
        "public_decision_witness_valid": True,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
