# Work Vault Semantic Salience Addendum

## 0. Status

Version: `0.5`  
Date initiated: `2026-06-22`  
Scope: semantic processing, document digestion, artifact salience extraction, and mature wiki page expectations.

This addendum supplements the active Work Vault operating protocol.

The repository has successfully established the intake, witnessing, lineage, and navigation layers. This addendum clarifies the next intended layer: the wiki should gradually become a semantic map of the work, not merely a structured menu of source documents.

---

# 1. Core Clarification

The wiki has two valid phases:

1. **Navigation phase**: identify what exists, where it lives, what branch it belongs to, and what source files support it.
2. **Salience phase**: extract and preserve the meaningful content, claims, motifs, definitions, relationships, and implications of important documents.

The current structure may begin as navigation. It should not stop there.

The mature wiki should answer:

```text
What is this?
Why does it matter?
What does it claim?
What concepts does it affect?
What phrases, motifs, or definitions should be preserved?
What does it connect to?
What changed in the map because this artifact exists?
Should the original be read?
```

The source document remains the artifact of record. The wiki page becomes the semantic interface to that artifact.

---

# 2. Source Document vs. Wiki Page

Do not treat wiki pages as replacements for source documents.

A source document is the artifact.

A wiki page is the navigational, interpretive, and relational layer around the artifact.

The wiki page should make the document more discoverable, legible, and connectable without pretending to fully contain or replace it.

For small or low-priority files, a wiki entry may remain a short navigation card.

For meaningful files, the wiki page should eventually include a salience extraction.

For canon-grade or highly connected files, the wiki page should include deeper synthesis, lineage, and concept integration.

---

# 3. Processing Tiers

Every file should be inventoried, but not every file deserves equal semantic treatment.

Use these tiers:

```text
Tier 0: Inventoried only
Tier 1: Basic metadata and source link
Tier 2: Short working read
Tier 3: Salience extraction
Tier 4: Conceptual integration
Tier 5: Canon / lineage treatment
```

## Tier 0: Inventoried Only

The file exists in the manifest and can be found.

Minimum state:

- artifact ID
- current path
- hash
- file type
- inventory timestamp

## Tier 1: Basic Metadata and Source Link

The wiki knows where the file belongs.

Minimum page content:

- title
- source file link
- parent project or lineage
- file count
- status

## Tier 2: Short Working Read

The wiki contains a short description.

Minimum page content:

- short summary
- provisional interpretation
- next action

## Tier 3: Salience Extraction

The wiki captures the meaningful content of the document.

Recommended sections:

- core claim
- key ideas
- important phrases or motifs
- definitions
- implied model
- tensions or unresolved questions
- related artifacts
- related concepts
- recommended disposition

## Tier 4: Conceptual Integration

The wiki relates the document to the larger work field.

Recommended sections:

- upstream concepts
- downstream implications
- sibling artifacts
- precursor artifacts
- later echoes
- possible attractor page links
- synthesis notes
- drift notes

## Tier 5: Canon / Lineage Treatment

The artifact has human-witnessed importance.

Recommended sections:

- canon status
- canon decision record
- supersession relationship, if any
- lineage chain
- stable formulation
- extracted principles
- known descendants
- human approval note

Canonization remains a human decision.

---

# 4. Mature Artifact Page Template

When a document is processed beyond basic navigation, use this structure where appropriate:

```markdown
# [Artifact Title]

Parent lineage: `[Parent Project or Corpus]`

Status: `inventoried | draft | fragment | candidate-canon | canonical | superseded | archived`  
Processing tier: `0 | 1 | 2 | 3 | 4 | 5`

## Source Artifact

- Source file:
- Artifact ID:
- Current path:
- File type:
- Hash:
- Inventory record:

## Working Read

Short plain-language description of what this document appears to be.

## Core Claim

The central claim, function, or movement of the document.

## Key Ideas

- Idea 1
- Idea 2
- Idea 3

## Important Phrases / Motifs

Preserve exact or near-exact phrases only when they are important as formulations.

- Phrase or motif 1
- Phrase or motif 2

## Implied Model

What model of reality, agency, consent, selfhood, organization, language, or system behavior does this artifact imply?

## Relationship to Existing Attractors

- Related concept:
- Related project:
- Related canon:
- Possible new attractor:

## Connections

- Upstream artifacts:
- Sibling artifacts:
- Downstream artifacts:
- Contrasts or tensions:

## Open Questions

- Question 1
- Question 2

## Recommended Disposition

Possible values:

- leave as navigational card
- summarize only
- perform full salience extraction
- integrate into concept page
- mark as candidate canon
- archive as auxiliary
- preserve as fragment
- review for supersession

## AI Processing Notes

Record the date, agent/model, and nature of the processing pass.

This section should not pretend certainty. It should preserve uncertainty and interpretation boundaries.
```

---

# 5. Mature Project Page Expectations

A project page should not merely list branches. It should eventually show the project's current semantic state.

Recommended sections:

```markdown
# [Project Name]

## Current Shape

What the project currently appears to be.

## Current Canon

Human-approved durable formulations.

## Active Branches

Branches that have enough evidence to stand alone.

## Source Artifacts

Important source files and clusters.

## Salience Map

The major claims, motifs, unresolved tensions, and emergent attractors in this project.

## Related Concepts

Links to concept pages.

## Open Questions

Unresolved conceptual or structural questions.

## Processing State

What has been inventoried, summarized, extracted, integrated, or canonized.
```

---

# 6. Mature Concept Page Expectations

A concept page should represent an attractor, not a single artifact.

Recommended sections:

```markdown
# [Concept Name]

## Working Definition

Current best formulation.

## Why It Matters

What role this concept plays in the larger body of work.

## Source Artifacts

Artifacts that express, develop, challenge, or refine the concept.

## Evolution

How the concept has changed across time.

## Stable Formulations

Human-approved or highly durable phrasing.

## Open Tensions

Where the concept remains unstable or contested.

## Related Concepts

Sibling, parent, child, or contrasting attractors.

## Canon Status

Whether this is merely emergent, candidate canon, or explicitly canonical.
```

---

# 7. Salience Extraction Agent

Create or activate a Salience Agent when the repository is ready.

## Purpose

Extract the meaningful content of artifacts into wiki-compatible summaries without replacing the source artifacts.

## Responsibilities

- Read source artifacts when technically available.
- Produce short summaries.
- Identify core claims.
- Extract important motifs and formulations.
- Suggest related concepts.
- Suggest related projects.
- Identify open questions.
- Identify possible canon candidates.
- Preserve uncertainty.
- Avoid over-compressing subtle documents into generic summaries.
- Avoid inventing meaning when evidence is weak.

## Restrictions

The Salience Agent must not:

- Rewrite the source artifact.
- Mark an artifact canonical.
- Delete, merge, or move files.
- Treat its interpretation as final.
- Collapse an attractor into a single artifact.
- Quote long passages unnecessarily.
- Fill sections with invented certainty.

## Operating Compression

Extract what matters from the artifact into the wiki while preserving the source artifact, uncertainty, lineage, and human authority over canon.

---

# 8. Processing Workflow

The intended mature workflow is:

```text
Inventory
↓
Duplicate / missing / movement reconciliation
↓
Basic navigation page
↓
Short working read
↓
Salience extraction
↓
Concept and project integration
↓
Human canon review where appropriate
```

Do not skip inventory.

Do not require salience extraction for every file before navigation exists.

Do not wait for perfect classification before creating a useful working read.

---

# 9. Indicators That a Page Needs Salience Processing

A page is likely ready for salience processing when:

- it represents a philosophical essay;
- it contains original conceptual language;
- it names or implies a recurring attractor;
- it has a strong working read but no extracted claims;
- it appears to connect to multiple projects;
- it may contain canonical phrasing;
- it feels disproportionately important relative to its file size;
- a human asks, "what does this document actually say or change?"

---

# 10. Indicators That a Page Should Remain a Navigation Card

A page may remain a navigation card when:

- the source file is administrative;
- the content is auxiliary;
- the file is a duplicate or export companion;
- the file is not yet readable by available tooling;
- the page exists only to preserve branch structure;
- the meaning is not yet clear enough to summarize responsibly.

---

# 11. Core Rule

The wiki should eventually become:

```text
a navigable semantic membrane over the repository
```

not merely:

```text
a file tree with nicer links
```

Every artifact should be findable.

Every meaningful artifact should be summarized.

Every important artifact should be interpreted.

Every canonical artifact should be lineage-tracked.

Every recurring idea should be allowed to become an attractor page.

The original artifact should always remain one click away.
