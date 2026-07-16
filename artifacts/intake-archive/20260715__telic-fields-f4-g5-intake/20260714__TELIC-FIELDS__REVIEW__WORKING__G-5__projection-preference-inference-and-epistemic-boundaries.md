---
title: "Projection, Preference Inference, and Epistemic Boundaries"
subtitle: "Requirements, User Models, Inverse Inference, Construct Validity, Calibration, and Privacy"
artifact_date: "2026-07-14"
artifact_type: "adjacent-fields-and-epistemic-review"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "draft"
processing_tier: 4
source_role: "research-and-claim-boundary-artifact"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "G.5"
companion_to:
  - "20260714__TELIC-FIELDS__PAPER__CANDIDATE__F-4__telic-projection-estimation.md"
research_note: >
  This review compares telic projection estimation with established practices
  for eliciting, inferring, modeling, measuring, and predicting human goals and
  preferences. It is not a systematic review. Negative search findings do not
  establish novelty.
---

# Projection, Preference Inference, and Epistemic Boundaries

## Executive finding

Telic projection estimation occupies a crowded technical and epistemic territory.

Requirements engineering already distinguishes elicitation from mere collection and recognizes ambiguity, incompleteness, conflict, volatility, stakeholder bias, and changing requirements. Goal-oriented methods represent actors, goals, dependencies, obstacles, and refinements.

User modeling and intent-recognition systems infer short-term or latent intent from language and behavior. Recommender systems often maintain evolving profiles. Preference learning, inverse decision theory, inverse reinforcement learning, and direct-preference methods infer objective structure from observed choices or comparisons. Theory-of-mind research evaluates whether models can reason about beliefs and intentions. Psychometrics and measurement theory warn that latent constructs are not directly observed and that validity concerns the interpretation and use of measurements. Calibration research shows that model confidence does not automatically track correctness, especially under distribution shift. Privacy law and data-minimization principles limit the legitimacy of collecting or processing every potentially useful signal.

The Telic Field Papers should not claim to invent scoped elicitation, latent-preference inference, user modeling, uncertainty, or provenance.

Their candidate contribution is the constitutional composition:

> **A projection is a source-attributed and scope-bounded representation whose epistemic adequacy, action authority, consent, privacy, expiration, and correction status remain separate.**

Existing methods often optimize one or more of:

- predictive accuracy;
- requirements completeness;
- preference identification;
- personalization;
- task efficiency;
- calibration.

Telic projection estimation adds the requirement that an accurate inference can remain unauthorized, over-scoped, stale, privacy-invasive, or constitutionally inadequate.

> **Accuracy answers whether the estimate predicts. Legitimacy answers whether the estimate may govern.**

---

# 1. Review frame

The review evaluates neighboring approaches across ten questions.

## 1.1 What is being estimated?

- requirement;
- goal;
- preference;
- reward;
- belief;
- intention;
- need;
- boundary;
- protected condition;
- future action.

## 1.2 Who is the source?

Is the estimate tied to:

- direct statement;
- observed behavior;
- authorized delegate;
- model inference;
- population pattern;
- institutional artifact?

## 1.3 What is the scope?

For which recipient, purpose, action, duration, and downstream use is the representation adequate?

## 1.4 What remains uncertain?

Does the method distinguish source, expression, interpretation, context, temporal, authority, ontological, and model uncertainty?

## 1.5 What establishes validity?

What evidence supports the claim that the representation means what the system says it means?

## 1.6 How is confidence calibrated?

Does reported confidence match actual performance under relevant conditions and distribution shifts?

## 1.7 Who may act?

Does the method separate predictive confidence from authority and consent?

## 1.8 How does correction work?

Can the source correct, revoke, expire, or contest the representation?

## 1.9 What privacy limits apply?

Does the method collect or infer only what is necessary for the authorized purpose?

## 1.10 What happens to derived records?

Do correction and revocation propagate through dependent systems?

---

# 2. Requirements elicitation

Requirements elicitation is not simply asking a user what they want and writing down the answer.

The field recognizes recurring problems of:

- scope;
- understanding;
- ambiguity;
- conflict;
- volatility;
- stakeholder diversity;
- organizational bias;
- tacit knowledge;
- domain constraints;
- rationale;
- changing context.

Goal-directed requirements acquisition and goal-oriented requirements engineering extend the process by representing why a system is needed, who depends on whom, what obstacles exist, and how goals refine into system requirements.

## Strong overlap

- incomplete expression;
- multi-round clarification;
- source and stakeholder identification;
- changing requirements;
- ambiguous language;
- dependencies;
- explicit rationale;
- traceability;
- alternative operationalizations.

## What telic projection estimation may add

Requirements methods often treat the elicited requirement as the relevant object once sufficiently validated.

The telic framework keeps several distinctions active:

- field versus requirement;
- requirement versus receiver interpretation;
- stated goal versus protected condition;
- goal versus boundary;
- source authority versus analyst inference;
- project scope versus outer-loop reuse;
- current requirement versus future standing;
- compliance with requirement versus betrayal of underlying field.

## Adjudication

**Telic projection estimation should be presented as an extension of elicitation, not a replacement.**

It is strongest where:

- several centers possess different standing;
- an inferred requirement may be over-authoritative;
- the action is high stakes;
- requirements will be reused by downstream systems;
- correction and revocation must propagate;
- privacy limits what should be elicited.

## Implementation bridge

A requirements artifact can be extended with:

```text
source_center
affected_centers
evidence_class
statement_or_inference
scope
authority
protected_conditions
unacceptable_sacrifices
uncertainty
expiration
correction_route
```

---

# 3. Intent recognition and user modeling

Intent-recognition systems infer what a user is trying to accomplish from utterances, click paths, context, history, and domain models. User-modeling systems maintain representations of interests, capabilities, preferences, and behavior to personalize interaction.

These methods are operationally close to projection estimation.

## Strong overlap

- incomplete and ambiguous expression;
- latent intent;
- multi-turn clarification;
- context dependence;
- temporal change;
- probabilistic inference;
- use of historical behavior;
- personalization;
- uncertainty.

## Core difference

An intent model usually exists to improve service performance.

A telic projection record exists to govern how an interpretation may be used.

The difference is visible in a recommender system.

A system may infer that a user is interested in a product category. That inference may improve click prediction. It does not establish:

- that the interest is enduring;
- that the user wants the profile retained;
- that the inference may be sold;
- that the category reflects a chosen identity;
- that the recommendation serves the user's long-term field;
- that adjacent sensitive traits may be inferred.

## Adjudication

**User intent should be treated as a scoped hypothesis, not an identity property.**

Short-term intent, long-term preference, and protected value must remain separate.

## Required design

Intent records should include:

- trigger;
- context;
- time;
- evidence;
- competing hypotheses;
- uncertainty;
- source confirmation;
- use scope;
- expiration;
- prohibited extrapolations.

---

# 4. Preference learning

Preference learning infers an ordering or policy from choices, ratings, comparisons, demonstrations, or feedback.

It is powerful precisely because people often cannot specify a complete objective function.

## Strong overlap

- indirect evidence;
- uncertainty;
- suboptimal decision-makers;
- pairwise comparison;
- context-dependent choice;
- learning from behavior;
- latent objective structure.

## Fundamental epistemic limit

Observed choice does not uniquely identify preference.

Choice may be shaped by:

- constrained options;
- imperfect information;
- coercion;
- habit;
- scarcity;
- risk;
- social expectation;
- temporal discounting;
- fatigue;
- inability to express a preferred alternative;
- strategic behavior.

Inverse decision theory shows that preference identification depends on assumptions about the decision environment, observability, uncertainty, and the decision-maker's behavior. Some uncertain decision settings can make tradeoffs more identifiable, but this remains identification under a model.

The learned object is not the person.

## Adjudication

**Preference estimates must remain model-relative and context-relative.**

Use:

> Under the assumed choice model and observed decisions, this tradeoff is estimated.

Avoid:

> The system discovered the user's true preference.

## Constitutional distinction

A preference-learning model may estimate:

\[
\theta_A
\]

where \(\theta_A\) parameterizes behavior.

A telic projection record must additionally preserve:

- who supplied the evidence;
- whether the source confirms the interpretation;
- whether use is authorized;
- which standing is absent;
- whether the estimate may govern action;
- when it expires.

---

# 5. Inverse reinforcement learning

Inverse reinforcement learning infers a reward function from observed behavior, assuming behavior was generated in relation to goals, rewards, or policies.

IRL is a strong neighbor for operative telos because it asks what objective would make observed behavior intelligible.

## Strong overlap

- inferred objective;
- behavior as evidence;
- action under uncertainty;
- personalized reward structure;
- distinction between observed policy and latent reward;
- suboptimal behavior.

## Core risks

The inverse problem is underdetermined.

Multiple reward functions can explain the same behavior.

Modelers must choose:

- state representation;
- features;
- rationality assumptions;
- environmental dynamics;
- observability;
- priors;
- regularization.

These choices contribute to the inferred objective.

## Adjudication

**IRL can estimate an operative behavioral model, not source-authorized purpose.**

An inferred reward may reveal:

- what behavior appears to restore;
- which features predict choice;
- what policy the observer expects.

It does not by itself establish:

- conscious intention;
- moral value;
- consent;
- legitimate authority;
- stable identity;
- complete field structure.

## Telic bridge

IRL outputs may enter projection estimation only as:

```text
evidence_class: model_inference
model_assumptions:
alternative_explanations:
source_review_status:
action_authority: none_unless_separately_granted
```

---

# 6. Direct preference optimization and aggregate feedback

Direct Preference Optimization and related methods steer model behavior from preferred and dispreferred outputs.

These approaches are efficient because they transform comparative judgments into policy updates without requiring a separately deployed reward model.

## Structural issue

The training process can erase:

- which person supplied which judgment;
- why the judgment was made;
- whether the preference was weak or protected;
- whether raters disagreed;
- cultural and contextual variation;
- changes over time;
- withdrawal;
- use consent;
- provider incentives.

The resulting model behaves as though a compressed aggregate preference relation were a stable operative objective.

## Adjudication

**Preference aggregation is a telic transformation and should be witnessed as such.**

A consentfully trained or aligned model should disclose:

- source populations;
- sampling;
- task context;
- disagreement;
- aggregation rules;
- constitutional principles;
- provider constraints;
- intended scope;
- withdrawal limitations;
- known cultural or domain gaps.

Telic projection estimation should be used before training and during use, not merely as another preference dataset.

---

# 7. Theory of mind

Theory of mind concerns reasoning about beliefs, intentions, desires, and knowledge states of others.

Recent evaluations show that some instruction-tuned language models perform strongly on several theory-of-mind-style tasks, while results vary by task design, model, prompting, robustness, and what counts as genuine social understanding.

## Relevance

A system capable of modeling another's belief or intention may produce better receiver mirrors.

It may also become more persuasive and manipulative.

Task performance does not establish:

- lived understanding;
- concern;
- consent;
- accurate person-specific inference;
- authority to act;
- robust performance outside benchmarks.

## Adjudication

**Theory-of-mind capability should be treated as interpretive power, not relational legitimacy.**

The stronger the inference capability, the stronger the requirements for:

- scope;
- uncertainty;
- contestability;
- privacy;
- non-manipulation;
- source correction;
- role limits.

A system should never use apparent ToM competence to claim privileged access to a user's hidden state.

---

# 8. Construct validity

A telic field, preference, intention, trust, dignity, safety, and internal standing are latent constructs.

They are not directly visible.

Construct validity concerns whether evidence supports the interpretation and use made from an observation or measure. Modern validity theory emphasizes that validity is not a permanent property of an instrument in isolation. It concerns the inferences and actions supported in a context.

This is highly compatible with projection integrity.

## Key implication

A projection can be reliable without being valid.

A system may consistently produce the same label while measuring the wrong construct.

Examples:

- engagement interpreted as satisfaction;
- retention interpreted as loyalty;
- compliance interpreted as consent;
- silence interpreted as agreement;
- continued employment interpreted as preference;
- physiological arousal interpreted as fear;
- purchase interpreted as endorsement;
- model confidence interpreted as certainty.

## Adjudication

**Telic projection validity must be claim-specific and action-specific.**

The question is:

> What evidence supports using this representation for this action in this context?

Not:

> Is this user model valid?

## Nomological discipline

Candidate constructs should be related to observable consequences and neighboring constructs.

For example, a projection of “protected privacy boundary” should predict:

- refusal of secondary use;
- correction when sharing expands;
- distress or withdrawal after breach;
- willingness under narrower scope.

If it does not, the construct or its interpretation requires revision.



# 9. Reliability, error, and construct drift

Projection systems can fail even when their average performance appears strong.

## 9.1 Measurement error

Observed statements and behaviors are noisy indicators.

Noise may come from:

- misunderstanding;
- interface constraints;
- language mismatch;
- social desirability;
- transient state;
- coercion;
- random variation;
- sensor error;
- missing context.

## 9.2 Model error

The system may map evidence to the wrong projection.

## 9.3 Construct drift

The meaning of the label changes over time.

A “high-value customer” label may begin as purchase history and later govern service priority, fraud suspicion, credit, or identity.

## 9.4 Scope drift

A model built for recommendation is used for eligibility or governance.

## 9.5 Population drift

A model is applied to centers unlike those represented in development.

## 9.6 Temporal drift

The source changes while the profile persists.

## Adjudication

**Projection integrity requires lifecycle validation, not one-time accuracy.**

The system should monitor:

- current scope;
- population;
- temporal relevance;
- source correction;
- downstream reuse;
- error distribution;
- affected standing.

---

# 10. Calibration

A model is calibrated when its reported confidence corresponds appropriately to observed accuracy under defined conditions.

Modern neural networks can be overconfident. Post-hoc calibration methods improve confidence estimates under some conditions, but calibration can degrade under distribution shift. Calibration measures also depend on binning, sample size, task, and evaluation design.

## Relevance

Calibration is necessary when a system exposes confidence in a telic inference.

It is not sufficient.

A projection may be:

- well calibrated but unauthorized;
- well calibrated but privacy-invasive;
- well calibrated at population level but wrong for the source;
- well calibrated for prediction but invalid for governance;
- well calibrated before context shift and poor afterward.

## Adjudication

**Calibration should govern how strongly an inference is held, not whether it may rule.**

A telic system should disclose:

```text
confidence_target:
calibration_population:
evaluation_period:
distribution_shift_status:
known_failure_modes:
```

## Semantic confidence

Language models often produce fluent statements that imply more certainty than their evidence supports.

Projection systems should prefer structured uncertainty over rhetorical hedging.

Use:

```yaml
inference:
  claim: "The user may prioritize continuity over speed."
  confidence: moderate
  evidence:
    - source statement 4
    - behavior event 9
  alternatives:
    - financial constraint
    - fear of change
  source_confirmed: false
```

---

# 11. Distribution shift

A projection estimated in one context may fail in another.

Examples:

- workplace behavior used to infer intimate preference;
- crisis decisions used to predict ordinary life;
- purchases used to infer political identity;
- past medical choices used after diagnosis changes;
- one culture's conversational norms applied to another;
- model behavior calibrated on benchmark tasks used in live relationships.

The field may be stable while the projection is scope-bound.

The projection may be stable while the field changes.

## Adjudication

**Cross-context transfer requires explicit justification.**

Default rule:

> A projection does not travel merely because it can be copied.

A system should ask:

- Is the construct equivalent?
- Is the source still represented?
- Are the consequences comparable?
- Is authority valid?
- Was cross-context use consented?
- What new centers are affected?

---

# 12. Privacy and data minimization

Privacy principles, including purpose limitation and data minimization, constrain the collection and processing of personal information.

This is not merely a legal compliance issue.

Projection estimation can create sensitive information that the source never directly disclosed.

Examples include inferred:

- health status;
- sexual orientation;
- political belief;
- relationship instability;
- vulnerability;
- financial stress;
- psychological state;
- future behavior.

An inference can be privacy-invasive even when generated from lawfully collected data.

## Adjudication

**Inferential privacy belongs inside projection integrity.**

Minimum rules:

1. collect only what is necessary;
2. infer only what is necessary;
3. use only for the authorized purpose;
4. restrict retention;
5. prevent hidden downstream reuse;
6. disclose consequential inference;
7. provide correction and contestability;
8. separate service delivery from model training consent.

## Important distinction

A user's willingness to provide context does not authorize every inference that context makes possible.

> **Information availability is not interpretive permission.**

---

# 13. Clinical formulation as a boundary case

Clinical formulation organizes information about a person's difficulties, vulnerabilities, triggers, maintaining factors, and strengths to guide care.

It is a useful comparison because it makes inferences about what matters and what sustains behavior.

## Strong overlap

- multiple evidence sources;
- uncertainty;
- historical context;
- current consequence;
- hypotheses rather than simple labels;
- revision over time;
- action guidance.

## Critical boundary

Clinical formulation occurs within professional, ethical, and legal frameworks and still carries risks of overinterpretation, power asymmetry, and diagnostic capture.

A general telic system must not imitate clinical authority.

## Adjudication

Projection estimation may borrow:

- hypothesis discipline;
- revision;
- explicit uncertainty;
- context sensitivity.

It must not borrow:

- diagnostic authority;
- hidden case formulation presented as fact;
- treatment power;
- coercive access to sensitive history.

---

# 14. Source correction and contestability

Many modeling systems allow users to change settings.

Fewer allow them to contest the interpretation itself.

A source should be able to say:

- I did not state that;
- that inference is wrong;
- that was true only in one context;
- this label is outdated;
- the model omitted a protected condition;
- I do not authorize this use;
- I cannot fully explain why, but the action should pause.

Correction must not require technical expertise.

The system should show:

```text
what was observed
what was inferred
what action depends on it
who receives it
how long it persists
how to correct or revoke it
```

## Adjudication

**Contestability is part of validity.**

A representation that cannot be corrected by the represented center should be treated as lower authority, especially in high-stakes action.

---

# 15. Revocation and machine learning

Revocation is difficult once data has shaped a trained model.

Deleting a source record may not remove its statistical influence.

This creates a boundary between:

- record revocation;
- inference revocation;
- training-data withdrawal;
- model unlearning;
- downstream decision review.

A system should not imply complete revocation if only the visible profile was deleted.

## Adjudication

Consent records must state what can and cannot be reversed.

For training use, disclose:

- whether data enters training;
- whether withdrawal is possible;
- whether derived checkpoints persist;
- whether outputs may still reflect aggregate influence;
- what future use stops after revocation.

Telic integrity requires truthful limits, not ceremonial control.

---

# 16. Epistemic-status register

A projection architecture should assign statuses that are intelligible to humans and machines.

Suggested statuses:

```text
DIRECT
CONFIRMED
DELEGATED
OBSERVED
INFERRED
CONTESTED
UNKNOWN
STALE
EXPIRED
REVOKED
OUT_OF_SCOPE
```

These are not confidence levels.

A direct statement can be uncertain.

An inference can be highly predictive.

A revoked statement may remain historically important.

The status indicates relation to source and authority.

## Recommended ordering

Do not convert statuses into one universal rank.

Different actions require different evidence.

An immediate protective pause may rely on observation.

A permanent eligibility denial should require stronger authority and review.

---

# 17. Comparison matrix

| Method | Primary object | Strength | Core epistemic risk | Telic extension |
|---|---|---|---|---|
| Requirements elicitation | Requirements and rationale | Clarification and stakeholder discovery | Treating elicited artifact as complete field | Add standing, scope, authority, expiration |
| GORE / i* | Goals, actors, dependencies | Why and strategic relations | Goal availability assumed | Add evidence class and source correction |
| Intent recognition | Current user intent | Fast service adaptation | Overconvergence and identity extrapolation | Treat as expiring scoped hypothesis |
| User modeling | Persistent user characteristics | Personalization | Stale profiles and hidden inference | Add review, contestability, minimum use |
| Preference learning | Choice ordering | Learning without full specification | Constrained choice mistaken for value | Preserve context, alternatives, consent |
| IRL | Latent reward | Behavioral explanation | Underdetermination and model assumptions | Mark as model-relative evidence |
| DPO / aggregate feedback | Preferred outputs | Efficient model steering | Source and disagreement erasure | Witness aggregation and use consent |
| Theory of mind | Beliefs and intentions | Social prediction | Competence mistaken for understanding or authority | Treat as interpretive power |
| Psychometrics | Latent constructs | Validity and measurement discipline | Reification of scores | Validate action-specific interpretation |
| Calibration | Confidence quality | Better uncertainty signaling | Confidence mistaken for legitimacy | Separate confidence from authority |
| Clinical formulation | Explanatory care hypothesis | Contextual and revisable understanding | Power and overinterpretation | Borrow hypothesis discipline only |
| Privacy minimization | Necessary data processing | Risk reduction and purpose limits | Narrow compliance without inferential control | Include inferred data and downstream use |

---

# 18. G.5 terminology adjudication

## Telic projection estimation

**Decision:** retain.

**Boundary:** scoped construction of a usable representation, not discovery of a true field.

## Telic projection

**Decision:** retain.

**Boundary:** source-attributed and corrigible representation.

## Receiver mirror

**Decision:** retain.

**Boundary:** receiver interpretation, not merely another copy of the projection.

## Projection integrity

**Decision:** retain.

**Boundary:** includes epistemic, semantic, authority, temporal, privacy, and correction dimensions.

## Source authority

**Decision:** retain.

**Boundary:** privileged self-description, not absolute infallibility.

## Interpretive authority

**Decision:** retain.

**Boundary:** ability to propose meaning, not permission to act.

## Action authority

**Decision:** retain.

**Boundary:** separately grounded in consent, delegation, role, or law.

## Inferential privacy

**Decision:** adopt.

**Boundary:** protection against unauthorized sensitive inference, not only unauthorized collection.

## Evidence class

**Decision:** adopt as a core record field.

## Uncertainty profile

**Decision:** adopt.

**Boundary:** multidimensional; not one confidence score.

## Projection expiration

**Decision:** retain as a default lifecycle concept.

## Projection revocation

**Decision:** retain.

**Boundary:** must disclose technical limits on downstream and trained-model reversal.

---

# 19. Claim adjudication

## May be stated strongly

- Human goals and preferences are not directly observable.
- Requirements and preferences can be ambiguous, incomplete, conflicted, and volatile.
- Behavior underdetermines latent purpose.
- User models are context and assumption dependent.
- Calibration does not establish authority or consent.
- Construct validity concerns the interpretation and use of measurements.
- Sensitive information can be inferred rather than directly collected.
- Source correction is necessary for consequential interpretation.
- Trained-model influence may not be fully reversible through record deletion.

## May be stated as a proposed synthesis

- Projection integrity usefully unifies epistemic and constitutional adequacy.
- Evidence classes improve telic records.
- Expiration should be the default for many user and intent models.
- Receiver mirrors deserve explicit representation.
- Inferential privacy is a core telic-system requirement.
- Telic projection records can improve requirements and preference systems.

## Must remain hypotheses

- Projection records reduce harmful preference misidentification.
- Mirror return improves consequential coordination enough to justify its burden.
- Multidimensional uncertainty profiles outperform simpler confidence measures.
- Telic projection estimation scales to large populations.
- Revocation propagation can be operationally effective across model ecosystems.

## Should not be claimed

- A projection reveals the true field.
- Direct statements are always complete or accurate.
- Behavior reveals authentic preference.
- A calibrated model is entitled to act.
- High theory-of-mind benchmark performance establishes human-like understanding.
- Data consent authorizes all derived inference.
- Deleting a profile fully removes training influence.

---

# 20. Required F.4 boundaries

F.4 appropriately includes:

- the historical terminology change from calculation to estimation;
- field/projection/mirror separation;
- evidence classes;
- source, interpretive, and action authority;
- multidimensional uncertainty;
- confidence versus authority;
- expiration;
- data minimization;
- low-verbal estimation;
- correction and revocation;
- a breach taxonomy;
- receiver responsibility;
- model-role limits;
- a minimal research schema;
- falsification conditions.

Before Phase I implementation, the schema should undergo:

- privacy review;
- legal review;
- usability testing;
- burden reduction;
- threat modeling;
- model-unlearning and revocation analysis.

---

# 21. Empirical agenda

## 21.1 Construct-validity program

For each projected construct:

1. define the claim;
2. define observable evidence;
3. identify neighboring constructs;
4. test expected relations;
5. test alternative explanations;
6. evaluate consequences of use;
7. revise continuously.

## 21.2 Calibration and authority study

Present users with calibrated and uncalibrated predictions.

Test whether explicit authority labels reduce inappropriate reliance beyond confidence labels alone.

## 21.3 Source-correction study

Measure how source correction changes:

- accuracy;
- trust;
- action;
- downstream propagation;
- perceived agency.

## 21.4 Inferential-privacy study

Compare:

- direct collection only;
- unrestricted inference;
- minimum-necessary inference;
- user-approved inference.

Measure performance, surprise, trust, and perceived violation.

## 21.5 Expiration study

Test different expiration and review schedules for user models.

Measure stale-profile harm and consent fatigue.

## 21.6 Requirements integration

Add projection fields to a GORE or i* workflow.

Measure stakeholder coverage, conflict discovery, and requirement volatility.

---

# 22. Bottom line

Telic projection estimation should proceed.

It should proceed as:

- a disciplined extension of requirements and user modeling;
- a source-aware interpretation layer;
- a governance boundary around preference inference;
- a validity and lifecycle framework;
- a privacy-minimizing method;
- a precursor to Phase I records and protocols.

It should not proceed as:

- mind reading;
- preference discovery without assumptions;
- permanent user profiling;
- authority derived from prediction;
- a justification for collecting complete context;
- a promise of full revocation where trained influence persists.

The strongest defensible formulation is:

> **Telic projection estimation does not solve the inverse problem of another center. It makes the assumptions, scope, authority, uncertainty, and correction of that inverse problem legible enough to govern action.**

---

# Primary references

Borsboom, Denny, Gideon J. Mellenbergh, and Jaap van Heerden. “The Concept of Validity.” *Psychological Review* 111, no. 4, 2004.

Christel, Michael G., and Kyo C. Kang. *Issues in Requirements Elicitation*. CMU/SEI-92-TR-012, 1992.

Cronbach, Lee J., and Paul E. Meehl. “Construct Validity in Psychological Tests.” *Psychological Bulletin* 52, no. 4, 1955.

Guo, Chuan, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. “On Calibration of Modern Neural Networks.” Proceedings of ICML, 2017.

Kumar, Ananya, Percy Liang, and Tengyu Ma. “Verified Uncertainty Calibration.” arXiv:1909.10155, 2019.

Laidlaw, Cassidy, and Stuart Russell. “Uncertain Decisions Facilitate Better Preference Learning.” arXiv:2106.10394, 2021.

Liu, Quanying, Haiyan Wu, and Anqi Liu. “Modeling and Interpreting Real-world Human Risk Decision Making with Inverse Reinforcement Learning.” arXiv:1906.05803, 2019.

Messick, Samuel. “Validity of Psychological Assessment.” *American Psychologist* 50, no. 9, 1995.

Rafailov, Rafael, et al. “Direct Preference Optimization: Your Language Model Is Secretly a Reward Model.” arXiv:2305.18290, 2023.

Tian, Junrui, et al. “User Intention Recognition and Requirement Elicitation Method for Conversational AI Services.” arXiv:2009.01509, 2020.

van Duijn, Max J., et al. “Theory of Mind in Large Language Models.” arXiv:2310.20320, 2023.

van Lamsweerde, Axel. “Goal-Oriented Requirements Engineering: A Guided Tour.” Proceedings of the Fifth IEEE International Symposium on Requirements Engineering, 2001.

Yu, Eric S. K. “Towards Modelling and Reasoning Support for Early-Phase Requirements Engineering.” Proceedings of the Third IEEE International Symposium on Requirements Engineering, 1997.

European Union. *General Data Protection Regulation*, Article 5.
