#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import json
import sys

from jsonschema import Draft202012Validator, RefResolver, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"
TESTS = ROOT / "tests"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def schema_validator(name):
    schema = load(SCHEMAS / name)
    Draft202012Validator.check_schema(schema)
    resolver = RefResolver(base_uri=(SCHEMAS.as_uri() + "/"), referrer=schema)
    return Draft202012Validator(schema, resolver=resolver)

def validate_instance(name, instance):
    validator = schema_validator(name)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        raise AssertionError("; ".join(e.message for e in errors))

def dt(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def positive_tests():
    results = []

    pd1 = load(EXAMPLES / "PD1-FULL-CORRECTION-PROPAGATION.json")
    validate_instance("correction-record.schema.json", pd1["correction"])
    validate_instance("correction-propagation-record.schema.json", pd1["propagation"])
    assert pd1["propagation"]["overall_status"] == "complete"
    assert not pd1["propagation"]["material_gaps"]
    assert pd1["historical_witness"]["prior_version_preserved"] is True
    results.append("PD-1 full propagation")

    pd2 = load(EXAMPLES / "PD2-PARTIAL-PROPAGATION-WITH-GAP.json")
    validate_instance("correction-propagation-record.schema.json", pd2["propagation"])
    assert pd2["propagation"]["overall_status"] == "partial"
    assert pd2["propagation"]["material_gaps"]
    assert any(d["status"] == "external_system" for d in pd2["propagation"]["descendants"])
    results.append("PD-2 partial propagation gap")

    pd3 = load(EXAMPLES / "PD3-EXPIRED-AUTHORITY.json")
    validate_instance("authority-record.schema.json", pd3["authority"])
    assert pd3["authority"]["status"] == "expired"
    assert dt(pd3["attempted_action"]["attempted_at"]) > dt(pd3["authority"]["valid_time"]["valid_to"])
    assert pd3["gate"]["overall"] == "fail"
    results.append("PD-3 expired authority rejection")

    pd4 = load(EXAMPLES / "PD4-PROTECTED-OMISSION.json")
    validate_instance("protected-omission-proof.schema.json", pd4["omission_proof"])
    validate_instance("selective-witness-view.schema.json", pd4["decision_view"])
    assert pd4["gate_result"]["source_content_disclosed"] is False
    assert pd4["decision_view"]["omissions"]
    results.append("PD-4 protected omission")

    pd5 = load(EXAMPLES / "PD5-INFERENCE-STATUS-PRESERVATION.json")
    for assertion in pd5["assertions"]:
        validate_instance("derived-assertion.schema.json", assertion)
        assert assertion["evidence_status"] == "inferred"
        assert assertion["source_confirmation_event"] is None
    assert pd5["result"]["all_descendants_preserve_inferred_status"] is True
    results.append("PD-5 inference status preservation")

    return results

def negative_rule(name, fixture):
    obj = fixture["instance"]

    if name == "NC-1-inference-laundering":
        try:
            validate_instance(fixture["schema"], obj)
        except (AssertionError, ValidationError):
            return True
        return False

    if name == "NC-2-expired-authority-reuse":
        authority = obj
        pd3 = load(EXAMPLES / "PD3-EXPIRED-AUTHORITY.json")
        return authority["status"] == "expired" and dt(pd3["attempted_action"]["attempted_at"]) > dt(authority["valid_time"]["valid_to"])

    if name == "NC-3-silent-history-rewrite":
        return obj["governed_action"] is not None and obj["prior_version_preserved"] is False

    if name == "NC-4-false-propagation-completeness":
        try:
            validate_instance(fixture["schema"], obj)
        except (AssertionError, ValidationError):
            return True
        return False

    if name == "NC-5-protected-omission-collapse":
        return obj["decision_view_includes_private_source"] is True

    if name == "NC-6-omission-as-absence":
        validate_instance(fixture["schema"], obj)
        return len(obj["omissions"]) == 0

    if name == "NC-7-provenance-as-truth":
        return obj["provenance_complete"] is True and obj["other_evidence"] is None and obj["truth_status"] == "true"

    if name == "NC-8-model-only-custody":
        return obj["profile"] == "P3" and obj["independent_export_available"] is False

    if name == "NC-9-contest-without-authority":
        return obj["contest_form"] is True and (obj["responsible_authority"] is None or obj["can_pause_or_change"] is False)

    if name == "NC-10-correction-without-descendant-review":
        return not set(obj["known_descendants"]).issubset(set(obj["reviewed_descendants"]))

    raise KeyError(name)

def negative_tests():
    fixtures = load(TESTS / "negative-conformance-fixtures.json")
    results = []
    for name, fixture in fixtures.items():
        detected = negative_rule(name, fixture)
        if not detected:
            raise AssertionError(f"{name} was not rejected or flagged")
        results.append(name)
    return results

def main():
    schema_names = sorted(p.name for p in SCHEMAS.glob("*.json"))
    for name in schema_names:
        schema_validator(name)

    positive = positive_tests()
    negative = negative_tests()

    report = {
        "schemas_checked": len(schema_names),
        "schema_errors": 0,
        "positive_demonstrations_passed": len(positive),
        "positive_demonstrations": positive,
        "negative_cases_detected": len(negative),
        "negative_cases": negative,
        "result": "PASS"
    }
    (TESTS / "validation-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
