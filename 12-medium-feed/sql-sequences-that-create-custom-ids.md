---
title: "SQL Sequences That Create Custom IDs"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/sql-sequences-that-create-custom-ids-a15fb95e9dfb?source=rss-4f9731d3205------2"
published: "Wed, 08 Jul 2026 19:41:00 GMT"
source: "author:@AlexanderObregon"
tags: [sql, software-development, programming, backend-development, database]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# SQL Sequences That Create Custom IDs

**Author:** Alexander Obregon
**Published:** Wed, 08 Jul 2026 19:41:00 GMT
**Tags:** sql, software-development, programming, backend-development, database
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/sql-sequences-that-create-custom-ids-a15fb95e9dfb?source=rss-4f9731d3205------2>

## Excerpt

Image Source Custom IDs make more sense when the database counter lives outside the table that stores the final row. Sequence objects return numeric values on request, and those values can become invoice numbers, shared order numbers, or reserved ID ranges for later allocation. The main difference from an identity column is that the counter can serve more than one table or statement. PostgreSQL calls nextval, SQL Server calls NEXT VALUE FOR, and Oracle reads sequence_name.NEXTVAL, while regular MySQL releases usually rely on AUTO_INCREMENT instead of standalone sequence objects. I publish…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
