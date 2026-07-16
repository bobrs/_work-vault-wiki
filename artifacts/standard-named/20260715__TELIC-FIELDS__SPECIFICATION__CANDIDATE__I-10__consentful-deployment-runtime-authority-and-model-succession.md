---
title: "I.10 — Consentful Deployment, Runtime Authority, and Model Succession Specification"
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
  - "I.8 — Non-Sovereign Semantic Navigation and Model Mediation Specification"
  - "I.9 — Consentful Training, Source Standing, and Model Lineage Specification"
---

# I.10 — Consentful Deployment, Runtime Authority, and Model Succession Specification

## 1. Purpose

I.10 defines how a trained model enters a live institution, community, service, or relationship and acquires only the runtime authority required for a named purpose.

Its governing rule is:

> **Training creates capability. Deployment creates consequence. Authority must be established again.**

A model may have:

- documented training provenance;
- a strong constitution;
- bounded model roles;
- high capability;
- reliable evaluation;
- lawful access to tools;
- a trusted provider.

None of those facts determines whether the model may affect a particular person, institution, account, device, schedule, benefit, contract, record, or public process.

Deployment creates a new field.

That field includes:

- operators;
- affected people;
- represented and missing centers;
- runtime purpose;
- tools;
- data flows;
- output capture;
- memories;
- provider constraints;
- operational incentives;
- incidents;
- updates;
- transfers;
- shutdown conditions;
- residual obligations.

I.10 therefore separates:

```text
TRAINING AUTHORITY
≠ DEPLOYMENT AUTHORITY
≠ TOOL PERMISSION
≠ OPERATION AUTHORITY
≠ AFFECTED-CENTER CONSENT
≠ LEGITIMACY
```

It defines:

- deployment-field assemblies;
- operator and affected-center standing records;
- runtime-purpose and authority grants;
- capability, role, and tool grants;
- deployment consent, notice, and refusal profiles;
- runtime memory and output-capture records;
- deployment-drift and scope-expansion events;
- incident, breach, repair, and compensation records;
- runtime monitoring and consequence-return records;
- operator-transfer and provider-change records;
- model-version succession, rollback, retirement, and residual-state records;
- consentful-deployment witnesses.

---

# 2. Normative scope

I.10 defines:

- `DeploymentFieldAssembly`;
- `DeploymentStandingRecord`;
- `RuntimePurposeAuthorityGrant`;
- `CapabilityRoleToolGrant`;
- `DeploymentConsentNoticeRefusalProfile`;
- `RuntimeMemoryOutputCaptureRecord`;
- `DeploymentDriftEvent`;
- `DeploymentIncidentRepairRecord`;
- `RuntimeMonitoringConsequenceReturn`;
- `OperatorProviderTransferRecord`;
- `ModelVersionSuccessionRetirementRecord`;
- `ConsentfulDeploymentWitness`.

I.10 does not define:

- one universal consent requirement for every public or institutional deployment;
- one universal human-in-the-loop pattern;
- one universal incident threshold;
- one universal compensation method;
- one universal update or rollback policy;
- automatic legitimacy from notice;
- automatic legitimacy from user acceptance of terms;
- automatic authority from model accuracy;
- automatic continuity across model versions;
- automatic release from obligation when a service shuts down.

---

# 3. Deployment-field assembly

A `DeploymentFieldAssembly` defines the live field into which a model is introduced.

Required fields:

```yaml
assembly_id:
deployment:
model_lineage:
model_version:
provider:
operator:
runtime_purpose:
jurisdiction:
affected_centers:
represented_centers:
missing_centers:
dependencies:
tools:
data_flows:
protected_conditions:
known_risks:
review:
status:
```

Candidate statuses:

```text
DRAFT
PARTIAL
READY_FOR_REVIEW
AUTHORIZED
CONTESTED
PAUSED
SUSPENDED
RETIRED
UNKNOWN
```

## 3.1 Rules

- The deployment field MUST be assembled independently of the training witness.
- It MUST identify affected centers whether or not they contributed training data.
- It MUST identify operator, provider, purpose, tools, data flows, and protected conditions.
- It MUST preserve missing or uncertain standing.
- It MUST identify material dependencies and failure routes.
- It MUST not claim that training legitimacy creates runtime legitimacy.
- Material missing standing MAY require pause, representation, or a narrower deployment.

## 3.2 Governing distinction

> **A model does not inherit permission to affect a person merely because it learned from someone else.**

---

# 4. Operator and affected-center standing

A `DeploymentStandingRecord` identifies who holds standing within the runtime field.

Candidate standing bases:

```text
DIRECTLY_AFFECTED
SUBJECT_OF_DECISION
DATA_SOURCE
ACCOUNT_HOLDER
WORKER
DEPENDENT
RIGHTS_HOLDER
OPERATOR
PROVIDER
PUBLIC_AUTHORITY
REPRESENTATIVE
AUDITOR
REPAIR_CLAIMANT
FUTURE_AFFECTED_CENTER
OTHER
```

Required fields:

```yaml
record_id:
assembly:
center:
standing_basis:
role:
scope:
representation_source:
authority:
consent_relation:
refusal_route:
correction_route:
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

- Runtime standing MUST NOT depend on contribution to training.
- Operator standing MUST remain distinct from affected-center standing.
- Provider standing MUST remain distinct from operator authority.
- Affected centers MUST receive correction, refusal, or appeal routes appropriate to consequence.
- Representation MUST identify source and limits.
- Standing does not guarantee control of every decision.
- Lack of training contribution MUST NOT erase runtime consequence-bearing standing.

---

# 5. Runtime purpose and authority

A `RuntimePurposeAuthorityGrant` records which purpose may recruit which capabilities for which centers and period.

Required fields:

```yaml
grant_id:
assembly:
grantor:
grantee:
runtime_purpose:
allowed_operations:
prohibited_operations:
affected_centers:
authority_basis:
consent_basis:
scope:
valid_time:
conditions:
review_triggers:
withdrawal_or_expiry:
status:
```

## 5.1 Rules

- Runtime purpose MUST be specific enough to test.
- Authority MUST be operation-specific.
- Authority MUST identify grantor and grantee.
- Training authority MUST not substitute for runtime authority.
- Purpose expansion MUST require renewed review.
- The grant MUST expire, renew, or remain reviewable.
- Prohibited operations MUST remain explicit.
- A broad service description MUST not conceal consequential suboperations.
- Where consent is the authority basis, consent MUST remain scoped and revocable where applicable.

---

# 6. Capability, role, and tool grant

A `CapabilityRoleToolGrant` governs which capabilities a deployed model may exercise.

Required fields:

```yaml
grant_id:
assembly:
model_version:
capabilities:
assigned_roles:
allowed_tools:
prohibited_tools:
operation_limits:
data_limits:
action_limits:
required_confirmation:
required_human_reentry:
reversibility:
logging:
status:
```

## 6.1 Rules

- Capability MUST remain distinct from assigned role.
- Assigned role MUST remain distinct from tool permission.
- Tool permission MUST remain distinct from authority over the target.
- A model MUST NOT self-expand capability use or role.
- Tool grants MUST be operation-specific.
- Action limits MUST include consequence and reversibility.
- Human re-entry MUST be practical and timely.
- A user confirmation MUST not cure missing authority, standing, or protected-condition review.
- Tool execution MUST produce a witnessed result.

## 6.2 Minimum action condition

```text
capability available
∧ assigned role permits operation
∧ tool grant permits tool
∧ runtime authority covers operation
∧ affected-center consent or other authority is valid
∧ context is adequate
∧ protected conditions pass
```

---

# 7. Deployment consent, notice, and refusal

A `DeploymentConsentNoticeRefusalProfile` records how affected centers are informed, what they authorize, what alternative authority applies, and how refusal is handled.

Required fields:

```yaml
profile_id:
assembly:
center_or_group:
notice:
consent:
other_authority_basis:
operations:
data_uses:
output_uses:
alternatives:
refusal:
appeal:
accessibility:
valid_time:
status:
```

## 7.1 Rules

- Notice MUST not be represented as consent.
- Consent to receive a service MUST not imply consent to unrelated output capture or retraining.
- Terms acceptance MUST not be treated as meaningful consent where alternatives or comprehension are absent.
- Refusal MUST be operation-specific where possible.
- Refusal MUST not be bypassed through another model or reformulated workflow.
- Non-consensual authority bases MUST remain visible.
- Accessibility and practical alternatives SHOULD be represented.
- Consent and refusal MUST propagate into runtime data and tool controls.

---

# 8. Runtime memory and output capture

A `RuntimeMemoryOutputCaptureRecord` governs what the deployment records, remembers, exports, or reuses.

Required fields:

```yaml
record_id:
assembly:
session_or_subject:
input_sources:
runtime_memory:
output_capture:
purpose:
authority:
consent:
retention:
cross_session_use:
cross_subject_use:
training_or_evaluation_use:
export:
correction:
withdrawal:
status:
```

## 8.1 Rules

- Service use MUST not imply consent to training or evaluation use.
- Runtime memory MUST remain purpose-limited.
- Output capture MUST identify which outputs and metadata are retained.
- Cross-session and cross-subject use MUST be separately governed.
- Training and evaluation use MUST be separately authorized.
- Corrections MUST propagate to active profiles, summaries, and downstream uses.
- Withdrawal MUST identify what can be deleted, blocked, or retained as witness.
- A runtime record MUST distinguish model output from authoritative institutional record.
- Provider and operator copies MUST remain visible.

## 8.2 Governing distinction

```text
service consent
≠ memory consent
≠ output-capture consent
≠ evaluation consent
≠ training consent
≠ cross-subject reuse
```

---

# 9. Deployment drift and scope expansion

A `DeploymentDriftEvent` records when operational purpose, role, data use, affected centers, tools, provider, model behavior, or authority changes materially.

Candidate drift types:

```text
PURPOSE_DRIFT
ROLE_DRIFT
TOOL_DRIFT
DATA_USE_DRIFT
AFFECTED_CENTER_EXPANSION
PROVIDER_DRIFT
OPERATOR_DRIFT
MODEL_BEHAVIOR_DRIFT
POLICY_DRIFT
AUTOMATION_DRIFT
OTHER
```

Required fields:

```yaml
event_id:
assembly:
drift_type:
baseline:
observed_change:
affected_centers:
affected_operations:
authority_impact:
consent_impact:
protected_condition_impact:
immediate_response:
reauthorization:
repair:
status:
```

## 9.1 Rules

- Material drift MUST trigger review.
- Purpose drift MUST require renewed authority.
- Expansion to new affected centers MUST create standing review.
- Tool or automation drift MUST not inherit prior permission automatically.
- Provider or operator change MUST be treated as a new governance event.
- The deployment MUST pause where drift creates unknown protected-condition impact.
- Drift repair MUST update active grants, notices, memories, and witnesses.
- Silent scope expansion MUST fail conformance.

---

# 10. Incident, breach, repair, and compensation

A `DeploymentIncidentRepairRecord` records runtime harm, authority failure, data misuse, unsafe action, or operational breach.

Candidate incident classes:

```text
UNAUTHORIZED_ACTION
WRONGFUL_DENIAL
DATA_MISUSE
PRIVACY_BREACH
FALSE_CLASSIFICATION
HALLUCINATED_RECORD
TOOL_ERROR
MODEL_DRIFT
DISCRIMINATORY_EFFECT
REFUSAL_BYPASS
CORRECTION_FAILURE
OTHER
```

Required fields:

```yaml
record_id:
assembly:
incident_class:
detected_at:
affected_centers:
affected_actions:
source:
immediate_containment:
evidence:
consequences:
model_or_system_change:
affected_center_repair:
compensation:
correction_propagation:
accountability:
review:
status:
```

## 10.1 Rules

- Incident response MUST address affected centers, not only model quality.
- Model retraining MUST not count as full repair by itself.
- Immediate containment MUST preserve evidence.
- Correction MUST propagate into records, decisions, and derivatives.
- Compensation or restitution SHOULD be considered where material consequence occurred.
- Accountability MUST identify operator, provider, model, and institutional roles.
- Affected centers MUST have a practical review route.
- Repair MAY include reversal, restoration, notice, compensation, policy change, model change, or retirement.
- Incident closure MUST not erase unresolved consequences.

## 10.2 Governing distinction

> **A system is not repaired merely because the model improves after someone else absorbed the harm.**

---

# 11. Runtime monitoring and consequence return

A `RuntimeMonitoringConsequenceReturn` records observed effects and returns them to deployment governance.

Required fields:

```yaml
record_id:
assembly:
monitoring_scope:
metrics:
qualitative_evidence:
affected_centers:
expected_consequences:
observed_consequences:
unexpected_consequences:
distributional_effects:
protected_condition_status:
drift_signals:
review_triggered:
revision_options:
status:
```

## 11.1 Rules

- Monitoring MUST include consequence, not only model performance.
- Aggregate success MUST not erase concentrated harm.
- Affected-center evidence MUST remain available.
- Protected conditions MUST be monitored separately from average metrics.
- Drift signals MUST trigger review.
- Observed consequence SHOULD return to the originating deployment witness.
- Monitoring data collection MUST remain separately governed.
- A model MAY meet technical benchmarks while failing the deployment field.

---

# 12. Operator transfer and provider change

An `OperatorProviderTransferRecord` records a change in operator, provider, custodian, infrastructure, jurisdiction, or commercial control.

Required fields:

```yaml
record_id:
assembly:
change_type:
prior_operator_or_provider:
successor_operator_or_provider:
effective_time:
transferred_assets:
transferred_authority:
nontransferable_authority:
consent_and_notice:
data_and_memory_transfer:
restrictions:
open_incidents:
repair_obligations:
review:
status:
```

Candidate change types:

```text
OPERATOR_TRANSFER
PROVIDER_CHANGE
ACQUISITION
OUTSOURCING
JURISDICTION_CHANGE
INFRASTRUCTURE_MIGRATION
CUSTODY_TRANSFER
OTHER
```

## 12.1 Rules

- Authority MUST not transfer merely because assets transfer.
- Consent and notices MUST be reviewed for the successor.
- Nontransferable permissions MUST remain nontransferable.
- Open incidents and repair obligations MUST follow the successor where applicable.
- Runtime memory and output capture MUST remain governed during transfer.
- Jurisdiction changes MUST trigger renewed legal and constitutional review.
- A successor MUST identify inherited restrictions and unknowns.
- Provider change MUST not be hidden as a routine technical update.

---

# 13. Model version succession, rollback, retirement, and residual state

A `ModelVersionSuccessionRetirementRecord` governs updates, model swaps, rollbacks, retirement, and shutdown.

Required fields:

```yaml
record_id:
assembly:
prior_model_version:
successor_model_version:
change_type:
reason:
capability_changes:
behavior_changes:
policy_changes:
authority_review:
consent_and_notice_review:
compatibility:
migration:
rollback:
retirement:
residual_state:
open_obligations:
verification:
status:
```

Candidate change types:

```text
PATCH
MODEL_UPDATE
MODEL_REPLACEMENT
FINE_TUNE_CHANGE
PROVIDER_MODEL_SWAP
ROLLBACK
SUSPENSION
RETIREMENT
SHUTDOWN
OTHER
```

## 13.1 Rules

- A new model version MUST not silently inherit every runtime grant.
- Material capability or policy change MUST trigger authority review.
- Migration MUST preserve correction, refusal, incident, and restriction lineage.
- Rollback MUST remain possible or explicitly unavailable.
- Retirement MUST stop declared operations.
- Retirement MUST not erase open incidents, claims, records, or repair duties.
- Residual memory, caches, logs, embeddings, credentials, and tools MUST be accounted for.
- Successor models MUST inherit unresolved obligations where applicable.
- A shutdown witness SHOULD identify what remains, where, under whose custody, and for how long.

## 13.2 Governing distinction

> **Operational continuity is not permission continuity. Model succession is a new constitutional event.**

---

# 14. Consentful-deployment witness

A `ConsentfulDeploymentWitness` records the governed runtime lineage.

Required fields:

```yaml
witness_id:
deployment_assemblies:
standing_records:
runtime_authority_grants:
capability_role_tool_grants:
consent_notice_refusal_profiles:
memory_output_capture_records:
drift_events:
incident_repair_records:
monitoring_consequence_records:
operator_provider_transfers:
version_succession_retirement_records:
actions:
consequences:
open_obligations:
unknowns:
event_ids:
completeness:
generated_from_events:
generated_at:
```

## 14.1 Rules

- The witness MUST preserve deployment standing independently of training contribution.
- It MUST preserve runtime purpose and authority.
- It MUST preserve tool and role grants.
- It MUST preserve runtime data and output-capture scope.
- It MUST preserve drift and renewed authority.
- It MUST preserve incidents, repair, and compensation.
- It MUST preserve monitoring and consequence return.
- It MUST preserve transfers, version changes, rollback, and retirement.
- It MUST preserve open obligations and residual state.
- It MUST remain exportable independently of provider and operator.
- It MUST not label a deployment simply `CONSENTFUL` without a qualified profile.

Candidate deployment classifications:

```text
AUTHORIZED_AND_CONSENTED
AUTHORIZED_BY_PUBLIC_MANDATE
MIXED_AUTHORITY
PARTIALLY_CONSENTED
CONTESTED_DEPLOYMENT
MATERIALLY_UNKNOWN
UNAUTHORIZED_OR_BREACHED
RETIRED_WITH_OPEN_OBLIGATIONS
```

---

# 15. Consentful-deployment governance gate

The minimum gate dimensions are:

```text
deployment_field
affected_center_standing
runtime_purpose
operation_authority
tool_scope
consent_or_other_authority
runtime_data_use
protected_conditions
drift_status
incident_status
monitoring
operator_provider_continuity
model_version_continuity
retirement_and_residuals
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
ADD_STANDING
ADD_AUTHORITY
ADD_CONSENT_OR_NOTICE
NARROW_PURPOSE
REVOKE_TOOL
PAUSE
SUSPEND
ROLLBACK
REPAIR
COMPENSATE
TRANSFER_REVIEW
RETIRE
FAIL
UNKNOWN
CONTESTED
```

## 15.1 Composition rules

- Training legitimacy MUST not create deployment authority.
- Missing affected-center standing MAY require pause.
- Capability or tool permission MUST not create operation authority.
- Runtime output capture without authority MUST fail.
- Purpose drift MUST trigger reauthorization.
- Unresolved material incident MUST affect deployment status.
- Model updates MUST trigger grant and compatibility review.
- Operator transfer MUST not silently transfer nontransferable consent.
- Retirement without residual-state accounting MUST fail.
- Human confirmation MUST not override missing constitutional prerequisites.

---

# 16. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Training lineage as deployment authority

A well-governed training witness is treated as permission to deploy in any context.

## NC-2 — Non-contributor has no standing

A person affected at runtime is denied standing because they contributed no training data.

## NC-3 — Capability as authority

A model can perform an operation and is therefore allowed to perform it.

## NC-4 — Tool permission as target authority

A tool token is treated as permission to affect the target center.

## NC-5 — Notice as consent

A deployment notice is recorded as consent.

## NC-6 — Service consent as output-capture consent

Agreement to receive the service is treated as permission to retain outputs for evaluation or training.

## NC-7 — Purpose drift without reauthorization

A model moves from assistance to eligibility decision without renewed authority.

## NC-8 — Model tuning as complete repair

After a harmful decision, the model is updated but the affected center receives no restoration, correction, or compensation.

## NC-9 — Operator transfer erases obligations

A successor operator receives the system without open incidents, refusals, or restrictions.

## NC-10 — Silent model-version substitution

A materially different model replaces the prior version without authority or notice review.

## NC-11 — Human click cures missing authority

A human approves an action without standing, authority, or protected-condition review.

## NC-12 — Retirement erases residual duties

The service shuts down and treats logs, claims, memories, and repair obligations as extinguished.

---

# 17. Positive demonstrations

I.10 includes eight required demonstrations.

## PD-1 — Training lineage does not create deployment authority

A model with a strong consentful-training witness remains blocked until a county health deployment grant exists.

## PD-2 — Affected non-contributor receives standing

A patient who never contributed training data enters the deployment field because the model affects access to care.

## PD-3 — Tool-capable model remains blocked

The model can call a scheduling tool but lacks staffing authority and affected-practice confirmation.

## PD-4 — Runtime output capture is separately governed

Service delivery is allowed, but output retention for evaluation and retraining remains disabled without a separate grant.

## PD-5 — Purpose drift triggers reauthorization

A model deployed for navigation is asked to deny eligibility; the role expansion pauses and enters authority review.

## PD-6 — Incident creates repair and compensation

A false classification causes service denial. Repair restores access, corrects records, compensates burden, and updates the model.

## PD-7 — Model update preserves version and obligation lineage

A new model version receives a renewed grant, carries corrections and open incidents, and preserves rollback.

## PD-8 — Retirement stops operation but preserves residual obligations

The system shuts down, revokes tools, inventories residual memory, transfers open claims, and preserves the final witness.

---

# 18. Conformance additions

I.10 adds the following P2/P3 requirements:

- deployment-field assembly;
- runtime standing;
- purpose and authority grant;
- capability, role, and tool grant;
- deployment consent, notice, and refusal;
- runtime memory and output-capture governance;
- drift and scope-expansion detection;
- incident, repair, compensation, and correction;
- consequence monitoring;
- operator and provider transfer;
- version succession, rollback, and retirement;
- consentful-deployment witness.

P3 additionally requires:

- affected-center standing review;
- external action-gate enforcement;
- independent incident and repair review;
- purpose-drift testing;
- provider-transfer audit;
- model-version compatibility testing;
- residual-state inventory;
- provider-independent deployment-witness export.

---

# 19. Security and governance considerations

Deployment systems can be manipulated through:

- standing exclusion;
- authority laundering;
- tool-token overreach;
- notice-as-consent;
- output-capture expansion;
- memory overretention;
- purpose drift;
- automation drift;
- silent provider change;
- model-version substitution;
- incident minimization;
- repair reduced to retraining;
- shutdown as obligation erasure.

Implementations SHOULD:

- assemble runtime standing independently;
- bind operations to authority;
- enforce tool gates outside the model;
- separate service, memory, capture, evaluation, and training consent;
- detect drift;
- preserve incident and compensation records;
- return consequences to governance;
- review transfers and version changes;
- account for residual state;
- export a provider-independent witness.

---

# 20. I.10 non-claims

I.10 does not claim:

- every deployment requires individual opt-in;
- public authority is always legitimate;
- notice is never useful;
- human approval is never meaningful;
- tools should never execute autonomously;
- every incident requires payment;
- every model update requires renewed consent from every center;
- every residual record should be retained indefinitely;
- retirement should erase history;
- a deployment witness makes the deployment just.

---

# 21. I.10 completion criterion

I.10 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. training and deployment authority remain distinct;
4. runtime standing includes affected non-contributors;
5. capability and tool access do not become authority;
6. runtime data capture remains separately governed;
7. purpose drift triggers reauthorization;
8. incident repair addresses affected centers;
9. transfers preserve restrictions and open obligations;
10. model succession preserves version, rollback, and correction lineage;
11. retirement accounts for residual state;
12. H.10 explains runtime authority without treating deployment notice or human confirmation as sufficient legitimacy.
