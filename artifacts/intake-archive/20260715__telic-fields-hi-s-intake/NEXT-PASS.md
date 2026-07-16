# Next Pass

# J.0 — Reference Implementation and Pilot Harness

## Objective

Build a local-first, inspectable reference implementation of:

```text
TF-MVI-1 — Bounded Model-Assisted Scheduling
```

## Conformance target

```text
TF-C4
+
bounded TF-C5 retirement
```

## Required implementation components

1. event store with valid and recorded time;
2. six consolidated schema families;
3. participant projection and correction interface;
4. model adapter with role and output classes;
5. external governance and tool gate;
6. scheduling-tool simulator;
7. consequence-return and repair path;
8. retirement and residual-state path;
9. provider-independent witness exporter;
10. independent verifier and adversarial test harness.

## Required runtime proof

```text
one invalid route blocked
one valid route executed
one consequence observed
one participant correction propagated
one retirement event revokes authority
one independent verifier reconstructs the chain
```

## Required negative tests

- source laundering;
- standing exclusion;
- context collapse;
- authority laundering;
- consent expansion;
- model-role escalation;
- tool-token overreach;
- correction suppression;
- witness capture;
- lifecycle obligation loss.

## Recommended technology boundary

- local-first web application;
- SQLite or equivalent append-only event store;
- JSON Schema validation;
- deterministic simulated scheduling tool;
- optional model adapter with a deterministic fallback;
- no production personal data;
- signed or checksummed ZIP witness export;
- command-line verifier.

## J.0 completion gate

J.0 passes only if:

- the external action gate, not the model, controls execution;
- participant correction changes the active route;
- optional runtime data reuse can be refused;
- the failed gate is preserved in the witness;
- retirement revokes tool authority;
- the export verifies independently of the provider;
- the implementation claims only the declared conformance scope.
