---
title: "Database Sharding with SQL Routing Columns"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/database-sharding-with-sql-routing-columns-8322d3728de9?source=rss-4f9731d3205------2"
published: "Thu, 20 Aug 2026 19:33:11 GMT"
source: "author:@AlexanderObregon"
tags: [coding, data-science, programming, sql, software-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Database Sharding with SQL Routing Columns

**Author:** Alexander Obregon
**Published:** Thu, 20 Aug 2026 19:33:11 GMT
**Tags:** coding, data-science, programming, sql, software-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/database-sharding-with-sql-routing-columns-8322d3728de9?source=rss-4f9731d3205------2>

## Excerpt

Image Source The main idea of sharding is that it lets storage and traffic grow past the practical limits of one server. The tables on those instances normally share the same schema, while the rows stored on them differ. Routing logic decides which database receives a write and which database should answer a read. In multi-tenant software, tenant_id is a common routing column because it gives the router a stable value that can keep one customer’s related rows in the same area. This choice affects much more than row placement because it determines how several databases can become involved in a…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
