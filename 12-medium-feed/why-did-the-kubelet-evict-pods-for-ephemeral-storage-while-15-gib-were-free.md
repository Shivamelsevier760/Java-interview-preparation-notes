---
title: "Why did the kubelet evict pods for ephemeral-storage while 15 GiB were free?"
author: "Kkhdevs"
url: "https://medium.com/@kkhdevs/why-did-the-kubelet-evict-pods-for-ephemeral-storage-while-15-gib-were-free-f0a663b9e499?source=rss------docker-5"
published: "Thu, 12 Nov 2026 00:39:06 GMT"
source: "tag:docker"
tags: [devops, docker, kubernetes, incident-management, sre]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Why did the kubelet evict pods for ephemeral-storage while 15 GiB were free?

**Author:** Kkhdevs
**Published:** Thu, 12 Nov 2026 00:39:06 GMT
**Tags:** devops, docker, kubernetes, incident-management, sre
**Source:** tag:docker
**URL:** <https://medium.com/@kkhdevs/why-did-the-kubelet-evict-pods-for-ephemeral-storage-while-15-gib-were-free-f0a663b9e499?source=rss------docker-5>

## Excerpt

Because of evictionMinimumReclaim. Once free space crosses the kubelet&apos;s 5 % threshold, eviction continues until free space is above&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
