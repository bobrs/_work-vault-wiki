# Reference Implementation

This page compresses the implementation sketch for the consent-scoped communication substrate.

## Source Artifact

- Source role: `standard_named_source`
- Inbound original: [consent_scoped_communication_reference_implementation_sketch.md](<../../../../../artifacts/intake-archive/20260710__consent-scoped-communication-intake/consent_scoped_communication_reference_implementation_sketch.md>)
- Standard-named source: [20260710__SIDE-PROJECTS-DESKTOP__SPEC__CONSENT-SCOPED-COMMUNICATION__v1__consent-scoped-communication-reference-implementation.md](<../../../../../artifacts/standard-named/20260710__SIDE-PROJECTS-DESKTOP__SPEC__CONSENT-SCOPED-COMMUNICATION__v1__consent-scoped-communication-reference-implementation.md>)

## Working Read

The sketch reduces the substrate to a single message grammar with explicit scope metadata. Scope can be declared, refined, forked, and terminated without changing the underlying semantics.

## Core Claim

A minimal implementation can support all common communication contexts if the message schema keeps scope and content separate and the enforcement layer stays pluggable.

## Key Ideas

- Message schema with scope metadata.
- Scope refinement and forking.
- Pluggable enforcement.
- AI follows scope like humans do.
- Cryptographic hardening can be added later.

## Related Pages

- [Consent-Scoped Communication](../index.md)
- [Substrate Specification](../spec/index.md)
- [Infrastructure Opportunity](../opportunity/index.md)
- [One Protocol. Every Conversation.](../overview/index.md)
- [Consent Grammar](../../consent-grammar/index.md)

## Attractor Bridge

- [Consent](../../../../attractors/consent/index.md)
- [Witness](../../../../attractors/witness/index.md)
- [Trust](../../../../attractors/trust/index.md)
- [Agency](../../../../attractors/agency/index.md)

## Notes

- This is a source-anchored implementation note, not a canon claim.
- Keep the message grammar stable if enforcement changes.
