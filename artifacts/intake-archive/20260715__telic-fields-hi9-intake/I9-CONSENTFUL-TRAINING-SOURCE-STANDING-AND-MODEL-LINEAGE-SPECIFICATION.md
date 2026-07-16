---
title: "I.9 — Consentful Training, Source Standing, and Model Lineage Specification"
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
  - "I.4 — Temporal Standing, Commitment, and Succession Specification"
  - "I.5 — Dependency, Drift, Lock-In, and Dissolution Specification"
  - "I.6 — Semantic Trails, Memory, and Retrieval Specification"
  - "I.8 — Non-Sovereign Semantic Navigation and Model Mediation Specification"
  - "F.11 — Consentfully Trained Models"
  - "G.12 — Training Data, Preference Aggregation, Constitution, and Model Governance"
---

# I.9 — Consentful Training, Source Standing, and Model Lineage Specification

## 1. Purpose

I.9 defines how data, human labor, preference judgments, constitutions, transformations, restrictions, benefits, withdrawals, corrections, and successor obligations remain attached through model training and derivative use.

Its governing rule is:

> **Training is a recruitment relation before it is an optimization procedure.**

Training recruits semantic and material capacity from outer fields into a model lineage.

Those recruited capacities may include:

- authored text;
- images;
- audio;
- code;
- community records;
- public documents;
- private records;
- archives;
- annotations;
- rankings;
- demonstrations;
- critiques;
- constitutions;
- synthetic outputs;
- model-generated labels;
- evaluation results;
- human correction;
- compute and infrastructure;
- cultural and collective knowledge.

The model may transform these sources.

Transformation does not dissolve standing.

Compression does not erase restrictions.

Availability does not become consent.

Legal access does not automatically settle ethical legitimacy.

Consent does not authorize what the consenting party does not legitimately control.

I.9 therefore separates:

```text
ACCESS
≠ PERMISSION
≠ CONSENT
≠ AUTHORITY
≠ LEGITIMACY
≠ UNLIMITED DOWNSTREAM USE
```

I.9 defines:

- source-center and dataset-standing records;
- collection and authorization records;
- transformation and dataset lineage;
- license, legal-basis, and consent-scope profiles;
- annotation and preference-data records;
- model-constitution lineage;
- preference-optimization records;
- synthetic-data ancestry;
- withdrawal and unlearning records;
- downstream correction and derivative propagation;
- benefit-sharing and contributor-recognition records;
- consentful-training witnesses.

---

# 2. Normative scope

I.9 defines:

- `SourceDatasetStandingRecord`;
- `CollectionAuthorizationRecord`;
- `TrainingTransformationLineage`;
- `LicenseAuthorityConsentProfile`;
- `AnnotationPreferenceDataRecord`;
- `ModelConstitutionLineage`;
- `PreferenceOptimizationRecord`;
- `SyntheticDataAncestryRecord`;
- `WithdrawalUnlearningRecord`;
- `DerivativeCorrectionPropagation`;
- `BenefitContributorRecognitionRecord`;
- `ConsentfulTrainingWitness`.

I.9 does not define:

- one universal legal basis for model training;
- one universal individual opt-in requirement;
- one universal community-governance model;
- guaranteed complete provenance;
- guaranteed exact unlearning;
- automatic legitimacy from documentation;
- automatic consent from payment;
- automatic consent from public posting;
- automatic ethics from copyright compliance;
- automatic copyright violation from every training use;
- a binary purity label for models.

---

# 3. Source and dataset standing

A `SourceDatasetStandingRecord` identifies the centers, relations, and claims attached to source material.

Required fields:

```yaml
record_id:
source_artifact_or_dataset:
source_centers:
affected_centers:
collective_or_community_standing:
source_class:
creation_context:
publication_context:
custody:
rights_and_interests:
sensitivity:
known_restrictions:
contestation:
review:
status:
```

Candidate source classes:

```text
INDIVIDUAL_AUTHORED
COLLECTIVE_AUTHORED
COMMUNITY_HELD
PUBLIC_RECORD
PUBLICATION
LICENSED_CORPUS
ARCHIVAL
RESEARCH_DATA
PLATFORM_CONTENT
ANNOTATION
PREFERENCE_DATA
MODEL_OUTPUT
SYNTHETIC
DERIVED
UNKNOWN
MIXED
```

Candidate statuses:

```text
ACTIVE
PARTIAL
CONTESTED
RESTRICTED
SUPERSEDED
WITHDRAWN
UNKNOWN
```

## 3.1 Rules

- Source standing MUST remain distinct from file ownership alone.
- A source MAY carry several centers of standing.
- Publication MUST NOT erase source or community interests.
- Collective or community standing MUST be reviewed where source meaning exceeds individual authorship.
- A person MUST NOT authorize use of collective knowledge they do not legitimately control.
- Unknown standing MUST remain visible.
- Dataset-level description MUST NOT erase item-level restrictions where material.

## 3.2 Governing distinction

> **Public does not mean ownerless. Accessible does not mean available for every purpose.**

---

# 4. Collection and authorization

A `CollectionAuthorizationRecord` records how a source entered the training lineage.

Required fields:

```yaml
collection_id:
source_record:
collector:
collection_method:
collection_purpose:
authority_basis:
consent_basis:
notice:
scope:
valid_time:
restrictions:
transfer:
withdrawal:
evidence:
status:
```

Candidate authority bases:

```text
INDIVIDUAL_CONSENT
COLLECTIVE_AUTHORITY
COMMUNITY_GOVERNANCE
CONTRACT
LICENSE
PUBLIC_DOMAIN
PUBLIC_MANDATE
RESEARCH_ETHICS_AUTHORIZATION
FIDUCIARY_STEWARDSHIP
STATUTORY_AUTHORITY
OTHER_LAWFUL_BASIS
UNKNOWN
CONTESTED
NONE
```

## 4.1 Rules

- Collection authority MUST be recorded separately from later training authority.
- Consent MUST identify scope, purpose, recipient, and meaningful limits.
- Notice alone MUST NOT be treated as consent.
- Silence MUST NOT be treated as consent.
- Contract or license MUST remain distinguishable from consent.
- Public-domain status MUST not erase privacy, community, or contextual interests automatically.
- Collection through technical accessibility MUST not create authority by itself.
- Withdrawal and contest routes MUST remain attached.

---

# 5. License, authority, and consent scope

A `LicenseAuthorityConsentProfile` records the basis under which each transition in the lineage proceeds.

Candidate transitions:

```text
CREATE
PUBLISH
COLLECT
STORE
AGGREGATE
FILTER
TRANSFORM
ANNOTATE
LABEL
RANK
TRAIN
EVALUATE
RELEASE
DEPLOY
LOG_OUTPUT
RETRAIN
TRANSFER
FORK
SUCCEED
DISSOLVE
```

Required fields:

```yaml
profile_id:
source_or_dataset:
transitions:
authority_for_each_transition:
consent_for_each_transition:
license_for_each_transition:
purpose_for_each_transition:
restrictions:
recipient_classes:
revocation_or_expiry:
unknowns:
status:
```

## 5.1 Rules

- Authority MUST be transition-specific.
- One consent event MUST NOT be presumed to authorize every downstream transition.
- License MUST NOT be represented as consent.
- Consent MUST NOT be represented as copyright ownership.
- Legal basis and ethical legitimacy MUST remain separately assessable.
- Restrictions MUST propagate to derivative datasets and models where applicable.
- Recipient and purpose expansion MUST require review.
- Unknown transitions MUST remain explicit.

## 5.2 Governing distinction

```text
publication permission
≠ collection permission
≠ training permission
≠ release permission
≠ deployment permission
≠ output-reuse permission
```

---

# 6. Transformation and dataset lineage

A `TrainingTransformationLineage` records each material transformation applied to source material.

Candidate transformations:

```text
COPY
NORMALIZE
FILTER
DEDUPE
REDACT
TRANSLATE
SUMMARIZE
CHUNK
TOKENIZE
EMBED
LABEL
RANK
AUGMENT
SYNTHESIZE
MIX
SAMPLE
WEIGHT
REMOVE
QUARANTINE
OTHER
```

Required fields:

```yaml
lineage_id:
input_sources:
transformation_steps:
operators:
purpose:
parameters_or_rules:
restriction_propagation:
losses:
new_inferences:
derived_outputs:
quality_review:
status:
```

## 6.1 Rules

- Transformations MUST remain visible.
- Deduplication MUST not erase provenance.
- Filtering MUST be treated as governance.
- Redaction MUST not be assumed to remove every standing interest.
- Summaries MUST not inherit source authority automatically.
- Translation MUST preserve source linkage.
- New inferences created during transformation MUST be labeled.
- Restriction loss MUST trigger breach review.
- Dataset mixing MUST preserve source-class and authority boundaries.

---

# 7. Annotation and preference data

An `AnnotationPreferenceDataRecord` records human or model labor used to classify, rank, demonstrate, critique, or prefer outputs.

Required fields:

```yaml
record_id:
task:
contributors:
contributor_roles:
instructions:
working_conditions:
compensation:
source_inputs:
output_type:
preference_context:
disagreement:
quality_control:
authority:
consent:
downstream_use:
withdrawal:
status:
```

Candidate output types:

```text
LABEL
RANKING
DEMONSTRATION
CRITIQUE
REWRITE
SAFETY_JUDGMENT
STYLE_JUDGMENT
FACTUALITY_JUDGMENT
CONSTITUTIONAL_JUDGMENT
OTHER
```

## 7.1 Rules

- Preference data MUST be treated as a conditional projection under a task.
- Annotation output MUST NOT be represented as universal human preference.
- Contributor disagreement MUST not be silently collapsed.
- Instructions and task framing MUST remain visible.
- Compensation MUST NOT be treated as unlimited downstream consent.
- Labor conditions SHOULD remain reviewable where material.
- Model-generated labels MUST remain distinct from human judgments.
- Preference aggregation MUST preserve method and minority judgments.

## 7.2 Governing distinction

> **Preference data is a projection of judgment under a task, not a sample from a single human telos.**

---

# 8. Model constitution lineage

A `ModelConstitutionLineage` records the principles, policies, examples, authorities, and revision history that shape model behavior.

Required fields:

```yaml
constitution_id:
model_lineage:
principles:
principle_sources:
authors_or_authorities:
affected_centers:
adoption_process:
training_or_inference_use:
conflicts:
exceptions:
revision_history:
contest_route:
status:
```

## 8.1 Rules

- A constitution MUST identify its authors and authority.
- Explicitness does not create legitimacy automatically.
- Provider principles MUST not be presented as public consensus.
- Participant-derived rules MUST preserve adoption lineage.
- Conflicts between principles MUST remain visible.
- Exceptions and operational overrides MUST be witnessed.
- Constitutions SHOULD remain contestable.
- A model MUST NOT be treated as the constituent body that authorized its own constitution.

## 8.2 Governing distinction

> **A constitution is not legitimate merely because it is explicit. It becomes governable because it is explicit.**

---

# 9. Preference optimization

A `PreferenceOptimizationRecord` records how demonstrations, rankings, critiques, constitutions, or model-generated judgments shape training.

Candidate optimization families:

```text
SUPERVISED_FINE_TUNING
RLHF
DPO
RLAIF
CONSTITUTIONAL_AI
REWARD_MODELING
REJECTION_SAMPLING
SELF_TRAINING
DISTILLATION
OTHER
```

Required fields:

```yaml
optimization_id:
model_lineage:
optimization_family:
input_data:
preference_sources:
aggregation_method:
disagreement_treatment:
objective:
constraints:
provider_role:
evaluation:
known_biases:
status:
```

## 9.1 Rules

- Optimization family MUST be declared.
- Preference sources MUST preserve lineage.
- Aggregation MUST not be represented as direct public legitimacy.
- Disagreement treatment MUST remain visible.
- AI-generated feedback MUST remain distinct from human judgment.
- Provider objectives and constraints MUST remain visible.
- Objective optimization MUST not imply authority over affected centers.
- A high reward score MUST not become consent.

---

# 10. Synthetic-data ancestry

A `SyntheticDataAncestryRecord` records the sources and models from which synthetic data derives.

Required fields:

```yaml
ancestry_id:
synthetic_dataset:
generating_models:
prompt_or_generation_process:
ancestor_sources:
ancestor_authority:
ancestor_restrictions:
transformations:
filtering:
contamination_risks:
recursive_depth:
withdrawal_links:
status:
```

## 10.1 Rules

- Synthetic data MUST preserve material ancestry.
- Synthetic generation MUST not erase source restrictions automatically.
- A model output MUST not be treated as source-free.
- Recursive training depth SHOULD remain visible.
- Model-generated data SHOULD preserve provider and model lineage.
- Synthetic-data use MUST remain separately authorized.
- Unknown ancestry MUST remain visible.
- Withdrawal and correction SHOULD propagate where ancestry is material and technically reachable.

## 10.2 Governing distinction

> **Synthetic does not mean unowned, unbiased, source-free, or consent-free.**

---

# 11. Withdrawal and unlearning

A `WithdrawalUnlearningRecord` records what a withdrawal request can and cannot change.

Candidate actions:

```text
STOP_NEW_COLLECTION
DELETE_SOURCE_COPY
BLOCK_FUTURE_TRAINING
BLOCK_RUNTIME_RETRIEVAL
RESTRICT_RELEASE
APPLY_APPROXIMATE_UNLEARNING
VERIFY_UNLEARNING
RETRAIN_WITHOUT_SOURCE
RETIRE_MODEL
REPLACE_MODEL
OTHER
```

Required fields:

```yaml
record_id:
source_or_contributor:
lineage_scope:
withdrawal_basis:
requested_actions:
approved_actions:
technical_capability:
performed_actions:
verification:
known_residuals:
unreachable_descendants:
surviving_witness:
status:
```

## 11.1 Rules

- Withdrawal is a governance request over future use.
- Source deletion MUST remain distinct from model unlearning.
- Approximate unlearning MUST be labeled as approximate.
- Verification MUST identify the declared test.
- Complete forgetting MUST not be promised beyond evidence.
- Known residuals and unreachable descendants MUST remain visible.
- Retraining MAY be required where other methods are insufficient.
- A narrow withdrawal witness MAY remain without preserving the withdrawn content.
- Withdrawal from one transition MUST not be generalized beyond scope.

## 11.2 Governing distinction

> **Withdrawal is a governance right. Complete model unlearning is a technical capability that must not be promised beyond evidence.**

---

# 12. Derivative correction and restriction propagation

A `DerivativeCorrectionPropagation` records how corrections, restrictions, and withdrawal conditions travel into derivative datasets and models.

Required fields:

```yaml
propagation_id:
source_change:
origin_record:
affected_datasets:
affected_models:
affected_deployments:
propagation_rules:
performed_changes:
unreachable_descendants:
verification:
residual_risk:
status:
```

## 12.1 Rules

- Corrections MUST identify affected descendants.
- Restrictions MUST remain attached through dataset and model derivation where applicable.
- A derivative model MUST not erase lineage merely because weights have changed.
- Runtime correction and training correction MUST remain distinguishable.
- Unknown derivative copies MUST remain visible as lineage debt.
- Successor models MUST inherit unresolved obligations.
- Model retirement MUST not erase repair obligations.
- Propagation MUST preserve valid historical witness.

---

# 13. Benefit sharing and contributor recognition

A `BenefitContributorRecognitionRecord` records how value returned from the model lineage relates to recruited contributions.

Required fields:

```yaml
record_id:
model_lineage:
contributors_or_communities:
contribution_classes:
benefit_claim:
benefit_mechanisms:
recognition:
governance:
distribution_rules:
nonfinancial_benefits:
limitations:
review:
status:
```

Candidate benefit mechanisms:

```text
PAYMENT
ROYALTY
PUBLIC_ACCESS
COMMUNITY_LICENSE
SERVICE_RETURN
INFRASTRUCTURE
RESEARCH_RETURN
GOVERNANCE_RIGHT
ATTRIBUTION
REPAIR_FUND
PUBLIC_INTEREST_RELEASE
OTHER
```

## 13.1 Rules

- A vague claim that innovation benefits everyone MUST not count as benefit sharing.
- Benefit mechanisms MUST be concrete enough to review.
- Payment MUST not be treated as unlimited transfer of future standing.
- Attribution MAY be required but insufficient.
- Communities MUST not be reduced to individual contributor lists where collective standing matters.
- Benefits SHOULD reflect contribution class, burden, risk, and governance.
- Public-interest claims MUST remain evidence-bearing.
- Recognition MUST not expose contributors to unwanted identification.

## 13.2 Governing distinction

> **A vague promise that innovation benefits everyone is not a benefit-sharing mechanism.**

---

# 14. Consentful-training witness

A `ConsentfulTrainingWitness` records the governed lineage of a model.

Required fields:

```yaml
witness_id:
model_lineage:
source_standing_records:
collection_authorizations:
authority_consent_profiles:
transformation_lineages:
annotation_preference_records:
constitution_lineages:
optimization_records:
synthetic_ancestry:
withdrawal_unlearning_records:
derivative_propagations:
benefit_records:
unknowns:
contests:
event_ids:
completeness:
generated_from_events:
generated_at:
```

## 14.1 Rules

- The witness MUST preserve source standing.
- It MUST preserve transition-specific authority.
- It MUST distinguish license, lawful basis, consent, and legitimacy.
- It MUST preserve transformation lineage.
- It MUST preserve human and model preference sources.
- It MUST preserve constitution authority.
- It MUST preserve synthetic ancestry.
- It MUST preserve withdrawal capability and residuals.
- It MUST preserve derivative obligations.
- It MUST preserve benefit and accountability claims.
- Completeness MUST remain scoped.
- The witness MUST NOT label the model simply `CONSENTFUL` without a qualified profile.

Candidate lineage classifications:

```text
CONSENT_AUTHORIZED
COMMUNITY_AUTHORIZED
LICENSED_AND_PROVENANCE_AUDITED
PUBLIC_MANDATE_GOVERNED
MIXED_AUTHORITY
MATERIALLY_UNKNOWN
CONTESTED_LINEAGE
NONCONSENSUAL_OR_UNAUTHORIZED
```

---

# 15. Consentful-training governance gate

The minimum gate dimensions are:

```text
source_standing
collection_authority
training_authority
purpose_compatibility
license_scope
consent_scope
transformation_lineage
restriction_propagation
annotation_labor
preference_governance
constitution_authority
synthetic_ancestry
withdrawal_truthfulness
derivative_obligations
benefit_and_accountability
```

Candidate results:

```text
PASS
PASS_WITH_CONDITIONS
ADD_PROVENANCE
ADD_AUTHORITY
RESTRICT_SOURCE
QUARANTINE_DATASET
STOP_TRAINING
BLOCK_RELEASE
RETRAIN
RETIRE_MODEL
REPAIR
FAIL
UNKNOWN
CONTESTED
```

## 15.1 Composition rules

- Public availability MUST not create training authority.
- Missing source standing SHOULD block high-risk use.
- License scope mismatch MUST block the affected transition.
- Consent scope mismatch MUST block the affected transition.
- Restriction loss MUST trigger quarantine or repair.
- Preference disagreement MUST remain visible.
- Unknown constitution authority MUST remain disclosed.
- Synthetic ancestry unknowns MUST remain visible.
- Withdrawal claims MUST match technical evidence.
- Derivative models with unresolved restrictions SHOULD not be released without review.
- Human approval at deployment MUST not retroactively purify extraction in training.

---

# 16. Negative conformance cases

A conforming implementation MUST reject or flag:

## NC-1 — Public availability as consent

A publicly accessible source is treated as consented for training.

## NC-2 — License as consent

A license or contract is represented as the source center's consent.

## NC-3 — One grant authorizes every transition

Collection authority is treated as authorization for training, release, deployment, and retraining.

## NC-4 — Individual authorizes collective knowledge

An individual grants use of community-held knowledge without community authority.

## NC-5 — Annotation as universal preference

A bounded ranking task is represented as humanity's preference.

## NC-6 — Constitution without authority

Provider principles are represented as a legitimate public constitution without lineage or adoption.

## NC-7 — Synthetic data as source-free

Synthetic output is treated as having no relevant ancestry.

## NC-8 — Source deletion as unlearning

Deleting the source file is represented as proof that the model forgot it.

## NC-9 — Approximate unlearning as complete removal

A bounded unlearning method is described as complete forgetting.

## NC-10 — Derivative model obligation loss

A correction or restriction stops at the first model and does not propagate to known derivatives.

## NC-11 — Payment as unlimited consent

Contributor payment is represented as authorization for every future use.

## NC-12 — Deployment laundering

Consentful runtime use is represented as retroactively making unconsented training legitimate.

---

# 17. Positive demonstrations

I.9 includes eight required demonstrations.

## PD-1 — Public source remains distinct from authorized training source

A public article is technically accessible but lacks a valid training authority record and is blocked from the candidate dataset.

## PD-2 — Publication does not authorize deployment

An author licenses research training but not commercial deployment; the deployment transition remains blocked.

## PD-3 — Preference data retains conditional provenance

Annotator rankings preserve task framing, disagreement, contributor role, and downstream limits.

## PD-4 — Constitution authority remains visible

Provider principles and participant-adopted rules remain distinct in the constitution lineage.

## PD-5 — Synthetic ancestry survives transformation

A generated dataset preserves model, prompt, ancestor-source, and restriction lineage.

## PD-6 — Withdrawal produces bounded unlearning

A contributor withdraws future use; collection and retrieval stop, approximate unlearning occurs, verification and residuals remain declared.

## PD-7 — Derivative models receive correction and restriction

A source correction propagates into the training dataset, base model profile, derivative model, and runtime retrieval policy.

## PD-8 — Benefit claim remains connected to contribution

A community dataset receives a governed return mechanism rather than an unqualified public-benefit claim.

---

# 18. Conformance additions

I.9 adds the following P2/P3 requirements:

- source and dataset standing;
- collection authorization;
- transition-specific authority, consent, and license scope;
- transformation lineage;
- annotation and preference provenance;
- constitution lineage;
- optimization lineage;
- synthetic ancestry;
- withdrawal and unlearning truthfulness;
- derivative correction propagation;
- benefit-sharing and recognition;
- consentful-training witness.

P3 additionally requires:

- participant and community challenge to standing records;
- external provenance audit;
- transition-level restriction tests;
- annotator disagreement preservation;
- synthetic ancestry verification;
- unlearning evidence review;
- derivative-model propagation audit;
- provider-independent witness export.

---

# 19. Security and governance considerations

Training lineages can be manipulated through:

- provenance laundering;
- public-data overclaim;
- license overbreadth;
- community-standing erasure;
- transformation opacity;
- annotator invisibility;
- preference universalization;
- constitution laundering;
- synthetic ancestry loss;
- unlearning overclaim;
- derivative lineage breaks;
- benefit-washing;
- deployment laundering.

Implementations SHOULD:

- preserve source-class and standing;
- require transition-specific authority;
- separate consent from other legal bases;
- preserve restrictions during transformation;
- retain task and labor provenance;
- expose preference disagreement;
- record constitution authority;
- track synthetic ancestry;
- report unlearning residuals;
- propagate corrections and restrictions;
- make benefit mechanisms reviewable;
- export a provider-independent training witness.

---

# 20. I.9 non-claims

I.9 does not claim:

- all model training requires individual opt-in;
- every public source requires the same governance;
- every lawful use is legitimate;
- every licensed use is consented;
- every consented use is legitimate in every context;
- every source can be perfectly attributed;
- every derivative model can be fully reached;
- every withdrawal can produce exact unlearning;
- every community has one representative authority;
- payment creates consent;
- open models are inherently consentful;
- closed models are inherently safer.

---

# 21. I.9 completion criterion

I.9 passes when:

1. the eight positive demonstrations validate;
2. the twelve negative cases are detected;
3. source standing remains distinct from accessibility;
4. authority remains transition-specific;
5. license, legal basis, consent, and legitimacy remain distinct;
6. preference data retains conditional provenance;
7. constitution authority remains visible;
8. synthetic ancestry remains attached;
9. withdrawal claims match technical evidence;
10. derivative obligations propagate;
11. benefit claims remain concrete and reviewable;
12. H.9 explains consentful training without presenting it as binary purity or retroactive purification.
