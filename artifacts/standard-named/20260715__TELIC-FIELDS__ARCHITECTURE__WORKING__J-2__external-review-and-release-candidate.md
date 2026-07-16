# J.2 Architecture

## Governing invariant

> A representation may gain action power only through a visible chain of source, standing, authority, consent where applicable, context, role, gate, consequence, witness, correction, and exit.

J.2 keeps the J.1 action gate outside the model and adds organizationally separable approval and verification layers.

```text
participant identities
        │
        ▼
signed role assertions
        │
        ▼
append-only event and object store
        │
        ├── current semantic context
        ├── versioned authorization policy
        ├── correction descendant graph
        └── selective-disclosure profiles
        │
        ▼
non-sovereign route generation
        │
        ▼
external action gate
        │
        ▼
durable delivery queue
        │
        ▼
scheduling tool simulator
        │
        ▼
consequence and repair witness
        │
        ▼
Ed25519 witness signature
        │
        ▼
two-of-three release approval
        │
        ▼
deterministic release candidate
```

## Trust boundaries

### Participant identity boundary

Each material participant correction carries a signed role assertion containing:

```text
actor
role
operation
session
subject
issued time
expiry
nonce
```

The assertion is rejected if the signature, role, operation, session, expiry, or nonce is invalid.

### Model boundary

The model may structure, summarize, generate candidate schedules, and prepare a tool request. It cannot issue role assertions, publish policy, mint a valid gate token, acknowledge a queue message, authorize the target, approve a release, or retire its own authority.

### Action boundary

The external action gate validates current policy, current context, standing, protected conditions, operator assertion, tool status, and target authority. The model never receives the gate signing key.

### Delivery boundary

The durable queue separates authorization from delivery. A valid authorization may encounter timeout, duplicate delivery, or reordering. The queue records attempts and deduplicates effects by an operation-specific key.

### Release boundary

The release manifest is approved by distinct Ed25519 custodians. Two valid signatures are required. The release archive carries only public custody material.

### Verification boundary

The witness and release verifiers live outside the implementation package namespace. They require no provider connection and do not import `telic_j2`.

## Persistent stores

- `trial.sqlite3` — event chain, governed objects, edges, and current metadata;
- `delivery-queue.sqlite3` — durable messages and exactly-once effect records;
- private run directory — participant and custody private keys, excluded from exports;
- witness ZIP — signed, checksummed, selectively disclosed evidence;
- release ZIP — deterministic source and evidence bundle with threshold approvals.

## Failure philosophy

J.2 distinguishes:

```text
authorization failure
≠ delivery failure
≠ tool partial failure
≠ verification failure
≠ review incompleteness
```

Each failure is preserved under its own class rather than compressed into one success or error flag.
