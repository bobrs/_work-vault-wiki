# Work Vault Semantic Compression and Link Seeding Addendum

## 0. Status

Version: `0.6`
Date initiated: `2026-06-22`
Scope: semantic processing, document digestion, artifact salience extraction, mature wiki page expectations, and deliberate link seeding.

This addendum supplements the active Work Vault operating protocol.

The repository has established intake, witnessing, lineage, navigation, and salience layers. This addendum clarifies the next intended layer: the wiki should become a semantic map of the work, not merely a structured menu of source documents.

---

# 1. Core Clarification

The wiki has two valid phases:

1. **Navigation phase**: identify what exists, where it lives, what branch it belongs to, and what source files support it.
2. **Salience phase**: extract and preserve the meaningful content, claims, motifs, definitions, relationships, implications, and useful cross-links of important documents.

The current structure may begin as navigation. It should not stop there.

When a project already has stable wiki pages, semantic extraction should take precedence over new intake. The goal is to make the existing pages materially better before widening the surface area.

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
Where should new links be planted?
```

The source document remains the artifact of record. The wiki page becomes the semantic interface to that artifact.

---

# 2. Source Document vs. Wiki Page

Do not treat wiki pages as replacements for source documents.

A source document is the artifact.

A wiki page is the navigational, interpretive, and relational layer around the artifact.

The wiki page should make the document more discoverable, legible, and connectable without pretending to fully contain or replace it.

For small or low-priority files, a wiki entry may remain a short navigation card.

For meaningful files, the wiki page should include a salience extraction and a short semantic compression.

For canon-grade or highly connected files, the wiki page should include deeper synthesis, lineage, concept integration, and explicit downstream links.
For foundational projects already represented in the wiki, extend the page content first and add only the structural minimum needed to keep the branch legible.

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
- deliberate link seeds

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

# 4. Semantic Compression Rule

Durable pages should not stop at a label and a link list.

When a file or branch reads as durable, the wiki page should usually include a few paragraphs of semantic compression:

- one paragraph summarizing the document or branch in plain language
- one paragraph naming the core claims, motifs, or function
- one paragraph describing relationships, tensions, implications, or downstream uses
- several more paragraphs when the material is central to the project and the page can support a fuller semantic read

For especially important artifacts or branches, page-length synthesis is appropriate if the material warrants it.

Do not force every page to become long-form. Use semantic compression when the page is durable, high-value, or structurally central.

---

# 5. Link Seeding Rule

Wiki pages should include deliberate places to connect related work.

Use sections such as:

- Related artifacts
- Parent lineage
- Sibling pages
- Downstream links
- Upstream links
- Possible attractor pages
- Open questions
- Cross-project echoes

Seed links even when they are provisional, but label them clearly if they are tentative.

The goal is to make the wiki a place where new connections can be added without rewriting the page structure.

---

# 6. Mature Artifact Page Template

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

## Suggested Links

- Link seed 1
- Link seed 2
- Link seed 3
```

---

# 7. Source Priority

The source document remains the artifact of record.

The wiki page is the semantic interface and should summarize, connect, and orient without replacing the source.
