# Personal Data Sovereignty Protocol (PDSP)

## A loop-based architecture for subjective, auditable, decentralized trust

### Purpose

PDSP reimagines digital trust as a decentralized, auditable, and consensual system of human-mediated loops rather than persistent identifiers or centralized ledgers.

The protocol is built to support secure, private, accountable relationships in both human and machine-mediated settings without relying on surveillance-based identity models.

### Core framing

PDSP treats each participant as the root of their own verifiable trust graph. That graph is represented as a Merkle mesh of semantic interactions, declarations, and proofs.

The protocol sits alongside Dialogica, which handles structured negotiation and discourse. Dialogica supplies mediation; PDSP supplies the sovereign trust substrate that makes those exchanges auditable and context-bound.

### Motivation

Existing identity systems, including decentralized ones, usually depend on persistent identifiers, third-party attestations, or global registries. PDSP argues that trust is instead situational, ephemeral, and socially contextual.

End-to-end encryption protects message content, but it does not by itself provide provable delivery, revocability, or human-centered consent. PDSP is the alternative path: shared moments, cryptographic witnessing, and loop-local meaning.

### Key concepts

#### HumanKey Protocol

HumanKey establishes a secure trust relationship between two parties through a shared TOTP-based secret and a negotiated local epoch. It is human-mediated, offline-capable, and mutual.

#### Abracadabradoo Protocol

Abracadabradoo adds cryptographic proof-of-receipt to encrypted interactions. It supports public declarations, semantic loops, and structured witness roles.

#### Self-rooted Merkle trees

Each participant maintains a personal Merkle tree or DAG that anchors interactions, declarations, and proofs. These trees serve as sovereign state registries without a universal root.

#### Semantic loops

A loop is a bounded trust container negotiated between two or more parties. It may include payloads, timing rules, consent flags, quorum policies, and third-party witnesses.

#### Subjective epochs

PDSP uses negotiated loop-local epochs rather than global time. Those subjective timebases allow TOTP synchronization and trust validation even in asynchronous or disconnected environments.

### Architecture overview

PDSP is composed of layered subsystems:

- Identity and Epoch Layer - HumanKey establishes ephemeral trust via TOTP-based handshakes and subjective time coordination.
- Semantic Loop Layer - Abracadabradoo creates structured encrypted interactions, receipts, and declarations.
- Merkle Anchoring Layer - The local log stores participations, declarations, and proofs.
- Witness and Role Layer - Observers, auditors, and validators can be represented explicitly.
- Declaration and Finalization Layer - Co-signed agreements or proofs can be published to external registries or shared memory systems.

Each loop is initiated through a HumanKey trust exchange, negotiated to set a shared rhythm, and carried forward with Abracadabradoo-encrypted messages.

### Comparison with Dialogica

Dialogica excels in formal mediation and structured conversation. PDSP provides the sovereign substrate: a network of pre-consensual interactions, verifiable exchanges, and shared semantic loops.

The two systems are meant to interoperate. PDSP loops can feed into Dialogica sessions as trust anchors or context providers, forming a layered dialogue pipeline.

### Use cases

- Medical consent - patient and clinician create a loop at the point of care; instructions and consent forms are receipt-verified and optionally declared.
- AI-human collaboration - a sensitive recommendation is transmitted through an Abracadabradoo loop and optionally witnessed.
- Civic governance and voting - a DAO or community group uses nested loops to reach quorum and finalize a proposal.
- Anonymous journalism - a whistleblower shares material within an encrypted loop where presence can be proven without revealing identities.
- Offline ticketing - event attendees receive ephemeral loop credentials that validate entry without a global ID.
- Private contracting - two parties negotiate a freelance agreement and anchor the final declaration to their Merkle roots.

### Implementation considerations

- Loop initialization UI for key exchange, epoch selection, and TOTP synchronization.
- Local Merkle logging for inclusion proofs and revocation-aware history.
- Declaration composition and validation with optional publication.
- TOTP drift management for disconnected or resynchronized devices.
- Witness-role support for observers, auditors, and validators.
- Selective disclosure so presence or consent can be proven without revealing the full loop.

### Open questions

- How do loops merge or split over time while preserving semantic coherence?
- What forms of cryptographic revocation should be supported?
- How can third-party witnesses be trusted in decentralized environments?
- Should a minimal protocol registry coordinate loop schemas and roles?
- Can loop states be migrated or time-shifted across devices?

### Appendix notes

This markdown copy is the source-facing conversion of the core PDSP manuscript. The lighter PDSP-lite spec line and the integration bundles remain separate documents and can be migrated next.
