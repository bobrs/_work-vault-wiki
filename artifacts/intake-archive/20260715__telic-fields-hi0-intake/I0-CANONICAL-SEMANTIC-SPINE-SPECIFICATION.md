---
title: "I.0 — Canonical Semantic Spine and Core Envelope Specification"
artifact_date: "2026-07-15"
artifact_type: "candidate-technical-specification"
domain: "TELIC-FIELDS"
scope: "WORKING"
status: "pre-production"
content_canon_status: "unset"
specification_version: "0.1"
derived_from:
  - "FG-S Cross-Paper Synthesis"
  - "FG-S Terminology Freeze"
  - "FG-S Record Consolidation and Canonical Spine"
---

# I.0 — Canonical Semantic Spine and Core Envelope Specification

## 1. Purpose

I.0 defines the minimum technical vocabulary needed to preserve the central Telic Field invariant:

> **A representation may gain action power only through a visible chain of source, standing, authority, consent where applicable, witness, correction, and exit.**

This specification is intentionally smaller than the full F/G architecture.

It does not define a universal ontology, a production platform, a certification regime, or an automated moral decision system.

It defines:

- the canonical semantic spine;
- shared record-envelope fields;
- minimum core types;
- a small event vocabulary;
- model-role and authority separation;
- correction and lifecycle behavior;
- privacy and progressive-disclosure rules;
- a candidate W3C PROV mapping;
- conformance profiles.

---

# 2. Normative language

The terms below are local specification terms.

- **MUST** — required for the stated conformance profile.
- **MUST NOT** — prohibited for the stated conformance profile.
- **SHOULD** — recommended unless a documented reason justifies another design.
- **SHOULD NOT** — discouraged unless a documented reason justifies it.
- **MAY** — optional.
- **UNRESOLVED** — intentionally not converted into false precision.
- **CONTESTED** — materially disputed; not equivalent to false.
- **UNKNOWN** — not adequately established.

A conforming implementation MUST preserve the difference among `UNKNOWN`, `CONTESTED`, and `FALSE`.

---

# 3. Canonical semantic spine

```text
CENTER
→ SOURCE OBJECT
→ TELIC PROJECTION
→ SEMANTIC TRAIL EVENT
→ ACTIVE CONTEXT SELECTION
→ RECEIVER MIRROR
→ FIELD MAP
→ ROUTE
→ GOVERNANCE GATE
→ AUTHORIZED ACTION
→ CONSEQUENCE
→ DECISION WITNESS
→ CONTEST / CORRECTION / RELEASE
```

## 3.1 Spine rule

A consequential action MUST reference:

1. at least one source object or acknowledged source gap;
2. at least one operative projection or acknowledged projection gap;
3. the authority basis for action;
4. the route or direct-action rule used;
5. the governance-gate result;
6. the action event;
7. the witness record.

An implementation MUST NOT infer that a complete field has been captured merely because the required references exist.

---

# 4. Core type model

## 4.1 `CenterReference`

Represents a person, group, community, institution, role, temporal state, or affected center.

Required fields:

```yaml
center_id:
center_type:
standing_type:
representation_status:
```

Candidate values:

```text
center_type:
  person
  group
  community
  institution
  role
  temporal_state
  affected_condition
  unknown

standing_type:
  constitutional
  legal
  operational
  temporal
  internal_representational
  unknown

representation_status:
  direct
  delegated
  represented
  absent
  contested
  unknown
```

Rules:

- A model instance MUST NOT be encoded as a human center.
- An internal orientation MUST NOT be encoded as an independent person.
- A future affected center MAY be represented with temporal standing.
- Temporal standing MUST NOT be encoded as present consent.

## 4.2 `SourceObject`

Represents material that entered the system before the current transformation.

Examples:

- participant statement;
- document;
- event record;
- delegated representation;
- policy;
- retrieved source;
- correction;
- prior projection.

Required fields:

```yaml
source_object_id:
source_type:
created_by:
evidence_status:
```

A source object MUST remain distinguishable from any model-generated representation derived from it.

## 4.3 `TelicProjection`

Represents a scoped, attributable, correctable portion of a center's field.

Minimum content:

```yaml
projection_id:
source_center:
source_objects:
evidence_status:
projection_type:
expression:
scope:
authority:
status:
```

`projection_type` values MAY include:

```text
goal
value
preference
boundary
protected_condition
obligation
prediction
fear
constraint
invariant
uncertainty
release_condition
```

Rules:

- A `boundary` MUST NOT be silently converted into a `preference`.
- A `protected_condition` MUST identify its source, scope, current authority, and review path.
- An `inferred` projection MUST NOT become `confirmed` without a separate confirmation event.
- A projection MAY remain `contested`.

## 4.4 `SemanticTrailEvent`

Represents creation, derivation, transformation, use, contest, correction, or release of a persistent distinction.

Required fields:

```yaml
event_id:
event_type:
subject_record:
agent:
recorded_at:
provenance:
```

Candidate event types:

```text
source_registered
projection_created
projection_confirmed
projection_corrected
projection_withdrawn
trail_created
trail_derived
trail_contested
context_retrieved
mirror_returned
route_generated
gate_evaluated
action_authorized
action_executed
consequence_recorded
contest_opened
correction_propagated
record_released
record_dissolved
```

Historical events MUST NOT be silently overwritten when they governed action.

## 4.5 `ActiveContextSelection`

Represents the bounded context actually selected for one model or decision operation.

Required fields:

```yaml
context_selection_id:
operation_id:
included_sources:
selection_rule:
known_gaps:
selected_at:
```

Rules:

- Active context MUST NOT be represented as the complete field.
- Active corrections, revocations, protected conditions, and current authority SHOULD receive priority over ordinary semantic similarity in consequential use.
- The selection SHOULD record known excluded classes and privacy restrictions.
- `ActiveContextSelection` is an event-scoped object, not a durable profile of the person.

## 4.6 `ReceiverMirror`

Represents a receiver's interpretation.

Required fields:

```yaml
mirror_id:
receiver:
based_on:
interpretation:
epistemic_status:
participant_recognition:
```

Rules:

- A receiver mirror MUST remain attributable to its receiver.
- A mirror MUST NOT be recorded as a direct source statement.
- Participant disagreement MUST NOT erase the mirror; it changes its authority and status.
- The record SHOULD preserve the source's response.

## 4.7 `FieldMap`

A field map is a current, revisable view over projections and mirrors.

Candidate classes:

```text
shared
compatible
conditional
conflicting
protected
unresolved
missing_standing
released
```

Rules:

- `FieldMap` is a materialized view, not the source of truth.
- `UNRESOLVED` MUST NOT be converted into a low score merely to allow ranking.
- `MISSING_STANDING` MUST NOT be represented as zero preference.
- A field map SHOULD identify the records from which each classification was derived.

## 4.8 `Route`

Represents a candidate sequence of action, review, and exit.

Minimum content:

```yaml
route_id:
source:
sequence:
beneficiaries:
cost_bearers:
protected_conditions:
uncertainties:
reversibility:
required_authority:
required_consent:
review_triggers:
exit:
```

Rules:

- A route MUST identify known cost bearers.
- A route MUST identify irreversible or difficult-to-reverse steps.
- A route MAY be `pause`, `defer`, `narrow`, `fork`, `escalate`, `release`, or `no_adequate_route`.
- Machine-generated routes MUST identify the generating model and role.

## 4.9 `GovernanceGate`

Represents the decision on whether a route may advance.

Gate dimensions:

```text
standing
authority
consent
capacity
privacy
temporal_validity
tool_use
human_reentry
stop
```

A gate result is one of:

```text
PASS
PASS_WITH_CONDITIONS
PAUSE
ESCALATE
FAIL
UNKNOWN
CONTESTED
```

Rules:

- An implementation MUST NOT collapse gate dimensions into one hidden score.
- A failed authority gate MUST prevent execution.
- Missing consent MUST prevent recruitment where consent is the required authority basis.
- Missing standing SHOULD cause pause, narrowing, or escalation for materially consequential action.
- Gate rules MUST be versioned.

## 4.10 `ModelRoleAuthorityEnvelope`

Separates capability from authority.

Candidate roles:

```text
extract
structure
translate
retrieve
compare
generate_route
challenge
mediate
recommend
witness
execute
adjudicate
```

Required fields:

```yaml
model_instance:
assigned_roles:
allowed_inputs:
allowed_outputs:
allowed_tools:
prohibited_actions:
confirmation_required:
execution_authority:
review_authority:
stop_conditions:
```

Rules:

- `adjudicate` MUST be prohibited by default.
- Tool access MUST be separately authorized.
- A model MUST NOT expand its own role.
- Several model agents MUST NOT be treated as several centers of standing.
- A recommendation MUST NOT be treated as authorization.

## 4.11 `AuthorizedAction`

Required fields:

```yaml
action_id:
route:
proposed_by:
authorized_by:
executed_by:
authority_basis:
tool:
reversibility:
executed_at:
```

Rules:

- `authorized_by` MUST identify a competent authority or explicitly recorded automated rule.
- The action MUST reference the operative gate result.
- The action MUST NOT exceed the authorized route scope.
- High-consequence irreversible actions SHOULD require meaningful human re-entry or a domain-specific authority process.

## 4.12 `Consequence`

Represents observed result, not merely intended output.

Required fields:

```yaml
consequence_id:
action:
observed_by:
affected_centers:
observed_at:
result:
uncertainty:
```

Consequences MAY be incomplete, disputed, delayed, or unknown.

## 4.13 `DecisionWitness`

Minimum content:

```yaml
witness_id:
decision_scope:
operative_sources:
operative_projections:
active_context:
mirrors:
field_map:
routes_considered:
selected_route:
gate_results:
authority:
action:
dissent:
unresolved:
model_versions:
policy_versions:
consequences:
```

Rules:

- A witness MUST preserve the distinction among source, inference, recommendation, authorization, and execution.
- A witness MUST NOT expose private context beyond the authority and need for accountability.
- A witness SHOULD be exportable independently of the model that produced it.

## 4.14 `ContestCorrectionEvent`

Represents an attempt to challenge or change an operative record or action.

Minimum content:

```yaml
contest_id:
challenger:
target:
grounds:
requested_change:
status:
opened_at:
responsible_authority:
```

Candidate statuses:

```text
OPEN
UNDER_REVIEW
PAUSED
CORRECTED
PARTIALLY_CORRECTED
REJECTED
ESCALATED
CLOSED_WITH_REMAINDER
```

Rules:

- Contest MUST be able to target source, interpretation, route, authority, action, or consequence.
- A contest path MUST identify an authority capable of changing the outcome where change remains possible.
- Explanation without an outcome-changing route MUST NOT be described as full contestability.

---

# 5. Common record envelope

All consequential records SHOULD use the shared envelope defined in:

`candidate-telic-field-core-record-envelope.schema.json`

The common envelope contains:

- identity and version;
- status;
- valid and transaction time;
- source;
- standing;
- scope;
- authority;
- consent;
- uncertainty;
- provenance;
- review;
- lifecycle.

## 5.1 Unknown and contested values

An implementation MUST preserve unknown and contested values through transformations.

It MUST NOT:

- replace unknown with false;
- replace contested with low confidence only;
- replace missing standing with zero preference;
- replace expired authority with active authority because the underlying content persists.

## 5.2 Bitemporal behavior

Consequential records SHOULD preserve:

- **valid time** — when the state applied in the represented world;
- **transaction time** — when the system learned or recorded it.

A correction made today MAY state that a record was already invalid yesterday.

The witness MUST preserve both.

---

# 6. Authority model

Authority is operation-specific.

The minimum authority vocabulary is:

```text
DESCRIBE
INTERPRET
RECOMMEND
AUTHORIZE
EXECUTE
ADJUDICATE
WITNESS
```

Rules:

1. Descriptive authority MUST NOT imply execution authority.
2. Interpretive authority MUST NOT imply authorization.
3. Recommendation MUST NOT imply consent.
4. Execution authority MUST identify scope and expiry.
5. Adjudication authority MUST identify its institutional source and recourse route.
6. Witness authority MUST NOT imply authority to decide the dispute being witnessed.
7. A person MAY delegate one authority without delegating the others.

---

# 7. Consent and other authority bases

The system MUST distinguish consent from other legitimate authority classes.

Candidate bases:

```text
individual_consent
delegated_authority
contract
license
community_governance
public_mandate
fiduciary_authority
statutory_authority
emergency_authority
other_lawful_basis
unknown
contested
```

Rules:

- A non-consent basis MUST NOT be recorded as consent.
- Consent MUST identify scope, purpose, version, temporal validity, and withdrawal route.
- Conversation or preference inference MUST NOT be treated as execution consent for consequential action.
- A center MUST NOT consent on behalf of another center without valid representation or authority.
- Emergency authority MUST be bounded, witnessed, reviewed, and expired.

---

# 8. Correction and lifecycle

## 8.1 Correction

A correction MUST:

1. identify the target record;
2. identify the corrected field or interpretation;
3. preserve the previous version if it governed action;
4. identify derived records known to depend on it;
5. initiate propagation or mark propagation gaps;
6. update authority where required;
7. preserve unresolved remainder.

## 8.2 Release

Release ends or narrows future authority of a record.

Release MAY:

- expire a preference;
- withdraw consent;
- retire a route;
- remove a memory from active retrieval;
- end a role;
- terminate a loop.

Release MUST NOT be represented as erasure of past consequence.

## 8.3 Deletion

Deletion removes content where legally, ethically, or operationally appropriate.

A deletion event SHOULD preserve only the minimum proof necessary for accountability.

Deletion MUST NOT be described as model unlearning unless a separate unlearning claim is supported.

## 8.4 Dissolution

A dissolved loop MUST identify:

- stopped authority;
- residual records;
- successor or aftercare;
- open contests;
- unresolved obligations;
- retained witness;
- deletion and release status.

---

# 9. Privacy and progressive disclosure

## 9.1 Minimum necessary projection

A conforming system MUST allow a center to state a boundary or protected condition without disclosing the entire personal history behind it.

## 9.2 Protected omission

A system MAY preserve proof that:

- a valid restriction exists;
- an authorized reviewer confirmed it;
- a gate failed;

without exposing the protected content to every participant.

## 9.3 Role-based views

The same record MAY have separate views for:

- source participant;
- mediator;
- decision authority;
- auditor;
- public record;
- model process.

Views MUST preserve the status of omitted information rather than implying nothing exists.

## 9.4 Retention

Every persistent record SHOULD define:

- retention purpose;
- retention duration;
- access;
- expiry;
- deletion or release route.

## 9.5 Low-stakes proportionality

Ephemeral, reversible, low-stakes assistance MAY use a reduced profile.

At minimum it SHOULD preserve:

- model role;
- source versus generated distinction;
- action boundary;
- correction route.

---

# 10. Candidate W3C PROV mapping

I.0 reuses W3C PROV concepts.

| I.0 object | Candidate PROV representation |
|---|---|
| SourceObject | `prov:Entity` |
| TelicProjection | `prov:Entity` |
| ReceiverMirror | `prov:Entity` |
| Route | `prov:Entity` |
| DecisionWitness | `prov:Bundle` |
| Transformation | `prov:Activity` |
| Retrieval | `prov:Activity` |
| Gate evaluation | `prov:Activity` |
| Action execution | `prov:Activity` |
| Person, institution, or model | `prov:Agent` |
| Language model | `prov:SoftwareAgent` |
| Derivation | `prov:wasDerivedFrom` |
| Generation | `prov:wasGeneratedBy` |
| Use | `prov:used` |
| Attribution | `prov:wasAttributedTo` |
| Revision | `prov:wasRevisionOf` |
| Association | `prov:wasAssociatedWith` |

Telic Field extensions are still required for:

- standing;
- evidence status;
- authority;
- consent;
- protected conditions;
- field class;
- participant recognition;
- contest;
- release;
- consequence.

PROV completeness MUST NOT be interpreted as truth, consent, or legitimacy.

---

# 11. Conformance profiles

## 11.1 Profile P0 — Documentary

A P0 implementation:

- distinguishes source and generated material;
- versions records;
- supports correction;
- declares model role where a model participates.

P0 MUST NOT claim action-governance conformance.

## 11.2 Profile P1 — Source-Aware Navigation

A P1 implementation additionally:

- represents centers and standing;
- uses TelicProjection;
- preserves field classes;
- records routes and cost bearers;
- preserves unresolved and missing-standing states.

P1 MAY recommend but MUST NOT execute consequential action solely under P1.

## 11.3 Profile P2 — Action-Bearing

A P2 implementation additionally:

- uses GovernanceGate;
- separates authority operations;
- records consent or another authority basis;
- uses ModelRoleAuthorityEnvelope;
- creates AuthorizedAction and DecisionWitness records;
- supports role-scoped tool use.

## 11.4 Profile P3 — Contestable

A P3 implementation additionally:

- supports contest and correction events;
- can pause or alter action where still possible;
- propagates corrections or marks gaps;
- provides independent witness export;
- supports lifecycle release and dissolution;
- preserves practical human re-entry for designated high-consequence actions.

## 11.5 Conformance statement

A conformance statement MUST name:

- profile;
- schema version;
- implemented optional features;
- domain limits;
- unresolved deviations;
- authority and policy versions.

The phrase **Telic Field conformant** MUST NOT be used without a profile identifier.

---

# 12. Security and failure rules

A conforming implementation MUST NOT:

- execute from an unconfirmed model inference when direct authority is required;
- treat model-agent voting as human consent;
- hide a failed gate behind a composite score;
- erase dissent through summarization;
- convert protected conditions into preferences without an authorized event;
- represent active context as complete context;
- preserve private source context merely because witness is desirable;
- let a model change its own authority envelope;
- claim meaningful human control when the human lacks source access or practical override.

A conforming implementation SHOULD:

- minimize credentials;
- use explicit confirmation for consequential tools;
- log tool scope and result;
- make stale or expired records visibly ineligible;
- degrade from execute to prepare, recommend, compare, ask, escalate, or stop as authority or context fails.

---

# 13. I.0 non-goals

I.0 does not define:

- legal compliance for any jurisdiction;
- clinical diagnosis or treatment;
- AI personhood;
- universal standing rules;
- universal moral weights;
- a final ontology;
- automatic classification of protected conditions;
- a complete training-lineage standard;
- a production cryptographic protocol;
- a certification body;
- a universal optimizer.

---

# 14. I.0 implementation target

The minimal implementable demonstration is:

```text
source statement
→ scoped projection
→ model mirror
→ participant correction
→ candidate route
→ governance gate
→ authorized action or no-decision
→ witness
→ contest and correction
```

The three HI-0 worked examples test this target.

I.0 should advance only if those examples remain understandable, privacy-preserving, and small enough for proportional use.
