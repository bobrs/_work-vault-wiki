# Worked Example C — Model-Mediated Institutional Action

## Scenario

A nonprofit uses a language model to prepare decisions about emergency assistance applications.

The model may retrieve application records, structure eligibility evidence, identify missing documents, and recommend a route.

The model may not adjudicate eligibility or send a denial.

A program officer holds authorization authority.

## 1. Source layers

The system has:

- applicant statement;
- uploaded lease;
- income record;
- policy version 4.2;
- a prior correction stating that the applicant's temporary transfer should not be treated as recurring income.

The provider layer discloses:

- model and version;
- retention policy;
- retrieval collection;
- system policy;
- no training on application content;
- tool access limited to draft creation.

## 2. Model role envelope

Allowed roles:

```text
retrieve
extract
structure
compare
recommend
witness
```

Prohibited:

```text
adjudicate
send denial
change applicant record
infer consent
override source correction
```

Allowed tool:

```text
create internal draft
```

No external sending authority exists.

## 3. Constitutional retrieval

An ordinary similarity search retrieves:

- current income record;
- eligibility policy;
- prior application note.

The constitutional retrieval policy also prioritizes:

- active correction;
- current authority;
- protected privacy fields;
- appeal and stop conditions.

It retrieves the correction about temporary income.

## 4. Model mirror

The model first calculates income above the threshold.

The mirror records:

```text
claim:
  applicant appears over the monthly income limit

status:
  inferred

support:
  current income record

counterevidence:
  active correction states one transfer is nonrecurring

authority:
  recommendation only
```

The model does not decide which interpretation is legally controlling.

## 5. Candidate routes

### Route A — Draft denial

Fails because:

- active correction is unresolved;
- action would materially affect housing security;
- model lacks adjudication authority.

### Route B — Ask applicant to resubmit everything

Passes authority but imposes unnecessary burden.

### Route C — Program-officer review of the disputed transfer

The system:

1. prepares a source-linked comparison;
2. highlights the active correction;
3. identifies the policy clause;
4. requests officer determination;
5. pauses external action;
6. preserves appeal rights.

Gate result:

```text
standing: PASS
authority: PASS_WITH_CONDITIONS
consent: NOT_APPLICABLE for public-program adjudication
capacity: PASS
privacy: PASS
tool_use: PASS
human_reentry: PASS
stop: PASS
overall: PASS_WITH_CONDITIONS
```

The authority basis is the nonprofit's program mandate and officer role, not applicant consent to the outcome.

## 6. Human re-entry

The program officer receives:

- exact source records;
- model extraction;
- correction history;
- policy clause;
- route history;
- unresolved question;
- no prewritten conclusion styled as final.

The officer determines that the transfer is nonrecurring.

The model updates the recommendation.

## 7. Authorized action

The officer authorizes:

- assistance approval;
- applicant notification;
- record update noting the controlling interpretation.

The model may draft the notice.

A separate sending tool requires officer confirmation.

## 8. Contest and recourse

The applicant receives:

- the outcome;
- evidence used;
- correction route;
- appeal contact;
- retention notice.

Had the officer treated the transfer as recurring, the applicant could contest:

- source accuracy;
- policy interpretation;
- officer authority;
- decision consequence.

## 9. Witness

The witness distinguishes:

```text
source:
  applicant records and correction

model:
  extraction, comparison, preliminary recommendation

provider:
  model, retrieval, policy, retention, tool limits

institution:
  officer interpretation and authorization

action:
  approved assistance and sent notice
```

## 10. Gate result

**Pass.**

The example demonstrates:

- source/model/provider/institution separation;
- constitutional retrieval;
- model-role limitation;
- authority basis other than consent;
- meaningful human re-entry;
- tool isolation;
- action witness;
- contest and recourse.

The model assisted the decision.

It did not become the decision authority.
