---
title: "Our Retry Logic Was Correct. Our Retry Timing Was Destroying the Downstream Service."
author: "syarif"
url: "https://elsyarifx.medium.com/our-retry-logic-was-correct-our-retry-timing-was-destroying-the-downstream-service-8ac4ef4f83fb?source=rss------distributed_systems-5"
published: "Sun, 28 Jun 2026 04:55:41 GMT"
source: "tag:distributed-systems"
tags: [backend-development, distributed-systems, programming, software-development, golang]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Our Retry Logic Was Correct. Our Retry Timing Was Destroying the Downstream Service.

**Author:** syarif
**Published:** Sun, 28 Jun 2026 04:55:41 GMT
**Tags:** backend-development, distributed-systems, programming, software-development, golang
**Source:** tag:distributed-systems
**URL:** <https://elsyarifx.medium.com/our-retry-logic-was-correct-our-retry-timing-was-destroying-the-downstream-service-8ac4ef4f83fb?source=rss------distributed_systems-5>

## Excerpt

Exponential backoff with jitter is the right answer. We had the backoff. We didn&#x2019;t have the jitter. Under load, all our retries fired&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
