# Witness-to-Witness Messaging Protocol

Working definition: a consent-bounded message transport where meaning travels with declared boundaries, and intermediaries are limited to carrying or enforcing those boundaries rather than rewriting them.

The incoming draft is useful because it treats communication as witness work instead of content transport alone. The core move is simple: humans declare consent, AI enforces declared constraints, and platforms remain transport layers. That makes the protocol a clean neighbor to consent-scoped communication, witness practice, and machine-readable intent.

In the wiki, this page should stay honest about scope. It is a protocol concept, not a universal communication truth. Its value is that it keeps intent, sensitivity, distribution, and derivatives attached to the message so the system can refuse misuse without inventing new permissions.
It sits next to shared persistence because both are about keeping state legible without forcing immediate action.
It also belongs near [Witness Infrastructure](../witness-infrastructure/index.md) because message-level witness only stays trustworthy when the surrounding continuity layer can carry the state forward without reinterpreting it.

## Protocol Surfaces

- Intent cascade: why the message is being shared.
- Sensitivity cascade: what must never be done with it.
- Distribution cascade: who may receive or forward it.
- Witness header: a human-readable, machine-parseable consent declaration.
- AI steward: a non-authoritative agent that enforces the declared boundary.

## Related Artifacts

- [Witness-to-Witness Messaging Protocol (Draft v0.1)](<../../../artifacts/incoming/witness_to_witness_messaging_protocol_draft_v_0.md>)

## Related Pages

- [Consent-Scoped Communication](../../projects/side-projects-desktop/consent-scoped-communication/index.md)
- [Substrate Specification](../../projects/side-projects-desktop/consent-scoped-communication/spec/index.md)
- [Intent-Consent](../intent-consent/index.md)
- [Witnessing](../witnessing/index.md)
- [Governance Diad](../governance-diad/index.md)
- [Consent Physics](../consent-physics/index.md)
- [AI Did Not Break Consent](../ai-did-not-break-consent/index.md)
- [Shared Persistence as a Coordination Primitive](../shared-persistence-as-a-coordination-primitive/index.md)
- [WitnessKey](../../projects/witnesskey/index.md)
- [Trust Interoperability Standard](../../projects/trust-interoperability-standard/index.md)
- [Quantum Invariants](../../projects/quantum-invariants/index.md)
- [Consentful Cybernetics](../../projects/consentful-cybernetics/index.md)
- [Witness Infrastructure](../witness-infrastructure/index.md)
- [LoopLink](../looplink/index.md)

## Attractor Bridge

- [Consent](../../attractors/consent/index.md)
- [Witness](../../attractors/witness/index.md)
- [Governance](../../attractors/governance/index.md)
- [Trust](../../attractors/trust/index.md)
- [Meaning](../../attractors/meaning/index.md)
- [Agency](../../attractors/agency/index.md)

## Notes

- This is a protocol concept, not a canon declaration.
- Keep scope and enforcement separate from message semantics.
- Revisit if a second protocol family makes the same boundary model durable.
