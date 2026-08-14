---
title: "Most Go Kafka Consumers Leak Through a Path Goroutine Profilers Don’t Flag"
author: "syarif"
url: "https://elsyarifx.medium.com/most-go-kafka-consumers-leak-through-a-path-goroutine-profilers-dont-flag-cc00334f93a8?source=rss------concurrency-5"
published: "Thu, 13 Aug 2026 14:34:07 GMT"
source: "tag:concurrency"
tags: [programming, software-engineering, golang, concurrency, performance]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Most Go Kafka Consumers Leak Through a Path Goroutine Profilers Don’t Flag

**Author:** syarif
**Published:** Thu, 13 Aug 2026 14:34:07 GMT
**Tags:** programming, software-engineering, golang, concurrency, performance
**Source:** tag:concurrency
**URL:** <https://elsyarifx.medium.com/most-go-kafka-consumers-leak-through-a-path-goroutine-profilers-dont-flag-cc00334f93a8?source=rss------concurrency-5>

## Excerpt

Not a stuck goroutine. A worker pool that keeps growing one rebalance at a time, invisible until the pod gets OOM-killed. Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
