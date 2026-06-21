# Work Vault Initial Operating Protocol

## 0. Status

Version: `0.1`
Date initiated: `2026-06-21`
Project type: Git-backed personal work vault, artifact wiki, and AI-managed continuity system.

This document establishes the initial instruction set for creating, maintaining, and evolving a git-native wiki and artifact management system for Bobby Simpson's body of work.

The system is intended to inventory all work files, whether sorted or unsorted; preserve file history; detect duplicates, missing files, added files, moved files, and renamed files; and support AI agents in maintaining a navigable wiki over the entire repository.

The repository is not merely storage. It is intended to become a witnessed, versioned, consent-aware artifact graph over a living body of work.

---

# 1. Initial Impetus

The impetus for this project emerged from the need for a durable wiki of all work files, including files that are already sorted and files that remain unsorted.

The initial concern was not simply "how to organize files," but how to create an architecture that can tolerate disorder, inventory any existing structure, and allow AI management agents to work out duplicates, missing files, added files, moved files, renamed files, and semantic relationships over time.

The core insight:

> If the entire body of work lives inside a large git repository, every artifact can become addressable, versioned, linkable, recoverable, and traceable.

The wiki should therefore not be separate from the files. It should be the human-readable navigation layer over a git-backed artifact substrate.

When a user clicks a link in the wiki, the link should open the relevant file, folder, artifact page, concept page, or index from the repository.

This project begins from the recognition that a body of work is not merely a collection of files. It is a living continuity field made of artifacts, attractors, projects, concepts, drafts, fragments, canon, abandoned paths, and unresolved possibilities.

The repository should preserve this without forcing premature order.

---

# 2. Core Purpose

The purpose of this system is to create a git-backed Work Vault that can:

1. Inventory all files in the repository.
2. Assign stable identities to artifacts independent of file path.
3. Detect duplicate, missing, moved, renamed, added, and modified files.
4. Generate and maintain a wiki over the body of work.
5. Preserve lineage, authorship, context, and transformation history.
6. Distinguish artifacts from attractors.
7. Allow AI agents to propose organization, summaries, classifications, links, and wiki updates.
8. Require explicit human review for destructive, canonical, or meaning-altering changes.
9. Use git commits as witnessed state transitions.
10. Preserve future AI interactions about this project for posterity.

---

# 3. Foundational Distinctions

## 3.1 Artifact vs. Attractor

This system must preserve the distinction between artifacts and attractors.

An artifact is discrete, addressable, stable, captured, and witnessed.

Examples:

- A markdown file.
- A PDF.
- A code file.
- A transcript.
- A diagram.
- A generated summary.
- A committed wiki page.

An attractor is continuous, field-like, evolving, emergent, and inferred.

Examples:

- Consentful provenance.
- ULiUA.
- Abracadoo.
- Semantic Integrity.
- Continuity Office.
- Artifact sovereignty.
- Consent backpropagation.
- The Work Vault itself.

Do not collapse attractors into artifacts.
Do not treat artifacts as the totality of the attractor they point toward.

The wiki should allow artifacts to point toward attractors, and attractors to gather artifacts, without confusing one for the other.

## 3.2 Path Is Not Identity

A file path is not the identity of an artifact.

A file may move.
A file may be renamed.
A file may be copied.
A file may be duplicated.
A file may be superseded.
A file may become missing from the current working tree while still existing in git history.

Artifact identity should be based on stable identifiers such as content hash, manifest ID, or assigned artifact UUID.

The system should track:

- Current path.
- Prior path or paths.
- Content hash.
- File size.
- File type.
- Last witnessed state.
- Related wiki page.
- Duplicate group, if applicable.
- Classification.
- Status.
- Lineage.

---

# 4. Source of Truth

The wiki is not the source of truth.

The source of truth is the combination of:

1. The files themselves.
2. The manifest.
3. Git history.
4. Agent action logs.
5. Human review decisions.

The wiki is a navigable interpretive layer over these sources.

The system should preserve the following division:

```text
Files     = what exists.
Manifest  = what the system knows.
Git       = how things changed.
Wiki      = how humans navigate.
Agents    = how coherence is maintained.
```

---

# 5. Initial Repository Structure

The initial repository should use a structure similar to:

```text
work-vault/
  README.md
  WIKI.md

  artifacts/
    incoming/
    sorted/
    archived/

  wiki/
    index.md
    concepts/
    projects/
    artifacts/
    timelines/
    unresolved/
    duplicate-review.md
    missing-files.md
    incoming-review.md

  manifest/
    inventory.jsonl
    duplicate_sets.json
    hash_index.json
    move_log.jsonl
    missing_log.jsonl
    agent_actions.jsonl
    ai_interactions.jsonl

  scripts/
    inventory.py
    detect_duplicates.py
    reconcile.py
    build_wiki_index.py
    check_links.py

  agents/
    inventory-agent.md
    reconcile-agent.md
    classification-agent.md
    wiki-agent.md
    continuity-agent.md
    canon-agent.md

  .vault/
    config.yaml
    rules.yaml
    schemas/
```

---

# 6. Artifact Spine Filename Convention

When this system initiates new files, it should prefer the Artifact Spine Protocol filename convention:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

Example:

```text
20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-1__initial-vault-operating-protocol.md
```

This naming convention is preferred for new artifacts, especially generated documents, instructions, reports, summaries, canonical pages, and exports.

However, the system must not assume that all existing files follow this convention.

Unsorted, legacy, ambiguous, and externally generated filenames should be inventoried before they are renamed.

---

# 7. Prime Directive

No file should be renamed, moved, deleted, merged, or overwritten until it has first been inventoried.

Initial rule:

> Witness before mutation.

This means the system should first record the previous state of a file before taking any structural action.

For high-impact actions, the agent should propose changes rather than silently applying them.

High-impact actions include:

- Deleting files.
- Merging duplicates.
- Renaming files.
- Moving files across major project/domain boundaries.
- Marking a file as canonical.
- Marking a file as superseded.
- Changing a concept page that affects interpretive structure.
- Rewriting human-authored material.
- Altering lineage metadata.

---

# 8. Core Workflow

The intended workflow is:

```text
Add files
-> Inventory agent witnesses them
-> Reconciliation agent compares current state to previous state
-> Classification agent proposes categories
-> Wiki agent updates navigation
-> Human reviews important structural or canonical changes
-> Git commit records the transition
```

The preferred agent action pattern is:

```text
Observe -> Propose -> Review -> Commit
```

Avoid:

```text
Guess -> Mutate -> Explain after the fact
```

---

# 9. File States

Each file may eventually have a state. States should be stored in metadata, not inferred only from folder location.

Initial states include:

```text
incoming
inventoried
classified
canonical
draft
fragment
duplicate
superseded
archived
missing
external-reference
private
secret
```

Notes:

- `incoming` means the file exists but has not yet been meaningfully classified.
- `inventoried` means the file has been witnessed and recorded.
- `classified` means the system has assigned domain/project/type metadata.
- `canonical` means the human has explicitly marked the artifact as canon-grade.
- `draft` means the file is active but not final.
- `fragment` means the file is partial but potentially meaningful.
- `duplicate` means the file appears to duplicate another artifact.
- `superseded` means the file remains preserved but is no longer the preferred version.
- `archived` means inactive but intentionally retained.
- `missing` means referenced but not present at the expected path.
- `external-reference` means the artifact points outside the repo.
- `private` means not intended for general surfacing.
- `secret` means explicitly restricted and should not be processed, summarized, exported, or disclosed without direct permission.

---

# 10. AI Interaction Log

This project should preserve future AI interactions related to the Work Vault for posterity.

The purpose is not to record every casual exchange, but to preserve meaningful AI interactions that affect the design, operation, interpretation, or evolution of the system.

AI interaction logs should be stored at:

```text
manifest/ai_interactions.jsonl
```

Each record should include:

```json
{
  "timestamp": "2026-06-21T00:00:00",
  "interaction_id": "AIINT-20260621-0001",
  "agent_or_model": "unknown",
  "human": "Bobby Simpson",
  "context": "Initial planning conversation",
  "summary": "Established the need for a git-backed wiki and AI-managed artifact inventory system.",
  "key_decisions": [],
  "resulting_artifacts": [],
  "open_questions": [],
  "posterity_notes": ""
}
```

---

# 11. Instruction Compression

## 11.1 Ultra-Compressed Instruction

```text
Maintain a git-backed Work Vault where files are witnessed before mutation, artifacts have stable identities independent of paths, the manifest and git history are sources of truth, the wiki is a navigational layer, AI agents propose before changing high-impact structure, duplicates/missing/moved files are reconciled through reviewable logs, artifacts and attractors remain distinct, canonization requires human witness, and meaningful AI interactions are recorded for posterity.
```

## 11.2 Short Operational Instruction

```text
Before changing files, inventory them. Treat file paths as mutable locations, not identities. Use hashes and manifest IDs to track artifacts. Preserve git history as witnessed lineage. Generate wiki pages from manifest state where possible. Separate artifacts from attractors. Let AI agents propose organization, classification, deduplication, and wiki updates, but require human review for destructive, structural, or canon-level changes. Record meaningful AI interactions in the AI interaction log.
```

## 11.3 Agent Safety Compression

```text
Do not silently delete, overwrite, merge, rename, move, canonize, or supersede files. First inventory, then propose, then await review unless explicitly authorized. Preserve uncertainty. Prefer reversible git-tracked changes.
```

---

# 12. Future AI Interaction Entry Template

Use this template after meaningful AI sessions about this project.

```json
{
  "timestamp": "",
  "interaction_id": "",
  "interaction_type": "",
  "agent_or_model": "",
  "human": "Bobby Simpson",
  "context": "",
  "summary": "",
  "key_decisions": [],
  "files_discussed": [],
  "files_created": [],
  "files_modified": [],
  "concepts_affected": [],
  "open_questions": [],
  "next_recommended_actions": [],
  "posterity_notes": ""
}
```

Suggested interaction ID format:

```text
AIINT-YYYYMMDD-0001
```

---

# 13. First Posterity Entry

```json
{
  "timestamp": "2026-06-21T00:00:00",
  "interaction_id": "AIINT-20260621-0001",
  "interaction_type": "planning",
  "agent_or_model": "GPT-5.5 Thinking",
  "human": "Bobby Simpson",
  "context": "Initial design conversation for a git-backed wiki and AI-managed artifact inventory system.",
  "summary": "The initial need was articulated as a desire for a wiki of all work files, including sorted and unsorted files. The conversation clarified that the deeper need is an inventoryable, git-backed artifact graph where AI agents can detect duplicates, missing files, added files, moved files, renamed files, and semantic relationships, while maintaining a wiki that opens directly into repository-backed artifacts.",
  "key_decisions": [
    "Host the entire work system inside a large git repository.",
    "Make every element of the wiki link into the repository.",
    "Separate artifacts, wiki pages, manifests, scripts, agents, and configuration.",
    "Treat file identity as independent from file path.",
    "Use inventory before organization.",
    "Use AI agents to propose reconciliation rather than silently mutate the repository.",
    "Use git commits as witnessed state transitions.",
    "Preserve meaningful future AI interactions for posterity."
  ],
  "files_discussed": [],
  "files_created": [
    "20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-1__initial-vault-operating-protocol.md"
  ],
  "files_modified": [],
  "concepts_affected": [
    "Work Vault",
    "Artifact graph",
    "Git-backed wiki",
    "Artifact vs Attractor",
    "Consentful provenance",
    "Witness before mutation",
    "AI-managed continuity"
  ],
  "open_questions": [
    "Which git host will be used?",
    "Will the repository be public, private, or mixed?",
    "What file types should be indexed first?",
    "Should large binaries be stored directly in git, Git LFS, or an adjacent object store?",
    "What level of AI autonomy is acceptable for different action classes?",
    "What local tools should power the first inventory pass?"
  ],
  "next_recommended_actions": [
    "Create the initial repository skeleton.",
    "Add this operating protocol to the repository root or docs folder.",
    "Create the first inventory script.",
    "Run a baseline inventory before moving or renaming files.",
    "Commit the baseline as the first witnessed state."
  ],
  "posterity_notes": "This project began from the recognition that organization should not require pretending the existing body of work is already clean. The system should meet the work where it is, witness it, and gradually make it navigable without destroying ambiguity or lineage."
}
```

---

# 14. Human Review Thresholds

AI agents may generally perform low-risk actions when explicitly instructed.

Low-risk examples:

- Generate reports.
- Create proposed wiki pages.
- Create summaries.
- Detect duplicates.
- Check links.
- Add non-destructive metadata.
- Create review queues.

AI agents should request or record explicit approval before high-risk actions.

High-risk examples:

- Delete files.
- Merge files.
- Rename files.
- Move files across major categories.
- Rewrite source artifacts.
- Mark artifacts as canonical.
- Mark artifacts as superseded.
- Publish or expose private material.
- Process anything marked `secret`.

---

# 15. Commit Message Convention

Git commits should describe witnessed state transitions.

Examples:

```text
inventory: add baseline manifest
wiki: generate initial project index
reconcile: add duplicate review report
manifest: record moved artifacts
canon: mark consentful provenance essay as canonical
agents: add initial reconciliation instructions
posterity: record initial AI planning interaction
```

Commit messages should be boring, legible, and reversible.

---

# 16. Opening Principle

The Work Vault should make the body of work more navigable without forcing premature closure.

It should preserve ambiguity where ambiguity is real.

It should distinguish between what exists, what is known, what is inferred, what is canonical, what is obsolete, and what remains unresolved.

The highest-level principle:

> Witness before mutation.
> Preserve lineage before optimization.
> Let artifacts remain artifacts.
> Let attractors remain alive.
