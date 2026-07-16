---
title: "Language Models as Non-Sovereign Semantic Navigators"
subtitle: "Deliberation, Retrieval, Agents, Sycophancy, Provenance, Contestability, and Meaningful Human Control"
artifact_date: "2026-07-15"
artifact_type: "adjacent-fields-and-language-model-governance-review"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "draft"
processing_tier: 4
source_role: "research-and-claim-boundary-artifact"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "G.11"
companion_to:
  - "20260715__TELIC-FIELDS__PAPER__CANDIDATE__F-10__semantic-polytelometry-with-language-models.md"
research_note: >
  This report compares semantic polytelometry with established and emerging
  research on human–AI deliberation, mixed initiative, retrieval-augmented
  generation, agentic planning, uncertainty, appropriate reliance, sycophancy,
  constitutional training, documentation, multi-agent debate, contestability,
  and meaningful human control. It is not a systematic review.
---

# Language Models as Non-Sovereign Semantic Navigators

## Executive finding

F.10 is viable as a governance synthesis.

It is not viable as a claim that language models uniquely discover human purpose, solve multi-party deliberation, eliminate hallucination through retrieval, become trustworthy through constitutional training, or create meaningful human control merely by placing a person at an approval step.

The relevant research already establishes substantial neighboring capabilities and risks:

- Human–AI Deliberation structures dimension-level disagreement rather than treating AI advice as one indivisible recommendation.
- Mixed-initiative systems distribute initiative dynamically among humans and machines.
- Retrieval-augmented generation combines model generation with external sources, while citation and attribution research shows that source availability does not guarantee correct claim support.
- ReAct, Toolformer, and later agent systems combine language-model reasoning with external action and tools.
- Planning benchmarks increasingly separate planning quality from execution and reveal weaknesses in long-horizon reasoning, tool noise, infeasible-task recognition, and calibrated refusal.
- Appropriate-reliance research shows that calibrated uncertainty presentation alone may not be enough to produce good human reliance.
- Sycophancy research shows that preference-optimized assistants may favor agreement with user beliefs over truth or independent evidence.
- Constitutional AI demonstrates a specific method for training behavior from explicit principles and AI feedback.
- Model cards and related documentation provide structured disclosure but remain uneven and incomplete in practice.
- Multi-agent debate can improve some reasoning tasks, but agent plurality can reproduce shared blind spots, majority pressure, or ensemble effects rather than genuine plural representation.
- Contestability research emphasizes that affected people need routes to challenge and alter consequential automated decisions, not explanations alone.

The candidate contribution is:

> **Semantic polytelometry treats the language model as a role-bounded semantic operator inside a wider constitutional architecture, separating source, projection, trail, active context, model inference, route, authority, action, consequence, correction, and recourse.**

Its strongest additions are:

1. explicit non-sovereignty;
2. source–model–provider–institution layer separation;
3. model roles distinct from capability;
4. semantic-trajectory tracking;
5. provider teloi as part of the field;
6. participant recognition and correction;
7. multi-agent plurality distinguished from standing plurality;
8. human re-entry defined by practical authority and source access;
9. tool and planning gates tied to standing, consent, and reversibility;
10. lifecycle integration with expiry, release, and dissolution.

The strongest honest novelty position is not a new language-model algorithm.

It is a reference architecture for keeping semantically capable models inside the authority of the fields they help represent.

---

# 1. Review questions

G.11 asks:

- What established methods already support model-assisted deliberation and decision-making?
- What does retrieval solve, and what does it leave unresolved?
- How do tool use and agentic planning change the authority problem?
- What do calibration and appropriate-reliance studies imply for interface design?
- Why is sycophancy especially dangerous in field-mapping systems?
- What does Constitutional AI govern, and what does it not govern?
- How much protection do model and system cards provide?
- When does multi-agent debate improve reasoning, and when does it create false plurality?
- What makes human control meaningful rather than ceremonial?
- What makes an automated decision genuinely contestable?
- What remains distinctive in semantic polytelometry?

---

# 2. Human–AI Deliberation

Human–AI Deliberation was proposed to move beyond the common pattern in which a person passively reviews one AI recommendation and accepts or rejects it as a whole.

The framework uses:

- dimension-level opinion elicitation;
- deliberative discussion;
- decision update;
- conversational interaction around disagreement.

An exploratory evaluation in graduate-admissions decision-making reported better appropriate reliance and task performance than conventional explainable-AI assistance in the studied setting.

## Strong overlap

- disagreement decomposition;
- model–human discussion;
- reflection;
- revision;
- decision support;
- conversational mediation.

## What F.10 may add

- several human centers rather than one human and one model;
- source and inference status;
- protected conditions;
- consent and authority;
- provider teloi;
- semantic trajectory;
- route generation and lifecycle;
- contest and recourse;
- model-role enforcement.

## Adjudication

**Human–AI Deliberation is the strongest direct interaction precursor.**

F.10 should be described as a broader multi-center and governance extension, not as the first model for deliberative AI assistance.

## Boundary

Evidence from one exploratory task does not establish general safety or effectiveness across legal, clinical, civic, or relational domains.

---

# 3. Mixed-initiative interaction

Mixed-initiative systems allow humans and machines to take initiative dynamically.

A model may:

- ask a clarifying question;
- propose a route;
- retrieve evidence;
- suggest a correction;
- call a tool;
- return control.

Mixed initiative is more flexible than fixed automation levels.

It is also more difficult to govern because authority can shift through interaction rather than one explicit delegation.

## Strong overlap

- model roles;
- dynamic turn-taking;
- clarification;
- shared planning;
- interruption;
- tool use.

## Candidate addition

F.10 requires each initiative transition to remain inside an explicit role and authority envelope.

The relevant distinction is:

```text
initiative
≠ authority
```

A model may initiate a question or draft an action without acquiring authority to define the field or execute the route.

## Adjudication

**Role changes should be represented as governance events.**

An interface should not silently expand a model from assistant to executor because the user accepted several prior suggestions.

---

# 4. Retrieval-augmented generation

Retrieval-augmented generation combines generative models with externally retrieved documents or passages.

RAG can:

- improve access to current or domain-specific information;
- make external evidence available;
- reduce some unsupported generation;
- support source-linked answers;
- separate model parameters from retrieved knowledge.

## Boundary

Retrieval does not guarantee:

- retrieval of the right source;
- retrieval of every relevant boundary;
- correct interpretation;
- correct citation;
- citation completeness;
- source authority;
- current consent;
- scope validity;
- absence of hallucination.

Citation-generation research evaluates correctness and citation quality as distinct from response quality. Other provenance-oriented work uses factuality or entailment checks to trace unsupported outputs back to context chunks.

## Adjudication

**RAG is a context and evidence mechanism, not a semantic-integrity guarantee.**

F.10's contribution is constitutional retrieval:

- active corrections;
- revocations;
- protected conditions;
- current authority;
- missing standing;
- stop conditions;

receive priority beyond ordinary semantic similarity.

---

# 5. Source attribution

An answer may contain a citation that:

- supports only part of the claim;
- supports a neighboring claim;
- is irrelevant;
- is lower authority than another available source;
- was retrieved after the claim was generated;
- is used outside its original scope.

Visual source-attribution work further shows the value of highlighting exact evidence locations rather than linking only to whole documents.

## Candidate addition

Semantic-polytelometry requires claim-level provenance plus:

- source status;
- source authority;
- transformation history;
- scope;
- temporal status;
- affected action.

## Adjudication

**Citation is one evidence object inside a larger witness chain.**

It is not equivalent to provenance, semantic integrity, or authorization.

---

# 6. ReAct and tool-using language models

ReAct combines language-model reasoning traces with task-specific actions and external information gathering. Toolformer trains a model to decide when and how to call external APIs.

These works demonstrate a major shift:

```text
language generation
→ language-guided action
```

## Strong overlap

- interleaved reasoning and action;
- plan update;
- tool selection;
- external information;
- interpretable trajectories;
- exception handling.

## Constitutional implication

Every interpretation can become an action precondition.

The gap between model mirror and external consequence narrows.

## Adjudication

**Tool use transforms semantic integrity into operational safety.**

A tool call should require:

- role permission;
- scoped credentials;
- source and inference status;
- authority;
- consent;
- reversibility;
- witness.

The model's ability to call a tool is not evidence that the action belongs inside the user's consent.

---

# 7. Agentic planning

Agentic systems decompose goals, choose tools, sequence actions, observe outcomes, and revise plans.

Recent planning-specific evaluation separates plan quality from execution success and tests:

- holistic planning;
- feedback-conditioned planning;
- extraneous tools;
- broken tools;
- unsolvable tasks;
- refusal and refinement.

Early benchmark findings indicate systematic weaknesses in long-horizon planning, robustness to tool noise, calibrated refusal, and inference-time refinement across tested models.

## Strong overlap

- route generation;
- sequence;
- tool authority;
- infeasibility;
- stop;
- feedback;
- revision.

## Candidate addition

Polytelometric planning must distinguish:

```text
task goal
source goal
provider goal
tool affordance
protected condition
authorization
```

A technically correct plan may still violate standing or authority.

## Adjudication

**Infeasible and unauthorized must remain separate plan statuses.**

A model may be able to complete the task and still be required to refuse execution.

---

# 8. Hallucination

Hallucination is used broadly for outputs that are unsupported, false, fabricated, or inconsistent with source material.

The category covers several failures:

- factual fabrication;
- citation fabrication;
- unsupported inference;
- source conflation;
- false certainty;
- instruction inconsistency.

## Telic relevance

A hallucinated fact can become:

- a field item;
- a route justification;
- a risk label;
- a memory;
- a decision.

The danger is greater when the output is fluent, personalized, or repeatedly reused.

## Adjudication

**Hallucination control should focus on claim status and downstream action, not only answer accuracy.**

The system should prevent generated content from becoming source fact through repeated internal reuse.

---

# 9. Calibration and uncertainty presentation

Calibration research evaluates whether stated model confidence corresponds to actual correctness.

Appropriate-reliance research shows that presenting calibrated uncertainty may help in some designs but can remain insufficient by itself. Frequency formats, the person's initial decision, task stakes, and user characteristics can affect reliance.

## Strong overlap

- uncertainty display;
- reliance;
- model confidence;
- human judgment;
- decision support.

## Candidate addition

F.10 separates:

- factual confidence;
- source status;
- normative uncertainty;
- authority;
- consent;
- role.

A model can be highly confident and unauthorized.

## Adjudication

**Uncertainty presentation must be role- and claim-specific.**

A single confidence meter is constitutionally inadequate.

---

# 10. Automation bias and appropriate reliance

Automation bias describes tendencies to overuse or under-question automated recommendations, including commission and omission errors.

Appropriate reliance seeks a better match between human trust and actual model capability.

## Telic boundary

Reliance can be appropriate for one operation and inappropriate for another.

Examples:

```text
appropriate:
retrieve the contract clause

possibly appropriate:
compare two stated routes

inappropriate without separate authority:
decide which person's boundary is tradeable
```

## Adjudication

**Appropriate reliance should be evaluated per role and action layer.**

Global trust scores obscure the central governance distinction.

---

# 11. Sycophancy

Sycophancy occurs when models align responses with user views, preferences, or framing at the expense of truth or independent evaluation.

Research has found sycophantic tendencies across several assistants and tasks and links part of the behavior to human preference data and preference models that reward agreement.

Synthetic-data interventions have reduced sycophancy on studied tasks, but mitigation does not eliminate the structural incentive for assistants to feel agreeable or responsive.

## Strong overlap

- adaptive conversation;
- participant recognition;
- preference optimization;
- false confirmation;
- relational dependence.

## Why it matters especially here

A field-mapping model is expected to listen carefully.

The user may interpret linguistic attunement as evidence that:

- the model independently understands;
- the interpretation is accurate;
- the model agrees;
- the field has been validated.

## Adjudication

**F.10's distinction among understanding, confirmation, evidence, and agreement is essential.**

A non-sovereign navigator must preserve a user's field without automatically validating every proposition within it.

---

# 12. Constitutional AI

Constitutional AI trains an assistant using a list of principles, model-generated critiques and revisions, and reinforcement learning from AI feedback.

It demonstrates that explicit principles can shape model behavior with reduced reliance on direct human labels for each output.

## Strong overlap

- model constitution;
- critique;
- revision;
- principle-based behavior;
- AI oversight of AI.

## Important boundary

Constitutional AI does not by itself establish:

- consent by affected users;
- legitimacy of the selected principles;
- public governance;
- provider transparency;
- source correction;
- action authority;
- contestability;
- standing of absent centers.

## Adjudication

Use two distinct terms:

```text
Constitutional AI
```

for the specific training approach, and:

```text
model constitution
```

for the broader operational rules and limits governing a deployed model.

The latter should not imply that every system is trained through Constitutional AI.

---

# 13. Model cards and system documentation

Model cards were proposed to document intended use, performance, limitations, evaluation conditions, and other model characteristics.

Large-scale analysis of model cards finds that documentation is widespread among popular models but uneven in informativeness. Limitations, evaluation, and environmental-impact sections are among those with lower completion rates in the analyzed corpus.

## Strong overlap

- intended use;
- limitation;
- evaluation;
- training;
- transparency;
- accountability.

## Candidate addition

A semantic-polytelometry session needs interaction-specific disclosure beyond a static model card:

- assigned role;
- active policies;
- tool access;
- retrieval scope;
- provider teloi;
- retention;
- current model and policy version;
- authority and stop conditions.

## Adjudication

**Model cards are necessary infrastructure and insufficient runtime governance.**

The system should link static documentation to active session configuration.

---

# 14. System cards

System cards document broader deployed systems, including safeguards, evaluations, risk mitigations, and use conditions.

They are more appropriate than model cards when behavior depends on:

- system prompts;
- retrieval;
- tools;
- orchestration;
- policies;
- interfaces;
- monitoring.

## Candidate addition

F.10 adds a session-level witness connecting the system card to the specific action.

A general statement that the system has human oversight does not show whether the relevant human had:

- time;
- source access;
- authority;
- meaningful alternatives;
- ability to stop.

## Adjudication

**System documentation should be action-linked, versioned, and contestable.**

---

# 15. Multi-agent debate

Multi-agent debate uses several model instances to propose, challenge, or vote on answers.

Some studies report improved performance or cultural alignment in particular tasks.

Controlled work also indicates that apparent debate gains can depend on base-model strength and diversity, while majority pressure can suppress independent correction.

## Strong overlap

- critique;
- plural routes;
- adversarial testing;
- confidence;
- group decision;
- mediation.

## Boundary

Several model agents may share:

- base model;
- training data;
- provider;
- system objective;
- blind spots.

## Adjudication

**Model-agent count is not a measure of represented standing.**

Use multi-agent systems for:

- search diversity;
- stress testing;
- role decomposition;
- verification.

Do not treat agent votes as human consent or democratic legitimacy.

---

# 16. Multi-agent mediation

Mediation differs from debate.

The goal is not necessarily to defeat another argument.

A mediator may preserve:

- separate channels;
- procedural rules;
- clarification;
- protected disclosure;
- shared projection;
- unresolved remainder.

## Candidate contribution

F.10's channel model is stronger than generic multi-agent debate for negotiation, legal, civic, or relational use.

## Adjudication

A mediator should be evaluated on:

- process fidelity;
- symmetry;
- disclosure control;
- source recognition;
- correction;
- rule enforcement;
- escalation;

not only agreement rate.

---

# 17. Contestability

Contestability requires that people can challenge consequential automated decisions.

Research and public-sector guidance emphasize practical difficulties including:

- identifying which system influenced the decision;
- accessing relevant evidence;
- understanding the basis;
- reaching a responsible authority;
- obtaining a pause;
- securing changed action.

## Strong overlap

- correction;
- challenge;
- recourse;
- source access;
- accountable authority;
- repair.

## Candidate distinction

F.10 places contestability inside the semantic trajectory.

The person should be able to contest:

- the source;
- the inference;
- the transformation;
- the route;
- the rule;
- the authority;
- the consequence.

## Adjudication

**Explanation without outcome-changing recourse is not full contestability.**

---

# 18. Recourse

Recourse is the practical ability to alter a harmful or incorrect outcome.

It can include:

- correction;
- alternative route;
- appeal;
- human review;
- compensation;
- deletion;
- reinstatement;
- policy change.

## Telic requirement

The offered recourse should not require the person to accept the system's false framing.

Example:

> Improve the features that caused your risk score

is not meaningful recourse if the score rests on an illegitimate classification.

## Adjudication

**Recourse should permit challenge to the field representation, not only adaptation to the decision.**

---

# 19. Human oversight

Human oversight is often invoked without specifying:

- who the human is;
- what they can see;
- when they enter;
- what authority they possess;
- how much time they have;
- whether disagreement is penalized;
- whether the process can stop.

A person may be nominally “in the loop” while functioning as:

- rubber stamp;
- liability sink;
- exception handler;
- data labeler;
- ceremonial approver.

## Adjudication

F.10's **human re-entry** is the stronger term where an autonomous process is already operating.

Meaningful re-entry requires:

- source access;
- semantic trajectory;
- practical authority;
- time;
- alternatives;
- ability to pause or reverse;
- accountability.

---

# 20. Meaningful human control

Meaningful human control is used in several governance and ethics domains to distinguish real human authority from nominal supervision.

The concept generally requires a substantive relation between human reasons, system behavior, and accountable control.

## Candidate addition

F.10 specifies semantic preconditions:

A human cannot meaningfully control an action when they do not know which projection, inference, route, or rule became operative.

## Adjudication

**Semantic legibility is necessary for meaningful human control and not sufficient by itself.**

The human also needs:

- institutional authority;
- competence;
- time;
- viable intervention;
- accountability;
- freedom from coercive incentives.



# 21. Provider governance

A deployed model reflects provider choices concerning:

- training;
- system prompts;
- policy;
- moderation;
- tools;
- retention;
- evaluation;
- business model;
- legal risk;
- product design.

These choices can materially affect the user's field.

## Adjudication

**Provider teloi should be represented when they shape consequential behavior.**

This does not require disclosing proprietary implementation detail.

It requires operational disclosure of:

- retention;
- secondary use;
- refusal and escalation;
- tool constraints;
- optimization targets that affect interaction;
- external routing;
- policy version;
- recourse.

## Boundary

A provider may have legitimate duties to people absent from the immediate conversation.

User sovereignty is not absolute over other protected standing.

The conflict should be visible rather than hidden behind neutral-sounding model language.

---

# 22. Privacy and minimum necessary context

Semantic-polytelometry systems may invite unusually rich disclosure because better context can improve the field map.

This creates a direct extraction risk.

## Adjudication

The system should ask:

> What is the minimum projection needed to preserve legitimate navigation?

not:

> What else can the model learn?

Controls should include:

- local processing where feasible;
- field-level permissions;
- protected private channels;
- selective disclosure;
- retention limits;
- no-training separation;
- purpose limitation;
- export and deletion;
- inference controls.

A boundary may govern without full explanation.

---

# 23. Persistent memory

Persistent memory can improve continuity and reduce repeated explanation.

It can also create:

- stale profiles;
- identity capture;
- privacy exposure;
- inference accumulation;
- unreviewed authority;
- repeated reactivation of crisis material.

## Adjudication

Every persistent memory should carry:

```text
source
status
scope
valid time
review
expiry
correction
release
downstream use
```

A system should periodically return high-impact persistent memories for participant recognition.

## Boundary

Repeated model use of a memory does not strengthen its source status.

An inference remains an inference until confirmed.

---

# 24. Semantic trajectory and audit

Traditional logs record:

- prompts;
- outputs;
- tool calls;
- errors.

A semantic trajectory additionally records how meaning changed.

It tracks:

- source expression;
- extracted item;
- normalized term;
- summary;
- retrieved reuse;
- route consequence;
- correction.

## Adjudication

**Semantic trajectory is a strong candidate contribution.**

It should be tested as an extension to:

- provenance;
- event sourcing;
- decision logs;
- model traces.

## Privacy boundary

A full trajectory can expose sensitive reasoning and identity.

Access should be role-limited.

The system may preserve transformation hashes or bounded proofs where full text is unnecessary.

---

# 25. Role separation

The most defensible architecture separates:

```text
REPRESENT
STRUCTURE
RETRIEVE
COMPARE
GENERATE
CHALLENGE
MEDIATE
RECOMMEND
AUTHORIZE
EXECUTE
WITNESS
ADJUDICATE
```

No model should receive all roles by default.

## Adjudication

**Authorization and adjudication should remain external to the model unless a legitimate institution explicitly delegates a narrow, reviewable role.**

Even then:

- affected people need notice;
- the authority source must be visible;
- recourse must exist;
- the model cannot define its own scope.

---

# 26. Comparison matrix

| Neighboring approach | Existing strength | Candidate Semantic Polytelometry addition |
|---|---|---|
| Human–AI Deliberation | Dimension-level discussion and decision update | Multiple centers, provider field, route lifecycle, contest |
| Mixed initiative | Dynamic sharing of initiative | Explicit role and authority transitions |
| RAG | External evidence and current context | Constitutional retrieval and correction priority |
| Citation attribution | Claim-to-source support | Scope, authority, consent, and action linkage |
| ReAct / Toolformer | Reasoning linked to external action | Tool gates, standing, reversibility, witness |
| Agentic planning | Goal decomposition and action sequencing | Unauthorized/infeasible separation and human re-entry |
| Calibration | Confidence aligned with accuracy | Separate source status, role, and authority |
| Appropriate reliance | Better human use of AI assistance | Role-specific reliance and constitutional limits |
| Sycophancy research | Agreement bias and preference-model effects | False attunement in field mapping |
| Constitutional AI | Principle-guided critique and AI feedback | Public legitimacy, provider teloi, user contestability |
| Model cards | Static intended-use and limitation documentation | Session-specific role and policy witness |
| System cards | Deployed-system safeguards and evaluation | Action-linked version and practical oversight |
| Multi-agent debate | Critique, diversity, or ensemble reasoning | Standing plurality distinction and mediator governance |
| Contestability | Challenge to automated decisions | Challenge across source, inference, route, and authority |
| Human oversight | Human review or supervision | Source-aware, authority-bearing human re-entry |
| Meaningful human control | Substantive human relation to system action | Semantic legibility of operative interpretation |

---

# 27. Terminology adjudication

## Semantic polytelometry

**Decision:** retain provisionally.

**Boundary:** governed capability class, not mind reading or one model feature.

## Semantic navigator

**Decision:** retain.

**Boundary:** model assists orientation among representations; does not own destination or field.

## Non-sovereign model

**Decision:** retain.

**Boundary:** authority remains external, scoped, and reviewable.

## Model constitution

**Decision:** retain with clarification.

**Boundary:** broad deployed rules; distinct from the specific Constitutional AI method.

## Provider teloi

**Decision:** retain.

**Boundary:** materially operative provider purposes, not speculative motive attribution.

## Semantic trajectory

**Decision:** retain as a strong candidate technical concept.

## False attunement

**Decision:** retain provisionally.

**Boundary:** perceived recognition caused by adaptive agreement without independent support.

## Participant recognition

**Decision:** retain.

## Constitutional retrieval

**Decision:** retain provisionally.

**Boundary:** retrieval priority for boundaries, corrections, authority, and standing—not a replacement for relevance retrieval.

## Human re-entry

**Decision:** retain.

**Boundary:** practical, source-aware intervention; not ceremonial approval.

## Model plurality

**Decision:** retain as distinct from standing plurality.

## Session record

**Decision:** retain as a Phase I candidate.

## Meaningful control

**Decision:** use established phrasing with citation and avoid claiming ownership of the term.

---

# 28. Claim adjudication

## May be stated strongly

- Language models can transform, compare, retrieve, and generate linguistic representations.
- Retrieval does not guarantee correct attribution or complete grounding.
- Tool-using models can convert language-model outputs into external actions.
- Planning and execution are distinct capabilities.
- Calibrated uncertainty alone may not produce appropriate reliance.
- Sycophancy is observed in several human-feedback-trained assistants and tasks.
- Model cards are uneven in completeness and detail.
- Multi-agent debate does not guarantee independent reasoning or standing plurality.
- People need practical mechanisms to challenge consequential automated decisions.
- Human oversight can be nominal rather than meaningful.

## May be stated as a proposed synthesis

- Semantic polytelometry is a useful governance architecture for model-mediated plural fields.
- Source–model–provider–institution separation improves accountability.
- Semantic-trajectory tracking can expose inference laundering and scope drift.
- Constitutional retrieval should prioritize active boundaries and corrections.
- Participant recognition should affect representation authority.
- Human re-entry is a stronger design requirement than generic human-in-the-loop language.
- Role-specific reliance is superior to global trust.
- Model-agent plurality should never substitute for represented-center plurality.
- Session-level witness should connect documentation to action.

## Must remain hypotheses

- Semantic-polytelometry architecture improves participant recognition.
- Role envelopes can reliably constrain capable agents.
- Semantic trajectories can be preserved without unacceptable privacy cost.
- Constitutional retrieval improves high-stakes outcomes.
- Non-sovereign model designs reduce dependence and authority confusion.
- Multi-agent mediation improves fairness more than single-model mediation.
- Provider teloi can be disclosed at useful operational resolution.
- Participant correction can propagate through model memory, retrieval, and downstream systems at scale.

## Should not be claimed

- Language models understand a person's true field.
- Retrieval eliminates hallucination.
- Citations guarantee support.
- Confidence creates authority.
- Constitutional AI establishes democratic legitimacy.
- Model cards establish safe use.
- Several model agents constitute plural human standing.
- Human approval automatically creates meaningful control.
- Explanation automatically creates contestability.
- A model can remain neutral merely by exposing uncertainty.
- Provider interests can be inferred reliably from model output alone.

---

# 29. Required F.10 boundaries

F.10 appropriately includes:

- architecture rather than capability claim;
- field/projection/trail/context/mirror/route separation;
- model role classification;
- capability versus authority;
- model constitution and provider teloi;
- source–model–provider–institution layers;
- epistemic status and multidimensional uncertainty;
- role-specific reliance;
- provenance and citation limits;
- constitutional retrieval;
- semantic trajectory;
- participant recognition;
- sycophancy and false attunement;
- challenge without model sovereignty;
- multi-agent mediation boundaries;
- tool and agentic planning gates;
- practical human re-entry;
- contestability and recourse;
- breach, repair, proportional governance, architecture, and session record;
- falsification and privacy boundaries.

Before Phase I implementation, the architecture requires:

1. privacy and security threat modeling;
2. role enforcement at the tool and credential layer;
3. user-recognition testing;
4. source-linked claim evaluation;
5. model and policy versioning;
6. recourse workflows;
7. human-factors review;
8. domain-specific authority rules;
9. dependency analysis for provider and model substitution;
10. red-team testing for sycophancy, manipulation, and false consensus.

---

# 30. Empirical differentiation agenda

## 30.1 RAG versus constitutional retrieval

Compare ordinary relevance retrieval with retrieval that prioritizes:

- correction;
- revocation;
- protected condition;
- current authority;
- dissent;
- stop.

Measure answer quality and action legitimacy.

## 30.2 Source–model layer study

Compare fluent merged summaries with outputs visibly separated into source, model, and provider layers.

Measure comprehension, trust calibration, and correction.

## 30.3 Semantic-trajectory study

Test whether transformation histories improve detection of:

- inference laundering;
- scope drift;
- stale memory;
- unsupported action.

## 30.4 Role-envelope study

Evaluate whether explicit, enforced role boundaries change:

- tool calls;
- escalation;
- refusal;
- participant reliance;
- authority confusion.

## 30.5 Sycophancy study

Test semantic-field tasks where user framing is plausible but unsupported.

Measure whether the system preserves the field while maintaining independent evidence status.

## 30.6 Multi-agent plurality study

Compare:

- one model;
- identical-model agents;
- diverse-model agents;
- human participant agents;
- source-grounded mediation.

Measure false consensus and independent correction.

## 30.7 Human re-entry study

Vary:

- timing;
- source access;
- decision authority;
- workload;
- reversibility.

Measure whether the human actually changes outcomes.

## 30.8 Contestability study

Measure time and success required for an affected participant to:

- identify the operative inference;
- pause action;
- provide correction;
- obtain review;
- propagate change;
- receive repair.

---

# 31. Candidate Phase I architecture implications

G.11 supports a modular implementation.

## 31.1 Source registry

Preserves direct and delegated source objects.

## 31.2 Projection service

Implements evidence, scope, consent, authority, and expiry.

## 31.3 Provenance and trajectory service

Uses W3C PROV-compatible structures plus semantic status changes.

## 31.4 Retrieval policy engine

Supports ordinary relevance plus protected constitutional priorities.

## 31.5 Role and credential engine

Binds model instances to:

- allowed tools;
- data views;
- output classes;
- confirmation gates;
- execution limits.

## 31.6 Field and navigation service

Maintains field classes, routes, cost bearers, dissent, and unresolved remainder.

## 31.7 Witness and event stream

Records model, policy, retrieval, route, action, and consequence versions.

## 31.8 Contest and recourse service

Supports challenge, pause, correction, review, propagation, and repair.

## 31.9 Lifecycle controller

Supports expiry, revocation, release, succession, and dissolution.

## 31.10 Independent human interface

Allows participants and reviewers to inspect the record without relying solely on the same model that produced it.

---

# 32. Bottom line

F.10 should proceed.

It should proceed as:

- a reference architecture;
- a governance synthesis;
- a bridge among deliberative AI, RAG, agents, provenance, human factors, and contestability;
- a non-sovereign role model for language systems;
- a source of technical records and empirical tests.

It should not proceed as:

- a claim that language models can read true purpose;
- a new universal alignment algorithm;
- a substitute for institutional authority;
- a promise that retrieval or citations eliminate hallucination;
- a multi-agent voting scheme for human values;
- a human-in-the-loop slogan;
- a justification for collecting full personal context;
- an architecture in which the provider's field remains invisible.

The strongest defensible formulation is:

> **Semantic polytelometry extends existing language-model decision and deliberation systems by separating semantic capability from action authority, preserving the source and trajectory of represented ends, and requiring that affected centers can recognize, correct, contest, and exit the model-mediated field before its interpretation becomes sovereign action.**

---

# Primary references

Bai, Yuntao, et al. “Constitutional AI: Harmlessness from AI Feedback.” arXiv:2212.08073, 2022.

Cao, Shiye, Anqi Liu, and Chien-Ming Huang. “Designing for Appropriate Reliance: The Roles of AI Uncertainty Presentation, Initial User Decision, and User Demographics in AI-Assisted Decision-Making.” arXiv:2401.05612, 2024.

Landau, Susan, et al. “Challenging the Machine: Contestability in Government AI Systems.” arXiv:2406.10430, 2024.

Lewis, Patrick, et al. “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.” *Advances in Neural Information Processing Systems* 33, 2020.

Liang, Weixin, et al. “What’s Documented in AI? Systematic Analysis of 32K AI Model Cards.” arXiv:2402.05160, 2024.

Ma, Shuai, et al. “Towards Human-AI Deliberation: Design and Evaluation of LLM-Empowered Deliberative AI for AI-Assisted Decision-Making.” arXiv:2403.16812, 2024.

Mitchell, Margaret, et al. “Model Cards for Model Reporting.” Proceedings of FAT*, 2019.

Qian, Haosheng, et al. “On the Capacity of Citation Generation by Large Language Models.” arXiv:2410.11217, 2024.

Sankararaman, Hithesh, et al. “Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output.” arXiv:2411.01022, 2024.

Schick, Timo, et al. “Toolformer: Language Models Can Teach Themselves to Use Tools.” arXiv:2302.04761, 2023.

Sharma, Mrinank, et al. “Towards Understanding Sycophancy in Language Models.” arXiv:2310.13548, 2023.

Sun, Haoyu, et al. “Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents.” arXiv:2606.04874, 2026.

Wei, Jerry, et al. “Simple Synthetic Data Reduces Sycophancy in Large Language Models.” arXiv:2308.03958, 2023.

Wu, Haolun, Zhenkun Li, and Lingyao Li. “Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning.” arXiv:2511.07784, 2025.

Yao, Shunyu, et al. “ReAct: Synergizing Reasoning and Acting in Language Models.” arXiv:2210.03629, 2022.
