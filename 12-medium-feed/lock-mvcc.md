---
title: "동시성 제어: 락(Lock)과 MVCC 메커니즘"
author: "Doheon Keum"
url: "https://medium.com/@heizence6626/%EB%8F%99%EC%8B%9C%EC%84%B1-%EC%A0%9C%EC%96%B4-%EB%9D%BD-lock-%EA%B3%BC-mvcc-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98-b4b894715429?source=rss------concurrency-5"
published: "Sat, 25 Jul 2026 07:31:01 GMT"
source: "tag:concurrency"
tags: [concurrency, mysql, mvcc, database, backend]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# 동시성 제어: 락(Lock)과 MVCC 메커니즘

**Author:** Doheon Keum
**Published:** Sat, 25 Jul 2026 07:31:01 GMT
**Tags:** concurrency, mysql, mvcc, database, backend
**Source:** tag:concurrency
**URL:** <https://medium.com/@heizence6626/%EB%8F%99%EC%8B%9C%EC%84%B1-%EC%A0%9C%EC%96%B4-%EB%9D%BD-lock-%EA%B3%BC-mvcc-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98-b4b894715429?source=rss------concurrency-5>

## Excerpt

&#xc5ec;&#xb7ec; &#xba85;&#xc774; &#xd558;&#xb098;&#xc758; &#xbb38;&#xc11c;&#xb97c; &#xb3d9;&#xc2dc;&#xc5d0; &#xc5f4;&#xc5b4; &#xd3b8;&#xc9d1;&#xd558;&#xb294; &#xc7a5;&#xba74;&#xc744; &#xb5a0;&#xc62c;&#xb824; &#xbcf4;&#xc138;&#xc694;. &#xc608;&#xc804; &#xc0ac;&#xbb34;&#xc2e4;&#xc5d0;&#xc11c;&#xb294; &#xb204;&#xad70;&#xac00; &#xd30c;&#xc77c;&#xc744; &#xc5f4;&#xba74; &#xb2e4;&#xb978; &#xc0ac;&#xb78c;&#xc740; &#x201c;&#xc0ac;&#xc6a9; &#xc911;&#x201d;&#xc774;&#xb77c;&#xb294; &#xba54;&#xc2dc;&#xc9c0;&#xb9cc; &#xbcf4;&#xace0; &#xae30;&#xb2e4;&#xb824;&#xc57c; &#xd588;&#xc2b5;&#xb2c8;&#xb2e4;.…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
