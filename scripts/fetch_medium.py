#!/usr/bin/env python3
"""
Fetch new Medium articles from a curated set of tag and author RSS feeds.

For each new article, write a markdown stub under content/medium-feed/ with
YAML frontmatter (title, author, url, tags, date, rating placeholder, read flag)
so you can mark it up after reading.

Dedup by URL across runs. Idempotent: safe to re-run daily.

Usage:
    pip install feedparser
    python fetch_medium.py
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import feedparser  # type: ignore
except ImportError:
    print("Install feedparser: pip install feedparser", file=sys.stderr)
    sys.exit(1)

# --- Curated feeds for senior Java / backend / DevOps roles -------------------
TAG_FEEDS = [
    "java",
    "spring-boot",
    "spring-framework",
    "microservices",
    "system-design",
    "kubernetes",
    "aws",
    "docker",
    "kafka",
    "distributed-systems",
    "concurrency",
    "jvm",
    "java-8",
    "java-17",
    "design-patterns",
    "rest-api",
    "backend",
    "software-architecture",
]

# Add Medium authors who publish high-signal Java/backend content here.
# Example: "@itnext" or "@javatechonline"
AUTHOR_FEEDS: list[str] = [
    "@javatechonline",
    "@dineshchandgr",
    "@AlexanderObregon",
]

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "12-medium-feed"
SEEN_FILE = OUT_DIR / ".seen-urls.json"

OUT_DIR.mkdir(parents=True, exist_ok=True)


def feed_urls() -> list[tuple[str, str]]:
    """Return [(label, url)] pairs."""
    out = []
    for tag in TAG_FEEDS:
        out.append((f"tag:{tag}", f"https://medium.com/feed/tag/{tag}"))
    for author in AUTHOR_FEEDS:
        out.append((f"author:{author}", f"https://medium.com/feed/{author}"))
    return out


def load_seen() -> set[str]:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text()))
    return set()


def save_seen(seen: set[str]) -> None:
    SEEN_FILE.write_text(json.dumps(sorted(seen), indent=2))


def slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:80] or "untitled"


def write_entry(entry, source_label: str) -> Path | None:
    url = entry.get("link", "")
    if not url:
        return None
    title = entry.get("title", "untitled").strip()
    author = entry.get("author", "unknown")
    published = entry.get("published", "")
    summary = entry.get("summary", "")
    tags = ", ".join(t.get("term", "") for t in entry.get("tags", []) if t.get("term"))

    # First-paragraph plain text from the HTML summary
    plain = re.sub(r"<[^>]+>", " ", summary)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) > 600:
        plain = plain[:600].rsplit(" ", 1)[0] + "…"

    filename = OUT_DIR / f"{slug(title)}.md"
    if filename.exists():
        return None  # already created

    body = f"""---
title: "{title.replace('"', "'")}"
author: "{author}"
url: "{url}"
published: "{published}"
source: "{source_label}"
tags: [{tags}]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# {title}

**Author:** {author}
**Published:** {published}
**Tags:** {tags}
**Source:** {source_label}
**URL:** <{url}>

## Excerpt

{plain}

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
"""
    filename.write_text(body, encoding="utf-8")
    return filename


def main() -> int:
    seen = load_seen()
    new_count = 0
    for label, url in feed_urls():
        try:
            feed = feedparser.parse(url)
        except Exception as exc:
            print(f"[skip] {label}: {exc}", file=sys.stderr)
            continue
        for entry in feed.entries:
            link = entry.get("link", "")
            if not link or link in seen:
                continue
            written = write_entry(entry, label)
            seen.add(link)
            if written:
                new_count += 1
                print(f"[new] {written.name}")
    save_seen(seen)
    print(f"\nDone. {new_count} new articles. Total seen: {len(seen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
