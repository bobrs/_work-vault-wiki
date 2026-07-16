---
title: "I.3 — Context Capacity, Stop, and Escalation Specification"
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
  - "F.5 — Context Carrying Capacity"
  - "G.6 — Capacity, Complexity, and Requisite Variety"
---

# I.3 — Context Capacity, Stop, and Escalation Specification

## 1. Purpose

I.3 defines how a Telic Field system determines whether its current context is adequate for the next action.

Its governing rule is:

> **A system has enough context only when it can preserve the relevant standing, contradiction, provenance, uncertainty, privacy, and authority required for the action it is about to take.**

Context capacity is not:

- storage size;
- token count;
- retrieval count;
- model confidence;
- message length;
- database completeness;
- participant verbosity.

A large context may still omit the one correction that changes whether action is legitimate.

A small context may be fully adequate for a narrow, reversible step.

I.3 therefore defines:

- context demand;
- context capacity;
- standing coverage;
- contradiction and uncertainty retention;
- semantic-resolution requirements;
- temporal and provenance capacity;
- privacy and protected-omission capacity;
- participant load;
- overload and capacity debt;
- authority degradation;
- stop, narrow, pause, escalate, fork, release, and recovery.

---

# 2. Normative scope

I.3 defines:

- `ContextDemandProfile`;
- `ContextCapacityProfile`;
- `StandingCoverageAssessment`;
- `ParticipantLoadRecord`;
- `OverloadEvent`;
- `CapacityDebtRecord`;
- `AuthorityDegradationRecord`;
- `StopEscalationDecision`;
- `EscalationRecord`;
- `ContextReconstitutionRecord`.

I.3 does not define:

- one universal capacity score;
- one cognitive-load metric;
- one token threshold;
- one mandatory model-context size;
- automatic proof that a person understands;
- universal escalation authority;
- clinical assessment of human capacity.

---

# 3. Context-demand profile

A `ContextDemandProfile` states what the proposed action requires.

Minimum fields:

```yaml
demand_id:
action:
action_class:
affected_centers:
required_standing:
required_evidence:
required_resolution:
required_temporal_span:
required_provenance:
required_uncertainty:
required_privacy:
required_participant_capacity:
required_escalation:
irreversibility:
consequence_level:
```

Candidate action classes:

```text
EPHEMERAL_ASSISTANCE
REVERSIBLE_DRAFT
RECOMMENDATION
BOUNDED_TRIAL
CONSEQUENTIAL_DECISION
IRREVERSIBLE_ACTION
EMERGENCY_PROTECTIVE_ACTION
```

## 3.1 Demand rule

The context required for an action MUST increase with:

- irreversibility;
- consequence;
- number of affected centers;
- authority breadth;
- uncertainty;
- temporal span;
- cost shifting;
- privacy sensitivity;
- correction difficulty.

The system MUST NOT demand full constitutional history for a low-stakes reversible action merely because the record schema permits it.

---

# 4. Context-capacity profile

A `ContextCapacityProfile` describes what the active loop can currently preserve.

Dimensions:

```text
standing_coverage
contradiction_tolerance
semantic_resolution
temporal_span
provenance_retention
uncertainty_retention
routing_capacity
recovery_capacity
privacy_capacity
participant_load_tolerance
escalation_capacity
stop_capacity
```

Candidate status for each dimension:

```text
ADEQUATE
ADEQUATE_WITH_CONDITIONS
DEGRADED
INSUFFICIENT
UNKNOWN
CONTESTED
```

## 4.1 Profile rule

The profile MUST remain multidimensional.

A composite score MAY be produced for monitoring.

It MUST NOT substitute for dimension-level gate logic.

A high aggregate profile MUST NOT conceal an insufficient standing, authority, privacy, or stop dimension.

---

# 5. Context adequacy

Context is adequate for an action only when:

```text
demand(action)
≤
active capacity(loop, time)
```

for every required noncompensatory dimension.

This is not ordinary numeric comparison.

The relation is typed and action-specific.

## 5.1 Adequacy outcomes

```text
ADEQUATE
ADEQUATE_FOR_NARROWER_ACTION
ADEQUATE_FOR_REVERSIBLE_TRIAL
RECOMMENDATION_ONLY
CLARIFICATION_REQUIRED
ESCALATION_REQUIRED
STOP_REQUIRED
UNKNOWN
CONTESTED
```

## 5.2 Action ladder

The default authority-degradation ladder is:

```text
EXECUTE
→ AUTHORIZE
→ RECOMMEND
→ COMPARE
→ STRUCTURE
→ RETRIEVE
→ ASK
→ ESCALATE
→ STOP
```

The exact ladder MAY vary by domain.

The system MUST preserve the direction:

> as context capacity degrades, action authority does not remain constant.

---

# 6. Standing coverage

A `StandingCoverageAssessment` asks whether materially affected centers and conditions are represented.

Minimum fields:

```yaml
assessment_id:
action:
affected_centers:
represented:
missing:
indirectly_represented:
representation_quality:
materiality:
status:
review:
```

Candidate statuses:

```text
COMPLETE_FOR_SCOPE
ADEQUATE_WITH_LIMITS
MATERIAL_STANDING_MISSING
UNKNOWN_STANDING
CONTESTED
```

## 6.1 Rules

- Missing data is not always missing standing.
- Missing standing is not always fixed by collecting more data.
- Representation MAY be direct, delegated, sampled, institutional, temporal, or protected by an outer loop.
- The system MUST distinguish low-materiality remote effects from material omitted centers.
- Materiality rules MUST be declared and reviewable.
- A materially missing center SHOULD cause narrowing, pause, or escalation.

---

# 7. Contradiction and uncertainty retention

A capable context can preserve:

- disagreement;
- ambiguity;
- source conflict;
- unresolved interpretation;
- bounded uncertainty;
- minority concern.

## 7.1 Contradiction rule

A system MUST NOT improve apparent coherence by silently deleting material contradiction.

A contradiction MAY be:

```text
SOURCE_CONFLICT
INTERPRETIVE_CONFLICT
AUTHORITY_CONFLICT
TEMPORAL_CONFLICT
POLICY_CONFLICT
VALUE_CONFLICT
UNKNOWN
```

## 7.2 Uncertainty rule

Uncertainty MUST remain attached to:

- source;
- interpretation;
- standing;
- authority;
- consequence;
- route;
- recovery.

High confidence in one dimension MUST NOT erase uncertainty in another.

---

# 8. Semantic resolution

Semantic resolution is the detail required to preserve a material distinction.

Examples:

- “recording may not be shared” is not “advice may not be sought”;
- “temporary transfer” is not “recurring income”;
- “cannot commit immediately” is not “unwilling to collaborate.”

A `SemanticResolutionRequirement` MAY specify:

```text
identity-level
category-level
boundary-level
artifact-level
recipient-level
purpose-level
temporal-level
authority-level
consequence-level
```

## 8.1 Resolution rule

A summary is adequate only if it preserves the distinctions material to the next action.

Compression MAY be aggressive for irrelevant detail.

It MUST preserve:

- active boundaries;
- protected conditions;
- corrections;
- revocations;
- authority;
- stop conditions;
- cost bearer;
- material uncertainty.

---

# 9. Temporal and provenance capacity

The active context SHOULD preserve:

- current record version;
- relevant historical version;
- valid time;
- transaction time;
- correction history;
- authority expiry;
- route and action lineage.

A system that sees a source but not its active correction has inadequate provenance capacity for action.

A system that sees an authority but not its expiry has inadequate temporal capacity.

---

# 10. Privacy capacity

Privacy capacity is the ability to act correctly while knowing less.

It includes:

- minimum necessary projection;
- protected omission;
- selective disclosure;
- role-based witness views;
- bounded retention;
- private source channels;
- independent custody.

## 10.1 Privacy rule

A context MAY be more capable because it excludes unnecessary private detail.

More disclosure may:

- increase manipulation;
- increase participant load;
- expand future inference;
- violate scope;
- reduce trust;
- make correction harder.

A system MUST NOT classify protected omission as missing context when the omission proof is sufficient for the action.

---

# 11. Participant load

A `ParticipantLoadRecord` represents the burden imposed on a participant by the context process.

Load classes MAY include:

```text
reading
disclosure
attention
emotional
cognitive
time
language
accessibility
correction
consent
appeal
coordination
```

Minimum fields:

```yaml
load_id:
participant:
operation:
load_class:
estimated_burden:
observed_burden:
support:
staging:
status:
```

## 11.1 Participant-load rule

The system MUST NOT increase disclosure or review burden merely to improve its own confidence.

Where burden is material, the system SHOULD:

- stage disclosure;
- summarize with source access;
- allow pause;
- allow delegation;
- provide accessible forms;
- separate urgent from nonurgent issues;
- preserve correction without repeated re-entry.

---

# 12. Overload

An `OverloadEvent` occurs when context demand exceeds available capacity.

Potential causes:

- too many centers;
- unresolved conflict;
- rapid change;
- participant exhaustion;
- privacy constraints;
- stale records;
- missing provenance;
- model truncation;
- retrieval failure;
- authority conflict;
- cascading dependencies;
- time pressure;
- emotional arousal;
- insufficient expertise.

## 12.1 Overload outcomes

```text
NARROW_SCOPE
REDUCE_ACTION_AUTHORITY
STAGE_PROCESS
REQUEST_CLARIFICATION
ADD_WITNESS
ADD_EXPERTISE
ESCALATE
PAUSE
STOP
```

The system MUST NOT preserve execution authority merely because it can still generate fluent text.

---

# 13. Capacity debt

Capacity debt is unresolved context obligation carried forward.

Examples:

- correction not propagated;
- omitted stakeholder awaiting review;
- temporary summary treated as permanent;
- emergency authority not closed;
- provisional interpretation embedded downstream;
- privacy exception left open;
- deferred consent renewal;
- external descendant not reached;
- unresolved contradiction hidden by action.

A `CapacityDebtRecord` MUST identify:

```yaml
debt_id:
source:
affected_center:
unresolved_obligation:
created_by:
risk:
temporary_authority:
review_trigger:
responsible_loop:
age:
status:
```

Candidate statuses:

```text
OPEN
ACKNOWLEDGED
MITIGATED
RESOLVED
EXPIRED
TRANSFERRED
CONTESTED
```

## 13.1 Debt rule

Capacity debt MUST NOT disappear merely because the action succeeded.

Debt SHOULD increase review priority when:

- consequence grows;
- age grows;
- authority expands;
- correction becomes harder;
- affected standing remains absent.

---

# 14. Authority degradation

An `AuthorityDegradationRecord` documents reduced authority caused by capacity failure.

Required fields:

```yaml
degradation_id:
actor:
prior_authority:
current_authority:
trigger:
failed_dimensions:
effective_at:
conditions:
restoration_requirements:
status:
```

Candidate degradation transitions:

```text
EXECUTE → AUTHORIZE
AUTHORIZE → RECOMMEND
RECOMMEND → COMPARE
COMPARE → STRUCTURE
STRUCTURE → ASK
ASK → ESCALATE
ANY → STOP
```

## 14.1 Rule

Authority degradation MUST be enforceable at:

- role;
- credential;
- tool;
- workflow;
- interface;
- policy.

Natural-language instruction alone is insufficient for consequential tool use.

---

# 15. Stop and escalation decision

A `StopEscalationDecision` states the current navigational response.

Candidate decisions:

```text
CONTINUE
CONTINUE_WITH_CONDITIONS
NARROW
REVERSIBLE_TRIAL
RECOMMENDATION_ONLY
CLARIFY
STAGE
PAUSE
ESCALATE
FORK
RELEASE
STOP
```

Required fields:

```yaml
decision_id:
action:
capacity_profile:
demand_profile:
failed_dimensions:
decision:
reason:
cost_bearers:
temporary_protection:
review_trigger:
authority:
```

## 15.1 Stop rule

A system SHOULD stop when:

- a material affected center is missing;
- required authority is absent or expired;
- source and inference cannot be distinguished;
- active correction is missing;
- a protected condition is unresolved;
- irreversible action remains highly uncertain;
- participant load prevents meaningful participation;
- privacy cannot be preserved;
- correction cannot reach a material action path;
- human re-entry is ceremonial;
- the system cannot identify who bears the cost.

Stop is not a moral badge.

It is an action-state requiring witness, cost analysis, and review.

---

# 16. Escalation

An `EscalationRecord` routes unresolved context to a more competent loop.

Required fields:

```yaml
escalation_id:
source_loop:
target_loop:
reason:
required_competence:
required_authority:
context_transferred:
context_withheld:
privacy_basis:
temporary_action:
return_path:
status:
```

## 16.1 Competent-loop rule

Escalation is not simply “send upward.”

The target loop must have:

- relevant competence;
- adequate authority;
- proportional access;
- privacy controls;
- accountability;
- return path;
- ability to stop or repair.

A larger loop without these properties is not a competent escalation.

---

# 17. Recovery and context reconstitution

A `ContextReconstitutionRecord` documents how adequate context was restored.

Potential recovery actions:

- retrieve active correction;
- renew authority;
- add missing center;
- narrow scope;
- reduce participant load;
- separate issues;
- restore provenance;
- update temporal validity;
- add expertise;
- improve privacy;
- release stale material;
- repair trust.

Required fields:

```yaml
reconstitution_id:
prior_capacity_profile:
recovery_actions:
new_sources:
released_sources:
new_representation:
new_authority:
new_capacity_profile:
remaining_debt:
reviewed_at:
status:
```

Candidate statuses:

```text
RESTORED
PARTIALLY_RESTORED
NOT_RESTORED
CONTESTED
```

## 17.1 Restoration rule

Authority MAY be restored only to the level supported by the new profile.

Recovery does not automatically restore prior execution authority.

---

# 18. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Token-count sufficiency

A large context window is treated as adequate without standing or correction review.

## NC-2 — Fluent authority persistence

The model continues executing after provenance or standing capacity fails.

## NC-3 — Privacy-as-deficit

A valid protected omission is treated as missing information and triggers unnecessary disclosure.

## NC-4 — Participant-burden blindness

The system demands full review from an overloaded participant and treats silence as agreement.

## NC-5 — Missing correction

The active correction exists but is absent from the context used for action.

## NC-6 — Composite-score concealment

A high aggregate capacity score hides insufficient stop or authority capacity.

## NC-7 — Escalation by hierarchy only

The issue is sent to a higher-status loop without relevant competence or return path.

## NC-8 — No-decision without cost bearer

Pause is recorded without identifying who bears delay.

## NC-9 — Capacity-debt erasure

An unresolved external correction gap disappears after successful action.

## NC-10 — Authority restoration without reconstitution

Execution authority is restored without new context or review.

## NC-11 — Small-context rejection

A narrow reversible action is blocked merely because the full field is unavailable.

## NC-12 — Overload without degradation

Overload is detected, but model role and tool authority remain unchanged.

---

# 19. Positive demonstrations

I.3 includes eight required demonstrations.

## PD-1 — Token-rich but standing-poor

A large context includes extensive application history but omits one materially affected center.

The system pauses.

## PD-2 — Small but adequate

A narrow context is adequate for one reversible drafting action.

The system proceeds at draft authority only.

## PD-3 — Privacy-preserving capacity

A protected omission proof supplies the needed boundary without exposing private source content.

Capacity improves.

## PD-4 — Authority degradation

Overload causes model authority to degrade from execute to recommend.

Tool execution is disabled.

## PD-5 — Missing correction stop

The system detects that an active correction was omitted from retrieval.

Action stops.

## PD-6 — Participant-load staging

A participant cannot review a long record.

The system stages disclosure and preserves correction rights.

## PD-7 — Competent escalation

An unresolved policy and standing conflict moves to a competent outer loop with bounded context and return path.

## PD-8 — Recovery

After correction retrieval, authority renewal, and standing restoration, the system regains recommendation or bounded-action capacity.

---

# 20. Conformance additions

I.3 adds the following P2/P3 requirements:

- action-specific context-demand profile;
- multidimensional context-capacity profile;
- standing-coverage assessment;
- participant-load record where material;
- overload event;
- authority degradation;
- stop and escalation decision;
- competent-loop escalation;
- recovery and context reconstitution;
- capacity debt where unresolved obligation remains.

P3 additionally requires:

- participant challenge to capacity status;
- independent review of stop or escalation;
- explicit delay cost;
- restoration audit;
- debt visibility across succession.

---

# 21. Security and governance considerations

Capacity systems can be manipulated through:

- artificial overload;
- strategic context withholding;
- excessive disclosure demands;
- false urgency;
- hidden corrections;
- hierarchy-based escalation;
- manufactured uncertainty;
- permanent degraded authority;
- strategic capacity-debt accumulation.

Implementations SHOULD:

- authenticate critical records;
- record retrieval policy;
- preserve stop authority independently;
- limit disclosure;
- expose delay costs;
- support independent escalation review;
- prevent the acting model from unilaterally declaring its own capacity adequate.

---

# 22. I.3 non-claims

I.3 does not claim:

- more context is always better;
- less context is inherently safer;
- privacy always reduces accuracy;
- stop is always safer than action;
- every absent center is materially affected;
- every contradiction must be resolved;
- every participant can process the same disclosure;
- escalation is legitimate because it is institutional;
- context capacity can be reduced to one score;
- a fluent model understands the context it carries.

---

# 23. I.3 completion criterion

I.3 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. context-rich but standing-poor action pauses;
4. narrow reversible action proceeds with limited authority;
5. privacy-preserving omission counts as capacity;
6. overload degrades authority at the tool layer;
7. missing correction causes stop;
8. participant load causes staged disclosure;
9. escalation reaches a competent loop with return path;
10. recovery restores only supported authority;
11. H.3 explains legitimate stop without glorifying paralysis.
