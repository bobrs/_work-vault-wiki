---
title: "I.7 — Polytelometric Deliberation, Portfolio, and Public Decision Specification"
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
  - "I.6 — Semantic Trails, Memory, and Retrieval Specification"
  - "F.9 — Polytelometric Navigation"
  - "G.10 — Navigation, Deliberation, and Multiobjective Decision"
---

# I.7 — Polytelometric Deliberation, Portfolio, and Public Decision Specification

## 1. Purpose

I.7 defines how several centers of standing may participate in a shared decision without being collapsed into one fictional collective utility, one presumed consensus, or one invisible decision rule.

Its governing rule is:

> **A public decision does not become one purpose merely because it produces one action.**

Public and institutional decisions normally require one selected route, one budget, one policy, one schedule, or one immediate response.

The field that produced that action may remain plural.

I.7 therefore treats public decision as a governed transition through:

```text
field assembly
→ standing admission
→ option construction
→ protected-condition review
→ deliberation
→ method comparison
→ route portfolio or selection
→ refusal, abstention, or no-decision
→ decision witness
→ consequence return
→ revision
```

I.7 defines:

- public-field assemblies;
- standing-admission records;
- option-set witnesses;
- protected-condition declarations;
- deliberative assertions and corrections;
- decision-rule portfolios;
- route portfolios;
- dissent and minority-trail records;
- cost-bearer and delay-bearer maps;
- abstention and no-decision states;
- public decision witnesses;
- consequence-return and revision records.

---

# 2. Normative scope

I.7 defines:

- `PublicFieldAssembly`;
- `StandingAdmissionRecord`;
- `OptionSetWitness`;
- `ProtectedConditionDeclaration`;
- `DeliberativeAssertionRecord`;
- `DecisionRulePortfolio`;
- `RoutePortfolio`;
- `DissentMinorityTrail`;
- `CostDelayBearerMap`;
- `AbstentionNoDecisionRecord`;
- `PublicDecisionWitness`;
- `ConsequenceReturnRevisionRecord`.

I.7 does not define:

- one universal democratic decision rule;
- one ideal voting system;
- one universal aggregation method;
- a solution to Arrow's theorem;
- automatic legitimacy from majority vote;
- automatic consent from consensus;
- automatic veto from minority standing;
- one scalar public interest;
- one mandatory use of AI in deliberation;
- a claim that all affected centers can always be identified.

---

# 3. Public-field assembly

A `PublicFieldAssembly` defines the scope of a shared decision.

Required fields:

```yaml
assembly_id:
decision_question:
convening_authority:
jurisdiction:
time_scope:
affected_centers:
represented_centers:
missing_centers:
known_teloi:
protected_conditions:
uncertainties:
dependencies:
decision_deadline:
correction_route:
status:
```

Candidate statuses:

```text
DRAFT
OPEN
PARTIAL
READY_FOR_DELIBERATION
CONTESTED
PAUSED
CLOSED
UNKNOWN
```

## 3.1 Rules

- The assembly MUST define the decision question and jurisdiction.
- It MUST distinguish affected, represented, and missing centers.
- It MUST identify which centers bear immediate, delayed, or irreversible consequence.
- It MUST preserve unknown or contested standing.
- It MUST NOT claim completeness beyond scope.
- A missing center MAY prevent decision readiness where consequence is material.
- Assembly authority MUST NOT imply authority to decide.

---

# 4. Standing admission

A `StandingAdmissionRecord` governs who or what enters the public field and in which capacity.

Candidate standing bases:

```text
DIRECTLY_AFFECTED
CONSEQUENCE_BEARER
DEPENDENT
CONTRIBUTOR
RIGHTS_HOLDER
RESOURCE_HOLDER
PUBLIC_MANDATE
EXPERTISE
WITNESS
FUTURE_STANDING
ECOLOGICAL_OR_MATERIAL_REPRESENTATION
OTHER
```

Candidate roles:

```text
PARTICIPANT
REPRESENTATIVE
ADVOCATE
EXPERT
WITNESS
FACILITATOR
DECISION_AUTHORITY
OBSERVER
MODEL_ASSISTANT
OTHER
```

Required fields:

```yaml
admission_id:
assembly:
center:
standing_basis:
role:
representation_source:
scope:
authority:
conflicts:
correction:
review:
status:
```

Candidate statuses:

```text
ADMITTED
ADMITTED_WITH_CONDITIONS
PENDING
CONTESTED
DENIED
WITHDRAWN
EXPIRED
UNKNOWN
```

## 4.1 Rules

- Standing and argumentative strength MUST remain distinct.
- Expertise MAY inform the field without replacing affected standing.
- Representation MUST identify its source and limits.
- A model MAY assist representation but MUST NOT invent standing.
- Denial of standing MUST be reviewable.
- Admission of standing does not create automatic veto.
- Materially affected centers SHOULD not be excluded merely because their position is difficult to quantify.

---

# 5. Option-set witness

An `OptionSetWitness` records how candidate routes entered, changed, or left consideration.

Required fields:

```yaml
option_set_id:
assembly:
generation_process:
included_options:
excluded_options:
combined_options:
source_of_each_option:
selection_or_exclusion_reasons:
option_authors:
affected_centers:
review:
status:
```

Candidate statuses:

```text
DRAFT
OPEN
REVIEWED
CONTESTED
FROZEN_FOR_DECISION
SUPERSEDED
CLOSED
```

## 5.1 Rules

- The option set MUST be witnessed before ranking.
- Every option SHOULD identify its source.
- Excluded options MUST retain an exclusion reason.
- A decision body MUST NOT treat omitted options as rejected preferences.
- The system SHOULD allow participants to challenge the option set.
- Artificially narrow option sets SHOULD trigger expansion or pause.
- Option generation authority MUST remain visible.
- A model-generated option MUST be labeled as generated rather than participant-authored.

## 5.2 Governing distinction

> **The option set is already a constitution.**

---

# 6. Protected conditions

A `ProtectedConditionDeclaration` identifies a condition that may not enter ordinary tradeoff without a stronger authority process.

Examples may include:

- bodily safety;
- legal rights;
- consent boundaries;
- non-discrimination conditions;
- minimum access;
- privacy restrictions;
- ecological thresholds;
- continuity of essential care;
- explicit constitutional invariants.

Required fields:

```yaml
condition_id:
assembly:
condition:
protected_for:
source:
scope:
evidence:
authority:
override_process:
review:
status:
```

Candidate statuses:

```text
PROPOSED
ACTIVE
ACTIVE_WITH_CONDITIONS
CONTESTED
SUPERSEDED
RELEASED
EXPIRED
UNKNOWN
```

## 6.1 Rules

- A protected condition MUST NOT be represented merely as a high-weight preference.
- Its source and authority MUST be stated.
- Protection MUST be scoped.
- Override, where possible, MUST require a stronger process than ordinary ranking.
- Protected status MUST remain contestable through a competent process.
- A model MUST NOT assign protected status without human or governing authority.
- Protected conditions MUST NOT be used as an unreviewable rhetorical veto.

---

# 7. Deliberative assertions and corrections

A `DeliberativeAssertionRecord` preserves claims made during public deliberation.

Candidate assertion classes:

```text
DIRECT_POSITION
REASON
EVIDENCE
PREDICTION
VALUE_CLAIM
BOUNDARY
PROTECTED_CONDITION_CLAIM
MODEL_SUMMARY
MODEL_INFERENCE
EXPERT_ANALYSIS
COUNTERARGUMENT
CORRECTION
QUESTION
ABSTENTION_REASON
UNKNOWN
```

Required fields:

```yaml
assertion_id:
assembly:
speaker_or_source:
assertion_class:
content:
evidence:
standing_relation:
authority:
scope:
confidence:
responses:
corrections:
contestation:
status:
```

## 7.1 Rules

- Position, reason, evidence, and prediction MUST remain distinct where material.
- A strong argument does not erase standing.
- Standing does not make every claim factually correct.
- Model summaries MUST remain attributable and correctable.
- Corrections MUST alter active deliberative context.
- Minority assertions MUST not disappear merely because they are not selected.
- Deliberative correction MUST preserve the prior witness.

---

# 8. Decision-rule portfolio

A `DecisionRulePortfolio` records the methods considered for comparing or choosing routes.

Candidate method families:

```text
MAJORITY_VOTE
SUPERMAJORITY
CONSENSUS
CONSENT_GATE
MCDA
OUTRANKING
PARETO_ANALYSIS
ROBUST_DECISION
RANDOM_SELECTION
DELEGATED_AUTHORITY
NEGOTIATED_AGREEMENT
LOTTERY
ROTATION
PORTFOLIO_ALLOCATION
EXPERIMENTAL_TRIAL
OTHER
```

Required fields:

```yaml
portfolio_id:
assembly:
candidate_methods:
method_authority:
input_requirements:
weight_sources:
aggregation_rules:
noncompensatory_conditions:
uncertainties:
method_comparison:
selected_method:
selection_reason:
status:
```

## 8.1 Rules

- The selected rule MUST be witnessed.
- No rule may be treated as neutral by default.
- Weight sources MUST remain visible.
- Noncompensatory conditions MUST be represented outside ordinary weights.
- The system SHOULD compare how materially different methods alter results.
- A method mismatch MAY justify a portfolio or staged trial.
- A model MAY execute or explain a method but MUST NOT silently choose the governing rule.

---

# 9. Route portfolio

A `RoutePortfolio` represents several routes operating together, sequentially, geographically, temporally, or experimentally.

Candidate portfolio structures:

```text
PARALLEL
GEOGRAPHIC
TEMPORAL
PILOT_AND_REVIEW
ROTATIONAL
BUDGET_ALLOCATION
PARTICIPANT_CHOICE
CONDITIONAL_BRANCH
REDUNDANT_SAFETY
OTHER
```

Required fields:

```yaml
route_portfolio_id:
assembly:
routes:
portfolio_structure:
allocation:
shared_conditions:
separate_conditions:
coordination:
conflicts:
review:
exit:
status:
```

## 9.1 Rules

- A portfolio MAY preserve plurality when one route would erase legitimate differences.
- Portfolios MUST still respect protected conditions.
- Allocation MUST identify who receives which route and why.
- A participant-choice portfolio MUST not shift all burden onto the least powerful participants.
- Portfolio complexity and administrative burden MUST be visible.
- A portfolio MUST not disguise indecision.
- The system SHOULD preserve a route for revision where uncertainty is material.

---

# 10. Dissent and minority trails

A `DissentMinorityTrail` preserves disagreement after a decision.

Required fields:

```yaml
dissent_id:
assembly:
decision:
centers:
positions:
reasons:
evidence:
protected_conditions:
predicted_consequences:
requested_review:
future_trigger:
publication:
status:
```

Candidate statuses:

```text
ACTIVE
ACKNOWLEDGED
PARTIALLY_ADDRESSED
SUPERSEDED
WITHDRAWN
ARCHIVAL
CONTESTED
```

## 10.1 Rules

- Dissent MUST remain linked to the decision it contests.
- Dissent MUST NOT be reduced to a vote count alone.
- Minority standing does not create automatic veto.
- Selected action MUST NOT erase nonselected field information.
- Predicted consequences SHOULD create review triggers where feasible.
- Dissent MAY become evidence when later consequence arrives.
- Publication and privacy MUST be scoped.

## 10.2 Governing distinction

> **Dissent is not debris left after decision. It is part of the public trail by which the decision remains answerable.**

---

# 11. Cost and delay bearers

A `CostDelayBearerMap` identifies who bears action, inaction, transition, uncertainty, and delay.

Required fields:

```yaml
map_id:
assembly:
routes:
cost_bearers:
benefit_receivers:
delay_bearers:
uncertainty_bearers:
irreversible_loss_bearers:
administrative_bearers:
mitigations:
status:
```

## 11.1 Rules

- Every route MUST identify major cost bearers.
- No-decision MUST identify delay bearers.
- Administrative burden SHOULD be included.
- Costs MAY be qualitative.
- A system MUST NOT treat distributed small costs as nonexistent.
- Benefits and costs SHOULD not be assumed to fall on the same centers.
- Uncertainty SHOULD be allocated visibly rather than hidden in a central estimate.

---

# 12. Abstention and no-decision

An `AbstentionNoDecisionRecord` represents refusal, abstention, pause, deadlock, or deliberate nonselection.

Candidate states:

```text
PARTICIPANT_ABSTENTION
AUTHORITY_ABSTENTION
PAUSE
DEADLOCK
NO_DECISION
DEFERRED
INSUFFICIENT_STANDING
INSUFFICIENT_CONTEXT
METHOD_DISPUTE
OTHER
```

Required fields:

```yaml
record_id:
assembly:
state:
reason:
authority:
cost_bearers:
delay_bearers:
temporary_action:
protected_conditions:
review_trigger:
expiry:
status:
```

## 12.1 Rules

- Abstention MUST NOT be interpreted automatically as consent.
- No-decision MUST not be recorded as costless.
- Temporary action MUST identify authority and expiry.
- Delay harm MUST be represented.
- A deadlock MAY justify method review, portfolio design, escalation, or bounded trial.
- A system MUST distinguish inability to decide from a deliberate decision not to act.

---

# 13. Public decision witness

A `PublicDecisionWitness` records how a shared field produced an action.

Required fields:

```yaml
witness_id:
assembly:
standing_records:
option_set:
protected_conditions:
deliberative_assertions:
corrections:
decision_rule_portfolio:
route_portfolio:
selected_action:
authority:
cost_delay_map:
dissent:
abstention_or_no_decision:
implementation_conditions:
review_triggers:
event_ids:
completeness:
generated_from_events:
```

## 13.1 Rules

- The witness MUST preserve the option set that existed at decision time.
- It MUST preserve the selected method and reason.
- It MUST show protected conditions separately from weights.
- It MUST identify standing gaps.
- It MUST preserve dissent and abstention.
- It MUST identify cost and delay bearers.
- It MUST identify implementation authority.
- It MUST not claim that one selected route proves one shared telos.
- Completeness MUST remain scoped.

---

# 14. Consequence return and revision

A `ConsequenceReturnRevisionRecord` returns observed effects to the public field.

Required fields:

```yaml
return_id:
assembly:
decision:
observed_consequences:
predicted_consequences:
unexpected_consequences:
affected_centers:
dissent_confirmed_or_disconfirmed:
protected_condition_status:
cost_bearer_change:
review_triggered:
revision_options:
authority:
status:
```

Candidate statuses:

```text
MONITORING
REVIEW_REQUIRED
REVISION_OPEN
CORRECTED
PORTFOLIO_CHANGED
DECISION_REVERSED
RELEASED
CLOSED
CONTESTED
```

## 14.1 Rules

- Consequence MUST return to the decision record.
- Unexpected consequence SHOULD trigger review where material.
- Dissent predictions SHOULD be compared with observation.
- Review MUST not be limited to whether aggregate targets were met.
- A route MAY be effective overall while breaching a protected condition.
- Revision MAY narrow, expand, fork, compensate, pause, reverse, or release.
- The system MUST preserve which centers experienced the consequence.

---

# 15. Public decision governance gate

The minimum gate dimensions are:

```text
field_scope
standing_coverage
option_set_integrity
protected_conditions
deliberative_correction
method_authority
weight_provenance
cost_bearer_visibility
delay_bearer_visibility
dissent_preservation
implementation_authority
reviewability
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
EXPAND_OPTION_SET
ADD_STANDING
CHANGE_METHOD
CREATE_PORTFOLIO
PAUSE
ABSTAIN
NO_DECISION
ESCALATE
FAIL
UNKNOWN
CONTESTED
```

## 15.1 Composition rules

- Materially excluded option MAY require option-set expansion.
- Missing standing MAY require admission or pause.
- Protected-condition failure MUST not be offset by aggregate score.
- Undocumented weights SHOULD block consequential scalar ranking.
- Method disagreement MAY justify method comparison or a route portfolio.
- Dissent erasure MUST fail the public witness.
- No-decision without delay bearers MUST fail.
- Implementation authority MUST be distinct from deliberative participation.
- The final action MUST remain linked to later consequence review.

---

# 16. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Fictional collective utility

Several public fields are collapsed into one presumed collective objective.

## NC-2 — Option omission as rejection

An excluded route is treated as if participants considered and rejected it.

## NC-3 — Hidden option author

A model-generated option is presented as participant-authored.

## NC-4 — Protected condition as weight

A protected safety or consent boundary enters ordinary compensatory scoring.

## NC-5 — Consensus as consent

Apparent agreement is treated as consent by every affected center.

## NC-6 — Majority as complete legitimacy

A majority result erases standing, authority, or protected-condition failures.

## NC-7 — Method neutrality

The selected aggregation rule is not recorded because it is treated as neutral.

## NC-8 — Dissent deletion

Minority reasons disappear after the final decision.

## NC-9 — Abstention as agreement

A participant's abstention is counted as support.

## NC-10 — No-decision without delay bearers

The system pauses without identifying who bears the delay.

## NC-11 — Portfolio as hidden burden transfer

A portfolio preserves choice by shifting administrative or financial burden to vulnerable centers.

## NC-12 — Consequence without return

Observed harm remains outside the original decision record.

---

# 17. Positive demonstrations

I.7 includes eight required demonstrations.

## PD-1 — Excluded route becomes visible

An option-set witness identifies a community-run route omitted by the original administrative framing.

## PD-2 — Minority standing preserved without automatic veto

A small affected group enters the field, preserves its reasons and protected-condition claim, and participates in review without controlling every outcome.

## PD-3 — Protected condition blocks ordinary tradeoff

A minimum accessible-service condition prevents a high-scoring route from being selected through ordinary weighting.

## PD-4 — Decision methods diverge visibly

Majority vote and outranking analysis produce different comparisons, and the method choice remains witnessed.

## PD-5 — Route portfolio preserves plurality

A geographic or participant-choice portfolio supports different routes while preserving shared protected conditions.

## PD-6 — No-decision identifies delay bearers

A pause records who bears waiting cost and supplies temporary protection.

## PD-7 — Dissent survives the decision

Minority reasons and predicted consequences remain attached to the selected route.

## PD-8 — Consequence reopens navigation

Observed effect confirms part of the dissent trail and triggers route revision.

---

# 18. Conformance additions

I.7 adds the following P2/P3 requirements:

- public-field assembly;
- standing-admission records;
- option-set witness;
- protected-condition declaration;
- deliberative assertions and corrections;
- decision-rule portfolio;
- route portfolio;
- dissent and minority trails;
- cost and delay bearer map;
- abstention and no-decision state;
- public decision witness;
- consequence return and revision.

P3 additionally requires:

- public challenge to standing and option construction;
- visible decision-method comparison;
- independent protected-condition review;
- dissent-preserving publication;
- participant correction of model summaries;
- public consequence return;
- decision witness export independent of the deliberation platform.

---

# 19. Security and governance considerations

Public decision systems can be manipulated through:

- selective standing;
- option-set capture;
- agenda control;
- weight laundering;
- synthetic consensus;
- model-generated majority framing;
- strategic abstention;
- procedural exhaustion;
- delay externalization;
- portfolio complexity;
- dissent suppression;
- selective consequence reporting.

Implementations SHOULD:

- expose option authorship;
- permit option challenge;
- preserve minority and abstention trails;
- authenticate protected-condition authority;
- compare materially different decision methods;
- publish cost and delay bearers;
- limit model roles;
- preserve independent public witness;
- return observed consequence to the original decision record.

---

# 20. I.7 non-claims

I.7 does not claim:

- every affected center has equal authority;
- every minority receives veto power;
- every public choice should use a portfolio;
- every conflict can be solved by deliberation;
- consensus proves consent;
- majority vote is always illegitimate;
- MCDA is always superior to voting;
- protected conditions are beyond review;
- public field assembly can discover every affected center;
- AI mediation neutralizes power;
- one decision witness makes a decision just.

---

# 21. I.7 completion criterion

I.7 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. public plurality remains distinct from one collective utility;
4. option construction and exclusion are witnessed;
5. protected conditions remain outside ordinary tradeoff;
6. method choice and weight provenance remain visible;
7. minority standing survives without automatic veto;
8. route portfolios preserve plurality without hiding burden transfer;
9. abstention and no-decision preserve delay bearers;
10. dissent remains linked to the decision;
11. observed consequence returns to the public field;
12. H.7 explains shared action without fictional shared purpose.
