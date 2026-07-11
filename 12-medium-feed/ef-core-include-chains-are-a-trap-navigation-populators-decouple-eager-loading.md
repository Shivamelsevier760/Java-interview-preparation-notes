---
title: "EF Core Include chains are a trap: navigation populators decouple eager loading"
author: "Ivan Ball-llovera"
url: "https://medium.com/@ivanball76/ef-core-include-chains-are-a-trap-navigation-populators-decouple-eager-loading-c378fa4497ac?source=rss------microservices-5"
published: "Sat, 11 Jul 2026 00:13:54 GMT"
source: "tag:microservices"
tags: [entity-framework-core, software-architecture, dotnet, csharp, microservices]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# EF Core Include chains are a trap: navigation populators decouple eager loading

**Author:** Ivan Ball-llovera
**Published:** Sat, 11 Jul 2026 00:13:54 GMT
**Tags:** entity-framework-core, software-architecture, dotnet, csharp, microservices
**Source:** tag:microservices
**URL:** <https://medium.com/@ivanball76/ef-core-include-chains-are-a-trap-navigation-populators-decouple-eager-loading-c378fa4497ac?source=rss------microservices-5>

## Excerpt

Include(x).Include(y).ThenInclude(z) couples your read model to one physical database. Here is the eager-loading boundary that batch-loads&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
