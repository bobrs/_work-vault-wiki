#!/usr/bin/env node
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(ROOT, "dist");
const MAX_FILE_SIZE = 25 * 1024 * 1024;

const REQUIRED_FILES = [
  "index.html",
  "search/index.html",
  "search.json",
  "graph/index.html",
  "graph/index.json",
  "graph/projects/index.html",
  "graph/projects.json",
  "graph/attractors/index.html",
  "graph/attractors.json",
  "graph/concepts/index.html",
  "graph/concepts.json",
  "graph/essays/index.html",
  "graph/essays.json",
  "graph/source-roles/index.html",
  "graph/source-roles.json",
  "graph/artifact-types/index.html",
  "graph/artifact-types.json",
  "wiki/index.html",
  "wiki/paths/index.html",
  "wiki/maintenance/index.html",
  "wiki/incoming-review.html",
  "wiki/duplicate-review.html",
  "wiki/missing-files.html",
  "vault/index.html",
  "ai/index.html",
  "start-here-for-ai/index.html",
  "readme.html",
];

const REQUIRED_TEXT_SNIPPETS = [
  { file: "index.html", snippet: "Wiki build version" },
  { file: "wiki/index.html", snippet: "Wiki build version" },
  { file: "search/index.html", snippet: "metadata-first" },
  { file: "graph/index.html", snippet: "Graph Exports" },
  { file: "wiki/maintenance/index.html", snippet: "Maintenance Hub" },
];

function fail(message) {
  throw new Error(message);
}

async function fileExists(relPath) {
  try {
    await fs.access(path.join(DIST, relPath));
    return true;
  } catch {
    return false;
  }
}

async function readJson(relPath) {
  const body = await fs.readFile(path.join(DIST, relPath), "utf8");
  try {
    return JSON.parse(body);
  } catch (error) {
    fail(`Invalid JSON in ${relPath}: ${error.message}`);
  }
}

async function ensureFile(relPath) {
  if (!(await fileExists(relPath))) {
    fail(`Missing required output: dist/${relPath}`);
  }
}

async function ensureSnippet(relPath, snippet) {
  const body = await fs.readFile(path.join(DIST, relPath), "utf8");
  if (!body.includes(snippet)) {
    fail(`Missing snippet "${snippet}" in dist/${relPath}`);
  }
}

async function walkFiles(dirRel = "") {
  const absDir = path.join(DIST, dirRel);
  const entries = await fs.readdir(absDir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const rel = path.join(dirRel, entry.name);
    if (entry.isDirectory()) {
      files.push(...await walkFiles(rel));
    } else if (entry.isFile()) {
      files.push(rel);
    }
  }
  return files;
}

async function main() {
  await ensureFile("index.html");
  for (const relPath of REQUIRED_FILES) {
    await ensureFile(relPath);
  }
  for (const { file, snippet } of REQUIRED_TEXT_SNIPPETS) {
    await ensureSnippet(file, snippet);
  }

  const searchRecords = await readJson("search.json");
  if (!Array.isArray(searchRecords) || searchRecords.length < 1) {
    fail("search.json must contain a non-empty array");
  }
  if (!searchRecords.some((record) => record.collection === "maintenance")) {
    fail("search.json is missing maintenance collection records");
  }
  if (!searchRecords.some((record) => record.collection === "graph")) {
    fail("search.json is missing graph collection records");
  }

  const graphIndex = await readJson("graph/index.json");
  if (!graphIndex || graphIndex.kind !== "graph_index" || !Array.isArray(graphIndex.collections) || graphIndex.collections.length < 1) {
    fail("graph/index.json must contain a graph_index payload with collections");
  }
  for (const relPath of [
    "graph/projects.json",
    "graph/attractors.json",
    "graph/concepts.json",
    "graph/essays.json",
    "graph/source-roles.json",
    "graph/artifact-types.json",
  ]) {
    const payload = await readJson(relPath);
    if (!payload || payload.kind !== "graph_collection" || !Array.isArray(payload.nodes) || !Array.isArray(payload.edges)) {
      fail(`${relPath} must contain a graph_collection payload`);
    }
  }

  const fileList = await walkFiles();
  const oversized = [];
  for (const relPath of fileList) {
    const stat = await fs.stat(path.join(DIST, relPath));
    if (stat.size > MAX_FILE_SIZE) {
      oversized.push({ relPath, size: stat.size });
    }
  }
  if (oversized.length) {
    const details = oversized.map((item) => `${item.relPath} (${item.size} bytes)`).join(", ");
    fail(`Files exceed the Cloudflare Pages 25 MiB limit: ${details}`);
  }

  console.log(`Validated ${fileList.length} files in dist/`);
}

main().catch((error) => {
  console.error(error.message || error);
  process.exit(1);
});
