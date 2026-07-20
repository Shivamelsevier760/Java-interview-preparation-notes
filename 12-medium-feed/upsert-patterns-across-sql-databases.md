---
title: "UPSERT Patterns Across SQL Databases"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/upsert-patterns-across-sql-databases-cba4243c7032?source=rss-4f9731d3205------2"
published: "Sun, 19 Jul 2026 12:59:44 GMT"
source: "author:@AlexanderObregon"
tags: [backend-development, software-development, technology, sql, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# UPSERT Patterns Across SQL Databases

**Author:** Alexander Obregon
**Published:** Sun, 19 Jul 2026 12:59:44 GMT
**Tags:** backend-development, software-development, technology, sql, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/upsert-patterns-across-sql-databases-cba4243c7032?source=rss-4f9731d3205------2>

## Excerpt

Image Source Insert-or-update logic lets one statement add a row when its identifying value is absent and revise the stored row when that value already exists. Each database product handles that decision differently. PostgreSQL adds ON CONFLICT to an INSERT statement and can infer a qualifying unique index or name the constraint that settles the conflict. MySQL provides ON DUPLICATE KEY UPDATE, which reacts to a primary or unique index violation and needs extra care on tables with several unique indexes. SQL Server includes MERGE, along with separate UPDATE and INSERT statements that are…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
