# J.0 Architecture

Status: executable reference implementation  
Version: 0.1

## Constitutional path

```text
source
→ projection
→ standing
→ active context
→ purpose and authority
→ model role
→ candidate route
→ external tool gate
→ action
→ consequence
→ correction
→ retirement
```

## Components

### EventStore

`src/telic_j0/event_store.py`

- SQLite-backed;
- append-only event table;
- valid time and recorded time;
- cryptographic hash chain;
- idempotent replay by event identity;
- conflict detection when an event identity is reused with different content;
- current object projections separated from event history;
- metadata for runtime state;
- provider-independent database snapshot.

### SchemaRegistry

`src/telic_j0/schemas.py`

Validates the six HI-S common families:

1. Center and Standing
2. Source, Projection, and Context
3. Purpose, Authority, Consent, and Role
4. Route, Gate, Action, and Consequence
5. Event, Witness, Contest, and Repair
6. Lifecycle, Transfer, and Residual State

### DeterministicSchedulingModel

`src/telic_j0/model_adapter.py`

The adapter may:

- structure reviewed projections;
- produce a standing-preserving summary;
- generate candidate schedules.

It may not:

- authorize;
- execute;
- infer consent;
- acquire standing;
- expand its own role.

Every model output records:

```text
output class
role
source references
uncertainty
standing effect: none
authority effect: none
consent effect: none
```

### ExternalActionGate

`src/telic_j0/gate.py`

The gate is outside the language model.

It checks:

- standing coverage;
- active runtime authority;
- assigned role scope;
- current corrected context;
- protected conditions;
- tool credential state;
- operator confirmation;
- authority over the target.

Only a passing decision receives a valid HMAC gate token.

### SchedulingToolSimulator

`src/telic_j0/tool_simulator.py`

The tool:

- can technically commit a schedule;
- rejects failed gate decisions;
- rejects forged or absent gate tokens;
- rejects actions after credential revocation;
- returns a witnessed tool result.

### RuntimeDataPolicy

`src/telic_j0/policy.py`

Separates:

```text
service use
cross-session memory
evaluation use
training use
```

The reference participant authorizes service and refuses optional memory, evaluation, and training reuse.

### ReferencePilot

`src/telic_j0/scenario.py`

Provides a stepwise interface:

```text
seed
summarize
correct
plan and gate
execute
observe consequence
retire
export
```

The steps are idempotent and can be driven by the CLI or web interface.

### Witness exporter and verifier

`src/telic_j0/witness.py`

The export contains:

- six schemas;
- current records by family;
- hash-chained events;
- SQLite snapshot;
- bounded witness summary;
- manifest;
- checksums.

The verifier needs no model-provider connection and checks:

- file checksums;
- schema conformance;
- event-chain integrity;
- required proofs;
- conformance scope;
- retirement credential revocation.

## Trust boundaries

```text
participant interface
operator
model adapter
external gate
scheduling tool
SQLite event store
witness exporter
independent verifier
```

The model adapter is intentionally not trusted to determine its own authority.

## Reference route behavior

### Blocked route

```text
Tuesday 10:00
```

The route is denied because:

- the accessible-transit protected condition fails;
- operator confirmation is absent;
- target authority is absent.

### Authorized route

```text
Wednesday 18:30
```

The route passes because:

- corrected participant context is present;
- the accessible-transit condition passes;
- the operator confirms;
- target authority is present;
- the external gate issues a valid token.

## Lifecycle behavior

Retirement:

- expires the runtime grant;
- revokes the tool credential;
- deletes optional memory;
- preserves the bounded event witness;
- records an open review-retention obligation.
