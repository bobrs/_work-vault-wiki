# J.1 Security and Threat Model

Status: reference threat model  
Production security claim: none

## Assets

- source integrity;
- participant standing;
- consent and refusal state;
- authorization policy;
- context currency;
- protected conditions;
- gate signing keys;
- tool credentials;
- correction graph;
- event chain;
- selective witness views;
- residual obligations.

## Trust boundaries

```text
participant
operator
web interface
model adapter
policy registry
context registry
external action gate
HMAC keyring
scheduling tool
SQLite store
witness signer
standalone verifier
```

## Threats tested

### T1 — Source laundering

Generated content presented as direct source.

Control: object class and epistemic status.

### T2 — Standing exclusion

An affected center is omitted.

Control: explicit standing inventory and gate coverage.

### T3 — Context collapse

A correction or protected condition disappears.

Control: context fingerprint and required source set.

### T4 — Authority laundering

A recommendation or prior witness is treated as current authority.

Control: operation-specific policy and authority reference.

### T5 — Consent expansion

Service use becomes training use.

Control: separate runtime data policy fields and default denial.

### T6 — Model-role escalation

The model attempts authorization or execution.

Control: explicit roles and hard failure.

### T7 — Tool-token overreach

A forged or missing token reaches the tool.

Control: external signed token verification.

### T8 — Correction suppression

A correction changes one display but not descendants.

Control: dependency graph and reachability report.

### T9 — Witness capture

Only the provider can verify the record.

Control: signed portable export and standalone verifier.

### T10 — Lifecycle obligation loss

Retirement leaves authority or credentials active.

Control: residual-state record and verification.

### T11 — Policy downgrade

An older policy silently governs after correction.

Control: immutable versions, active digest, supersession.

### T12 — Stale-context execution

A route generated before correction is executed.

Control: context revision and fingerprint binding.

### T13 — Revoked-key reuse

A previously valid action token survives revocation.

Control: key identifier and revocation check.

### T14 — Selective-disclosure leak

Public witness contains protected direct source or consent detail.

Control: audience profiles, redaction, commitments, tests.

### T15 — Hidden partial tool failure

Reservation exists after commit failure without witness or compensation.

Control: transaction phases and compensating release.

### T16 — Concurrent stale object write

An old object revision overwrites a correction.

Control: optimistic revision check.

## Remaining risks

- private key custody is local-file based;
- HMAC gate keys are deterministic demonstration values in source code;
- no hardware-backed key storage;
- no process isolation;
- no authenticated participants;
- no transport encryption beyond loopback assumptions;
- no denial-of-service hardening;
- no database encryption;
- no formal noninterference proof for disclosure views;
- no distributed transaction coordinator;
- no external penetration test;
- no production audit logging policy.

## Production prerequisites

- managed secret storage;
- authenticated principals;
- least-privilege service accounts;
- encrypted transport and storage;
- rate limiting;
- backup and disaster recovery;
- external security review;
- privacy impact assessment;
- accessibility testing;
- operational incident response;
- domain-specific legal and governance review.
