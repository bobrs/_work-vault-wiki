# Withdrawal and Unlearning Evidence Matrix

Status: research artifact  
Content canon status: unset

| State | What has changed | What must not be claimed |
|---|---|---|
| Collection stopped | No new source collection | Existing copies or model influence are gone |
| Source copy deleted | A stored source record was removed | Training influence was removed |
| Future training blocked | Future pipelines exclude the source | Existing models forgot it |
| Runtime retrieval blocked | The source will not be retrieved for current use | Parametric influence is absent |
| Output suppressed | Specified outputs are filtered or refused | Knowledge or influence was removed |
| Approximate unlearning applied | A removal method changed the model | Exact equivalence to retraining |
| Behavioral tests passed | Target outputs or probes no longer recover content under tested conditions | No other access path remains |
| Privacy tests passed | Leakage was reduced under a declared adversary and benchmark | Privacy risk is zero |
| Retrained without source | A new model was trained without the designated source set | Every derivative and prior copy is gone |
| Model retired | An operated model was withdrawn | The model, weights, copies, and downstream effects are dissolved |
| Residual unknown | Influence cannot be established confidently | Deletion or forgetting is complete |

## Required unlearning report

```yaml
request_scope:
source_identifiers:
affected_models:
administrative_actions:
unlearning_method:
comparison_baseline:
behavioral_tests:
privacy_tests:
retained_utility:
sequential_request_tests:
adversary_model:
known_residuals:
downstream_models:
verification_authority:
status:
```

## Governing formulation

> Withdrawal is a governance right. Complete model unlearning is a technical claim whose scope must be proven rather than presumed.
