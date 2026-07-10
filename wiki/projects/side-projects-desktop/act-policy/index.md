# ACT–POLICY Seed Crystal

This branch collects the ACT–POLICY substrate and its worked examples.

It is a provisional protocol-family branch, not a concept declaration. The material defines a minimal substrate for consent-bound meaning systems: what can happen, how it is allowed, who may verify it, and how shared state evolves.

At the project level, ACT–POLICY is the executable edge of the consent grammar. It sits between intention and permission, and it keeps witness, policy, and state separate enough to stay legible when the branch is reused across other protocols.

## Nested Lineage Pages

- [Spec](spec/index.md)
- [Worked Examples](worked-examples/index.md)

## Representative Files

- [ACT–POLICY Seed Crystal v0.1.md](<../../../../artifacts/standard-named/20260710__SIDE-PROJECTS-DESKTOP__SPEC__ACT-POLICY__v0-1__act-policy-seed-crystal.md>) · [archive copy](<../../../../artifacts/intake-archive/20260710__act-policy-intake/act_policy_seed_crystal_v_0.md>)
- [ACT–POLICY Seed Crystal v0.1 — Worked Examples.md](<../../../../artifacts/standard-named/20260710__SIDE-PROJECTS-DESKTOP__WORKED-EXAMPLES__ACT-POLICY__v0-1__act-policy-worked-examples.md>) · [archive copy](<../../../../artifacts/intake-archive/20260710__act-policy-intake/act_policy_seed_crystal_v_0 (1).md>)

## Working Read

The substrate is intentionally sparse: ACT names an attempted semantic transformation, POLICY decides whether it is allowed, WITNESS verifies and records the evaluation, and STATE changes only through accepted acts. That makes the family useful as a compact machinery layer rather than as a general philosophy.

The worked examples show the same machinery in motion, including consent policy setup, witness overlays, readback, and a Dialogica mapping that demonstrates how the substrate can support mediation without inventing new primitives.

The useful pattern is not only what the branch can do, but what it refuses to blur. An act is not the same thing as a policy, witness is not the same thing as permission, and state is not the same thing as intent. That separation is why the branch can travel cleanly into consent, governance, witness, and loop-based systems without becoming generic process language.

In practice, this branch should be read as a field atlas for machine-readable legitimacy: if a move is going to alter a shared system, ACT–POLICY describes the minimum grammar needed to explain why that move was accepted, rejected, or left pending.

## Semantic Role

- Act names the attempted move.
- Policy names the admissibility rule.
- Witness names the record of evaluation.
- State names the resulting shared condition.
- Consent names the boundary that keeps the sequence legitimate.
- Governance names the constraint system that can carry the sequence forward.

## Attractor Bridge

- [Consent](../../../../attractors/consent/index.md)
- [Governance](../../../../attractors/governance/index.md)
- [Witness](../../../../attractors/witness/index.md)
- [Loop Mechanics](../../../../attractors/loop-mechanics/index.md)
- [Provenance](../../../../attractors/provenance/index.md)
- [Trust](../../../../attractors/trust/index.md)

## Related Links

- [Side Projects Desktop](../index.md)
- [Witnessing](../../../../concepts/witnessing/index.md)
- [Governance Diad](../../../../concepts/governance-diad/index.md)
- [Consent Physics](../../../../concepts/consent-physics/index.md)
- [Intent-Consent](../../../../concepts/intent-consent/index.md)
- [LOOPtLOOP](../../../../concepts/looptloop/index.md)
- [WitnessKey](../../witnesskey/index.md)
- [Trust Interoperability Standard](../../trust-interoperability-standard/index.md)

## Next Actions

1. Keep the spec and worked examples together unless a stronger seam appears.
2. Add new child pages only if the substrate develops a second durable branch.
3. Route future policy/witness examples here if they genuinely reuse this primitive set.
4. Expand the attractor bridge only when a link carries explanatory weight, not just adjacency.
