# Personal Data Sovereignty Protocol (PDSP)

## A LoopLink-based architecture for subjective, auditable, decentralized trust

### Purpose

This restatement of PDSP makes the transport layer explicit. Trust is modeled as a set of loop-scoped interactions built on LoopLink and Abracadabradoo rather than on persistent identity or centralized ledgers.

The focus is the same sovereignty problem, but with stronger emphasis on ratcheted presence, loop-local meaning, and selective proof.

### Core framing

PDSP treats digital trust as a decentralized and consensual mesh of human-mediated semantic loops. Each participant maintains their own verifiable trust graph, represented as a Merkle mesh of interactions.

Compared with the other PDSP manuscript, this version foregrounds LoopLink as the identity and presence layer, with Abracadabradoo carrying the semantic loop layer above it.

### Motivation

Persistent identifiers and global registries assume that trust is static and transferable. PDSP argues instead that trust is situational, ephemeral, and socially contextual.

End-to-end encryption preserves content, but not necessarily delivery, revocation, or consent structure. PDSP answers with ratcheted presence confirmation, loop-local meaning, and proofs that stay attached to the trust relationship itself.

### Key concepts

#### LoopLink Protocol

LoopLink forms and maintains bilateral trust relationships through a ratcheted handshake, mutual signatures, and heartbeat pulses. Identity is loop-scoped, revocable, and offline-capable.

#### Abracadabradoo Protocol

Abracadabradoo adds cryptographic proof-of-receipt and semantic metadata to encrypted messaging. It supports public declarations, witness roles, and selective verifiability.

#### Self-rooted Merkle trees

Each participant maintains a personal Merkle tree or DAG anchoring interactions, declarations, and proofs. There is no universal root, only intersecting trees that form a Merkle mesh.

#### Semantic loops

A loop is a bounded trust container negotiated between two or more parties. It can include payloads, timing rules, consent flags, quorum policies, and third-party witnesses.

#### Ratcheted pulse epochs

Instead of global time, PDSP uses loop-local pulse chains derived from LoopLink state to prove a shared now. A missed pulse naturally decays the relationship; resynchronization or revocation must be explicit.

### Architecture overview

PDSP is implemented as a layered architecture:

- Identity and Presence Layer - LoopLink establishes loop-scoped identity, mutual authentication, and pulse synchronization.
- Semantic Loop Layer - Abracadabradoo creates structured encrypted interactions, receipts, and declarations.
- Merkle Anchoring Layer - The local log stores participations, declarations, and proofs.
- Witness and Role Layer - Observers, auditors, and validators can be represented explicitly.
- Declaration and Finalization Layer - Co-signed agreements or proofs can be published to external registries or shared memory systems.

### Comparison with Dialogica

Dialogica handles formal mediation and structured conversation. PDSP provides the sovereign substrate: living consent loops, verifiable exchanges, and shared semantic context.

PDSP loops can feed into Dialogica sessions as trust anchors or context providers.

### Use cases

- Medical consent - a patient and clinician create a LoopLink loop at the point of care.
- AI-human collaboration - a sensitive recommendation is exchanged within a loop and optionally witnessed.
- Civic governance and voting - nested loops reach quorum on a proposal and finalize it across participants' trees.
- Anonymous journalism - a whistleblower proves presence through ratcheted pulses without revealing identity.
- Offline ticketing - attendees receive latent LoopLink loops as tickets.
- Private contracting - a final declaration is co-signed and anchored to the participants' Merkle roots.

### Implementation considerations

- Loop initialization UI for QR, NFC, or equivalent key exchange.
- Local Merkle logging with inclusion proofs and selective disclosure.
- Pulse management with configurable cadence and drift windows.
- Declaration composition and validation with optional publication.
- Witness-role support for third-party observers.
- Selective disclosure so presence or consent can be proven without revealing the full loop.

### Open questions

- How do multiparty extensions affect pulse ratcheting and Merkle anchoring?
- What forms of cryptographic revocation or decay should be supported?
- How can third-party witnesses be trusted and verified?
- Should a minimal protocol registry coordinate loop schemas and roles?
- Can loop states be migrated or time-shifted across devices?

### Appendix notes

This markdown copy is the LoopLink-forward source version of the core PDSP manuscript. It is the one the wiki should prefer when referring to the transport and presence layer of the protocol.
