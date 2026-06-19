---
title: "Soft Deletes in SQL Tables"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/soft-deletes-in-sql-tables-7c4fb37441e8?source=rss-4f9731d3205------2"
published: "Thu, 18 Jun 2026 18:51:00 GMT"
source: "author:@AlexanderObregon"
tags: [coding, database, software-development, sql, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Soft Deletes in SQL Tables

**Author:** Alexander Obregon
**Published:** Thu, 18 Jun 2026 18:51:00 GMT
**Tags:** coding, database, software-development, sql, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/soft-deletes-in-sql-tables-7c4fb37441e8?source=rss-4f9731d3205------2>

## Excerpt

Image Source With soft deletes, a table keeps a row in place while normal application views treat it as removed. Instead of running DELETE FROM orders WHERE id = 25, the database updates a marker like is_deleted = true or deleted_at = CURRENT_TIMESTAMP. Queries for active records filter out rows with that marker, admin screens can still review them, and restore queries can bring the row back without rebuilding it from backups or audit logs. Soft deletes fit business tables where removed data still has value for support, reporting, recovery, legal review, or user-facing undo flows. I publish…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
