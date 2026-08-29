---
title: "The Dual-Write Problem: Why “Update the DB, Then Publish an Event” Is Broken"
author: "Jatin Jain Saraf"
url: "https://medium.com/@jatinjainsaraf/the-dual-write-problem-why-update-the-db-then-publish-an-event-is-broken-7ec5ca89fdfb?source=rss------system_design-5"
published: "Sat, 29 Aug 2026 03:29:04 GMT"
source: "tag:system-design"
tags: [postgresql, systems-thinking, design-systems]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# The Dual-Write Problem: Why “Update the DB, Then Publish an Event” Is Broken

**Author:** Jatin Jain Saraf
**Published:** Sat, 29 Aug 2026 03:29:04 GMT
**Tags:** postgresql, systems-thinking, design-systems
**Source:** tag:system-design
**URL:** <https://medium.com/@jatinjainsaraf/the-dual-write-problem-why-update-the-db-then-publish-an-event-is-broken-7ec5ca89fdfb?source=rss------system_design-5>

## Excerpt

An order gets saved to Postgres. The next line of code publishes an &#x201c;order created&#x201d; event to a message broker, so the payments service can&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
