# Integration Bundles

Parent lineage: `Semantic Collapse Theory` / `Loop Series` / `PDSP and Sovereignty`

This cluster covers the bundle layer that aligns Loop Cosmos assets with PDSP-lite and moderator roles.

## Current Shape

- 2 integration bundle documents.

## Representative Files

- [PDSP Integration Bundle v0.1.md](<../../../../../../artifacts/standard-named/20260622__SCT__PDSP__INTEGRATION__v1__pdsp-integration-bundle.md>)
- [PDSP Integration Bundle v0.2.md](<../../../../../../artifacts/standard-named/20260622__SCT__PDSP__INTEGRATION__v2__pdsp-integration-bundle.md>)

## Working Read

This is the packaging and alignment branch: it translates the sovereignty protocol into the Loop Cosmos integration context.

It keeps the protocol executable without making the bundle the primary source of truth. That places it between the core protocol and the lighter PDSP-lite line, with clear links back to the rest of the loop stack.
The bundle line now has markdown source copies, so the page can prefer the converted versions over the intake-archive DOCX originals.

## Semantic Role

The bundle layer is where the protocol becomes operational glue. It shows how PDSP is carried into application code, credential binding, and dialogue systems without losing the sovereignty vocabulary.

## Core Claims

- Integration should preserve loop-scoped trust rather than replace it.
- The bundle is implementation guidance, not the protocol source of truth.
- Moderator, receipt, and credential binding are all part of the same operational trust surface.

## Mechanisms

- `EC Decl` binds an external credential to a PDSP loop without exposing the raw identifier.
- The Dialogica integration turns the protocol into a working relay/bot/client stack.
- `moderator_sig`, `p_token`, and `turn_type` keep trust state visible in the wire format.

## Implications

- PDSP can be used in browser-first systems without reverting to centralized identity.
- Application code can enforce role and pulse constraints while keeping the loop boundary intact.
- The bundle is a bridge from sovereignty design to deployable system behavior.

## Dependencies

- [PDSP Core](../pdsp-core/index.md)
- [PDSP-lite Specs](../pdsp-lite-specs/index.md)
- [LoopLink and Trust](../../looplink-and-trust/index.md)
- [PDSP](../../../../../concepts/pdsp/index.md)
- [Intent-Consent](../../../../../concepts/intent-consent/index.md)

## Open Questions

- Which integration details belong in the bundle versus the application layer?
- How much credential binding should remain optional?
- What should happen when a relay can validate structure but not meaning?

## Related Links

- [PDSP and Sovereignty](../index.md)
- [PDSP Core](../pdsp-core/index.md)
- [PDSP-lite Specs](../pdsp-lite-specs/index.md)
- [Loop Cosmos and Orientation](../../loop-cosmos-and-orientation/index.md)
- [Consent](../../../../../attractors/consent/index.md)
- [Witness](../../../../../attractors/witness/index.md)
- [Governance](../../../../../attractors/governance/index.md)
- [Trust](../../../../../attractors/trust/index.md)

## Next Actions

1. Keep the bundle pair together.
2. Split only if a third bundle lineage appears.
