# Record Consolidation and Canonical Semantic Spine

Status: candidate Phase I input  
Content canon status: unset

The F/G sequence produced eight primary record families, two supporting profiles, and several matrices. The bridge pass preserves all eight conceptual objects while removing repeated envelope fields from the future technical specification.

---

# 1. Consolidation principle

The existing research records repeat:

- identifiers;
- status;
- source;
- standing;
- scope;
- authority;
- consent;
- uncertainty;
- valid time;
- transaction time;
- provenance;
- review;
- lifecycle;
- correction.

Phase I should define these once.

Each specialized record then references the common envelope and adds only domain-specific fields.

> **A field repeated across records should become a shared type unless its meaning materially changes.**

---

# 2. Canonical semantic spine

```text
CENTER
  ↓ creates, confirms, delegates, or is represented by
SOURCE OBJECT
  ↓ scoped through
TELIC PROJECTION
  ↓ preserved or transformed as
SEMANTIC TRAIL
  ↓ selected into
ACTIVE CONTEXT
  ↓ interpreted by
RECEIVER MIRROR
  ↓ organized into
FIELD MAP
  ↓ explored through
ROUTE
  ↓ constrained by
GOVERNANCE GATE
  ↓ permits
AUTHORIZED ACTION
  ↓ produces
CONSEQUENCE
  ↓ preserved through
WITNESS
  ↓ enables
CORRECTION / REVIEW / RELEASE / SUCCESSION / DISSOLUTION
```

Surrounding profiles and relations:

```text
CONTEXT CAPACITY
TEMPORAL STANDING
LOOP DEPENDENCY AND SUBSTRATE
MODEL ROLE AND CREDENTIAL
TRAINING LINEAGE
CONTEST AND RECOURSE
```

---

# 3. Common Telic Record Envelope

Every consequential object may carry a common envelope.

```yaml
record_id:
record_type:
schema_version:
record_version:

status:
  draft
  active
  restricted
  contested
  stale
  expired
  superseded
  released
  deleted
  archived
  dissolved

valid_time:
  valid_from:
  valid_to:

transaction_time:
  recorded_at:
  superseded_at:

source:
  source_objects: []
  source_centers: []
  represented_by: []
  evidence_status:

standing:
  affected_centers: []
  standing_type:
  missing_standing: []

scope:
  domain:
  recipients: []
  purposes: []
  prohibited_uses: []

authority:
  descriptive:
  interpretive:
  recommendation:
  authorization:
  execution:
  adjudication:

consent:
  basis:
  scope:
  version:
  state:
  withdrawal_route:

uncertainty:
  factual:
  source:
  interpretation:
  authority:
  consequence:
  unresolved: []

provenance:
  bundle:
  derivations: []
  transformations: []
  models: []
  policy_versions: []

review:
  review_trigger:
  review_at:
  review_authority:
  correction_route:

lifecycle:
  expiry:
  release_conditions: []
  successor:
  residual_state: []
```

Not every object exposes every field.

Domain profiles should define required subsets.

---

# 4. Shared types

## 4.1 CenterReference

Represents a person, community, institution, role, temporal state, or other affected center.

Required:

```yaml
center_id:
center_type:
standing_type:
representation_status:
delegation:
```

Do not encode an internal orientation or model agent as an ordinary person.

## 4.2 EvidenceStatus

Frozen values:

```text
DIRECT
CONFIRMED
DELEGATED
OBSERVED
INFERRED
GENERATED
RETRIEVED
CONTESTED
UNKNOWN
STALE
EXPIRED
REVOKED
OUT_OF_SCOPE
```

## 4.3 AuthorityEnvelope

Separate:

```text
DESCRIBE
INTERPRET
RECOMMEND
AUTHORIZE
EXECUTE
ADJUDICATE
WITNESS
```

Authority is operation-specific.

## 4.4 ConsentEnvelope

Contains:

- authority basis;
- consent state where applicable;
- scope;
- purpose;
- version;
- valid time;
- withdrawal;
- downstream use.

Do not encode non-consent authority as `consent=true`.

## 4.5 ProvenanceBundle

Map to W3C PROV:

- entity;
- activity;
- agent;
- derivation;
- revision;
- association;
- bundle.

Add Telic Field terms for standing, authority, consent, semantic status, uptake, consequence, and release.

## 4.6 LifecycleState

Common lifecycle:

```text
DRAFT
ACTIVE
PAUSED
RESTRICTED
CONTESTED
STALE
EXPIRED
SUPERSEDED
RELEASED
DELETED
ARCHIVED
DISSOLVED
```

Specialized records may add domain states without redefining the common states.

---

# 5. Specialized record families

## 5.1 Telic Projection Record

**Purpose**

Represents what a center has made available for a defined relation or action.

**Own fields**

- desired states;
- avoided states;
- boundaries;
- protected conditions;
- unacceptable sacrifices;
- evidence class;
- source confirmation;
- derived projections.

**Does not own**

- full source field;
- navigation route;
- model decision;
- complete temporal history.

**Primary references**

```text
CenterReference
SourceObject
ConsentEnvelope
AuthorityEnvelope
ProvenanceBundle
```

---

## 5.2 Context Carrying Capacity Profile

**Purpose**

Assesses whether an active loop can preserve enough relevant difference for legitimate next action.

**Object type**

Assessment profile, not an event ledger.

**Dimensions**

- standing coverage;
- contradiction tolerance;
- semantic resolution;
- temporal span;
- provenance retention;
- uncertainty retention;
- routing capacity;
- recovery capacity;
- privacy capacity;
- participant-load tolerance;
- escalation capacity;
- stop capacity.

**Consolidation rule**

Do not copy center, consent, or provenance fields into the profile.

Reference the session, route, or loop being assessed.

---

## 5.3 Temporal Standing Record

**Purpose**

Represents relations among earlier authority, current action, future affected centers, successors, commitments, and release.

**Own fields**

- prior authority;
- future affected centers;
- possibilities preserved and closed;
- irreversible effects;
- commitments;
- revision authority;
- release conditions.

**Consolidation rule**

Use the common valid-time and transaction-time types.

Reference consent and authority versions rather than duplicating them.

---

## 5.4 Loop Dependency and Compatibility Record

**Purpose**

Represents a loop's substrate, dependency flows, compatibility, lock-in, exit, and residual state.

**Own fields**

- declared, encoded, rewarded, operative, and protected teloi;
- material, semantic, relational, institutional, telic, and capacity substrate;
- dependency flows;
- receiving field;
- compatibility status;
- lock-in;
- forkability;
- dissolution route;
- residual state.

**Consolidation rule**

Dependency sources and affected centers use CenterReference or LoopReference.

Do not duplicate semantic-trail details; reference the relevant trail records.

---

## 5.5 Semantic Trail Record

**Purpose**

Represents a persistent distinction, its lineage, interpretation, uptake, consequence, correction, and release.

**Own fields**

- trace type;
- semantic content;
- alternative interpretations;
- telic function;
- uptake events;
- forks;
- derived trails;
- semantic-integrity status.

**Consolidation rule**

All creation and transformation lineage uses ProvenanceBundle.

Action consequences reference DecisionWitness or ActionEvent.

---

## 5.6 Polytelometric Navigation Record

**Purpose**

Represents a plural-end decision field and candidate routes.

**Own fields**

- decision scope;
- centers;
- telic items;
- field relations;
- routes;
- cost bearers;
- analysis adapters;
- governance gates;
- selected route;
- dissent;
- unresolved remainder.

**Consolidation rule**

Telic items reference Projection Records where available.

Routes reference Temporal Standing, Capacity Profile, and Loop Dependency assessments instead of copying their contents.

---

## 5.7 Semantic Polytelometry Session Record

**Purpose**

Orchestrates participants, provider, model roles, context, routes, actions, semantic trajectories, contest, and witness for a model-mediated session.

**Object type**

Session aggregate and event stream.

**Own fields**

- participant roles;
- provider disclosure;
- model instances and role envelopes;
- active-context retrieval events;
- model outputs;
- semantic trajectory;
- actions;
- contest and recourse;
- session lifecycle.

**Consolidation rule**

Reference Projection, Trail, Navigation, Capacity, Temporal Standing, and Training Lineage records.

Do not reproduce them as nested authoritative copies.

---

## 5.8 Consentful Training Lineage Record

**Purpose**

Represents model source authority, transformations, labor, preference governance, constitutions, training events, synthetic data, withdrawal, benefit, and succession.

**Own fields**

- model and provider;
- declared and prohibited purposes;
- release regime;
- source collections;
- training authority;
- transformations;
- human contributions;
- preference governance;
- model constitution;
- training events and checkpoints;
- synthetic lineage;
- withdrawal and unlearning;
- derivative and successor models;
- benefit and accountability.

**Consolidation rule**

Use ProvenanceBundle for source and transformation lineage.

Link runtime use to the Session Record without collapsing training and operation profiles.

---

# 6. Supporting policy profiles

## 6.1 Constitutional Self Safety Profile

This is a **domain policy profile**, not a core record.

It constrains AI use in internal-self or mental-health-adjacent contexts.

It should be implemented as:

```text
DomainPolicyProfile: constitutional_self
```

with:

- allowed roles;
- prohibited roles;
- required controls;
- escalation and crisis boundaries.

## 6.2 Candidate Architecture Module Map

The earlier G.3 architecture is retained as a module inventory.

It is superseded as the canonical object model by this consolidation.

Its modules map as follows:

| Earlier module | Consolidated service |
|---|---|
| standing registry | Center and Standing Registry |
| projection capture | Projection Service |
| inference ledger | Semantic Trail and Trajectory Service |
| mirror return | Participant Recognition Interface |
| relation graph | Semantic Graph / Trail Store |
| consent authority envelope | Common Authority and Consent Types |
| comparison engine | Navigation Analysis Adapters |
| route generator | Navigation Service |
| witness provenance layer | PROV and Event Stream |
| context capacity monitor | Capacity Assessment Service |
| stop escalation controller | Governance Gate Engine |
| decision-system adapters | Declared Analysis and Execution Adapters |

---

# 7. Event model

The canonical spine should be event-oriented.

Candidate common events:

```text
center_registered
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
field_classified
route_generated
route_rejected
consent_granted
consent_withdrawn
authority_delegated
authority_expired
gate_failed
action_authorized
action_executed
consequence_recorded
contest_opened
correction_propagated
route_revised
loop_forked
record_released
successor_assigned
loop_dissolved
```

Training-lineage events remain a separate but linkable namespace.

---

# 8. Identity and versioning

Every core object requires:

- stable identifier;
- schema version;
- record version;
- valid time;
- transaction time;
- provenance;
- supersession relation.

Corrections must not silently overwrite records that governed action.

A current projection may supersede an earlier projection.

The decision witness should identify which version was operative.

---

# 9. Graph and event stream

The architecture should use both.

## Graph

Useful for:

- centers;
- projections;
- relations;
- dependencies;
- routes;
- provenance;
- successor links.

## Event stream

Useful for:

- order;
- validity;
- correction;
- authorization;
- action;
- consequence;
- contest;
- release.

The current graph is a materialized view over witnessed events.

A graph edge without event and authority history should not govern consequential action by default.

---

# 10. Minimal Phase I slice

Phase I should not implement every field.

The minimum viable slice is:

1. **CenterReference**
2. **Common Telic Record Envelope**
3. **Telic Projection Record**
4. **Semantic Trail / Provenance Event**
5. **Polytelometric Navigation Record**
6. **Model Role and Authority Envelope**
7. **Decision Witness**
8. **Contest and Correction Event**

Temporal Standing, Capacity, Loop Dependency, and Training Lineage should enter as referenced profiles in the second increment.

This slice can demonstrate the central invariant:

```text
source projection
→ model interpretation
→ participant correction
→ candidate route
→ authority gate
→ witnessed action
```

---

# 11. Schema design rules

1. Unknown is a valid value.
2. Contested is not false.
3. Inference never silently becomes direct statement.
4. Consent and authority are operation-specific.
5. Protected conditions are typed separately from preferences.
6. Missing standing is represented, not scored as zero.
7. Model role is separate from model capability.
8. Every consequential action references its operative projection and route.
9. Every correction identifies affected descendants.
10. Release disables future authority without falsifying necessary history.
11. Domain profiles may add constraints but must not erase common provenance.
12. The schema itself is versioned, contestable, exportable, and forkable.

---

# 12. Open technical questions

- How much of the common envelope should be mandatory?
- How can protected omission be proven without exposing content?
- Which identifiers remain portable across providers?
- How should community authority be attested without centralizing control?
- How are consent and authority conflicts represented?
- How should source correction propagate into model memory and derived summaries?
- What is the smallest semantic-trajectory record that still exposes material drift?
- Which fields can be automatically generated without increasing false authority?
- How can the system express domain-specific legal standing without corrupting constitutional standing?
- Which event store and graph technologies best preserve selective disclosure and bitemporal history?

These questions belong in I.0 and I.1.

They should not be settled through the public reader path.
