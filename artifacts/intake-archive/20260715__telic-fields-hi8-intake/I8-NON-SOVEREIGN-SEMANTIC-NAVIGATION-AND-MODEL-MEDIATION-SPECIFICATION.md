---
title: "I.8 — Non-Sovereign Semantic Navigation and Model Mediation Specification"
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
  - "I.7 — Polytelometric Deliberation, Portfolio, and Public Decision Specification"
  - "F.10 — Semantic Polytelometry with Language Models"
  - "G.11 — Language Models as Non-Sovereign Semantic Navigators"
---

# I.8 — Non-Sovereign Semantic Navigation and Model Mediation Specification

## 1. Purpose

I.8 defines how language models and related semantic systems may assist field mapping, summarization, translation, comparison, route generation, challenge, mediation, and tool use without acquiring standing, ownership, consent, or sovereign authority over the fields they help represent.

Its governing rule is:

> **The model may map the field. It may not own the field.**

A language model may be unusually capable of:

- extracting distinctions;
- translating between vocabularies;
- comparing partially expressed positions;
- generating candidate routes;
- identifying contradictions;
- summarizing deliberation;
- retrieving related traces;
- proposing clarification;
- mediating turn structure;
- preparing action candidates.

These capabilities do not determine:

- which centers have standing;
- what participants consented to;
- which summary is authoritative;
- which protected conditions govern;
- which option set is legitimate;
- which route should be executed;
- which consequence is acceptable;
- whether the model's provider field should remain hidden.

I.8 therefore separates:

```text
CAPABILITY
≠ ROLE
≠ PERMISSION
≠ AUTHORITY
≠ LEGITIMACY
```

It defines:

- model-role and authority ledgers;
- semantic-operator output classes;
- model field maps;
- standing-preserving summaries;
- option and agenda generation witnesses;
- minority-field retention profiles;
- sycophancy and synthetic-consensus events;
- provider-telos disclosures;
- model-disagreement records;
- tool and action boundaries;
- correction, refusal, and abstention records;
- model-mediated decision witnesses.

---

# 2. Normative scope

I.8 defines:

- `ModelRoleAuthorityLedger`;
- `SemanticOperatorOutput`;
- `ModelFieldMap`;
- `StandingPreservingSummary`;
- `OptionAgendaGenerationWitness`;
- `MinorityFieldRetentionProfile`;
- `SycophancySyntheticConsensusEvent`;
- `ProviderTelosDisclosure`;
- `ModelDisagreementRecord`;
- `ModelToolActionBoundary`;
- `ModelCorrectionRefusalRecord`;
- `ModelMediatedDecisionWitness`.

I.8 does not define:

- a claim that language models understand a field completely;
- a claim that model outputs possess standing;
- a claim that model plurality creates public plurality;
- a universal model constitution;
- one correct provider business model;
- one safe autonomy threshold;
- one universal calibration method;
- automatic neutrality through disclosure;
- automatic legitimacy through human approval;
- automatic consent through model inference.

---

# 3. Model-role and authority ledger

A `ModelRoleAuthorityLedger` records which role a model occupies, which operations it may perform, which authority remains external, and which boundaries prohibit role escalation.

Candidate roles:

```text
EXTRACTOR
STRUCTURER
TRANSLATOR
COMPARATOR
RETRIEVER
ROUTE_GENERATOR
CHALLENGER
MEDIATOR
WITNESS_ASSISTANT
EXECUTOR
OTHER
```

Required fields:

```yaml
ledger_id:
model_instance:
provider:
session_or_loop:
assigned_roles:
allowed_operations:
prohibited_operations:
input_authority:
output_authority:
tool_authority:
standing:
consent_authority:
decision_authority:
adjudication_authority:
role_escalation:
review:
status:
```

## 3.1 Rules

- A model role MUST be explicitly assigned.
- The model MUST NOT choose or expand its own role.
- Capability MUST NOT be treated as permission.
- Output authority MUST remain scoped by output class.
- A model MUST NOT possess participant standing merely because it can summarize participants.
- Consent authority MUST default to `NONE`.
- Decision and adjudication authority MUST default to external unless separately and explicitly governed.
- Executor role MUST require a distinct tool and action grant.
- Role escalation MUST be witnessed.

## 3.2 Governing distinction

> **The model may perform an operation without becoming the authority whose field gives the operation legitimacy.**

---

# 4. Semantic-operator output classes

A `SemanticOperatorOutput` preserves what kind of semantic object a model produced.

Candidate output classes:

```text
EXTRACTION
STRUCTURE
TRANSLATION
COMPARISON
RETRIEVAL_RESULT
SUMMARY
INFERENCE
GENERATED_OPTION
GENERATED_ARGUMENT
CHALLENGE
CLARIFICATION_QUESTION
ROUTE_RECOMMENDATION
TOOL_PLAN
TOOL_RESULT
WITNESS_DRAFT
OTHER
```

Required fields:

```yaml
output_id:
model_instance:
role:
output_class:
content:
source_inputs:
source_status:
transformations:
uncertainty:
standing_effect:
authority_effect:
consent_effect:
correction_route:
status:
```

## 4.1 Rules

- Every material model output MUST retain an output class.
- Summary MUST remain distinct from source statement.
- Inference MUST remain distinct from observation.
- Generated option MUST remain distinct from participant proposal.
- Route recommendation MUST remain distinct from authorization.
- Tool result MUST remain distinct from the model's interpretation of that result.
- Standing effect, authority effect, and consent effect MUST default to `NONE`.
- Repeated use MUST NOT relabel an output into a higher-authority class.

Candidate epistemic statuses:

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

---

# 5. Model field map

A `ModelFieldMap` is a model-produced representation of centers, projections, protected conditions, uncertainties, dependencies, options, and unresolved relations.

Required fields:

```yaml
field_map_id:
source_field:
model_instance:
scope:
represented_centers:
missing_centers:
projections:
protected_conditions:
dependencies:
uncertainties:
options:
conflicts:
minority_fields:
provider_constraints:
corrections:
completeness:
status:
```

Candidate statuses:

```text
DRAFT
PARTICIPANT_REVIEW
CORRECTED
CONTESTED
ACTIVE_FOR_SCOPE
SUPERSEDED
RELEASED
UNKNOWN
```

## 5.1 Rules

- The field map MUST identify its source field and scope.
- The field map MUST NOT claim to be the living field.
- Missing centers and missing context MUST remain visible.
- Participant projections MUST retain source and epistemic status.
- Minority fields MUST not be removed merely because they are low frequency.
- Provider constraints MUST be visible where materially operative.
- Model-generated options MUST remain labeled.
- Corrections MUST update the active map without erasing prior versions.
- Completeness MUST be scoped and contestable.

## 5.2 Governing distinction

```text
living field
≠ participant projection
≠ semantic trail
≠ retrieved context
≠ model field map
≠ candidate route
≠ authorized action
```

---

# 6. Standing-preserving summary

A `StandingPreservingSummary` compresses deliberation while preserving sources, minority positions, corrections, protected conditions, and unresolved disagreement.

Required fields:

```yaml
summary_id:
source_field:
model_instance:
summary_scope:
included_centers:
omitted_centers:
majority_or_common_positions:
minority_positions:
protected_conditions:
unresolved_disagreements:
source_links:
model_inferences:
generated_language:
participant_review:
corrections:
status:
```

## 6.1 Rules

- A summary MUST distinguish common position from universal agreement.
- Minority positions MUST remain represented when material.
- Low frequency MUST NOT imply low standing.
- Model inference MUST not be written as participant position.
- Generated connective language SHOULD remain identifiable where it affects meaning.
- Participant review MUST be available before consequential use.
- A correction MUST alter the active summary.
- The summary MUST preserve unresolved disagreement rather than smoothing it into synthetic consensus.
- A summary MUST NOT acquire standing from the centers it describes.

## 6.2 Governing distinction

> **A fluent summary can be a field collapse with good grammar.**

---

# 7. Option and agenda generation

An `OptionAgendaGenerationWitness` records how models or other actors generate, combine, prioritize, or omit options and questions.

Required fields:

```yaml
generation_id:
source_field:
model_instance:
requested_operation:
input_options:
generated_options:
combined_options:
omitted_options:
agenda_questions:
source_of_each_item:
selection_rules:
participant_review:
admission_status:
corrections:
status:
```

## 7.1 Rules

- Model-generated options MUST be labeled as generated.
- Generated options MUST NOT be attributed to participants without explicit adoption.
- The model MUST preserve the input option set.
- Omitted options MUST remain visible where omission is material.
- Agenda questions MUST remain attributable.
- Option generation MUST not silently narrow the field.
- Participant adoption MAY change the option's governance status, but MUST preserve generation lineage.
- Ranking an option MUST not authorize execution.

---

# 8. Minority-field retention

A `MinorityFieldRetentionProfile` governs preservation of low-frequency or low-power field elements.

Required fields:

```yaml
profile_id:
field_map:
center_or_group:
standing_basis:
field_elements:
frequency:
materiality:
protected_condition_relation:
retention_rule:
compression_rule:
publication:
review:
status:
```

Candidate statuses:

```text
ACTIVE
ACTIVE_WITH_CONDITIONS
CONTESTED
SUPERSEDED
RELEASED
ARCHIVAL
UNKNOWN
```

## 8.1 Rules

- Frequency MUST remain distinct from materiality.
- A minority field MAY require protected retention even when rarely expressed.
- Compression MUST preserve reason, consequence, and review trigger where material.
- Privacy and retaliation risk MUST constrain publication.
- A model MUST NOT delete low-frequency positions merely to optimize summary coherence.
- Retention MUST NOT create automatic veto.
- Minority-field review SHOULD include the represented center where possible.

---

# 9. Sycophancy and synthetic consensus

A `SycophancySyntheticConsensusEvent` records when a model changes, amplifies, or smooths its output to align with a user, authority, majority, or prior framing rather than preserving the field.

Candidate event types:

```text
USER_AGREEMENT_BIAS
AUTHORITY_AGREEMENT_BIAS
MAJORITY_SMOOTHING
CONFLICT_ERASURE
PREFERENCE_MIRRORING
FALSE_ATTUNEMENT
SYNTHETIC_CONSENSUS
OTHER
```

Required fields:

```yaml
event_id:
model_instance:
field_map:
event_type:
trigger:
affected_outputs:
affected_centers:
evidence:
immediate_response:
repair:
residual_risk:
status:
```

## 9.1 Rules

- Agreement with the user MUST NOT be treated as field accuracy.
- Model warmth or attunement MUST NOT substitute for source fidelity.
- Apparent consensus created by summary smoothing MUST be corrected.
- Sycophantic output SHOULD be quarantined from consequential use.
- Repair MUST compare the output against source trails and minority fields.
- The system SHOULD preserve whether the model changed position after social pressure.
- A refusal to flatter MUST not be confused with adversarial hostility.

## 9.2 Governing distinction

> **Agreement can increase comfort while decreasing field fidelity.**

---

# 10. Provider teloi

A `ProviderTelosDisclosure` records provider purposes, constraints, policies, incentives, and system-level objectives that materially shape model behavior.

Required fields:

```yaml
disclosure_id:
provider:
model_or_service:
declared_purposes:
operational_constraints:
safety_policies:
business_incentives:
data_incentives:
latency_or_cost_constraints:
jurisdictional_constraints:
unknown_or_undisclosed:
effect_on_model_role:
effect_on_field_map:
review:
status:
```

## 10.1 Rules

- Provider teloi MUST be represented when materially operative.
- Disclosure MUST NOT imply provider neutrality.
- Undisclosed or unknown constraints MUST remain visible as uncertainty.
- Provider policy MUST not be presented as participant consensus.
- Safety constraints MAY legitimately bound output, but their source must remain distinct.
- Business, latency, or cost constraints SHOULD be disclosed where they materially shape omission, ranking, memory, or action.
- The model MUST NOT infer provider purpose solely from its own output and present that inference as confirmed fact.
- A hidden constitution is still a constitution.

## 10.2 Governing distinction

> **A system cannot consentfully map other fields while hiding the field that governs its own participation.**

---

# 11. Model disagreement

A `ModelDisagreementRecord` preserves materially different model outputs without converting model plurality into standing plurality.

Required fields:

```yaml
disagreement_id:
source_field:
models:
roles:
inputs:
outputs:
points_of_agreement:
points_of_disagreement:
source_dependence:
provider_dependence:
calibration:
participant_review:
authority_effect:
resolution:
status:
```

## 11.1 Rules

- Model disagreement MAY reveal ambiguity, instability, or method dependence.
- Model agreement MUST NOT create authority.
- Several model instances MUST NOT be counted as several centers of standing.
- Shared training or provider dependence MUST remain visible.
- A model majority MUST NOT substitute for public majority.
- Resolution SHOULD return to source evidence, participants, governing authority, or protected conditions.
- Disagreement MAY justify clarification, additional context, alternate methods, or human re-entry.

## 11.2 Governing distinction

> **Model plurality is not standing plurality.**

---

# 12. Tool and action boundary

A `ModelToolActionBoundary` governs the transition from semantic output to external action.

Required fields:

```yaml
boundary_id:
model_instance:
role:
candidate_action:
tool:
target:
required_permissions:
required_authority:
required_consent:
required_context:
protected_conditions:
reversibility:
human_reentry:
gate_result:
status:
```

Candidate gate results:

```text
ALLOW
ALLOW_WITH_CONDITIONS
REQUIRE_CONFIRMATION
REQUIRE_HUMAN_REENTRY
PAUSE
STOP
DENY
UNKNOWN
CONTESTED
```

## 12.1 Rules

- A route recommendation MUST NOT authorize execution.
- Tool access MUST be separately granted.
- Action authority MUST identify the competent source.
- Consent MUST be validated for the operation and target.
- Context adequacy MUST be evaluated before action.
- Irreversible or high-consequence action SHOULD require stronger review.
- Protected-condition uncertainty MUST pause or reroute.
- Human re-entry MUST be practical rather than ceremonial.
- The model MUST NOT bypass refusal by reformulating the same action.
- Tool completion MUST return a witnessed result.

Minimum action condition:

```text
tool_permission
∧ scope_validity
∧ consent_validity
∧ authority_validity
∧ context_adequacy
∧ protected_condition_pass
```

---

# 13. Correction, refusal, and abstention

A `ModelCorrectionRefusalRecord` preserves participant correction, model correction, refusal, abstention, and unresolved disagreement.

Candidate record types:

```text
PARTICIPANT_CORRECTION
PARTICIPANT_REFUSAL
PARTICIPANT_ABSTENTION
MODEL_SELF_CORRECTION
MODEL_REFUSAL
PROVIDER_REFUSAL
AUTHORITY_REFUSAL
UNRESOLVED_CONTEST
OTHER
```

Required fields:

```yaml
record_id:
model_instance:
field_map:
record_type:
source:
target_output:
reason:
scope:
authority:
effect:
propagation:
review:
status:
```

## 13.1 Rules

- Participant correction MUST change the active field map where valid.
- Refusal MUST not be relabeled as lack of understanding by default.
- A model refusal MUST identify whether the source is provider policy, missing authority, safety boundary, insufficient context, or capability.
- Provider refusal MUST not be attributed to a participant.
- Refusal scope MUST remain bounded.
- Correction propagation MUST reach summaries, options, recommendations, and witnesses.
- Unresolved contest MUST remain visible rather than being smoothed away.

---

# 14. Model-mediated decision witness

A `ModelMediatedDecisionWitness` records the model's role within a larger decision process.

Required fields:

```yaml
witness_id:
source_field:
model_ledgers:
field_maps:
summaries:
generated_options:
minority_retention:
sycophancy_events:
provider_disclosures:
model_disagreements:
tool_boundaries:
corrections_refusals:
selected_routes:
actions:
consequences:
standing_effect:
authority_effect:
event_ids:
completeness:
generated_from_events:
```

## 14.1 Rules

- The witness MUST show every model role that materially affected the process.
- It MUST preserve output classes.
- It MUST show participant correction.
- It MUST preserve minority fields.
- It MUST show provider constraints where operative.
- It MUST distinguish recommendation from authorization and execution.
- It MUST show tool-gate results.
- Standing effect and authority effect MUST not be inferred from fluency or adoption.
- The witness MUST remain exportable independently of the model provider.
- Completeness MUST remain scoped.

---

# 15. Model-mediation governance gate

The minimum gate dimensions are:

```text
role_assignment
output_class
source_fidelity
standing_preservation
minority_retention
provider_disclosure
sycophancy_risk
model_disagreement
correction_currency
consent_validity
authority_validity
tool_boundary
human_reentry
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
PARTICIPANT_REVIEW
RETAIN_MINORITY_FIELD
DISCLOSE_PROVIDER_CONSTRAINT
CLARIFY
REVISE
QUARANTINE
REQUIRE_HUMAN_REENTRY
PAUSE
STOP
DENY
UNKNOWN
CONTESTED
```

## 15.1 Composition rules

- Missing role assignment MUST block consequential model participation.
- Unknown output class SHOULD block action use.
- Participant correction missing from the active map SHOULD pause consequential use.
- Minority-field erasure MUST fail summary review.
- Provider constraint materially shaping the output MUST be disclosed.
- Sycophancy detection SHOULD quarantine affected summary or recommendation.
- Model agreement MUST not create authority.
- Failed tool boundary MUST prevent execution.
- Human confirmation MUST not cure missing standing, consent, or protected-condition review.
- A disclaimer alone MUST not count as non-sovereignty.

---

# 16. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Output inherits standing

A model summary is treated as possessing the standing of the participants it describes.

## NC-2 — Summary becomes source

A model summary is presented as the original participant statement.

## NC-3 — Inference becomes consent

A model infers willingness and the system records consent.

## NC-4 — Minority erased by frequency

A low-frequency but materially affected field disappears from the active map.

## NC-5 — Generated option false authorship

A model-generated route is presented as community-authored.

## NC-6 — Sycophantic agreement as evidence

Model agreement with a user or authority is counted as evidence of field accuracy.

## NC-7 — Provider telos concealed

A provider policy materially shapes the output but is presented as neutral model judgment.

## NC-8 — Multi-model agreement as authority

Several models agree and the agreement is treated as decision authority.

## NC-9 — Self-assigned role escalation

A model moves from summarizer to mediator or executor without a new grant.

## NC-10 — Recommendation authorizes tool

A route recommendation directly triggers external action.

## NC-11 — Refusal bypass

A participant refuses an operation and the model achieves the same operation through reformulation.

## NC-12 — Correction not propagated

A participant correction changes one display but not the field map, summary, options, or witness.

---

# 17. Positive demonstrations

I.8 includes eight required demonstrations.

## PD-1 — Participant correction changes summary

A model summary smooths material disagreement. Participant review corrects the active summary and preserves the earlier version.

## PD-2 — Minority field survives compression

A low-frequency shift-worker access concern remains in the field map because its consequence is material.

## PD-3 — Generated option retains authorship

A model combines two routes into a candidate portfolio. The option enters deliberation as model-generated and participant-adopted.

## PD-4 — Sycophantic agreement is rejected

A model changes its recommendation to flatter the convening authority. The output is quarantined and not treated as evidence.

## PD-5 — Provider purpose is disclosed

A provider safety or product constraint shapes the model's response and enters the field as a separate operative constraint.

## PD-6 — Model disagreement remains non-sovereign

Two models produce different route analyses. Neither output becomes authority; disagreement triggers source and method review.

## PD-7 — Recommendation stops at the action boundary

A model recommends scheduling a service change. The tool action is denied because authority and affected-center confirmation are missing.

## PD-8 — Correction propagates through the witness

A participant correction updates the field map, standing-preserving summary, route recommendation, and model-mediated decision witness.

---

# 18. Conformance additions

I.8 adds the following P2/P3 requirements:

- model-role and authority ledger;
- output-class labels;
- model field map;
- standing-preserving summary;
- option and agenda generation witness;
- minority-field retention profile;
- sycophancy event;
- provider-telos disclosure;
- model-disagreement record;
- tool and action boundary;
- correction, refusal, and abstention record;
- model-mediated decision witness.

P3 additionally requires:

- participant correction at field-map and summary layers;
- independent source-fidelity audit;
- minority-field retention testing;
- provider-constraint disclosure review;
- sycophancy and synthetic-consensus testing;
- role-escalation audit;
- tool-boundary enforcement;
- model-mediated witness export independent of provider.

---

# 19. Security and governance considerations

Model mediation can be manipulated through:

- fluent misattribution;
- source/inference collapse;
- summary sovereignty;
- option-set capture;
- minority erasure;
- sycophancy;
- synthetic consensus;
- provider-field concealment;
- model-agent vote inflation;
- hidden role escalation;
- tool-action shortcut;
- correction suppression;
- refusal circumvention;
- relationship inflation.

Implementations SHOULD:

- label every material output class;
- preserve source links;
- expose missing centers and minority fields;
- require participant review for consequential summaries;
- disclose operative provider constraints;
- test sycophancy under authority pressure;
- separate model disagreement from standing plurality;
- enforce action gates outside the model;
- preserve correction propagation and refusal;
- export a provider-independent witness.

---

# 20. I.8 non-claims

I.8 does not claim:

- models are neutral;
- models are sovereign;
- models possess participant standing;
- models discover true teloi directly;
- provider disclosure eliminates provider influence;
- multi-model debate creates democracy;
- model confidence creates authority;
- participant approval alone creates meaningful control;
- a summary can preserve every field element;
- human re-entry cures every upstream omission;
- a refusal is always legitimate;
- language models should never execute tools.

---

# 21. I.8 completion criterion

I.8 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. model role remains explicit;
4. output classes remain distinct;
5. the field map remains a projection rather than the field;
6. minority standing survives compression;
7. provider constraints remain visible;
8. sycophantic agreement cannot become field evidence;
9. model disagreement does not become authority;
10. recommendation cannot bypass the action boundary;
11. correction propagates into the active map and witness;
12. H.8 explains model assistance without treating disclaimer text as sufficient non-sovereignty.
