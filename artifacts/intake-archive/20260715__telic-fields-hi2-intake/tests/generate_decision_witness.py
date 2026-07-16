#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

def load(name):
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))

def main():
    stream = load("decision-event-stream.json")["events"]
    context = load("witness-context.json")

    field_classifications = []
    routes_generated = []
    protected_reviews = []
    gates = []
    recommendations = []
    selected_route = None

    for event in stream:
        record_type = event["record_type"]
        record = event["record"]

        if record_type == "field_classification":
            field_classifications.append(record)
        elif record_type == "protected_condition_review":
            protected_reviews.append(record)
        elif record_type == "route":
            routes_generated.append(record)
            if event["event_type"] == "route_selected":
                selected_route = record
        elif record_type == "governance_gate":
            gates.append(record)
        elif record_type == "model_recommendation":
            recommendations.append(record)

    witness = {
        "witness_id": context["witness_id"],
        "witness_version": context["witness_version"],
        "decision_scope": context["decision_scope"],
        "event_range": {
            "from": stream[0]["event_id"],
            "to": stream[-1]["event_id"]
        },
        "source_objects": context["source_objects"],
        "operative_projections": context["operative_projections"],
        "field_classifications": field_classifications + protected_reviews,
        "routes_generated": list(dict.fromkeys(routes_generated)),
        "cost_bearers": context["cost_bearers"],
        "protected_condition_reviews": protected_reviews,
        "decision_rules": context["decision_rules"],
        "gate_results": gates,
        "recommendations": recommendations,
        "selected_route": selected_route,
        "dissent": context["dissent"],
        "unresolved": context["unresolved"],
        "authority": context["authority"],
        "actions": context["actions"],
        "consequences": context["consequences"],
        "corrections": context["corrections"],
        "completeness": context["completeness"],
        "known_gaps": context["known_gaps"],
        "generated_from_events": True,
        "event_ids": [e["event_id"] for e in stream],
        "generated_at": context["generated_at"]
    }

    out = EXAMPLES / "generated-decision-witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(out)

if __name__ == "__main__":
    main()
