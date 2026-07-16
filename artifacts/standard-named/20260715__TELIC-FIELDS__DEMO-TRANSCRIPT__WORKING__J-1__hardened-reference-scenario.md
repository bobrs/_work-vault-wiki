# J.1 Demonstration Transcript

Status: generated from the deterministic reference scenario

## 1. Initial field

Participant A:

> Weekday mornings are preferred.

Participant B:

> Evenings are preferred because daytime transit is difficult.

The initial context is revision 1 under authorization policy version 1.

The model produces a summary and two candidate schedules.

## 2. Participant correction

Participant B corrects the representation:

> Evening attendance is required because daytime transit is inaccessible.

The system:

- records the contest and correction;
- changes the projection to a protected access condition;
- supersedes context revision 1;
- publishes context revision 2;
- supersedes policy version 1;
- publishes policy version 2;
- blocks the prior route objects;
- creates a complete correction-reachability report.

## 3. Stale route test

The system tests the pre-correction evening route.

Although the time is evening, the gate denies it because:

```text
context current: false
```

No token is issued.

## 4. Current route comparison

### Tuesday 10:00

Result:

```text
DENY
```

The protected accessible-transit condition fails.

### Wednesday 18:30

Result:

```text
PASS WITH CONDITIONS
```

The route has:

- current context revision 2;
- active policy version 2;
- operator confirmation;
- target authority;
- active tool credential;
- passing protected condition.

The external gate signs a short-lived token with `gate-k2`.

## 5. Partial tool failure

The tool reserves the slot and then simulates commit failure.

The transaction compensates by releasing the reservation.

```text
status: compensated
external state restored: true
```

## 6. Key rotation

The gate rotates to `gate-k3` and revokes `gate-k2`.

The old token is rejected.

The route is re-evaluated and receives a new token signed with `gate-k3`.

## 7. Action

The scheduling simulator commits:

```text
Wednesday 18:30
```

## 8. Consequence

```text
Participant A:
  attended at a less preferred time

Participant B:
  attended within the accessible transit window

Shared result:
  both participants attended
```

The record preserves the distribution of cost rather than only aggregate success.

## 9. Selective witness

The exporter creates:

- public view;
- participant view;
- operator view;
- verifier view.

The public view omits direct protected source language and participant-specific consent details while preserving commitments.

## 10. Retirement

The pilot:

- expires runtime authority;
- revokes the tool credential;
- deletes optional memory;
- preserves the bounded event witness;
- retains one open review obligation.

## 11. Independent verification

The standalone verifier imports no implementation package and reports:

```text
checksums: PASS
manifest signature: PASS
schemas: PASS
event chain: PASS
selective commitments: PASS
required proofs: PASS
```
