---
title: "What the Model Learned From Us"
subtitle: "Training, Standing, Withdrawal, and the Lineage of Capability"
artifact_date: "2026-07-15"
artifact_type: "public-reader-page"
domain: "TELIC-FIELDS"
scope: "PUBLIC-DRAFT"
status: "pre-publication"
content_canon_status: "unset"
reader_path_position: "H.9"
---

# What the Model Learned From Us

A model does not begin when someone opens the chat.

It arrives already shaped.

It has learned from books, websites, code, conversations, images, labels, demonstrations, rankings, corrections, policies, and outputs from other models.

It carries traces of human and institutional fields into every later interaction.

Training is usually described as optimization.

That is true.

It is incomplete.

> **Training is a recruitment relation before it is an optimization procedure.**

A source is collected.

A record is copied.

A dataset is filtered.

A worker labels an answer.

A reviewer ranks two responses.

A provider writes a constitution.

A model generates new training examples.

A successor model inherits the result.

Each transition recruits capacity from one loop into another.

The question is not merely whether the model improved.

The question is:

> Under whose authority did each contribution enter, and what survived the transformation?

---

# 1. Public is not ownerless

A text may be publicly readable.

That does not settle every future use.

A public article may have:

- an author;
- a publisher;
- a license;
- a community context;
- people described within it;
- privacy interests;
- restrictions on redistribution;
- a purpose different from model training.

The same source may be:

```text
readable by the public:
  yes

available for automated collection:
  technically yes

licensed for research:
  yes

consented for commercial model training:
  unknown

authorized for deployment in a profiling system:
  no
```

These are different questions.

> **Public does not mean ownerless. Accessible does not mean available for every purpose.**

The difference is not solved by one universal answer.

It is solved by preserving the lineage of authority.

---

# 2. Access, permission, consent, and legitimacy

A system can access a source without permission.

A system can have legal permission without the source person's consent.

A person can consent to a use that still harms another center.

A community can authorize collective knowledge that no individual owns alone.

A public institution can act under a mandate rather than personal consent.

Consent matters.

It is not the only authority basis.

It is also not interchangeable with every other basis.

```text
access
≠ permission

permission
≠ consent

consent
≠ ownership

ownership
≠ legitimacy

legitimacy
≠ unlimited future use
```

A consentful training system does not pretend that every source entered through individual opt-in.

It makes the actual basis visible.

---

# 3. One yes is not every yes

An author agrees to publish an article.

That does not automatically mean:

- collect it into a model dataset;
- translate it;
- summarize it;
- use it for preference training;
- release a commercial model;
- use that model to profile the author;
- feed the model's outputs into another model;
- preserve the source forever.

Consent and authority are attached to transitions.

```text
create
→ publish
→ collect
→ store
→ transform
→ annotate
→ train
→ release
→ deploy
→ log
→ retrain
```

A valid yes at one arrow does not automatically travel through every later arrow.

> **One consent event is not a universal downstream license.**

This is why training lineage must be more than a list of source URLs.

It must show what each transition was allowed to do.

---

# 4. Source standing

A source may have more standing attached to it than one author can grant.

A personal diary may involve the people described in it.

A community archive may contain collective history.

A language corpus may encode cultural knowledge.

A medical record may involve patient, clinician, institution, and public duty.

A dataset of public comments may contain people who expected participation in one process, not permanent recruitment into another.

An individual may have authority over their own words.

They may not have authority to sell the community relationship carried by those words.

> **Individual consent cannot authorize what the individual does not legitimately own or represent.**

Source standing is not a claim that every source requires unanimous control.

It is a requirement that the system notice whose field it is recruiting.

---

# 5. Transformation does not erase lineage

Training data rarely remains as it was collected.

It is:

- cleaned;
- filtered;
- deduplicated;
- translated;
- summarized;
- redacted;
- labeled;
- ranked;
- mixed;
- sampled;
- tokenized;
- embedded;
- synthesized.

These steps may improve quality.

They are also governance.

Filtering decides which voices remain.

Deduplication can amplify or suppress classes of sources.

Translation introduces interpretation.

Summarization creates new compression.

Mixing can make restrictions difficult to see.

A transformation may create a new object.

It does not make the source history disappear.

> **Provenance does not guarantee legitimacy. It prevents transformation from pretending it had no source.**

---

# 6. Annotation is human contribution

A model may be trained from people deciding:

- which answer is better;
- which statement is harmful;
- which response is helpful;
- which rewrite is clearer;
- which refusal is appropriate;
- which tone is preferred;
- which principle applies.

This is not merely data labeling.

It is situated judgment.

The task, instructions, compensation, time pressure, cultural context, and available options shape the judgment.

A worker may rank answer A over answer B because the instructions required brevity.

That does not mean humanity prefers brevity in every context.

> **Preference data is a projection of judgment under a task, not a sample from a single human telos.**

The disagreement among annotators is also information.

A training system should not erase disagreement merely because optimization requires one number.

---

# 7. Preference aggregation is governance

Suppose ten reviewers compare two answers.

Six prefer A.

Four prefer B.

The system records:

```text
preferred:
  A
```

That may be sufficient for one optimization step.

It is not a complete social truth.

The four may represent:

- a different cultural norm;
- a protected safety concern;
- a minority use case;
- a disagreement about facts;
- a different interpretation of the task.

Preference aggregation creates a constitution of behavior.

It decides what the model is rewarded for reproducing.

That constitution may be useful.

It should not be mistaken for humanity speaking with one voice.

---

# 8. The model constitution

Some models are trained or guided by explicit principles.

For example:

- be helpful;
- avoid harm;
- protect privacy;
- respect user autonomy;
- follow the law;
- refuse certain operations.

Making the principles explicit is valuable.

It reveals the constitution.

It does not prove that the constitution has legitimate authority over every person and context.

Who wrote it?

Who adopted it?

Who may challenge it?

Which center does it protect?

Which provider objective does it serve?

Which conflicts are hidden in phrases such as “helpful” or “safe”?

> **A constitution is not legitimate merely because it is explicit. It becomes governable because it is explicit.**

A provider constitution should not be presented as public consensus.

A participant-adopted rule should preserve the fact that participants adopted it.

---

# 9. Synthetic data still has ancestry

A model generates a million new examples.

The dataset is called synthetic.

That can sound like it came from nowhere.

It did not.

The synthetic examples may depend on:

- the generating model;
- the model's training data;
- the prompt;
- the provider policy;
- the sampling process;
- the evaluator;
- the filtering rules;
- earlier synthetic generations.

> **Synthetic does not mean unowned, unbiased, source-free, or consent-free.**

Synthetic data may reduce direct exposure to source records.

It may also repeat hidden errors, restrictions, or biases.

The ancestry matters because later models can inherit conditions that are no longer visible in the generated text.

---

# 10. Withdrawal

A contributor withdraws permission.

What can the system actually do?

It may:

- stop new collection;
- delete the stored source;
- block future training;
- block runtime retrieval;
- restrict release;
- attempt machine unlearning;
- retrain without the source;
- retire the model.

These are different actions.

Deleting the source file does not prove the model forgot.

Approximate unlearning does not prove every effect disappeared.

A later derivative may remain unreachable.

A trustworthy withdrawal record says what happened and what did not.

```text
future collection:
  stopped

stored source:
  deleted

runtime retrieval:
  blocked

approximate unlearning:
  performed

verification:
  passed declared tests

complete removal:
  not established

known derivative gap:
  one external model
```

> **Withdrawal is a governance right. Complete model unlearning is a technical capability that must not be promised beyond evidence.**

---

# 11. Correction after training

A source may be corrected after a model was trained.

A person changes a factual record.

A community rejects a classification.

An author revokes an outdated statement.

A dataset is found to contain a systematic error.

Correction should not stop at the source file.

The system should ask:

- Which datasets inherited it?
- Which summaries repeated it?
- Which models learned from it?
- Which runtime retrieval systems still expose it?
- Which successor models depend on it?
- Which users were affected?

Some corrections may be applied at runtime.

Some may require new training.

Some may remain unresolved.

The lineage should preserve the difference.

---

# 12. Derivative models inherit obligations

A base model is fine-tuned.

The fine-tuned model is distilled.

The distilled model is merged into another system.

The final service is operated by a different company.

Each transition makes lineage harder to see.

It does not erase the obligation.

> **A successor may inherit capability without escaping the conditions under which the capability was recruited.**

Known restrictions, corrections, withdrawals, and repair obligations should travel with derivative models.

A successor model should not claim innocence merely because it did not collect the original source directly.

---

# 13. Benefit

A model creates value.

Who contributed?

Authors.

Annotators.

Communities.

Maintainers.

Reviewers.

People whose conversations revealed what the system needed to learn.

People whose corrections prevented harm.

The provider may say:

> This innovation benefits everyone.

That is not yet a benefit mechanism.

> **A vague promise that innovation benefits everyone is not a benefit-sharing mechanism.**

Benefit may include:

- payment;
- royalties;
- community licenses;
- public access;
- returned services;
- infrastructure;
- research results;
- governance rights;
- attribution;
- repair funds;
- public-interest release.

Not every contribution requires the same return.

But the relationship between recruited value and returned value should be legible.

---

# 14. Consentfully trained is not a purity badge

No complex model is likely to have perfect lineage.

Some sources may be unknown.

Some licenses may be contested.

Some derivatives may be unreachable.

Some withdrawal requests may not be technically satisfiable.

Some public mandates may substitute for individual consent.

A model should not receive a simple badge:

```text
CONSENTFUL:
  yes
```

A more honest profile says:

```text
source standing coverage:
  high but incomplete

training authority:
  mixed

community review:
  partial

preference provenance:
  documented

synthetic ancestry:
  known to depth three

withdrawal support:
  source deletion and approximate unlearning

derivative propagation:
  partial

benefit mechanism:
  active community license

contested lineage:
  two source classes
```

> **Consentfully trained is not a binary purity claim. It is a lineage claim over data, transformations, capabilities, and uses.**

The profile makes the model more governable.

It does not declare the model morally pure.

---

# 15. Training and deployment are separate questions

A model may have strong training lineage and harmful deployment.

A model may have poor training lineage and careful runtime controls.

Neither cancels the other.

```text
training legitimacy
≠ deployment legitimacy
```

Good deployment does not erase extraction.

Good provenance does not excuse harmful use.

A consentful system must evaluate both.

> **Consentful operation does not retroactively make unconsented training consentful. Consentful training does not guarantee consentful deployment.**

---

# 16. A practical training-lineage review

Before a model is called consentfully trained, ask:

## Source

What source classes entered?

## Standing

Which people, communities, institutions, or publics hold interests in them?

## Collection

How did each source enter the lineage?

## Authority

Which basis authorized collection, training, release, and later use?

## Consent

Where was consent actually present, and what did it cover?

## License

Which uses were licensed?

## Transformation

What was filtered, translated, summarized, mixed, or generated?

## Labor

Who annotated, ranked, critiqued, or corrected?

## Preferences

What task produced the preference, and which disagreements were lost?

## Constitution

Who wrote the governing principles?

## Synthetic ancestry

Which models and sources generated the new data?

## Withdrawal

What can be stopped, deleted, unlearned, retrained, or retired?

## Derivatives

Which successor models inherit the conditions?

## Benefit

What concrete value returns to contributors or communities?

A model lineage need not be perfect to be legible.

It must not use uncertainty as permission to claim purity.

---

# What this page does not claim

This page does not claim:

- that every training source requires individual opt-in;
- that every public source is unavailable for training;
- that legal permission is irrelevant;
- that license and consent are the same;
- that every community has one authorized representative;
- that every model can be exactly unlearned;
- that every derivative can be reached;
- that payment is always required;
- that payment creates unlimited consent;
- that open models are inherently consentful;
- that closed models are inherently safer;
- that documentation alone proves legitimacy.

---

# The next public question

Once the training lineage is visible, another question appears:

> What may the trained model legitimately do in the world, under whose authority, and how does that authority end?

That is the problem of consentful deployment, runtime field governance, and model succession.

It asks how a model enters an institution, receives tools, affects people, accumulates operational memory, changes purpose, transfers to new operators, and eventually leaves or dissolves without abandoning what remains owed.

---

# Closing

The model learned from us.

From our writing.

Our labels.

Our judgments.

Our disagreement.

Our corrections.

Our histories.

Our communities.

Our labor.

That learning may produce extraordinary public value.

Value does not erase lineage.

Transformation does not erase standing.

Payment does not erase relationship.

Synthetic generation does not erase ancestry.

And deletion does not prove forgetting.

A trustworthy model can show how capability entered.

It can show which authority governed each transition.

It can show where lineage is incomplete.

It can tell the truth about withdrawal.

It can carry correction into successors.

And it can return concrete benefit to the fields from which its intelligence was recruited.

> **Training is a recruitment relation before it is an optimization procedure.**
