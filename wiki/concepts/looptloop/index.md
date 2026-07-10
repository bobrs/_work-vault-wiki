# LOOPtLOOP

Working definition: a lightweight witness substrate for hash-only private authorization and live provenance loops.

This concept appears across the CICP access rail, WitnessKey, the archived LOOPtLOOP platform companions, and the public `looptloop.online` surface. It is the ingredient that turns consent, witness, and provenance into an inspectable public surface without exposing private payloads.

The public site makes the operating claim explicit: private authorization can be witnessed by hash, and provenance can be made visible in recorded media. That is the core semantic role here. LOOPtLOOP is not a generic identity system; it is a bounded witness and provenance layer with a narrow public contract.

ACT–POLICY is a useful formal neighbor because it expresses the act/policy/witness/state grammar that LOOPtLOOP depends on when a private authorization must stay machine-readable without exposing the payload itself.

## Machine-Readable Surface

- [llms.txt](https://looptloop.online/llms.txt)
- Public API base: `https://api.looptloop.online/v0`
- Public repository: `https://github.com/bobrs/LOOPtLOOP`
- Public pages: `/`, `/witnessmark/`, `/verify/`, `/provenance/`, `/provenance/stage/`, `/provenance/verify/`
- Public license package: `/LICENSE`, `/IPOL.md`
- The homepage embeds a JSON manifest and JSON-LD API metadata for machine consumers

## Core Claims

- Private payload stays private.
- Witness should verify the hash, consent envelope, timing, and signature-bound receipt.
- Provenance can be visible without claiming total truth or legal identity.
- Status must stay explicit and bounded.

## Mechanisms

- Hash private authorization content locally.
- Send only `sha256:` payload hashes and consent-envelope metadata for authorization witness flows.
- Create, accept, reject, and verify authorization offers as explicit state transitions.
- Use provenance loops and rotating codes to show that a recording participated in live witness.

## Implications

- A public service can witness consent without becoming a data sink.
- Verification is a bounded act, not a universal claim.
- The same substrate can support witness receipts, provenance overlays, and consent-aware mechanics.

## Dependencies

- [Witnessing](../witnessing/index.md)
- [Intent-Consent](../intent-consent/index.md)
- [Provenance](../../attractors/provenance/index.md)
- [Trust](../../attractors/trust/index.md)
- [Governance Diad](../governance-diad/index.md)
- [LoopLink](../looplink/index.md)
- [Consent–Intent Compression Protocol (CICP)](../../projects/consent-intent-compression-protocol/index.md)
- [WitnessKey](../../projects/witnesskey/index.md)
- [LOOPtLOOP](../../projects/looptloop/index.md)
- [ACT–POLICY](../../projects/side-projects-desktop/act-policy/index.md)

## Open Questions

- How far should witness receipts extend before they become generalized identity?
- Which provenance claims belong in the public surface, and which should remain local?
- What future loop-state mechanics are compatible with the current public contract?
- How should machine consumers distinguish bounded witness from stronger claims?

## Related Artifacts

- [LOOPtLOOP Addendum- Loop Bootstrap Seed – Presence-Based API Expansion.docx](<../../../artifacts/intake-archive/20260622__patents-intake/LOOPtLOOP platform/LOOPtLOOP Addendum- Loop Bootstrap Seed – Presence-Based API Expansion.docx>)
- [LOOPtLOOP -- Two-Way TOTP Consent Loop Implementation Overview.docx](<../../../artifacts/archived/Patents/LOOPtLOOP platform/LOOPtLOOP -- Two-Way TOTP Consent Loop Implementation Overview.docx>)
- [LOOPtLOOP Field Infrastructure Applications.docx](<../../../artifacts/archived/Patents/LOOPtLOOP platform/LOOPtLOOP Field Infrastructure Applications.docx>)

## Related Pages

- [Consent–Intent Compression Protocol (CICP)](../../projects/consent-intent-compression-protocol/index.md)
- [Implementation and Access](../../projects/consent-intent-compression-protocol/implementation-and-access/index.md)
- [Pairing and Field Access](../../projects/consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/index.md)
- [Field Pairing and Consent Loop](../../projects/consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/field-pairing-and-consent-loop/index.md)
- [Field Infrastructure Applications](../../projects/consent-intent-compression-protocol/implementation-and-access/pairing-and-field-access/field-infrastructure-applications/index.md)
- [WitnessKey](../../projects/witnesskey/index.md)
- [Platform and Field Applications](../../projects/patents/platform-and-field-applications/index.md)
- [LoopLink](../looplink/index.md)

## Notes

- This is a concept page, not a canon claim.
- Treat LOOPtLOOP as a prime ingredient when witness, consent, and provenance need a public, machine-readable edge.
- Keep it distinct from broader identity, billing, or platform claims unless the public contract expands.
