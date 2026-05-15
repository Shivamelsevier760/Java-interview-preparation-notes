---
title: "Manacher’s Algorithm for Finding Palindromes in Java Strings"
author: "Alexander Obregon"
url: "https://medium.com/@AlexanderObregon/https-alexanderobregon-substack-com-p-manachers-algorithm-for-finding-palindromes-0ea-fb199f6dc461?source=rss-4f9731d3205------2"
published: "Tue, 12 May 2026 22:36:10 GMT"
source: "author:@AlexanderObregon"
tags: [software-development, programming, java, algorithms, data-structures]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# Manacher’s Algorithm for Finding Palindromes in Java Strings

**Author:** Alexander Obregon
**Published:** Tue, 12 May 2026 22:36:10 GMT
**Tags:** software-development, programming, java, algorithms, data-structures
**Source:** author:@AlexanderObregon
**URL:** <https://medium.com/@AlexanderObregon/https-alexanderobregon-substack-com-p-manachers-algorithm-for-finding-palindromes-0ea-fb199f6dc461?source=rss-4f9731d3205------2>

## Excerpt

Image Source Palindrome search gets expensive fast when every center has to expand outward from the beginning with no memory of what was already found. Manacher’s Algorithm cuts out that repeated checking by carrying forward palindrome length data from earlier positions, so a center inside a larger confirmed match can start with information that is already available before any fresh character comparisons begin. That reuse gives the algorithm a linear-time scan while still finding the longest palindromic substring and the palindrome radius at every center. In Java, arrays and index-based…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
