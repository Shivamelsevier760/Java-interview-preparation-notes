---
title: "Mo’s Algorithm for Range Queries in Java"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/mos-algorithm-for-range-queries-in-java-05a89e7d4de2?source=rss-4f9731d3205------2"
published: "Fri, 29 May 2026 18:16:00 GMT"
source: "author:@AlexanderObregon"
tags: [java, programming, coding, software-development, algorithms]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Mo’s Algorithm for Range Queries in Java

**Author:** Alexander Obregon
**Published:** Fri, 29 May 2026 18:16:00 GMT
**Tags:** java, programming, coding, software-development, algorithms
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/mos-algorithm-for-range-queries-in-java-05a89e7d4de2?source=rss-4f9731d3205------2>

## Excerpt

Image Source Range query problems can get expensive when every request scans its own slice of the array from scratch. Mo’s Algorithm handles that by processing all queries offline, then sorting them so nearby ranges are answered near one another. The algorithm keeps one active range with a left edge, a right edge, and saved state for the values currently inside that range. As the sorted queries move forward, indexes that enter the range are added, and indexes that leave are removed. For a problem like counting distinct values in a subarray, that means we update only the changed positions…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
