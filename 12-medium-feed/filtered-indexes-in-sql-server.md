---
title: "Filtered Indexes in SQL Server"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/filtered-indexes-in-sql-server-946b62d99a5c?source=rss-4f9731d3205------2"
published: "Thu, 14 May 2026 18:11:00 GMT"
source: "author:@AlexanderObregon"
tags: [programming, sql-server, backend-development, sql, software-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Filtered Indexes in SQL Server

**Author:** Alexander Obregon
**Published:** Thu, 14 May 2026 18:11:00 GMT
**Tags:** programming, sql-server, backend-development, sql, software-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/filtered-indexes-in-sql-server-946b62d99a5c?source=rss-4f9731d3205------2>

## Excerpt

Image Source With filtered rowstore indexes, SQL Server can build a nonclustered index that covers only the rows a query is likely to read. That changes the size of the index, the statistics attached to it, and the upkeep tied to INSERT, UPDATE, and DELETE activity. On tables where the busiest queries keep returning to the same narrow slice of data, that smaller index can do more good than one that tracks every row in the table. Its benefits come from trimming storage, lowering upkeep, and helping query performance when the filter matches a well-defined subset. I publish many free articles…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
