# Language-Model Role and Authority Matrix

Status: draft  
Content canon status: unset

| Role | Permitted contribution | Principal risk | Default authority |
|---|---|---|---|
| Extractor | Identify candidate statements, boundaries, uncertainties, and entities | Omission or inference presented as direct statement | None |
| Structurer | Place material into records, graphs, timelines, or field classes | Ontology capture and false precision | None |
| Translator | Re-express material across vocabularies or domains | Semantic substitution and cultural loss | None |
| Comparator | Identify agreement, contradiction, change, or modeled consequence | Hidden comparison rule and false equivalence | None |
| Retriever | Select source and historical context | Missing boundaries, corrections, revocations, or dissent | None |
| Route generator | Propose actions, stages, forks, reviews, or exits | Framing the option set and omitting refusal | None |
| Challenger | Surface counterevidence, alternatives, and missing standing | False balance, overload, or model domination | None |
| Mediator | Manage turn-taking, rules, clarification, and shared projections | Hidden asymmetry or summary sovereignty | Procedural only, if delegated |
| Recommender | Rank or recommend routes under a declared rule | Recommendation treated as authorization | Recommendation only |
| Witness assistant | Preserve source, transformation, action, and correction | Surveillance and overretention | Record only |
| Executor | Call tools or perform external action | Scope drift and irreversible consequence | Explicit, narrow, revocable delegation |
| Adjudicator | Resolve contested standing, rights, or authority | Model sovereignty | Prohibited by default |

## Governing separations

```text
capability ≠ role
role ≠ permission
permission ≠ authority
authority ≠ legitimacy
recommendation ≠ consent
execution ≠ adjudication
model plurality ≠ standing plurality
human approval ≠ meaningful control
```

## Minimum role envelope

```yaml
assigned_role:
allowed_inputs:
allowed_transformations:
allowed_outputs:
allowed_tools:
prohibited_actions:
confirmation_required:
execution_authority:
review_authority:
stop_conditions:
```

## Hard boundary

> The model may increase the legibility of a field without gaining title to the field, the route, or the decision.
