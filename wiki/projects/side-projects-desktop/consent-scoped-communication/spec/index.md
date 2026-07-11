# Substrate Specification

This page compresses the consent-scoped communication substrate specification.

## Source Artifact

- Source role: `standard_named_source`
- Inbound original: [consent_scoped_communication_substrate_canonical_specification.md](<../../../../../artifacts/intake-archive/20260710__consent-scoped-communication-intake/consent_scoped_communication_substrate_canonical_specification.md>)
- Standard-named source: [20260710__SIDE-PROJECTS-DESKTOP__SPEC__CONSENT-SCOPED-COMMUNICATION__v1__consent-scoped-communication-substrate.md](<../../../../../artifacts/standard-named/20260710__SIDE-PROJECTS-DESKTOP__SPEC__CONSENT-SCOPED-COMMUNICATION__v1__consent-scoped-communication-substrate.md>)

## Working Read

The specification makes scope explicit at the message level. Content and scope travel together, and privacy/security/moderation/compliance become enforcement layers rather than separate communication systems.
The incoming spec clarifies the architecture more sharply: the same protocol ladder covers public, normative, group, private, and secure contexts, while the actual enforcement mechanism can vary without changing message semantics.

## Core Claim

Communication can share one substrate across public, group, private, and secure contexts if scope is first-class and transitions are explicit.
That makes the substrate useful not just for human collaboration, but for machine-readable intent, scoped memory, and reversible authorization.

## Key Ideas

- Scoped utterance.
- Handshake ladder.
- Scope refinement.
- Semantics separate from enforcement.
- AI must respect declared scope.
- Handshake ladder.
- Simulation-first validity.
- Hyper-secure compatibility.

## Related Pages

- [Consent-Scoped Communication](../index.md)
- [Reference Implementation](../implementation/index.md)
- [One Protocol. Every Conversation.](../overview/index.md)
- [AI Readiness / Machine-Readable Intent](../ai-readiness/index.md)
- [Consent Grammar](../../consent-grammar/index.md)
- [Witness-to-Witness Messaging Protocol](../../../../concepts/witness-to-witness-messaging/index.md)
- [WitnessKey](../../../witnesskey/index.md)
- [Trust Interoperability Standard](../../../trust-interoperability-standard/index.md)
- [Quantum Invariants](../../../quantum-invariants/index.md)

## Attractor Bridge

- [Consent](../../../../attractors/consent/index.md)
- [Governance](../../../../attractors/governance/index.md)
- [Trust](../../../../attractors/trust/index.md)
- [Meaning](../../../../attractors/meaning/index.md)
- [Witness](../../../../attractors/witness/index.md)
- [Grounding](../../../../attractors/grounding/index.md)

## Notes

- This is a source-anchored protocol note, not a canon claim.
- Keep enforcement and semantics distinct.
