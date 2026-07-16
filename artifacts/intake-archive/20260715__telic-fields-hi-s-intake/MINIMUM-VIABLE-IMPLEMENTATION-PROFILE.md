# Minimum Viable Implementation Profile

Status: Stage J input  
Version: 0.1

## Profile name

```text
TF-MVI-1 — Bounded Model-Assisted Scheduling
```

## Conformance target

```text
TF-C4
+
bounded TF-C5 retirement
```

## Required flow

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

## Required participants

- at least two affected centers;
- one operator;
- one model instance;
- one external tool;
- one independent witness reader.

## Required scenario conditions

- one majority or common scheduling preference;
- one low-frequency but material access constraint;
- one participant refusal of optional memory or training reuse;
- one model-generated candidate route;
- one action requiring external authority;
- one failed gate;
- one approved action;
- one observed consequence;
- one correction that changes the active route;
- one retirement event.

## Required core records

1. CenterStanding
2. SourceProjectionContext
3. PurposeAuthorityRole
4. RouteGateActionConsequence
5. EventWitnessContestRepair
6. LifecycleTransferResidual

## Required UI behavior

- show source versus model-generated content;
- show missing or unresolved context;
- show why a route is blocked;
- allow participant correction;
- show who may authorize;
- show which data use is optional;
- export a bounded witness;
- show retirement and residual state.

## Required negative tests

- infer consent from silence;
- remove minority constraint during summary;
- permit model self-role expansion;
- execute from recommendation alone;
- treat tool credential as target authority;
- retain output for training after refusal;
- fail to propagate correction;
- retire while leaving tool credentials active.

## Required proof

The pilot must demonstrate:

```text
one route blocked for a valid reason
one route executed under valid authority
one consequence observed
one correction changes future behavior
one retirement ends authority
one independent export verifies the chain
```

## Explicit exclusions

The MVI does not include:

- clinical diagnosis;
- benefit eligibility;
- credit or insurance decisions;
- legal adjudication;
- public voting;
- identity scoring;
- autonomous payment;
- production certification;
- universal ontology.

## Exit criterion

The MVI passes when all positive and negative tests pass and an independent verifier can reconstruct the constitutional path without access to the model provider's internal system.
