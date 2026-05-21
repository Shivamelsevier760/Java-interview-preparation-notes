---
title: "SQL Semi Joins with Match Checks"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/sql-semi-joins-with-match-checks-912164b501b9?source=rss-4f9731d3205------2"
published: "Thu, 21 May 2026 02:25:41 GMT"
source: "author:@AlexanderObregon"
tags: [backend-development, sql, programming, software-development, technology]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# SQL Semi Joins with Match Checks

**Author:** Alexander Obregon
**Published:** Thu, 21 May 2026 02:25:41 GMT
**Tags:** backend-development, sql, programming, software-development, technology
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/sql-semi-joins-with-match-checks-912164b501b9?source=rss-4f9731d3205------2>

## Excerpt

Image Source Match checks come up when one table needs to keep rows that have a related row in another table. The query does not need columns from the matching table, because the only question is if a match exists. That is where semi join logic fits. It filters rows from one input by checking the other input, while the final result still returns rows from one side only. EXISTS fits this well because it asks the database for a true-or-false result instead of asking it to build joined output rows. The result stays focused on the row being tested, which makes the query read closer to the actual…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
