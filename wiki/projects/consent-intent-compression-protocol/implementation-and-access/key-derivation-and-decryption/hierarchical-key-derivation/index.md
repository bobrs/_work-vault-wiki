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
