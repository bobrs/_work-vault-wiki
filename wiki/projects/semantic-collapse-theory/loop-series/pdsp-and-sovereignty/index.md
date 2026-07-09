# PDSP and Sovereignty

Parent lineage: `Semantic Collapse Theory` / `Loop Series`

This cluster covers the personal data sovereignty protocol, its LoopLink-based variant, the integration bundles, and the evolving PDSP-lite specifications.

## Current Shape

- 7 PDSP and sovereignty documents.
- 3 nested lineage pages organize those documents.

## Nested Lineage Pages

- [PDSP Core](pdsp-core/index.md)
- [Integration Bundles](integration-bundles/index.md)
- [PDSP-lite Specs](pdsp-lite-specs/index.md)

## Representative Files

- [PDSP Core / personal-data-sovereignty-protocol.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__CORE__v1__personal-data-sovereignty-protocol.md>)
- [PDSP Core / personal-data-sovereignty-protocol-looplink-based-architecture.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__CORE__v2__personal-data-sovereignty-protocol-looplink-based-architecture.md>)
- [PDSP-lite Specs / pdsp-lite-specification v0.1.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v1__pdsp-lite-specification.md>)
- [PDSP-lite Specs / pdsp-lite-specification v0.2.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v2__pdsp-lite-specification.md>)
- [PDSP-lite Specs / pdsp-lite-specification v0.3.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__LITE__SPEC__v3__pdsp-lite-specification.md>)
- [Integration Bundles / pdsp-integration-bundle v0.1.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__INTEGRATION__v1__pdsp-integration-bundle.md>)
- [Integration Bundles / pdsp-integration-bundle v0.2.md](<../../../../../artifacts/standard-named/20260622__SCT__PDSP__INTEGRATION__v2__pdsp-integration-bundle.md>)

## Working Read

This branch now separates into the core sovereignty protocol, the integration bundles, and the PDSP-lite spec line. The split follows the document titles closely and keeps the implementation path visible.

It is the sovereignty branch of the loop series. The documents here hold the protocol core, the bundle-level application layer, and the lighter spec line that makes the branch easier to carry forward.

The broader semantic role of this branch is to treat PDSP as a sovereignty attractor rather than a single spec family. It is the place where personal data, trust, and subjective auditability are organized into a loop-based trust model.

Because PDSP depends on LoopLink transport and touches the governance logic of SCT, it is one of the main bridges between the loop stack and the origin/governance material.
The core manuscript pair now has markdown source copies in `artifacts/standard-named/`, so this branch can prefer markdown for the main protocol reading while leaving the remaining spec and bundle line items in archive form for now.
The PDSP-lite specs and integration bundles now have markdown source copies as well, which makes the branch fully indexed across the core, transport, and implementation layers.

## Semantic Role

This branch is the source of the protocol family as a whole. It separates the sovereignty substrate, the packet-level spec, and the integration bundles while keeping them tied to the same trust problem.

The important move is not just versioning. It is that the documents show the same sovereignty idea at three scales: protocol core, minimal interoperability surface, and integration packaging.

## Core Claims

- Trust should be auditable without becoming centralized.
- Loop-scoped identity is more useful here than persistent global identity.
- Packet-level interoperability is only meaningful if the trust loop remains legible.
- The core and the implementation layers are different expressions of the same sovereignty model.

## Mechanism Stack

- `PDSP Core` names the subjective trust graph and the sovereignty substrate.
- `PDSP-lite Specs` define the minimal packet and validation surface.
- `Integration Bundles` translate the protocol into application-facing dialogue and bridge context.
- `LoopLink` provides the transport and presence layer beneath the rest of the branch.

## Implications

- Readers can move from theory to implementation without changing the trust vocabulary.
- The branch can support both protocol exploration and concrete system design.
- Civic, medical, and AI-human use cases all remain downstream of the same sovereignty pattern.

## Dependencies

- [PDSP](../../../../concepts/pdsp/index.md)
- [LoopLink](../../../../concepts/looplink/index.md)
- [Intent-Consent](../../../../concepts/intent-consent/index.md)
- [Witnessing](../../../../concepts/witnessing/index.md)
- [Governance Diad](../../../../concepts/governance-diad/index.md)
- [Abracadabracadoo](../../../../concepts/abracadabracadoo/index.md)
- [PDSP Core](pdsp-core/index.md)
- [PDSP-lite Specs](pdsp-lite-specs/index.md)
- [Integration Bundles](integration-bundles/index.md)

## Open Questions

- How do protocol variants preserve coherence across the shared trust vocabulary?
- What revocation or decay semantics should be surfaced centrally?
- How much witness structure belongs in the substrate versus the bundle layer?
- Can loop states be migrated without weakening provenance?

## Related Concepts

- [PDSP](../../../../concepts/pdsp/index.md)
- [LoopLink](../../../../concepts/looplink/index.md)
- [POLEMEMELOP](../../../../concepts/polememelop/index.md)

## Related Links

- [Loop Series](../index.md)
- [LoopLink and Trust](../looplink-and-trust/index.md)
- [Origin and Governance](../../origin-and-governance/index.md)
- [Loop Economy Series](../loop-economy-series/index.md)
- [Consent](../../../../attractors/consent/index.md)
- [Witness](../../../../attractors/witness/index.md)
- [Provenance](../../../../attractors/provenance/index.md)
- [Trust](../../../../attractors/trust/index.md)

## Next Actions

1. Keep the three nested lineage pages stable.
2. Split again only if one of the three tracks develops another durable seam.
