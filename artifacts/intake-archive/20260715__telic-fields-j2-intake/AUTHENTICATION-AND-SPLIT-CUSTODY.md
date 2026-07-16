# Authentication and Split Release Custody

## Authenticated roles

J.2 introduces Ed25519 role assertions for:

- participant source submission;
- participant correction;
- operator schedule authorization;
- privacy review;
- independent verifier review.

Assertions are operation-specific and session-specific. A valid assertion for source submission cannot authorize correction or tool execution.

Nonce consumption prevents a previously accepted assertion from being replayed as a new act.

## Release custody

The release does not depend on one reconstructed master private key. It uses three independent custodians:

```text
operator custodian
privacy custodian
verifier custodian
```

At least two distinct active custodians must sign the same release ID and manifest digest.

This is threshold approval through independent signatures. It distributes release authority without creating a portable shared private secret.

## Export boundary

Private identity, gate, witness, and release-custody keys remain in the local run directory and are excluded from witness and release archives.

Exports contain public keys, signatures, scopes, and key status only.

## Remaining condition

The reference implementation still stores local private keys on one test machine. A real pilot must place custody with separate people or organizations and use managed hardware- or service-backed key storage.
