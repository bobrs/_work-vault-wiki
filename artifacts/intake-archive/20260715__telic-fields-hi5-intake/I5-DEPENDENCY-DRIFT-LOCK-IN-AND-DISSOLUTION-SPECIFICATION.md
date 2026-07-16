---
title: "I.5 — Dependency, Drift, Lock-In, and Dissolution Specification"
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
  - "F.7 — Dependent Loops and Telic Incompatibility"
  - "G.8 — Transplantation, Lock-In, Drift, and Dissolution Review"
---

# I.5 — Dependency, Drift, Lock-In, and Dissolution Specification

## 1. Purpose

I.5 defines how a Telic Field system represents the support relationships that allow a loop to exist, persist, change purpose, capture its substrate, fork, or end.

Its governing rule is:

> **No derived loop is self-grounding.**

Every loop depends on support it does not fully generate for itself.

That support may include:

- labor;
- attention;
- care;
- data;
- money;
- legitimacy;
- physical infrastructure;
- legal authority;
- energy;
- correction;
- social recognition;
- technical maintenance;
- risk bearing;
- repair;
- exit capacity.

Dependence is not inherently illegitimate.

A legitimate dependency makes support, authority, burden, reciprocity, review, correction, and exit visible.

Dependence becomes dangerous when a loop treats continued support as proof of consent, hides the burden required to keep it alive, changes purpose without renewing authority, prevents exit, or survives after the substrate that made it coherent has disappeared.

I.5 defines:

- supporting-loop references;
- dependent-loop records;
- substrate-contribution maps;
- support and authority grants;
- support-burden records;
- hidden-recruitment events;
- telic-compatibility and transplant assessments;
- mission, value, and authority drift;
- lock-in and capture profiles;
- fork and exit records;
- dissolution and residual-state records;
- dependency witnesses.

---

# 2. Normative scope

I.5 defines:

- `SupportingLoopReference`;
- `DependentLoopRecord`;
- `SubstrateContributionMap`;
- `SupportAuthorityGrant`;
- `SupportBurdenRecord`;
- `HiddenRecruitmentEvent`;
- `TelicCompatibilityAssessment`;
- `DriftRecord`;
- `LockInCaptureProfile`;
- `ForkExitRecord`;
- `DissolutionResidualStateRecord`;
- `DependencyWitness`.

I.5 does not define:

- a universal theory of organizational failure;
- a clinical diagnosis of dependency;
- a biological theory of graft rejection;
- one ideal organizational form;
- one mandatory mission statement;
- one scalar measure of compatibility;
- automatic proof that persistence is illegitimate;
- automatic proof that dissolution is preferable;
- a universal legal dissolution process.

---

# 3. Supporting loops

A `SupportingLoopReference` identifies a loop that supplies a material contribution to another loop.

Minimum fields:

```yaml
supporting_loop_id:
center:
loop_type:
standing:
contribution_classes:
authority_source:
consent_or_governance_basis:
review:
exit:
status:
```

Candidate loop types:

```text
PERSON
TEAM
HOUSEHOLD
COMMUNITY
INSTITUTION
MARKET
PUBLIC_AUTHORITY
TECHNICAL_SYSTEM
ECOLOGICAL_SYSTEM
FUNDING_LOOP
DATA_SOURCE
MAINTENANCE_LOOP
OTHER
```

Candidate contribution classes:

```text
LABOR
ATTENTION
CARE
DATA
MONEY
LEGITIMACY
AUTHORITY
INFRASTRUCTURE
ENERGY
CORRECTION
RISK
REPAIR
REPUTATION
ACCESS
STORAGE
COMPUTE
GOVERNANCE
OTHER
```

## 3.1 Rules

- A supporting loop MUST remain distinguishable from the dependent loop it supports.
- The supporting loop's continued contribution MUST NOT be presumed from historical participation alone.
- A supporting loop MAY support several dependent loops.
- A supporting loop MAY withdraw, narrow, transfer, or condition support.
- A support relationship MUST identify who has authority to alter it.
- A dependent loop MUST NOT describe support as internally generated when it is materially external.

---

# 4. Dependent-loop record

A `DependentLoopRecord` represents a loop whose continued operation relies on one or more supporting loops.

Required fields:

```yaml
dependent_loop_id:
purpose:
declared_beneficiaries:
affected_centers:
supporting_loops:
required_contributions:
authority_to_recruit_support:
reciprocity:
review:
exit:
correction:
status:
```

Candidate statuses:

```text
PROPOSED
ACTIVE
CONDITIONAL
UNDER_REVIEW
DRIFTED
CAPTURED
FORKING
DISSOLVING
DISSOLVED
RELEASED
CONTESTED
UNKNOWN
```

## 4.1 Rules

- A dependent loop MUST identify the contributions required for its operation.
- It MUST identify which contributions are volunteered, contracted, mandated, delegated, inherited, or unknown.
- It MUST distinguish operation from legitimacy.
- It MUST expose the authority by which support is recruited.
- It SHOULD identify how contributors can correct, refuse, reduce, or leave.
- It MUST NOT treat contributor dependence on the loop as proof of free consent.

---

# 5. Substrate-contribution map

A `SubstrateContributionMap` records what keeps a loop alive.

Required fields:

```yaml
map_id:
dependent_loop:
contributions:
  - supporting_loop:
    contribution_class:
    quantity_or_scope:
    criticality:
    visibility:
    authority:
    reciprocity:
    substitutability:
    withdrawal_effect:
    correction_route:
status:
```

Candidate criticality values:

```text
NONCRITICAL
IMPORTANT
CRITICAL
SINGLE_POINT_OF_FAILURE
UNKNOWN
```

Candidate visibility values:

```text
VISIBLE
PARTLY_VISIBLE
HIDDEN
MISATTRIBUTED
UNKNOWN
```

## 5.1 Rules

- A material hidden contribution MUST be surfaced before high-consequence governance.
- A contribution SHOULD identify who bears maintenance and repair.
- Substitutability MUST NOT be used to erase the standing of the current contributor.
- A single point of failure SHOULD trigger review of dependency concentration.
- A system SHOULD distinguish technical replaceability from relational or constitutional replaceability.

---

# 6. Support and authority grant

A `SupportAuthorityGrant` represents the authority under which a dependent loop may recruit a contribution.

Required fields:

```yaml
grant_id:
supporting_loop:
dependent_loop:
contribution:
basis:
scope:
valid_time:
burden_limit:
reciprocity:
review:
withdrawal:
transfer:
status:
```

Candidate bases:

```text
CONSENT
CONTRACT
EMPLOYMENT
PUBLIC_MANDATE
FIDUCIARY_DUTY
COMMUNITY_GOVERNANCE
LICENSE
OWNERSHIP
EMERGENCY
INHERITED_OBLIGATION
OTHER_LAWFUL_BASIS
UNKNOWN
CONTESTED
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
BREACHED
UNKNOWN
```

## 6.1 Rules

- Support authority MUST be scoped by contribution and operation.
- Continued support MUST NOT expand the dependent loop's purpose automatically.
- Withdrawal MAY end future recruitment while preserving valid reliance or residual obligation.
- Emergency support authority MUST expire or renew explicitly.
- A grant MUST identify burden limits or a review process where burden cannot be predetermined.
- A dependent loop MUST NOT reinterpret unavoidable participation as open-ended authorization.

---

# 7. Support burden

A `SupportBurdenRecord` represents what a supporting loop bears to sustain a dependent loop.

Candidate burden classes:

```text
LABOR
TIME
ATTENTION
EMOTIONAL
FINANCIAL
PRIVACY
SAFETY
HEALTH
OPPORTUNITY
LOCK_IN
REPUTATION
CORRECTION
REPAIR
GOVERNANCE
ENVIRONMENTAL
FUTURE_OPTION_LOSS
OTHER
```

Required fields:

```yaml
burden_id:
supporting_loop:
dependent_loop:
burden_class:
expected_burden:
observed_burden:
reciprocity_received:
visibility:
reversibility:
proportionality:
review:
status:
```

Candidate proportionality states:

```text
PROPORTIONATE
PROPORTIONATE_WITH_CONDITIONS
DISPROPORTIONATE
UNKNOWN
CONTESTED
```

## 7.1 Rules

- Output success MUST NOT erase support burden.
- Burden MAY become disproportionate even when the loop's original purpose remains legitimate.
- A disproportionate burden SHOULD trigger narrowing, redistribution, support renewal, fork, release, or dissolution review.
- The burden record MUST identify who bears the cost of maintenance and correction.
- A dependent loop MUST NOT classify uncompensated correction or care as incidental when it is structurally required.

---

# 8. Hidden recruitment

A `HiddenRecruitmentEvent` occurs when a loop recruits support beyond visible or authorized scope.

Examples include:

- user conversation recruited into training without clear scope;
- employee care work treated as culture rather than labor;
- community legitimacy used to justify decisions the community did not authorize;
- personal data reused for a new institutional purpose;
- maintenance work assumed after a project launch;
- public emergency powers retained for ordinary operations;
- family care treated as infinitely available;
- volunteer attention converted into commercial value without disclosure.

Required fields:

```yaml
event_id:
dependent_loop:
supporting_loop:
contribution:
claimed_basis:
actual_basis:
scope_difference:
burden:
detected_at:
immediate_response:
repair:
status:
```

Candidate statuses:

```text
DETECTED
PAUSED
UNDER_REVIEW
REPAIRED
PARTIALLY_REPAIRED
RELEASED
DISSOLVED
CONTESTED
```

## 8.1 Rules

- Hidden recruitment MUST NOT be normalized by repeated use.
- Detection SHOULD pause new recruitment where materially consequential.
- Repair SHOULD include correction of the authority record, burden recognition, notice, release, compensation, deletion, transfer, or dissolution as applicable.
- A hidden contribution MAY remain historically relevant without remaining available for future use.

---

# 9. Telic compatibility and transplant assessment

A `TelicCompatibilityAssessment` evaluates whether a purpose, process, policy, or organizational form can operate coherently within a new host field.

The preferred technical terms are:

```text
TELIC_COMPATIBILITY
TELIC_TRANSPLANT_FAILURE
CONSTITUTIONAL_SUBSTRATE_MISMATCH
```

“Teleological graft rejection” MAY be retained as lineage language or explanatory metaphor.

It MUST NOT be treated as a biological claim.

Required fields:

```yaml
assessment_id:
transplanted_object:
source_field:
host_field:
required_substrate:
available_substrate:
shared_invariants:
conflicts:
missing_support:
authority_fit:
burden_fit:
correction_fit:
exit_fit:
status:
```

Candidate statuses:

```text
COMPATIBLE
COMPATIBLE_WITH_ADAPTATION
CONDITIONAL
SUBSTRATE_MISMATCH
TELIC_INCOMPATIBILITY
TRANSPLANT_FAILURE
UNKNOWN
CONTESTED
```

## 9.1 Rules

- Similar form MUST NOT be treated as proof of compatible purpose.
- A copied process SHOULD identify the substrate conditions that made it work in the source field.
- Host adaptation MAY be required.
- Local adaptation MUST NOT be presumed superior by default.
- A transplant failure MAY reflect absent authority, absent trust, absent capability, incompatible burden, or conflicting protected conditions.
- The assessment MUST distinguish process failure from moral or biological defect in the host.

---

# 10. Drift

A `DriftRecord` documents material change between a loop's declared and operative field.

Candidate drift types:

```text
MISSION_DRIFT
VALUE_DRIFT
AUTHORITY_DRIFT
BENEFICIARY_DRIFT
SCOPE_DRIFT
INCENTIVE_DRIFT
DATA_USE_DRIFT
RISK_DRIFT
GOVERNANCE_DRIFT
OTHER
```

Required fields:

```yaml
drift_id:
dependent_loop:
drift_type:
declared_state:
operative_state:
evidence:
affected_centers:
authority_change:
burden_change:
beneficiary_change:
detected_at:
review:
status:
```

Candidate statuses:

```text
CANDIDATE
CONFIRMED
CONTESTED
CORRECTING
REAUTHORIZED
FORKING
RELEASED
DISSOLVED
```

## 10.1 Rules

- Drift is not automatically bad.
- Drift becomes constitutionally material when purpose, authority, beneficiaries, burdens, or protected conditions change.
- Material drift SHOULD trigger reauthorization or governance review.
- Rebranding MUST NOT substitute for reauthorization.
- A loop MAY legitimately evolve.
- Evolution MUST remain distinguishable from covert purpose substitution.

## 10.2 Governing distinction

> **Mission drift can be the system departing from its purpose—or the purpose departing from the field.**

---

# 11. Lock-in and capture

A `LockInCaptureProfile` identifies how continued participation, support, or exit is constrained.

Candidate lock-in mechanisms:

```text
CONTRACTUAL
TECHNICAL
DATA
FINANCIAL
IDENTITY
REPUTATIONAL
SOCIAL
INSTITUTIONAL
LEGAL
INFRASTRUCTURAL
COGNITIVE
DEPENDENCY
NETWORK
OTHER
```

Candidate capture types:

```text
SUPPORT_CAPTURE
AUTHORITY_CAPTURE
DATA_CAPTURE
ROLE_CAPTURE
MISSION_CAPTURE
REGULATORY_CAPTURE
VENDOR_CAPTURE
MODEL_CAPTURE
TEMPORAL_CAPTURE
OTHER
```

Required fields:

```yaml
profile_id:
dependent_loop:
affected_supporting_loops:
lock_in_mechanisms:
switching_costs:
exit_available:
exit_effective:
authority_withdrawn:
support_continues:
capture_type:
correction_route:
status:
```

Candidate statuses:

```text
LOW
MODERATE
HIGH
CAPTURED
RELEASING
RELEASED
CONTESTED
UNKNOWN
```

## 11.1 Rules

- Exit must be practical, not merely textual.
- High switching cost MUST be visible.
- Continued support after authority withdrawal MUST trigger capture review.
- Dependence on the loop for livelihood, identity, care, or infrastructure MUST NOT be treated as proof of voluntary continuation.
- Lock-in MAY be legitimate when bounded, visible, proportionate, and reviewable.
- A captured loop SHOULD lose authority to expand its own support requirements.

---

# 12. Fork and exit

A `ForkExitRecord` represents a governed separation.

Required fields:

```yaml
fork_exit_id:
source_loop:
departing_centers:
remaining_centers:
reason:
records:
assets:
obligations:
authority:
shared_infrastructure:
privacy:
transition:
repair:
status:
```

Candidate statuses:

```text
PROPOSED
NEGOTIATING
ACTIVE
COMPLETED
CONTESTED
FAILED
RELEASED
```

## 12.1 Rules

- Exit MUST identify what the departing center may take, leave, correct, delete, or continue.
- A fork SHOULD preserve lineage without implying continued shared authority.
- Shared infrastructure MUST receive explicit governance.
- Exit MUST NOT be punished through unrelated data retention, reputation damage, or withheld portability.
- Valid residual obligations MAY survive exit.
- A clean fork MAY preserve more integrity than forced consensus.

---

# 13. Dissolution and residual state

A `DissolutionResidualStateRecord` represents the governed end of a loop.

Required fields:

```yaml
dissolution_id:
loop:
reason:
authority:
effective_at:
support_released:
assets:
records:
restricted_data:
obligations:
unresolved_harms:
repair_funds:
successor:
deletion:
public_notice:
final_witness:
status:
```

Candidate statuses:

```text
PROPOSED
APPROVED
IN_PROGRESS
PARTIAL
COMPLETED
CONTESTED
FAILED
```

## 13.1 Rules

- Dissolution MUST NOT erase history.
- Dissolution MUST release future recruitment of support.
- Residual obligations MUST remain assigned.
- Restricted data MUST receive custody, deletion, or transfer rules.
- A successor MUST NOT be invented merely to preserve form.
- Dissolution MAY be the legitimate repair when authority, substrate, or purpose cannot be restored.
- The final witness MUST distinguish ended authority from surviving obligation.

## 13.2 Governing distinction

> **Dissolution is sometimes the repair.**

---

# 14. Dependency witness

A `DependencyWitness` records the support structure and lifecycle of a dependent loop.

Required fields:

```yaml
witness_id:
dependent_loop:
declared_purpose:
operative_purpose:
supporting_loops:
substrate_map:
support_grants:
support_burdens:
hidden_recruitment:
compatibility_assessments:
drift:
lock_in:
forks:
dissolution:
corrections:
completeness:
generated_from_events:
```

## 14.1 Rules

- The witness MUST identify both visible and known hidden support.
- It MUST preserve who supplied the support and under what authority.
- It MUST identify burden, reciprocity, and exit.
- It MUST identify purpose and authority changes.
- It MUST preserve withdrawal, fork, release, and dissolution events.
- Completeness MUST remain scoped.
- The witness MUST NOT treat dependency as pathology by default.

---

# 15. Dependency governance gate

The minimum gate dimensions are:

```text
support_visibility
support_authority
burden_proportionality
reciprocity
telic_compatibility
mission_alignment
authority_alignment
exit_effectiveness
correction_capacity
lock_in
capture
residual_obligation
dissolution_readiness
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
PAUSE
ESCALATE
FORK
RELEASE
DISSOLVE
FAIL
UNKNOWN
CONTESTED
```

## 15.1 Composition rules

- Hidden critical support SHOULD prevent expansion.
- Withdrawn authority with continuing recruitment SHOULD fail.
- Disproportionate burden SHOULD trigger redistribution, narrowing, fork, release, or dissolution review.
- Telic incompatibility SHOULD prevent automatic transplant.
- Material mission or authority drift SHOULD require reauthorization.
- Ineffective exit with continuing support MAY constitute capture.
- Dissolution readiness SHOULD be evaluated before a loop becomes unable to preserve records and obligations.
- A loop MUST NOT evaluate its own dependency gate without independent review where it controls contributor exit.

---

# 16. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Self-grounding fiction

A dependent loop describes materially external support as internally generated.

## NC-2 — Continued support as consent

Historical or unavoidable support is treated as current authorization.

## NC-3 — Hidden recruitment normalization

Repeated unauthorized use becomes the claimed basis for future use.

## NC-4 — Burden erasure by output

Successful output removes the support-burden record.

## NC-5 — Form as compatibility

A copied process is treated as compatible because its visible structure matches.

## NC-6 — Drift without reauthorization

The operative beneficiary or purpose changes materially while authority remains unchanged.

## NC-7 — Textual exit only

A participant may formally exit but cannot obtain records, portability, livelihood transition, or effective release.

## NC-8 — Authority withdrawal ignored

A support grant is withdrawn while recruitment continues.

## NC-9 — Asset-preserving dissolution

The loop dissolves while leaving obligations and harms unassigned.

## NC-10 — Biological pathologizing

Telic incompatibility is described as a biological defect in participants or host communities.

## NC-11 — Fork as erasure

A fork removes shared history or misrepresents lineage.

## NC-12 — Forced loop preservation

Repair is rejected solely because it would end the dependent loop.

---

# 17. Positive demonstrations

I.5 includes eight required demonstrations.

## PD-1 — Legitimate dependency

A dependent loop operates with visible support, bounded authority, proportionate burden, reciprocity, correction, and exit.

## PD-2 — Hidden recruitment detected

A contribution used outside scope is identified, paused, and routed to repair.

## PD-3 — Substrate mismatch

A copied process fails because the host lacks the authority, trust, capability, or protected conditions that supported the source implementation.

## PD-4 — Mission drift

The operative beneficiary changes materially, triggering reauthorization.

## PD-5 — Disproportionate support burden

Maintenance and correction burden exceed the grant and trigger redistribution or release.

## PD-6 — Lock-in after authority withdrawal

Support continues after withdrawal, producing a capture finding and disabled recruitment.

## PD-7 — Fork

Compatible participants preserve lineage and shared assets while separating authority and future records.

## PD-8 — Dissolution

A loop ends while preserving obligations, restricted data, repair, public notice, and final witness.

---

# 18. Conformance additions

I.5 adds the following P2/P3 requirements:

- supporting-loop references;
- dependent-loop record;
- substrate-contribution map;
- support-authority grants;
- support-burden records;
- hidden-recruitment events;
- telic-compatibility assessment for transplanted or imported forms;
- material drift review;
- lock-in and capture profile;
- governed fork and exit;
- dissolution and residual-state record;
- dependency witness.

P3 additionally requires:

- contributor challenge to support scope;
- independent capture review;
- practical portability and exit assessment;
- burden and reciprocity witness;
- dissolution readiness;
- successor and residual-state audit.

---

# 19. Security and governance considerations

Dependency systems can be manipulated through:

- hidden support extraction;
- fabricated reciprocity;
- coercive contracts;
- dependency concentration;
- mission laundering;
- artificial switching costs;
- record hostage-taking;
- contributor replacement threats;
- false dissolution urgency;
- selective history;
- captive oversight.

Implementations SHOULD:

- authenticate grants and withdrawals;
- expose critical dependencies;
- separate operation from legitimacy;
- preserve independent exit controls;
- record support burden;
- test practical portability;
- require independent review where the loop controls its own exit conditions;
- prepare residual-state records before crisis.

---

# 20. I.5 non-claims

I.5 does not claim:

- dependency is inherently unhealthy;
- all imported institutions fail;
- mission drift is always bad;
- local adaptation is always superior;
- every switching cost is coercive;
- every persistent loop is captured;
- every contributor has equal authority;
- dissolution is always preferable to repair;
- a host field has one unified purpose;
- biological graft rejection explains institutional behavior;
- a single compatibility score can govern all transplants.

---

# 21. I.5 completion criterion

I.5 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. legitimate dependency remains possible;
4. hidden recruitment causes pause and repair;
5. substrate mismatch prevents automatic transplant;
6. material drift triggers reauthorization;
7. disproportionate burden changes the route;
8. withdrawn support authority disables recruitment;
9. practical exit is distinguished from textual exit;
10. fork preserves lineage without preserving shared sovereignty;
11. dissolution preserves residual obligations and witness;
12. H.5 explains ending a loop without pathologizing dependence or blaming contributors for structural failure.
