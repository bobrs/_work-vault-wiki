# Candidate Semantic-Trail to W3C PROV Mapping

Status: research artifact  
Content canon status: unset

## Reuse first

The Semantic Trail architecture should extend W3C PROV rather than create a parallel provenance substrate.

| Semantic-trail element | Candidate PROV representation |
|---|---|
| Source artifact | `prov:Entity` |
| Trace, projection, or summary | `prov:Entity` |
| Creation, extraction, compression, translation, or generation | `prov:Activity` |
| Human, institution, community, or role | `prov:Agent` |
| Language model or software system | `prov:SoftwareAgent` |
| Trace generation | `prov:wasGeneratedBy` |
| Source read or retrieval | `prov:used` |
| Attribution | `prov:wasAttributedTo` |
| Derivation | `prov:wasDerivedFrom` |
| Revision | `prov:wasRevisionOf` |
| Responsible agent | `prov:wasAssociatedWith` |
| Witness package | `prov:Bundle` |

## Required Telic Field extensions

PROV remains domain-general. A semantic-trail profile requires additional terms for:

```text
center_of_standing
affected_center
evidence_status
descriptive_authority
interpretive_authority
action_authority
consent_scope
protected_condition
uncertainty_status
semantic_integrity_status
valid_time
expiry
contest
release
uptake
consequence
```

## Design constraints

- A provenance graph must not expose protected source context merely to prove lineage.
- Model-generated reformulations remain derived entities.
- A summary must point to source entities and transformation activity.
- Corrections should create revisions rather than silently rewriting historical use.
- Release may disable future use while preserving a bounded historical witness.
- Provenance completeness does not establish truth, legitimacy, or consent.
