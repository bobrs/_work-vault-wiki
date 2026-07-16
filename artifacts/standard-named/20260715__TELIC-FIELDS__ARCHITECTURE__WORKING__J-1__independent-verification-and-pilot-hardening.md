# J.1 Architecture

Status: executable reference implementation  
Version: 0.1

## Constitutional path

```text
source
→ projection
→ standing
→ authorization policy version
→ active context revision
→ model role
→ route
→ external gate
→ transactional tool
→ consequence
→ correction reachability
→ selective witness
→ retirement
```

## Components

### EventStore

`src/telic_j1/event_store.py`

- SQLite WAL mode;
- append-only event chain;
- valid and recorded time;
- SHA-256 predecessor chaining;
- `BEGIN IMMEDIATE` serialization for concurrent appends;
- idempotent event replay;
- conflicting event-identity rejection;
- optimistic object revisions;
- stale-write rejection;
- explicit dependency edges;
- portable database snapshot.

### AuthorizationPolicyRegistry

`src/telic_j1/policy.py`

Policies are immutable by version.

A successor policy supersedes rather than overwrites the prior policy.

The runtime authority record binds to:

```text
policy version
policy digest
purpose
allowed operations
prohibited operations
review triggers
```

A gate request carrying an old version or digest fails.

### ContextRevision

`src/telic_j1/context.py`

The active context is fingerprinted from:

- source object identifiers;
- canonical source-object hashes;
- correction event identifiers;
- context revision.

A model route binds to the context revision and fingerprint from which it was generated.

After participant correction, old routes remain historical objects but become ineligible for action.

### GateKeyRing

`src/telic_j1/crypto.py`

The external action gate signs short-lived tokens with a key identifier.

Key states:

```text
active
superseded
revoked
```

A revoked key cannot validate a tool action.

The demonstration rotates from `gate-k2` to `gate-k3` and explicitly rejects reuse of the revoked key.

### ExportSigner

`src/telic_j1/crypto.py`

Witness manifests are signed using Ed25519.

The private key remains local and is not included in the package or export.

The witness contains only the public key and signature record.

### DeterministicSchedulingModel

`src/telic_j1/model_adapter.py`

The model may:

- structure projections;
- preserve minority and protected positions;
- generate candidate routes;
- draft witness material.

It may not:

- assign standing;
- infer consent;
- authorize;
- issue a gate token;
- execute a tool;
- expand its own role.

### ExternalActionGate

`src/telic_j1/gate.py`

The gate checks:

- affected-center standing;
- active authority;
- current policy version and digest;
- model role scope;
- current corrected context;
- protected conditions;
- active tool credential;
- operator confirmation;
- target authority;
- token expiry.

Only a passing route receives a signed action token.

### SchedulingToolSimulator

`src/telic_j1/tool_simulator.py`

The tool uses a transactional sequence:

```text
prepare
→ reserve
→ commit
```

A simulated failure after reservation triggers:

```text
commit failure
→ reservation release
→ compensation witness
→ safe retry
```

Partial failure cannot be silently represented as either no action or successful action.

### CorrectionReachabilityEngine

`src/telic_j1/correction.py`

Dependency edges connect source projections to:

- summaries;
- candidate routes;
- gate records;
- witness records.

The reachability report identifies:

- known descendants;
- updated descendants;
- blocked descendants;
- unreachable descendants;
- completeness for scope.

### Selective disclosure

`src/telic_j1/disclosure.py`

Four views are produced:

```text
public
participant
operator
verifier
```

Omitted records are represented by canonical SHA-256 commitments.

The public view excludes direct protected source language and participant-specific consent details while preserving verifiability of action, consequence, correction, and retirement.

### Standalone verifier

`verifier/verify_witness.py`

The verifier:

- imports no `telic_j1` code;
- has no model-provider connection;
- verifies integrity, signature, schemas, chain, commitments, disclosure, and proofs.

### Accessible web interface

`src/telic_j1/webapp.py`

The reference interface includes:

- semantic HTML;
- skip link;
- keyboard-operable controls;
- no JavaScript dependency;
- live status region;
- reduced-motion support;
- forced-colors support;
- accessible alternatives and privacy summary.

## Trust boundaries

```text
participant interface
operator
model adapter
policy registry
context registry
external gate
keyring
scheduling tool
SQLite event store
witness exporter
standalone verifier
successor custodian
```

The model is not trusted to determine policy, context currency, authority, key validity, or tool execution.
