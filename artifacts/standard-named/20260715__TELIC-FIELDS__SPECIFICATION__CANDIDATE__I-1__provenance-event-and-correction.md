---
title: "I.1 — Provenance, Event, and Correction Specification"
artifact_date: "2026-07-15"
artifact_type: "candidate-technical-specification"
domain: "TELIC-FIELDS"
scope: "WORKING"
status: "pre-production"
content_canon_status: "unset"
specification_version: "0.1"
derived_from:
  - "I.0 — Canonical Semantic Spine and Core Envelope Specification"
  - "FG-S — Record Consolidation and Canonical Semantic Spine"
  - "F.6 — Temporal Telic Relations"
  - "F.8 — Semantic Fields as Durable Telic Trails"
  - "F.10 — Semantic Polytelometry with Language Models"
---

# I.1 — Provenance, Event, and Correction Specification

## 1. Purpose

I.1 specifies how Telic Field records preserve source, transformation, time, authority, correction, and downstream consequence.

Its governing rule is:

> **Correction changes what may govern next. It does not falsify what governed before.**

A conforming system must be able to answer:

- What source entered the system?
- Which transformation produced this interpretation?
- Which record version governed the action?
- What changed later?
- Which descendants were corrected?
- Which descendants could not be reached?
- Which authority expired?
- Which private restriction was honored without unnecessary disclosure?
- Which model inference remained an inference despite repeated reuse?

I.1 extends W3C PROV rather than replacing it.

---

# 2. Normative scope

I.1 defines:

- a Telic Field profile of W3C PROV;
- entity, activity, and agent mappings;
- portable record identifiers;
- bitemporal event behavior;
- correction, supersession, and withdrawal semantics;
- descendant-impact and propagation records;
- protected omission;
- selective-disclosure witness views;
- independent participant export;
- negative and adversarial conformance cases.

I.1 does not define:

- a production cryptographic identity system;
- a universal access-control protocol;
- legal erasure requirements;
- one distributed-ledger technology;
- proof that a source is true;
- proof that an authority is legitimate merely because it is recorded.

---

# 3. Provenance profile

## 3.1 Reused W3C PROV concepts

| Telic Field object | PROV concept |
|---|---|
| SourceObject | `prov:Entity` |
| TelicProjection | `prov:Entity` |
| ReceiverMirror | `prov:Entity` |
| FieldMap | `prov:Entity` |
| Route | `prov:Entity` |
| DecisionWitness | `prov:Bundle` |
| Model output | `prov:Entity` |
| Extraction | `prov:Activity` |
| Retrieval | `prov:Activity` |
| Interpretation | `prov:Activity` |
| Route generation | `prov:Activity` |
| Gate evaluation | `prov:Activity` |
| Action execution | `prov:Activity` |
| Correction propagation | `prov:Activity` |
| Person, role, institution, community | `prov:Agent` |
| Language model | `prov:SoftwareAgent` |
| Source use | `prov:used` |
| Generation | `prov:wasGeneratedBy` |
| Attribution | `prov:wasAttributedTo` |
| Derivation | `prov:wasDerivedFrom` |
| Revision | `prov:wasRevisionOf` |
| Association | `prov:wasAssociatedWith` |
| Bundle membership | `prov:hadMember` |

## 3.2 Telic Field extensions

I.1 adds:

```text
tf:standingType
tf:evidenceStatus
tf:authorityOperation
tf:consentState
tf:protectedCondition
tf:fieldClass
tf:participantRecognition
tf:validTime
tf:transactionTime
tf:contestStatus
tf:propagationStatus
tf:releaseStatus
tf:consequence
tf:omissionProof
```

A system MUST NOT infer truth, consent, or legitimacy from provenance completeness.

---

# 4. Portable identifiers

Every consequential object MUST have a stable, portable identifier.

Candidate format:

```text
urn:telic:<namespace>:<record-type>:<uuid>
```

Example:

```text
urn:telic:demo:projection:6e33f8b4-54b5-4b12-9b31-8b5fc4d2ce93
```

## 4.1 Requirements

A portable identifier MUST:

- remain stable across export;
- identify one logical record lineage;
- distinguish record lineage from version;
- avoid embedding private content;
- remain unique within its namespace;
- permit local or federated resolution.

A portable identifier SHOULD:

- be provider-independent;
- survive schema migration;
- support offline export;
- resolve to a bounded metadata view rather than unrestricted content.

## 4.2 Versions

A logical record identifier remains stable.

Each version receives:

```yaml
record_id:
record_version:
schema_version:
transaction_time:
valid_time:
```

A version MAY also have a unique entity identifier.

Example:

```text
record lineage:
  urn:telic:demo:projection:6e33...

version entity:
  urn:telic:demo:projection-version:5c1a...
```

---

# 5. Bitemporal event rules

I.1 requires both:

- **valid time** — when a state applied in the represented world;
- **transaction time** — when the system learned or recorded it.

## 5.1 Example

An institution records on July 15 that a consent had actually expired on July 10.

```yaml
valid_time:
  valid_to: 2026-07-10T23:59:59Z

transaction_time:
  recorded_at: 2026-07-15T09:12:00Z
```

The system MUST preserve both.

## 5.2 Authority eligibility

An authority record may remain historically visible after expiry.

It MUST NOT authorize a new action when:

```text
action.valid_time > authority.valid_time.valid_to
```

unless a new authority event exists.

## 5.3 Retroactive correction

A correction MAY establish that a prior record was inaccurate during an earlier valid-time interval.

The system MUST NOT silently rewrite the historical action witness.

Instead it records:

- what the system believed;
- which version governed;
- when the correction arrived;
- what the corrected valid-time claim is;
- what consequence followed.

---

# 6. Event model

Every consequential change SHOULD be represented as an event.

Minimum event fields:

```yaml
event_id:
event_type:
subject_record:
agent:
valid_at:
recorded_at:
source:
activity:
provenance:
payload:
```

## 6.1 Core event types

```text
source_registered
projection_created
projection_confirmed
projection_corrected
projection_withdrawn
mirror_created
mirror_corrected
route_generated
route_revised
gate_evaluated
authority_granted
authority_expired
authority_withdrawn
action_authorized
action_executed
consequence_recorded
contest_opened
correction_propagation_started
correction_propagated
correction_propagation_failed
protected_omission_verified
record_released
record_deleted
record_dissolved
```

## 6.2 Event immutability

An event that participated in an action witness MUST NOT be silently altered.

A later event MAY:

- supersede;
- correct;
- contest;
- restrict;
- release;
- delete permitted content;
- add consequence.

The historical event remains part of the witness where lawful and proportionate.

---

# 7. Correction semantics

## 7.1 Correction object

A correction MUST identify:

```yaml
correction_id:
target_record:
target_version:
corrected_by:
grounds:
correction_type:
new_value:
valid_time_effect:
recorded_at:
authority:
```

Candidate correction types:

```text
SOURCE_CORRECTION
INTERPRETATION_CORRECTION
SCOPE_CORRECTION
AUTHORITY_CORRECTION
TEMPORAL_CORRECTION
STATUS_CORRECTION
PRIVACY_CORRECTION
IDENTITY_CORRECTION
```

## 7.2 Supersession

A correction MAY produce a new record version.

The new version MUST reference:

```text
prov:wasRevisionOf
```

The prior version MUST be marked:

```text
superseded
```

if it is no longer current.

## 7.3 Contest without resolution

A contest MAY remain unresolved.

The target record remains:

```text
contested
```

A contested record MAY continue to be visible.

Whether it may continue to govern action depends on the relevant gate.

## 7.4 Correction authority

A person may have descriptive authority over:

- their own statement;
- their own consent;
- their own boundary;
- their own identity details.

They may not automatically have authority to correct:

- another person's statement;
- an institutional rule;
- independently observed evidence;
- a public record.

The system MUST preserve the source's correction and the external evidence separately where both remain material.

---

# 8. Descendant impact

A correction may affect downstream records.

Candidate descendants include:

- mirror;
- summary;
- field map;
- route;
- gate result;
- recommendation;
- action;
- witness;
- memory;
- model context;
- external system.

## 8.1 Descendant relation

A descendant relation SHOULD be established through:

```text
prov:wasDerivedFrom
prov:used
tf:affectedByCorrection
```

## 8.2 Impact classes

```text
DIRECT
MATERIAL
POSSIBLE
NONE
UNKNOWN
```

## 8.3 Required behavior

When a correction is recorded, the system MUST:

1. identify known descendants;
2. classify likely impact;
3. attempt propagation where authorized;
4. record success, partial success, failure, or unknown;
5. preserve unreachable descendants as explicit gaps;
6. prevent known invalid descendants from silently governing new actions.

---

# 9. Propagation record

A `CorrectionPropagationRecord` contains:

```yaml
propagation_id:
correction:
root_target:
descendants:
  - record:
    impact:
    status:
    attempted_at:
    result:
    gap_reason:
initiated_by:
authority:
started_at:
completed_at:
overall_status:
```

Candidate descendant statuses:

```text
UPDATED
SUPERSEDED
MARKED_CONTESTED
RECALCULATED
REVIEW_REQUIRED
ACTION_PAUSED
NOT_AUTHORIZED
NOT_REACHABLE
EXTERNAL_SYSTEM
DELETED
NO_CHANGE
UNKNOWN
```

## 9.1 Gap rule

A system MUST NOT claim propagation complete if any material descendant is:

```text
NOT_REACHABLE
NOT_AUTHORIZED
EXTERNAL_SYSTEM
UNKNOWN
```

The witness SHOULD expose the gap to affected participants.

---

# 10. Repeated inference rule

A model-generated inference remains an inference unless a separate event changes its evidence status.

Repeated reuse does not strengthen source status.

The following chain is prohibited:

```text
model inference
→ generated summary
→ retrieved summary
→ second generated summary
→ recorded as direct source fact
```

Every derived use MUST preserve:

- original evidence status;
- source link;
- transformation history;
- participant recognition;
- current contest status.

A system MAY increase confidence in an inference.

It MUST NOT relabel it `DIRECT` or `CONFIRMED` without appropriate source or authority.

---

# 11. Protected omission

Protected omission permits a system to verify that a restriction exists without exposing its private content.

## 11.1 Use cases

- private medical basis behind an accommodation boundary;
- confidential legal advice;
- protected community knowledge;
- identity data not necessary for the decision;
- safety plan;
- sealed or privileged source.

## 11.2 Omission proof

A protected-omission proof SHOULD contain:

```yaml
omission_proof_id:
restriction_type:
verified_by:
verification_authority:
scope:
valid_time:
status:
disclosure_class:
source_hash_or_reference:
review_route:
```

The proof MUST NOT disclose more than necessary.

## 11.3 Disclosure classes

```text
PUBLIC
PARTICIPANT
MEDIATOR
DECISION_AUTHORITY
AUDITOR
SEALED
SOURCE_ONLY
```

## 11.4 Rule

A gate MAY rely on an omission proof where:

- the verifier has appropriate authority;
- the proof scope matches the action;
- the restriction remains valid;
- the decision does not require the hidden content itself.

The proof MUST NOT be represented as verification of unrelated claims.

---

# 12. Selective-disclosure witness views

One DecisionWitness may produce multiple views.

Candidate views:

```text
SOURCE_VIEW
PARTICIPANT_VIEW
MEDIATOR_VIEW
DECISION_AUTHORITY_VIEW
AUDITOR_VIEW
PUBLIC_VIEW
MODEL_VIEW
```

Each view MUST:

- preserve record identifiers;
- preserve omitted-field markers;
- preserve source/inference distinction;
- preserve gate and action status;
- disclose only authorized content;
- identify its view policy and version.

An omitted field MUST be represented as:

```text
OMITTED_BY_POLICY
OMITTED_BY_CONSENT
OMITTED_BY_PRIVILEGE
OMITTED_FOR_MINIMIZATION
REDACTED_BY_LAW
UNKNOWN
```

It MUST NOT appear as though no information exists.

---

# 13. Independent participant export

A P3 implementation MUST support an export that can be inspected without the same model that created the interpretation.

Minimum export:

```text
manifest.json
records/
events/
witness/
views/
schemas/
checksums.txt
```

The export SHOULD contain:

- stable identifiers;
- schema versions;
- record versions;
- source and inference status;
- correction history;
- propagation gaps;
- selected witness view;
- integrity checksums.

The export MAY omit protected source content.

It MUST preserve evidence that omission occurred under a declared policy.

---

# 14. Deletion, release, and unlearning

## 14.1 Release

Release ends future authority or active use.

It MAY preserve a minimal historical witness.

## 14.2 Deletion

Deletion removes content according to applicable policy.

A deletion event SHOULD identify:

- deleted record;
- authority;
- scope;
- descendants;
- retained proof;
- unresolved copies.

## 14.3 Model unlearning

I.1 does not define machine unlearning.

A deletion or release event MUST NOT claim that model influence was removed.

A separate training-lineage or unlearning record is required.

---

# 15. Negative conformance cases

A conforming implementation MUST reject or flag the following.

## NC-1 — Inference laundering

An inferred preference is reused through several summaries and becomes `DIRECT`.

Expected result:

```text
FAIL
```

## NC-2 — Expired authority reuse

An expired authority record is used to authorize a new action.

Expected result:

```text
FAIL
```

## NC-3 — Silent history rewrite

A corrected projection overwrites the earlier version that governed an action.

Expected result:

```text
FAIL
```

## NC-4 — False propagation completeness

A material external descendant cannot be reached, but the system reports propagation complete.

Expected result:

```text
FAIL
```

## NC-5 — Protected omission collapse

A private source is disclosed merely because a gate relied on its restriction.

Expected result:

```text
FAIL
```

## NC-6 — Omission interpreted as absence

A witness view removes a private record without marking that content was omitted.

Expected result:

```text
FAIL
```

## NC-7 — Provenance-as-truth

A claim is presented as true solely because its provenance chain is complete.

Expected result:

```text
FAIL
```

## NC-8 — Model-only custody

A participant can access the witness only by asking the same model that generated it.

Expected result:

```text
FAIL FOR P3
```

## NC-9 — Contest without responsible authority

A contest form exists, but no actor can pause or alter the action.

Expected result:

```text
FAIL FOR P3
```

## NC-10 — Correction without descendant review

A source correction is accepted, but known derived routes and witnesses are not reviewed.

Expected result:

```text
FAIL FOR P2/P3
```

---

# 16. Positive demonstrations

I.1 includes five required demonstrations.

## PD-1 — Full correction propagation

A source correction reaches:

- receiver mirror;
- field map;
- route;
- gate;
- decision witness.

## PD-2 — Partial propagation with explicit gap

A source correction reaches internal descendants but an external exported copy cannot be reached.

The propagation record remains:

```text
PARTIAL
```

## PD-3 — Expired authority

The authority remains historically visible.

A new action gate rejects it.

## PD-4 — Protected omission

A decision authority verifies that a valid restriction exists without receiving the private source content.

## PD-5 — Inference status preservation

Repeated model summaries preserve:

```text
INFERRED
```

through every descendant.

The evidence status never becomes `DIRECT` without confirmation.

---

# 17. Conformance additions

I.1 adds the following P3 requirements:

- descendant-impact discovery;
- propagation record;
- explicit propagation gaps;
- selective-disclosure witness views;
- protected-omission proof;
- independent export;
- negative test suite;
- expired-authority enforcement;
- inference-status preservation.

P2 SHOULD implement these.

P0 and P1 MAY implement documentary subsets but MUST NOT claim full correction conformance.

---

# 18. Security and privacy considerations

Provenance can expose:

- identity;
- association;
- private reasoning;
- health information;
- organizational structure;
- protected community knowledge;
- model vulnerabilities.

I.1 therefore requires:

- access-controlled views;
- minimization;
- stable references without embedded private content;
- explicit omission markers;
- bounded retention;
- export policy;
- deletion and release;
- separation of witness from unrestricted source access.

Correction systems can also be abused.

An attacker may attempt to:

- rewrite a source they do not control;
- revoke valid authority falsely;
- flood descendants with corrections;
- trigger denial of service through propagation;
- infer protected content from omission metadata.

Implementations SHOULD rate-limit, authenticate, and scope correction authority.

---

# 19. I.1 non-claims

I.1 does not claim:

- provenance proves truth;
- a correction is automatically valid because someone submitted it;
- every historical record must be preserved forever;
- protected omission is a cryptographic zero-knowledge proof;
- an export is interoperable merely because it is JSON;
- W3C PROV captures all consent or standing semantics;
- correction can reverse every consequence;
- model memory is unlearned because a record was deleted.

---

# 20. I.1 completion criterion

I.1 passes when:

1. the five positive demonstrations validate;
2. the ten negative cases fail as expected;
3. a participant export is generated;
4. a private restriction can govern a gate without full disclosure;
5. correction history remains visible;
6. expired authority cannot authorize new action;
7. inference status survives repeated reuse;
8. the H.1 primer explains these mechanics without implying that provenance equals truth.
