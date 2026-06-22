#!/usr/bin/env node
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(ROOT, "dist");
const REPO_URL = "https://github.com/bobrs/_work-vault-wiki/blob/main";
const SOURCE_MARKDOWN = [];
const OUTPUT_FOR_SOURCE = new Map();

const NAV_ITEMS = [
  ["Home", "/index.html"],
  ["Wiki", "/wiki/index.html"],
  ["Vault", "/vault/index.html"],
  ["Projects", "/wiki/projects/index.html"],
  ["Concepts", "/wiki/concepts/index.html"],
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
      max-width: 1060px;
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
        border-right: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      }
      .content { padding: 16px; }
      .page { padding: 20px; }
      .card { grid-column: span 12; }
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
  return pageShell({
    title: "Work Vault",
    subtitle: "Public landing page for the repository and wiki",
    body: `
      <p class="eyebrow">Public landing</p>
      <div class="title-row">
        <h1>Work Vault</h1>
        <span class="tag">static publish prep</span>
      </div>
      <p>This site is the static web wrapper for a public vault. The raw repository stays on GitHub, while this interface renders the wiki and exposes the file inventory as a browsable map.</p>
      <div class="hero-grid">
        <div class="card">
          <p class="stat">${stats.total}</p>
          <p class="muted">Files witnessed in the current repository snapshot.</p>
        </div>
        <div class="card">
          <p class="stat">${rawCount}</p>
          <p class="muted">Raw vault files under <code>artifacts/</code>.</p>
        </div>
        <div class="card">
          <p class="stat">${pageCount}</p>
          <p class="muted">Markdown wiki and instruction pages rendered as static HTML.</p>
        </div>
        <div class="card">
          <p class="stat">${duplicateGroups}</p>
          <p class="muted">Exact duplicate hash groups recorded in the current manifest.</p>
        </div>
        <div class="card wide">
          <h2>Current corpus</h2>
          <p>The incoming batch is still represented as an intake corpus. The active branch pages describe the major clusters and point at the files that support them.</p>
          <p><a href="/wiki/index.html">Open the wiki</a> or <a href="/vault/index.html">browse the vault map</a>.</p>
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
  await fs.writeFile(path.join(DIST, "index.html"), rootPage, "utf8");

  const vaultPage = renderVaultPage(records);
  await fs.mkdir(path.join(DIST, "vault"), { recursive: true });
  await fs.writeFile(path.join(DIST, "vault", "index.html"), vaultPage, "utf8");

  for (const source of SOURCE_MARKDOWN) {
    const outRel = outputForSource(source);
    const absOut = path.join(DIST, outRel);
    await fs.mkdir(path.dirname(absOut), { recursive: true });
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
    await fs.writeFile(absOut, html, "utf8");
  }

  console.log(`Built ${SOURCE_MARKDOWN.length} markdown pages and the vault map in ${DIST}.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
