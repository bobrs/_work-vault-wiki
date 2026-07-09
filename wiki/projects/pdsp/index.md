# PDSP

This project collects the Personal Data Sovereignty Protocol as a top-level branch of the wiki.

It is the project-facing entry point for the sovereignty substrate: the core protocol, the PDSP-lite spec line, and the integration bundles now read as one project family rather than only as a nested SCT seam.

## Semantic Role

This project is the wiki entry point for the PDSP trust model. It sits above the detailed SCT lineage so readers can enter the work as a project, not just as a protocol fragment.

The project page should explain why PDSP matters: it is the surface where subjective trust graphs, loop-scoped identity, witness structure, and consent-bearing transport become one sovereignty problem.

## Current Shape

- 1 top-level project landing page.
- 1 nested SCT branch that carries the full protocol family.
- 3 subfamilies inside that branch: core, PDSP-lite specs, and integration bundles.

## Core Claims

- Trust is local, situational, and auditable.
- Identity should be loop-scoped instead of globally persistent.
- Consent, witness, and recovery belong to the protocol surface.
- Interoperability only matters if the sovereignty model stays legible.

## Mechanisms

- `HumanKey` establishes the initial trust relationship.
- `LoopLink` carries presence and transport semantics.
- `Abracadabradoo` carries receipts, declarations, and witness roles.
- The PDSP-lite specs reduce the model to a minimal interoperable packet surface.
- The integration bundles translate the model into application-facing behavior.

## Implications

- The project can support civic, medical, AI-human, and private contracting use cases without changing the core trust vocabulary.
- Readers can move from project-level meaning into protocol-level detail without losing the thread.
- The wiki can treat PDSP as a durable project family rather than a single spec artifact.

## Primary Pages

- [PDSP and Sovereignty](../semantic-collapse-theory/loop-series/pdsp-and-sovereignty/index.md)
- [PDSP Core](../semantic-collapse-theory/loop-series/pdsp-and-sovereignty/pdsp-core/index.md)
- [PDSP-lite Specs](../semantic-collapse-theory/loop-series/pdsp-and-sovereignty/pdsp-lite-specs/index.md)
- [Integration Bundles](../semantic-collapse-theory/loop-series/pdsp-and-sovereignty/integration-bundles/index.md)

## Working Read

PDSP is the project where subjective trust graphs, loop-scoped identity, and consent-bearing transport are modeled together.

The project now sits high enough in the wiki that readers do not have to start from the concept page or from the SCT loop series. They can enter directly from Projects, then branch into the deeper protocol pages as needed.
The project page should remain a meaning-first entry point, while the nested SCT branch stays the detailed source of record.

## Dependencies

- [PDSP](../../concepts/pdsp/index.md)
- [LoopLink](../../concepts/looplink/index.md)
- [Intent-Consent](../../concepts/intent-consent/index.md)
- [Witnessing](../../concepts/witnessing/index.md)
- [Governance Diad](../../concepts/governance-diad/index.md)
- [Abracadabracadoo](../../concepts/abracadabracadoo/index.md)

## Open Questions

- Which PDSP surface should be considered the project-level public entry point versus the protocol-level source of record?
- How far should the project page expand before it starts duplicating the nested SCT branch?
- When does a PDSP variant become durable enough to deserve its own project subtree?

## Related Concepts

- [PDSP](../../concepts/pdsp/index.md)
- [LoopLink](../../concepts/looplink/index.md)
- [Intent-Consent](../../concepts/intent-consent/index.md)
- [Witnessing](../../concepts/witnessing/index.md)
- [Governance Diad](../../concepts/governance-diad/index.md)

## Attractor Bridge

- [Consent](../../attractors/consent/index.md)
- [Witness](../../attractors/witness/index.md)
- [Provenance](../../attractors/provenance/index.md)
- [Trust](../../attractors/trust/index.md)

## Notes

- This is a project page, not a canon claim.
- Keep the SCT branch as the detailed lineage source of record.
- Use this page as the direct project entry point for PDSP work.
- Prefer the project page for orientation and the nested branch for protocol detail.
