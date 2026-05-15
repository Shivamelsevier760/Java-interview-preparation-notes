---
title: "Expression Indexes in SQL Queries"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/expression-indexes-in-sql-queries-7e8f2528aa67?source=rss-4f9731d3205------2"
published: "Tue, 05 May 2026 00:02:02 GMT"
source: "author:@AlexanderObregon"
tags: [software-development, database-indexing, programming, sql, backend-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Expression Indexes in SQL Queries

**Author:** Alexander Obregon
**Published:** Tue, 05 May 2026 00:02:02 GMT
**Tags:** software-development, database-indexing, programming, sql, backend-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/expression-indexes-in-sql-queries-7e8f2528aa67?source=rss-4f9731d3205------2>

## Excerpt

Image Source Databases run into this problem whenever a query filters on lower(email), on a date pulled from a timestamp, or on something derived from two columns. If an index holds only the raw column data, the optimizer does not always have a direct way to search by that transformed result. An expression index fixes that by storing the result of the expression inside the index, which lets the search target the same transformed result named in the predicate. PostgreSQL calls these indexes indexes on expressions, Oracle calls them function-based indexes, MySQL supports functional index parts,…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
