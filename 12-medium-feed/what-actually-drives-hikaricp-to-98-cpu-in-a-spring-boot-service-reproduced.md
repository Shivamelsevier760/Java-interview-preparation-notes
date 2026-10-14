---
title: "What Actually Drives HikariCP to 98% CPU in a Spring Boot Service, Reproduced"
author: "Navya Devadiga"
url: "https://medium.com/system-design-architecture-deep-dives/what-actually-drives-hikaricp-to-98-cpu-in-a-spring-boot-service-reproduced-9f3867886e91?source=rss------java-5"
published: "Wed, 14 Oct 2026 08:48:50 GMT"
source: "tag:java"
tags: [debugging, java, spring-boot, database, performance]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# What Actually Drives HikariCP to 98% CPU in a Spring Boot Service, Reproduced

**Author:** Navya Devadiga
**Published:** Wed, 14 Oct 2026 08:48:50 GMT
**Tags:** debugging, java, spring-boot, database, performance
**Source:** tag:java
**URL:** <https://medium.com/system-design-architecture-deep-dives/what-actually-drives-hikaricp-to-98-cpu-in-a-spring-boot-service-reproduced-9f3867886e91?source=rss------java-5>

## Excerpt

Starving the pool with 400 threads used a third of a core. Creating a HikariCP pool per request used a whole core to serve 116 queries a&#x2026; Continue reading on System Design &amp; Architecture Deep Dives »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
