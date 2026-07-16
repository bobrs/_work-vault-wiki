---
title: "Training Data, Preference Aggregation, Constitution, and Model Governance"
subtitle: "Consent, Licensing, Documentation, RLHF, Unlearning, Synthetic Data, Collective Authority, and Benefit"
artifact_date: "2026-07-15"
artifact_type: "adjacent-fields-and-training-governance-review"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "draft"
processing_tier: 4
source_role: "research-and-claim-boundary-artifact"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "G.12"
companion_to:
  - "20260715__TELIC-FIELDS__PAPER__CANDIDATE__F-11__consentfully-trained-models.md"
research_note: >
  This is an interdisciplinary governance review rather than a legal opinion or
  systematic review. Copyright, privacy, data protection, research ethics,
  employment, consumer protection, and Indigenous governance vary by
  jurisdiction and community. Legal claims must be reviewed before
  implementation.
---

# Training Data, Preference Aggregation, Constitution, and Model Governance

## Executive finding

F.11 is viable if **consentfully trained** remains a qualified, auditable governance profile rather than a universal binary label.

The adjacent fields already establish most of the component mechanisms:

- informed consent and research ethics distinguish permission from mere access and require attention to risk, voluntariness, purpose, and vulnerable populations;
- data protection law distinguishes lawful bases, purpose limitation, data minimization, accuracy, retention, and erasure;
- copyright, contract, license, public domain, and statutory exceptions govern some—but not all—source interests;
- Datasheets for Datasets, Data Statements, Dataset Nutrition Labels, model cards, and system cards document portions of the development lifecycle;
- data-provenance research shows that licensing and attribution metadata are frequently missing or incorrect in widely used datasets;
- RLHF, DPO, RLAIF, and Constitutional AI provide distinct technical mechanisms for shaping model behavior from demonstrations, comparisons, learned rewards, direct preference optimization, AI feedback, and principles;
- social-choice and preference-learning research already show that aggregation does not discover one universal human preference;
- machine-unlearning research distinguishes exact and approximate approaches and increasingly emphasizes verification, retained utility, privacy leakage, and sequential requests;
- synthetic-data research identifies both useful augmentation regimes and recursive model-collapse risks;
- data trusts, cooperatives, commons, CARE, OCAP, and related community-governance structures provide alternatives to atomized individual consent;
- benefit sharing and collective authority are established concerns in research ethics, Indigenous governance, health, genetics, and public data systems.

The Telic Field Papers should not claim to discover any of these.

The candidate contribution is the composition:

> **A consentful training lineage records the authority under which source data, human labor, preference judgments, constitutions, transformations, and benefits are recruited into a model; keeps disagreement, restrictions, withdrawal limits, and succession obligations attached through the pipeline; and evaluates training separately from deployment.**

The strongest additions are:

1. training as outer-loop recruitment;
2. source standing beyond individual data subjects;
3. transition-specific authority through the full training chain;
4. restriction and obligation propagation into derivative models;
5. explicit preference-plurality status;
6. truthful separation of source deletion, future exclusion, unlearning, and retraining;
7. benefit and community governance as first-class lineage fields;
8. synthetic-data lineage and recursive semantic-risk controls;
9. training and operation profiles kept separate;
10. model succession carrying restrictions and duties.

The principal risk is ethical laundering.

A model with incomplete, disputed, or mixed-authority sources should not receive a simple *consentfully trained* badge.

---

# 1. Review questions

G.12 asks:

- When is consent the appropriate authority for training?
- Which other authority bases may legitimately govern sources?
- How do copyright, license, privacy, and consent differ?
- What do dataset-documentation standards preserve?
- How often do provenance and license records fail in practice?
- How do RLHF, DPO, RLAIF, and Constitutional AI differ technically and constitutionally?
- How are evaluator preferences aggregated?
- What happens to disagreement?
- What can deletion and machine unlearning actually promise?
- How should opt-out signals propagate?
- When does synthetic data preserve, obscure, or recursively degrade source fields?
- How can data trusts, cooperatives, and community governance improve authority?
- What does Indigenous data sovereignty require beyond individual consent?
- How should benefit and obligations pass into derivative and successor models?
- What remains distinctive in consentful training lineage?

---

# 2. Informed consent and research ethics

Research ethics treats consent as a process rather than a box.

Core concerns include:

- information;
- comprehension;
- voluntariness;
- capacity;
- risk;
- benefit;
- vulnerable populations;
- continuing participation;
- withdrawal;
- institutional review.

Large-scale model training challenges conventional consent because:

- the future model and uses may be unknown;
- data may be repurposed;
- models may be widely released;
- individual influence is difficult to trace;
- collective effects may exceed individual risk;
- complete unlearning may not be available.

## Adjudication

**Research consent is a strong design precedent and not a universal authority for all model training.**

Public records, public-domain works, licensed materials, and lawful statistical processing may rely on other bases.

Where research consent is used, broad future-use language should not be treated as unlimited authority.

## Continuing consent

Long-lived training programs may need:

- periodic notice;
- changed-purpose review;
- community oversight;
- withdrawal update;
- new-risk communication.

One initial signature may not carry the entire model lifecycle.

---

# 3. Data protection

The GDPR provides a useful official reference point for several principles:

- lawfulness, fairness, and transparency;
- purpose limitation;
- data minimization;
- accuracy;
- storage limitation;
- integrity and confidentiality;
- accountability;
- rights including erasure under specified conditions.

Consent is one lawful basis among others.

It must not be used where it is not freely given or where another basis is actually relied upon.

## Strong overlap

- purpose;
- minimization;
- retention;
- transparency;
- accuracy;
- rights;
- controller responsibility;
- downstream processing.

## Important boundary

The right to erasure is not absolute.

Nor does erasure from a source system automatically prove removal from a trained model.

## Adjudication

**F.11 should preserve legal-basis terminology rather than call all lawful processing consentful.**

The broader architectural term should be **training authority**, with consent as one authority class.

---

# 4. Purpose limitation and data minimization

Purpose limitation asks whether data is collected and processed for specified, explicit, legitimate purposes and whether later use remains compatible.

Data minimization asks whether processing is adequate, relevant, and limited to what is necessary.

These principles conflict with common foundation-model practices that favor:

- maximal collection;
- open-ended capability;
- indefinite retention;
- later repurposing.

Technical research argues that data-driven systems can often operate with less data than they collect, while identifying real implementation tradeoffs.

## Adjudication

**The training-purpose record must be more specific than “improve models.”**

Purpose should be expressed through:

- model class;
- capability;
- release regime;
- domains;
- foreseeable restrictions;
- derivative use;
- review.

## Boundary

A foundation model's generality makes narrow ex ante purpose difficult.

That difficulty should be disclosed as a governance limitation, not converted into unrestricted purpose.

---

# 5. Copyright, license, and public access

Copyright governs protected expression.

Licenses grant specified permissions.

Public domain removes some exclusive copyright constraints.

Public accessibility merely means that content can be reached.

These states do not collapse.

## Adjudication

A training-lineage record should preserve:

```text
copyright_status
license
jurisdiction
access_method
contractual_terms
text_and_data_mining_status
dispute
attribution
```

## Boundary

The law of generative-AI training remains contested and jurisdiction-specific.

F.11 appropriately refuses a universal conclusion.

## Governance beyond copyright

Even lawful copyright use may raise:

- privacy;
- confidentiality;
- collective authority;
- attribution;
- labor;
- cultural harm;
- benefit;
- purpose.

Copyright compliance is one layer.

It is not the whole field.

---

# 6. Public data

Open government and scientific data can support public benefit.

The term *public data* is dangerously ambiguous.

It may mean:

- publicly accessible;
- publicly owned;
- public-domain;
- openly licensed;
- government-held;
- published under legal duty;
- available for one public purpose.

## Adjudication

**Public must always be qualified.**

A model should record whether data is:

```text
PUBLICLY ACCESSIBLE
PUBLIC DOMAIN
OPEN LICENSED
GOVERNMENT RECORD
PUBLIC-MANDATE RESEARCH
RESTRICTED PUBLIC ACCESS
```

A public record can still contain personal or collective risk.

---

# 7. Datasheets for Datasets

Datasheets for Datasets propose standardized documentation of:

- motivation;
- composition;
- collection;
- preprocessing;
- uses;
- distribution;
- maintenance.

The contribution is foundational because it treats dataset creation as an accountable engineering activity rather than an invisible precursor.

## Strong overlap

- provenance;
- purpose;
- composition;
- collection;
- use;
- maintenance;
- limitations.

## Candidate addition

A consentful training lineage adds executable and lifecycle fields for:

- authority;
- consent;
- collective governance;
- restriction propagation;
- withdrawal;
- benefit;
- derivative models;
- disputes.

## Adjudication

**Extend datasheets rather than replace them.**

---

# 8. Data Statements

Data Statements for NLP emphasize the need to document the social and demographic characteristics of language data so that system limitations, bias, and generalizability are more visible.

## Strong overlap

- language community;
- speaker population;
- context;
- representativeness;
- bias;
- scientific validity.

## Candidate addition

Consentful lineage asks:

- who authorized collection;
- whether community authority applies;
- whether public release was within scope;
- how future models may use the language resource;
- what benefit returns.

## Adjudication

**Data Statements are a key precursor for source-community representation.**

Documentation of demographics does not itself confer authority.

---

# 9. Dataset Nutrition Labels

Dataset Nutrition Labels offer modular contextual and diagnostic information intended to support data selection and risk recognition.

## Strong overlap

- standardized summary;
- context;
- alerts;
- quality;
- bias;
- intended use.

## Candidate addition

The lineage record connects a label to:

- actual training events;
- restriction enforcement;
- derivative models;
- withdrawal and correction.

## Adjudication

Labels should not become static compliance badges.

They need versions, provenance, and operational links.

---

# 10. Provenance in practice

The Data Provenance Initiative audited more than 1,800 text datasets and reported major gaps in licensing and attribution metadata, including frequent omission and miscategorization.

## Strong overlap

- source lineage;
- license;
- dataset parentage;
- attribution;
- audit;
- legal and ethical uncertainty.

## Adjudication

**Provenance coverage must be measured, not merely asserted.**

Candidate coverage metrics include:

- source-known percentage;
- license-known percentage;
- authority-known percentage;
- restrictions-propagated percentage;
- disputed-source percentage;
- derivative-lineage completeness.

## Boundary

Complete provenance does not establish lawful or legitimate use.

It makes the claim testable.

---

# 11. Archives and sociocultural collection

Archival scholarship has long addressed:

- consent;
- selection;
- power;
- inclusion;
- privacy;
- context;
- description;
- stewardship.

Research applying archival lessons to machine-learning data collection emphasizes that collection and annotation require institutional methods, not only technical pipelines.

## Adjudication

**Training-data governance should incorporate archival expertise.**

Especially important are:

- collection context;
- silences;
- community stewardship;
- access restrictions;
- descriptive power;
- deletion and retention.

---

# 12. RLHF

InstructGPT is a canonical RLHF example.

Its pipeline includes:

- labeler demonstrations;
- rankings of model outputs;
- reward-model training;
- reinforcement learning against the learned reward.

The resulting model was preferred over the larger base GPT-3 in the reported prompt distribution and evaluation.

## Governance significance

RLHF converts bounded human judgments into a training signal that shapes broad model behavior.

The judgment population, task distribution, policy, and aggregation rule matter.

## Adjudication

**RLHF should be described as alignment to a feedback process—not direct alignment to humanity.**

The preference model is a receiver mirror of evaluator judgments.

---

# 13. DPO

DPO reformulates standard preference optimization so a language model can be optimized directly from preferred and rejected responses using a classification-style objective.

It avoids a separately trained explicit reward model and RL loop in the standard pipeline.

## Governance significance

DPO simplifies optimization.

It does not remove:

- evaluator selection;
- task framing;
- preference conflict;
- policy;
- reference-model effects;
- source authority.

## Adjudication

**Simpler optimization is not simpler legitimacy.**

A DPO dataset needs the same preference provenance as RLHF data.

---

# 14. RLAIF and Constitutional AI

Constitutional AI combines:

- explicit human-written principles;
- model-generated critique and revision;
- AI-generated preferences;
- reinforcement learning from AI feedback.

Its important governance innovation is that principles become a visible object of training.

## Boundary

The method does not answer:

- whether the principles are legitimate;
- who is represented;
- who may revise them;
- how conflicts are adjudicated;
- how deployment is governed.

## Adjudication

**Use Constitutional AI as a technical method and model constitutions as the broader governance object.**

The constitution should carry provenance, authority, revision, dissent, and protected-standing fields.

---

# 15. Preference aggregation

Preference models often assume that pairwise choices can be summarized into a latent reward or ordering.

This is useful and lossy.

Preferences may vary by:

- culture;
- task;
- role;
- risk;
- language;
- demographic;
- policy;
- time;
- framing;
- alternatives shown.

## Strong overlap with social choice

Aggregation rules select among conflicting judgments.

No method is neutral.

## Adjudication

A preference-training record should preserve:

```text
population
sampling
task
policy
choice set
aggregation rule
disagreement
protected objection
adjudication
known missing groups
```

## Boundary

A reward model should never be described as *the human reward function*.

---

# 16. Annotator disagreement

Disagreement can indicate:

- ambiguity;
- error;
- cultural difference;
- value conflict;
- task confusion;
- poor instruction;
- legitimate plurality.

Common pipelines collapse disagreement into a majority label or adjudicated ground truth.

## Adjudication

**Disagreement is training data about the field.**

Candidate treatments include:

- distributional labels;
- subgroup models;
- uncertainty;
- multiple policies;
- abstention;
- protected exceptions;
- human escalation.

Not every disagreement should be preserved forever.

Material disagreement should not disappear silently.

---

# 17. Human labor and conditions

Annotation and moderation work can expose people to:

- disturbing content;
- repetitive cognitive strain;
- low pay;
- opaque evaluation;
- surveillance;
- non-disclosure constraints;
- downstream consequences they do not understand.

## Adjudication

**Labor conditions belong inside model lineage.**

A model should not receive a consentful-training classification when critical human contribution was recruited under materially coercive or unsafe conditions.

## Boundary

Employment consent can be structurally constrained.

A signed task agreement may not establish meaningful voluntariness.

---

# 18. Machine unlearning

Machine unlearning aims to remove specified training influence.

The literature distinguishes:

- exact;
- approximate;
- centralized;
- federated;
- graph;
- verification;
- privacy and security concerns.

For modern language models, exact retraining without specified data is often expensive.

Approximate methods trade removal, utility, scale, and verification.

## Adjudication

**Unlearning status must be granular.**

Use:

```text
SOURCE_DELETED
FUTURE_TRAINING_BLOCKED
OUTPUT_SUPPRESSED
APPROXIMATE_UNLEARNING
RETRAINED_WITHOUT_SOURCE
VERIFICATION_PASSED
VERIFICATION_FAILED
RESIDUAL_UNKNOWN
```

Do not use one word—*deleted*—for all states.

---

# 19. Unlearning evaluation

MUSE evaluates six desirable properties:

- no verbatim memorization;
- no knowledge memorization;
- no privacy leakage;
- retained utility;
- scalability;
- sustainability under sequential requests.

Its reported experiments found serious limitations among tested methods, including privacy and utility concerns.

Other research argues that common unlearning benchmarks can overstate progress and may be vulnerable to benign modifications and target ambiguity.

OpenUnlearning provides a unified evaluation framework spanning methods, metrics, and checkpoints.

## Adjudication

**Unlearning claims require benchmark and threat-model disclosure.**

No finite benchmark proves complete absence of influence.

## Governance implication

A withdrawal right should remain valid even where technical removal is incomplete.

The remedy may include retraining, restriction, compensation, or model retirement.

---

# 20. Opt-out and machine-readable restrictions

Robots Exclusion Protocol communicates crawler access preferences.

It was not designed as a complete licensing or training-consent language.

Recent proposals such as `ai.txt` and decentralized consent registries explore finer-grained AI-use signaling.

## Strong overlap

- machine-readable refusal;
- domain or item scope;
- crawler control;
- training-use expression;
- provenance and reward.

## Boundary

Technical signals face:

- voluntary compliance;
- identity of crawlers;
- fragmented syntax;
- copied data;
- archives;
- downstream datasets;
- prior collection;
- legal uncertainty.

## Adjudication

**Opt-out signals should propagate as provenance-bearing restrictions, not be discarded after collection.**

Their absence should not automatically be called consent.

---

# 21. Synthetic data

Synthetic data can support:

- privacy;
- rare cases;
- balancing;
- simulation;
- instruction generation;
- self-improvement.

Its risks include:

- hidden source memorization;
- provenance loss;
- error amplification;
- circular evaluation;
- policy monoculture;
- source displacement.

## Adjudication

Synthetic data should carry:

```text
generating_model
model_version
source lineage
prompt or constitution
filters
real-person relation
intended use
contamination tests
```

Synthetic status does not erase source obligations.

---

# 22. Model collapse

Research on recursive training shows that replacing real data with recursively generated synthetic data can degrade models and lose distributional tails in studied regimes.

Other work finds that retaining and accumulating original real data alongside synthetic data can avoid collapse in studied settings.

## Adjudication

**Avoid the universal claim that synthetic data inevitably causes collapse.**

Use:

> Recursive synthetic replacement can cause model collapse; outcomes depend on data regime and retention of real data.

## Telic extension

Distributional tail loss is also a standing problem.

Rare language and minority expression can disappear before average performance reveals the harm.

---

# 23. Data trusts

Data trusts are used inconsistently in practice.

A practical health-data review identified minimum requirements including:

- legal authority;
- accountable governance;
- transparent purpose;
- comprehensive data management;
- training and accountability;
- ongoing public and stakeholder engagement.

## Adjudication

**Data trust is a governance structure, not a trustworthiness label.**

A trust should state:

- legal form;
- beneficiary;
- trustee or steward duties;
- authority;
- purpose;
- access;
- audit;
- exit;
- enforcement.

---

# 24. Data cooperatives

Data cooperatives emphasize member ownership or control, democratic governance, economic participation, and community benefit.

They may offer stronger participant authority than one-time consent.

They also face:

- participation burden;
- collective-action cost;
- scale;
- technical complexity;
- internal disagreement;
- capture.

## Adjudication

**Data cooperatives are plausible training-data governors, not automatic solutions.**

Their legitimacy depends on actual member power and protection of internal minorities.

---

# 25. Commons

Knowledge and data commons use collective rules to govern shared resources.

AI-relevant commons may include:

- data;
- models;
- compute;
- evaluation;
- ontologies;
- energy;
- public infrastructure.

## Boundary

Open access is not sufficient.

Commons governance requires:

- contribution rules;
- maintenance;
- monitoring;
- conflict resolution;
- authority;
- benefit;
- succession.

## Adjudication

A public or commons model should document its governance architecture as carefully as a commercial model documents ownership.

---

# 26. Indigenous data governance

The CARE Principles center:

- Collective Benefit;
- Authority to Control;
- Responsibility;
- Ethics.

OCAP centers:

- Ownership;
- Control;
- Access;
- Possession.

These frameworks respond to histories of extraction, misrepresentation, and government or institutional control over Indigenous data.

## Adjudication

**Indigenous data is not simply an underrepresented dataset awaiting inclusion.**

A community may:

- govern access;
- require collective benefit;
- restrict reuse;
- require local possession;
- refuse AI training.

## Hard boundary

The framework must not universalize one Indigenous governance model across distinct peoples.

Community-specific authority governs.

---

# 27. Benefit sharing

Benefit sharing appears in:

- research ethics;
- genetics;
- biodiversity;
- public health;
- Indigenous governance;
- platform and data-governance proposals.

Potential benefits include:

- payment;
- royalties;
- shared infrastructure;
- model access;
- research findings;
- public service;
- governance rights;
- capacity building;
- community funds.

## Adjudication

**Benefit sharing should be linked to contribution, risk, power, and governance—not used to purchase blanket consent.**

A payment does not cure a prohibited use.

A public model does not automatically distribute benefit fairly.

---

# 28. Data provenance as governance lever

Recent frontier-model governance proposals treat data not only as a harm source but as a lever for:

- monitoring;
- dataset reporting;
- security;
- filtering;
- vendor accountability;
- detection of unauthorized use.

## Adjudication

F.11's lineage record aligns with this direction.

It adds:

- standing;
- consent;
- community authority;
- benefit;
- succession;
- deployment separation.

## Boundary

Provenance systems can become surveillance infrastructure.

They need minimization and access control.



# 29. Comparison matrix

| Neighboring field or method | Existing contribution | Candidate consentful-training addition |
|---|---|---|
| Research ethics | Information, voluntariness, risk, continuing participation, withdrawal | Full model-lifecycle and derivative-use lineage |
| Data protection | Lawful basis, purpose limitation, minimization, accuracy, retention, rights | Training and operational authority profiles kept separate |
| Copyright and licensing | Rights, permissions, exceptions, attribution | Standing, privacy, collective authority, benefit, succession |
| Datasheets | Dataset motivation, composition, collection, use, maintenance | Executable restrictions, authority, withdrawal, derivative lineage |
| Data Statements | Language-community and demographic context | Community authority, benefit, refusal, and future-use governance |
| Dataset Nutrition Labels | Modular context and risk alerts | Versioned connection to actual training and model descendants |
| Data provenance | Source, license, parentage, attribution | Consent, standing, community authority, benefit, and restrictions |
| RLHF | Human demonstrations, preferences, reward modeling, policy optimization | Evaluator population, disagreement, policy authority, protected objections |
| DPO | Direct optimization from preferred/rejected outputs | Same preference-governance requirements despite simpler optimization |
| RLAIF / Constitutional AI | AI feedback guided by explicit principles | Principle legitimacy, authorship, revision, conflict, represented standing |
| Machine unlearning | Exact/approximate removal and evaluation | Truthful withdrawal states, governance remedy, succession propagation |
| Opt-out signals | Machine-readable exclusion or use preferences | Persistent restriction propagation across data and models |
| Synthetic data | Augmentation, privacy, simulation, self-training | Generating-model lineage, source obligations, tail and diversity protection |
| Data trusts | Accountable stewardship and controlled sharing | Model-specific purpose, derivative use, withdrawal, and benefit |
| Data cooperatives | Democratic member governance and economic participation | Training and deployment authority under member control |
| Knowledge commons | Collective rules for shared resources | Consent, privacy, contribution, model release, and lifecycle |
| CARE / OCAP | Collective benefit, authority, responsibility, ethics, ownership, access, possession | AI-training lineage and derivative-model obligation |
| Benefit sharing | Return of value and capacity to contributors or communities | Model-specific value capture and continuing governance |
| Frontier data governance | Dataset reporting, monitoring, security, filtering, supply-chain controls | Standing-aware and consent-aware provenance |

---

# 30. Training authority taxonomy

The broader term **training authority** should be preferred over treating every basis as consent.

Candidate classes:

```text
INDIVIDUAL CONSENT
COLLECTIVE AUTHORITY
COMMUNITY GOVERNANCE
CONTRACT
LICENSE
PUBLIC DOMAIN
PUBLIC MANDATE
RESEARCH ETHICS AUTHORIZATION
FIDUCIARY STEWARDSHIP
STATUTORY AUTHORITY
OTHER LAWFUL BASIS
UNKNOWN
CONTESTED
EXPIRED
WITHDRAWN
```

Each record should include:

- source;
- jurisdiction;
- scope;
- purpose;
- duration;
- derivative use;
- release regime;
- restrictions;
- withdrawal;
- contest;
- verification.

## Adjudication

**Training authority: adopt.**

**Consentful training: retain as an umbrella only when the profile accurately distinguishes non-consent authority classes.**

---

# 31. Consentful-training classification

A binary label is not recommended.

Candidate classifications include:

## 31.1 Consent-authorized

Material source classes are governed through valid individual consent.

## 31.2 Community-authorized

Material sources are governed by a legitimate community authority.

## 31.3 Licensed and provenance-audited

Use is governed primarily by license or contract with strong source lineage.

## 31.4 Public-mandate governed

Training is supported by a public or research mandate with safeguards and accountability.

## 31.5 Mixed-authority

Several authority classes apply.

## 31.6 Materially unknown

Material source authority cannot be established.

## 31.7 Contested lineage

Important source classes or uses are disputed.

## 31.8 Nonconsensual or unauthorized

Use lacks the authority it claims or proceeds against a valid refusal.

## Adjudication

A model may use the phrase **consentfully trained** only with a visible profile such as:

> Mixed-authority training; high provenance coverage; licensed and public-domain core; community-governed specialized corpus; future-use withdrawal supported; complete model unlearning not guaranteed.

---

# 32. Training versus deployment matrix

| Training | Deployment | Governance interpretation |
|---|---|---|
| Strong | Strong | Best current profile; still requires ongoing review |
| Strong | Weak | Authorized sources deployed through illegitimate purpose or action |
| Weak | Strong | Better operation does not repair disputed recruitment |
| Weak | Weak | Both provenance and use require repair |
| Unknown | Strong | Deployment may be bounded, but training uncertainty remains material |
| Contested | Public-benefit claim | Public benefit cannot adjudicate source dispute by assertion |
| Community-authorized | Open weights | Release may exceed community authority |
| Licensed | New high-risk domain | License may not resolve privacy, standing, or domain legitimacy |

## Stable formulation

> **Good deployment does not erase extraction. Good provenance does not excuse harmful use.**

---

# 33. Restriction propagation

A restriction can be lost at each stage:

```text
source
→ crawler
→ archive
→ dataset
→ filtered corpus
→ fine-tuning set
→ checkpoint
→ model merge
→ derivative model
→ application
```

## Required properties

- persistent identifier;
- machine-readable restriction;
- source and authority;
- valid time;
- transformation compatibility;
- derivative-use rule;
- withdrawal state;
- audit.

## Adjudication

**Restriction propagation is a central Phase I requirement.**

It should be integrated with provenance and event sourcing rather than treated as dataset metadata alone.

## Boundary

Not every restriction is lawful, enforceable, or legitimate.

The system should preserve the claim and its status rather than silently accept or discard it.

---

# 34. Withdrawal ladder

The review supports a precise ladder:

```text
1. STOP NEW COLLECTION
2. DELETE SOURCE COPY
3. BLOCK FUTURE TRAINING
4. BLOCK RUNTIME RETRIEVAL
5. RESTRICT MODEL RELEASE OR USE
6. APPLY APPROXIMATE UNLEARNING
7. VERIFY AGAINST DECLARED TESTS
8. RETRAIN WITHOUT SOURCE
9. RETIRE OR REPLACE MODEL
```

Each level has different cost and effectiveness.

## Adjudication

**Withdrawal rights should name the supported rung.**

A developer should not imply rung 8 when it offers only rung 2.

---

# 35. Unlearning evidence classes

Candidate evidence classes:

## 35.1 Administrative

The source was removed from storage or an index.

## 35.2 Procedural

Future pipelines exclude the source.

## 35.3 Behavioral

Specified outputs or knowledge probes no longer recover target content.

## 35.4 Privacy

Membership or extraction tests show reduced leakage under a declared adversary.

## 35.5 Comparative

The result approaches a model retrained without the source.

## 35.6 Certified

A formal or architectural guarantee applies under stated assumptions.

## 35.7 Unknown

The model influence was not adequately tested.

## Adjudication

Use the strongest evidence class actually established.

Do not infer semantic erasure from behavioral suppression alone.

---

# 36. Synthetic-data governance

A synthetic-data record should include:

```yaml
generator:
generator_version:
source_lineage:
generation_policy:
prompt_distribution:
human_review:
filters:
real_person_relationship:
privacy_tests:
copyright_or_license_status:
synthetic_proportion:
deduplication:
tail_preservation:
minority_coverage:
evaluation_contamination:
recursive_generation_depth:
```

## Adjudication

**Synthetic data should be treated as derived data with inherited obligations.**

It is not a clean-room source merely because a model generated it.

## Model-collapse boundary

The evidence supports conditional claims.

Avoid:

> Training on synthetic data causes inevitable model collapse.

Prefer:

> Recursive replacement of real data with synthetic outputs can produce collapse and tail loss; mixed and accumulating real-data regimes can behave differently.

---

# 37. Preference-governance profile

A preference dataset should disclose:

```yaml
task_domain:
evaluator_population:
recruitment:
compensation:
instruction_policy:
alternatives_presented:
choice_format:
model_or_system_context:
demographic_and_cultural_coverage:
disagreement_distribution:
aggregation_rule:
adjudication:
protected_objections:
known_missing_standing:
intended_behavior_scope:
expiry_or_review:
```

## Adjudication

**Preference provenance is as important as data provenance.**

A model behavior claim such as *aligned with human preferences* is incomplete without this profile.

## Boundary

Some evaluator details may be private or create safety risk.

Disclosure can be aggregate while governance remains auditable.

---

# 38. Constitution-governance profile

A model constitution should disclose:

- principles;
- authorship;
- intended standing;
- interpretation method;
- ordering or conflict rules;
- evaluator or critique model;
- revision authority;
- public status;
- cultural and jurisdictional scope;
- contest route;
- known omissions.

## Adjudication

**Explicit principles improve governability but do not establish legitimacy.**

A constitution can be:

- public;
- private;
- community-governed;
- statutory;
- contractual;
- provider-selected;
- mixed.

The source of authority matters.

---

# 39. Community governance profile

A community-governed source should record:

```text
community identity
authority body
membership or constituency
decision process
dissent and minority protection
source categories
allowed uses
prohibited uses
benefit
access
possession or custody
withdrawal
successor authority
external complaint
```

## Adjudication

**Collective authority should not be inferred from a self-appointed intermediary.**

Evidence of legitimate representation is required.

## Boundary

Community-specific protocols may prohibit public disclosure of governance detail.

A bounded attestation may be more appropriate than full transparency.

---

# 40. Benefit profile

Candidate benefit classes:

```text
DIRECT PAYMENT
ROYALTY
ATTRIBUTION
COMMUNITY FUND
PUBLIC MODEL ACCESS
LOCAL INFRASTRUCTURE
CAPACITY BUILDING
RESEARCH RETURN
GOVERNANCE RIGHTS
PRIORITY SERVICE
NO MATERIAL BENEFIT
UNKNOWN
```

## Adjudication

Benefit should be assessed against:

- source contribution;
- risk;
- historical extraction;
- substitutability;
- value captured;
- community preference.

Benefit sharing is not equivalent to purchasing all future rights.

---

# 41. Model succession

Training lineage must survive:

- fine-tuning;
- distillation;
- merging;
- quantization;
- checkpoint conversion;
- provider acquisition;
- model sale;
- open-weight release;
- hosted derivative services.

## Required succession fields

- parent models;
- inherited datasets;
- inherited restrictions;
- inherited constitutions;
- unresolved disputes;
- unlearning obligations;
- benefit commitments;
- release changes;
- responsible successor.

## Adjudication

**Capability should not transfer without attached obligations.**

A successor claiming the model's benefit should inherit the governance burden that made the model possible.

---

# 42. Model dissolution

A model may need retirement because:

- authority expired;
- source dispute is unrepairable;
- unlearning is infeasible;
- security risk is unacceptable;
- constitution failed;
- successor model replaces it;
- purpose completed;
- provider dissolves.

Dissolution should address:

- endpoints;
- weights;
- copies;
- checkpoints;
- datasets;
- derived models;
- applications;
- user memory;
- claims;
- audit;
- aftercare.

## Adjudication

F.7's dissolution protocol should be applied to model lineage.

Turning off one API is not complete model dissolution.

---

# 43. Terminology adjudication

## Consentfully trained model

**Decision:** retain provisionally as a qualified governance classification.

**Boundary:** profile, not binary moral badge.

## Training recruitment

**Decision:** retain.

**Boundary:** semantic and material contribution into an outer loop.

## Training authority

**Decision:** adopt as the broader technical term.

## Source standing

**Decision:** retain.

## Preference provenance

**Decision:** adopt.

## Preference universalization breach

**Decision:** retain.

## Constitution authority

**Decision:** retain.

## Restriction propagation

**Decision:** adopt.

## Withdrawal ladder

**Decision:** adopt.

## Unlearning verification

**Decision:** use established terminology.

## Synthetic-data lineage

**Decision:** adopt.

## Recursive semantic pollution

**Decision:** retain as an explanatory phrase, not a standardized technical term.

## Benefit governance

**Decision:** adopt.

## Training/operation separation

**Decision:** adopt as a foundational invariant.

## Consentful provenance in; consentful interpretation out

**Decision:** retain as a governing formulation.

---

# 44. Claim adjudication

## May be stated strongly

- Technical access is not identical to permission or consent.
- Consent is one lawful or ethical authority mechanism among several.
- Dataset documentation is established but often incomplete.
- Dataset license and attribution metadata can be missing or incorrect.
- RLHF uses bounded human demonstrations or preferences to shape model behavior.
- DPO simplifies preference optimization but retains preference-data governance questions.
- Constitutional AI uses explicit principles and AI feedback to shape behavior.
- Preference aggregation can erase disagreement.
- Machine unlearning includes exact and approximate methods and remains difficult to verify for LLMs.
- Synthetic-data outcomes depend on the recursive and mixed-data regime.
- Collective and Indigenous data-governance frameworks preserve interests that individual consent may not represent.
- Model and dataset restrictions can be lost through derivative pipelines.

## May be stated as a proposed synthesis

- Training should be modeled as outer-loop recruitment.
- Source standing should extend beyond conventional individual data subjects.
- Training authority should be recorded at each transition.
- Consentful training should be a profile rather than a badge.
- Preference provenance should accompany preference-trained models.
- Withdrawal should be represented as a ladder of distinct capabilities.
- Synthetic data should inherit source and model obligations.
- Benefit governance should be part of model lineage.
- Training and operation should receive separate consentfulness profiles.
- Model succession should carry restrictions and duties.

## Must remain hypotheses

- Consentful-lineage records improve source and community trust.
- Restriction propagation can scale to web-scale training.
- Preference-plurality records improve model behavior.
- Community-governed training improves representation without creating new capture.
- Benefit governance is administratively feasible at foundation-model scale.
- Withdrawal profiles change contribution decisions meaningfully.
- Synthetic-data lineage reduces collapse, pollution, or legal risk.
- The term *consentfully trained* can resist marketing dilution.

## Should not be claimed

- Every training source requires individual opt-in consent.
- Public data is ownerless.
- Legal permission proves ethical legitimacy.
- Datasheets prove compliance.
- RLHF represents humanity.
- DPO removes value judgment.
- Constitutional AI creates a legitimate constitution.
- Source deletion proves model forgetting.
- Approximate unlearning guarantees removal.
- Synthetic data is consent-free.
- Indigenous data governance is one universal protocol.
- Payment purchases unlimited future use.
- Open models are inherently consentful.
- Closed models are inherently safer.

---

# 45. Required F.11 boundaries

F.11 appropriately includes:

- training as recruitment;
- access, permission, consent, and legitimacy separation;
- individual and collective standing;
- training authority classes;
- purpose and transition-specific consent;
- provenance and documentation;
- preprocessing and labor;
- RLHF, DPO, RLAIF, and constitutions;
- preference disagreement;
- opt-out and refusal;
- withdrawal and unlearning;
- synthetic data and conditional model-collapse claims;
- copyright and legal uncertainty;
- public, trust, cooperative, commons, community, and Indigenous governance;
- benefit;
- model succession;
- training and operation separation;
- breach, repair, formal sketch, and falsification.

Before Phase I specification, the record requires:

1. legal review by jurisdiction;
2. integration with W3C PROV and dataset standards;
3. machine-readable license and restriction review;
4. preference-data documentation standard;
5. community-governance attestation model;
6. privacy-preserving provenance;
7. unlearning evidence taxonomy review;
8. benefit-governance pilots;
9. successor-obligation protocol;
10. anti-greenwashing and anti-consent-washing controls.

---

# 46. Empirical differentiation agenda

## 46.1 Authority-coverage audit

Audit training collections for:

- source;
- license;
- authority;
- purpose;
- community status;
- withdrawal;
- benefit.

Compare documentation claims with evidence.

## 46.2 Restriction propagation benchmark

Attach restrictions to source items and trace them through:

- archive;
- dataset merge;
- preprocessing;
- fine-tuning;
- distillation;
- model release.

Measure survival and enforcement.

## 46.3 Preference-provenance benchmark

Compare model behavior trained from:

- aggregate labels only;
- disagreement distributions;
- subgroup context;
- protected objections;
- constitutional priorities.

## 46.4 Training-consent comprehension

Test whether contributors understand:

- model purpose;
- release regime;
- derivative use;
- withdrawal;
- unlearning limits;
- benefit.

## 46.5 Community-governance pilots

Compare:

- institutional control;
- individual consent;
- data trust;
- cooperative;
- community authority.

Measure participation, legitimacy, minority protection, and benefit.

## 46.6 Unlearning evidence benchmark

Require standardized reporting across:

- source deletion;
- future exclusion;
- approximate unlearning;
- retraining.

Measure false claims and user understanding.

## 46.7 Synthetic-lineage benchmark

Measure whether source and generator provenance survives recursive data production.

## 46.8 Succession audit

Test whether obligations survive model transfer, merge, and open-weight release.

---

# 47. Candidate Phase I architecture implications

G.12 supports a training-governance architecture with the following modules.

## 47.1 Source and authority registry

Stores:

- source identity or class;
- provenance;
- authority basis;
- jurisdiction;
- purpose;
- restrictions;
- community governance;
- benefit;
- dispute.

## 47.2 Transformation lineage

Records:

- preprocessing;
- filtering;
- deduplication;
- annotation;
- aggregation;
- synthetic generation;
- parentage.

## 47.3 Preference-governance service

Stores:

- evaluator population;
- task and policy;
- disagreement;
- aggregation;
- constitution;
- adjudication.

## 47.4 Restriction-propagation engine

Carries restrictions through datasets, checkpoints, merges, and derivatives.

## 47.5 Training event stream

Records model and checkpoint lineage with valid and transaction time.

## 47.6 Withdrawal and unlearning service

Separates:

- source deletion;
- future exclusion;
- retrieval blocking;
- approximate unlearning;
- retraining;
- verification.

## 47.7 Community and benefit service

Supports:

- authority attestations;
- benefit terms;
- governance rights;
- reporting;
- dispute.

## 47.8 Model succession service

Transfers:

- restrictions;
- disputes;
- constitutions;
- unlearning duties;
- benefit obligations;
- responsible authority.

## 47.9 Public training profile

Publishes a bounded, auditable profile without exposing sensitive source data.

## 47.10 Training–operation linkage

Connects training lineage to the F.10 semantic-polytelometry session architecture while keeping the profiles distinct.

---

# 48. Bottom line

F.11 should proceed.

It should proceed as:

- a qualified governance classification;
- a model-lineage architecture;
- a bridge among data documentation, preference training, unlearning, collective governance, and deployment;
- an auditable profile rather than a moral badge;
- a final foundation for the Telic Field Papers' consentful-model branch.

It should not proceed as:

- an individual opt-in requirement for all knowledge;
- a legal conclusion about all AI training;
- a claim that documentation equals legitimacy;
- a promise of perfect unlearning;
- a payment scheme that purchases unlimited use;
- a claim that public or open models are automatically ethical;
- a marketing label detached from source-class evidence.

The strongest defensible formulation is:

> **Consentful training extends established data, preference, documentation, and governance practices by preserving the authority, restrictions, disagreement, withdrawal limits, benefit obligations, and successor duties attached to the semantic and human contributions from which a model is built—while evaluating that lineage separately from the legitimacy of any later deployment.**

---

# Primary references

Bai, Yuntao, et al. “Constitutional AI: Harmlessness from AI Feedback.” arXiv:2212.08073, 2022.

Bender, Emily M., and Batya Friedman. “Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science.” *Transactions of the Association for Computational Linguistics* 6, 2018.

Biega, Asia J., and Michèle Finck. “Reviving Purpose Limitation and Data Minimisation in Data-Driven Systems.” arXiv:2101.06203, 2021.

Carroll, Stephanie Russo, et al. “The CARE Principles for Indigenous Data Governance.” *Data Science Journal* 19, 2020.

European Union. *Regulation (EU) 2016/679 (General Data Protection Regulation)*, 2016.

Gebru, Timnit, et al. “Datasheets for Datasets.” *Communications of the ACM* 64, no. 12, 2021.

Gerstgrasser, Matthias, et al. “Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.” arXiv:2404.01413, 2024.

Holland, Sarah, et al. “The Dataset Nutrition Label: A Framework to Drive Higher Data Quality Standards.” arXiv:1805.03677, 2018.

Jo, Eun Seo, and Timnit Gebru. “Lessons from Archives: Strategies for Collecting Sociocultural Data in Machine Learning.” arXiv:1912.10389, 2019.

Longpre, Shayne, et al. “The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing & Attribution in AI.” arXiv:2310.16787, 2023.

Mitchell, Margaret, et al. “Model Cards for Model Reporting.” Proceedings of FAT*, 2019.

Ouyang, Long, et al. “Training Language Models to Follow Instructions with Human Feedback.” arXiv:2203.02155, 2022.

Paprica, P. Alison, et al. “Essential Requirements for Establishing and Operating Data Trusts.” arXiv:2005.06604, 2020.

Rafailov, Rafael, et al. “Direct Preference Optimization: Your Language Model Is Secretly a Reward Model.” arXiv:2305.18290, 2023.

Seddik, Mohamed El Amine, et al. “How Bad Is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse.” arXiv:2404.05090, 2024.

Shi, Weijia, et al. “MUSE: Machine Unlearning Six-Way Evaluation for Language Models.” arXiv:2407.06460, 2024.

Thaker, Pratiksha, et al. “Position: LLM Unlearning Benchmarks Are Weak Measures of Progress.” arXiv:2410.02879, 2024.

Wang, Weiqi, et al. “Machine Unlearning: A Comprehensive Survey.” arXiv:2405.07406, 2024.
