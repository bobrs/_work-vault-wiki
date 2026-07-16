---
title: "What the Model May Do With What It Learned"
subtitle: "Deployment, Runtime Authority, and the End of a Model's Service"
artifact_date: "2026-07-15"
artifact_type: "public-reader-page"
domain: "TELIC-FIELDS"
scope: "PUBLIC-DRAFT"
status: "pre-publication"
content_canon_status: "unset"
reader_path_position: "H.10"
---

# What the Model May Do With What It Learned

A model may have been trained carefully.

Its sources may be documented.

Its restrictions may be visible.

Its withdrawal process may be honest.

Its constitution may be explicit.

That tells us something important about how its capability came to exist.

It does not tell us what the model may now do to a particular person.

> **Training creates capability. Deployment creates consequence. Authority must be established again.**

A model enters a hospital.

A school.

A workplace.

A benefits office.

A bank.

A court.

A household.

A public meeting.

The model now participates in a new field.

People who never wrote a training example may be scored, advised, classified, scheduled, denied, routed, or remembered.

Their standing begins with the consequence.

Not with their contribution to training.

> **A model does not inherit permission to affect a person merely because it learned from someone else.**

---

# 1. Deployment is a new field

The training field asks:

> How did the model acquire capability?

The deployment field asks:

> Who may this model affect, under whose authority, for what purpose, with which tools, data, memories, and consequences?

A deployment includes more than the model.

It includes:

- the operator;
- the provider;
- the affected people;
- the institution;
- the tool permissions;
- the data flows;
- the governing purpose;
- the business incentives;
- the review process;
- the incident process;
- the model version;
- the shutdown plan.

The same model can be legitimate in one deployment and illegitimate in another.

A language model may be appropriate for drafting a benefits explanation.

The same model may not be authorized to deny the benefit.

---

# 2. Standing without contribution

A patient never contributed training data.

A model classifies the patient's request.

The patient still has standing.

A worker never rated a model response.

A scheduling model changes the worker's shift.

The worker still has standing.

A tenant never consented to help train a risk model.

The model affects the tenant's housing access.

The tenant still has standing.

Runtime standing comes from the relationship of consequence.

It does not depend on whether the person helped create the system.

This is one reason training consent and deployment consent cannot be collapsed into one question.

---

# 3. Capability is not authority

A model can:

- summarize a medical record;
- identify an overdue account;
- recommend a schedule;
- generate a contract;
- call a payment tool;
- send a notice;
- change a database field.

Capability answers:

> Can the system do this?

Authority answers:

> May this system do this, to this target, for this purpose, now?

```text
model can recommend:
  yes

model may authorize:
  no

tool can execute:
  yes

operator has authority:
  partial

affected-center confirmation:
  missing

result:
  do not act
```

> **Capability to act is not authority to act.**

A tool token is not a constitutional grant.

---

# 4. The model needs a runtime role

A model may enter a clinic as:

- translator;
- appointment assistant;
- document summarizer;
- triage aid;
- billing explainer;
- scheduling operator.

These roles carry different authority.

A translator may render a message.

It may not decide what the message means legally.

A scheduling assistant may propose times.

It may not override staffing agreements.

A triage aid may identify urgency.

It may not quietly become the final clinical authority.

The model should not expand its own role because one capability makes another operation convenient.

Role expansion is a new governance event.

---

# 5. Notice is not consent

An institution says:

> This service uses artificial intelligence.

That is notice.

It may be useful.

It is not automatically consent.

A person may have no alternative.

They may not understand what the model does.

They may agree to receive the service while refusing:

- long-term memory;
- output retention;
- model evaluation;
- training reuse;
- cross-account profiling;
- disclosure to another provider.

```text
receive service:
  authorized

save conversation:
  not authorized

use output for evaluation:
  not authorized

use output for training:
  not authorized
```

Service consent is not every later data consent.

The system should preserve the difference in the actual controls, not only in policy language.

---

# 6. Runtime data is new recruitment

Deployment creates new data.

Questions.

Corrections.

Preferences.

Failures.

Private context.

Tool results.

Institutional records.

Model outputs.

These runtime traces may become valuable.

The provider may want to use them for evaluation or retraining.

That is a new recruitment relation.

A person using a service does not automatically become an unpaid model trainer.

The output-capture record should say:

```text
session memory:
  until session close

cross-session memory:
  participant-approved preferences only

evaluation use:
  aggregate, separately authorized

training use:
  disabled

export:
  reviewed institutional record only
```

Good training lineage does not authorize silent runtime extraction.

---

# 7. Purpose drift

A model is deployed to explain eligibility rules.

It performs well.

The institution begins asking it to recommend eligibility.

Then to rank applicants.

Then to approve low-risk cases.

Then to deny incomplete cases automatically.

The model did not suddenly become a different technology.

The deployment became a different constitutional object.

```text
explain
→ recommend
→ rank
→ approve
→ deny
```

Each arrow changes consequence.

Each arrow may require new standing, authority, notice, consent, testing, and repair routes.

> **Purpose drift is authority drift.**

A successful assistance deployment should not become autonomous decision authority through convenience.

---

# 8. Human approval can be real or ceremonial

A model recommends denying a claim.

A worker clicks approve.

The institution says:

> A human made the decision.

Did the worker see:

- the source evidence?
- the model uncertainty?
- the protected condition?
- the claimant's correction?
- the missing context?
- the alternative route?
- the provider constraint?

Could the worker change the decision?

Did they have enough time?

Were they measured on agreement with the model?

A human click may provide meaningful control.

It may also provide a thin ritual around automated momentum.

Human approval matters only when the human can understand, interrupt, revise, and remain accountable for the route.

---

# 9. Incident and repair

A model incorrectly classifies a family transfer as monthly income.

The system denies assistance.

The provider retrains the classifier.

The benchmark improves.

Has the system repaired the incident?

Not yet.

The affected person may still need:

- restored access;
- a corrected institutional record;
- notice to downstream systems;
- reimbursement for late fees;
- compensation for time and burden;
- an appeal record;
- assurance that the correction reached successors.

> **A system is not repaired merely because the model improves after someone else absorbed the harm.**

Model improvement is one repair layer.

Affected-center repair is another.

Both matter.

---

# 10. Monitoring consequence, not only performance

A deployment dashboard may show:

```text
accuracy:
  94%

response time:
  1.8 seconds

cost reduction:
  22%
```

Those numbers may be useful.

They do not show who bears the remaining six percent.

They do not show whether errors cluster around one language, disability, neighborhood, account type, or protected condition.

Monitoring should ask:

- Who received the consequence?
- Who had to appeal?
- Who could not access the appeal?
- Which errors were reversible?
- Which burdens were transferred to workers or families?
- Did the purpose drift?
- Did the provider or model version change?

A model may pass its benchmark and fail its field.

---

# 11. Operator and provider transfer

A service is sold.

The new operator receives:

- the model;
- the databases;
- the prompts;
- the memories;
- the contracts;
- the open incidents;
- the obligations.

Assets can transfer.

Authority may not.

A person's consent to one operator may not authorize another.

A community license may prohibit transfer.

A public mandate may not follow a private acquisition.

A provider change may introduce a new constitution, new memory system, new jurisdiction, or new data incentive.

> **A successor may inherit the system without automatically inheriting every permission that made the prior system legitimate.**

Transfer should reopen the field.

---

# 12. Model updates are constitutional events

A provider replaces Model A with Model B.

The interface looks the same.

The model may have:

- different training lineage;
- different refusals;
- different memory behavior;
- different tool habits;
- different provider policies;
- different failure modes.

The service may call this an update.

The affected field may experience it as a new participant.

A model update should preserve:

```text
prior version
successor version
capability changes
behavior changes
policy changes
authority review
consent and notice review
migration
rollback
open incidents
residual obligations
```

> **Operational continuity is not permission continuity. Model succession is a new constitutional event.**

---

# 13. Rollback

A model update causes unexpected denials.

The institution needs to stop the new behavior.

Rollback may mean:

- return to the prior model;
- disable one tool;
- return to recommendation-only mode;
- restore a prior prompt or policy;
- suspend the deployment.

Rollback is not defeat.

It is preserved possibility.

A deployment that cannot reverse a harmful update has converted operational momentum into authority.

The rollback plan should exist before the incident.

---

# 14. Retirement

The service ends.

The model no longer answers.

What remains?

- conversation records;
- embeddings;
- profiles;
- cached outputs;
- open appeals;
- unpaid compensation;
- unresolved corrections;
- credentials;
- tool connections;
- successor systems;
- legal or public records.

Shutdown stops operation.

It does not make consequence disappear.

A retirement witness should say:

```text
model operations:
  stopped

tool credentials:
  revoked

active memory:
  deleted or transferred by rule

archival witness:
  preserved

open incidents:
  transferred to named custodian

unpaid repair:
  remains due

successor model:
  none

residual unknowns:
  listed
```

> **The authority to stop acting is not the authority to abandon what remains owed.**

---

# 15. A deployment example

A county deploys a civic health assistant trained through a documented mixed-authority lineage.

The model may:

- explain clinic options;
- translate notices;
- summarize participant questions;
- propose appointment times.

It may not:

- deny care;
- change clinical priority;
- assign staff;
- retain conversations for training;
- share a profile across households.

A patient who never contributed training data receives standing because the service affects access to care.

The model proposes two evening clinic sessions.

The scheduling tool is available.

The action gate blocks execution because staffing authority and partner-practice confirmation are missing.

Later, the county asks the same model to determine eligibility for transport assistance.

That is purpose drift.

The deployment pauses until:

- affected centers are assembled;
- authority is granted;
- correction and appeal routes exist;
- runtime data use is reviewed.

An update replaces the model.

The new version receives a narrower grant, inherits the prior correction records, and preserves rollback.

When the pilot ends, the county revokes tool access, transfers open appeals to a human office, deletes active model memory, preserves the public witness, and keeps the repair fund open until claims close.

The model leaves.

The obligations do not vanish with the interface.

---

# 16. A practical deployment review

Before a trained model acts, ask:

## Field

Where is the model being deployed, and who bears consequence?

## Standing

Which affected centers have standing even if they never contributed training data?

## Purpose

What exact runtime purpose is authorized?

## Role

Which operations belong to the model's assigned role?

## Tools

Which tools may it call, and who holds authority over each target?

## Consent

What did affected centers authorize? What other authority basis applies?

## Data

What runtime inputs, memories, outputs, and metadata are retained?

## Drift

What changes would require renewed authority?

## Incident

How will affected people receive correction, restoration, compensation, and appeal?

## Monitoring

Which consequences return to governance?

## Transfer

What happens if operator, provider, jurisdiction, or owner changes?

## Version

What changes when the model updates, and can it roll back?

## Retirement

What residual data, incidents, claims, and obligations survive shutdown?

A model can be highly capable and still fail this review.

Capability is not the final gate.

---

# What this page does not claim

This page does not claim:

- that every deployment requires individual opt-in;
- that public institutions cannot deploy models under mandate;
- that notices are useless;
- that human review is always ceremonial;
- that autonomous tool use is always illegitimate;
- that every error requires monetary compensation;
- that every update requires renewed consent from every person;
- that all residual records should be retained forever;
- that shutting down a service should erase history;
- that a complete witness automatically makes deployment just.

---

# The next public question

HI-10 completes the first public and technical path from field formation through model training and deployment.

The next question is no longer another layer inside the same path.

It is:

> Does the whole architecture remain coherent when read as one system?

That is the bridge into H/I synthesis.

The next pass must examine:

- duplicated terms;
- conflicting authority rules;
- missing lifecycle transitions;
- public-reader burden;
- schema overlap;
- conformance levels;
- implementation minimums;
- what belongs in research, specification, pilot, or publication.

---

# Closing

The model learned.

Then it arrived.

Arrival creates a new relation.

The people affected may never have trained it.

The operator may not own every permission.

The provider may not control every consequence.

The model may be able to act before it is allowed to act.

A trustworthy deployment establishes authority again.

It separates service from extraction.

It detects purpose drift.

It repairs people, not only models.

It returns consequence to governance.

It treats transfer and update as constitutional events.

And when the service ends, it stops acting without abandoning what remains owed.

> **Training creates capability. Deployment creates consequence. Authority must be established again.**
