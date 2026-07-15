---
title: "SQL Server Bulk Delete Batches"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/sql-server-bulk-delete-batches-c53d3b315118?source=rss-4f9731d3205------2"
published: "Wed, 15 Jul 2026 03:52:49 GMT"
source: "author:@AlexanderObregon"
tags: [sql, sql-server, software-development, backend-development, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# SQL Server Bulk Delete Batches

**Author:** Alexander Obregon
**Published:** Wed, 15 Jul 2026 03:52:49 GMT
**Tags:** sql, sql-server, software-development, backend-development, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/sql-server-bulk-delete-batches-c53d3b315118?source=rss-4f9731d3205------2>

## Excerpt

Image Source Large cleanup jobs can put pressure on a busy database when too much data is deleted in one transaction. The delete may be valid, but the transaction can hold locks for longer, grow the transaction log quickly, and make normal reads or writes wait behind the cleanup. Batch deletes break that job into smaller repeatable passes. Each pass removes up to the configured number of old rows, records the affected row count, commits, then continues until no matching rows remain. SQL Server batch delete code should rely on DELETE TOP for row limits, while SET ROWCOUNT should be left out of…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
