---
title: "1Panel 顯示 OpenResty 異常時：從雜訊 log 找到 80/443 埠衝突的根因"
author: "krownsh"
url: "https://medium.com/@bgkong1205/1panel-%E9%A1%AF%E7%A4%BA-openresty-%E7%95%B0%E5%B8%B8%E6%99%82-%E5%BE%9E%E9%9B%9C%E8%A8%8A-log-%E6%89%BE%E5%88%B0-80-443-%E5%9F%A0%E8%A1%9D%E7%AA%81%E7%9A%84%E6%A0%B9%E5%9B%A0-92d95fb4ff75?source=rss------docker-5"
published: "Fri, 18 Sep 2026 01:29:54 GMT"
source: "tag:docker"
tags: [proxy, nginx, troubleshooting, devops, docker]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# 1Panel 顯示 OpenResty 異常時：從雜訊 log 找到 80/443 埠衝突的根因

**Author:** krownsh
**Published:** Fri, 18 Sep 2026 01:29:54 GMT
**Tags:** proxy, nginx, troubleshooting, devops, docker
**Source:** tag:docker
**URL:** <https://medium.com/@bgkong1205/1panel-%E9%A1%AF%E7%A4%BA-openresty-%E7%95%B0%E5%B8%B8%E6%99%82-%E5%BE%9E%E9%9B%9C%E8%A8%8A-log-%E6%89%BE%E5%88%B0-80-443-%E5%9F%A0%E8%A1%9D%E7%AA%81%E7%9A%84%E6%A0%B9%E5%9B%A0-92d95fb4ff75?source=rss------docker-5>

## Excerpt

&#x6309;&#x4e0b;&#x91cd;&#x555f;&#x5f8c; OpenResty &#x986f;&#x793a;&#x7570;&#x5e38;&#xff0c;&#x672a;&#x5fc5;&#x662f;&#x6700;&#x8fd1;&#x6539;&#x904e;&#x7684;&#x7db2;&#x7ad9;&#x8a2d;&#x5b9a;&#x3002;&#x9019;&#x6b21;&#x6839;&#x56e0;&#x662f;&#x4e3b;&#x6a5f;&#x7684; system Nginx &#x5df2;&#x76e3;&#x807d; :80&#xff0c;&#x800c; 1Panel &#x7ba1;&#x7406;&#x7684; OpenResty &#x5bb9;&#x5668;&#x4e5f;&#x8981;&#x767c;&#x5e03;&#x540c;&#x4e00;&#x500b; host port&#x3002;&#x5169;&#x500b; process &#x4e0d;&#x53ef;&#x80fd;&#x540c;&#x6642;&#x4f54;&#x7528;&#x540c;&#x4e00;&#x7d44;&#x2026; Continue reading on Medium »

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
