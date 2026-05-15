---
title: "Covering Indexes in SQL Queries"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/covering-indexes-in-sql-queries-912a137127f8?source=rss-4f9731d3205------2"
published: "Mon, 27 Apr 2026 22:29:48 GMT"
source: "author:@AlexanderObregon"
tags: [programming, software-development, sql, database-indexing, backend-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Covering Indexes in SQL Queries

**Author:** Alexander Obregon
**Published:** Mon, 27 Apr 2026 22:29:48 GMT
**Tags:** programming, software-development, sql, database-indexing, backend-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/covering-indexes-in-sql-queries-912a137127f8?source=rss-4f9731d3205------2>

## Excerpt

Image Source The idea of a covering index makes more sense when you tie it to what the database is actually doing during a query. It is not a separate index type with its own CREATE INDEX command. It is just a way to describe a case where one index already contains every column a query needs, so the database can return the result from the index itself instead of going back to the base table for extra column values. In SQL Server, that can happen with a nonclustered index. In PostgreSQL, it lines up with index-only scans when the needed columns are stored in the index. In MySQL, the same idea…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
