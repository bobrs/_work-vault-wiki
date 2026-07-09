# Personal Data Sovereignty Protocol (PDSP-lite) Specification v0.3

Status: Draft 04 - 11 May 2025

## 1. Introduction

PDSP-lite v0.3 extends v0.2 with two optional, human-friendly onboarding profiles:

- `loop://exchange` URI - a compact URI for QR, NFC, or deep-link hand-off of a participant's public key.
- `TOTP-HK-1` voice/SMS handshake - retained from the legacy HumanKey draft for cases where visual channels are unavailable.

The core packet header from v0.2 is unchanged. Implementations MAY ignore both profiles if QR or NFC key exchange suffices.

## 2. Packet Header Schema

Identical to v0.2. Refer to PDSP-lite v0.2 for the normative field table.

## 3. Validation and Error Codes

Validation semantics are unchanged from v0.2.

## 4. Optional Onboarding Profiles

### 4.1 `loop://exchange` URI

Preferred for QR, NFC, or link-click onboarding. Conveys only the public key; the secure LoopLink handshake still applies.

### 4.2 `TOTP-HK-1` voice/SMS

Six-digit code swap for voice-only scenarios. Clients MUST rotate to random keys immediately after loop creation.

## 5. Change Log

- v0.3 (Draft 04, 2025-05-11) - Added the `loop://` URI scheme and clarified the `TOTP-HK-1` fallback. No changes to the header schema.
- v0.2 (Draft 03) - Added `participants_delta`, `turn_type`, new roles, and API verbs.
- v0.1 (Draft 02) - Initial public draft.

## Appendix A - `TOTP-HK-1` Handshake

Reference pointer retained for the full algorithm profile, flow, and security notes.

## Appendix B - `loop://exchange` URI Scheme

Provisional reference for the compact onboarding URI.
