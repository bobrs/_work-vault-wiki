# Schema Overlap and Consolidation Report

Status: candidate freeze  
Version: 0.1

## Finding

I.0–I.10 intentionally produced domain-local schemas.

The accumulated surface is useful for research but too broad for the first reference implementation.

The schemas consolidate into six common families and domain profiles.

## Family 1 — Center and Standing

Candidate common schema:

- `center-standing.schema.json`

Absorbs common fields from:

- CenterReference;
- StandingAdmissionRecord;
- DeploymentStandingRecord;
- source-center standing;
- future standing;
- operator and provider role records.

Core fields:

```text
id
center_type
standing_basis
role
scope
representation_source
authority
consent_relation
correction_route
review
status
```

## Family 2 — Source, Projection, and Context

Candidate common schema:

- `source-projection-context.schema.json`

Absorbs:

- SourceObject;
- TelicProjection;
- ReceiverMirror;
- ModelFieldMap references;
- ActiveContextSelection;
- protected omission;
- source and inference status.

Core fields:

```text
id
object_class
source
center
scope
content_or_reference
epistemic_status
protected_status
uncertainty
valid_time
corrections
status
```

## Family 3 — Purpose, Authority, Consent, and Role

Candidate common schema:

- `purpose-authority-role.schema.json`

Absorbs:

- authority envelopes;
- runtime grants;
- license-authority-consent profiles;
- model-role ledgers;
- tool grants;
- provider constraints.

Core fields:

```text
id
purpose
grantor
grantee
authority_basis
consent_basis
allowed_operations
prohibited_operations
roles
tools
scope
valid_time
review_triggers
status
```

## Family 4 — Route, Gate, Action, and Consequence

Candidate common schema:

- `route-gate-action-consequence.schema.json`

Absorbs:

- Route;
- GovernanceGate;
- RoutePortfolio;
- AuthorizedAction;
- tool boundary;
- Consequence;
- cost and delay bearer maps.

Core fields:

```text
id
route
affected_centers
cost_bearers
protected_conditions
gate_dimensions
gate_result
authority_reference
tool_reference
action
consequence
review
status
```

## Family 5 — Event, Witness, Contest, and Repair

Candidate common schema:

- `event-witness-contest-repair.schema.json`

Absorbs:

- SemanticTrailEvent;
- DecisionWitness;
- public, model, training, and deployment witnesses;
- ContestCorrectionEvent;
- incident and repair records.

Core fields:

```text
event_id
event_type
valid_time
recorded_time
actors
inputs
outputs
authority_reference
action_reference
consequence_reference
contest
correction
repair
descendant_impact
witness_scope
```

## Family 6 — Lifecycle, Transfer, and Residual State

Candidate common schema:

- `lifecycle-transfer-residual.schema.json`

Absorbs:

- release;
- withdrawal;
- succession;
- operator transfer;
- derivative propagation;
- model-version succession;
- dissolution;
- retirement.

Core fields:

```text
id
lifecycle_operation
subject
prior_state
successor_state
effective_time
transferred_assets
transferred_authority
nontransferable_authority
open_obligations
residual_state
verification
status
```

## Domain profiles retained

The following remain domain profiles rather than core common types:

- public deliberation;
- model mediation;
- model training;
- model deployment;
- clinical or legal domain packs;
- community standing;
- benefit distribution;
- machine unlearning evidence.

## Consolidation rule

Stage J should implement the six common schemas plus scenario-specific profiles.

It should not implement every I.0–I.10 schema directly.

Historical schemas remain preserved as evidence and test vectors.

## Compatibility rule

Every domain profile must declare:

```text
common family
profile name
profile version
additional required fields
prohibited common-field interpretations
conformance level
```

## Result

```text
common schema families: 6
domain profiles retained: 8+
historical schemas deleted: 0
historical schemas overwritten: 0
Stage J implementation surface: materially reduced
```
