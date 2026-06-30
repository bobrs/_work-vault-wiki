# Key Derivation and Decryption

Parent lineage: `Consent–Intent Compression Protocol (CICP)` / `Implementation and Access`

This cluster covers deterministic key hierarchies and selective decryption over temporal ranges.

It is the cryptographic control point in the implementation rail: identity is arranged hierarchically, and access is reduced to a time-bound question of visibility.

## Current Shape

- 2 key derivation and decryption documents.
- 2 nested lineage pages now organize the cryptographic branch.

## Representative Files

- [Hierarchical Key Derivation in Loop-Based Systems (BIP-32 Integration).docx](<../../../../../artifacts/intake-archive/20260622__consent-crystal-structure-research-intake/Consent–Intent Compression Protocol (CICP)/Hierarchical Key Derivation in Loop-Based Systems (BIP-32 Integration).docx>)
- [Selective Decryption via Hierarchical Temporal Key Derivation.docx](<../../../../../artifacts/intake-archive/20260622__consent-crystal-structure-research-intake/Consent–Intent Compression Protocol (CICP)/Selective Decryption via Hierarchical Temporal Key Derivation.docx>)

## Nested Lineage Pages

- [Hierarchical Key Derivation](hierarchical-key-derivation/index.md)
- [Selective Decryption](selective-decryption/index.md)

## Working Read

This is the cryptographic access-control layer: key trees for identity management and time-based selective decryption.

The deeper role here is to define how identity can be represented hierarchically while still allowing time-bound access. It is the CICP page where cryptographic structure meets consent logic most directly, since key derivation and selective decryption both encode who may see what, and when.

This makes it the control point for privacy and temporal access inside the implementation branch. The branch now separates the key tree from the selective visibility policy so the hierarchy and the time-bound access rule can be reasoned about independently.

## Core Claim

If access is consent-bound, then cryptographic identity must also be consent-bound. CICP uses hierarchical derivation to keep identity structured and selective decryption to keep disclosure scoped to the relevant time slice, session, or event.

## Mechanisms

- A root seed can generate a deterministic tree of related keys.
- A path can encode site, ritual, participant, and time slice.
- Parent keys can reveal child ranges when policy allows it.
- Sibling branches remain isolated.
- The same structure can support both identity management and delayed disclosure.

## Terminology

- Hierarchical key derivation: deterministic creation of a nested key tree.
- Temporal key tree: a derivation tree organized by time.
- Selective decryption: revealing only the intended segment of encrypted data.
- Hardened path: a branch boundary used where privacy needs stronger separation.

## Implications

The cryptographic rail makes the consent story legible to machines. It gives the branch a way to say that not every record should be equally visible, and not every disclosure should be permanent. That is what allows the protocol family to talk about privacy without reducing the whole project to generic encryption.

## Open Questions

- Which path granularity is useful by default: minute, hour, session, or event?
- Should key hierarchy primarily express identity, memory, or both?
- Which disclosures should be reversible, and which should remain opaque even to ancestors?

## Related Links

- [Consent Crystal Structure Research](../../../../consent-crystal-structure-research/index.md)
- [Consent–Intent Compression Protocol (CICP)](../../index.md)
- [Implementation and Access](../index.md)
- [Protocol Foundations](../../protocol-foundations/index.md)
- [Pairing and Field Access](../pairing-and-field-access/index.md)
- [Ritual Token Initialization](../ritual-token-initialization/index.md)
- [Loop Training](../../loop-training/index.md)
- [POLEMEMELOP](../../../../concepts/polememelop/index.md)
- [Hierarchical Key Derivation](hierarchical-key-derivation/index.md)
- [Selective Decryption](selective-decryption/index.md)

## Next Actions

1. Keep the key-tree and selective-decryption pages stable.
2. Split again only if a finer cryptographic seam appears.
