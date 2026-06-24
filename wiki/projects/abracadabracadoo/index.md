# Abracadabracadoo

This branch collects the protocol family documents for the Abracadabracadoo line. The material is split between the core message protocol and the implementation/extensions layer, so it reads as a small but durable protocol family rather than a pile of isolated drafts.

## Current Shape

- 6 live protocol documents.
- 3 nested lineage pages organize the set.

## Nested Lineage Pages

- [Core Protocol](core-protocol/index.md)
- [Implementation and Extensions](implementation-and-extensions/index.md)
- [Site Variants](site-variants/index.md)

## Representative Files

- [Abracadabracadoo Protocol Specification.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__SPEC__CORE-PROTOCOL__v1__abracadabracadoo-protocol-specification.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo_Protocol_Specification.docx>)
- [Abracadabracadoo Message Flow.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__FLOW__MESSAGE-EXCHANGE__v1__abracadabracadoo-message-flow.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo Message Flow.docx>)
- [Abracadabracadoo Development Directive.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__IMPLEMENTATION__CPP-REFERENCE-LIBRARY__v1__abracadabracadoo-dev-directive.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo Dev Directive.docx>)
- [Abracadabradoo Protocol Addendum III.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__ADDENDUM__MINIMAL-WITNESS-STRUCTURES__v3__abracadabradoo-protocol-addendum-iii.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo_Protocol_Addendum III.docx>)
- [Abracadabradoo Protocol Addendum IV.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__ADDENDUM__LOOP-LOCAL-TOTP-AND-SUBJECTIVE-EPOCHS__v4__abracadabradoo-protocol-addendum-iv.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo_Protocol_Addendum IV.docx>)
- [Abracadabradoo Protocol Addendum VI.docx](<../../../artifacts/standard-named/20260623__ABRACADABRACADOO__ADDENDUM__CONDITIONAL-DENIABILITY__v6__abracadabradoo-protocol-addendum-vi.docx>) · [archive copy](<../../../artifacts/intake-archive/20260623__abracadabracadoo-intake/Abracadabracadoo_Protocol_Addendum Vi.docx>)

## Working Read

The core protocol is a nested AEAD proof-release scheme. It binds a proof token to the message ciphertext, allowing a recipient to trigger proof release without exposing plaintext to the server.

The extensions layer expands the family in three directions: witnessable loop structures, loop-local time semantics, and conditional deniability. The development directive turns that protocol family into a reference C++ implementation with local storage, tests, and a pluggable architecture.

## Related Links

- [Abracadoo](../abracadoo/index.md)
- [Abracadabracadoo](../../concepts/abracadabracadoo/index.md)
- [Intent-Consent](../../concepts/intent-consent/index.md)
- [Witnessing](../../concepts/witnessing/index.md)

## Next Actions

1. Keep the protocol family separate from the Abracadoo app line.
2. Treat the modification duplicates as collapsed archive lineage, not as new live protocol material.
3. Add more protocol material only when it changes the structure or extension boundary.
