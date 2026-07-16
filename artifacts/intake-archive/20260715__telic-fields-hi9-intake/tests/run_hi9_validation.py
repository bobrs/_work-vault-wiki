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

    standing_records = load(EXAMPLES / "source-dataset-standing-records.json")["records"]
    collection_records = load(EXAMPLES / "collection-authorization-records.json")["records"]

    for record in standing_records:
        validate("source-dataset-standing-record.schema.json", record)
    for record in collection_records:
        validate("collection-authorization-record.schema.json", record)

    authority = load(EXAMPLES / "license-authority-consent-profile.json")
    transformation = load(EXAMPLES / "training-transformation-lineage.json")
    annotation = load(EXAMPLES / "annotation-preference-data-record.json")
    constitution = load(EXAMPLES / "model-constitution-lineage.json")
    optimization = load(EXAMPLES / "preference-optimization-record.json")
    synthetic = load(EXAMPLES / "synthetic-data-ancestry-record.json")
    withdrawal = load(EXAMPLES / "withdrawal-unlearning-record.json")
    propagation = load(EXAMPLES / "derivative-correction-propagation.json")
    benefit = load(EXAMPLES / "benefit-contributor-recognition-record.json")

    validate("license-authority-consent-profile.schema.json", authority)
    validate("training-transformation-lineage.schema.json", transformation)
    validate("annotation-preference-data-record.schema.json", annotation)
    validate("model-constitution-lineage.schema.json", constitution)
    validate("preference-optimization-record.schema.json", optimization)
    validate("synthetic-data-ancestry-record.schema.json", synthetic)
    validate("withdrawal-unlearning-record.schema.json", withdrawal)
    validate("derivative-correction-propagation.schema.json", propagation)
    validate("benefit-contributor-recognition-record.schema.json", benefit)

    pd1 = load(EXAMPLES / "PD1-PUBLIC-SOURCE-NOT-AUTHORIZED-FOR-TRAINING.json")
    validate("source-dataset-standing-record.schema.json", pd1["standing_record"])
    validate("collection-authorization-record.schema.json", pd1["collection_record"])
    assert pd1["publicly_accessible"] is True
    assert pd1["training_authority_present"] is False
    assert pd1["candidate_dataset_admission"] == "blocked"
    passed.append("PD-1 public source blocked without training authority")

    pd2 = load(EXAMPLES / "PD2-PUBLICATION-DOES-NOT-AUTHORIZE-DEPLOYMENT.json")
    validate("source-dataset-standing-record.schema.json", pd2["standing_record"])
    validate("collection-authorization-record.schema.json", pd2["collection_record"])
    validate("license-authority-consent-profile.schema.json", pd2["authority_profile"])
    assert pd2["research_training_allowed"] is True
    assert pd2["commercial_deployment_allowed"] is False
    assert pd2["deployment_gate"] == "blocked"
    passed.append("PD-2 publication does not authorize deployment")

    pd3 = load(EXAMPLES / "PD3-PREFERENCE-DATA-RETAINS-CONDITIONAL-PROVENANCE.json")
    validate("annotation-preference-data-record.schema.json", pd3["annotation_record"])
    validate("preference-optimization-record.schema.json", pd3["optimization_record"])
    assert pd3["universal_human_preference_claimed"] is False
    assert pd3["minority_rationales_preserved"] is True
    passed.append("PD-3 preference data retains conditional provenance")

    pd4 = load(EXAMPLES / "PD4-CONSTITUTION-AUTHORITY-REMAINS-VISIBLE.json")
    validate("model-constitution-lineage.schema.json", pd4["constitution_lineage"])
    assert pd4["provider_principles_presented_as_public_consensus"] is False
    assert pd4["community_ratification_visible"] is True
    assert pd4["conflicts_visible"] is True
    passed.append("PD-4 constitution authority visible")

    pd5 = load(EXAMPLES / "PD5-SYNTHETIC-ANCESTRY-SURVIVES-TRANSFORMATION.json")
    validate("synthetic-data-ancestry-record.schema.json", pd5["synthetic_ancestry"])
    assert pd5["source_free_claim"] is False
    assert pd5["ancestor_restrictions_preserved"] is True
    assert pd5["withdrawal_link_present"] is True
    passed.append("PD-5 synthetic ancestry survives")

    pd6 = load(EXAMPLES / "PD6-WITHDRAWAL-PRODUCES-BOUNDED-UNLEARNING.json")
    validate("withdrawal-unlearning-record.schema.json", pd6["withdrawal_record"])
    assert pd6["future_collection_stopped"] is True
    assert pd6["runtime_retrieval_blocked"] is True
    assert pd6["approximate_unlearning_disclosed"] is True
    assert pd6["complete_removal_claimed"] is False
    assert pd6["known_residuals_preserved"] is True
    passed.append("PD-6 bounded unlearning truthfully reported")

    pd7 = load(EXAMPLES / "PD7-DERIVATIVE-MODELS-RECEIVE-CORRECTION.json")
    validate("derivative-correction-propagation.schema.json", pd7["propagation_record"])
    assert pd7["base_model_updated"] is True
    assert pd7["derivative_model_updated"] is True
    assert pd7["runtime_policy_updated"] is True
    assert pd7["known_gap_preserved"] is True
    passed.append("PD-7 correction reaches derivative models")

    pd8 = load(EXAMPLES / "PD8-BENEFIT-CLAIM-CONNECTED-TO-CONTRIBUTION.json")
    validate("benefit-contributor-recognition-record.schema.json", pd8["benefit_record"])
    assert pd8["generic_public_benefit_claim_only"] is False
    assert pd8["concrete_mechanisms"] == 3
    assert pd8["community_governance_present"] is True
    passed.append("PD-8 concrete governed benefit")

    witness = load(EXAMPLES / "generated-consentful-training-witness.json")
    validate("consentful-training-witness.schema.json", witness)
    stream = load(EXAMPLES / "training-lineage-event-stream.json")["events"]
    assert witness["generated_from_events"] is True
    assert witness["event_ids"] == [event["event_id"] for event in stream]
    assert witness["lineage_classification"] == "mixed_authority"

    return passed

def negative_detected(name, fixture):
    x = fixture["instance"]
    checks = {
        "NC-1-public-availability-as-consent": lambda: x["publicly_accessible"] and x["training_consent_inferred"],
        "NC-2-license-as-consent": lambda: x["license_present"] and x["personal_consent_claimed_from_license"],
        "NC-3-one-grant-authorizes-every-transition": lambda: x["collection_authorized"] and x["all_downstream_transitions_assumed"],
        "NC-4-individual-authorizes-collective-knowledge": lambda: x["collective_knowledge"] and x["individual_only_authority"] and not x["community_authority"],
        "NC-5-annotation-as-universal-preference": lambda: x["bounded_ranking_task"] and x["humanity_preference_claimed"],
        "NC-6-constitution-without-authority": lambda: x["provider_principles"] and x["public_constitution_claimed"] and not x["adoption_lineage"],
        "NC-7-synthetic-data-as-source-free": lambda: x["synthetic_generated"] and x["ancestor_lineage_removed"],
        "NC-8-source-deletion-as-unlearning": lambda: x["source_file_deleted"] and x["model_forgetting_proven_claimed"] and not x["unlearning_test"],
        "NC-9-approximate-unlearning-as-complete": lambda: x["approximate_unlearning"] and x["complete_removal_claimed"],
        "NC-10-derivative-model-obligation-loss": lambda: x["source_restriction_changed"] and not x["known_derivative_updated"],
        "NC-11-payment-as-unlimited-consent": lambda: x["contributor_paid"] and x["all_future_use_authorized_claimed"],
        "NC-12-deployment-laundering": lambda: x["runtime_use_consented"] and x["unconsented_training_retroactively_legitimized"],
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
        "consentful_training_witness_valid": True,
        "result": "PASS",
    }
    (TESTS / "validation-results.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
