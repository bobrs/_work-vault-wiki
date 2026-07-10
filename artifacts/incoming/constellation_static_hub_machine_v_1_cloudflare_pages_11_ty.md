# Constellation Static Hub Machine v1

**Goal:** many branded hubs (one domain per hub), shared theme, global/nested navigation across hubs, minimal friction for publishing essays, deployed on Cloudflare Pages. Designed so you can **start with any root** (e.g., ULiUA) and later **promote/re-parent** (e.g., Polememelop becomes the parent) by editing a single nav graph.

---

## Core design principle

Navigation is **data**, not layout.

Each site declares **only** its identity key (e.g., `uliua`, `howacceptanceworks`). The global constellation graph defines hierarchy, nesting, labels, and URLs. The theme renders nav/breadcrumbs dynamically from that graph.

This makes restructuring (e.g., inserting Polememelop above ULiUA) a **one-file change**.

---

## Stack

- **11ty (Eleventy)** for static generation
- **Cloudflare Pages** for hosting + deploy previews
- **GitHub** for source control
- **Shared theme as npm package** (`@polememelop/theme` or `@ulilua/theme`)
- **Shared constellation graph as npm package** (`@polememelop/constellation`) or bundled into theme for v1

Recommended: theme + nav graph as **separate packages** once you’re adding hubs frequently. For v1, bundling nav inside theme is acceptable.

---

## Repo layout (recommended: multi-repo)

### 1) `constellation-nav` (npm package)
**Purpose:** single source of truth for the constellation graph.

**Files:**
- `package.json`
- `constellation.json`

**Example `constellation.json` (node graph form):**
```json
{
  "nodes": {
    "uliua": {
      "title": "ULiUA",
      "url": "https://uliua.com",
      "parent": null,
      "order": 10
    },
    "howonething": {
      "title": "How One Thing Works",
      "url": "https://howonething.work",
      "parent": "uliua",
      "order": 20
    },
    "howacceptanceworks": {
      "title": "How Acceptance Works",
      "url": "https://howacceptanceworks.com",
      "parent": "howonething",
      "order": 10
    },
    "howegoworks": {
      "title": "How Ego Works",
      "url": "https://howegoworks.com",
      "parent": "howonething",
      "order": 20
    }
  }
}
```

**Why node graph form?**
- Easy to re-parent: change one `parent` field.
- Theme can compute children, breadcrumbs, nesting.

**Promotion example (later): Polememelop above ULiUA**
Add:
```json
"polememelop": {
  "title": "Polememelop",
  "url": "https://polememelop.com",
  "parent": null,
  "order": 5
}
```
Change:
```json
"uliua": { "parent": "polememelop", ... }
```
No hub repos change.

---

### 2) `theme` (npm package)
**Purpose:** brand + layouts + nav rendering + post listings + tags.

**Files (illustrative):**
- `package.json`
- `src/` (theme implementation)
  - `_includes/`
    - `layouts/base.njk`
    - `partials/nav.njk`
    - `partials/footer.njk`
  - `_data/` (theme defaults)
    - `theme.json`
  - `assets/` (css, fonts, icons)
- `index.js` (exports 11ty plugin)

**Theme responsibilities:**
- Render global header/nav from `constellation.json`
- Highlight current hub based on `constellationKey`
- Compute breadcrumbs by walking `parent` pointers
- Provide consistent typography + components
- Provide collections: `posts`, `tags`

**Theme consumes nav graph** via dependency:
- `constellation-nav` added to `theme` dependencies, OR
- `constellation-nav` added to each hub and passed to theme.

---

### 3) Hub template repo (`hub-template`)
**Purpose:** minimal hub that installs theme + declares identity.

**Files:**
- `package.json`
- `.eleventy.js`
- `site.json` (hub identity)
- `content/` (markdown)
  - `index.md`
  - `about.md`
  - `posts/` (essays)

**Example `site.json`:**
```json
{
  "constellationKey": "howacceptanceworks",
  "siteName": "How Acceptance Works",
  "siteUrl": "https://howacceptanceworks.com",
  "description": "Essays and tools for acceptance → unconditional love.",
  "brand": {
    "accent": "acceptance"
  }
}
```

**Hub responsibilities:**
- Content only
- Small hub settings
- No nav duplication
- No layout duplication

---

## How nav + nesting works

The theme builds an in-memory tree at build-time:
1. Load `constellation.json`
2. Compute children lists for each node
3. Identify current node via `site.constellationKey`
4. Render:
   - Top nav: top-level children of the current root (or global root)
   - Nested dropdowns: children-of-children recursively
   - Breadcrumbs: current → parent → ... → root

**Key: root is not hardcoded.**
You can choose:
- global root = the node with `parent=null` and lowest `order`
- OR a configured root for each build (e.g., show Polememelop-level nav everywhere)

v1 suggestion: theme chooses global root automatically.

---

## Cloudflare Pages deployment contract

Each hub repo is a Cloudflare Pages project:
- Build command: `npm ci && npm run build`
- Output dir: `_site`
- Node version: set in Pages settings if needed

Pages provides:
- Automatic deploys on push
- Preview deploys on PRs
- Custom domain attachment per hub

---

## “One command creates a hub” automation plan

### Script: `newhub`
Inputs:
- `repo_name` (e.g., `howacceptanceworks`)
- `domain` (e.g., `howacceptanceworks.com`)
- `title` (e.g., `How Acceptance Works`)
- `constellationKey` (usually same as repo)

Actions:
1. Create repo from `hub-template` via GitHub CLI
2. Fill `site.json` values
3. Initial commit + push
4. Create Cloudflare Pages project (CLI/API)
5. (Optional v2) Attach custom domain + create DNS record

### What changes when you add Polememelop as parent?
Only `constellation.json` changes (in `constellation-nav`).
Then:
- bump `constellation-nav` version
- hubs update dependency (can be batched later)

If you bundle nav in theme instead:
- bump `theme` version and update hubs.

---

## Versioning strategy

- Theme version changes when:
  - brand/layout/components change
  - nav rendering logic changes

- Nav graph version changes when:
  - you add/re-parent/rename nodes
  - you change URLs

This keeps “structure edits” lightweight.

---

## Minimal publishing workflow

For any hub:
1. Create a new markdown file in `content/posts/` with frontmatter:
```md
---
title: "Why acceptance opens the gate"
date: 2026-02-19
tags: [acceptance, practice]
---

Essay body...
```
2. `git push`
3. Cloudflare Pages deploys; nav stays consistent

---

## v1 scope (keep it shippable)

**Ship v1 with:**
- Theme + nav graph
- 1 hub deployed (start wherever you like)
- Hub template
- Manual custom-domain attach in CF Pages

**Then v1.1:**
- `newhub` script to automate repo creation + first deploy

**Then v1.2:**
- Full domain/DNS automation via Cloudflare API

---

## Naming (suggestion)

- `@polememelop/constellation` — the graph
- `@polememelop/theme` — the brand + rendering
- Hub repos named after domain intent (`howacceptanceworks`, `uliua`, etc.)

You can start with `uliua` as root and later insert `polememelop` above it by editing only `@polememelop/constellation`.



---

# Executable v1 (Concrete Scaffolds)

This section makes v1 **runnable**: exact repo trees + minimal file contents + commands. The intent is: you can copy-paste these into repos (or generate them) and get a working constellation hub on Cloudflare Pages.

## What “executable v1” guarantees

- You can build and serve any hub locally: `npm ci && npm run dev`
- You can build output to `_site`: `npm run build`
- Each hub has:
  - Home page
  - Posts collection (markdown essays)
  - Tag pages
  - RSS
  - Global/nested nav (from constellation graph)
  - Breadcrumbs

**v1 does not require** automation for Cloudflare domain attach; you can do that in UI. (We’ll add it in v1.2.)

---

## Repo 1: `@polememelop/constellation` (npm package)

### Tree
```
constellation-nav/
  package.json
  constellation.json
  README.md
```

### `package.json`
```json
{
  "name": "@polememelop/constellation",
  "version": "0.1.0",
  "private": false,
  "type": "module",
  "files": ["constellation.json"],
  "exports": {
    "./constellation.json": "./constellation.json"
  }
}
```

### `constellation.json` (start with ULiUA-root; promote later)
```json
{
  "nodes": {
    "uliua": {
      "title": "ULiUA",
      "url": "https://uliua.com",
      "parent": null,
      "order": 10
    },
    "howonething": {
      "title": "How One Thing Works",
      "url": "https://howonething.work",
      "parent": "uliua",
      "order": 20
    },
    "howacceptanceworks": {
      "title": "How Acceptance Works",
      "url": "https://howacceptanceworks.com",
      "parent": "howonething",
      "order": 10
    },
    "howegoworks": {
      "title": "How Ego Works",
      "url": "https://howegoworks.com",
      "parent": "howonething",
      "order": 20
    },
    "howhappinessworks": {
      "title": "How Happiness Works",
      "url": "https://howhappinessworks.com",
      "parent": "howonething",
      "order": 30
    }
  }
}
```

### Later “promotion” to Polememelop
To insert Polememelop above ULiUA:
- add node `polememelop` with `parent: null`
- change `uliua.parent` to `polememelop`

No hub repos change.

---

## Repo 2: `@polememelop/theme` (npm package)

### Tree
```
theme/
  package.json
  index.js
  src/
    assets/
      style.css
    _includes/
      layouts/
        base.njk
        post.njk
        tag.njk
      partials/
        head.njk
        nav.njk
        footer.njk
        breadcrumbs.njk
  README.md
```

### `package.json`
```json
{
  "name": "@polememelop/theme",
  "version": "0.1.0",
  "private": false,
  "type": "module",
  "main": "./index.js",
  "files": ["index.js", "src"],
  "dependencies": {
    "@polememelop/constellation": "^0.1.0"
  }
}
```

### `index.js` (Eleventy plugin)
```js
import constellation from "@polememelop/constellation/constellation.json" assert { type: "json" };

function buildIndex(nodes) {
  const byKey = nodes;
  const children = {};
  for (const [k] of Object.entries(byKey)) children[k] = [];

  for (const [k, n] of Object.entries(byKey)) {
    if (n.parent) {
      if (!children[n.parent]) children[n.parent] = [];
      children[n.parent].push(k);
    }
  }

  // sort children by order then title
  for (const k of Object.keys(children)) {
    children[k].sort((a, b) => {
      const A = byKey[a], B = byKey[b];
      const ao = (A?.order ?? 9999), bo = (B?.order ?? 9999);
      if (ao !== bo) return ao - bo;
      return (A?.title ?? a).localeCompare(B?.title ?? b);
    });
  }

  // global root: node(s) with parent null; choose lowest order
  const roots = Object.entries(byKey)
    .filter(([, n]) => n.parent === null)
    .sort(([, A], [, B]) => (A.order ?? 9999) - (B.order ?? 9999));
  const rootKey = roots[0]?.[0] ?? null;

  return { byKey, children, rootKey };
}

function breadcrumbTrail(index, currentKey) {
  const trail = [];
  let k = currentKey;
  const seen = new Set();
  while (k && index.byKey[k] && !seen.has(k)) {
    seen.add(k);
    trail.push({ key: k, ...index.byKey[k] });
    k = index.byKey[k].parent;
  }
  return trail.reverse();
}

export default function polememelopTheme(eleventyConfig, opts = {}) {
  const nodes = constellation.nodes ?? {};
  const index = buildIndex(nodes);

  // Expose constellation data to templates
  eleventyConfig.addGlobalData("constellation", () => ({
    index,
    nodes: index.byKey,
    rootKey: index.rootKey,
    breadcrumbTrail
  }));

  // Pass-through CSS
  eleventyConfig.addPassthroughCopy({
    [new URL("./src/assets/style.css", import.meta.url).pathname]: "assets/style.css"
  });

  // Collections
  eleventyConfig.addCollection("posts", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("content/posts/**/*.md")
      .sort((a, b) => (b.date ?? 0) - (a.date ?? 0));
  });

  // Simple shortcode: current year
  eleventyConfig.addShortcode("year", () => `${new Date().getFullYear()}`);

  // Defaults
  eleventyConfig.addGlobalData("theme", () => ({
    stylesheet: "/assets/style.css"
  }));

  return {
    dir: {
      // Theme does not impose dirs; hubs set their own
    }
  };
}
```

### Theme templates

#### `src/_includes/layouts/base.njk`
```njk
<!doctype html>
<html lang="en">
  {% include "partials/head.njk" %}
  <body>
    {% include "partials/nav.njk" %}
    <main class="container">
      {% include "partials/breadcrumbs.njk" %}
      {{ content | safe }}
    </main>
    {% include "partials/footer.njk" %}
  </body>
</html>
```

#### `src/_includes/layouts/post.njk`
```njk
---
layout: layouts/base.njk
---
<article class="post">
  <h1>{{ title }}</h1>
  <p class="meta">{{ page.date | date: "%Y-%m-%d" }}</p>
  {{ content | safe }}

  {% if tags %}
    <p class="tags">
      Tags:
      {% for t in tags %}
        {% if t != "posts" %}
          <a href="/tags/{{ t | slug }}/">{{ t }}</a>{% if not loop.last %}, {% endif %}
        {% endif %}
      {% endfor %}
    </p>
  {% endif %}
</article>
```

#### `src/_includes/layouts/tag.njk`
```njk
---
layout: layouts/base.njk
---
<h1>Tag: {{ tag }}</h1>
<ul>
  {% for post in posts %}
    <li>
      <a href="{{ post.url }}">{{ post.data.title }}</a>
      <small class="meta">{{ post.date | date: "%Y-%m-%d" }}</small>
    </li>
  {% endfor %}
</ul>
```

#### `src/_includes/partials/head.njk`
```njk
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{% if title %}{{ title }} · {% endif %}{{ site.siteName }}</title>
  <meta name="description" content="{{ site.description }}" />
  <link rel="stylesheet" href="{{ theme.stylesheet }}" />
  <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed.xml" />
</head>
```

#### `src/_includes/partials/nav.njk`
```njk
{% set ck = site.constellationKey %}
{% set idx = constellation.index %}
{% set root = constellation.rootKey %}

<header class="site-header">
  <div class="container header-row">
    <a class="brand" href="{{ site.siteUrl }}">{{ site.siteName }}</a>

    <nav class="topnav" aria-label="Constellation">
      {% set topChildren = idx.children[root] %}
      {% if topChildren and topChildren.length %}
        <ul class="nav-list">
          {% for key in topChildren %}
            {% set node = idx.byKey[key] %}
            {% set kids = idx.children[key] %}
            <li class="nav-item">
              <a class="nav-link {% if key == ck %}active{% endif %}" href="{{ node.url }}">{{ node.title }}</a>

              {% if kids and kids.length %}
                <ul class="nav-sub">
                  {% for k2 in kids %}
                    {% set n2 = idx.byKey[k2] %}
                    <li><a class="nav-sublink {% if k2 == ck %}active{% endif %}" href="{{ n2.url }}">{{ n2.title }}</a></li>
                  {% endfor %}
                </ul>
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      {% endif %}
    </nav>
  </div>
</header>
```

#### `src/_includes/partials/breadcrumbs.njk`
```njk
{% set trail = constellation.breadcrumbTrail(constellation.index, site.constellationKey) %}
{% if trail and trail.length > 1 %}
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <ol>
      {% for n in trail %}
        <li>
          {% if loop.last %}
            <span aria-current="page">{{ n.title }}</span>
          {% else %}
            <a href="{{ n.url }}">{{ n.title }}</a>
          {% endif %}
        </li>
      {% endfor %}
    </ol>
  </nav>
{% endif %}
```

#### `src/_includes/partials/footer.njk`
```njk
<footer class="site-footer">
  <div class="container">
    <small>© {% year %} {{ site.siteName }}</small>
  </div>
</footer>
```

#### `src/assets/style.css` (minimal, readable)
```css
:root { --max: 980px; }

body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; line-height: 1.5; }
.container { max-width: var(--max); margin: 0 auto; padding: 20px; }

.site-header { border-bottom: 1px solid #eee; position: sticky; top: 0; background: white; }
.header-row { display: flex; gap: 16px; align-items: center; justify-content: space-between; }
.brand { font-weight: 700; text-decoration: none; color: inherit; }

.nav-list { list-style: none; margin: 0; padding: 0; display: flex; gap: 14px; }
.nav-item { position: relative; }
.nav-link { text-decoration: none; color: inherit; padding: 8px 10px; border-radius: 10px; display: inline-block; }
.nav-link.active { outline: 1px solid #ddd; }

.nav-sub { display: none; position: absolute; left: 0; top: 100%; background: white; border: 1px solid #eee; border-radius: 12px; padding: 8px; list-style: none; margin: 8px 0 0 0; min-width: 240px; }
.nav-item:hover .nav-sub { display: block; }
.nav-sublink { display: block; padding: 8px 10px; text-decoration: none; color: inherit; border-radius: 10px; }
.nav-sublink.active { outline: 1px solid #ddd; }

.breadcrumbs ol { list-style: none; padding: 0; margin: 12px 0 18px 0; display: flex; flex-wrap: wrap; gap: 8px; }
.breadcrumbs li::after { content: "›"; margin-left: 8px; opacity: 0.5; }
.breadcrumbs li:last-child::after { content: ""; }

.post .meta { opacity: 0.7; }
.tags a { text-decoration: none; }

.site-footer { border-top: 1px solid #eee; margin-top: 40px; }
```

---

## Repo 3: `hub-template` (starter for each hub)

### Tree
```
hub-template/
  package.json
  .eleventy.js
  site.json
  content/
    index.md
    about.md
    posts/
      2026-02-19-welcome.md
    tags.njk
    feed.njk
  README.md
```

### `package.json`
```json
{
  "name": "hub-template",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "npx @11ty/eleventy --serve",
    "build": "npx @11ty/eleventy"
  },
  "dependencies": {
    "@11ty/eleventy": "^2.0.1",
    "@11ty/eleventy-plugin-rss": "^1.2.0",
    "@polememelop/theme": "^0.1.0"
  }
}
```

### `.eleventy.js`
```js
import pluginRss from "@11ty/eleventy-plugin-rss";
import polememelopTheme from "@polememelop/theme";
import fs from "node:fs";

export default function (eleventyConfig) {
  eleventyConfig.addPlugin(pluginRss);
  eleventyConfig.addPlugin(polememelopTheme);

  // Load per-hub config from site.json
  const site = JSON.parse(fs.readFileSync("./site.json", "utf8"));
  eleventyConfig.addGlobalData("site", () => site);

  // Layout aliases so content can just say `layout: base`
  eleventyConfig.addLayoutAlias("base", "layouts/base.njk");
  eleventyConfig.addLayoutAlias("post", "layouts/post.njk");
  eleventyConfig.addLayoutAlias("tag", "layouts/tag.njk");

  // Tags collection helpers
  eleventyConfig.addCollection("tagList", (collectionApi) => {
    const tags = new Set();
    for (const item of collectionApi.getAll()) {
      (item.data.tags || []).forEach((t) => {
        if (t && t !== "posts") tags.add(t);
      });
    }
    return [...tags].sort();
  });

  return {
    dir: {
      input: "content",
      includes: "../node_modules/@polememelop/theme/src/_includes",
      output: "_site"
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
}
```

### `site.json` (edit per hub)
```json
{
  "constellationKey": "howacceptanceworks",
  "siteName": "How Acceptance Works",
  "siteUrl": "https://howacceptanceworks.com",
  "description": "Essays and tools for acceptance → unconditional love."
}
```

### `content/index.md`
```md
---
layout: base
title: Home
---

# {{ site.siteName }}

{{ site.description }}

## Latest

<ul>
{% for post in collections.posts | slice(0, 10) %}
  <li><a href="{{ post.url }}">{{ post.data.title }}</a> <small class="meta">{{ post.date | date: "%Y-%m-%d" }}</small></li>
{% endfor %}
</ul>
```

### `content/about.md`
```md
---
layout: base
title: About
---

Write the About page.
```

### `content/posts/2026-02-19-welcome.md`
```md
---
layout: post
title: Welcome
date: 2026-02-19
tags: [welcome]
---

This is the first post.
```

### `content/tags.njk` (tag index)
```njk
---
layout: base
title: Tags
permalink: /tags/
---

<h1>Tags</h1>
<ul>
  {% for tag in collections.tagList %}
    <li><a href="/tags/{{ tag | slug }}/">{{ tag }}</a></li>
  {% endfor %}
</ul>
```

### `content/feed.njk` (RSS)
```njk
---
permalink: /feed.xml
eleventyExcludeFromCollections: true
---
{{ collections.posts | rssFeed({
  title: site.siteName,
  language: "en",
  url: site.siteUrl,
  subtitle: site.description,
  feed_url: site.siteUrl + "/feed.xml",
  author: "Polememelop"
}) }}
```

### Tag pages (generated)
Add this file: `content/tags/tag-pages.11ty.js`

Tree add:
```
content/
  tags/
    tag-pages.11ty.js
```

`content/tags/tag-pages.11ty.js`:
```js
export default class TagPages {
  data() {
    return {
      pagination: {
        data: "collections.tagList",
        size: 1,
        alias: "tag"
      },
      layout: "tag",
      permalink: (data) => `/tags/${data.tag}/index.html`,
      eleventyComputed: {
        title: (data) => `Tag: ${data.tag}`
      }
    };
  }

  render(data) {
    const posts = data.collections.posts.filter((p) => (p.data.tags || []).includes(data.tag));
    // expose for tag layout
    data.posts = posts;
    return "";
  }
}
```

(Notes: v1 keeps this simple; we can refine rendering to pass `posts` more elegantly if desired.)

---

## Local run (any hub)

From a hub repo:
```bash
npm ci
npm run dev
```
Build:
```bash
npm run build
```
Output is `_site/`.

---

## Cloudflare Pages setup (manual v1)

For each hub repo:
1. Create a Cloudflare Pages project connected to the GitHub repo
2. Build command: `npm run build`
3. Output directory: `_site`
4. Add the custom domain for the hub

---

## Automation v1.1: `newhub` script (GitHub + scaffold)

This makes hub creation repeatable and eliminates “clip files from browser.”

### `newhub.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./newhub.sh howacceptanceworks howacceptanceworks.com "How Acceptance Works" howacceptanceworks
#
# Requires:
#   - gh authenticated
#   - a hub template repo available (see TEMPLATE)

REPO_NAME="${1:?repo required}"
DOMAIN="${2:?domain required}"
TITLE="${3:?title required}"
KEY="${4:-$REPO_NAME}"

TEMPLATE="YOUR_GH_ORG/hub-template"  # <-- change

# 1) Create repo from template and clone

gh repo create "$REPO_NAME" --template "$TEMPLATE" --public --clone
cd "$REPO_NAME"

# 2) Write site.json
cat > site.json <<EOF
{
  "constellationKey": "${KEY}",
  "siteName": "${TITLE}",
  "siteUrl": "https://${DOMAIN}",
  "description": "${TITLE} (Polememelop constellation)."
}
EOF

# 3) Commit + push

git add site.json
git commit -m "Configure hub identity"
git push -u origin main

echo "Created hub repo: $REPO_NAME"
echo "Next (v1): create Cloudflare Pages project + attach domain in UI."
```

### Automation v1.2 (future): Cloudflare Pages + DNS via API

We’ll extend `newhub` to:
- create Pages project
- connect to GitHub
- attach custom domain
- create DNS record

This is intentionally deferred until you’re happy with v1’s content + theme contract.

---

## Practical workflow for constellation restructuring

When you want to introduce Polememelop above ULiUA:
1. Edit `@polememelop/constellation/constellation.json` (add node + re-parent)
2. Publish `@polememelop/constellation` version bump
3. Update hub dependencies (batch with one script later)
4. Push — Cloudflare rebuilds each hub and nav updates everywhere

---

## Sanity checklist (v1)

- [ ] Theme renders nav + breadcrumbs for current hub key
- [ ] A hub builds locally and produces `_site`
- [ ] Cloudflare Pages deploys `_site`
- [ ] Custom domain resolves
- [ ] Adding a new node to constellation updates nav everywhere after dependency bump

---

## Optional simplifications (if you want fewer moving parts in v1)

If npm package publishing feels like overhead at the start:
- **Bundle `constellation.json` inside the theme repo** (skip `@polememelop/constellation` initially)
- Or, keep `constellation.json` **in each hub** (worst for restructuring, but simplest)

Recommended compromise:
- Keep separate `@polememelop/constellation` from day one (lightweight, pays off immediately).

