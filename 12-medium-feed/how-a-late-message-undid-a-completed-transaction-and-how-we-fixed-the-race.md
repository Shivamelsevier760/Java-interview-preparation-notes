---
title: "How a Late Message Undid a Completed Transaction (and How We Fixed the Race)"
author: "Sumit Pandey"
url: "https://medium.com/@sumitpandey0663/how-a-late-message-undid-a-completed-transaction-and-how-we-fixed-the-race-4aa835b55c82?source=rss------concurrency-5"
published: "Mon, 16 Nov 2026 20:45:46 GMT"
source: "tag:concurrency"
tags: [concurrency, cassandra, distributed-systems, backend-development, software-engineering]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# How a Late Message Undid a Completed Transaction (and How We Fixed the Race)

**Author:** Sumit Pandey
**Published:** Mon, 16 Nov 2026 20:45:46 GMT
**Tags:** concurrency, cassandra, distributed-systems, backend-development, software-engineering
**Source:** tag:concurrency
**URL:** <https://medium.com/@sumitpandey0663/how-a-late-message-undid-a-completed-transaction-and-how-we-fixed-the-race-4aa835b55c82?source=rss------concurrency-5>

## Excerpt

Reports showed a transaction completed; the next step said it hadn&#x2019;t. The logs found two messages 13 ms apart, a check-then-act race, and&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
