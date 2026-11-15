---
title: "Our JVM pods were OOM-killed with 5 GiB of heap free"
author: "Aditya Barik"
url: "https://medium.com/@aditya.barik32/our-jvm-pods-were-oom-killed-with-5-gib-of-heap-free-a44b01094dd8?source=rss------jvm-5"
published: "Sat, 14 Nov 2026 17:16:44 GMT"
source: "tag:jvm"
tags: [java, jemalloc, jvm, heap-memory, glibc]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Our JVM pods were OOM-killed with 5 GiB of heap free

**Author:** Aditya Barik
**Published:** Sat, 14 Nov 2026 17:16:44 GMT
**Tags:** java, jemalloc, jvm, heap-memory, glibc
**Source:** tag:jvm
**URL:** <https://medium.com/@aditya.barik32/our-jvm-pods-were-oom-killed-with-5-gib-of-heap-free-a44b01094dd8?source=rss------jvm-5>

## Excerpt

The heap was never the problem. More than 2 GiB per pod was sitting in the C allocator, already freed by the application and never&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
