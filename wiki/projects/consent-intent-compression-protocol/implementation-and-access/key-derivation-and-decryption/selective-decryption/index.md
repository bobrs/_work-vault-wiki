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

## Core Claim

Access can be made granular by tying encryption to time structure. Instead of storing one monolithic secret, the protocol can encrypt segments against a temporal tree so that only the intended slice becomes visible later.

## Mechanisms

- A root key can represent a session, day, or event.
- Child keys can represent hour, minute, second, or another chosen temporal unit.
- Each segment can be encrypted independently.
- Ancestor keys can reveal descendant ranges when policy allows it.

## Terminology

- Temporal key tree: a key hierarchy organized by time.
- Selective disclosure: revealing only the relevant portion of an encrypted stream.
- Ancestor key: a key that can unlock a broader range of child data.
- Scoped visibility: access limited by time, consent, or policy.

## Implications

This page gives the branch a practical answer to the question of partial disclosure. It supports use cases where the full record should exist, but not all of it should be equally available. That is central to the consent logic of the whole project.

## Open Questions

- What temporal granularity should be default for different contexts?
- When does delayed disclosure need additional policy beyond the key tree?
- What should remain hidden even from ancestor keys?

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
