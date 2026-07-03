---
title: "Edmonds-Karp Max Flow in Dart"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/edmonds-karp-max-flow-in-dart-bd3be6aa9352?source=rss-4f9731d3205------2"
published: "Thu, 02 Jul 2026 22:23:31 GMT"
source: "author:@AlexanderObregon"
tags: [dart, algorithms, software-development, programming, data-structures]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Edmonds-Karp Max Flow in Dart

**Author:** Alexander Obregon
**Published:** Thu, 02 Jul 2026 22:23:31 GMT
**Tags:** dart, algorithms, software-development, programming, data-structures
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/edmonds-karp-max-flow-in-dart-bd3be6aa9352?source=rss-4f9731d3205------2>

## Excerpt

Image Source Maximum flow problems ask how much flow can move from a source node to a sink node through directed edges with capacity limits. Edmonds-Karp answers that by repeating a focused cycle. It runs BFS from the source to the sink, finds the shortest augmenting route by edge count, sends the largest amount that route can still carry, then updates the residual graph for the next pass. The residual graph is the best way to read the algorithm as it runs. Forward residual capacity means an edge can still carry more flow, while reverse residual capacity means earlier flow can be reduced and…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
