---
title: "Semantic Polytelometry G.3: Empirical and Architecture Comparison"
subtitle: "Requirements, Values, Deliberation, Preference Learning, Constitutional Control, and Provenance"
artifact_date: "2026-07-14"
artifact_type: "architecture-comparison-review"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "draft"
processing_tier: 4
source_role: "research-and-architecture-boundary-artifact"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "G.3"
companion_to:
  - "20260714__TELIC-FIELDS__PAPER__CANDIDATE__F-2__dyadic-composition-of-telic-fields.md"
provenance_note: >
  This is a focused architecture comparison, not a systematic review of every
  relevant system. It identifies reusable components, missing safeguards, and
  empirical comparisons for semantic polytelometry. Statements of absence mean
  absence from the reviewed architectures, not proof that no prior system has
  implemented the feature.
---

# Semantic Polytelometry G.3: Empirical and Architecture Comparison

## Executive finding

Semantic polytelometry should not be built as an entirely new stack.

Most of its technical components already exist in neighboring fields:

- goal-oriented requirements engineering models actors, goals, obstacles, dependencies, and refinements;
- i* models intentional actors and strategic dependencies;
- value-sensitive design identifies direct and indirect stakeholders and iteratively studies value conflicts;
- computational argumentation represents claims, reasons, attacks, support, and contestability;
- negotiation and group decision-support systems model preferences, concessions, mediation, and multicriteria tradeoffs;
- deliberation platforms cluster opinion, identify consensus, and summarize large conversations;
- multiobjective optimization and MCDA compare alternatives across several objectives;
- preference-learning systems transform human comparisons into model behavior;
- constitutional AI uses explicit written principles to critique and steer model outputs;
- W3C PROV, model cards, and datasheets document lineage, responsibility, intended use, and limitations.

The proposed architecture is distinctive only if it preserves a combination these systems usually separate:

1. centers of standing, including absent affected centers;
2. source-attributed telic projections;
3. explicit separation of statement, inference, and receiver mirror;
4. consent to telic recruitment and outer-loop use;
5. unresolved remainder rather than forced aggregation;
6. relation-level and emergent teloi;
7. witnessed transformations and corrections;
8. context carrying capacity and stop conditions;
9. non-sovereign model authority;
10. clean exit, revocation, and delegation boundaries.

Within the reviewed literature, no single architecture supplies all ten.

That is a design hypothesis, not a novelty proof.

---

# 1. Evaluation frame

Each neighboring architecture is evaluated against eleven questions.

## 1.1 Standing

Does the method identify all centers materially affected by the system, including indirect or absent participants?

## 1.2 Telic source

Does it preserve whose end, value, goal, or constraint is being represented?

## 1.3 Projection distinction

Does it distinguish the source field from the representation used by the system?

## 1.4 Inference visibility

Can participants see what the machine or analyst inferred rather than received directly?

## 1.5 Authority

Does it represent who may define, revise, delegate, or enforce the goal?

## 1.6 Consent

Does it record whether participants authorized recruitment into the represented purpose and downstream uses?

## 1.7 Plurality

Can it preserve incompatible and unresolved ends without immediate scalarization or consensus?

## 1.8 Witness and provenance

Can it trace transformations, revisions, agents, activities, and derived claims?

## 1.9 Capacity

Can it detect when the system can no longer hold the relevant context or plurality?

## 1.10 Contestability and exit

Can affected participants correct, refuse, revoke, escalate, or leave?

## 1.11 Model non-sovereignty

Does the architecture keep the model's interpretation subordinate to participant and governance authority?

---

# 2. Goal-oriented requirements engineering

Goal-oriented requirements engineering asks why a system should exist before reducing the answer to functional requirements. KAOS models goals, obstacles, responsibilities, refinements, and operationalization. The i* tradition models intentional actors, goals, soft goals, tasks, resources, and strategic dependencies.

These are deep implementation neighbors.

## What GORE already provides

- explicit goals;
- actor responsibility;
- goal decomposition;
- obstacles;
- alternative means;
- dependencies;
- traceability from purpose to requirements;
- conflict and refinement;
- system boundary reasoning.

The i* framework is especially close to dyadic telic composition because it treats actors as intentional and dependencies as sources of both opportunity and vulnerability.

## What semantic polytelometry may add

GORE commonly begins once a goal is available for modeling. It does not necessarily preserve:

- the distinction between a living field and a stated goal;
- whether the goal was inferred or source-confirmed;
- standing of indirect affected centers;
- consent to recruitment into the system goal;
- the difference between a boundary and an objective;
- unresolved internal plurality inside an actor;
- relation-level emergent teloi;
- model-role limits.

## Architecture decision

Do not invent another goal graph.

Use or adapt established actor-goal structures.

Add fields for:

```text
source_center
affected_centers
statement_or_inference
authority
consent_scope
protected_conditions
unacceptable_sacrifices
confidence
expiration
correction_history
outer_loop_routes
```

## Empirical comparison

Compare a standard GORE elicitation process with a telic-projection-enhanced process.

Primary outcome:

> Does the extension change which goals are admitted, which items become constraints, and which stakeholders receive standing?

---

# 3. Value-sensitive design

Value-sensitive design integrates conceptual, empirical, and technical investigations of human values throughout design. Its stakeholder analysis explicitly includes direct and indirect stakeholders, making it one of the strongest neighbors for centers of standing.

## What VSD already provides

- stakeholder identification;
- direct and indirect effects;
- value conflicts;
- iterative inquiry;
- empirical engagement;
- technical investigation;
- long-term and multi-lifespan considerations;
- moral imagination;
- methods for making values visible during design.

## What semantic polytelometry may add

VSD does not by itself require a persistent runtime representation of:

- source-attributed projections;
- participant correction;
- relation-level teloi;
- consent to specific recruitment;
- downstream outer-loop routing;
- witnessed semantic transformations;
- context capacity;
- model inference boundaries.

VSD is primarily a design methodology. Semantic polytelometry is proposed as both a design method and an operational coordination layer.

## Architecture decision

Use VSD methods for:

- stakeholder discovery;
- value elicitation;
- indirect-impact analysis;
- multi-lifespan inquiry;
- public design review.

Do not replace value inquiry with a model-generated telic map.

## Empirical comparison

Test whether persistent projection records improve continuity between VSD's conceptual, empirical, and technical investigations.

---

# 4. Computational argumentation

Computational argumentation models claims, premises, support, attack, acceptability, and reasoning. Recent argumentative-LLM work emphasizes that decisions should be explainable and contestable by exposing an argumentation framework rather than only a final answer.

## What argumentation already provides

- explicit reasons;
- support and attack relations;
- contestability;
- explainability;
- formal evaluation;
- counterargument;
- claim revision;
- structured disagreement.

## What semantic polytelometry may add

An argument graph does not necessarily preserve:

- the center whose future bears the consequence;
- the protected condition behind the argument;
- whether a statement is a goal, fear, boundary, fact, or inference;
- consent to a route;
- nonverbal or low-verbal standing;
- context capacity;
- outer-loop recruitment;
- clean exit.

A strong argument may still represent an illegitimate telos.

A weakly expressed concern may carry protected standing.

## Architecture decision

Use argumentation frameworks for the **reason layer**, not as the whole telic map.

Link arguments to:

```text
projection_id
source_center
claim_type
protected_condition
authority
evidence
confidence
contest_status
```

## Empirical comparison

Test whether standing-linked argument maps reduce the tendency to equate rhetorical strength with legitimate authority.

---

# 5. Negotiation and group decision support

Negotiation-support systems and group decision-support systems represent parties, preferences, offers, concessions, mediation, and tradeoffs. Many integrate AHP, PROMETHEE, utility functions, or other multicriteria methods.

## What these systems already provide

- preference elicitation;
- alternatives;
- concession protocols;
- mediation;
- tradeoff analysis;
- group aggregation;
- agreement support;
- multicriteria comparison.

## What semantic polytelometry may add

Preference and utility representations often underrepresent:

- source uncertainty;
- non-negotiable standing;
- boundaries that must not be traded;
- hidden cost bearers;
- absent centers;
- disagreement inside a participant;
- authority to make concessions;
- relational purpose and exit;
- provenance of changed preferences.

## Architecture decision

Separate four categories before negotiation:

```text
negotiable preference
protected condition
hard boundary
unresolved uncertainty
```

Only the first category should enter ordinary concession logic without further governance.

## Empirical comparison

Compare ordinary multicriteria negotiation with a process that protects boundaries and standing from tradeoff.

Measure agreement quality, later regret, perceived coercion, and breach.

---

# 6. Deliberation platforms

Polis and related platforms use machine intelligence to cluster opinion, identify areas of agreement, and support deliberation at scale. Research on LLM augmentation of Polis shows both substantial promise and risks, including sensitivity to model context limitations.

## What deliberation platforms already provide

- large-scale participation;
- statement collection;
- opinion clustering;
- consensus discovery;
- visualization;
- summarization;
- facilitation;
- public meaning-making.

## What semantic polytelometry may add

Consensus-oriented systems may still lose:

- minority protected conditions;
- why a statement matters;
- authority and affected standing;
- source correction after summarization;
- distinctions between agreement and consent;
- unresolved incommensurability;
- outer-loop implementation consequences;
- context dropped by clustering or summarization.

Consensus is one relational state.

It is not the only legitimate output.

## Architecture decision

A semantic-polytelometric deliberation layer should produce at least:

```text
shared field
conflict field
protected minority field
unresolved field
missing-standing field
candidate route field
```

It should not rank consensus above protected dissent by default.

## Empirical comparison

Compare consensus summaries with telic maps.

Measure:

- participant recognition;
- minority preservation;
- source correction;
- policy relevance;
- false consensus.

---

# 7. Multiobjective optimization and MCDA

Multiobjective optimization represents several objective functions and identifies tradeoffs, often through Pareto-optimal sets. Multi-criteria decision analysis supports structured evaluation of alternatives under several criteria and stakeholder preferences.

## What these methods already provide

- multiple objectives;
- explicit tradeoffs;
- constraints;
- alternatives;
- Pareto frontiers;
- sensitivity analysis;
- interactive preference elicitation;
- decision support.

## What semantic polytelometry may add

Optimization does not determine whether the objective set is constitutionally adequate.

Before optimization, a system must ask:

- Who defined the objective?
- Which center is absent?
- Which item is not commensurable?
- Which item is a boundary?
- Which cost is externalized?
- What authority supports the weight?
- What remains uncertain?
- Who may refuse the decision model?

## Architecture decision

Semantic polytelometry should export a **decision-ready subset**, not its entire field, into optimization.

The export must identify:

```text
objectives
constraints
protected invariants
non-comparable remainder
authority
affected centers
confidence
review triggers
```

## Empirical comparison

Test whether the pre-optimization layer changes:

- objective inclusion;
- constraint classification;
- weighting;
- choice of alternatives;
- participant consent to the model.

---

# 8. Preference learning and DPO

Preference learning converts comparisons, ratings, demonstrations, or choices into model behavior. Direct Preference Optimization simplifies alignment by optimizing directly from preferred and dispreferred outputs without an explicit reward-modeling pipeline.

## What preference learning already provides

- scalable feedback;
- pairwise comparisons;
- policy steering;
- learning from demonstrations;
- personalized or aggregate preferences;
- empirical model improvement.

## Structural concern

Preference learning compresses human judgment into a training signal.

The process may erase:

- who preferred what;
- why;
- under which context;
- whether the preference was weak or protected;
- conflicts among participants;
- uncertainty;
- changes over time;
- consent for downstream model use.

The learned model then behaves as though the compressed preference relation were an operative objective.

## Architecture decision

Semantic polytelometry should not replace preference learning. It should constrain when preference data may be converted into optimization.

A **projection-to-training gate** should require:

- provenance;
- use consent;
- scope;
- aggregation policy;
- dissent policy;
- withdrawal policy;
- temporal validity;
- protected categories;
- uncertainty retention.

## Empirical comparison

Compare a preference-trained model with a source-attributed, retrieval-time telic map.

Test:

- personalization;
- correction;
- plurality retention;
- withdrawal;
- cross-context misuse.

---

# 9. Constitutional AI

Constitutional AI uses written principles to guide model critique, revision, and AI-generated preference feedback. It demonstrates that an explicit normative layer can steer model behavior with reduced direct human labeling.

## What Constitutional AI already provides

- explicit principles;
- critique and revision;
- principle-conditioned judgment;
- AI-generated feedback;
- behavioral steering;
- a visible concept of model constitution.

## What semantic polytelometry may add

A constitution is itself a telic projection.

The important questions are:

- Who authored it?
- Whose standing does it represent?
- What authority does it claim?
- What conflicts exist among principles?
- What happens when a participant's local field conflicts with the provider constitution?
- Can the constitution be inspected, forked, or locally replaced?
- What outer institutional teloi remain hidden?

## Architecture decision

Treat the model constitution as one declared field inside the map, not as the neutral frame of the map.

Record:

```text
principle
author
authority
scope
priority
conflicts
revision process
provider interest
participant override rules
```

## Empirical comparison

Test whether exposing the constitution as a participant-visible telic projection improves trust, contestability, and correct use.

---

# 10. Provenance standards and documentation

W3C PROV provides a domain-agnostic model for entities, activities, agents, derivations, responsibility, bundles, and provenance exchange. Model cards and datasheets document intended use, composition, evaluation, limitations, and responsible deployment.

These are essential substrates.

## What provenance and documentation already provide

- entities and activities;
- agents and responsibility;
- derivation;
- generation and use;
- revision;
- provenance of provenance;
- intended use;
- limitations;
- dataset motivation and collection;
- evaluation context.

## What semantic polytelometry may add

Standard provenance does not automatically encode:

- standing;
- consent to telic recruitment;
- source field versus inferred projection;
- protected conditions;
- authority to revise purpose;
- context capacity;
- unresolved remainder;
- exit or revocation;
- relational teloi.

Documentation can also become static while the field changes.

## Architecture decision

Extend rather than replace W3C PROV.

Candidate mapping:

```text
telic projection       -> prov:Entity
projection estimation  -> prov:Activity
source center           -> prov:Agent
model mediator          -> prov:SoftwareAgent
correction              -> prov:Revision / derivation
witness bundle          -> prov:Bundle
consent event           -> domain extension
standing relation       -> domain extension
authority envelope      -> domain extension
```

Model cards and datasheets should describe the model and dataset.

Telic records should describe the live relation and its authorized use.

---

# 11. Comparison matrix

| Architecture | Strong contribution | Typical missing layer for semantic polytelometry |
|---|---|---|
| GORE / KAOS | Goals, obstacles, refinement, responsibility | Field/projection distinction, consent, absent standing |
| i* | Intentional actors and dependencies | Source correction, witness, runtime consent |
| Value-sensitive design | Direct and indirect stakeholders, value conflicts | Persistent operational projection and authority records |
| Computational argumentation | Reasons, attacks, support, contestability | Standing, boundaries, nonverbal concerns |
| Negotiation support | Preferences, concessions, mediation | Protected conditions, outer-loop routing |
| Deliberation platforms | Scale, clustering, consensus, summarization | Minority standing, consent, unresolved remainder |
| MCDA / MOO | Tradeoffs, Pareto alternatives, sensitivity | Legitimation of objectives and weights |
| Preference learning / DPO | Scalable behavior steering | Provenance, plurality, withdrawal, context |
| Constitutional AI | Explicit principles and critique | Constitution authorship, authority, forkability |
| W3C PROV | Interoperable provenance and derivation | Telic standing, consent, capacity |
| Model cards / datasheets | Intended use, limitations, dataset context | Live relation state and participant correction |

No row is a failed approach.

Each supplies part of the eventual architecture.

---

# 12. Candidate semantic-polytelometry architecture

The comparison supports a modular architecture.

## 12.1 Standing registry

Records:

```text
center_id
center_type
representation_authority
affected_scope
delegates
boundaries
status
```

It must support absent or represented centers without pretending the representative is identical to the center.

## 12.2 Projection capture

Stores source-approved projections:

```text
projection_id
source_center
scope
time
desired_states
avoided_states
protected_conditions
unacceptable_sacrifices
uncertainty
expiration
```

## 12.3 Inference ledger

Separates model interpretation from source statement:

```text
inference
supporting_evidence
model
confidence
known_alternatives
source_review_status
```

## 12.4 Mirror return

Allows receivers and models to disclose what they believe they understood.

The source may correct the mirror without rewriting the historical record.

## 12.5 Relation graph

Represents:

- centers;
- projections;
- dependencies;
- shared ends;
- conflicts;
- boundaries;
- emergent relation-level teloi;
- outer-loop enrollment.

## 12.6 Consent and authority envelope

Records:

```text
authorized_actions
authorized_purposes
duration
data_use
delegation
outer_loop_routes
revocation
exit
```

## 12.7 Comparison engine

Produces:

```text
shared field
compatible field
conditional field
conflict field
protected field
unresolved field
missing-standing field
```

It does not determine the winner.

## 12.8 Route generator

Proposes alternatives with:

```text
preserved_conditions
sacrificed_conditions
cost_bearers
required_consent
reversibility
review_trigger
```

## 12.9 Witness and provenance layer

Uses interoperable provenance concepts to record:

- source;
- activity;
- derivation;
- revision;
- responsible agent;
- transformation;
- bundle.

## 12.10 Context capacity monitor

Tracks whether the active process still represents enough relevant difference for the stakes.

Possible signals:

- missing centers;
- unresolved contradiction count;
- summary compression ratio;
- correction frequency;
- uncertainty loss;
- minority disappearance;
- context-window truncation;
- participant overload.

## 12.11 Stop and escalation controller

When capacity or authority fails, the system must:

- pause;
- narrow scope;
- request clarification;
- restore omitted context;
- recruit a witness;
- route to a competent outer loop;
- refuse;
- support exit.

## 12.12 Decision-system adapters

Export governed subsets into:

- GORE;
- argumentation frameworks;
- MCDA;
- multiobjective optimization;
- deliberation platforms;
- negotiation protocols;
- project management;
- smart contracts.

The adapter must preserve links back to the source telic records.

---

# 13. Minimal data objects

## 13.1 Telic Projection Record

```yaml
projection_id:
source_center:
scope:
effective_time:
expires:
statement:
desired_states: []
avoided_states: []
protected_conditions: []
unacceptable_sacrifices: []
authority:
consent_status:
uncertainty:
provenance:
corrections: []
```

## 13.2 Polytelometric Comparison Record

```yaml
comparison_id:
projections: []
shared: []
compatible: []
conditional: []
conflicting: []
protected: []
unresolved: []
missing_standing: []
model_inferences: []
participant_corrections: []
```

## 13.3 Route Record

```yaml
route_id:
preserves: []
sacrifices: []
cost_bearers: []
required_authority: []
required_consent: []
reversibility:
review_trigger:
witness_requirements:
```

## 13.4 Capacity Record

```yaml
capacity_id:
represented_centers:
protected_conditions:
unresolved_conflicts:
temporal_span:
provenance_retained:
uncertainty_retained:
participant_load:
model_context_status:
stop_condition:
```

These are research objects, not final Phase I specifications.

---

# 14. Empirical program

## Study A — Requirements comparison

Compare ordinary GORE with telic-enhanced GORE.

Outcomes:

- stakeholder coverage;
- objective changes;
- constraint changes;
- traceability;
- participant recognition;
- late requirement reversal.

## Study B — Deliberation comparison

Compare:

- ordinary summary;
- consensus summary;
- argument map;
- polytelometric map.

Outcomes:

- source recognition;
- minority preservation;
- correction;
- false consensus;
- decision usefulness.

## Study C — Negotiation comparison

Compare ordinary preference elicitation with projection-plus-boundary elicitation.

Outcomes:

- agreement;
- later regret;
- perceived coercion;
- breach;
- durability.

## Study D — Preference-learning comparison

Compare:

- DPO-trained model;
- personalized preference model;
- retrieval-time source-attributed telic map.

Outcomes:

- correction;
- withdrawal;
- context transfer;
- plurality;
- user control.

## Study E — Constitutional transparency

Expose or hide the model constitution and provider constraints.

Outcomes:

- trust calibration;
- appropriate reliance;
- contestability;
- participant consent.

## Study F — Provenance and witness

Compare raw transcript, static summary, PROV-linked summary, and source-correctable witness record.

Outcomes:

- dispute resolution;
- transformation legibility;
- correction latency;
- attribution accuracy.

---

# 15. Core evaluation metrics

## Standing coverage

What percentage of materially affected centers are represented?

## Source fidelity

Can each represented end be traced to a source statement, authorized delegate, or explicit inference?

## Correction latency

How long does an incorrect interpretation remain operative after correction becomes available?

## Unresolved-remainder preservation

Does the system retain material disagreement that does not fit the selected route?

## Authority legibility

Can users determine who may define, revise, or enforce each objective or constraint?

## Consent validity

Was the action authorized for its actual purpose, scope, duration, and downstream use?

## Context sufficiency

Did the active process preserve the differences required for the stakes?

## Route reversibility

Can the system return, revise, fork, or exit without disproportionate loss?

## Provenance completeness

Can transformations be reconstructed across agents and activities?

## Non-sovereignty

Can participants correct or reject the model's interpretation without first persuading the model that they are right?

---

# 16. Failure risks

## 16.1 Administrative overgrowth

The record structure may become too costly for ordinary relations.

Mitigation: progressive disclosure and scope-sensitive profiles.

## 16.2 Confessional extraction

Projection capture may pressure people to reveal more than the relation requires.

Mitigation: minimum-necessary projection and protective omission.

## 16.3 Model reification

Participants may treat a generated map as a diagnosis or true field.

Mitigation: visible inference, correction, and expiration.

## 16.4 Power laundering

An institution may use procedural consent records to legitimize structurally coercive choices.

Mitigation: standing, exit realism, and outer-loop review.

## 16.5 Consensus bias

Shared-field outputs may suppress protected dissent.

Mitigation: separate shared, protected, and unresolved outputs.

## 16.6 Infinite context

The system may continually request more information instead of deciding.

Mitigation: capacity-aware scope, satisficing, and explicit remainder.

## 16.7 Provenance surveillance

A complete record may become a coercive surveillance substrate.

Mitigation: selective disclosure, retention limits, local custody, and provenance abstraction.

## 16.8 False neutrality

The model's provider constitution and training history may remain outside the map.

Mitigation: model and provider telic disclosures.

---

# 17. Architecture conclusion

Semantic polytelometry should be built as an orchestration layer across established disciplines.

It should borrow:

- actor-goal graphs from requirements engineering;
- stakeholder discovery from value-sensitive design;
- contestability from computational argumentation;
- tradeoff methods from negotiation and MCDA;
- scale and clustering from deliberation systems;
- optimization from multiobjective methods;
- principle visibility from constitutional AI;
- lineage from W3C PROV;
- deployment disclosure from model cards and datasheets.

It should add:

- standing;
- projection versus field;
- inference visibility;
- consent to telic recruitment;
- unresolved remainder;
- context carrying capacity;
- relation-level purpose;
- non-sovereign model authority;
- clean exit.

The architecture is justified only if these additions produce measurable improvements.

Without that evidence, semantic polytelometry is a useful vocabulary around existing tools.

With that evidence, it may become a distinct coordination layer.

---

# 18. Next research questions

- What is the smallest record that preserves the claimed advantage?
- Which fields must remain qualitative?
- Which parts can safely enter vectors or utility models?
- How should absent centers be represented?
- How can consent be meaningful under structural dependence?
- How should model constitutions enter the comparison graph?
- Can provenance remain useful without becoming surveillance?
- What capacity signals reliably predict standing loss?
- What is the correct outer loop when a dyad cannot continue?
- How should the architecture behave when participants reject the same witness?

---

# Primary references

Bai, Yuntao, et al. “Constitutional AI: Harmlessness from AI Feedback.” arXiv:2212.08073, 2022.

Friedman, Batya, David G. Hendry, and Alan Borning. “A Survey of Value Sensitive Design Methods.” *Foundations and Trends in Human–Computer Interaction* 11, no. 2, 2017.

Freedman, Gabriel, et al. “Argumentative Large Language Models for Explainable and Contestable Claim Verification.” arXiv:2405.02079, 2024.

Gebru, Timnit, et al. “Datasheets for Datasets.” arXiv:1803.09010; later *Communications of the ACM* 64, no. 12, 2021.

Mitchell, Margaret, et al. “Model Cards for Model Reporting.” arXiv:1810.03993; FAT* 2019.

Moreau, Luc, and Paolo Missier, eds. *PROV-DM: The PROV Data Model*. W3C Recommendation, 2013.

Rafailov, Rafael, et al. “Direct Preference Optimization: Your Language Model Is Secretly a Reward Model.” arXiv:2305.18290, 2023.

Small, Christopher T., et al. “Opportunities and Risks of LLMs for Scalable Deliberation with Polis.” arXiv:2306.11932, 2023.

van Lamsweerde, Axel. “Goal-Oriented Requirements Engineering: A Guided Tour.” Proceedings of the Fifth IEEE International Symposium on Requirements Engineering, 2001.

Yu, Eric S. K. “Towards Modelling and Reasoning Support for Early-Phase Requirements Engineering.” Proceedings of the Third IEEE International Symposium on Requirements Engineering, 1997.
