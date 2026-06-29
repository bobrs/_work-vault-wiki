# Selective Decryption

Parent lineage: `Consent–Intent Compression Protocol (CICP)` / `Implementation and Access` / `Key Derivation and Decryption`

This page isolates the time-bound visibility side of the cryptographic access layer: when content becomes readable, and under what scoped conditions.

It is the policy seam of the cryptographic branch. The document here treats decryption as selective access control rather than as a generic secret-handling step.

## Current Shape

- 1 selective decryption document.

## Representative Files

- [Selective Decryption via Hierarchical Temporal Key Derivation.docx](<../../../../../../artifacts/intake-archive/20260622__consent-crystal-structure-research-intake/Consent–Intent Compression Protocol (CICP)/Selective Decryption via Hierarchical Temporal Key Derivation.docx>)

## Working Read

This branch covers the access-policy edge: which slices of content become visible, and when. It is the time-bounded counterpart to the hierarchy defined in the key-derivation page.

The document belongs here because it translates the derived key structure into an actual visibility rule. That keeps policy separate from structure while preserving the dependency between the two.

## Related Links

- [Consent Crystal Structure Research](../../../../../consent-crystal-structure-research/index.md)
- [Consent–Intent Compression Protocol (CICP)](../../../index.md)
- [Implementation and Access](../../index.md)
- [Key Derivation and Decryption](../index.md)
- [Hierarchical Key Derivation](../hierarchical-key-derivation/index.md)
- [Pairing and Field Access](../../pairing-and-field-access/index.md)
- [Ritual Token Initialization](../../ritual-token-initialization/index.md)

## Next Actions

1. Keep the selective-decryption seam stable.
2. Split again only if a finer temporal-access branch appears.
