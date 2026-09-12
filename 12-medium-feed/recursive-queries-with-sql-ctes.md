---
title: "Recursive Queries with SQL CTEs"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/recursive-queries-with-sql-ctes-f4d27eddfbf4?source=rss-4f9731d3205------2"
published: "Fri, 11 Sep 2026 18:51:01 GMT"
source: "author:@AlexanderObregon"
tags: [programming, software-development, sql, data-science, backend-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Recursive Queries with SQL CTEs

**Author:** Alexander Obregon
**Published:** Fri, 11 Sep 2026 18:51:01 GMT
**Tags:** programming, software-development, sql, data-science, backend-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/recursive-queries-with-sql-ctes-f4d27eddfbf4?source=rss-4f9731d3205------2>

## Excerpt

Image Source Hierarchical data can contain relationships where one row points back to a different row in the same table, which is common with category trees, employee reporting chains, folder hierarchies, product components, threaded comments, and related data. Tables can keep only the direct parent reference for a row while a recursive common table expression follows those references through as much of the hierarchy as needed. Within the CTE, the first query member returns the starting rows, then the recursive member joins those results back to the source table to find the next level.…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
