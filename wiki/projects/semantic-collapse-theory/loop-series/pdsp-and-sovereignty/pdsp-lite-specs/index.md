# PDSP-lite Specs

Parent lineage: `Semantic Collapse Theory` / `Loop Series` / `PDSP and Sovereignty`

This cluster covers the minimal interoperable packet format and onboarding profiles for PDSP-lite.

## Current Shape

- 3 PDSP-lite specification documents.

## Representative Files

- [PDSP-lite Specification v0.1.md](<../../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v1__pdsp-lite-specification.md>)
- [PDSP-lite Specification v0.2.md](<../../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v2__pdsp-lite-specification.md>)
- [PDSP-lite Specification v0.3.md](<../../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v3__pdsp-lite-specification.md>)

## Working Read

This is the implementation-facing line: a minimal packet header surface, then incremental onboarding and exchange profiles.

It is the narrowest operational expression of the PDSP branch, so it should stay linked to the core protocol, the bundle layer, and the LoopLink transport layer.
The spec line now has markdown source copies, so this page can prefer the converted text over the intake-archive DOCX originals.

## Semantic Role

This cluster narrows PDSP into the smallest interoperable surface that still preserves loop identity, pulse validation, and witnessable receipt.

It is the place where the trust model becomes machine-checkable. The fields are not arbitrary metadata; they are the minimum structure required to keep presence, consent, and provenance attached to the exchange.

## Core Claims

- Interoperability needs a stable header surface.
- Pulse-based validation is part of sovereignty, not just transport housekeeping.
- A packet can carry consent and witness structure without carrying a global identity.

## Mechanisms

- `loop_id` defines the loop boundary.
- `pulse_n` acts as the ratcheting epoch.
- `participants` and `roles` keep the loop locally legible.
- `moderator_sig` and `p_token` make validation and receipt explicit.
- `participants_delta`, `turn_type`, and `loop://exchange` extend the same surface into multi-party and onboarding contexts.

## Implications

- The packet becomes a consent-bearing unit, not just a message envelope.
- Roles can be introduced without central registries.
- Human-friendly onboarding stays compatible with protocol rigor.

## Dependencies

- [PDSP Core](../pdsp-core/index.md)
- [PDSP and Sovereignty](../index.md)
- [Integration Bundles](../integration-bundles/index.md)
- [LoopLink and Trust](../../looplink-and-trust/index.md)
- [Intent-Consent](../../../../../concepts/intent-consent/index.md)

## Open Questions

- How should tools handle invalid or stale pulse states in practice?
- What is the boundary between role semantics and external policy?
- When should onboarding profiles be treated as optional versus required?

## Related Links

- [PDSP and Sovereignty](../index.md)
- [PDSP Core](../pdsp-core/index.md)
- [Integration Bundles](../integration-bundles/index.md)
- [LoopLink and Trust](../../looplink-and-trust/index.md)
- [Consent](../../../../../attractors/consent/index.md)
- [Trust](../../../../../attractors/trust/index.md)

## Next Actions

1. Keep the PDSP-lite spec line stable.
2. Split only if a new version family becomes durable enough for its own page.
