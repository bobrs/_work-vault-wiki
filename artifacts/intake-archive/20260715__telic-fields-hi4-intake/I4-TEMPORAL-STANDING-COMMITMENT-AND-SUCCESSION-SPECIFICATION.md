---
title: "I.4 — Temporal Standing, Commitment, and Succession Specification"
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
  - "F.6 — Temporal Telic Relations"
  - "G.7 — Time, Identity, Commitment, and Future Standing"
---

# I.4 — Temporal Standing, Commitment, and Succession Specification

## 1. Purpose

I.4 defines how a Telic Field system represents authority, standing, commitment, consent, possibility, obligation, and repair across time.

Its governing rule is:

> **The present may govern the next action. It does not own every condition that later states and successors will inherit.**

Temporal governance is required whenever:

- a present action closes a later option;
- an earlier promise recruits future action;
- consent persists across changing context;
- authority expires;
- a projection becomes stale;
- a successor inherits assets, obligations, or records;
- an irreversible consequence crosses beyond the current decision window;
- release or repair must preserve history without preserving obsolete authority.

I.4 defines:

- temporal centers;
- continuity relations;
- commitment records;
- versioned consent and authority;
- future-standing assessments;
- irreversibility and option-preservation profiles;
- commitment review and release;
- stale-projection and expired-authority events;
- temporal breach and repair;
- succession and inherited-obligation records;
- bitemporal witness views.

---

# 2. Normative scope

I.4 defines:

- `TemporalCenterReference`;
- `ContinuityRelation`;
- `CommitmentRecord`;
- `TemporalConsentAuthorityRecord`;
- `FutureStandingAssessment`;
- `IrreversibilityOptionProfile`;
- `CommitmentReviewReleaseRecord`;
- `TemporalStateChangeEvent`;
- `TemporalBreachRepairRecord`;
- `SuccessionObligationRecord`;
- `TemporalDecisionWitness`.

I.4 does not define:

- a metaphysical theory of personal identity;
- legal personhood for future selves;
- present consent by future generations;
- one universal discount rate;
- one rule for advance directives;
- one mandatory succession law;
- automatic obligation inheritance;
- permanent authority for earlier commitments;
- complete reversibility of past consequences.

---

# 3. Temporal centers

A `TemporalCenterReference` identifies a materially relevant state of a person, institution, role, community, system, or condition at a particular time or interval.

Minimum fields:

```yaml
temporal_center_id:
base_center:
center_type:
time_position:
valid_time:
representation_status:
standing_type:
continuity_claim:
```

Candidate time positions:

```text
EARLIER
PRESENT
LATER
SUCCESSOR
ANCESTOR
CONTEMPORARY
UNKNOWN
```

Candidate representation statuses:

```text
DIRECT
PRIOR_DIRECT
DELEGATED
REPRESENTED
PROJECTED
ABSENT
CONTESTED
UNKNOWN
```

## 3.1 Rules

- A later temporal center MAY have represented standing.
- A later temporal center MUST NOT be recorded as presently consenting unless an actual consent event exists.
- An earlier temporal center MAY remain the source of a valid commitment or directive.
- Earlier source authority MUST be tested against present scope, context, validity, and review.
- A temporal center is a governance reference, not necessarily a separate person.

---

# 4. Continuity relation

A `ContinuityRelation` states why consequences, commitments, obligations, or authority may travel between temporal centers.

Potential continuity carriers include:

```text
embodiment
legal_identity
role
record
contract
causal_history
delegation
organizational_lineage
property
relationship
public_mandate
cryptographic_control
social_recognition
```

Required fields:

```yaml
continuity_id:
from_center:
to_center:
carriers:
scope:
strength:
contested:
authority_effect:
obligation_effect:
review:
```

Candidate strength values:

```text
STRONG
PARTIAL
CONDITIONAL
WEAK
BROKEN
UNKNOWN
CONTESTED
```

## 4.1 Rules

- Continuity MUST be scoped.
- Continuity of assets does not automatically imply continuity of every authority.
- Continuity of identity does not imply unchanged preference.
- Broken continuity MAY end authority while leaving consequence or obligation.
- A system MUST identify which carrier supports each inherited claim.
- Persistence alone MUST NOT be treated as proof of legitimate continuity.

---

# 5. Commitment record

A `CommitmentRecord` represents a bounded recruitment of future action by an earlier decision.

Minimum fields:

```yaml
commitment_id:
committing_center:
beneficiaries:
affected_future_centers:
commitment_type:
expression:
scope:
formation_authority:
valid_time:
review_triggers:
release_conditions:
reliance:
residual_obligations:
status:
```

Candidate commitment types:

```text
PROMISE
CONTRACT
PLAN
DIRECTIVE
DELEGATION
POLICY
ROLE_DUTY
FIDUCIARY_DUTY
PUBLIC_COMMITMENT
SELF_COMMITMENT
OTHER
```

Candidate statuses:

```text
PROPOSED
ACTIVE
CONDITIONAL
DUE_FOR_REVIEW
CONTESTED
BREACHED
PARTIALLY_FULFILLED
FULFILLED
RELEASED
EXPIRED
SUPERSEDED
DISSOLVED
```

## 5.1 Commitment authority

A commitment MAY bind later action only where:

- formation authority was valid;
- scope remains applicable;
- affected standing was represented adequately;
- reliance and consequence remain visible;
- review and release rules remain available;
- no stronger protected condition or current authority invalidates the action.

## 5.2 Governing distinction

> **Commitment gives the past a voice. It does not make the past sovereign.**

---

# 6. Versioned consent and authority

A `TemporalConsentAuthorityRecord` represents the temporal lifecycle of consent or another authority basis.

Required fields:

```yaml
record_id:
record_type:
source_center:
basis:
operation:
scope:
version:
valid_time:
transaction_time:
state:
renewal:
withdrawal:
surviving_obligations:
historical_effect:
```

Candidate record types:

```text
CONSENT
DELEGATED_AUTHORITY
CONTRACTUAL_AUTHORITY
PUBLIC_AUTHORITY
FIDUCIARY_AUTHORITY
EMERGENCY_AUTHORITY
OTHER_AUTHORITY
```

Candidate states:

```text
VALID_WHEN_GIVEN
ACTIVE
CONDITIONAL
STALE
EXPIRED
WITHDRAWN
SUPERSEDED
CONTESTED
INCAPACITY_TRIGGERED
UNKNOWN
```

## 6.1 Rules

- Consent MUST be versioned rather than overwritten.
- The current state MUST remain distinguishable from historical validity.
- `VALID_WHEN_GIVEN` does not imply `ACTIVE_NOW`.
- Expired or withdrawn authority MUST remain historically visible where proportionate.
- Expired authority MUST NOT authorize new action.
- Withdrawal MAY affect future use without erasing past reliance or consequence.
- Surviving obligations MUST be stated separately from surviving authority.

## 6.2 Governing distinction

> **Consent remembered is not necessarily consent renewed.**

---

# 7. Future-standing assessment

A `FutureStandingAssessment` represents how a present action affects later centers or conditions.

Minimum fields:

```yaml
assessment_id:
present_action:
future_centers:
represented_interests:
source_basis:
uncertainty:
possibilities_preserved:
possibilities_closed:
irreversible_effects:
temporary_effects:
protective_conditions:
review_path:
status:
```

Candidate statuses:

```text
ADEQUATELY_REPRESENTED
ADEQUATELY_REPRESENTED_WITH_CONDITIONS
MATERIAL_FUTURE_STANDING_MISSING
CONTESTED
UNKNOWN
```

## 7.1 Rules

- Future standing MUST NOT be represented as future consent.
- A present actor MAY estimate later interests but MUST mark the estimate as projection.
- The less correctable the future error, the more standing review is required.
- Present needs retain standing.
- The assessment MUST NOT assume that preserving all options is always preferable.
- Possibility preservation is action-specific and materiality-bound.

---

# 8. Irreversibility and option preservation

An `IrreversibilityOptionProfile` identifies how a route changes later possibility.

Required fields:

```yaml
profile_id:
action:
affected_centers:
reversibility:
rollback_window:
repairability:
possibilities_preserved:
possibilities_closed:
closure_duration:
closure_authority:
standing_review:
uncertainty:
status:
```

Candidate reversibility values:

```text
HIGHLY_REVERSIBLE
REVERSIBLE_WITH_COST
PARTIALLY_REVERSIBLE
PRACTICALLY_IRREVERSIBLE
IRREVERSIBLE
UNKNOWN
```

## 8.1 Rules

- Irreversibility MUST increase future-standing review.
- Option closure MUST identify who inherits the loss.
- A reversible trial SHOULD be preferred when future values are uncertain and learning is expected.
- Reversibility MUST NOT be used to excuse repeated harm.
- Repairability is distinct from technical rollback.
- A route that is technically reversible MAY remain socially or temporally irreversible.

---

# 9. Commitment review and release

A `CommitmentReviewReleaseRecord` evaluates whether a commitment should continue, narrow, renew, transfer, repair, or end.

Required fields:

```yaml
review_id:
commitment:
current_context:
changed_conditions:
current_standing:
reliance:
authority_status:
review_result:
release_effect:
transition:
residual_obligations:
witness:
```

Candidate review results:

```text
CONTINUE
CONTINUE_WITH_CONDITIONS
RENEW
NARROW
TRANSFER
PAUSE
REPAIR
RELEASE
DISSOLVE
CONTESTED
UNKNOWN
```

## 9.1 Rules

- Changed conditions SHOULD trigger review where material.
- Release MUST NOT erase historical consequence.
- Release MAY require notice, transition, compensation, transfer, or bounded completion.
- Reliance MUST NOT be fabricated to prevent legitimate exit.
- A commitment may cease to govern while gratitude, evidence, repair, or residual obligation remains.

## 9.2 Governing distinction

> **A telos may cease to govern without being erased from history.**

---

# 10. Temporal state-change events

A `TemporalStateChangeEvent` records changes to projection, authority, consent, commitment, obligation, or continuity.

Candidate event types:

```text
COMMITMENT_CREATED
COMMITMENT_RENEWED
COMMITMENT_NARROWED
COMMITMENT_RELEASED
COMMITMENT_BREACHED
CONSENT_EXPIRED
CONSENT_WITHDRAWN
AUTHORITY_EXPIRED
AUTHORITY_TRANSFERRED
PROJECTION_BECAME_STALE
PROJECTION_SUPERSEDED
FUTURE_STANDING_ADDED
OPTION_CLOSED
OPTION_REOPENED
SUCCESSOR_ASSIGNED
OBLIGATION_TRANSFERRED
LOOP_DISSOLVED
TEMPORAL_REPAIR_COMPLETED
```

Required fields:

```yaml
event_id:
event_type:
subject_record:
valid_at:
recorded_at:
agent:
authority:
prior_state:
new_state:
reason:
```

## 10.1 Stale projection rule

A projection becomes stale when:

- its valid interval ends;
- the source marks it outdated;
- changed conditions materially weaken it;
- a later direct statement supersedes it;
- its authority expires;
- its scope no longer matches the action.

A stale projection MAY remain historically relevant.

It MUST NOT silently govern new action.

---

# 11. Temporal breach and repair

A `TemporalBreachRepairRecord` represents a failure in temporal governance.

Candidate breach types:

```text
FUTURE_STANDING_BREACH
STALE_PROJECTION_BREACH
INHERITED_AUTHORITY_BREACH
CONSENT_PERSISTENCE_BREACH
SUCCESSION_BREACH
REVISION_ERASURE_BREACH
RELEASE_BREACH
PRESENT_ERASURE_BREACH
TEMPORAL_CAPTURE
OPTION_CLOSURE_BREACH
```

Required fields:

```yaml
breach_id:
breach_type:
affected_centers:
source_commitment_or_authority:
action:
consequence:
detected_at:
repair_options:
selected_repair:
repair_authority:
residual_harm:
status:
```

Candidate repairs:

```text
RESTORE_RECORD
CORRECT_PROJECTION
PAUSE_ACTION
REOPEN_OPTION
RENEW_CONSENT
RELEASE_OBLIGATION
TRANSFER_AUTHORITY
COMPENSATE
NOTIFY_SUCCESSOR
PRESERVE_RELIANCE
DOCUMENT_IRREVERSIBLE_LOSS
DISSOLVE
OTHER
```

## 11.1 Rules

- Repair MUST distinguish reversible state from irreversible loss.
- Repair MUST preserve the prior witness.
- Repair MAY include release rather than continuation.
- A breach may remain partially repaired.
- A later preference does not automatically erase another party's valid reliance.
- Earlier reliance does not automatically justify permanent captivity.

---

# 12. Succession and inherited obligation

A `SuccessionObligationRecord` represents what transfers when a person, office, institution, system, or loop changes holder or form.

Required fields:

```yaml
succession_id:
predecessor:
successor:
continuity_relation:
assets_transferred:
capabilities_transferred:
authority_transferred:
authority_not_transferred:
obligations_transferred:
obligations_under_review:
records_transferred:
records_restricted:
effective_at:
review:
status:
```

Candidate statuses:

```text
PROPOSED
ACTIVE
CONDITIONAL
CONTESTED
PARTIAL
COMPLETED
RELEASED
DISSOLVED
```

## 12.1 Rules

- A successor claiming continuity for benefit SHOULD identify attached obligations.
- Asset continuity MUST NOT imply unlimited authority continuity.
- Authority MUST be revalidated by operation and scope.
- Records MAY transfer with tighter access than the predecessor had.
- A successor MAY contest or seek release from obligations through a competent process.
- Dissolution MUST identify residual state, unresolved obligation, records, and repair routes.

## 12.2 Governing distinction

> **Succession is a constitutional transformation, not merely a change of personnel.**

---

# 13. Bitemporal decision witness

A `TemporalDecisionWitness` preserves both:

- what was valid in the represented world;
- what the system knew when it acted.

Required fields:

```yaml
witness_id:
decision:
event_range:
operative_records:
valid_time_view:
transaction_time_view:
commitments:
consent_and_authority:
future_standing:
irreversibility:
successor_effects:
selected_action:
consequence:
later_changes:
repairs:
completeness:
```

## 13.1 Rules

- A correction made later MUST NOT falsify what the system knew earlier.
- The witness MUST identify which version actually governed.
- The witness MUST identify authority state at action time.
- The witness MUST distinguish historical explanation from current eligibility.
- A present reader MUST be able to reconstruct why an action occurred and why the same action may no longer be allowed.

---

# 14. Temporal governance gate

The minimum temporal gate dimensions are:

```text
continuity
commitment_scope
authority_validity
consent_validity
future_standing
irreversibility
option_preservation
reliance
review_availability
succession
release
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
PAUSE
ESCALATE
FAIL
UNKNOWN
CONTESTED
```

## 14.1 Composition rules

- Expired authority MUST fail new action.
- Material future standing missing for irreversible action SHOULD pause or fail.
- Stale projection MUST NOT pass as current direct evidence.
- A valid commitment MAY pass only within scope.
- A successor MUST NOT use predecessor authority beyond the transferred operation.
- Lack of review or release SHOULD reduce authority for long-duration commitments.
- Present emergency needs MAY justify bounded temporary action with after-action review.

---

# 15. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Future standing as consent

A projected later interest is recorded as current consent.

## NC-2 — Persistence as legitimacy

A commitment remains active solely because the record still exists.

## NC-3 — Permanent commitment sovereignty

An earlier commitment binds later action without review, scope, or release.

## NC-4 — Historical rewrite

A later correction overwrites the version that governed an earlier action.

## NC-5 — Expired consent reuse

Expired consent authorizes a new use.

## NC-6 — Stale projection action

A stale preference is treated as current direct evidence.

## NC-7 — Asset-only succession

A successor claims assets while omitting attached obligations.

## NC-8 — Unlimited successor authority

A successor inherits every predecessor permission automatically.

## NC-9 — Irreversible option closure without standing

A present route permanently closes a future option without represented future standing.

## NC-10 — Present erasure

A speculative future interest automatically overrides urgent present standing.

## NC-11 — Release as erasure

A released commitment deletes past consequence and valid reliance.

## NC-12 — Repair as forced continuation

Repair requires preserving the loop even when dissolution is the legitimate outcome.

---

# 16. Positive demonstrations

I.4 includes eight required demonstrations.

## PD-1 — Present action preserves later option

A present decision uses a reversible trial rather than permanent closure.

## PD-2 — Valid commitment binds within scope

An active commitment governs a bounded action because formation authority, scope, and review remain valid.

## PD-3 — Changed conditions trigger review

Material context change moves a commitment to `DUE_FOR_REVIEW`.

## PD-4 — Stale projection loses authority

An earlier preference remains historically visible but becomes ineligible for new action.

## PD-5 — Consent expires without erasing witness

An earlier use remains historically authorized; a new use fails.

## PD-6 — Future standing blocks irreversible action

An irreversible route pauses because later affected standing is materially absent.

## PD-7 — Successor inherits obligation without unlimited authority

A successor receives assets, records, and defined obligations while predecessor execution authority is revalidated separately.

## PD-8 — Temporal breach produces repair or release

A stale projection breach results in correction, notification, option reopening, and partial release rather than forced continuation.

---

# 17. Conformance additions

I.4 adds the following P2/P3 requirements:

- temporal-center references;
- scoped continuity relations;
- commitment records;
- versioned consent and authority;
- future-standing assessment for materially future-affecting action;
- irreversibility and option-preservation profile;
- commitment review and release;
- stale-projection detection;
- temporal breach and repair;
- succession and inherited-obligation record;
- bitemporal decision witness.

P3 additionally requires:

- participant challenge to temporal standing and continuity;
- visible expiry and review;
- release path;
- successor contest and obligation review;
- repair records for irreversible loss;
- independent temporal witness export.

---

# 18. Security and governance considerations

Temporal systems can be manipulated through:

- fabricated future interests;
- stale profile reuse;
- automatic renewal;
- hidden expiry;
- commitment lock-in;
- emergency authority persistence;
- successor asset extraction;
- erased reliance;
- irreversible option closure;
- speculative paternalism.

Implementations SHOULD:

- require version and valid time;
- mark projection source and staleness;
- authenticate renewal and withdrawal;
- expose review triggers;
- preserve present standing;
- require stronger authority for irreversible closure;
- distinguish assets, obligations, and authority in succession;
- allow release and dissolution;
- prevent the acting system from declaring its own continuity sufficient.

---

# 19. I.4 non-claims

I.4 does not claim:

- future selves are separate legal persons;
- future generations presently consent;
- earlier commitments always outrank later welfare;
- later preferences automatically erase reliance;
- every action should preserve every option;
- every commitment should be freely reversible without consequence;
- identity requires sameness;
- succession carries every predecessor power;
- institutional continuity is always desirable;
- temporal standing resolves population ethics or advance-directive conflict.

---

# 20. I.4 completion criterion

I.4 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. future standing remains distinct from consent;
4. valid commitment binds only within scope;
5. changed context triggers review;
6. stale projection loses action authority;
7. expired consent cannot authorize new use;
8. irreversible action pauses when future standing is materially absent;
9. successor obligations and authority remain separate;
10. temporal breach supports repair or release;
11. H.4 explains continuity without sameness and revision without betrayal.
