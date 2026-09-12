---
title: "Understanding Bitcask, Part 1: Append-Only Storage, KeyDir, and Safe Compaction"
author: "Lakshay Sharma"
url: "https://medium.com/@lakshyaa149/bitcask-deep-dive-1-b3e63fff003e?source=rss------system_design-5"
published: "Fri, 11 Sep 2026 20:39:13 GMT"
source: "tag:system-design"
tags: [bitcask, design-systems, deep-dives, append-only-write, log-structured-hash-table]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Understanding Bitcask, Part 1: Append-Only Storage, KeyDir, and Safe Compaction

**Author:** Lakshay Sharma
**Published:** Fri, 11 Sep 2026 20:39:13 GMT
**Tags:** bitcask, design-systems, deep-dives, append-only-write, log-structured-hash-table
**Source:** tag:system-design
**URL:** <https://medium.com/@lakshyaa149/bitcask-deep-dive-1-b3e63fff003e?source=rss------system_design-5>

## Excerpt

How Bitcask handles active files, fast lookups, and races between normal writes and merging. Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
