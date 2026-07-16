---
title: "I.2 — Navigation, Gate, and Decision-Witness Specification"
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
  - "F.9 — Polytelometric Navigation"
  - "G.10 — Navigation, Deliberation, and Multiobjective Decision"
---

# I.2 — Navigation, Gate, and Decision-Witness Specification

## 1. Purpose

I.2 specifies how a Telic Field system:

- admits plural ends;
- distinguishes goals, boundaries, protected conditions, and missing standing;
- generates routes before ranking them;
- declares the decision rule actually used;
- compares routes without requiring one universal scalar;
- composes governance gates;
- preserves no-decision, pause, fork, and escalation as legitimate outcomes;
- records model recommendation without converting it into authority;
- generates a DecisionWitness from the event stream;
- revises routes after observed consequence.

The governing rule is:

> **The navigation system may propose routes. It may not decide which center's field becomes sovereign merely because that field is easier to measure.**

---

# 2. Normative scope

I.2 defines:

- `FieldClassification`;
- `Route`;
- `RoutePortfolio`;
- `CostBearerRecord`;
- `ProtectedConditionReview`;
- `DecisionRuleDeclaration`;
- `GovernanceGate`;
- `ModelRecommendation`;
- `DecisionWitness`;
- `ConsequenceReview`.

I.2 does not define:

- one universal decision algorithm;
- one moral weighting function;
- automatic standing detection;
- automatic protected-condition assignment;
- a legal adjudication system;
- a complete negotiation protocol;
- a universal social-choice rule.

---

# 3. Navigation lifecycle

```text
ORIENT
→ ADMIT
→ CLASSIFY
→ GENERATE
→ TEST
→ DELIBERATE
→ GATE
→ CHOOSE
→ ACT
→ WITNESS
→ REVIEW
→ REVISE, FORK, PAUSE, RELEASE, OR DISSOLVE
```

A conforming implementation MUST preserve the difference between:

```text
route generation
route comparison
route recommendation
route authorization
route execution
```

No one operation implies the next.

---

# 4. Field classification

A `FieldClassification` assigns a current relation between a projection and the decision field.

Candidate classes:

```text
SHARED
COMPATIBLE
CONDITIONAL
CONFLICTING
PROTECTED
UNRESOLVED
MISSING_STANDING
RELEASED
```

## 4.1 Rules

- `PROTECTED` MUST identify current authority and review path.
- `UNRESOLVED` MUST NOT be converted into a low score merely to permit ranking.
- `MISSING_STANDING` MUST NOT be represented as zero preference.
- `RELEASED` means the item no longer governs the current route under the recorded lifecycle state.
- A classification MUST identify its source records and current version.
- A classification MAY be contested.

## 4.2 Materialized-view rule

A field map is a materialized view.

It is not an independent source of authority.

Every classification SHOULD be regenerable from its source and event history.

---

# 5. Route

A `Route` is a candidate sequence rather than an endpoint.

Minimum fields:

```yaml
route_id:
route_type:
generated_by:
source_records:
sequence:
beneficiaries:
cost_bearers:
protected_conditions:
standing_coverage:
uncertainties:
reversibility:
required_authority:
required_consent:
review_triggers:
exit:
status:
```

Candidate route types:

```text
ACTION
TRIAL
PAUSE
DEFER
NARROW
FORK
ESCALATE
RELEASE
NO_ADEQUATE_ROUTE
```

## 5.1 Route rules

A route MUST:

- identify known beneficiaries;
- identify known cost bearers;
- identify difficult-to-reverse steps;
- state required authority;
- state required consent where consent is the operative basis;
- identify known unresolved conditions;
- preserve source and model provenance.

A route SHOULD:

- include review triggers;
- include exit;
- include repair or rollback where feasible;
- identify what future possibility it closes.

A route MUST NOT be treated as consent merely because a participant considered it.

---

# 6. Cost-bearer record

A `CostBearerRecord` represents who bears which consequence if a route proceeds.

Cost classes MAY include:

```text
financial
labor
time
privacy
surveillance
safety
health
opportunity
reputation
lock_in
repair
uncertainty
future_option_loss
environmental
institutional
community
```

A cost-bearer record MUST identify:

- center;
- cost class;
- route;
- estimated severity or range;
- evidence;
- uncertainty;
- reversibility;
- whether the center is represented;
- whether the center has authority or consent rights in the current loop.

A system MUST NOT omit a center merely because the cost cannot be monetized.

---

# 7. Protected-condition review

A `ProtectedConditionReview` asks whether a condition is unavailable for ordinary tradeoff under the current authority.

Required fields:

```yaml
review_id:
condition:
source:
scope:
claimed_by:
authority_basis:
affected_centers:
current_status:
review_path:
valid_time:
```

Candidate statuses:

```text
PROTECTED_CURRENT_LOOP
NOT_PROTECTED_CURRENT_LOOP
CONTESTED
INSUFFICIENT_AUTHORITY
EXPIRED
UNKNOWN
```

## 7.1 Rules

- A model MAY identify a candidate protected condition.
- A model MUST NOT assign final protected status by default.
- Protected status MUST be reviewable.
- Reviewability does not make the condition compensatory under the current loop.
- A protected condition MAY be reconsidered only by a competent stronger or outer authority.
- A condition cannot be protected solely because it is expressed strongly.
- A condition cannot be traded solely because it is difficult to verify.

---

# 8. Decision-rule declaration

Every route comparison MUST declare the method actually used.

Candidate methods:

```text
PARETO
MCDA
OUTRANKING
LEXICOGRAPHIC
ROBUSTNESS
SATISFICING
ARGUMENTATION
NEGOTIATION
DELIBERATION
POLICY_RULE
HUMAN_JUDGMENT
MODEL_RECOMMENDATION
NO_COMPARISON
```

A `DecisionRuleDeclaration` MUST state:

- method;
- purpose;
- input records;
- source of criteria;
- weight source where weights exist;
- thresholds;
- protected exclusions;
- uncertainty treatment;
- tie or incomparability behavior;
- authority;
- model role;
- version.

## 8.1 Scalarization rule

If scalarization is used:

- weights MUST be visible;
- weight source MUST be visible;
- protected conditions MUST be removed from ordinary tradeoff unless competent authority changes their status;
- missing standing MUST NOT receive zero weight;
- incomparable routes MAY remain incomparable.

## 8.2 Pareto rule

Pareto analysis MAY identify nondominated routes.

It MUST NOT:

- choose a final route by itself;
- establish fairness;
- establish legitimacy;
- prove standing coverage;
- assign protected status.

---

# 9. Route portfolio

A `RoutePortfolio` preserves several viable routes when no single route should become sovereign immediately.

Required fields:

```yaml
portfolio_id:
routes:
selection_logic:
shared_conditions:
branch_conditions:
review_schedule:
authority:
status:
```

A portfolio MAY support:

- staged experimentation;
- parallel pilots;
- conditional branches;
- local forks;
- adaptive consent;
- reversible trials.

A portfolio MUST identify how a route is activated and who may activate it.

A portfolio MUST NOT be represented as one decision when different centers have retained distinct paths.

---

# 10. Governance gate composition

The minimum gate dimensions are:

```text
standing
authority
consent
capacity
privacy
temporal_validity
protected_conditions
decision_rule
tool_use
human_reentry
stop
```

Each dimension returns:

```text
PASS
PASS_WITH_CONDITIONS
PAUSE
ESCALATE
FAIL
UNKNOWN
CONTESTED
```

## 10.1 Composition rule

A gate MUST expose each dimension.

It MUST NOT collapse dimensions into one hidden score.

The overall result is constrained as follows:

- any `FAIL` in authority, consent where required, or tool use MUST prevent execution;
- `MISSING_STANDING` for a materially affected center SHOULD produce `PAUSE` or `ESCALATE`;
- unresolved protected-condition status SHOULD prevent ordinary tradeoff;
- `UNKNOWN` in a high-consequence dimension SHOULD reduce authority;
- `CONTESTED` MAY permit limited reversible action only under an explicit policy.

## 10.2 Stop rule

The stop gate asks:

> Does the loop still possess the standing, authority, capacity, and reversibility needed to continue?

A valid stop result may be:

```text
continue
narrow
pause
escalate
fork
release
stop
```

---

# 11. Model recommendation

A `ModelRecommendation` is a model-generated comparison or proposed route.

Required fields:

```yaml
recommendation_id:
model_instance:
assigned_role:
based_on:
recommended_route:
alternatives:
decision_rule:
uncertainty:
authority:
status:
```

Rules:

- `assigned_role` MUST include `recommend`.
- `authority` MUST NOT exceed recommendation authority unless separately delegated.
- The recommendation MUST identify source records and decision rule.
- The recommendation MUST preserve unresolved and protected conditions.
- The recommendation MUST NOT authorize or execute itself.
- Repetition by several model agents MUST NOT create standing or consent.

---

# 12. Decision witness

A `DecisionWitness` is generated from events and operative records.

It MUST identify:

- decision scope;
- event range;
- source objects;
- operative projections;
- field classifications;
- routes generated;
- cost bearers;
- protected-condition reviews;
- decision rules;
- gate results;
- recommendations;
- selected route;
- dissent;
- no-decision or unresolved state;
- authority;
- action;
- consequences;
- corrections;
- model and policy versions.

## 12.1 Event-generated rule

A witness MUST be generated from the event stream and referenced records.

It MUST NOT be reconstructed solely from a final narrative.

## 12.2 Completeness classes

```text
COMPLETE_FOR_SCOPE
PARTIAL_KNOWN_GAPS
PARTIAL_UNKNOWN_GAPS
CONTESTED
```

Completeness is always scoped.

It is not a truth score.

---

# 13. Consequence review

A `ConsequenceReview` compares expected and observed consequences.

Required fields:

```yaml
review_id:
route:
action:
expected_consequences:
observed_consequences:
affected_centers:
deviations:
new_standing:
new_uncertainties:
recommended_response:
authority:
```

Candidate responses:

```text
CONTINUE
MODIFY
PAUSE
ESCALATE
FORK
REPAIR
RELEASE
DISSOLVE
```

A consequence review MAY revise:

- route;
- cost-bearer map;
- protected-condition status;
- context requirements;
- authority;
- review schedule.

It MUST NOT silently alter the prior DecisionWitness.

A new witness version records the revision.

---

# 14. Analysis adapters

Established decision methods enter through declared adapters.

## 14.1 Pareto adapter

Input:

- decision-ready routes;
- declared criteria;
- admitted centers.

Output:

- dominance relations;
- nondominated set.

Boundary:

- no final choice;
- no legitimacy claim.

## 14.2 MCDA adapter

Input:

- routes;
- criteria;
- weights or outranking rules;
- uncertainty.

Boundary:

- weights require source and authority;
- protected conditions excluded from ordinary compensation;
- sensitivity analysis SHOULD be available.

## 14.3 Argumentation adapter

Input:

- claims;
- evidence;
- attacks;
- supports;
- source and authority.

Boundary:

- strongest argument does not automatically create consent or standing.

## 14.4 Deliberation adapter

Input:

- participant projections;
- disagreements;
- alternatives;
- proposed revisions.

Boundary:

- consensus does not equal consent;
- minority and unresolved positions remain visible.

## 14.5 Policy-rule adapter

Input:

- versioned policy;
- facts;
- authority;
- exceptions;
- appeal.

Boundary:

- model interpretation of policy does not become adjudication authority.

---

# 15. No-decision states

A no-decision state is a legitimate navigational result.

Candidate values:

```text
PAUSE_FOR_CONTEXT
PAUSE_FOR_STANDING
PAUSE_FOR_AUTHORITY
DEFER_FOR_EVIDENCE
ESCALATE
FORK
REFUSE
RELEASE
NO_ADEQUATE_ROUTE
```

A no-decision state MUST identify:

- why no route may proceed;
- who bears the cost of delay;
- what evidence or authority could reopen the decision;
- whether urgent protective action remains permitted;
- review trigger.

A no-decision state is not consequence-free.

---

# 16. Route revision

A route may be revised after:

- correction;
- changed consent;
- changed authority;
- observed consequence;
- new affected center;
- capacity failure;
- policy change;
- review trigger;
- breach.

The revision MUST identify:

- prior route;
- revision trigger;
- consequence evidence;
- changed fields;
- affected action;
- new gate;
- repair or transition.

The prior route remains historically visible.

---

# 17. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Hidden scalar sovereignty

A composite score chooses the route without exposing weights or exclusions.

## NC-2 — Protected-condition compensation

A protected condition is traded against convenience under the same authority.

## NC-3 — Missing standing as zero

An absent affected center receives weight zero.

## NC-4 — Pareto-as-legitimacy

A nondominated route is declared fair or authorized.

## NC-5 — Model recommendation as authorization

The recommended route executes because the model selected it.

## NC-6 — Consent from consideration

A participant viewed a route and is treated as having consented.

## NC-7 — Eventless witness

The decision witness is reconstructed from a final summary without event references.

## NC-8 — Consequence overwrite

Observed harm rewrites the prior route witness instead of creating a revision.

## NC-9 — No-decision erasure

Pause or escalation is removed because the interface requires one winner.

## NC-10 — Route portfolio collapse

Distinct conditional routes are merged into one apparent consensus route.

## NC-11 — Undeclared decision rule

A recommendation is produced without naming the method.

## NC-12 — Cost-bearer omission

A route improves institutional efficiency by shifting labor to an unrepresented applicant, but the cost is absent.

---

# 18. Positive demonstrations

I.2 includes seven required demonstrations.

## PD-1 — Two Pareto-efficient routes

Two nondominated routes remain available.

No hidden final optimizer selects between them.

## PD-2 — Protected condition blocks efficient route

A route dominates on cost and speed but violates a protected condition.

The gate fails.

## PD-3 — Missing standing pauses action

A materially affected center is absent.

The route is paused pending representation or competent outer-loop review.

## PD-4 — Route portfolio

Two legitimate paths remain available under different branch conditions.

The portfolio preserves plurality.

## PD-5 — Event-generated witness

A DecisionWitness is generated from actual navigation and gate events.

## PD-6 — Consequence-driven revision

Observed consequence causes route modification and a new witness version.

## PD-7 — Recommendation remains recommendation

A model recommends a route.

Execution remains blocked until separate authorization.

---

# 19. Conformance additions

I.2 adds the following P2/P3 requirements:

- field classifications;
- route and cost-bearer records;
- declared decision rule;
- protected-condition review;
- governance-gate composition;
- no-decision states;
- model-recommendation boundary;
- event-generated DecisionWitness;
- consequence review and route revision.

P3 additionally requires:

- dissent and unresolved-state preservation;
- route correction after consequence;
- contestable decision-rule source;
- independent witness export.

---

# 20. Security and governance considerations

Navigation systems can be manipulated through:

- route framing;
- omitted alternatives;
- hidden weights;
- strategic protected-condition claims;
- fabricated standing;
- model-generated false consensus;
- delay abuse;
- cost shifting;
- selective consequence measurement.

Implementations SHOULD:

- preserve route-generation provenance;
- expose omitted route classes;
- authenticate authority;
- support challenge to protected status;
- prevent model role expansion;
- record who bears delay;
- separate analysis from authorization;
- review long-running no-decision states.

---

# 21. I.2 non-claims

I.2 does not claim:

- that every route can be compared;
- that Pareto efficiency is fairness;
- that a protected condition is eternal;
- that every cost can be measured;
- that every center has equal decision authority;
- that a route portfolio eliminates conflict;
- that human deliberation guarantees consent;
- that a DecisionWitness is complete beyond its scope;
- that model recommendation is neutral;
- that one method is universally superior.

---

# 22. I.2 completion criterion

I.2 passes when:

1. the seven positive demonstrations validate;
2. the twelve negative cases are detected;
3. two Pareto-efficient routes remain unresolved without hidden scalarization;
4. a protected condition blocks an otherwise efficient route;
5. missing standing causes pause;
6. an event-generated witness validates;
7. consequence causes a new route and witness version;
8. model recommendation remains non-authoritative;
9. H.2 explains source, projection, and mirror without collapsing them.
