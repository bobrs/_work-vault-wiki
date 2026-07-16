# Policy, Key, and Context Hardening

## Policy versioning

J.1 begins under authorization policy version 1.

Participant B corrects an ordinary preference into a protected access condition.

The system publishes policy version 2, adding explicit requirements for:

- correction reachability;
- stale-context rejection.

The prior policy remains preserved as `superseded`.

Runtime authority is updated to the new policy version and digest.

A route generated under policy or context version 1 cannot silently act under version 2.

## Context fingerprint

The context fingerprint commits to:

```text
projection identifiers
canonical projection hashes
correction event identifiers
context revision
```

A route must carry both:

```text
context revision
context fingerprint
```

The gate compares them with the active context.

The pre-correction evening route is denied even though its clock time would satisfy the corrected access condition, because it was generated from the wrong semantic state.

> A route can be operationally plausible and constitutionally stale.

## Gate-key rotation

The demonstration begins with:

```text
gate-k1: revoked
gate-k2: active
```

After a compensated partial tool failure:

```text
gate-k2: revoked
gate-k3: active
```

The old token is rejected.

The route is re-evaluated under the current policy, context, and key before retry.

This prevents a previously issued token from silently surviving a key-compromise response or governance transition.

## Export signing

Action tokens use a local HMAC keyring because the gate and tool share an operational trust domain in the reference pilot.

Witness manifests use Ed25519 because independent verification requires a public verification key without disclosure of the signing key.

The two key systems are intentionally distinct.
