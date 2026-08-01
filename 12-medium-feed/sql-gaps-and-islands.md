---
title: "SQL Gaps and Islands"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/sql-gaps-and-islands-6ef34af6eb7f?source=rss-4f9731d3205------2"
published: "Fri, 31 Jul 2026 18:46:02 GMT"
source: "author:@AlexanderObregon"
tags: [backend-development, sql, coding, programming, software-development]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# SQL Gaps and Islands

**Author:** Alexander Obregon
**Published:** Fri, 31 Jul 2026 18:46:02 GMT
**Tags:** backend-development, sql, coding, programming, software-development
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/sql-gaps-and-islands-6ef34af6eb7f?source=rss-4f9731d3205------2>

## Excerpt

Image Source Rows stored separately can still belong to the same uninterrupted period when their dates or times follow the continuity rule chosen for the query. Attendance records may contain a five-day streak, followed by a pause and then a two-day streak, while subscription ranges can overlap or meet at their boundaries and belong to the same active period. Event data can also leave empty spans that a report needs to return as breaks. Gaps and islands queries group ordered rows into these ranges. An island is a run of related values with no break under the chosen rule, while a gap is the…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
