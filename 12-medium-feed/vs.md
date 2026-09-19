---
title: "서버는 어떻게 수천개의 요청을 동시에 처리하는가: 스레드 vs 이벤트 루프"
author: "Doheon Keum"
url: "https://medium.com/@heizence6626/%EC%84%9C%EB%B2%84%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%88%98%EC%B2%9C%EA%B0%9C%EC%9D%98-%EC%9A%94%EC%B2%AD%EC%9D%84-%EB%8F%99%EC%8B%9C%EC%97%90-%EC%B2%98%EB%A6%AC%ED%95%98%EB%8A%94%EA%B0%80-%EC%8A%A4%EB%A0%88%EB%93%9C-vs-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84-09d6f6177a12?source=rss------spring_boot-5"
published: "Sat, 19 Sep 2026 06:21:01 GMT"
source: "tag:spring-boot"
tags: [nodejs, event-loop, spring-boot, concurrency, backend]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# 서버는 어떻게 수천개의 요청을 동시에 처리하는가: 스레드 vs 이벤트 루프

**Author:** Doheon Keum
**Published:** Sat, 19 Sep 2026 06:21:01 GMT
**Tags:** nodejs, event-loop, spring-boot, concurrency, backend
**Source:** tag:spring-boot
**URL:** <https://medium.com/@heizence6626/%EC%84%9C%EB%B2%84%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%88%98%EC%B2%9C%EA%B0%9C%EC%9D%98-%EC%9A%94%EC%B2%AD%EC%9D%84-%EB%8F%99%EC%8B%9C%EC%97%90-%EC%B2%98%EB%A6%AC%ED%95%98%EB%8A%94%EA%B0%80-%EC%8A%A4%EB%A0%88%EB%93%9C-vs-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84-09d6f6177a12?source=rss------spring_boot-5>

## Excerpt

&#xc810;&#xc2ec;&#xc2dc;&#xac04;, &#xc88c;&#xc11d;&#xc774; &#xb9cc; &#xac1c;&#xb098; &#xb418;&#xb294; &#xac70;&#xb300;&#xd55c; &#xc2dd;&#xb2f9;&#xc744; &#xc0c1;&#xc0c1;&#xd574; &#xbcf4;&#xc138;&#xc694;. &#xc190;&#xb2d8;&#xc774; &#xbb3c;&#xbc00;&#xb4ef; &#xbc00;&#xb824;&#xb4ed;&#xb2c8;&#xb2e4;. &#xac00;&#xc7a5; &#xb2e8;&#xc21c;&#xd55c; &#xd574;&#xbc95;&#xc740; &#x201c;&#xc190;&#xb2d8; &#xd55c; &#xba85;&#xb2f9; &#xc6e8;&#xc774;&#xd130; &#xd55c; &#xba85;&#x201d;&#xc785;&#xb2c8;&#xb2e4;. &#xd14c;&#xc774;&#xbe14;&#xb9c8;&#xb2e4; &#xc804;&#xb2f4; &#xc6e8;&#xc774;&#xd130;&#xb97c;…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
