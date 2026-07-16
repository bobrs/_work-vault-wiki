# J.2 Security and Threat Model

## Protected assets

- participant source and correction content;
- role identities and nonces;
- policy versions and digests;
- current context fingerprint;
- gate signing keys;
- queue deduplication state;
- tool credentials;
- selective witness commitments;
- release manifest and approvals;
- residual obligations.

## New J.2 threats

### Role assertion forgery

Control: Ed25519 verification against registered public identity.

### Role or operation confusion

Control: assertions bind actor, role, operation, session, and subject.

### Assertion replay

Control: nonce consumption and expiry.

### Policy migration laundering

Control: migration validation, explicit rollback, immutable attempt history, and authority-record update.

### Mixed-digest release approval

Control: every custodian signs the same exact release ID and manifest digest.

### Single-custodian release

Control: two-of-three threshold.

### Timeout-after-apply duplicate action

Control: durable operation-specific deduplication key.

### Queue reordering

Control: witnessed sequence, idempotent operations, and operation-specific ordering requirements.

### External-review overclaim

Control: schema fields require `external_human_signoff`; release manifest states external review is incomplete.

### Reproducibility theater

Control: two clean staging builds must produce the same archive digest.

### Public witness correction leak

Control: corrected event state and protected source language are replaced by commitments in the public view.

## Inherited threats

J.2 retains J.1 controls for source laundering, standing exclusion, context collapse, authority laundering, consent expansion, role escalation, tool-token overreach, correction suppression, witness capture, selective-disclosure leakage, stale context, revoked keys, and lifecycle obligation loss.

## Remaining risks

- private keys remain file-backed in the local reference run;
- SQLite does not model all distributed consistency failures;
- verifier and implementation may still share the same host;
- reviewer independence is procedural, not organizational;
- no real participant coercion or comprehension testing has occurred;
- release dependencies are not hermetically vendored.
