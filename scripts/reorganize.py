#!/usr/bin/env python3
"""
Reorganize a Notion markdown export into a clean, categorized vault.

What it does:
  1. Walks the source export recursively.
  2. Strips Notion's 32-char hash suffixes from every file and folder.
  3. Lowercases + kebab-cases filenames.
  4. Rewrites internal markdown links (images, page links) to point at the new paths.
  5. Maps top-level pages to category folders (interview / work / personal).
  6. Generates a .md mirror next to every Notion-database .csv for grep-ability.

Usage:
  python reorganize.py <source-dir> <dest-dir>
"""
from __future__ import annotations

import csv
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote

HASH_RE = re.compile(r"[ _-]?[0-9a-f]{32}(?:[ _-]all)?(?=\.[^.]+$|$)")

# --- Category mapping: top-level Notion page name -> vault folder ----------
# Match is on the cleaned (hash-stripped, trimmed) name, case-insensitive.
CATEGORY_MAP: dict[str, str] = {
    # Java (highest priority for interview prep)
    "java linkedin interview questions": "01-java/linkedin",
    "java instant interview question from linkedin coll": "01-java/linkedin-instant",
    "java interview questions and notes from linkedin t": "01-java/linkedin-notes",
    "java interview final from linkedin for the develop": "01-java/linkedin-final",
    "java interview questions from elsevier": "01-java/elsevier",
    "java printable notes by code decode": "01-java/code-decode",
    "interview questions collected by the linkedin cand": "01-java/linkedin-candidates",
    "learning through real interview questions": "01-java/real-interviews",
    "leetcode java interview questions": "01-java/leetcode",
    # Microservices
    "microservices interview questions for 3+ years exp": "02-microservices",
    # Medium series
    "medium interview company questions deep dive serie": "03-medium-series/deep-dive",
    "medium interview company questions part 1": "03-medium-series/part-1",
    "medium interview company questions part 2": "03-medium-series/part-2",
    "medium interview company questions part 3 by shiva": "03-medium-series/part-3",
    "medium interview company questions part 4 by shiva": "03-medium-series/part-4",
    "medium interview company questions part 5 by shiva": "03-medium-series/part-5",
    "medium interview company questions part 6 by shiva": "03-medium-series/part-6",
    "medium interview company questions part 7 by shiva": "03-medium-series/part-7",
    "medium interview questions part 1": "03-medium-series/other-part-1",
    "medium interview questions part 2": "03-medium-series/other-part-2",
    "medium articles to read for the interview question": "03-medium-series/to-read",
    # Networking
    "networking interview questions": "04-networking",
    # AWS Cloud Practitioner
    "aws cloud practioner notes and resources to study": "05-aws-cloud-practitioner/notes-and-resources",
    "aws cloud practitioner from tutorial dojo": "05-aws-cloud-practitioner/tutorials-dojo",
    "aws cloud practitioner notes for the examination": "05-aws-cloud-practitioner/exam-notes",
    "aws cloud practitioner test mistake questions for": "05-aws-cloud-practitioner/test-mistakes",
    "aws handmade notes from reyaz": "05-aws-cloud-practitioner/handmade-reyaz",
    "aws key points to remember": "05-aws-cloud-practitioner/key-points",
    "cheat sheets for aws cloud practitioner": "05-aws-cloud-practitioner/cheat-sheets",
    "need to print this cloud practitioner notes": "05-aws-cloud-practitioner/printable",
    "tutorials dojo test notes and questions": "05-aws-cloud-practitioner/tutorials-dojo-tests",
    "aws practice mock results": "05-aws-cloud-practitioner/mock-results",
    # AWS Developer Associate
    "aws developer associate (dva-c02)": "06-aws-developer-associate",
    # DevOps
    "devops training and roadmap content from elsevier": "07-devops",
    # Behavioral
    "self introduction sandeep kumar": "08-behavioral/self-intro-sandeep",
    "self introduction for interviews": "08-behavioral/self-intro",
    "self introduction new for the interviews": "08-behavioral/self-intro-new",
    # References
    "important links from learning point of view": "09-references/important-links",
    "reading list": "09-references/reading-list",
    # Work
    "cdm ticket to change the ecr": "10-work/cdm-ecr",
    "change request ticket issue that i need to fix": "10-work/change-request",
    "change the ecr id for the cdrc - 7467": "10-work/ecr-cdrc-7467",
    "changed the ecr id in cdm for the change request i": "10-work/ecr-changed",
    "changing the ecr id for the particular change requ": "10-work/ecr-changing",
    "existing code in the cdm for the checkmarx": "10-work/checkmarx",
    "detailed notes along with the meeting with raj": "10-work/meeting-raj",
    "meeting demo automating bypass for pattern 3 cdm t": "10-work/meeting-bypass",
    "trillium address validation": "10-work/trillium",
    "semarchy certification training notes": "10-work/semarchy",
    "gdpr": "10-work/gdpr",
    "entities and their attributes in elsevier": "10-work/entities",
    "mechanism to bulk upload pre-determined matches pr": "10-work/bulk-upload",
    "recent and upcoming discussion with buddy": "10-work/buddy-discussions",
    # Personal
    "journal": "11-personal/journal",
    "personal home": "11-personal/home",
    "people": "11-personal/people",
    "quick note": "11-personal/quick-notes",
    "task list": "11-personal/tasks",
    "getting started": "11-personal/getting-started",
    "home": "11-personal/home-page",
    "@september 16, 2025 2 31 pm": "11-personal/dated-2025-09-16",
    "untitled": "11-personal/untitled",
    "screen view": "11-personal/screen-view",
}

# ---------------------------------------------------------------------------


def strip_hash(name: str) -> str:
    """Strip Notion's 32-char hex hash suffix and tidy whitespace."""
    stem, dot, ext = name.rpartition(".")
    if not dot:  # no extension (directory or extensionless file)
        cleaned = HASH_RE.sub("", name).strip()
        return cleaned
    cleaned_stem = HASH_RE.sub("", stem).strip()
    return f"{cleaned_stem}.{ext}" if cleaned_stem else f"untitled.{ext}"


def kebab(name: str) -> str:
    """Convert a name to lowercase-kebab-case while preserving extension."""
    stem, dot, ext = name.rpartition(".")
    if not dot:
        return _kebab_part(name)
    return f"{_kebab_part(stem)}.{ext.lower()}"


def _kebab_part(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "untitled"


def category_for(top_level_clean_name: str) -> str:
    """Return the target category folder for a given top-level page name."""
    # Drop extension so .md/.csv top-level entries map the same as their dir twins
    key = top_level_clean_name.rsplit(".", 1)[0].lower().strip()
    if key in CATEGORY_MAP:
        return CATEGORY_MAP[key]
    # Fuzzy fallbacks
    if "java" in key and "interview" in key:
        return "01-java/misc"
    if "spring" in key:
        return "02-microservices/spring-misc"
    if "microservice" in key:
        return "02-microservices/misc"
    if "medium" in key:
        return "03-medium-series/misc"
    if "aws" in key:
        return "05-aws-cloud-practitioner/misc"
    if "devops" in key or "kubernetes" in key or "docker" in key:
        return "07-devops/misc"
    if "interview" in key:
        return "01-java/misc"
    if "self introduction" in key:
        return "08-behavioral/misc"
    return "99-uncategorized"


def build_rename_plan(src_root: Path, dest_root: Path) -> dict[Path, Path]:
    """Walk source and build {source-path -> dest-path} for every file & dir."""
    plan: dict[Path, Path] = {}
    src_root = src_root.resolve()
    top_entries = sorted(src_root.iterdir())

    # First pass: derive top-level category for each immediate child
    top_category: dict[str, str] = {}
    for entry in top_entries:
        clean = strip_hash(entry.name)
        top_category[entry.name] = category_for(clean)

    for entry in top_entries:
        rel = entry.relative_to(src_root)
        category = top_category[entry.name]
        _walk(entry, src_root, dest_root / category, plan)
    return plan


def _walk(node: Path, src_root: Path, dest_dir: Path, plan: dict[Path, Path]) -> None:
    """Recursively assign clean dest paths."""
    cleaned = kebab(strip_hash(node.name))
    target = dest_dir / cleaned
    # Avoid collisions
    if target in plan.values():
        i = 2
        while True:
            stem, dot, ext = cleaned.rpartition(".")
            if dot:
                candidate = dest_dir / f"{stem}-{i}.{ext}"
            else:
                candidate = dest_dir / f"{cleaned}-{i}"
            if candidate not in plan.values():
                target = candidate
                break
            i += 1
    plan[node] = target
    if node.is_dir():
        for child in sorted(node.iterdir()):
            _walk(child, src_root, target, plan)


def rewrite_md_links(text: str, src_md: Path, plan: dict[Path, Path]) -> str:
    """Rewrite markdown links/images so they point at the new locations.

    Notion writes links like:  ![alt](Page%20Name%20<hash>/image.png)
    """
    src_dir = src_md.parent
    new_md = plan[src_md]
    new_dir = new_md.parent
    # Reverse lookup: (resolved absolute source path) -> new absolute path
    abs_plan = {p.resolve(): t for p, t in plan.items()}

    def replace(match: re.Match) -> str:
        prefix, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        decoded = unquote(url.split("#")[0].split("?")[0])
        anchor = url[len(quote(decoded)):] if quote(decoded) in url else ""
        candidate = (src_dir / decoded).resolve()
        if candidate in abs_plan:
            new_target = abs_plan[candidate]
            try:
                new_rel = os.path.relpath(new_target, new_dir)
            except ValueError:
                new_rel = str(new_target)
            new_rel = new_rel.replace(os.sep, "/")
            return f"{prefix}({quote(new_rel)}{anchor})"
        return match.group(0)

    # Match both ![alt](url) and [text](url)
    pattern = re.compile(r"(!?\[[^\]]*\])\(([^)]+)\)")
    return pattern.sub(replace, text)


def csv_to_md(csv_path: Path) -> str:
    """Render a CSV file as a markdown table."""
    rows = []
    try:
        with open(csv_path, "r", encoding="utf-8", errors="replace") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
    except Exception as exc:
        return f"_Failed to parse CSV: {exc}_\n"
    if not rows:
        return "_(empty database)_\n"
    headers = rows[0]
    width = len(headers)
    out = []
    out.append("| " + " | ".join(h.strip() or "—" for h in headers) + " |")
    out.append("| " + " | ".join("---" for _ in range(width)) + " |")
    for row in rows[1:]:
        cells = [c.replace("\n", "<br>").replace("|", "\\|").strip() or "—" for c in row]
        if len(cells) < width:
            cells.extend(["—"] * (width - len(cells)))
        out.append("| " + " | ".join(cells[:width]) + " |")
    return "\n".join(out) + "\n"


def execute_plan(plan: dict[Path, Path]) -> tuple[int, int, int]:
    """Copy files according to the plan, rewriting markdown links along the way."""
    files = 0
    dirs = 0
    csv_extras = 0
    for src, dest in plan.items():
        if src.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
            dirs += 1
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".md":
            text = src.read_text(encoding="utf-8", errors="replace")
            text = rewrite_md_links(text, src, plan)
            dest.write_text(text, encoding="utf-8")
        elif src.suffix.lower() == ".csv":
            shutil.copy2(src, dest)
            md_text = csv_to_md(src)
            md_dest = dest.with_suffix(".md")
            md_dest.write_text(
                f"# {dest.stem.replace('-', ' ').title()} (database export)\n\n{md_text}",
                encoding="utf-8",
            )
            csv_extras += 1
        else:
            shutil.copy2(src, dest)
        files += 1
    return files, dirs, csv_extras


def main():
    if len(sys.argv) != 3:
        print("usage: reorganize.py <source-dir> <dest-dir>", file=sys.stderr)
        sys.exit(2)
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    plan = build_rename_plan(src, dest)
    files, dirs, csv_extras = execute_plan(plan)
    print(f"copied {files} files into {dirs} directories")
    print(f"generated {csv_extras} markdown mirrors of CSV databases")


if __name__ == "__main__":
    main()
