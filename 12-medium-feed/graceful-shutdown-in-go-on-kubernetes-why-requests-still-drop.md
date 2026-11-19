---
title: "Graceful shutdown in Go on Kubernetes: why requests still drop"
author: "Michal Kovaľ"
url: "https://medium.com/@micqogamer/graceful-shutdown-in-go-on-kubernetes-why-requests-still-drop-fbeab8db54dd?source=rss------kubernetes-5"
published: "Thu, 19 Nov 2026 13:09:28 GMT"
source: "tag:kubernetes"
tags: [rabbitmq, kubernetes, golang, concurrency]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Graceful shutdown in Go on Kubernetes: why requests still drop

**Author:** Michal Kovaľ
**Published:** Thu, 19 Nov 2026 13:09:28 GMT
**Tags:** rabbitmq, kubernetes, golang, concurrency
**Source:** tag:kubernetes
**URL:** <https://medium.com/@micqogamer/graceful-shutdown-in-go-on-kubernetes-why-requests-still-drop-fbeab8db54dd?source=rss------kubernetes-5>

## Excerpt

You handle SIGTERM and call Shutdown, yet every rollout still produces a few 502s. The bug is usually not in your Go code. Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
