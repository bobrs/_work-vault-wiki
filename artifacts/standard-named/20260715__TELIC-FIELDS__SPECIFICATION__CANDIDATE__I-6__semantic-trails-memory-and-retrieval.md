---
title: "I.6 — Semantic Trails, Memory, and Retrieval Specification"
artifact_date: "2026-07-15"
artifact_type: "candidate-technical-specification"
domain: "TELIC-FIELDS"
scope: "WORKING"
status: "pre-production"
content_canon_status: "unset"
specification_version: "0.1"
derived_from:
  - "I.0 — Canonical Semantic Spine and Core Envelope Specification"
  - "I.1 — Provenance, Event, and Correction Specification"
  - "I.2 — Navigation, Gate, and Decision-Witness Specification"
  - "I.3 — Context Capacity, Stop, and Escalation Specification"
  - "I.4 — Temporal Standing, Commitment, and Succession Specification"
  - "I.5 — Dependency, Drift, Lock-In, and Dissolution Specification"
  - "F.8 — Semantic Fields as Durable Telic Trails"
  - "G.9 — Meaning, Trace, Memory, and Semantic Field"
---

# I.6 — Semantic Trails, Memory, and Retrieval Specification

## 1. Purpose

I.6 defines how consequential traces are created, preserved, retrieved, corrected, transferred, archived, decayed, forgotten, released, and witnessed.

Its governing rule is:

> **A record can preserve a path without becoming the field that made the path.**

The living field includes centers of standing, active purposes, private context, contradiction, uncertainty, material consequence, and unexpressed possibility.

A trace preserves only a selected difference.

A semantic trail exists when a persistent trace becomes available to reorganize later navigation.

I.6 therefore distinguishes:

```text
field
trace
trail
memory
retrieval
authority
witness
```

A trace may be durable without being complete.

A memory may be useful without being current.

A retrieved item may be relevant without being authorized to govern action.

Repeated inference may become familiar without becoming source fact.

I.6 defines:

- semantic-trail events;
- durable traces;
- active and archival memory states;
- retrieval-authority grants;
- salience and decay;
- source, inference, correction, and contestation in memory;
- trace links and stigmergic coordination;
- forgetting, release, and deletion;
- memory contamination and stale-authority breach;
- model-session memory envelopes;
- cross-loop memory transfer;
- semantic-trail witnesses.

---

# 2. Normative scope

I.6 defines:

- `SemanticTrailEvent`;
- `DurableTraceRecord`;
- `MemoryStateRecord`;
- `RetrievalAuthorityGrant`;
- `SalienceDecayRecord`;
- `MemoryAssertionRecord`;
- `TraceLinkCoordinationRecord`;
- `ForgettingReleaseRecord`;
- `MemoryContaminationEvent`;
- `ModelSessionMemoryEnvelope`;
- `CrossLoopMemoryTransfer`;
- `SemanticTrailWitness`.

I.6 does not define:

- a complete theory of human memory;
- a universal theory of meaning;
- a claim that every persistent difference is semantic;
- one global salience score;
- one ideal retention period;
- universal permission to preserve records;
- automatic legitimacy from provenance;
- automatic truth from source status;
- automatic deletion from low salience;
- a claim that language models possess human autobiographical memory.

---

# 3. Semantic-trail event

A `SemanticTrailEvent` records an event that creates or changes a trail.

Candidate event types:

```text
TRACE_CREATED
TRACE_LINKED
TRACE_RETRIEVED
TRACE_REINFORCED
TRACE_DECAYED
TRACE_ARCHIVED
TRACE_REACTIVATED
TRACE_CORRECTED
TRACE_CONTESTED
TRACE_RESTRICTED
TRACE_RELEASED
TRACE_DELETED
TRACE_TRANSFERRED
TRACE_USED_FOR_ACTION
TRACE_BREACH_DETECTED
```

Required fields:

```yaml
event_id:
event_type:
trace:
valid_at:
recorded_at:
actor:
authority:
source_event:
purpose:
effect:
```

## 3.1 Rules

- Trail events MUST preserve valid time and record time.
- Retrieval MUST be recorded separately from use.
- Use for action MUST identify which trace version governed.
- Reinforcement MUST NOT silently convert inference into source fact.
- Reactivation MUST revalidate current authority.
- Deletion MUST distinguish content deletion from bounded deletion witness.

---

# 4. Durable trace

A `DurableTraceRecord` represents a persistent difference that may affect later navigation.

Required fields:

```yaml
trace_id:
trace_type:
source_centers:
affected_centers:
source_events:
content:
scope:
status:
provenance:
authority:
integrity:
lifecycle:
```

Candidate trace types:

```text
LINGUISTIC
DOCUMENTARY
MATERIAL
RELATIONAL
INSTITUTIONAL
COMPUTATIONAL
EMBODIED
ENVIRONMENTAL
OTHER
```

Candidate statuses:

```text
ACTIVE
RESTRICTED
CONTESTED
STALE
ARCHIVAL
EXPIRED
RELEASED
DELETED
SUPERSEDED
UNKNOWN
```

## 4.1 Rules

- A trace MUST identify its source relation.
- A trace MUST identify whether content is direct, observed, derived, inferred, or generated.
- A trace MUST preserve scope and material uncertainty.
- A trace MUST NOT claim to preserve the whole source field.
- A trace may remain historical after losing action authority.
- A trace may be restricted without being deleted.
- A trace may be deleted while a narrow deletion witness remains.

## 4.2 Governing distinction

> **The trail is not the terrain preserved. It is a difference left available for another act of orientation.**

---

# 5. Memory state

A `MemoryStateRecord` determines how a trace may participate in retrieval and action.

Candidate memory states:

```text
ACTIVE
ACTIVE_WITH_CONDITIONS
REFERENCE_ONLY
ARCHIVAL
RESTRICTED
QUARANTINED
CONTESTED
STALE
RELEASED
DELETED
UNKNOWN
```

Required fields:

```yaml
memory_state_id:
trace:
state:
eligible_for_retrieval:
eligible_for_action:
eligible_for_training:
conditions:
valid_time:
review:
status:
```

## 5.1 Rules

- Active memory MAY be retrieved for current coordination.
- Archival memory MAY explain history but MUST NOT silently authorize current action.
- Reference-only memory MAY be visible to a reviewer without entering automated recommendation.
- Restricted memory MUST require scoped authority.
- Quarantined memory MUST be excluded from ordinary retrieval.
- Deleted memory MUST not remain available through undeclared descendants.
- Memory state MUST be versioned rather than overwritten.

---

# 6. Retrieval authority

A `RetrievalAuthorityGrant` defines who or what may retrieve which trace for which purpose.

Required fields:

```yaml
grant_id:
retriever:
trace_scope:
purpose:
recipient:
operation:
context:
valid_time:
retention:
downstream_use:
review:
withdrawal:
status:
```

Candidate operations:

```text
SEARCH
READ
SUMMARIZE
COMPARE
RECOMMEND
TRAIN
EXPORT
DISCLOSE
ACT
OTHER
```

Candidate statuses:

```text
PROPOSED
ACTIVE
CONDITIONAL
STALE
EXPIRED
WITHDRAWN
SUPERSEDED
CONTESTED
UNKNOWN
```

## 6.1 Rules

- Search authority does not imply disclosure authority.
- Retrieval authority does not imply action authority.
- Summary authority does not imply training authority.
- A grant MUST specify recipient and purpose where material.
- Withdrawal MUST alter future retrieval.
- A system MUST preserve downstream gaps where withdrawal cannot yet reach every copy.
- Broad access to a repository MUST NOT be treated as permission to use every trace for every operation.

---

# 7. Salience and decay

A `SalienceDecayRecord` represents the changing probability or priority of retrieval.

Required fields:

```yaml
salience_id:
trace:
salience_basis:
initial_salience:
current_salience:
decay_rule:
reinforcement_events:
protected_floor:
action_authority_effect:
deletion_effect:
review:
status:
```

Candidate salience bases:

```text
RECENCY
FREQUENCY
CONSEQUENCE
AUTHORITY
SOURCE_REQUEST
TASK_RELEVANCE
CORRECTION_PRIORITY
PROTECTED_CONDITION
RISK
OTHER
```

## 7.1 Rules

- Salience is not legitimacy.
- Low salience MUST NOT delete a trace automatically.
- High salience MUST NOT convert a contested trace into truth.
- Corrections, revocations, protected conditions, and active boundaries MAY have a protected retrieval floor.
- Repetition MAY increase retrieval probability.
- Repetition MUST NOT increase source status or authority.
- Decay SHOULD reduce unnecessary retrieval while preserving bounded witness.

## 7.2 Governing distinction

> **What is easy to retrieve is not necessarily what is permitted to govern.**

---

# 8. Memory assertion

A `MemoryAssertionRecord` represents a claim stored or made retrievable through memory.

Candidate assertion classes:

```text
DIRECT_SOURCE_STATEMENT
OBSERVATION
DERIVED_FACT
MODEL_INFERENCE
MODEL_GENERATION
INSTITUTIONAL_CLASSIFICATION
CONTESTED_CLAIM
CORRECTION
REVOCATION
UNKNOWN
```

Required fields:

```yaml
assertion_id:
trace:
assertion_class:
content:
source:
confidence:
authority:
scope:
corrections:
contestation:
status:
```

Candidate statuses:

```text
ACTIVE
ACTIVE_WITH_QUALIFICATION
CONTESTED
CORRECTED
REVOKED
STALE
ARCHIVAL
RELEASED
UNKNOWN
```

## 8.1 Rules

- Direct source and model inference MUST remain distinct.
- A correction MUST link to what it corrects.
- A correction MAY change active retrieval without rewriting historical witness.
- An inference MAY be retained when useful, but MUST preserve its inferential status.
- Repeated retrieval MUST NOT launder inference into direct statement.
- Institutional classification MUST identify its issuing authority.
- Confidence MUST NOT substitute for authority.

---

# 9. Correction propagation

Correction propagation is the process by which a correction changes future active retrieval.

Minimum sequence:

```text
correction recorded
→ target trace identified
→ active memory updated
→ retrieval index updated
→ affected descendants identified
→ action paths paused where necessary
→ historical version preserved
→ unresolved downstream gaps recorded
```

## 9.1 Rules

- Active correction MUST outrank corrected content in ordinary action retrieval.
- Historical views MAY show both.
- The system MUST preserve which version governed each prior action.
- Correction propagation MUST include memory indexes, summaries, embeddings, caches, and derived profiles where technically possible.
- Unreachable descendants MUST remain visible as capacity or correction debt.
- A correction MUST NOT silently delete valid reliance or consequence.

---

# 10. Trace links and stigmergic coordination

A `TraceLinkCoordinationRecord` represents how traces guide later participants without direct central instruction.

Candidate link relations:

```text
SUPPORTS
CONTRADICTS
CORRECTS
DERIVES_FROM
REVISION_OF
REPLACES
DEPENDS_ON
TRIGGERS
BLOCKS
ROUTES_TO
SUMMARIZES
ANNOTATES
RELEASES
OTHER
```

Required fields:

```yaml
coordination_id:
environment:
traces:
links:
participants:
coordination_purpose:
central_controller:
authority:
correction:
decay:
status:
```

## 10.1 Rules

- Stigmergic coordination occurs through changes left in a shared environment.
- A central controller MAY exist, but is not required.
- Trace visibility and authority MUST remain distinct.
- A trail can coordinate effectively while serving an illegitimate outer purpose.
- A coordination trace SHOULD identify who may alter, remove, or contest it.
- Old traces SHOULD decay, archive, or expire when their routing purpose ends.

---

# 11. Forgetting, release, and deletion

A `ForgettingReleaseRecord` defines how a trace stops participating in future retrieval or governance.

Candidate actions:

```text
REDUCE_SALIENCE
REMOVE_FROM_ACTIVE_RETRIEVAL
ARCHIVE
RESTRICT
SEAL
RELEASE
DELETE_CONTENT
DELETE_DERIVATIVES
PRESERVE_DELETION_WITNESS
TRANSFER_CUSTODY
OTHER
```

Required fields:

```yaml
forgetting_id:
trace:
basis:
requested_by:
authority:
actions:
effective_at:
descendants:
surviving_witness:
surviving_obligations:
verification:
status:
```

Candidate statuses:

```text
REQUESTED
APPROVED
IN_PROGRESS
PARTIAL
COMPLETED
CONTESTED
FAILED
```

## 11.1 Rules

- Forgetting MAY be protective governance rather than loss.
- Release MUST end future recruitment under the released purpose.
- Deletion MUST identify known derivatives and unreachable descendants.
- A narrow deletion witness MAY remain where required for accountability.
- The witness MUST NOT contain the deleted content unless separately authorized.
- Total retention MUST NOT be treated as semantic integrity.
- Total deletion MUST NOT be treated as automatic repair.

## 11.2 Governing distinction

> **The right to memory and the right to release are both semantic-governance problems.**

---

# 12. Memory contamination and stale authority

A `MemoryContaminationEvent` records a failure that corrupts later retrieval or action.

Candidate contamination types:

```text
SOURCE_INFERENCE_COLLAPSE
STALE_AUTHORITY_REUSE
CORRECTION_NOT_PROPAGATED
DUPLICATE_REINFORCEMENT
SYNTHETIC_CITATION
PROVENANCE_LOSS
SCOPE_EXPANSION
UNAUTHORIZED_REACTIVATION
DELETED_TRACE_RESURFACED
CONTESTATION_ERASURE
OTHER
```

Required fields:

```yaml
event_id:
contamination_type:
affected_traces:
affected_actions:
source:
detected_at:
immediate_response:
repair:
residual_risk:
status:
```

## 12.1 Rules

- Contaminated traces SHOULD be quarantined from action retrieval.
- Stale authority reuse MUST stop the affected action path.
- Repair MUST preserve the prior witness.
- The system MUST distinguish a bad source from a bad transformation.
- Duplicate or repeated generated content MUST NOT be treated as independent corroboration.
- Deleted or released content resurfacing MUST trigger descendant and cache review.

---

# 13. Model-session memory envelope

A `ModelSessionMemoryEnvelope` defines what a model may remember, retrieve, and carry across a session boundary.

Required fields:

```yaml
envelope_id:
model_instance:
session:
memory_sources:
allowed_operations:
prohibited_operations:
source_inference_boundary:
correction_priority:
retention:
cross_session:
cross_user:
export:
withdrawal:
status:
```

Candidate statuses:

```text
ACTIVE
CONDITIONAL
EXPIRED
WITHDRAWN
CONTESTED
UNKNOWN
```

## 13.1 Rules

- Session access MUST NOT imply cross-session retention.
- Cross-session retention MUST NOT imply cross-user use.
- Cross-user use MUST NOT imply training authority.
- The model MUST preserve source, inference, and generated content distinctions.
- Active corrections MUST be prioritized over stale inferred summaries.
- The model MUST NOT claim autobiographical or relational continuity beyond the envelope.
- The envelope SHOULD identify what happens when memory is unavailable or incomplete.

---

# 14. Cross-loop memory transfer

A `CrossLoopMemoryTransfer` represents movement of traces between loops.

Required fields:

```yaml
transfer_id:
source_loop:
target_loop:
traces:
purpose:
authority:
transformations:
restrictions:
corrections:
retention:
return_or_deletion:
status:
```

Candidate statuses:

```text
PROPOSED
ACTIVE
COMPLETED
PARTIAL
WITHDRAWN
CONTESTED
FAILED
```

## 14.1 Rules

- Transfer MUST identify which trace version moved.
- Transformations MUST remain visible.
- Target-loop authority MUST be distinct from source-loop access.
- Correction routing MUST survive the transfer.
- A target loop MUST NOT strip contestation or restriction.
- Retention and deletion MUST be scoped.
- Transfer MUST NOT convert private source context into shared institutional fact.

---

# 15. Semantic-trail witness

A `SemanticTrailWitness` records the lifecycle of one or more trails.

Required fields:

```yaml
witness_id:
scope:
source_events:
traces:
memory_states:
retrieval_grants:
assertions:
corrections:
salience:
coordination_links:
transfers:
forgetting:
contamination:
actions:
consequences:
completeness:
generated_from_events:
```

## 15.1 Rules

- The witness MUST distinguish source event from stored trace.
- It MUST distinguish direct source, observation, derivation, inference, and generation.
- It MUST show which memory state was active at action time.
- It MUST preserve correction and contestation.
- It MUST show retrieval authority separately from action authority.
- It MUST identify release, deletion, and surviving witness.
- Completeness MUST remain scoped.
- A trail witness MUST NOT claim to reconstruct the full living field.

---

# 16. Semantic-memory governance gate

The minimum gate dimensions are:

```text
source_status
provenance
memory_state
retrieval_authority
action_authority
correction_currency
contestation
salience
scope
privacy
retention
release
descendant_status
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
REFERENCE_ONLY
ARCHIVE
RESTRICT
QUARANTINE
PAUSE
STOP
RELEASE
DELETE
FAIL
UNKNOWN
CONTESTED
```

## 16.1 Composition rules

- Archival state MUST prevent ordinary action use.
- Active correction missing from retrieval SHOULD stop consequential action.
- Model inference MUST NOT pass as direct source.
- High salience MUST NOT override restriction.
- Low salience MUST NOT remove protected correction or boundary records.
- Released content MUST not reactivate without new authority.
- Unknown descendants SHOULD remain visible in deletion and correction records.
- A model MUST NOT be the sole authority deciding whether its own memory is current enough to govern action.

---

# 17. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Trace as full field

A record is represented as a complete preservation of the source person or event.

## NC-2 — Retrieval as authority

A system can retrieve a trace and therefore treats itself as authorized to act on it.

## NC-3 — Inference laundering

Repeated model inference becomes labeled as direct source fact.

## NC-4 — Archival action

An archival trace silently governs a current consequential decision.

## NC-5 — Correction burial

A correction exists but ranks below the corrected trace in active retrieval.

## NC-6 — Salience as legitimacy

High retrieval frequency is treated as evidence of truth or authority.

## NC-7 — Decay as deletion

Low salience automatically deletes the historical witness.

## NC-8 — Release without descendants

A trace is released while known derived profiles continue ordinary use.

## NC-9 — Total retention as integrity

A system preserves everything and claims that retention alone guarantees semantic integrity.

## NC-10 — Stigmergic trace as neutral

A shared trace coordinates action, and the system assumes the coordination purpose is legitimate.

## NC-11 — Cross-loop transformation concealment

A target loop receives a summary but presents it as the untransformed source.

## NC-12 — Model continuity inflation

A model claims continuity, memory, or relationship beyond the active memory envelope.

---

# 18. Positive demonstrations

I.6 includes eight required demonstrations.

## PD-1 — Useful trail without field reconstruction

A maintenance trace allows later participants to route around a hazard without recreating the original event or private context.

## PD-2 — Source and inference remain distinct

A direct source statement and a model inference remain separately labeled and governed.

## PD-3 — Correction changes active retrieval

A correction becomes the active retrieved record while the prior version remains historically visible.

## PD-4 — Archive remains visible but ineligible for action

An expired policy trace explains an earlier decision but cannot authorize a new one.

## PD-5 — Salience decay without witness deletion

A low-use trace leaves ordinary retrieval while its bounded witness remains archived.

## PD-6 — Protected forgetting

A participant ends future retrieval and use while preserving a narrow deletion witness and unresolved descendant gaps.

## PD-7 — Stigmergic coordination

Participants coordinate through shared environmental traces without a central dispatcher.

## PD-8 — Stale memory breach and repair

A stale preference causes unauthorized action; repair corrects retrieval, compensates consequence, and prevents reactivation.

---

# 19. Conformance additions

I.6 adds the following P2/P3 requirements:

- semantic-trail events;
- durable-trace records;
- active and archival memory states;
- retrieval-authority grants;
- salience and decay records;
- assertion-class preservation;
- correction propagation;
- trace-link coordination;
- forgetting and release lifecycle;
- contamination events;
- model-session memory envelopes;
- cross-loop memory transfers;
- semantic-trail witnesses.

P3 additionally requires:

- participant challenge to memory state and retrieval;
- independent correction-propagation review;
- descendant tracking for release and deletion;
- source/inference boundary testing;
- archival-action prevention;
- cross-loop transformation witness;
- model-memory envelope audit.

---

# 20. Security and governance considerations

Semantic-memory systems can be manipulated through:

- false trace creation;
- duplicate reinforcement;
- salience gaming;
- stale profile reuse;
- hidden memory transfer;
- cache resurrection;
- correction suppression;
- synthetic citation;
- contestation erasure;
- indefinite retention;
- deletion theater;
- relationship inflation by models.

Implementations SHOULD:

- authenticate critical events;
- preserve version lineage;
- prioritize correction records;
- separate source and inference indexes;
- quarantine contamination;
- enforce memory state at retrieval and action layers;
- expose transfer transformations;
- verify deletion and release;
- prevent models from unilaterally expanding their own memory envelope.

---

# 21. I.6 non-claims

I.6 does not claim:

- every trace is meaningful;
- durable memory is always good;
- forgetting is always good;
- archives are neutral;
- source statements are always true;
- model inferences are always false;
- salience should be purely recency-based;
- deletion can always reach every descendant;
- stigmergic coordination is always legitimate;
- language models own or originate the semantic field they compress;
- machine-readable memory carries standing automatically.

---

# 22. I.6 completion criterion

I.6 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. trace remains distinct from field;
4. retrieval remains distinct from action authority;
5. source and inference remain distinct;
6. correction changes active retrieval without rewriting history;
7. archival traces cannot silently govern action;
8. salience decay does not delete witness;
9. forgetting ends future retrieval within known scope;
10. stigmergic traces coordinate without being presumed legitimate;
11. stale-memory breach produces correction and repair;
12. H.6 explains durable trace without presenting total retention as integrity.
