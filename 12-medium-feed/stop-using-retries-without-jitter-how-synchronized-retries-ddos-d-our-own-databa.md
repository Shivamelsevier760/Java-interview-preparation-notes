---
title: "Stop Using Retries Without Jitter — How Synchronized Retries DDoS’d Our Own Database"
author: "The Concurrent Mind"
url: "https://medium.com/@kp9810113/stop-using-retries-without-jitter-how-synchronized-retries-ddosd-our-own-database-54ef52ec2b7b?source=rss------system_design-5"
published: "Sat, 21 Nov 2026 08:18:48 GMT"
source: "tag:system-design"
tags: [design-systems, distributed-systems, programming, software-engineering, database]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Stop Using Retries Without Jitter — How Synchronized Retries DDoS’d Our Own Database

**Author:** The Concurrent Mind
**Published:** Sat, 21 Nov 2026 08:18:48 GMT
**Tags:** design-systems, distributed-systems, programming, software-engineering, database
**Source:** tag:system-design
**URL:** <https://medium.com/@kp9810113/stop-using-retries-without-jitter-how-synchronized-retries-ddosd-our-own-database-54ef52ec2b7b?source=rss------system_design-5>

## Excerpt

40 app servers retried their failed queries at the same instant. Then they all waited exactly the same amount of time and did it again. Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
