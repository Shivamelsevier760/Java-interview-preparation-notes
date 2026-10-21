---
title: "[백엔드] 여담 V1 성능개선 6 리프레시 토큰 교체를 Lua로 묶어 통신과 충돌 재시도 감소"
author: "Miles.lim"
url: "https://medium.com/yeodam-tech/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%97%AC%EB%8B%B4-v1-%EC%84%B1%EB%8A%A5%EA%B0%9C%EC%84%A0-6-%EB%A6%AC%ED%94%84%EB%A0%88%EC%8B%9C-%ED%86%A0%ED%81%B0-%EA%B5%90%EC%B2%B4%EB%A5%BC-lua%EB%A1%9C-%EB%AC%B6%EC%96%B4-%ED%86%B5%EC%8B%A0%EA%B3%BC-%EC%B6%A9%EB%8F%8C-%EC%9E%AC%EC%8B%9C%EB%8F%84%EB%A5%BC-%EC%A4%84%EC%98%80%EB%8B%A4-e71c4a67cb8a?source=rss------backend-5"
published: "Wed, 21 Oct 2026 01:02:53 GMT"
source: "tag:backend"
tags: [backend]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# [백엔드] 여담 V1 성능개선 6 리프레시 토큰 교체를 Lua로 묶어 통신과 충돌 재시도 감소

**Author:** Miles.lim
**Published:** Wed, 21 Oct 2026 01:02:53 GMT
**Tags:** backend
**Source:** tag:backend
**URL:** <https://medium.com/yeodam-tech/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%97%AC%EB%8B%B4-v1-%EC%84%B1%EB%8A%A5%EA%B0%9C%EC%84%A0-6-%EB%A6%AC%ED%94%84%EB%A0%88%EC%8B%9C-%ED%86%A0%ED%81%B0-%EA%B5%90%EC%B2%B4%EB%A5%BC-lua%EB%A1%9C-%EB%AC%B6%EC%96%B4-%ED%86%B5%EC%8B%A0%EA%B3%BC-%EC%B6%A9%EB%8F%8C-%EC%9E%AC%EC%8B%9C%EB%8F%84%EB%A5%BC-%EC%A4%84%EC%98%80%EB%8B%A4-e71c4a67cb8a?source=rss------backend-5>

## Excerpt

&#xb9ac;&#xd504;&#xb808;&#xc2dc; &#xd1a0;&#xd070; &#xc7ac;&#xbc1c;&#xae09;&#xc758; Redis &#xcc98;&#xb9ac; &#xbe44;&#xc6a9;&#xc744; &#xc904;&#xc774;&#xb294; &#xc791;&#xc5c5;&#xc744; &#xc9c4;&#xd589;&#xd588;&#xb2e4;. &#xac1c;&#xc120; &#xc804;&#xc5d0;&#xb294; &#xac19;&#xc740; &#xd68c;&#xc6d0;&#xc758; &#xc11c;&#xb85c; &#xb2e4;&#xb978; 10&#xac1c; &#xc138;&#xc158;&#xc73c;&#xb85c; &#xbcf4;&#xb0b8; 1,200&#xd68c; &#xc694;&#xccad; &#xc911; 35&#xd68c;&#xac00; 503&#xc73c;&#xb85c; &#xc2e4;&#xd328;&#xd588;&#xb2e4;. Redis&#xac00; &#xaebc;&#xc9c4; &#xc0c1;&#xd669;&#xc740; &#xc544;&#xb2c8;&#xc5c8;&#xb2e4;.…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
