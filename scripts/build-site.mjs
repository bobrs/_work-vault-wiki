#!/usr/bin/env node
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(ROOT, "dist");
const REPO_URL = "https://github.com/bobrs/_work-vault-wiki/blob/main";
const SOURCE_MARKDOWN = [];
const OUTPUT_FOR_SOURCE = new Map();
const WORKER_PAGES = new Map();

const NAV_ITEMS = [
  ["Home", "/index.html"],
  ["Wiki", "/wiki/index.html"],
  ["Attractors", "/wiki/attractors/index.html"],
  ["Vault", "/vault/index.html"],
  ["Projects", "/wiki/projects/index.html"],
  ["Concepts", "/wiki/concepts/index.html"],
  ["Essays", "/wiki/external/shimmerymemory/essays/index.html"],
  ["Source Roles", "/wiki/source-roles/index.html"],
  ["Artifact Types", "/wiki/artifact-types/index.html"],
  ["Incoming", "/wiki/incoming-review.html"],
  ["Duplicates", "/wiki/duplicate-review.html"],
  ["Missing", "/wiki/missing-files.html"],
  ["README", "/readme.html"],
  ["WIKI.md", "/wiki-guide.html"],
];

function encodePathSegments(relPath) {
  return relPath
    .split(path.posix.sep)
    .map((part) => encodeURIComponent(part))
    .join("/");
}

function githubUrl(relPath) {
  return `${REPO_URL}/${encodePathSegments(relPath)}`;
}

function isMarkdownSource(relPath) {
  return relPath.endsWith(".md");
}

async function walkMarkdown(dirRel) {
  const absDir = path.join(ROOT, dirRel);
  const entries = await fs.readdir(absDir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name === "dist" || entry.name === ".git" || entry.name === "node_modules") {
      continue;
    }
    const rel = path.posix.join(dirRel, entry.name);
    if (entry.isDirectory()) {
      await walkMarkdown(rel);
    } else if (entry.isFile() && isMarkdownSource(rel)) {
      SOURCE_MARKDOWN.push(rel);
    }
  }
}

function outputForSource(relPath) {
  if (OUTPUT_FOR_SOURCE.has(relPath)) return OUTPUT_FOR_SOURCE.get(relPath);
  const dir = path.posix.dirname(relPath);
  const base = path.posix.basename(relPath, ".md");
  let out;
  if (relPath === "README.md") {
    out = "readme.html";
  } else if (relPath === "WIKI.md") {
    out = "wiki-guide.html";
  } else if (base === "index") {
    out = path.posix.join(dir, "index.html");
  } else {
    out = path.posix.join(dir, `${base}.html`);
  }
  OUTPUT_FOR_SOURCE.set(relPath, out);
  return out;
}

function routeForOutput(outRel) {
  return `/${outRel.split(path.sep).join("/")}`;
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function relativeHref(fromOut, toOut) {
  const fromDir = path.posix.dirname(fromOut);
  const rel = path.posix.relative(fromDir === "." ? "" : fromDir, toOut);
  return rel || path.posix.basename(toOut);
}

function resolveRepoPath(sourceRel, target) {
  const sourceDir = path.posix.dirname(sourceRel);
  return path.posix.normalize(path.posix.join(sourceDir, target));
}

function rewriteLink(sourceRel, href) {
  if (/^(https?:|mailto:|#)/i.test(href)) return href;
  if (href.startsWith("/")) return href;
  let cleaned = href.split("#")[0].trim();
  cleaned = cleaned.replaceAll("&lt;", "<").replaceAll("&gt;", ">");
  if (cleaned.startsWith("<") && cleaned.endsWith(">")) {
    cleaned = cleaned.slice(1, -1);
  }
  const absRepoPath = resolveRepoPath(sourceRel, cleaned);
  const markdownTarget = OUTPUT_FOR_SOURCE.get(absRepoPath);
  if (markdownTarget) {
    return relativeHref(outputForSource(sourceRel), markdownTarget);
  }
  return githubUrl(absRepoPath);
}

function renderInline(sourceRel, text) {
  const fragments = [];
  const token = (html) => {
    fragments.push(html);
    return `\u0001${fragments.length - 1}\u0001`;
  };

  let working = text.replace(/`([^`]+)`/g, (_, code) => token(`<code>${escapeHtml(code)}</code>`));
  working = working.replace(/\[([^\]]+)\]\(<([^>]+)>\)/g, (_, label, href) => {
    const rewritten = rewriteLink(sourceRel, href.trim());
    return token(`<a href="${escapeHtml(rewritten)}">${escapeHtml(label)}</a>`);
  });
  working = working.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const rewritten = rewriteLink(sourceRel, href.trim());
    return token(`<a href="${escapeHtml(rewritten)}">${escapeHtml(label)}</a>`);
  });

  working = escapeHtml(working);
  working = working.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  working = working.replace(/\*([^*]+)\*/g, "<em>$1</em>");

  return working.replace(/\u0001(\d+)\u0001/g, (_, idx) => fragments[Number(idx)]);
}

function flushParagraph(sourceRel, lines, out) {
  if (!lines.length) return;
  out.push(`<p>${renderInline(sourceRel, lines.join(" "))}</p>`);
  lines.length = 0;
}

function flushList(sourceRel, listType, items, out) {
  if (!listType || !items.length) return;
  const tag = listType === "ol" ? "ol" : "ul";
  out.push(`<${tag}>`);
  for (const item of items) {
    out.push(`<li>${renderInline(sourceRel, item)}</li>`);
  }
  out.push(`</${tag}>`);
  items.length = 0;
}

function flushQuote(sourceRel, quoteLines, out) {
  if (!quoteLines.length) return;
  const joined = quoteLines.join(" ");
  out.push(`<blockquote><p>${renderInline(sourceRel, joined)}</p></blockquote>`);
  quoteLines.length = 0;
}

function renderMarkdown(sourceRel, markdown) {
  const lines = markdown.replaceAll("\r\n", "\n").split("\n");
  const out = [];
  const para = [];
  const quote = [];
  const listItems = [];
  let listType = null;
  let inCode = false;
  let codeLines = [];
  let codeFence = "```";

  function flushAll() {
    flushParagraph(sourceRel, para, out);
    flushQuote(sourceRel, quote, out);
    flushList(sourceRel, listType, listItems, out);
    listType = null;
  }

  for (const rawLine of lines) {
    const line = rawLine.replace(/\t/g, "  ");
    if (inCode) {
      if (line.trim().startsWith(codeFence)) {
        out.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
        codeLines = [];
        inCode = false;
      } else {
        codeLines.push(line);
      }
      continue;
    }

    if (line.trim().startsWith("```")) {
      flushAll();
      inCode = true;
      codeFence = "```";
      continue;
    }

    if (!line.trim()) {
      flushAll();
      continue;
    }

    const heading = line.match(/^(#{1,6})\s+(.*)$/);
    if (heading) {
      flushAll();
      const level = heading[1].length;
      out.push(`<h${level}>${renderInline(sourceRel, heading[2].trim())}</h${level}>`);
      continue;
    }

    const quoteMatch = line.match(/^>\s?(.*)$/);
    if (quoteMatch) {
      flushParagraph(sourceRel, para, out);
      flushList(sourceRel, listType, listItems, out);
      listType = null;
      quote.push(quoteMatch[1]);
      continue;
    }

    const unordered = line.match(/^\s*[-*]\s+(.*)$/);
    if (unordered) {
      flushParagraph(sourceRel, para, out);
      flushQuote(sourceRel, quote, out);
      if (listType && listType !== "ul") {
        flushList(sourceRel, listType, listItems, out);
      }
      listType = "ul";
      listItems.push(unordered[1]);
      continue;
    }

    const ordered = line.match(/^\s*\d+\.\s+(.*)$/);
    if (ordered) {
      flushParagraph(sourceRel, para, out);
      flushQuote(sourceRel, quote, out);
      if (listType && listType !== "ol") {
        flushList(sourceRel, listType, listItems, out);
      }
      listType = "ol";
      listItems.push(ordered[1]);
      continue;
    }

    flushQuote(sourceRel, quote, out);
    flushList(sourceRel, listType, listItems, out);
    listType = null;
    para.push(line.trim());
  }

  if (inCode) {
    out.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
  }
  flushAll();
  return out.join("\n");
}

function pageShell({ title, subtitle, body, navActive = "" }) {
  const nav = NAV_ITEMS.map(([label, href]) => {
    const active = href === navActive ? " active" : "";
    return `<a class="nav-link${active}" href="${href}">${label}</a>`;
  }).join("");

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${escapeHtml(subtitle || title)}">
  <title>${escapeHtml(title)}</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f4efe8;
      --panel: rgba(252, 249, 244, 0.9);
      --panel-strong: #f8f3ea;
      --text: #1d232d;
      --muted: #5a6574;
      --line: rgba(29, 35, 45, 0.14);
      --accent: #184e77;
      --accent-2: #d97706;
      --shadow: 0 18px 60px rgba(29, 35, 45, 0.14);
    }
    * { box-sizing: border-box; }
    html, body { margin: 0; min-height: 100%; }
    body {
      font-family: Georgia, "Times New Roman", serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(24, 78, 119, 0.12), transparent 32%),
        radial-gradient(circle at top right, rgba(217, 119, 6, 0.12), transparent 26%),
        linear-gradient(180deg, #f8f5f0 0%, #eef2f4 100%);
    }
    a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }
    .shell {
      display: grid;
      grid-template-columns: 290px minmax(0, 1fr);
      min-height: 100vh;
    }
    .sidebar {
      position: sticky;
      top: 0;
      height: 100vh;
      padding: 28px 20px;
      background: linear-gradient(180deg, rgba(18, 27, 38, 0.98), rgba(28, 40, 56, 0.96));
      color: #f5efe4;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
      overflow: auto;
    }
    .brand {
      font-size: 1.35rem;
      line-height: 1.1;
      margin: 0 0 10px;
      letter-spacing: 0.02em;
    }
    .sidebar p, .sidebar small { color: rgba(245, 239, 228, 0.78); }
    .nav {
      display: grid;
      gap: 10px;
      margin: 24px 0;
    }
    .nav-link {
      display: block;
      padding: 10px 12px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.06);
      color: #f7f1e7;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .nav-link.active {
      background: linear-gradient(90deg, rgba(24, 78, 119, 0.9), rgba(217, 119, 6, 0.65));
      border-color: transparent;
    }
    .sidebar-card {
      margin-top: 18px;
      padding: 14px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .content {
      padding: 34px;
    }
    .page {
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 24px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(10px);
    }
    .eyebrow {
      font-size: 0.8rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--accent-2);
      margin: 0 0 12px;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: Georgia, "Times New Roman", serif;
      line-height: 1.15;
      margin: 1.3em 0 0.45em;
    }
    h1 { font-size: clamp(2.1rem, 4vw, 3.2rem); margin-top: 0; }
    h2 { font-size: 1.55rem; border-bottom: 1px solid var(--line); padding-bottom: 0.25em; }
    h3 { font-size: 1.2rem; }
    p, li { font-size: 1.03rem; line-height: 1.75; }
    ul, ol { padding-left: 1.4rem; }
    blockquote {
      margin: 1.2rem 0;
      padding: 0.9rem 1rem;
      border-left: 4px solid var(--accent);
      background: rgba(24, 78, 119, 0.06);
      border-radius: 0 12px 12px 0;
    }
    pre {
      overflow: auto;
      padding: 16px;
      border-radius: 16px;
      background: #0f1720;
      color: #f5f8ff;
      font-size: 0.92rem;
      line-height: 1.6;
    }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.94em;
      background: rgba(15, 23, 32, 0.08);
      padding: 0.15rem 0.32rem;
      border-radius: 6px;
    }
    pre code { background: transparent; padding: 0; }
    .hero-grid {
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 18px;
      margin: 22px 0 10px;
    }
    .card {
      grid-column: span 6;
      padding: 18px;
      border-radius: 18px;
      background: var(--panel-strong);
      border: 1px solid var(--line);
    }
    .card.wide { grid-column: span 12; }
    .stat {
      font-size: 2.05rem;
      margin: 0 0 8px;
    }
    .gateway-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 18px 0 24px;
    }
    .gateway-action {
      display: inline-flex;
      align-items: center;
      min-height: 40px;
      padding: 8px 12px;
      border-radius: 10px;
      background: rgba(24, 78, 119, 0.1);
      border: 1px solid rgba(24, 78, 119, 0.18);
      text-decoration: none;
      font-weight: 600;
    }
    .attractor-grid, .browse-grid, .status-grid {
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 14px;
      margin: 18px 0 12px;
    }
    .attractor-card {
      grid-column: span 4;
      display: block;
      min-height: 100%;
      padding: 16px;
      border-radius: 10px;
      background: rgba(248, 243, 234, 0.92);
      border: 1px solid var(--line);
      text-decoration: none;
      color: var(--text);
    }
    .attractor-card:hover {
      border-color: rgba(24, 78, 119, 0.38);
      box-shadow: 0 10px 28px rgba(29, 35, 45, 0.1);
    }
    .attractor-card h3 {
      margin-top: 0;
      color: var(--accent);
    }
    .subpaths {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 12px;
    }
    .subpaths span {
      display: inline-flex;
      padding: 3px 8px;
      border-radius: 999px;
      background: rgba(24, 78, 119, 0.08);
      color: var(--muted);
      font-size: 0.82rem;
      line-height: 1.35;
    }
    .browse-card, .status-card {
      grid-column: span 3;
      padding: 14px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.42);
      border: 1px solid var(--line);
    }
    .browse-card a {
      font-weight: 700;
      text-decoration: none;
    }
    .browse-card p, .status-card p {
      margin: 8px 0 0;
      line-height: 1.55;
    }
    .muted { color: var(--muted); }
    .file-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
    }
    .file-table th, .file-table td {
      text-align: left;
      padding: 10px 8px;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
    }
    .tag {
      display: inline-block;
      font-size: 0.76rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.22rem 0.55rem;
      border-radius: 999px;
      background: rgba(24, 78, 119, 0.11);
      color: var(--accent);
    }
    .footer {
      margin-top: 26px;
      color: var(--muted);
      font-size: 0.92rem;
    }
    .title-row {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 4px;
    }
    @media (max-width: 980px) {
      .shell { grid-template-columns: 1fr; }
      .sidebar {
        position: relative;
        height: auto;
        padding: 14px 16px;
        border-right: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      }
      .brand {
        font-size: 1.15rem;
        margin-bottom: 4px;
      }
      .sidebar p {
        margin: 0;
        font-size: 0.92rem;
        line-height: 1.35;
      }
      .nav {
        display: flex;
        gap: 8px;
        margin: 12px -4px 0;
        overflow-x: auto;
        padding: 0 4px 4px;
      }
      .nav-link {
        flex: 0 0 auto;
        padding: 8px 10px;
        border-radius: 10px;
        font-size: 0.9rem;
        white-space: nowrap;
      }
      .sidebar-card { display: none; }
      .content { padding: 16px; }
      .page { padding: 20px; }
      .card { grid-column: span 12; }
      .attractor-card, .browse-card, .status-card { grid-column: span 12; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside class="sidebar">
      <h1 class="brand">Work Vault Wiki</h1>
      <p>Public static interface for the vault, wiki, and raw repository source.</p>
      <nav class="nav">${nav}</nav>
      <div class="sidebar-card">
        <small>Source repo</small>
        <p style="margin: 8px 0 0;"><a href="https://github.com/bobrs/_work-vault-wiki" style="color:#f7f1e7;">bobrs/_work-vault-wiki</a></p>
      </div>
    </aside>
    <main class="content">
      <section class="page">
        ${body}
      </section>
    </main>
  </div>
</body>
</html>`;
}

function rootLanding({ stats, pageCount, duplicateGroups, rawCount }) {
  const attractors = [
    {
      title: "Witness",
      href: "/wiki/attractors/witness/index.html",
      body: "How fields become artifacts: observation, collapse, testimony, accountability, and the discipline of not merging too soon.",
      paths: ["observation", "artifact collapse", "testimony", "accountability", "non-merge"],
    },
    {
      title: "Consent",
      href: "/wiki/attractors/consent/index.html",
      body: "The boundary logic of living systems: authorization, refusal, participation, reversibility, and semantic fit.",
      paths: ["boundary", "sovereignty", "authorization", "refusal", "reversibility"],
    },
    {
      title: "Attention",
      href: "/wiki/attractors/attention/index.html",
      body: "The selection layer of reality: salience, compression, curiosity, care, distortion, and what gets to become real.",
      paths: ["compression", "salience", "curiosity", "distortion", "care"],
    },
    {
      title: "Intuition",
      href: "/wiki/attractors/intuition/index.html",
      body: "Pattern recognition before explanation: body knowledge, latent processing, felt sense, and pre-verbal signal.",
      paths: ["felt sense", "latent processing", "body knowledge", "pattern recognition"],
    },
    {
      title: "Provenance",
      href: "/wiki/attractors/provenance/index.html",
      body: "The lineage of meaning: origin, context, transformation, authorship, admissibility, and consentful recordkeeping.",
      paths: ["lineage", "attribution", "transformation", "admissibility", "consentful record"],
    },
    {
      title: "Governance",
      href: "/wiki/attractors/governance/index.html",
      body: "How power becomes structure: legitimacy, constraint, accountability, institutions, drift, and collective coordination.",
      paths: ["legitimacy", "constraint", "accountability", "institutions", "drift"],
    },
    {
      title: "Grounding",
      href: "/wiki/attractors/grounding/index.html",
      body: "Where abstraction touches earth: body, place, safety, materials, limits, nervous systems, and lived constraint.",
      paths: ["embodiment", "place", "safety", "material limits", "nervous system"],
    },
    {
      title: "Loop Mechanics",
      href: "/wiki/attractors/loop-mechanics/index.html",
      body: "How systems return: recursion, feedback, stabilization, drift, rupture, repair, traps, and regenerative flow.",
      paths: ["feedback", "recursion", "drift", "rupture", "repair"],
    },
    {
      title: "Agency",
      href: "/wiki/attractors/agency/index.html",
      body: "The capacity to act: escape, choice, authorship, constraint, survival loops, and the cost of free will.",
      paths: ["escape", "choice", "capacity", "authorship", "survival loops"],
    },
    {
      title: "Meaning",
      href: "/wiki/attractors/meaning/index.html",
      body: "How symbols become consequential: language, story, artifact, metaphor, interpretation, and shared reality.",
      paths: ["language", "story", "metaphor", "interpretation", "shared reality"],
    },
    {
      title: "Memory",
      href: "/wiki/attractors/memory/index.html",
      body: "Continuity across time: archive, forgetting, recurrence, personal history, machine memory, and cultural inheritance.",
      paths: ["archive", "forgetting", "recurrence", "machine memory", "inheritance"],
    },
    {
      title: "Trust",
      href: "/wiki/attractors/trust/index.html",
      body: "Confidence under vulnerability: verification, relationship, proof, coherence, witness, and repair.",
      paths: ["verification", "relationship", "proof", "coherence", "repair"],
    },
  ];
  const attractorCards = attractors
    .map((card) => `
      <a class="attractor-card" href="${card.href}">
        <h3>${card.title}</h3>
        <p>${card.body}</p>
        <div class="subpaths">${card.paths.map((pathLabel) => `<span>${pathLabel}</span>`).join("")}</div>
      </a>
    `)
    .join("");
  return pageShell({
    title: "Work Vault Wiki",
    subtitle: "A living map of artifacts, attractors, and published work",
    body: `
      <p class="eyebrow">Attractor Gateway</p>
      <div class="title-row">
        <h1>Work Vault Wiki</h1>
        <span class="tag">public map</span>
      </div>
      <p>A living map of artifacts, attractors, and published work across witness, consent, attention, provenance, governance, grounding, loop mechanics, agency, meaning, memory, and trust.</p>
      <div class="gateway-actions">
        <a class="gateway-action" href="/wiki/index.html">Structured Wiki Index</a>
        <a class="gateway-action" href="/wiki/projects/index.html">Projects</a>
        <a class="gateway-action" href="/wiki/concepts/index.html">Concepts</a>
        <a class="gateway-action" href="/wiki/external/shimmerymemory/essays/index.html">Published Essays</a>
        <a class="gateway-action" href="/vault/index.html">Raw Vault</a>
        <a class="gateway-action" href="https://github.com/bobrs/_work-vault-wiki">GitHub Source</a>
      </div>

      <h2>Enter by Attractor</h2>
      <div class="attractor-grid">
        ${attractorCards}
      </div>

      <h2>Browse the Wiki</h2>
      <div class="browse-grid">
        <div class="browse-card"><a href="/wiki/projects/index.html">Projects</a><p class="muted">Project families, branches, and source-backed pages.</p></div>
        <div class="browse-card"><a href="/wiki/concepts/index.html">Concepts</a><p class="muted">Recurring concepts that have stabilized across the corpus.</p></div>
        <div class="browse-card"><a href="/wiki/external/shimmerymemory/essays/index.html">Published Essays</a><p class="muted">Public Shimmery Memory essay metadata and source links.</p></div>
        <div class="browse-card"><a href="/wiki/artifacts/index.html">Artifact Index</a><p class="muted">Wiki-side artifact navigation and source references.</p></div>
        <div class="browse-card"><a href="/wiki/source-roles/index.html">Source Roles</a><p class="muted">Inbound originals and standard-named source copies.</p></div>
        <div class="browse-card"><a href="/wiki/artifact-types/index.html">Artifact Types</a><p class="muted">Source-layer browsing by file type and companion asset kind.</p></div>
        <div class="browse-card"><a href="/vault/index.html">Raw Vault</a><p class="muted">Browsable repository inventory with GitHub source links.</p></div>
        <div class="browse-card"><a href="/wiki/timelines/index.html">Timelines</a><p class="muted">Chronological views and time-based orientation.</p></div>
        <div class="browse-card"><a href="/wiki/unresolved/index.html">Unresolved</a><p class="muted">Open classification, naming, and interpretation questions.</p></div>
        <div class="browse-card"><a href="/wiki/duplicate-review.html">Duplicate Review</a><p class="muted">Duplicate sets and collapse decisions.</p></div>
        <div class="browse-card"><a href="/wiki/missing-files.html">Missing Files</a><p class="muted">Broken, absent, or not-yet-routed source references.</p></div>
        <div class="browse-card"><a href="/wiki/incoming-review.html">Incoming Review</a><p class="muted">Current intake triage and routing state.</p></div>
        <div class="browse-card"><a href="/readme.html">README</a><p class="muted">Repository overview rendered from source.</p></div>
        <div class="browse-card"><a href="/wiki-guide.html">WIKI.md</a><p class="muted">Project wiki guide and source navigation.</p></div>
      </div>

      <h2>Vault Status</h2>
      <div class="status-grid">
        <div class="status-card">
          <p class="stat">${stats.total}</p>
          <p class="muted">Files in the current repository inventory.</p>
        </div>
        <div class="status-card">
          <p class="stat">${rawCount}</p>
          <p class="muted">Raw vault files under <code>artifacts/</code>.</p>
        </div>
        <div class="status-card">
          <p class="stat">${pageCount}</p>
          <p class="muted">Markdown pages rendered as static HTML.</p>
        </div>
        <div class="status-card">
          <p class="stat">${duplicateGroups}</p>
          <p class="muted">Exact duplicate hash groups in the manifest.</p>
        </div>
      </div>
    `,
    navActive: "/index.html",
  });
}

function renderVaultPage(records) {
  const groups = new Map();
  for (const record of records) {
    const top = record.current_path.split("/")[0];
    if (!groups.has(top)) groups.set(top, []);
    groups.get(top).push(record);
  }
  const sections = [...groups.entries()]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([group, items]) => {
      const rows = items
        .sort((a, b) => a.current_path.localeCompare(b.current_path))
        .map((r) => `
          <tr>
            <td><a href="${githubUrl(r.current_path)}">${escapeHtml(r.current_path)}</a></td>
            <td>${escapeHtml(r.record_kind || "")}</td>
            <td>${escapeHtml(r.extension || "[none]")}</td>
            <td>${r.size_bytes}</td>
          </tr>
        `)
        .join("");
      return `
        <section>
          <h2>${escapeHtml(group)} (${items.length})</h2>
          <table class="file-table">
            <thead>
              <tr><th>Path</th><th>Kind</th><th>Ext</th><th>Bytes</th></tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        </section>
      `;
    })
    .join("");

  return pageShell({
    title: "Vault Map",
    subtitle: "Public file browser for the raw vault",
    body: `
      <p class="eyebrow">Raw source map</p>
      <div class="title-row">
        <h1>Vault Map</h1>
        <span class="tag">GitHub links</span>
      </div>
      <p class="muted">Each entry links to the public GitHub repository so the raw vault remains visible without duplicating binary assets into the site build.</p>
      ${sections}
    `,
    navActive: "/vault/index.html",
  });
}

function groupRecords(records, keyFn) {
  const groups = new Map();
  for (const record of records) {
    const key = keyFn(record);
    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key).push(record);
  }
  return groups;
}

function sortRecordsByPath(records) {
  return [...records].sort((a, b) => a.current_path.localeCompare(b.current_path));
}

function pageHrefForWikiPage(wikiPage) {
  return `/${wikiPage.replace(/\.md$/, ".html")}`;
}

function recordPrimaryHref(record) {
  if (record.wiki_page) return pageHrefForWikiPage(record.wiki_page);
  if (record.standard_named_path) return githubUrl(record.standard_named_path);
  return githubUrl(record.current_path);
}

function recordPrimaryLabel(record) {
  return record.standard_named_filename || record.original_filename || path.posix.basename(record.current_path);
}

function sourceRoleLabel(role) {
  if (role === "standard_named_source") return "Standard-Named Source";
  if (role === "inbound_original") return "Inbound Original";
  if (!role) return "Unassigned";
  return role;
}

function extensionLabel(extension) {
  if (!extension) return "[no extension]";
  return extension;
}

function renderRecordTable(records, { showRole = false, showStandardNamed = false, showInbound = false, showWiki = true } = {}) {
  const headerCells = ["Item"];
  if (showRole) headerCells.push("Source Role");
  if (showWiki) headerCells.push("Wiki Page");
  if (showInbound) headerCells.push("Inbound Path");
  if (showStandardNamed) headerCells.push("Standard-Named Path");
  const rows = records
    .map((record) => {
      const cells = [`<a href="${escapeHtml(recordPrimaryHref(record))}">${escapeHtml(recordPrimaryLabel(record))}</a>`];
      if (showRole) cells.push(escapeHtml(sourceRoleLabel(record.source_role)));
      if (showWiki) {
        cells.push(
          record.wiki_page
            ? `<a href="${escapeHtml(pageHrefForWikiPage(record.wiki_page))}">${escapeHtml(record.wiki_page)}</a>`
            : "—"
        );
      }
      if (showInbound) {
        cells.push(
          record.inbound_path
            ? `<a href="${escapeHtml(githubUrl(record.inbound_path))}">${escapeHtml(record.inbound_path)}</a>`
            : "—"
        );
      }
      if (showStandardNamed) {
        cells.push(
          record.standard_named_path
            ? `<a href="${escapeHtml(githubUrl(record.standard_named_path))}">${escapeHtml(record.standard_named_path)}</a>`
            : "—"
        );
      }
      return `<tr>${cells.map((cell) => `<td>${cell}</td>`).join("")}</tr>`;
    })
    .join("");
  return `
    <table class="file-table">
      <thead>
        <tr>${headerCells.map((cell) => `<th>${escapeHtml(cell)}</th>`).join("")}</tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

function renderSourceRolesPage(records) {
  const explicit = records.filter((record) => record.source_role === "standard_named_source" || record.source_role === "inbound_original");
  const groups = groupRecords(explicit, (record) => record.source_role);
  const standardNamed = sortRecordsByPath(groups.get("standard_named_source") || []);
  const inboundOriginal = sortRecordsByPath(groups.get("inbound_original") || []);
  const unassignedCount = records.length - explicit.length;

  return pageShell({
    title: "Source Roles",
    subtitle: "Generated index of inventory source roles",
    body: `
      <p class="eyebrow">Generated index</p>
      <div class="title-row">
        <h1>Source Roles</h1>
        <span class="tag">manifest/inventory.jsonl</span>
      </div>
      <p>This page indexes the source layer by role. It is generated from the inventory manifest and keeps inbound originals separate from standard-named source copies.</p>
      <div class="status-grid">
        <div class="status-card"><p class="stat">${standardNamed.length}</p><p class="muted">Standard-named source copies.</p></div>
        <div class="status-card"><p class="stat">${inboundOriginal.length}</p><p class="muted">Inbound originals.</p></div>
        <div class="status-card"><p class="stat">${unassignedCount}</p><p class="muted">Inventory rows without a source role.</p></div>
      </div>
      <h2>Standard-Named Source</h2>
      ${renderRecordTable(standardNamed, { showWiki: true, showInbound: true, showStandardNamed: true })}
      <h2>Inbound Original</h2>
      ${renderRecordTable(inboundOriginal, { showWiki: true, showInbound: true, showStandardNamed: false })}
      <h2>Notes</h2>
      <p class="muted">Use the full Artifact Index when you need the entire vault. This page focuses on the source layer only.</p>
    `,
    navActive: "/wiki/source-roles/index.html",
  });
}

function renderArtifactTypesPage(records) {
  const sourceLayer = records.filter((record) => record.source_role === "standard_named_source" || record.source_role === "inbound_original");
  const groups = [...groupRecords(sourceLayer, (record) => extensionLabel(record.extension)).entries()]
    .sort((a, b) => {
      if (b[1].length !== a[1].length) return b[1].length - a[1].length;
      return a[0].localeCompare(b[0]);
    });

  const typeCards = groups
    .map(([extension, items]) => `
      <div class="status-card">
        <p class="stat">${items.length}</p>
        <p class="muted">${escapeHtml(extension)} items in the source layer.</p>
      </div>
    `)
    .join("");

  const sections = groups
    .map(([extension, items]) => `
      <section>
        <h2>${escapeHtml(extensionLabel(extension))} (${items.length})</h2>
        ${renderRecordTable(sortRecordsByPath(items), { showRole: true, showWiki: true, showInbound: true, showStandardNamed: true })}
      </section>
    `)
    .join("");

  return pageShell({
    title: "Artifact Types",
    subtitle: "Generated index of source-layer artifact types",
    body: `
      <p class="eyebrow">Generated index</p>
      <div class="title-row">
        <h1>Artifact Types</h1>
        <span class="tag">source-layer view</span>
      </div>
      <p>This page groups the source layer by file type so it is easier to browse document families, media companions, and code or asset files without losing the source-layer distinction.</p>
      <div class="status-grid">${typeCards}</div>
      ${sections}
      <h2>Notes</h2>
      <p class="muted">Use the full Artifact Index when you need the complete repository inventory. This page is intentionally scoped to the source layer and its companion assets.</p>
    `,
    navActive: "/wiki/artifact-types/index.html",
  });
}

async function writeRenderedPage(outRel, html) {
  const absOut = path.join(DIST, outRel);
  await fs.mkdir(path.dirname(absOut), { recursive: true });
  await fs.writeFile(absOut, html, "utf8");

  const publicOut = path.join(DIST, "server", "public", outRel);
  await fs.mkdir(path.dirname(publicOut), { recursive: true });
  await fs.writeFile(publicOut, html, "utf8");

  const route = routeForOutput(outRel);
  WORKER_PAGES.set(route, html);
  if (route === "/index.html") {
    WORKER_PAGES.set("/", html);
  } else if (route.endsWith("/index.html")) {
    WORKER_PAGES.set(route.slice(0, -10), html);
  }
}

async function writeWorkerEntrypoints() {
  const pagesObject = Object.fromEntries(
    [...WORKER_PAGES.entries()].sort(([a], [b]) => a.localeCompare(b))
  );
  const pagesModule = `export const PAGES = ${JSON.stringify(pagesObject, null, 2)};\n`;
  const workerModule = `import { PAGES } from "./pages.js";\n\nfunction normalizePath(pathname) {\n  if (pathname === "/") return "/index.html";\n  if (pathname in PAGES) return pathname;\n  if (pathname.endsWith("/")) {\n    const indexPath = \`\${pathname}index.html\`;\n    if (indexPath in PAGES) return indexPath;\n  }\n  if (!pathname.endsWith(".html")) {\n    const htmlPath = \`\${pathname}.html\`;\n    if (htmlPath in PAGES) return htmlPath;\n    const indexPath = \`\${pathname}/index.html\`;\n    if (indexPath in PAGES) return indexPath;\n  }\n  return pathname;\n}\n\nexport default {\n  async fetch(request) {\n    const { pathname } = new URL(request.url);\n    const route = normalizePath(pathname);\n    const body = PAGES[route];\n    if (body) {\n      return new Response(body, {\n        headers: { "content-type": "text/html; charset=utf-8" },\n      });\n    }\n    return new Response("Not found", {\n      status: 404,\n      headers: { "content-type": "text/plain; charset=utf-8" },\n    });\n  },\n};\n`;
  const serverIndexModule = `export { default } from "../index.js";\n`;

  await fs.writeFile(path.join(DIST, "pages.js"), pagesModule, "utf8");
  await fs.writeFile(path.join(DIST, "index.js"), workerModule, "utf8");
  await fs.mkdir(path.join(DIST, "server"), { recursive: true });
  await fs.writeFile(path.join(DIST, "server", "index.js"), serverIndexModule, "utf8");
}

async function main() {
  await fs.rm(DIST, { recursive: true, force: true });
  await fs.mkdir(DIST, { recursive: true });

  await walkMarkdown(".");
  for (const source of SOURCE_MARKDOWN) {
    outputForSource(source);
  }

  const inventoryPath = path.join(ROOT, "manifest", "inventory.jsonl");
  const inventory = await fs.readFile(inventoryPath, "utf8");
  const records = inventory
    .split("\n")
    .filter(Boolean)
    .map((line) => JSON.parse(line));
  const rawRecords = records.filter((r) => r.current_path.startsWith("artifacts/"));
  const duplicateGroups = JSON.parse(
    await fs.readFile(path.join(ROOT, "manifest", "duplicate_sets.json"), "utf8")
  );
  const summary = {
    total: records.length,
    markdown: SOURCE_MARKDOWN.length,
    raw: rawRecords.length,
    duplicateGroups: Object.keys(duplicateGroups).length,
  };

  const rootPage = rootLanding({
    stats: summary,
    pageCount: SOURCE_MARKDOWN.length,
    duplicateGroups: summary.duplicateGroups,
    rawCount: summary.raw,
  });
  await writeRenderedPage("index.html", rootPage);

  const vaultPage = renderVaultPage(records);
  await writeRenderedPage(path.join("vault", "index.html"), vaultPage);

  const sourceRolesPage = renderSourceRolesPage(records);
  await writeRenderedPage(path.join("wiki", "source-roles", "index.html"), sourceRolesPage);

  const artifactTypesPage = renderArtifactTypesPage(records);
  await writeRenderedPage(path.join("wiki", "artifact-types", "index.html"), artifactTypesPage);

  for (const source of SOURCE_MARKDOWN) {
    const outRel = outputForSource(source);
    const sourceText = await fs.readFile(path.join(ROOT, source), "utf8");
    const rendered = renderMarkdown(source, sourceText);
    const titleMatch = sourceText.match(/^#\s+(.+)$/m);
    const title = titleMatch ? titleMatch[1].trim() : path.posix.basename(source, ".md");
    const navActive = `/${outRel.replaceAll(path.sep, "/")}`;
    const body = `
      <p class="eyebrow">${escapeHtml(path.posix.dirname(source) === "." ? "repository" : path.posix.dirname(source))}</p>
      <div class="title-row">
        <h1>${escapeHtml(title)}</h1>
        <span class="tag">${escapeHtml(source)}</span>
      </div>
      <p class="muted">Rendered from markdown source. <a href="${githubUrl(source)}">Open raw source on GitHub</a>.</p>
      ${rendered}
    `;
    const html = pageShell({
      title,
      subtitle: source,
      body,
      navActive,
    });
    await writeRenderedPage(outRel, html);
  }

  await writeWorkerEntrypoints();

  console.log(`Built ${SOURCE_MARKDOWN.length} markdown pages and the vault map in ${DIST}.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
