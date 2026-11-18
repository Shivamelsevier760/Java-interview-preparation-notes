---
title: "The Double-Booked Seat: Fixing a Booking Race Condition in Postgres"
author: "Somnath Khadanga"
url: "https://medium.com/@somnathkhadanga810/the-double-booked-seat-fixing-a-booking-race-condition-in-postgres-33aa616cf1e3?source=rss------system_design-5"
published: "Wed, 18 Nov 2026 14:07:14 GMT"
source: "tag:system-design"
tags: [concurrency, design-systems, postgresql]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# The Double-Booked Seat: Fixing a Booking Race Condition in Postgres

**Author:** Somnath Khadanga
**Published:** Wed, 18 Nov 2026 14:07:14 GMT
**Tags:** concurrency, design-systems, postgresql
**Source:** tag:system-design
**URL:** <https://medium.com/@somnathkhadanga810/the-double-booked-seat-fixing-a-booking-race-condition-in-postgres-33aa616cf1e3?source=rss------system_design-5>

## Excerpt

Scenario: two users hit Book on the last seat at the same moment. The code checks that the seat is available, charges the card, then marks&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
