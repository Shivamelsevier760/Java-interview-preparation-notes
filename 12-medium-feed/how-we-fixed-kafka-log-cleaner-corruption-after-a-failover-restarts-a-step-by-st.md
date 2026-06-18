---
title: "How We Fixed Kafka Log Cleaner Corruption After a Failover/Restarts — A Step-by-Step Guide"
author: "N S N Murthy Kancharla"
url: "https://medium.com/@nsnmurthyk/how-we-fixed-kafka-log-cleaner-corruption-after-a-failover-restarts-a-step-by-step-guide-679495f5ea80?source=rss------kafka-5"
published: "Thu, 18 Jun 2026 03:35:57 GMT"
source: "tag:kafka"
tags: [devops, kafka, site-reliability-engineer, disaster-recovery, kafka-internal]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# How We Fixed Kafka Log Cleaner Corruption After a Failover/Restarts — A Step-by-Step Guide

**Author:** N S N Murthy Kancharla
**Published:** Thu, 18 Jun 2026 03:35:57 GMT
**Tags:** devops, kafka, site-reliability-engineer, disaster-recovery, kafka-internal
**Source:** tag:kafka
**URL:** <https://medium.com/@nsnmurthyk/how-we-fixed-kafka-log-cleaner-corruption-after-a-failover-restarts-a-step-by-step-guide-679495f5ea80?source=rss------kafka-5>

## Excerpt

After a failover/restarts, our Kafka log cleaner silently stalled on __consumer_offsets, disk kept growing, and we had no alerts. Here&apos;s&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
