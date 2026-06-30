# Hierarchical Key Derivation

Parent lineage: `Consent–Intent Compression Protocol (CICP)` / `Implementation and Access` / `Key Derivation and Decryption`

This page isolates the key-tree side of the cryptographic access layer: deterministic hierarchy, identity structure, and the BIP-32-style derivation model.

It is the identity-seeding seam of the cryptographic branch. The document here defines how access roots are arranged before selective decryption decides what can be seen.

## Current Shape

- 1 key derivation document.

## Representative Files

- [Hierarchical Key Derivation in Loop-Based Systems (BIP-32 Integration).docx](<../../../../../../artifacts/intake-archive/20260622__consent-crystal-structure-research-intake/Consent–Intent Compression Protocol (CICP)/Hierarchical Key Derivation in Loop-Based Systems (BIP-32 Integration).docx>)

## Working Read

This branch covers the key tree and identity hierarchy, not the retrieval policy. It is the structure that selective decryption depends on.

The BIP-32 integration material belongs here because it describes how keys are derived in a repeatable hierarchy that can later be used for scoped access.

## Core Claim

Identity and access become manageable when they are derived instead of improvised. A deterministic key tree lets the protocol keep one root while still creating many scoped branches for loop identities, session encryption, or relationship-specific memory.

## Mechanisms

- A single root seed can generate a hierarchy of child keys.
- A path can encode site, ritual, participant, and time.
- Hardened branches can protect privacy between derivation zones.
- The same tree can support symbolic memory, session keys, and token derivation.

## Terminology

- Root seed: the top-level source from which branches are derived.
- Derivation path: the symbolic address of a key branch.
- Hardened path: a boundary that blocks certain forms of derivation leakage.
- Symbolic memory path: a path used to index a meaningful event or relation.

## Implications

This page is where the protocol becomes structurally legible to machines. The branch shows that key hierarchy is not just a crypto convenience; it is also a way to encode relationship shape and memory scope into the access model.

## Open Questions

- Which path dimensions should be standard, and which should remain contextual?
- Should the derivation tree represent people, events, or both?
- How much of the path should be visible to the user versus hidden in implementation?

## Related Links

- [Consent Crystal Structure Research](../../../../../consent-crystal-structure-research/index.md)
- [Consent–Intent Compression Protocol (CICP)](../../../index.md)
- [Implementation and Access](../../index.md)
- [Key Derivation and Decryption](../index.md)
- [Selective Decryption](../selective-decryption/index.md)
- [Pairing and Field Access](../../pairing-and-field-access/index.md)
- [Ritual Token Initialization](../../ritual-token-initialization/index.md)

## Next Actions

1. Keep the key-tree seam stable.
2. Split again only if another derivation dialect appears.
