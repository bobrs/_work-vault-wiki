# LOOPtLOOP

This project collects the public witness and provenance surface around LOOPtLOOP.

It is the top-level project entry for the hash-only authorization, witness receipt, and live provenance loop family now exposed at `looptloop.online`.

## Semantic Role

This project is the public contract surface for LOOPtLOOP. It is where the wiki treats hash-only authorization, bounded witness, and provenance loops as a real project rather than only a concept or historical artifact cluster.

The important distinction is that this page points at a live machine-readable public system, while the concept page explains the meaning of the term. The project page should stay oriented toward deployment, public contract, and supported lineage.

## Current Shape

- 1 top-level project landing page.
- 1 public machine-readable surface.
- 3 legacy branches that now act as supporting lineage: CICP access, WitnessKey, and the archived patent companions.

## Public Surface

- [Public site](https://looptloop.online/)
- [Machine-readable summary](https://looptloop.online/llms.txt)
- [API base](https://api.looptloop.online/v0)
- [Public repository](https://github.com/bobrs/LOOPtLOOP)

## Core Claims

- Private payload stays private.
- Witness is bounded and hash-first.
- Consent envelopes and provenance signals can be public without exposing the underlying payload.
- The public surface is narrow on purpose and should not be inflated into a broader identity claim.

## Mechanisms

- Hash locally before witness.
- Verify receipts and status explicitly before reliance.
- Use provenance loops for visible recording claims.
- Keep the public contract machine-readable so downstream tooling can consume it safely.

## Implications

- The project can be entered from Projects without knowing the historical patent lineage first.
- The wiki can treat LOOPtLOOP as a current public project surface, not only a historical acronym.
- CICP, WitnessKey, and the patents branch remain supporting lineages rather than the primary entry point.

## Primary Pages

- [LOOPtLOOP](../../concepts/looptloop/index.md)
- [Implementation and Access](../consent-intent-compression-protocol/implementation-and-access/index.md)
- [Pairing and Field Access](../consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/index.md)
- [Field Pairing and Consent Loop](../consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/field-pairing-and-consent-loop/index.md)
- [Field Infrastructure Applications](../consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/field-infrastructure-applications/index.md)
- [WitnessKey](../witnesskey/index.md)
- [Platform and Field Applications](../patents/platform-and-field-applications/index.md)

## Working Read

LOOPtLOOP is the project where hash-only witness, consent envelopes, and provenance loops become a public surface with a machine-readable contract.

The project now sits alongside the other top-level wiki projects, so readers can enter from Projects and then move down into the CICP, WitnessKey, or patents branches depending on whether they want access, authorization, or historical lineage.

The public contract is intentionally narrow: it witnesses hashes, preserves private payload boundaries, and makes provenance visible without claiming more than the API supports.

## Dependencies

- [LOOPtLOOP](../../concepts/looptloop/index.md)
- [Witnessing](../../concepts/witnessing/index.md)
- [Intent-Consent](../../concepts/intent-consent/index.md)
- [Governance Diad](../../concepts/governance-diad/index.md)
- [LoopLink](../../concepts/looplink/index.md)
- [Consent–Intent Compression Protocol (CICP)](../consent-intent-compression-protocol/index.md)
- [WitnessKey](../witnesskey/index.md)
- [Platform and Field Applications](../patents/platform-and-field-applications/index.md)

## Open Questions

- How far should the public witness contract expand before it stops being LOOPtLOOP?
- Which provenance claims belong on the public surface versus in supporting lineages?
- When does a legacy companion become a separate project rather than an archived branch?

## Related Concepts

- [LOOPtLOOP](../../concepts/looptloop/index.md)
- [Witnessing](../../concepts/witnessing/index.md)
- [Intent-Consent](../../concepts/intent-consent/index.md)
- [Governance Diad](../../concepts/governance-diad/index.md)
- [LoopLink](../../concepts/looplink/index.md)

## Attractor Bridge

- [Consent](../../attractors/consent/index.md)
- [Witness](../../attractors/witness/index.md)
- [Provenance](../../attractors/provenance/index.md)
- [Trust](../../attractors/trust/index.md)

## Notes

- This is a project page, not a canon claim.
- Keep the public site, concept page, and supporting branches consistent with the same bounded witness contract.
- Treat `looptloop.online` as the live public surface for the project.
