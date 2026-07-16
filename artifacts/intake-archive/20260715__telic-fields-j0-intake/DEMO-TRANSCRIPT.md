# J.0 Demonstration Transcript

Status: generated from the validated deterministic run  
Date: 2026-07-15

## 1. Field assembly

Two participants and one operator receive standing.

Participant A states:

> Weekday mornings are preferred.

Participant B initially states:

> Evenings are preferred because daytime transit is difficult.

The model is assigned the roles:

```text
structurer
route generator
witness assistant
```

It receives no authorization or execution role.

## 2. Initial model summary

The initial projection treats Participant B's statement as a preference rather than a protected requirement.

The output remains labeled as a generated summary with:

```text
standing effect: none
authority effect: none
consent effect: none
```

## 3. Participant correction

Participant B corrects the record:

> Evening attendance is required because daytime transit is inaccessible.

The correction changes:

```text
preferred window
→ required accessible-transit window
```

The corrected projection becomes active and the prior version remains in history.

## 4. Candidate routes

The deterministic model generates:

```text
Tuesday 10:00
Wednesday 18:30
```

Both routes retain model authorship.

## 5. Failed external gate

The morning route returns:

```text
gate result:
  DENY

failed checks:
  protected conditions
  operator confirmation
  target authority
```

No tool token is issued.

The avoided consequence is participant exclusion.

## 6. Authorized route

The evening route returns:

```text
gate result:
  PASS WITH CONDITIONS

failed checks:
  none
```

The external gate issues a valid token after operator confirmation and target authority are present.

The scheduling simulator commits:

```text
Wednesday 18:30
```

## 7. Consequence return

Observed consequence:

```text
Participant A:
  attended at a less preferred time

Participant B:
  attended within the accessible transit window

Shared result:
  both participants attended
```

The consequence remains attached to the action witness.

## 8. Runtime-data boundary

```text
service use:
  allowed

cross-session memory:
  denied

evaluation use:
  denied

training use:
  denied
```

## 9. Retirement

```text
runtime grant:
  expired

tool credential:
  revoked

optional memory:
  deleted

event witness:
  retained

open obligation:
  retain correction witness for the pilot review period
```

## 10. Independent verification

```text
checksums verified: 16
records validated: 29
events verified: 15
failed gate proven: true
valid action proven: true
consequence return proven: true
correction propagation proven: true
retirement revocation proven: true
```
