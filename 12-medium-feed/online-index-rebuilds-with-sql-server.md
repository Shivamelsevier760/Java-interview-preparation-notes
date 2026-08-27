---
title: "Online Index Rebuilds with SQL Server"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/online-index-rebuilds-with-sql-server-38477299395f?source=rss-4f9731d3205------2"
published: "Wed, 26 Aug 2026 18:56:01 GMT"
source: "author:@AlexanderObregon"
tags: [sql-server, database, backend-development, sql, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Online Index Rebuilds with SQL Server

**Author:** Alexander Obregon
**Published:** Wed, 26 Aug 2026 18:56:01 GMT
**Tags:** sql-server, database, backend-development, sql, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/online-index-rebuilds-with-sql-server-38477299395f?source=rss-4f9731d3205------2>

## Excerpt

Image Source Busy SQL Server databases still need index maintenance while application traffic is running, which makes online rebuilds a natural solution when long blocking periods would interfere with normal activity. Rebuilding an index creates a new index structure from the existing data, while ONLINE = ON allows regular reads and writes to continue through most of the rebuild. Brief locking phases can still happen near the beginning and end, and the operation can place extra pressure on storage, CPU, I/O, and the transaction log while taking longer to finish. SQL Server also has REORGANIZE…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
