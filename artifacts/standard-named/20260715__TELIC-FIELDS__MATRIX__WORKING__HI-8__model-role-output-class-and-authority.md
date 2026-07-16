# Model Role, Output Class, and Authority Matrix

Status: candidate pre-production  
Content canon status: unset

| Model role | Typical outputs | May do | Must not infer |
|---|---|---|---|
| Extractor | Terms, entities, claims, boundaries | Identify candidate distinctions | That extraction is complete or authoritative |
| Structurer | Field map, issue graph, dependency map | Organize reviewed source material | Standing, consent, or public mandate |
| Translator | Cross-vocabulary rendering | Offer parallel phrasing | That translation preserves every implication |
| Comparator | Difference, tradeoff, uncertainty | Compare under disclosed methods | Which method should govern |
| Retriever | Source and context candidates | Return authorized traces | That retrieved content may govern action |
| Route generator | Candidate options and portfolios | Expand the option set | Participant authorship or adoption |
| Challenger | Counterargument, missing-context prompt | Test assumptions and premature consensus | Adjudicative authority |
| Mediator | Turn structure, clarification, bounded summaries | Support process under assigned rules | Ownership of participant positions |
| Witness assistant | Draft event and decision records | Prepare reviewable witness artifacts | That a draft is the final witness |
| Executor | Tool plan and tool result | Execute only through a passed action gate | Consent, authority, or scope from recommendation alone |

## Output-class boundary

```text
extraction
structure
translation
comparison
retrieval result
summary
inference
generated option
generated argument
challenge
clarification question
route recommendation
tool plan
tool result
witness draft
```

Every material output should preserve:

```text
source inputs
source status
transformations
uncertainty
standing effect: none
authority effect: none
consent effect: none
correction route
```

## Hard distinctions

```text
capability ≠ role
role ≠ permission
permission ≠ authority
authority ≠ legitimacy
summary ≠ source
inference ≠ consent
recommendation ≠ authorization
tool result ≠ interpretation
```

## Governing principle

> The model may perform an operation without becoming the authority whose field gives the operation legitimacy.
