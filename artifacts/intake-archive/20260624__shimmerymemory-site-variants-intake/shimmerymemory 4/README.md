# Shimmery Memory

An Astro site for clean essays plus a playful glyph field.

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

The production output is `dist/`.

## Cloudflare Pages settings

- Framework preset: Astro
- Build command: `npm run build`
- Build output directory: `dist`

## Adding an essay

Create a Markdown file in `src/content/essays/`.

Example:

```md
---
title: "My New Essay"
subtitle: "Optional subtitle"
description: "One-sentence summary for cards, SEO, and previews."
date: 2026-05-27
draft: false
tags:
  - shimmer
  - consent
attribution:
  label: "Shimmery Memory"
  url: "/"
related_elements:
  - label: "P3 — Authorization and Consent Gate"
    site: "Quantum Invariants"
    url: "https://quantuminvariants.com/spine/primitives#P3"
    type: "primitive"
---

Essay body begins here.
```

To hide an essay from the published site, set `draft: true`.
Attribution is optional. Remove the entire `attribution:` block when you do not want a byline/source link.
