# HI-7 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

Twelve candidate Draft 2020-12 schemas were checked:

- `public-field-assembly.schema.json`
- `standing-admission-record.schema.json`
- `option-set-witness.schema.json`
- `protected-condition-declaration.schema.json`
- `deliberative-assertion-record.schema.json`
- `decision-rule-portfolio.schema.json`
- `route-portfolio.schema.json`
- `dissent-minority-trail.schema.json`
- `cost-delay-bearer-map.schema.json`
- `abstention-no-decision-record.schema.json`
- `public-decision-witness.schema.json`
- `consequence-return-revision.schema.json`

Result:

```text
schemas checked: 12
schema errors: 0
```

## Positive demonstrations

All eight required demonstrations passed:

1. an excluded route became visible and entered the option set;
2. minority standing remained represented without becoming automatic veto;
3. a protected condition blocked ordinary compensatory tradeoff;
4. majority, weighted, outranking, and robust methods produced visibly different comparisons;
5. a route portfolio preserved several forms of access;
6. a no-decision state identified delay bearers and temporary protection;
7. dissent remained attached to the selected route;
8. observed consequence returned to the field and reopened navigation.

Result:

```text
positive demonstrations passed: 8
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. fictional collective utility;
2. option omission represented as participant rejection;
3. hidden model authorship;
4. protected condition represented as an ordinary weight;
5. consensus represented as universal consent;
6. majority represented as complete legitimacy;
7. method treated as neutral and unwitnessed;
8. dissent deleted after decision;
9. abstention counted as support;
10. no-decision represented without delay bearers;
11. portfolio burden shifted invisibly to vulnerable centers;
12. observed consequence left outside the original decision record.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## Public DecisionWitness

The event-generated PublicDecisionWitness preserves:

- field scope;
- standing admissions;
- option construction and authorship;
- protected conditions;
- deliberative assertions and correction;
- decision-method comparison;
- route portfolio;
- selected action and authority;
- cost and delay bearers;
- dissent;
- no-decision state;
- implementation conditions;
- review triggers.

Result:

```text
public decision witness: PASS
generated_from_events: true
dissent preserved: true
option authorship preserved: true
```

## Independent public-decision export

The export contains:

- public-field assembly;
- standing records;
- option-set witness;
- protected condition;
- assertions and corrections;
- decision-rule portfolio;
- route portfolio;
- dissent trail;
- cost and delay map;
- no-decision record;
- eight demonstrations;
- event stream;
- PublicDecisionWitness;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 32
checksum failures: 0
independent of deliberation platform: true
```

## Public-page consistency review

H.7 was checked against I.7 for the following claims:

- one action does not imply one public purpose;
- standing precedes counting;
- option construction is constitutional power;
- protected conditions differ from heavily weighted preferences;
- weights and methods remain claims rather than neutral facts;
- portfolios may preserve plurality but may shift burden;
- minority standing does not create automatic veto;
- dissent remains part of the decision;
- abstention is not agreement;
- no-decision has delay bearers;
- observed consequence returns to public judgment.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- legal standing or voting eligibility;
- one valid democratic decision rule;
- universal protected conditions;
- fairness of the county clinic example;
- completeness of affected-center discovery;
- neutrality of facilitation;
- production security;
- public-reader comprehension;
- scientific proof of the broader framework.

## Conditions before production use

- authenticate standing and representation sources;
- define domain-specific protected-condition authority;
- implement public challenge to option construction;
- expose model-generated option authorship;
- compare at least two materially different decision methods;
- test burden allocation in route portfolios;
- implement dissent-preserving publication and privacy controls;
- return observed consequence to the original witness;
- conduct independent reader testing of H.1 through H.7.
