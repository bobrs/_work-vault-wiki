---
title: "Telic Field Papers — A–K Control Plane"
artifact_date: "2026-07-16"
artifact_type: "series-control-plane"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "current guidance"
processing_tier: 4
source_role: "semantic-wiki-layer"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "A-K"
---

# Telic Field Papers — A–K Control Plane

This page is the active orientation and integration surface for the entire Telic Field Papers series. It maps provenance, conceptual research, public and technical branches, implementation passes, gates, evidence, boundaries, and next actions without replacing the underlying source artifacts.

The control plane is current guidance. It is not a canon declaration, a production approval, or an external-review finding.

## Operating rule

Read the series as a witnessed progression:

```text
source and lineage
→ concepts and adjacent-field review
→ public and technical formulations
→ conformance and threat boundaries
→ executable reference implementation
→ external exercise and governance admission
```

Installation, standard naming, validation, or linkage does not promote a source to canon. Archived package claims remain historical evidence; active repository corrections and current wiki status govern present navigation.

## Current A–K map

| Stage | Function | Active status | Primary control surface | Next gate |
|---|---|---|---|---|
| A–C | Provenance package, formal intake, and lineage container | Complete | [Sources](../sources.md), [Lineage](../lineage.md), [Artifact Index](../artifacts/index.md) | Preserve source precedence and evidence identity |
| D | Artifact and concept-page installation | Complete and independently verified | [HI-S status correction](../artifacts/hi-s-cross-branch-synthesis/index.md#verified-stage-d) | Keep installed artifacts linked and current |
| E | Link seeding and existing-page integration | Complete and independently verified | [HI-S status correction](../artifacts/hi-s-cross-branch-synthesis/index.md#verified-stage-e) | Keep seeded links resolving |
| F | Foundational paper series | Complete at candidate-paper level | [F artifact pages](../artifacts/index.md) | Adjacent-field constraints and claim discipline |
| G | Adjacent-fields review | Complete at working-review level | [G artifact pages](../artifacts/index.md), [Sources](../sources.md) | Preserve evidence, uncertainty, and non-novelty boundaries |
| FG-S | Cross-paper synthesis and terminology freeze | Complete at candidate-freeze level | [FG-S synthesis](../artifacts/fg-s-synthesis/index.md) | Maintain the shared vocabulary and claim ledger |
| H | Public reader path H.0–H.10 | Complete at candidate-draft level; wiki-ingested | [HI-0 branch opening](../artifacts/hi-0-controlled-branch/index.md) and paired HI pages | Reader comprehension and public boundary review |
| I | Technical specification I.0–I.10 | Complete at candidate-specification level; wiki-ingested | [HI-0 branch opening](../artifacts/hi-0-controlled-branch/index.md) and paired HI pages | Schema, fixture, verifier, and conformance review |
| HI-S | Cross-branch synthesis and conformance freeze | Complete at candidate-freeze level | [HI-S synthesis](../artifacts/hi-s-cross-branch-synthesis/index.md) | J-stage implementation boundaries |
| J.0 | Reference implementation and pilot harness | Complete at executable-candidate level; PASS WITH CONDITIONS | [J.0 provenance](../artifacts/j0-reference-implementation/index.md) | Independent verification and hardening |
| J.1 | Independent verification, selective disclosure, and pilot hardening | Complete at executable-candidate level; PASS WITH CONDITIONS | [J.1 provenance](../artifacts/j1-independent-verification/index.md) | External review and multi-party trial |
| J.2 | External-review readiness, multi-party trial, and release candidate | Complete at candidate-release level; PASS WITH CONDITIONS | [J.2 provenance](../artifacts/j2-external-review-and-release-candidate/index.md) | J.3 observed external exercise and governance handoff |
| J.3 | Observed external exercise, governance handoff, and pilot admission | Not started | Reserved next-pass seam | External human and organizational evidence |
| K | Future descendant branch | Not started | Reserved; no scope inferred | Define only after J.3 outcome |

## Evidence envelope

Each installed pass should remain traceable through the same evidence envelope:

1. exact inbound package or source reference;
2. preserved intake archive;
3. byte-preserving standard-named copies;
4. manifest and content hashes;
5. semantic provenance page;
6. gate and validation report;
7. explicit claims, conditions, and non-claims;
8. roadmap transition and next gate.

The machine-readable inventory and source records are in [`manifest/`](../../../../manifest/) and the package-level source route is [Sources](../sources.md).

## Concept-to-series integration

| Existing semantic seam | Telic stages | Integration target |
|---|---|---|
| Provenance, witness, and correction | A–C, HI-1, J.0–J.2 | Source identity, correction reachability, selective witnesses, and release evidence |
| Standing, projection, and constitutional self | F.3–G.5, HI-2–HI-3 | Candidate concepts, boundary matrices, current-context checks, and legitimate stops |
| Context, time, and succession | F.5–G.7, HI-3–HI-4, J.1–J.2 | Capacity, temporal standing, policy versioning, rollback, and residual obligations |
| Loops, dependency, and semantic trails | F.7–G.9, HI-5–HI-6 | Dependency governance, dissolution, memory eligibility, retrieval, and correction propagation |
| Navigation, deliberation, and public decision | F.9–G.10, HI-7 | Route portfolios, protected conditions, dissent, consequence, and public decision witnesses |
| Models, training, deployment, and non-sovereignty | F.10–G.12, HI-8–HI-10 | Role boundaries, consentful training, runtime authority, model mediation, and succession |
| Conformance, governance, and release | FG-S, HI-S, J.0–J.3 | Terminology, schemas, threat model, implementation, external review, and pilot admission |

The next integration pass should add explicit links from these seams to the existing [candidate concepts](../index.md#candidate-concepts), [lineage surfaces](../index.md#lineage-surfaces), and relevant attractor gateways, while preserving the distinction between internal lineage and external adjacent fields.

## Public, technical, and operational routes

- [Public reader paths](../../../paths/index.md) should route readers from origin and concepts into the H branch before exposing implementation detail.
- [Artifact Index](../artifacts/index.md) should remain the human-facing source-to-stage map.
- [Sources](../sources.md) should remain the citation and standard-name route.
- The generated [Search](/search/index.html) and [Graph](/graph/index.html) surfaces should expose stage, phase, source role, status, and lineage relationships.
- The generated [Maintenance Hub](/wiki/maintenance/index.html) should carry unresolved links, duplicate review, missing files, stale metadata, and J.3 admission conditions as operational queues.

## Active conditions

- H, I, and HI-S remain candidate or working materials; they are not standards merely because they are wiki-ingested.
- J.0–J.2 remain bounded synthetic implementations and release candidates, not production systems or certifications.
- J.2’s packaged two-build reproducibility claim is valid within its evidence snapshot; cross-run byte-identical parity remains an open condition for J.3.
- External human security, privacy, accessibility, governance, and participant-comprehension review remain outstanding.
- Stage D and Stage E are active, independently verified repository state. Stale “unconfirmed” wording in archived packages remains historical only.
- K has no defined scope and must not be inferred from the current J-stage roadmap.

## Next integration sequence

1. Add concept and attractor bridges for provenance, consent, correction, context, time, memory, governance, and model non-sovereignty.
2. Add H/I cross-links so each public concept maps to its technical specification, schema, example, negative fixture, and validation record.
3. Add graph and search metadata for stage, branch, evidence status, and conformance level.
4. Connect J.0–J.2 evidence to the maintenance and AI-answer surfaces without treating implementation output as theory proof.
5. Prepare the J.3 admission checklist: separate organizational custody, real identity and role lifecycle, observed multi-party exercise, external reviews, networked fault testing, reviewer dispositions, and cross-run release reproducibility.
6. Rebuild, validate, and perform targeted link and graph audits after each integration slice.

## Source precedence

1. The recovered origin transcript governs exact wording, sequence, and provenance.
2. Preserved inbound packages and standard-named source copies govern artifact evidence.
3. The glossary, claim ledger, terminology freezes, and conformance pages govern provisional vocabulary and claim status.
4. The control plane governs current navigation and integration status.
5. Derived summaries and implementation results do not outrank their source artifacts.
