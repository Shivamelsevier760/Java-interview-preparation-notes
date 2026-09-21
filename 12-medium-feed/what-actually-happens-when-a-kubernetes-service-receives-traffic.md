---
title: "What Actually Happens When a Kubernetes Service Receives Traffic?"
author: "Tom Jose | DevOps"
url: "https://medium.com/kotaicode/what-actually-happens-when-a-kubernetes-service-receives-traffic-d3bfdef9c3d7?source=rss------kubernetes-5"
published: "Mon, 21 Sep 2026 10:01:04 GMT"
source: "tag:kubernetes"
tags: [aws, kubernetes, cloud-computing, devops, software-engineering]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# What Actually Happens When a Kubernetes Service Receives Traffic?

**Author:** Tom Jose | DevOps
**Published:** Mon, 21 Sep 2026 10:01:04 GMT
**Tags:** aws, kubernetes, cloud-computing, devops, software-engineering
**Source:** tag:kubernetes
**URL:** <https://medium.com/kotaicode/what-actually-happens-when-a-kubernetes-service-receives-traffic-d3bfdef9c3d7?source=rss------kubernetes-5>

## Excerpt

kube-proxy doesn&#x2019;t load balance. It writes iptables rules that the kernel uses to pick a Pod. There&#x2019;s a difference. Continue reading on kotaicode »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
