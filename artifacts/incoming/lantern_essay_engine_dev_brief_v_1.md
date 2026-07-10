# Lantern Essay Engine — Dev Brief (v1)

## Purpose

Build a **single Next.js codebase** that can serve **multiple domains** (e.g. howtrustworks.com, howeverthingworks.com, polememelop.com), each hosting **single-page essays** with a **dimension selector** that lets readers switch conceptual lenses on the same content.

This is a **static‑first essay engine**.
- Git is the CMS.
- No admin UI in v1.
- Fast, legible, intentional pages.

Conceptually: *How one thing works is how everything works.*  
Structurally: *All branches lead to the root.*

---

## Core Requirements (Non‑Negotiable)

1. **Multi‑domain support from one repo**  
   One codebase must serve multiple domains, with per‑domain configuration.

2. **Essays are single pages**  
   Each essay renders as one page (no pagination), with a clean reading experience.

3. **Dimension selector**  
   Essays can be viewed through multiple conceptual “dimensions” (lenses), switchable at runtime without page reload.

4. **Invariant references**  
   Essays can reference canonical “invariants” fetched from quantuminvariants.com (JSON‑fed, programmatic).

5. **Root‑trail footer**  
   Every page must render a footer that points inward toward a defined root (ultimately polememelop.com). This should be hard to accidentally break.

6. **Static‑first, versioned by Git**  
   Content lives in the repo. Publishing == merge.

---

## Recommended Stack (Flexible)

Defaults (can be adjusted if there’s a strong reason):

- **Next.js (App Router)**
- **TypeScript**
- **MDX** for content
- Static generation preferred where possible

You are free to choose:
- MDX tooling (next-mdx-remote, @next/mdx, Contentlayer, etc.)
- Styling system (Tailwind, CSS modules, etc.)
- Data caching strategy

As long as the **content contracts** below are honored.

---

## Multi‑Domain Architecture

### Goal

One repo → many domains.

Each request resolves to a `siteId`, which controls:
- Which essays are available
- Footer root‑trail
- Theming / tone (later)

### Acceptable Approaches

**Option A — Middleware host routing (preferred)**
- `middleware.ts` inspects `Host` header
- Maps domain → `siteId`
- Rewrites internally (e.g. `/_sites/howtrustworks/...`)

**Option B — Multiple deploys from one repo**
- Each deploy sets `SITE_ID` env var
- Simpler runtime, more deploy config

Either approach is fine.

---

## Content Structure

### Folder Layout (illustrative)

```
/content
  /howtrustworks
    /essays
      /trust-is-a-loop
        index.mdx
        /dimensions
          simple.mdx
          formal.mdx
  /howeverthingworks
    /essays
      /how-one-thing-works
        index.mdx
```

### Essay = Directory

Each essay lives in its own folder and is addressable by slug.

---

## MDX Frontmatter Contract

Each `index.mdx` must support the following frontmatter fields:

- `title` — string
- `description` — string
- `slug` — string
- `defaultDimension` — string key
- `dimensions` — array of `{ key, label }`
- `tags` — string[] (lightweight metadata)
- `rootTrail` — array of `{ label, url }`
- `draft` — optional boolean

Example (conceptual):

- dimensions:
  - `{ key: "simple", label: "ALIF" }`
  - `{ key: "formal", label: "Formal" }`
- defaultDimension: `"simple"`

---

## Dimension System (v1)

### What a Dimension Is

A **dimension** is a conceptual lens on the same essay:
- different wording
- different emphasis
- possibly different invariant references

### Required Behavior

- Reader can switch dimensions at runtime
- No full page reload
- UI can be tabs or segmented control (slider optional later)
- Optional URL sync (`?d=formal`) is a nice‑to‑have

### Acceptable Implementations

**Approach A — Separate MDX per dimension (recommended)**
- Each dimension has its own MDX partial
- Selector swaps which partial renders

**Approach B — Conditional sections inside one MDX**
- Custom `<Dimension>` component controls visibility

Keep it simple in v1.

---

## Invariants Integration

Provide a small component API usable inside MDX:

- `<Invariant id="sovereignty" />`
- `<InvariantCard id="consent-loop" />`

Implementation details:
- Fetch invariant definitions from quantuminvariants.com (JSON endpoint)
- Cache appropriately (build‑time or runtime cache)
- Render readable inline or card UI

Fancy UX is not required in v1; clarity is.

---

## Footer: “All Branches Lead to the Root”

Every page must render a **root‑trail footer**.

### Root‑Trail

An ordered list of links pointing inward, e.g.:

- How Everything Works → howeverthingworks.com
- POLEMEMELOP → polememelop.com

### Enforcement

- Root‑trail should come from a **central site config**
- Essays may override only if explicitly needed
- Default behavior must always include the inward path

---

## Tags & Dependencies (Intentionally Light in v1)

We are **not** building a dependency graph yet.

For now:
- `tags: string[]` exist as metadata
- Optional future hook:
  - `dependencyTags`
  - `dependencyPaths` (unused in v1)

The **dimension selector** is the proto‑mechanism for multiple paths. Don’t overbuild.

---

## Git‑Based Workflow

- Content edits via PRs
- Merge = publish
- Rollbacks via Git

Optional (nice to have):
- `draft: true` hides essays from index in prod
- Basic sitemap generation

---

## v1 Deliverables Checklist

- [ ] Multi‑domain routing working locally and in prod
- [ ] Essay index per site
- [ ] Essay page rendering MDX
- [ ] Dimension selector switching content
- [ ] Invariant component fetching JSON
- [ ] Root‑trail footer enforced
- [ ] Minimal README: “How to add an essay + dimension”

---

## Freedom to Play (Encouraged)

You have freedom in:
- MDX plumbing
- Domain routing strategy
- Styling system
- Caching & performance tactics
- Dimension UI design

Please **do not change** without discussion:
- Content contracts (frontmatter keys)
- Invariant component API
- Guaranteed presence of root‑trail footer

---

## Guiding Principle

This system should feel like **lanterns in a fog**:
- Each page self‑contained
- Orientation always visible
- Depth without overwhelm

We will iterate. v1 should be elegant, simple, and structurally honest.

