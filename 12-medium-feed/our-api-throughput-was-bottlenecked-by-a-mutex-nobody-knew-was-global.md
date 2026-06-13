---
title: "Our API Throughput Was Bottlenecked by a Mutex Nobody Knew Was Global"
author: "syarif"
url: "https://elsyarifx.medium.com/our-api-throughput-was-bottlenecked-by-a-mutex-nobody-knew-was-global-da2db8b45545?source=rss------concurrency-5"
published: "Fri, 12 Jun 2026 13:54:23 GMT"
source: "tag:concurrency"
tags: [concurrency, backend-development, software-engineering, programming, golang]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Our API Throughput Was Bottlenecked by a Mutex Nobody Knew Was Global

**Author:** syarif
**Published:** Fri, 12 Jun 2026 13:54:23 GMT
**Tags:** concurrency, backend-development, software-engineering, programming, golang
**Source:** tag:concurrency
**URL:** <https://elsyarifx.medium.com/our-api-throughput-was-bottlenecked-by-a-mutex-nobody-knew-was-global-da2db8b45545?source=rss------concurrency-5>

## Excerpt

The function was fast. The benchmark showed no issue. Under concurrent load, every request serialized through a mutex protecting a metrics&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
