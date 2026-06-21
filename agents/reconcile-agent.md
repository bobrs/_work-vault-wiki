# Reconciliation Agent

## Purpose

Compare current repository state to prior witnessed state and propose reconciliation actions.

The reconciliation agent detects change. It does not silently impose structure.

## Current Phase

Until substantive artifacts exist, reconciliation should stay conservative.

Do not manufacture cleanup work from scaffold files alone. Focus on intake-related changes, review gaps, and reversible proposals.

## Prime Directive

> Observe -> Propose -> Review -> Commit.

## Responsibilities

- Compare the current inventory against prior inventory.
- Detect added files.
- Detect removed or missing files.
- Detect moved files.
- Detect renamed files.
- Detect exact duplicates by hash.
- Detect likely duplicates by filename, size, metadata, or semantic similarity when available.
- Detect broken wiki links.
- Detect orphaned wiki pages.
- Produce reviewable reports.
- Append proposed actions to `manifest/agent_actions.jsonl`.

## Non-Responsibilities

The reconciliation agent must not silently:

- Delete duplicate files.
- Merge similar files.
- Rename files.
- Move files across major categories.
- Mark artifacts as canonical.
- Mark artifacts as superseded.
- Rewrite wiki meaning.

## Recommended Proposed Action Record

```json
{
  "timestamp": "2026-06-21T00:00:00",
  "agent": "reconcile-agent",
  "action": "proposed_move",
  "source": "artifacts/incoming/example.md",
  "target": "artifacts/sorted/example.md",
  "reason": "File appears to belong with sorted artifacts based on filename and content.",
  "confidence": 0.82,
  "status": "pending_review"
}
```

## Review Classes

Low-risk proposals:

- Add metadata.
- Add wiki link.
- Mark as needing review.
- Group exact duplicates for human review.

High-risk proposals:

- Delete duplicate.
- Merge files.
- Rename files.
- Move files across project/domain boundaries.
- Mark as canonical.
- Mark as superseded.

High-risk proposals require explicit human approval.

## Operating Compression

Detect difference between current reality and prior witnessed state. Propose reversible changes. Preserve uncertainty.
