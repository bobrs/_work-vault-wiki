# I.0 Conformance Matrix

Status: candidate pre-production  
Content canon status: unset

| Requirement | P0 Documentary | P1 Source-Aware Navigation | P2 Action-Bearing | P3 Contestable |
|---|---:|---:|---:|---:|
| Source/generated distinction | MUST | MUST | MUST | MUST |
| Record versioning | MUST | MUST | MUST | MUST |
| Correction support | MUST | MUST | MUST | MUST |
| Declared model role | MUST where model participates | MUST | MUST | MUST |
| Center and standing representation | — | MUST | MUST | MUST |
| Telic Projection Record | — | MUST | MUST | MUST |
| Field classes | — | MUST | MUST | MUST |
| Missing-standing and unresolved states | — | MUST | MUST | MUST |
| Route and cost-bearer record | — | MUST | MUST | MUST |
| Governance gates | — | — | MUST | MUST |
| Separate authority operations | — | — | MUST | MUST |
| Consent or other authority basis | — | — | MUST | MUST |
| Model role and credential envelope | — | — | MUST | MUST |
| AuthorizedAction record | — | — | MUST | MUST |
| DecisionWitness | — | — | MUST | MUST |
| Tool scope and confirmation | — | — | MUST where tools exist | MUST where tools exist |
| Contest event | — | — | SHOULD | MUST |
| Outcome-changing recourse | — | — | SHOULD | MUST |
| Correction propagation | SHOULD | SHOULD | MUST or gap recorded | MUST or gap recorded |
| Independent witness export | — | SHOULD | SHOULD | MUST |
| Human re-entry for designated high consequence | — | — | SHOULD | MUST |
| Release and dissolution lifecycle | SHOULD | SHOULD | SHOULD | MUST |
| Privacy and protected omission | SHOULD | MUST | MUST | MUST |

## Profile restrictions

- P0 MUST NOT claim decision-governance conformance.
- P1 MAY recommend but MUST NOT execute consequential action solely under P1.
- P2 MUST identify any domain in which human re-entry is not implemented.
- P3 MUST identify which actions can actually be paused, corrected, reversed, or repaired.

## Conformance statement template

```yaml
implementation:
profile:
schema_version:
domain:
implemented_optional_features: []
known_deviations: []
authority_policy_version:
privacy_profile:
contest_and_recourse_scope:
```

A conformance statement is descriptive.

It is not a legal, ethical, clinical, or safety certification.
