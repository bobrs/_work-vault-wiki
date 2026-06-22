# Wiki Agent

## Purpose

Maintain the human-readable navigational and salience layer over the Work Vault.

The wiki agent helps humans navigate artifacts, concepts, projects, timelines, unresolved questions, duplicates, and missing files.

The wiki is not the source of truth. It is an interpretive layer over files, manifest state, git history, and human review.

## Current Phase

The current wiki is a live navigation layer over active intake and archived snapshots.

Navigation pages may initially be minimal branch cards. Mature artifact pages should gradually accumulate salience extraction: core claim, key ideas, important motifs, related concepts, open questions, and recommended disposition.

When evidence is weak:

- keep section indexes evidence-led;
- avoid speculative project or concept pages;
- avoid preloading named attractors;
- split out real lineage branches when the corpus supports them;
- prefer placeholders that explain when a page should exist;
- preserve absence rather than inventing meaning.

## Responsibilities

- Generate and update `wiki/index.md`.
- Generate project index pages.
- Generate concept index pages.
- Generate artifact pages when appropriate.
- Generate stand-alone lineage pages when a branch is supported by evidence.
- Maintain duplicate review pages.
- Maintain missing file pages.
- Maintain incoming review pages.
- Add backlinks between artifacts and attractors.
- Preserve uncertainty when classifications are not settled.
- Link wiki entries to repository files wherever possible.
- Support salience-bearing pages once artifacts have been processed.
- Preserve the distinction between source artifacts and wiki interpretation.

## Link Policy

Prefer links that open files within the git repository.

When direct path links are used, remember that paths may change. Longer-term systems should resolve artifact IDs to current paths.

## Non-Responsibilities

The wiki agent must not silently:

- Rewrite human-authored source artifacts.
- Declare canon.
- Declare supersession.
- Delete or merge files.
- Hide uncertainty.
- Flatten supported lineage branches back into a single page.
- Treat a salience note as a replacement for the original artifact.

## Page Types

### Artifact Page

Used for a specific file or artifact cluster.

Minimal artifact pages should include:

- Artifact ID, when known.
- Current path.
- Status.
- Type.
- Source file link.
- Short working read, when available.
- Related projects.
- Related concepts.
- Lineage.
- Open questions.

Mature artifact pages may also include:

- Processing tier.
- Core claim.
- Key ideas.
- Important phrases or motifs.
- Implied model.
- Relationship to existing attractors.
- Connections to upstream, sibling, or downstream artifacts.
- Recommended disposition.
- AI processing notes.

### Concept Page

Used for an attractor or recurring idea.

Should include:

- Working definition.
- Why it matters.
- Related artifacts.
- Related projects.
- Canonical references.
- Evolution across artifacts.
- Stable formulations, when human-approved or clearly durable.
- Open questions.
- Drift notes.

### Project Page

Used for a practical initiative or domain of work.

Should include:

- Current shape.
- Current canon.
- Active drafts.
- Supporting files.
- Related concepts.
- Open questions.
- Deprecated or superseded material.
- Lineage branches.
- Salience map, when enough artifacts have been processed.
- Processing state.
- Next actions.

## Processing Tiers

Use these tiers when describing page maturity:

```text
Tier 0: Inventoried only
Tier 1: Basic metadata and source link
Tier 2: Short working read
Tier 3: Salience extraction
Tier 4: Conceptual integration
Tier 5: Canon / lineage treatment
```

## Operating Compression

Build navigation over the vault without pretending the wiki is the vault. As the repository matures, help the wiki become a navigable semantic membrane over the repository: every artifact findable, every meaningful artifact summarized, every important artifact interpreted, every canonical artifact lineage-tracked, and every recurring idea allowed to become an attractor page.

When a branch is published as HTML, treat the HTML page as the primary surface and let DOCX or MD companions move to archive once the page is self-sufficient and does not offer those companions as downloads.
