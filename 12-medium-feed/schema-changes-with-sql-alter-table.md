---
title: "Schema Changes with SQL ALTER TABLE"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/schema-changes-with-sql-alter-table-f088e706756f?source=rss-4f9731d3205------2"
published: "Thu, 19 Nov 2026 18:26:01 GMT"
source: "author:@AlexanderObregon"
tags: [postgresql, sql, backend-development, coding, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Schema Changes with SQL ALTER TABLE

**Author:** Alexander Obregon
**Published:** Thu, 19 Nov 2026 18:26:01 GMT
**Tags:** postgresql, sql, backend-development, coding, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/schema-changes-with-sql-alter-table-f088e706756f?source=rss-4f9731d3205------2>

## Excerpt

Image Source Database tables don’t always stay the same as an application grows. New requirements can call for extra columns, different data types, or changes to the rules that control what values can be stored. SQL provides the ALTER TABLE statement to update an existing table's structure without having to recreate it from scratch. The records already stored in the table remain, but how they're affected depends on the change being made. Adding a column can introduce NULL values or defaults, while modifying a data type may require existing values to be converted. Other changes, including new…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
