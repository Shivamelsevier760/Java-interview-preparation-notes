# Senior Java Interview Vault

Welcome. This is your personal study site — every Java, Spring Boot, microservices, AWS, system design, and behavioral note you've ever taken, in one searchable place.

!!! tip "How to study with this site"
    1. **Daily review** — pick one topic from the left sidebar and read it cover-to-cover.
    2. **Search anything** — hit ++slash++ or ++ctrl+k++ and type. Full-text search across 311 notes.
    3. **Mobile-friendly** — bookmark this page on your phone for commute reading.
    4. **Edit on GitHub** — every page has an "Edit this page" pencil icon in the top right. Fix typos, add insights as you re-read.

## Where to start

<div class="grid cards" markdown>

- :material-language-java: **[Java Core, Concurrency, JVM](01-java/)**

    154 notes — your biggest collection. Start here. HashMap internals, ConcurrentHashMap, volatile vs synchronized, GC, memory model, streams.

- :material-spring: **[Spring Boot & Microservices](02-microservices/)**

    Microservices interview questions for 3+ years experience — autoconfig, circuit breakers, service discovery, distributed transactions.

- :material-newspaper-variant: **[Medium Series](03-medium-series/)**

    Your own curated Medium interview series (parts 1–7) plus a deep-dive collection from real company interviews.

- :material-aws: **[AWS Cloud Practitioner](05-aws-cloud-practitioner/)**

    Notes from Tutorials Dojo, Reyaz's handmade notes, cheat sheets, mock test mistakes — everything for the CLF-C02 cert.

- :material-rocket-launch: **[AWS Developer Associate](06-aws-developer-associate/)**

    DVA-C02 training content. Heaviest section by storage (lots of training-course screenshots).

- :material-account-tie: **[Behavioral & Self-Intro](08-behavioral/)**

    Three polished self-introduction variants for screening calls.

</div>

## Suggested 4-week study plan

Use the search bar to find specific topics inside each week.

**Week 1 — Java fundamentals revisit.** Collections deep dive (HashMap, ConcurrentHashMap, ArrayList vs LinkedList), generics, equals/hashCode contract, immutability. Goal: be able to explain HashMap internals in 60 seconds and ConcurrentHashMap segment locking in another 60.

**Week 2 — JVM, memory & concurrency.** Memory model and happens-before, garbage collectors (Serial, Parallel, G1, ZGC), `volatile` vs `synchronized` vs `Atomic*`, `CompletableFuture`, ExecutorService internals, thread pools. Goal: be unflappable on any thread-safety question.

**Week 3 — Spring Boot & microservices.** Autoconfiguration internals, bean lifecycle, transaction propagation, REST design, service discovery (Eureka), circuit breakers (Resilience4j), Kafka consumer groups, distributed tracing, idempotency. Goal: design a system end-to-end on a whiteboard.

**Week 4 — Cloud, DevOps & system design.** AWS core services (EC2, S3, Lambda, RDS, SQS, SNS, IAM), Docker fundamentals, Kubernetes basics, CI/CD pipelines, observability. Practice 5 system-design problems from your Medium series. Goal: confident on cloud + design rounds.

## A note on the cheatsheet

The repo also contains a `cheatsheet.md` (~75,000 lines, all Java/Microservices/Networking/Behavioral inlined). It's deliberately not on this site — too big to render as a single page. Open it from the [GitHub repo](https://github.com/Shivamelsevier760/Java-interview-preparation-notes/blob/main/cheatsheet.md) or your local clone for night-before review.

---

_Last build: see footer. Push any change to `main` and the site rebuilds automatically._
