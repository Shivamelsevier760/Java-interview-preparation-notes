---
title: "Heavy-Light Decomposition in Java"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/heavy-light-decomposition-in-java-455200c139da?source=rss-4f9731d3205------2"
published: "Sat, 13 Jun 2026 12:09:29 GMT"
source: "author:@AlexanderObregon"
tags: [data-structures, algorithms, java, software-development, programming]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Heavy-Light Decomposition in Java

**Author:** Alexander Obregon
**Published:** Sat, 13 Jun 2026 12:09:29 GMT
**Tags:** data-structures, algorithms, java, software-development, programming
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/heavy-light-decomposition-in-java-455200c139da?source=rss-4f9731d3205------2>

## Excerpt

Image Source Tree queries get expensive when every request walks from node to node across a long route. Heavy-light decomposition gives that route an array-based layout instead. The tree is rooted, each node chooses one heavy child, and those heavy chains receive nearby positions in an array. From there, one route between two nodes breaks into a small set of array ranges. With a segment tree over those positions, path sums, path maximums, and other associative queries run in O(log^2 n) time after O(n) preprocessing. You can also check out my Substack , where I post more articles like this and…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
