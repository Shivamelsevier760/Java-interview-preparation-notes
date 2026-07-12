#!/usr/bin/env node
/**
 * extract_qa.mjs — Extract interview questions & answers from the curated
 * topic folders into `13-questions-and-answers/`.
 *
 * Usage:  node scripts/extract_qa.mjs
 *
 * Heuristics:
 *  - A heading is a question if it ends with `?`, starts with `Q1:`/`Q:` style
 *    prefixes, or is a numbered item that starts with an interrogative or
 *    imperative keyword (What/How/Explain/Describe/...).
 *  - The answer is the body below the heading, up to the next heading of the
 *    same or higher level, or the next question heading.
 *  - Markdown tables: the first column is treated as the question, the other
 *    columns as notes/follow-ups. `*(Looking for: ...)*` fragments inside the
 *    question cell become "interviewer guidance" in the answer.
 *  - Standalone `**Q1: ...**` paragraph lines are treated as questions.
 *  - Numbered/bulleted list items that read like questions are collected in a
 *    per-topic "question bank" (no recorded answer).
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT_DIR_NAME = '13-questions-and-answers';
const OUT_DIR = path.join(ROOT, OUT_DIR_NAME);
const SCRIPT_REL = 'scripts/extract_qa.mjs';

const TOPICS = [
  { src: '01-java', slug: 'java', title: 'Java — Core, Concurrency, JVM, Collections' },
  { src: '02-microservices', slug: 'microservices', title: 'Spring Boot & Microservices' },
  { src: '03-medium-series', slug: 'medium-series', title: 'Medium Interview Series (company questions)' },
  { src: '04-networking', slug: 'networking', title: 'Networking' },
  { src: '05-aws-cloud-practitioner', slug: 'aws-cloud-practitioner', title: 'AWS Cloud Practitioner' },
  { src: '06-aws-developer-associate', slug: 'aws-developer-associate', title: 'AWS Developer Associate (DVA-C02)' },
  { src: '07-devops', slug: 'devops', title: 'DevOps & Cloud' },
  { src: '08-behavioral', slug: 'behavioral', title: 'Behavioral' },
];

// Notion-template noise that lives inside 01-java/linkedin — not interview content.
const EXCLUDED_DIRS = new Set([
  'goals', 'habit-tracker', 'notebook', 'notes-drafts', 'reading-list',
]);
const EXCLUDED_FILES = new Set([
  'goals.md', 'goals-2.md', 'habit-tracker.md', 'notebook.md', 'notebook-2.md',
  'notes-drafts.md', 'notes-drafts-2.md', 'reading-list.md', 'reading-list-2.md',
  'simple-budget.md', 'task-list.md', 'task-list-2.md', 'travel-planner.md',
  'weekly-plan.md',
]);

const INTERROGATIVE =
  /^(what|how|why|when|where|which|who|whom|whose|explain|describe|define|differentiate|difference|compare|can|could|is|are|do|does|did|should|would|will|tell|name|list|write|implement|design|give|state|mention|have you|walk)\b/i;

const MAX_ANSWER_CHARS = 8000;

// ---------------------------------------------------------------------------
// helpers
// ---------------------------------------------------------------------------

function walkMarkdownFiles(dir) {
  const out = [];
  if (!fs.existsSync(dir)) return out;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (EXCLUDED_DIRS.has(entry.name)) continue;
      out.push(...walkMarkdownFiles(full));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      if (EXCLUDED_FILES.has(entry.name)) continue;
      out.push(full);
    }
  }
  return out;
}

/** Strip markdown inline syntax + emoji so we can reason about the text. */
function cleanInline(s) {
  return s
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/[*_`~]+/g, '')
    .replace(/[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{FE0F}\u{200D}]/gu, '')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Does this (cleaned) text read like an interview question? */
function isQuestion(text) {
  const t = text.replace(/["'”’)\]]+$/g, '').trim();
  if (!t || t.length < 8) return false;
  if (/\?$/.test(t)) return true;
  if (/^q\s*\d*\s*[:.)]/i.test(t)) return true;
  const numbered = t.match(/^\d+\s*[.):—–-]\s*(.+)$/);
  if (numbered && INTERROGATIVE.test(numbered[1].trim())) return true;
  return false;
}

/** Strip leading "1." / "Q1:" style prefixes from a question for display. */
function displayQuestion(text) {
  return text
    .replace(/^q\s*\d*\s*[:.)]\s*/i, '')
    .replace(/^\d+\s*[.):—–-]\s*/, '')
    .trim();
}

/** Normalized key used for de-duplication. */
function dedupeKey(text) {
  return displayQuestion(cleanInline(text)).toLowerCase().replace(/[^a-z0-9]+/g, '');
}

/** Tidy an answer body: drop images, demote headings, strip answer labels. */
function tidyAnswer(lines) {
  const out = [];
  let fence = false;
  for (let line of lines) {
    const trimmed = line.trim();
    if (/^(```|~~~)/.test(trimmed)) {
      fence = !fence;
      out.push(line);
      continue;
    }
    if (fence) {
      out.push(line);
      continue;
    }
    if (/^!\[[^\]]*\]\([^)]*\)\s*$/.test(trimmed)) continue; // image-only line
    const heading = trimmed.match(/^#{1,6}\s+(.*)$/);
    if (heading) {
      out.push(`**${cleanInline(heading[1])}**`);
      continue;
    }
    line = line.replace(/^\s*\*\*(answer|a)\s*:?\s*\*\*\s*:?\s*/i, '');
    line = line.replace(/^\s*(answer|ans)\s*:\s*/i, '');
    out.push(line);
  }
  let text = out.join('\n').replace(/\n{3,}/g, '\n\n').trim();
  if (text.length > MAX_ANSWER_CHARS) {
    text = text.slice(0, MAX_ANSWER_CHARS).replace(/\s+\S*$/, '');
    text += '\n\n*…(truncated — see the source note for the full answer)*';
  }
  return text;
}

// ---------------------------------------------------------------------------
// per-file extraction
// ---------------------------------------------------------------------------

function extractFromFile(absPath) {
  const rel = path.relative(ROOT, absPath).split(path.sep).join('/');
  const raw = fs.readFileSync(absPath, 'utf8');
  const lines = raw.split(/\r?\n/);

  const answered = [];
  const unanswered = [];

  // Pass 1: locate structural markers (headings / Q-lines / fences / tables).
  const markers = []; // { idx, level, text } — level 99 for standalone Q-lines
  let fence = false;
  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trim();
    if (/^(```|~~~)/.test(trimmed)) { fence = !fence; continue; }
    if (fence) continue;
    const h = trimmed.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      markers.push({ idx: i, level: h[1].length, text: h[2] });
      continue;
    }
    // Standalone "**Q1: ...**" / "Q:" paragraph lines (not list items, not tables).
    if (!/^[|>]/.test(trimmed) && !/^(\d+\.|[-*+])\s/.test(trimmed)) {
      const cleaned = cleanInline(trimmed);
      if (/^q\s*\d*\s*[:.)]/i.test(cleaned) && cleaned.length >= 8) {
        markers.push({ idx: i, level: 99, text: trimmed });
      }
    }
  }

  // Pass 2: emit question/answer pairs from the markers.
  for (let m = 0; m < markers.length; m++) {
    const mk = markers[m];
    const cleaned = cleanInline(mk.text);
    if (!isQuestion(cleaned)) continue;

    let end = lines.length;
    for (let n = m + 1; n < markers.length; n++) {
      const nx = markers[n];
      const nxCleaned = cleanInline(nx.text);
      const nxLevel = nx.level === 99 ? mk.level : nx.level;
      if (nxLevel <= mk.level || isQuestion(nxCleaned)) { end = nx.idx; break; }
    }

    const answer = tidyAnswer(lines.slice(mk.idx + 1, end));
    const q = displayQuestion(cleaned);
    if (answer) answered.push({ q, answer, source: rel });
    else unanswered.push({ q, source: rel });
  }

  // Pass 3: table rows — first column question, remaining columns notes.
  fence = false;
  let row = null; // accumulating logical row
  const flushRow = () => {
    if (!row) return;
    const cells = row
      .join(' ')
      .split('|')
      .slice(1, -1)
      .map((c) => c.trim());
    row = null;
    if (!cells.length) return;
    const first = cells[0];
    if (!first || /^[-: ]+$/.test(first)) return; // separator row
    // Split off "*(Looking for: ...)*" guidance embedded in the question cell.
    let qPart = first;
    let guidance = '';
    const gm = first.match(/^(.*?)[(（]\s*(looking for|note)\s*:?\s*(.*)$/is);
    if (gm) {
      qPart = gm[1];
      guidance = `${gm[2]}: ${gm[3]}`.replace(/[)）]\s*$/, '').trim();
    }
    const qClean = cleanInline(qPart);
    if (!isQuestion(qClean)) return;
    const rest = cells.slice(1).map((c) => cleanInline(c)).filter(Boolean);
    const parts = [];
    if (guidance) {
      const g = cleanInline(guidance).replace(/\)+\s*$/, '').trim();
      if (g) parts.push(`**Interviewer guidance:** ${g}`);
    }
    if (rest.length) parts.push(`**Follow-ups / notes:** ${rest.join(' — ')}`);
    const q = displayQuestion(qClean);
    if (parts.length) answered.push({ q, answer: parts.join('\n\n'), source: rel });
    else unanswered.push({ q, source: rel });
  };
  for (const line of lines) {
    const trimmed = line.trim();
    if (/^(```|~~~)/.test(trimmed)) { fence = !fence; flushRow(); continue; }
    if (fence) continue;
    if (row) {
      row.push(trimmed);
      if (trimmed.endsWith('|')) flushRow();
      continue;
    }
    if (trimmed.startsWith('|')) {
      row = [trimmed];
      if (trimmed.length > 1 && trimmed.endsWith('|')) flushRow();
    }
  }
  flushRow();

  // Pass 4: list items that read like questions -> question bank.
  fence = false;
  for (const line of lines) {
    const trimmed = line.trim();
    if (/^(```|~~~)/.test(trimmed)) { fence = !fence; continue; }
    if (fence) continue;
    const li = trimmed.match(/^(?:\d+\.|[-*+])\s+(.*)$/);
    if (!li) continue;
    const cleaned = cleanInline(li[1].replace(/^\[[ xX]\]\s*/, ''));
    if (cleaned.length < 15) continue;
    if (/\?$/.test(cleaned.replace(/["'”’)\]]+$/g, '')) || INTERROGATIVE.test(cleaned)) {
      // Require it to *really* look like a question, not a statement bullet.
      if (isQuestion(cleaned) || (INTERROGATIVE.test(cleaned) && /\?/.test(cleaned))) {
        unanswered.push({ q: displayQuestion(cleaned), source: rel });
      }
    }
  }

  return { answered, unanswered };
}

// ---------------------------------------------------------------------------
// output
// ---------------------------------------------------------------------------

function mdEscapePipes(s) {
  return s.replace(/\|/g, '\\|');
}

function buildTopicFile(topic, answered, unanswered) {
  const L = [];
  L.push(`# ${topic.title} — Interview Q&A`);
  L.push('');
  L.push(
    `> Auto-extracted from the notes in [\`${topic.src}/\`](../${topic.src}/) by [\`${SCRIPT_REL}\`](../${SCRIPT_REL}).`,
  );
  L.push('> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.');
  L.push('');
  L.push(
    `**${answered.length} answered question${answered.length === 1 ? '' : 's'}** · ` +
      `**${unanswered.length} question prompt${unanswered.length === 1 ? '' : 's'} without recorded answers**`,
  );
  L.push('');

  if (answered.length) {
    L.push('---');
    L.push('');
    answered.forEach((e, i) => {
      L.push(`## ${i + 1}. ${e.q}`);
      L.push('');
      L.push(`*Source: [\`${e.source}\`](../${e.source})*`);
      L.push('');
      L.push(e.answer);
      L.push('');
      L.push('---');
      L.push('');
    });
  }

  if (unanswered.length) {
    L.push('## Question bank (no recorded answers)');
    L.push('');
    L.push('Prompts collected from the notes that have no written answer yet:');
    L.push('');
    for (const e of unanswered) {
      L.push(`- ${mdEscapePipes(e.q)} — *[\`${e.source}\`](../${e.source})*`);
    }
    L.push('');
  }

  return L.join('\n');
}

function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const summary = [];
  for (const topic of TOPICS) {
    const files = walkMarkdownFiles(path.join(ROOT, topic.src));
    const answered = [];
    const unanswered = [];
    const seen = new Set();

    for (const file of files.sort()) {
      const res = extractFromFile(file);
      for (const e of res.answered) {
        const key = dedupeKey(e.q);
        if (!key || seen.has(key)) continue;
        seen.add(key);
        answered.push(e);
      }
      for (const e of res.unanswered) {
        const key = dedupeKey(e.q);
        if (!key || seen.has(key)) continue;
        seen.add(key);
        unanswered.push(e);
      }
    }

    const fileName = `${topic.slug}-questions-and-answers.md`;
    if (answered.length + unanswered.length === 0) {
      console.log(`${topic.src.padEnd(28)} -> (no Q&A found — skipped)`);
      continue;
    }
    fs.writeFileSync(path.join(OUT_DIR, fileName), buildTopicFile(topic, answered, unanswered) + '\n');
    summary.push({ topic, fileName, answered: answered.length, unanswered: unanswered.length });
    console.log(
      `${topic.src.padEnd(28)} -> ${fileName.padEnd(48)} ${String(answered.length).padStart(4)} answered, ${String(unanswered.length).padStart(4)} question-bank`,
    );
  }

  // Folder index.
  const idx = [];
  idx.push('# Questions & Answers — Extracted Q&A Bank');
  idx.push('');
  idx.push(
    `All interview questions and answers extracted from the curated topic folders, collected in one place. ` +
      `Generated by [\`${SCRIPT_REL}\`](../${SCRIPT_REL}) — regenerate with \`node scripts/extract_qa.mjs\`.`,
  );
  idx.push('');
  idx.push('| Topic | File | Answered Q&A | Question bank |');
  idx.push('| --- | --- | ---: | ---: |');
  let ta = 0;
  let tu = 0;
  for (const s of summary) {
    idx.push(
      `| ${s.topic.title} | [\`${s.fileName}\`](./${s.fileName}) | ${s.answered} | ${s.unanswered} |`,
    );
    ta += s.answered;
    tu += s.unanswered;
  }
  idx.push(`| **Total** | | **${ta}** | **${tu}** |`);
  idx.push('');
  idx.push('**Answered Q&A** — questions with a written answer extracted from the notes.');
  idx.push('');
  idx.push(
    '**Question bank** — question prompts found in the notes (e.g. "questions asked in my interview" lists) that have no recorded answer yet.',
  );
  idx.push('');
  fs.writeFileSync(path.join(OUT_DIR, 'README.md'), idx.join('\n') + '\n');
  console.log(`\nTotal: ${ta} answered, ${tu} question-bank entries -> ${OUT_DIR_NAME}/`);
}

main();
