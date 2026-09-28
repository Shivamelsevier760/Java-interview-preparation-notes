---
title: "เปลี่ยน USB Webcam ธรรมดาให้เป็นกล้อง IP ด้วย go2rtc + Docker (พร้อมวิธีกู้ระบบเมื่อไฟดับ) — Part 1"
author: "Areefan mahmud"
url: "https://medium.com/@areefan.moph/%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99-usb-webcam-%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%94%E0%B8%B2%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%87-ip-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-go2rtc-docker-%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B9%E0%B9%89%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%84%E0%B8%9F%E0%B8%94%E0%B8%B1%E0%B8%9A-part-1-8e4fd126ccdf?source=rss------docker-5"
published: "Mon, 28 Sep 2026 07:17:58 GMT"
source: "tag:docker"
tags: [webcam, home-assistant, docker]
rating:        # fill in 1–5 after you read it
read: false    # flip to true when done
notes: ""      # your one-liner takeaway
---

# เปลี่ยน USB Webcam ธรรมดาให้เป็นกล้อง IP ด้วย go2rtc + Docker (พร้อมวิธีกู้ระบบเมื่อไฟดับ) — Part 1

**Author:** Areefan mahmud
**Published:** Mon, 28 Sep 2026 07:17:58 GMT
**Tags:** webcam, home-assistant, docker
**Source:** tag:docker
**URL:** <https://medium.com/@areefan.moph/%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99-usb-webcam-%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%94%E0%B8%B2%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%87-ip-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-go2rtc-docker-%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B9%E0%B9%89%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%84%E0%B8%9F%E0%B8%94%E0%B8%B1%E0%B8%9A-part-1-8e4fd126ccdf?source=rss------docker-5>

## Excerpt

&#xe1a;&#xe31;&#xe19;&#xe17;&#xe36;&#xe01;&#xe08;&#xe32;&#xe01;&#xe1b;&#xe23;&#xe30;&#xe2a;&#xe1a;&#xe01;&#xe32;&#xe23;&#xe13;&#xe4c;&#xe08;&#xe23;&#xe34;&#xe07;: &#xe15;&#xe34;&#xe14;&#xe15;&#xe31;&#xe49;&#xe07;&#xe15;&#xe31;&#xe49;&#xe07;&#xe41;&#xe15;&#xe48;&#xe28;&#xe39;&#xe19;&#xe22;&#xe4c; &#xe41;&#xe01;&#xe49;&#xe1b;&#xe31;&#xe0d;&#xe2b;&#xe32;&#xe01;&#xe25;&#xe49;&#xe2d;&#xe07; webcam &#xe17;&#xe35;&#xe48; go2rtc &#xe44;&#xe21;&#xe48;&#xe22;&#xe2d;&#xe21;&#xe2d;&#xe48;&#xe32;&#xe19;…

## My notes

_(write your takeaways here after reading — questions this article could be asked
about in interviews, code snippets to remember, follow-up topics)_
