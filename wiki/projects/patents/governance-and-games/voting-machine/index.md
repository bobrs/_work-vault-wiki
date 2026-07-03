# Voting Machine

Parent lineage: `Patents` / `Governance and Games`

This branch covers the offline-capable voting seam, including the core provisional draft, supporting filing paperwork, and the `N417` attachment.

This page is the public landing page for the voting-machine concept in the Work Vault. The provisional patent itself has been abandoned and is treated here as an informing artifact: useful as a design record, not as active patent strategy.
It now also serves as the detailed lineage witness for the promoted [Voting Machine](../../../voting-machine/index.md) project page.

## Current Shape

- 3 live files.
- 1 voting-system provisional manuscript.
- 2 filing/support PDFs.

## Representative Files

- [Enhanced Offline-Capable Voting Infrastructure Using Deterministic Cryptographic Key Derivation.md](<../../../../../artifacts/standard-named/20260622__PATENTS__GOVERNANCE-GAMES__VOTING-MACHINE__v1__offline-capable-voting-infrastructure-using-deterministic-cryptographic-key-derivation.md>) · [archive copy](<../../../../../artifacts/intake-archive/20260622__patents-intake/Voting Machine/Provisional Patent Application- Offline-Capable Voting Infrastructure Using Deterministic Cryptographic Key Derivation.docx>)
- [Provisional_Patent_Cover_Sheet_Bobby_Simpson_Voting_System.pdf](<../../../../../artifacts/intake-archive/20260622__patents-intake/Voting Machine/Provisional_Patent_Cover_Sheet_Bobby_Simpson_Voting_System.pdf>)
- [N417.pdf](<../../../../../artifacts/intake-archive/20260622__patents-intake/Voting Machine/N417.pdf>)

## Working Read

This is the access-control side of the governance cluster. The filing package reads as one stable branch: voting infrastructure, cover sheet, and attachment.

Read as an informing artifact, the branch describes how an offline voting system can preserve custody, determinism, and reviewability without depending on a live network. The useful semantic center is not the filing status; it is the governance shape: how identity, access, entropy, and evidence stay legible while a vote is prepared, cast, and reviewed.

The markdown source copy now carries the manuscript as the working reference, while the cover sheet and `N417` remain the historical/legal witnesses.

That makes the page a direct route into the governance attractor: authority is being encoded as deterministic custody, and custody is being made auditable without requiring live connectivity.

## Plain-Language Orientation

The voting-machine artifact proposes an offline election system where the important state transitions can be reproduced, audited, and checked without trusting a live network. Check-in, vote casting, receipt generation, and audit logging are separated into distinct cryptographic domains derived from a shared root seed.

The key move is not simply "make voting digital." The key move is to make a vote traceable enough for audit while still preserving the boundary around voter identity. The system tries to hold several constraints at once: voter access, ballot secrecy, tamper-evident logging, post-election verification, and operation in low-connectivity environments.

## How The System Works

- A check-in station validates a voter and derives a voter/session-specific token.
- A voting machine re-derives the relevant key material to authenticate the token and encrypt or commit the vote.
- An audit terminal verifies inclusion proofs or Merkle roots without needing identifying data.
- A log system receives one-way transmitted records so custody can be checked after the fact.
- Published seed/path rules allow later verification without requiring continuous network availability.

The design separates validation, vote authentication, and audit metadata into different derivation domains. That separation is central: it keeps the system from collapsing identity, voting action, and audit evidence into one overpowered record.

## Consent Reading

This artifact belongs in the consent vocabulary because voting is one of the clearest civic cases where participation must be authorized, bounded, witnessed, and protected from coercive transparency.

In Work Vault terms, the system treats consent as a continuing condition rather than a one-time permission. The voter consents to participate in an election process, but that does not imply consent to identity exposure, network surveillance, mutable logs, or post-hoc reinterpretation of the vote. The design tries to keep those boundaries separate by using deterministic keys, receipts, one-way logs, and audit terminals with limited knowledge.

The important consent question is not "did someone press a button?" It is whether the system preserves the conditions under which that action can remain legitimate: authorized access, private choice, reviewable custody, and evidence that can be checked without becoming a new instrument of control.

This makes the voting-machine branch a useful companion to [Consent](../../../../attractors/consent/index.md), [Intent-Consent](../../../../concepts/intent-consent/index.md), [Consent Physics](../../../../concepts/consent-physics/index.md), and [The Consentocracy Bridge](../../../../external/shimmerymemory/essays/changing-the-optimization-primitive/index.md). It also touches [Provenance](../../../../attractors/provenance/index.md), because the vote record must carry enough lineage to be admissible without carrying too much identity.

## Governance Reading

Governance appears here as constrained authority. The system must let an election authority run the process, but it should not require everyone to trust that authority blindly. The proposed mechanism distributes trust across derivation paths, logs, receipts, audit terminals, and post-election verification.

That gives the page a strong relationship to [Governance](../../../../attractors/governance/index.md), [Witness](../../../../attractors/witness/index.md), and [Trust](../../../../attractors/trust/index.md). A vote becomes legitimate only if the system can witness the right things: eligibility, cast status, inclusion, log integrity, and auditability. It must also refuse to witness the wrong things, especially voter identity attached to ballot choice.

## What To Read Next

- Start with the markdown source copy for the technical artifact: [Enhanced Offline-Capable Voting Infrastructure Using Deterministic Cryptographic Key Derivation.md](<../../../../../artifacts/standard-named/20260622__PATENTS__GOVERNANCE-GAMES__VOTING-MACHINE__v1__offline-capable-voting-infrastructure-using-deterministic-cryptographic-key-derivation.md>).
- Use [Consent](../../../../attractors/consent/index.md) for the boundary and authorization vocabulary.
- Use [The Consentocracy Bridge](../../../../external/shimmerymemory/essays/changing-the-optimization-primitive/index.md) for the wider governance/provenance argument.
- Use [The Historical Record of the Future Requires Consentful Loops](../../../../external/shimmerymemory/essays/historical-record-future-consentful-loops/index.md) for admissible recordkeeping across time.
- Use [Sovereign Governance](../../../continuity-engine/sovereign-governance/index.md) when the voting-machine concept is being read through Tribal, regulatory, or authority-sensitive settings.

## Next Actions

1. Keep the voting manuscript and filing attachments together.
2. Split only if a separate filing or election seam appears.
3. Keep the markdown source copy as the editable reference and the PDFs as archival companions.

## Related Links

- [Voting Machine project](../../../voting-machine/index.md)
- [Governance](../../../../attractors/governance/index.md)
- [Consent](../../../../attractors/consent/index.md)
- [Intent-Consent](../../../../concepts/intent-consent/index.md)
- [Consent Physics](../../../../concepts/consent-physics/index.md)
- [The Consentocracy Bridge](../../../../external/shimmerymemory/essays/changing-the-optimization-primitive/index.md)
- [The Historical Record of the Future Requires Consentful Loops](../../../../external/shimmerymemory/essays/historical-record-future-consentful-loops/index.md)
- [Provenance](../../../../attractors/provenance/index.md)
- [Witness](../../../../attractors/witness/index.md)
- [Trust](../../../../attractors/trust/index.md)
- [Quantum Invariants](../../../quantum-invariants/index.md)
- [Semantic Integrity](../../../semantic-integrity/index.md)
- [Continuity Engine / Sovereign Governance](../../../continuity-engine/sovereign-governance/index.md)
- [Governance Diad](../../../semantic-collapse-theory/story/governance-diad/index.md)
