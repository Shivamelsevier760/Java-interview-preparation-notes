# Java — Core, Concurrency, JVM, Collections — Interview Q&A

> Auto-extracted from the notes in [`01-java/`](../01-java/) by [`scripts/extract_qa.mjs`](../scripts/extract_qa.mjs).
> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.

**407 answered questions** · **91 question prompts without recorded answers**

---

## 1. Trap 1 — “If One Microservice Fails, Others Are Independent, Right?”

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

**Why this sounds correct (but isn’t)**

Microservices are sold as:

> “Independent services that can fail without affecting others”
> 

This is **true only at the infrastructure level**:

- Separate codebases
- Separate deployments
- Separate scaling

---

**The Real Meaning of “Independence”**

**What microservices actually give you**

Microservices reduce:

- **Deployment coupling** → You can deploy Payment without redeploying Order
- **Code coupling** → Teams can evolve APIs independently

They **do NOT** remove:

- **Runtime dependency**
- **Business coupling**
- **Failure propagation**

**Concrete Failure Walkthrough (This Is the Key)**

**Normal flow**

`Client
  ↓
Order Service
  ↓
Payment Service
  ↓
Inventory Service`

Everything works.

---

**Now Payment Service goes down**

**What developers expect**

> “Payment fails, but Order and Inventory are fine.”
> 

This is fantasy.

**What actually happens**

**1) Order Service keeps receiving traffic**

Orders keep coming in.
Order Service tries to call Payment Service.

---

**2) Payment calls start timing out**

Each Order request now:

- Opens an HTTP connection
- Waits for timeout (say 5 seconds)
- Consumes a request thread

Threads are now **blocked**, not working.

**3) Thread pool exhaustion**

Order Service has:

- Limited request threads (Tomcat / Netty / Undertow)
- Limited DB connections

As threads block:

- New requests queue
- Latency increases
- Timeouts cascade

---

**4) Retry amplification**

If retries exist (and they usually do):

`1 request → 3 retries → 3 more blocked threads`

Traffic **multiplies** during failure.

This is how **one service outage kills healthy services**.

**5) Downstream effects**

Meanwhile:

- Inventory is never updated
- Kafka topics grow (events not processed)
- Consumers rebalance
- Message replay increases
- DB pools saturate
- CPU spikes from retry logic

Now **three services look unhealthy**, even though only one failed.

---

**Why This Is Logical Coupling**

Even though:

- No shared code
- No shared database
- No shared deployment

They are still coupled by:

- **Business flow**
- **Synchronous calls**
- **Shared assumptions**

That is **logical coupling**, not technical coupling.

> “Microservices reduce deployment coupling, but runtime dependencies still exist.
When a downstream service fails, upstream services can suffer from thread exhaustion, retry storms, and cascading failures unless defensive patterns are used.”
> 

---

**Analogy**

> “Microservices are like separate ships, but they are still connected by ropes.
If one ship sinks and the ropes aren’t cut, it pulls the others down.”
> 

---

**Trap 2 — “Retries Make Systems More Reliable”**

**Why this belief exists**

Retries *do* help **transient failures**:

- Brief network hiccups
- Momentary GC pauses
- Short-lived leader elections

Because of this, people generalize:

> “If a call fails, retrying is always safer.”
> 

That assumption **kills distributed systems**.

---

**Walkthrough: How Retry Storms Actually Happen**

**Initial state (healthy system)**

- Service B can handle **1000 req/sec**
- Service A sends **1000 req/sec**
- Everything works

**Failure starts**

Service B becomes slow (not dead):

- DB is overloaded
- GC pauses increase
- Latency jumps from 50 ms → 3 seconds

This is the **most dangerous state**: slow, not down.

---

**Step 1 — Timeouts trigger retries**

Service A has:

`timeout = 2s
retries = 3`

Each request now does:

`call → timeout → retry → timeout → retry → timeout`

So **1 request becomes 3 requests**.

**Step 2 — Traffic multiplies**

`1000 original requests
→ 3000 retry requests`

But Service B is already struggling.

Now:

- CPU spikes
- Thread pools saturate
- DB connections exhaust
- Latency increases further

---

**Step 3 — Positive feedback loop (death spiral)**

This is the killer insight interviewers want.

As Service B slows down:

- More timeouts occur
- More retries fire
- Even more load is generated
- Latency worsens again

This loop feeds itself.

This is called a **self-amplifying failure**.

**Step 4 — Cascading failure**

Now it spreads:

- Service A threads block waiting
- Request queues grow
- Service A becomes slow
- Upstream services retry *Service A*
- Entire cluster degrades

One slow service takes down the system.

---

**Why Retries Are Worse Than Failures**

A **hard failure** (connection refused):

- Fails fast
- Little resource usage
- Easier to recover

A **slow failure** (timeouts + retries):

- Consumes threads
- Holds DB connections
- Burns CPU
- Spreads damage

Retries turn **slow failures into global outages**.

Retries exist to:

- Hide transient blips
- Smooth brief instability

They do **not** exist to:

- Fix broken dependencies
- Compensate for overload

**What Makes Retries Safe**

**1) Bounded retries**

Never retry indefinitely.

`Max retries = 1–3`

More retries ≠ more reliability.

---

**2) Exponential backoff**

Each retry waits longer:

`Retry 1 → 100ms
Retry 2 → 300ms
Retry 3 → 900ms`

This:

- Reduces pressure
- Gives the system time to recover

**3) Jitter (critical)**

---

## 2. What exactly is jitter?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

Normally, retries look like this:

`Retry 1 → wait 1s  
Retry 2 → wait 2s  
Retry 3 → wait 4s`

In a distributed system:

- 1,000 services fail together
- They **all retry at 1s**
- They **all retry again at 2s**
- Backend collapses again

**Jitter fixes this by adding randomness**

`Retry 1 → wait 1s ± random
Retry 2 → wait 2s ± random
Retry 3 → wait 4s ± random`

So retries are **spread over time**, not synchronized.

---

## 3. Trap 1 — Do Streams Execute Line by Line?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

Most of us imagine streams like this:

First all elements go through `filter`**J**
Then all elements go through `map`
Then all elements go through `findFirst`

That is **wrong**.

Let’s see the code again:

```java
list.stream()
.filter(x -> {
    System.out.println("filter " + x);
    return x > 2;
})
.map(x -> {
    System.out.println("map " + x);
    return x * 10;
})
.findFirst();
```

Assume the list is:

`[1, 2, 3, 4, 5]`

Now let’s walk through what really happens.

Now let’s walk through what really happens.

---

**What developers think happens**

Most people think Java runs it like this:

`filter(1)
filter(2)
filter(3)
filter(4)
filter(5)

map(3)
map(4)
map(5)

findFirst()`

This is how loops work.

But **streams do not work like loops**.

**What actually happens**

Streams work like a **conveyor belt**.

Each element goes through the whole pipeline **before the next element is touched**.

Now step by step:

**Step 1 — Take first element**

`x = 1
filter(1) → false`

So 1 is discarded.
`map` is never called.

Output:

`filter 1`

---

**Step 2 — Take second element**

`x = 2
filter(2) → false`

Discarded again.

Output:

`filter 2`

---

**Step 3 — Take third element**

`x = 3
filter(3) → true
map(3) → 30
findFirst() → FOUND`

Once `findFirst()` finds a value, the stream **stops immediately**.

Elements 4 and 5 are **never touched**.

Output:

`filter 3
map 3`

So the full output becomes:

`filter 1
filter 2
filter 3
map 3`

**Why this is an interview trap**

Because many candidates say:
“First filter runs for all elements, then map runs for all elements.”

That would be true for loops.
It is **not true for streams**.

Streams use:

- Lazy evaluation
- Short-circuiting
- Element-by-element execution

This changes:

- Performance
- Logging
- Side effects
- Debugging

---

**One-line answer**

“Streams do not run stage by stage.
They run element by element and stop as soon as the terminal operation is satisfied.”

---

## 4. What thread pool does parallelStream use?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

Parallel streams do **not** create new threads.
They use a **shared JVM pool** called the **ForkJoinPool common pool**.

This pool is also used by:

- CompletableFuture
- Some framework internals
- Other parallel streams

This pool has roughly:

`number of CPU cores`

threads.
On an 8-core machine → around 8 threads.

---

---

## 5. What happens when callRemoteService blocks?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

Each thread in the pool does this:

`send request → wait for response`

While waiting:

- The thread is not doing any CPU work
- But it is still occupied
- It cannot process other tasks

Now imagine:

- 8 threads
- 8 orders sent
- All waiting for remote service

The pool is now **fully blocked**.

Any new parallelStream or CompletableFuture now has:

- No threads available
- Work queued
- Application slows down

This is how one line of code can slow down the entire JVM.

---

## 6. Step 1 — What is user?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

`findUser()` returns:

- `Optional.of(userObject)` if a user exists
- `Optional.empty()` if no user exists

So now `user` can be:

- A box with a User inside
- Or an empty box

---

---

## 7. Step 2 — What does map do?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

`map` does **not** mean “just call a method”.

It means:

> “If a value exists inside the Optional, apply this function to it.
 If no value exists, do nothing and return empty.”
> 

So Java internally does this:

```java
If user is present:
    call getName()
    take the result
    wrap it into Optional
Else:
    return Optional.empty()
```

---

## 8. Step 3 — What if getName() returns null?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

This is the real trap.

Suppose:

`User u = new User();
u.setName(null);`

Then:

`Optional<User> user = Optional.of(u);
Optional<String> name = user.map(User::getName);`

Now `getName()` returns null.

What does Optional.map do?

It does **not** create `Optional.of(null)`.
 That is illegal.

Instead, Java silently converts it to:

`Optional.empty()`

So now:

- You had a user
- The value disappeared
- No exception was thrown
- No error was logged
- The data was silently lost

Your program continues, but with missing data.

---

## 9. “Does LocalDateTime represent a real time?”

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

Most candidates think:

“If I call `LocalDateTime.now()`, I get the current time.”

That is only half true.

You get:

> A date and time
> 
> 
> **without any time zone**
> 

It is just a clock reading.

Example:

`LocalDateTime t = LocalDateTime.now();`

This might print:

`2025-01-10 10:00`

But where?

- India?
- London?
- New York?

There is no answer, because `LocalDateTime` does not store it.

---

---

## 10. What represents real time?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

A real moment in time must include:

- Date
- Time
- Time zone or offset

That is what `Instant` or `ZonedDateTime` represent.

`LocalDateTime` represents a **wall clock**, not a point in time.

---

---

## 11. What is 0x100?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

It is just a **name** we give to a memory location so we can *talk* about it.

Think of it like:

- House number **100**
- Phone number **98765**

It is just an **identifier**.

So:

- `0x100` = “address of first User object”
- `0x200` = “address of second User object”

---

## 12. Why Lombok’s @Data can be dangerous

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

`@Data` looks convenient, but it **silently generates behavior you may NOT want**.

```java
@Data
class User {
    private int id;
    private String name;
}
```

Behind the scenes, **Project Lombok** generates **ALL of this**:

- getters
- setters
- `toString()`
- `equals()`
- `hashCode()`
- required constructor

The danger is **not Lombok itself**, but **what it chooses to include by default**.

---

---

## 13. What happened?

*Source: [`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*

- `hashCode()` was calculated using **name**
- name changed
- hashCode changed
- object is now in the **wrong bucket**

The object still exists
 But it can’t be found anymore

**Silent data corruption**.

---

---

## 14. Main Question: Can you talk me through your role in your last project, and the technical pieces you were responsible for?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Sample Answer:**

> In my last project, I worked as a backend developer on a payment processing platform for a fintech client. I was responsible for designing and implementing microservices using Java 17, Spring Boot 3.3, and PostgreSQL.
> 
> 
> My core responsibilities included developing APIs for transaction management, integrating with third-party payment gateways, and handling idempotent payment retries using **Resilience4J** with circuit breakers and retries. I also worked closely with the DevOps team to **containerize services using Docker** and deploy them via **Kubernetes**.
> 
> I actively participated in **system design discussions**, especially around improving database performance with read replicas and using **Redis for caching frequently accessed data**.
> 
> On a day-to-day basis, I followed **TDD**, wrote integration tests using **Testcontainers**, and we used **GitHub Actions** for CI/CD pipelines.
> 

---

---

## 15. Can you walk me through a specific feature or module you built — from requirement to deployment?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> One key feature I owned was implementing a real-time transaction history API. I started with gathering requirements from product, then designed the schema and REST contract.
> 
> 
> I used **Spring Data JPA** with custom queries for performance, and cached the recent transactions using Redis. We exposed it via a secured JWT-authenticated API.
> 
> I wrote both unit and integration tests, and monitored it post-deployment using **Spring Boot Actuator** and **Grafana dashboards**.
> 

---

---

## 16. Were you responsible for writing tests or CI/CD as well?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Yes, absolutely. I wrote unit tests using JUnit 5 and Mockito, and used Testcontainers to run integration tests with real Postgres instances during the build.
> 
> 
> For CI/CD, we had a GitHub Actions pipeline that ran tests, built Docker images, and deployed to our dev K8s cluster. I also added Slack notifications on build failures.
> 

---

---

## 17. Did you collaborate on the architecture or mainly work on assigned tickets?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> I was involved in both. While I implemented most of the features myself, I also participated in architecture decisions — for example, choosing between event-driven (Kafka) vs. synchronous APIs for inter-service communication, and suggesting using idempotency keys to make payment retries safe.
> 

---

---

## 18. How was the team structured and what development practices did you follow?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> We were a team of 6 backend devs, 2 QA, 1 DevOps. We followed Scrum, with 2-week sprints, daily standups, and Jira for tracking.
> 
> 
> Every PR went through **mandatory code review**, and we aimed for 80%+ coverage. We did regular **retrospectives** and **pair programming** for complex tasks.
> 
> ### 🟩 **Main Question: What have you been working on recently, and what sort of work were you carrying out?**
> 
> ### 💬 Sample Answer:
> 
> > Recently, I’ve been focused on a major feature for a real-time analytics service for a payments platform. The goal was to enable the system to process and visualize transaction data from different services in near real-time.
> > 
> > 
> > I designed the **microservices architecture** for handling incoming transactions, with **Kafka for event streaming** and **Redis** for caching real-time data. I was responsible for the **API design**, ensuring **idempotency**, and implementing **fault tolerance** using **Resilience4J**.
> > 
> > A significant part of my work was optimizing the system for high throughput — I worked with the **database team** to optimize SQL queries, and **implemented a data pipeline** for batch processing to handle high volumes of data.
> > 
> > I also handled the deployment pipeline using **Docker and Kubernetes** and set up **monitoring and alerting** for production systems using **Prometheus** and **Grafana**.
> > 
> 
> ---
> 
> ### 🟨 **Follow-Up Questions Based on Their Answer:**
> 
> ### ➤ **Were you working on bug fixes, or were you more involved with new feature development?**
> 
> > My primary focus recently has been on new feature development, especially for scaling the transaction history API and handling edge cases in the payment workflow. However, I also collaborated closely with QA on fixing performance issues related to long-running queries and ensuring the overall stability of the system.
> > 
> 
> ### ➤ **Were you mainly handling tasks assigned to you, or were you part of the planning and design process as well?**
> 
> > I was actively involved in the design phase, particularly in choosing technologies (e.g., Kafka, Redis) and defining the APIs. I also participated in architecture reviews to ensure the system could scale and handle future growth. While I did work on assigned tickets, I contributed heavily to discussions about system design and the deployment pipeline.
> > 
> 
> ### ➤ **Were you working alone or with a team? How did you manage that?**
> 
> > I was part of a cross-functional team — 6 backend developers, 2 front-end engineers, and 1 DevOps. We followed Agile Scrum, so I had ownership of features, but we also paired on difficult tasks. We did daily standups and had regular sprint retrospectives where we discussed blockers and improvements.
> > 
> 
> ---
> 
> ### 🧠 **Key Points to Highlight in Your Answer:**
> 
> 1. **Focus on Complexity**: Emphasize the **scalability** and **new feature development** aspects rather than bug fixes.
> 2. **Team Dynamics**: If you were part of the architecture design or did any planning, mention that to show you weren’t just executing tasks.
> 3. **End-to-End Ownership**: Make sure to touch on everything from design to implementation, testing, and deployment, to show full-stack or feature ownership.
> 4. **Tech Stack**: Name specific tools, frameworks, or patterns used to demonstrate your technical proficiency.

---

## 19. What steps did you take to convince your team or manager about the solution?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> I initially created a small prototype and ran performance benchmarks to show the improvement. After getting buy-in from the technical lead, I presented the solution to the broader team, addressing potential concerns around message processing order and failure handling. I made sure everyone understood how to implement the changes in their services.
>

---

## 20. What challenges did you face while implementing this?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> One of the main challenges was ensuring that the new background workers didn’t impact the overall transaction integrity, especially when it came to handling retries. I had to work with the team to integrate distributed tracing to track the flow of each transaction and ensure everything stayed idempotent.
>

---

## 21. Did you get any recognition for taking the initiative?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Yes, the solution was presented during a quarterly tech review, and I received positive feedback from both the engineering and product teams. It was recognized as an important step toward improving system reliability and scaling.
> 

---

---

## 22. How did you handle disagreements during code reviews?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> In case of disagreements, we discussed the pros and cons of the approach. For example, in one instance, a colleague suggested a more complex solution, while I advocated for a simpler one. We reached a consensus after discussing the trade-offs between maintainability and performance. We always made sure to align on the overall project goals.
>

---

## 23. Did you have regular meetings with the team to align on work?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Yes, we had daily standups where we discussed our progress, blockers, and any dependencies. Additionally, we held sprint planning and retrospectives, where we could reflect on what went well and what we could improve for the next sprint.
>

---

## 24. How did you handle the testing process?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> I made sure to write thorough unit and integration tests as part of the development process. However, I also worked with QA engineers to ensure the functionality worked well in real-world scenarios. For example, after my initial testing, the QA team would create more specific user acceptance tests to validate edge cases that we might not have considered.
> 

---

---

## 25. How were disagreements or differences in opinion handled during the architectural design?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> When there were differing opinions, we encouraged an open discussion where everyone could present their reasons for the approach they were advocating. For example, during the design of the payment service, some team members advocated for using REST APIs while others suggested gRPC for better performance. After evaluating both options, we agreed to use REST APIs because it was better suited for our needs, given the complexity of client integrations. However, we decided to use gRPC for internal services to optimize latency.
>

---

## 26. Were there any specific tools or processes that helped with decision-making during these discussions?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> We used UML diagrams to visualize and model the system’s architecture, which helped everyone understand the design decisions better. Additionally, we made use of design patterns like Event Sourcing and CQRS to ensure the architecture was scalable and maintainable. Peer reviews of our design documents were also part of the process to ensure we hadn’t overlooked any important aspects.
>

---

## 27. Did you face any challenges in implementing the architecture that was decided on?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Yes, one challenge was scaling the payment service to handle a high volume of transactions. While the initial design used traditional relational databases, we found that we had to integrate NoSQL solutions for storing transaction logs and message queues to handle high concurrency. I collaborated with the team to adjust the architecture to ensure it could handle the increased load without sacrificing data consistency or availability.
> 

---

---

## 28. How much of your day is still spent coding?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> If you’re in a leadership position, make sure to explain how much time you still spend coding and how you balance that with your other responsibilities. If you’re more focused on managing people or projects, explain how you ensure the team stays productive while balancing your leadership duties.
>

---

## 29. How do you handle work-life balance, given your responsibilities?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Show how you prioritize tasks and keep your team aligned with deadlines while maintaining a healthy work-life balance. Mention if you set clear expectations and manage workload distribution to prevent burnout.
>

---

## 30. Are there any tools or processes that make your day more efficient?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> Share any tools you use to stay organized or increase productivity, such as task management tools (like Jira or Trello), CI/CD pipelines for automation, or monitoring tools (like New Relic, Prometheus).
>

---

## 31. Do you get involved in the deployment process?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

> If you're in a senior or lead role, you might still play a role in deployments. You can explain how you work with DevOps to ensure smooth releases, or if you're more focused on architecture or mentorship, mention how you're involved in the deployment strategy and high-level decisions.
> 

---

---

## 32. Where Have I Used Immutable Objects?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

1. **In multi-threaded applications**:
    - **Example**: In a multi-threaded environment, I used immutable objects to represent shared data that would be read by multiple threads but not modified by them. For instance, an immutable `Person` object could be used to ensure thread-safety without the need for synchronization when shared between threads.
2. **In Java Collections**:
    - **Example**: I have often used immutable objects as keys in `HashMap` and `HashSet` because their state remains constant, ensuring consistent behavior in these hash-based collections. I used immutable classes to represent data that should not change after it's inserted into the collection.
3. **In functional programming**:
    - **Example**: While working with functional programming paradigms in Java, I used immutable objects to represent values that could not be changed once created. This was particularly useful when implementing things like value objects and working with streams.
4. **In financial systems**:
    - **Example**: In a financial application, I used immutable objects to represent entities like `Transaction` or `Account`, where the values of certain fields should not be altered after creation to ensure the integrity of the data.
5. **In caching**:
    - **Example**: In a caching layer, I used immutable objects for cache entries to ensure that once an object is put in the cache, its state doesn't change. This ensured the consistency of the cache across various components in the system.

---

In summary, immutable objects are a great way to enforce consistency, avoid bugs related to state changes, and improve thread safety in Java applications. They are useful in various scenarios like multi-threading, functional programming, and when designing stable data models.

Question : What is a difference between String, StringBuilder and StringBuffer?Which fits better on what situation?

---

## 33. Which One Fits Better in Which Situation?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

1. **When to Use `String`:**
    - When the string's value doesn’t change.
    - For string literals, constants, or when you don’t need to modify the string after it is created.
    - When immutability is important (e.g., hashmaps with `String` keys, string constants in Java).
    - Example: `String str = "Hello";`
2. **When to Use `StringBuilder`:**
    - When you need to build or modify strings in a single-threaded environment, especially in loops or when performing a lot of concatenation.
    - Best for performance when dealing with string concatenation in scenarios where thread safety is not a concern.
    - Example: Building an HTML document or CSV string in a loop.
3. **When to Use `StringBuffer`:**
    - When you need a mutable string in a multi-threaded environment and thread safety is a concern.
    - Suitable for cases where multiple threads are modifying the string, such as when different threads are working on parts of a string concurrently.
    - Example: Logging systems where multiple threads are concurrently appending logs.

---

---

## 34. What is the synchronized keyword in Java?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

In Java, the `synchronized` keyword is used to ensure that only one thread can access a particular block of code or method at a time, providing **mutual exclusion** and ensuring **thread safety**. When a method or block is marked as `synchronized`, the thread holds a **lock** on the object or class it is synchronized on, preventing other threads from entering the synchronized section of code until the lock is released.

---

## 35. How does the synchronized keyword affect performance?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

Yes, using the `synchronized` keyword can affect performance, and here's how:

---

## 36. How to mitigate performance issues with synchronized?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

1. **Reduce Lock Contention**: Minimize the scope of synchronized code to reduce the amount of time each thread holds the lock. Use synchronized blocks instead of synchronizing entire methods when possible.
2. **Use Fine-Grained Locks**: Instead of synchronizing on a large shared object, use multiple locks for smaller, independent sections of code. This allows multiple threads to access different parts of the code concurrently.
3. **Use `java.util.concurrent` Classes**: Java provides concurrency utilities like `ReentrantLock`, `ReadWriteLock`, `Semaphore`, and `Atomic variables` in the `java.util.concurrent` package, which provide more advanced and flexible control over thread synchronization. These can sometimes offer better performance compared to the basic `synchronized` keyword.
4. **Avoid Locking on Heavy Resources**: If possible, avoid synchronizing methods that perform I/O or network operations, as these tend to be slow operations. You can use separate locks for different resources to avoid bottlenecks.
5. **Minimize Shared Data**: Reduce the amount of shared data between threads, as synchronization is mostly required to access shared mutable state. Using immutable objects can reduce the need for synchronization.

---

---

## 37. When you to use abstract class and when interface?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Give some example where you chose to use Abstract class.

---

## 38. What is an anonymous class? and when it is useful?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Did you used anywhere in code?

---

## 39. What are the benefits of a stateless architecture?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Interviewer guidance:** Looking for: horizontal scaling mainly, no need to replicate state

**Follow-ups / notes:** Have you worked with a stateless architecture? What was good? Bad?

---

## 40. Can you go through any caching strategies you've used in the past?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Interviewer guidance:** Note: Can talk about any caching at all, memcached, local memory cache, HTTP caching, anything. They need to have awareness of the importance of caching

**Follow-ups / notes:** Where are all the places caching could be used in a simple web application serving static and dynamic content (i.e. user → web app → db) What are the important design factors when designing a cache (looking for eviction strategy, TTL, size, clustering etc) What are the pitfalls of caching? (Looking for: Staleness, high memory requirements) Benefit of caching vs app scaling. If caching goes down how do you make sure a system is still be able to cope

---

## 41. What are some principles you stick to when coding, or teaching others to code?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Interviewer guidance:** Note: Everybody is different, but people should be able to give a few good answers for what matters to them e.g. good (or no!) documentation, immutability, readability, SOLID, etc

**Follow-ups / notes:** Should be a bunch of follow up questions here

---

## 42. Tell me about a time you had a disagreement with a colleague, how did you handle it?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Looking for ability to resolve conflict & work with others

---

## 43. When was the last time you took the initiative on something?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Looking for ability to do more than simply go through assigned tickets. Especially important for senior+ levels.

---

## 44. What's the most recent thing you did that you are really proud of?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Hopefully something they did to think outside the box or go the extra mile. This is their chance to impress you

---

## 45. As Lead, what would you say is important in your interactions with a PO/BA?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** Things to follow up on • push back on requirements from a technical point of view ◦ a synergy between tech and product • Handling tech debt and working with PO to prioritise

---

## 46. Could you explain you experience working with more junior developers?

*Source: [`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*

**Follow-ups / notes:** This is a coaching question • How does lead coach devs ◦ Does he/she get involved in pair programming?

---

## 47. What Java version do you use?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> I primarily work with Java 17, which is the current LTS version. It brings performance optimizations and several useful language enhancements over Java 8 and 11.
> 

---

---

## 48. What new features were introduced in Java 17?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> Java 17 introduced several powerful features. A few highlights:
> 
> 
> 🔹 **Sealed Classes** – They let us control which classes can extend or implement a superclass. Great for modeling restricted hierarchies.<br>
> 🔹 **Pattern Matching for `instanceof`** – Cleaner and more readable `instanceof` checks.<br>
> 🔹 **Switch Enhancements** – Switch can now be used as an expression and support pattern matching (previewed in earlier versions, stable by 17).<br>
> 🔹 **Records** – For immutable data carriers, introduced in Java 16 but fully stable in Java 17.<br>
> 🔹 **Text Blocks** – Multiline strings with better formatting (introduced earlier but used often in Java 17 apps).<br>
> 🔹 **Foreign Function & Memory API (Incubator)** – For interacting with native code without JNI.
> 

> Also, Java 17 being an LTS makes it a great upgrade from 8 or 11 due to performance, GC enhancements, and security improvements.
> 

---

---

## 49. Filter Emp list where name starts with your first name using Streams

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

```jsx
import java.util.*;
import java.util.stream.*;

class Emp {
    int id;
    String name;

    Emp(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public String toString() {
        return "Emp{id=" + id + ", name='" + name + "'}";
    }
}

public class StreamFilterExample {
    public static void main(String[] args) {
        List<Emp> employees = List.of(
            new Emp(1, "Amit Sharma"),
            new Emp(2, "Ravi Kumar"),
            new Emp(3, "Amit Yadav"),
            new Emp(4, "Raj Singh")
        );

        String firstName = "Amit";

        List<Emp> filtered = employees.stream()
            .filter(e -> e.name.startsWith(firstName))
            .collect(Collectors.toList());

        filtered.forEach(System.out::println);
    }
}

```

---

## 50. Sort the list in reverse order (by name)

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Option 1: Using .sorted() with Comparator (Streams)**

```jsx
List<Emp> sortedList = employees.stream()
    .sorted(Comparator.comparing(Emp::name).reversed())
    .collect(Collectors.toList());

```

🔸 Option 2: Using `List.sort()` with Lambda (what you used)

```jsx
List<Emp> empList = new ArrayList<>(employees);
empList.sort((e1, e2) -> e2.name.compareTo(e1.name)); // reversed

```

Both are valid. If the interviewer asks follow-ups like:

> "What's happening in the lambda?"
> 

You can confidently say:

> "We're using a comparator lambda that takes two employees e1 and e2, and compares their names in descending (reverse) order using compareTo."
>

---

## 51. What map implementations do you know in Java?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Real-world answer:**

> I’ve worked with several Map implementations:
> 
> - `HashMap` – Unordered, allows one null key, not thread-safe
> - `LinkedHashMap` – Maintains insertion order
> - `TreeMap` – Sorted by natural/comparator ordering
> - `ConcurrentHashMap` – Thread-safe version for concurrent access
> - `WeakHashMap`, `IdentityHashMap`, `EnumMap` – used in specific scenarios

🔥 **Follow-up Tip**: If asked about when to use which — tie it to ordering, concurrency, or memory sensitivity (e.g., `WeakHashMap` with caches).

---

---

## 52. How does HashMap work internally?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

You nailed most of it, just needs a tidy summary:

> HashMap uses an array of buckets. When we insert a key-value pair:
> 
> - It calls `hashCode()` on the key to find the index
> - If there's a collision, it uses chaining (a linked list or a tree) to store multiple entries in that bucket
> - `equals()` is used to compare keys in the same bucket

---

---

## 53. What is chaining?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> Chaining means storing multiple key-value pairs in the same bucket using a LinkedList (pre-Java 8), or a balanced binary tree (like Red-Black Tree) if too many collisions occur (Java 8+).
> 

---

---

## 54. Follow-up: What's the time complexity of insertion with chaining?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

- **Best case** (good hashing, low collisions): `O(1)`
- **Worst case** (bad hash, all keys in one bucket):
    - LinkedList: `O(m)` where `m` is number of items in the bucket
    - Tree (Java 8+): `O(log m)`

---

---

## 55. Why was the interviewer hinting "tree"?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

Because **Java 8 introduced self-balancing Red-Black Trees** in `HashMap` to handle high-collision buckets efficiently.

**Trigger point:**

> When a bucket contains > 8 entries, and the total number of buckets is > 64, Java converts that bucket from a LinkedList to a Red-Black Tree.
> 

That improves worst-case complexity from `O(m)` to `O(log m)` for lookups and insertions.

---

---

## 56. What version of Spring Boot do you use?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> I currently work with Spring Boot 3.3, which is aligned with Spring Framework 6 and uses Jakarta EE 10 under the hood. It brings improved native support (GraalVM), better observability, and support for newer Java versions like Java 17 and 21.
> 

---

---

## 57. What is Dependency Injection in Spring Boot? What are the advantages?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> Dependency Injection (DI) is a design pattern where Spring automatically provides required dependencies (beans) to a class instead of manually instantiating them.
> 
> 
> In Spring Boot, DI is handled by the **IoC container**, and we use annotations like `@Autowired`, `@Component`, `@Service`, etc. to wire beans.
> 

**Advantages of DI:**

- ✅ **Loose Coupling** – Classes depend on interfaces, not implementations
- ✅ **Easier Testing** – Mocks can be injected easily in unit tests
- ✅ **Reusability** – Beans can be reused across services
- ✅ **Lifecycle Management** – Spring manages instantiation, destruction, and scopes
- ✅ **Memory Efficient** – Beans like singletons reduce object creation

---

---

## 58. Follow-up: What is a Singleton in Spring?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> A singleton bean is created only once per Spring container, and the same instance is reused across the app. By default, all Spring beans are singletons unless explicitly scoped differently.
> 

---

---

## 59. If a prototype bean is autowired inside a singleton, will it act like prototype?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**A (Correct):**

> No, it won’t behave like a prototype. The prototype bean will be created once at startup, when the singleton is created. After that, the same instance is reused by the singleton.
> 

This is because:

- Spring injects the prototype **only once during singleton creation**
- The prototype scope doesn’t apply dynamically unless manually handled

---

---

## 60. How to get prototype behavior inside a singleton?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

You can use:

---

## 61. What types of databases have you used?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> I’ve worked with PostgreSQL (relational), MongoDB (NoSQL/document-oriented), and SAP HANA (in-memory relational DB used often in enterprise scenarios).
> 
> 
> PostgreSQL and HANA follow SQL standards, while MongoDB uses a flexible document model and JSON-like queries.
> 

---

---

## 62. Follow-up: Is HANA SQL or NoSQL?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

> HANA is a relational (SQL-based) database, but it's designed for high-performance, in-memory processing. It also supports advanced analytics, JSON-like structures, and can handle both OLTP and OLAP workloads. So it's SQL but optimized for modern, high-speed data processing.
> 

---

---

## 63. Longest Common Prefix Among Words

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Example:**

```java

Input: ["flower", "flow", "flight"]
Output: "fl"

```

**Brute-force approach:**

- Start with the first word as a prefix
- Loop through each next word, shorten the prefix until it matches

```jsx
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
        while (!strs[i].startsWith(prefix)) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
    }
    return prefix;
}

```

✅ Time complexity: **O(m * n)** where `m = prefix length`, `n = number of words`

---

**Trie-based approach:**

- Build a Trie with all words
- Walk down from root until you hit a branch (more than 1 child) or end of word

✅ **Time complexity:** Still O(m * n) but more scalable if reused or extended

> 💡 Bonus: Interviewers love it when you say:
"I’d prefer the simple iterative approach unless prefix queries are frequent, in which case I’d use a Trie."
> 

---

---

## 64. Longest Common Substring Among Words

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Note:** This is **not prefix** — substring can appear *anywhere* in all strings.

**Brute-force idea:**

- Compare every substring of the shortest word with all others — **O(n * m^2)** — not efficient

---

**Optimal approach: Dynamic Programming (2-string version)**

```jsx
int[][] dp = new int[m+1][n+1];
int maxLen = 0, endIdx = 0;
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        if (a.charAt(i-1) == b.charAt(j-1)) {
            dp[i][j] = dp[i-1][j-1] + 1;
            if (dp[i][j] > maxLen) {
                maxLen = dp[i][j];
                endIdx = i;
            }
        }
    }
}
String result = a.substring(endIdx - maxLen, endIdx);

```

✅ Time complexity: **O(m * n)** for two strings

---

## 65. Tell me about a time you faced a challenge and what you learned from it

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Great structure (STAR):**

- **S** (Situation): Set the stage
- **T** (Task): What you had to achieve
- **A** (Action): What *you* did
- **R** (Result): Outcome + Learning

**Sample Polished Answer:**

> In one of my recent projects, we were migrating a legacy monolithic Java application to microservices. Midway, we ran into issues with data consistency between services, especially with eventual consistency patterns like outbox and sagas.
> 
> 
> My task was to debug intermittent transaction failures that weren’t easily reproducible.
> 
> I worked with our team to implement **distributed tracing using Spring Sleuth + Zipkin**, and added temporary logs with correlation IDs to identify where requests were failing. After pinpointing a race condition in our retry mechanism, I introduced **idempotency keys** in our payment API and adjusted retry logic using **Resilience4j**.
> 
> This experience taught me that **observability and logging** in distributed systems are just as important as writing clean code. It also made me appreciate proactive design patterns that prevent downstream chaos.
> 

👉 **Learning**: Deepened understanding of fault tolerance and observability.

---

---

## 66. This job can be very monotonous. How do you deal with it?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

This is a test for **self-motivation** and **mental resilience**. STAR works well again.

**Sample Polished Answer:**

> In one of my previous projects, I was maintaining a legacy Spring Boot system with repetitive tasks like debugging similar null-pointer exceptions or updating outdated dependencies.
> 
> 
> Instead of getting stuck in the monotony, I created **internal tooling scripts and documentation** to automate repetitive steps — like generating debug reports or smoke tests. I also scheduled **weekly self-learning hours** to explore topics like **Vert.x and reactive streams**, which made me better prepared for modern systems.
> 
> What I’ve learned is that monotony often reveals patterns, and automating those patterns or using that time to skill up can make a routine job feel more **impactful and future-focused**.
> 

👉 **Key takeaway**: I thrive in repetitive work by automating, upskilling, and keeping a long-term perspective.

---

## 67. How do you stay up to date and relevant in the field?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Sample Answer:**

> I make it a habit to allocate 30–60 minutes a few times a week to stay current. I follow sources like:
> 
> - **Java Champion blogs**, Baeldung, DZone, and InfoQ for backend trends
> - GitHub projects, changelogs (like Java 21 or Spring Boot 3.x), and newsletters like Java Weekly
> - I also explore **system design discussions** on platforms like Reddit or LinkedIn
> 
> I recently completed hands-on work with **Reactive programming and Vert.x** after reading about high-concurrency models. And I use what I learn — for example, implementing **Resilience4J circuit breakers** after studying Netflix OSS patterns.
> 
> Conferences like **Devoxx or SpringOne** (even just watching talks) also help me stay in sync with what’s next.
> 

👉 Emphasize: You don’t just “read,” you **apply** new learnings in your real work.

---

---

## 68. What do you think about GenAI?

*Source: [`01-java/leetcode/leetcode-java-interview-questions.md`](../01-java/leetcode/leetcode-java-interview-questions.md)*

**Sample Answer:**

> I think GenAI is transforming the way we build software — not just by writing code, but by helping us reason through complex systems, generate test cases, design APIs, or even document legacy code.
> 
> 
> Tools like GitHub Copilot are already improving developer productivity, and I’ve used ChatGPT myself to experiment with quick prototyping and alternate solutions during debugging or interviews.
> 
> That said, I believe GenAI is a **co-pilot, not a replacement**. It enhances our creativity and efficiency but still relies on the developer’s judgment for correctness, security, and performance — especially in fintech or sensitive domains where precision is key.
> 
> I’m excited about its future, particularly in **automating repetitive tasks**, **generating tests**, and **exploring system design alternatives quickly**.
> 

👉 Bonus points: You’re **tech-positive**, but also responsible and grounded.

---

## 69. How to Really Convert PDF to PNG?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

You can use:

- **Apache PDFBox** to render pages to image
- **iText + Java2D**
- Or **Ghostscript (external tool)**

1. What is the Singleton design pattern?

The **Singleton Design Pattern** is one of the **creational patterns** that ensures a **class has only one instance** and provides a **global point of access** to that instance.

---

## 70. So — How Is Bill Pugh Singleton Thread-Safe Even with a 20-Thread Pool?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Let’s say you have a fixed thread pool of 20 threads — and all 20 threads **simultaneously** call:

```java
Singleton instance = Singleton.getInstance();

```

**What Actually Happens Behind the Scenes:**

1. **Class Not Yet Loaded**
    
    When the application starts, the `SingletonHelper` class (the static inner class) **has not been loaded** yet.
    
2. **Multiple Threads Call `getInstance()`**
    
    The first time `getInstance()` is called by any of the threads, they all try to **access `SingletonHelper.INSTANCE`**.
    
3. **JVM Classloading Comes Into Play**
    
    The Java **ClassLoader** ensures that the static inner class `SingletonHelper` is **loaded exactly once**, **even if accessed by multiple threads concurrently**.
    
    - Class loading is **synchronized internally by the JVM**.
    - **Only one thread loads the class**, and other threads **wait** until it’s fully loaded.
    - This makes it **thread-safe without explicit synchronization**.
4. **Once Loaded, Instance is Shared**
    
    After the class is loaded, `INSTANCE` is initialized once and cached. Any further calls to `getInstance()` from any thread simply return the already-initialized instance — no locks, no waiting.

---

## 71. What is the difference between == and .equals()?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

`==` checks reference equality; `.equals()` checks object content.

---

## 72. What is a constructor in Java?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

A special method used to initialize objects. It has the same name as the class and no return type.

---

## 73. What is the difference between ArrayList and LinkedList?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

- `ArrayList`: Fast random access, slow insert/delete.
- `LinkedList`: Slow access, fast insert/delete.

---

## 74. What is the purpose of final keyword?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

- Final variable: Constant.
- Final method: Can't be overridden.
- Final class: Can't be inherited.

---

## 75. What is the difference between HashMap and ConcurrentHashMap?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

- `HashMap`: Not thread-safe.
- `ConcurrentHashMap`: Thread-safe with better concurrency.

---

---

## 76. What are the four pillars of OOP?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Encapsulation, Inheritance, Polymorphism, Abstraction.

---

## 77. What is encapsulation?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Wrapping data and code into a single unit (class), often with private fields and public getters/setters.

---

## 78. What is polymorphism?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

One interface, many implementations. Achieved via method overloading and overriding.

---

---

## 79. Difference between synchronized and ReentrantLock?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Both ensure thread safety. `ReentrantLock` gives more control (tryLock, fair lock), but needs manual unlock.

---

## 80. What is a thread-safe class?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

A class that works correctly when accessed by multiple threads concurrently (e.g., `Vector`, `ConcurrentHashMap`).

---

---

## 81. What is Spring Boot?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

A framework for building standalone Spring apps with embedded server and minimal config.

---

## 82. How do you create a REST API in Spring Boot?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Use `@RestController`, `@GetMapping`, `@PostMapping`, etc., with a service layer for logic.

---

## 83. What is Dependency Injection?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Design pattern where objects are injected via constructor/setter to reduce tight coupling.

---

---

## 84. What is the difference between JPA and Hibernate?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

- JPA: Specification.
- Hibernate: Implementation of JPA.

---

## 85. How do you handle transactions in Spring?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Use `@Transactional` annotation.

---

## 86. How do you handle Java 8 to Java 11 migration in a project?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

I ensured compatibility by updating the `JDK`, resolving removed APIs, and leveraging new features gradually. Focused on:

- Replacing deprecated APIs (e.g., `javax.xml.bind` removed in Java 11).
- Updating `build tools` (e.g., Maven/Gradle to support Java 11).
- Testing all modules with Java 11 for runtime and compilation issues.
- Modularizing code if needed using `module-info.java`.

---

## 87. What is a functional interface?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

A **functional interface** has only **one abstract method** and can be used with **lambda expressions**.

Java provides several built-in ones in `java.util.function` package:

- **`Predicate<T>`** – returns boolean
    
    Example: `x -> x > 10`
    
- **`Function<T, R>`** – transforms input to output
    
    Example: `x -> x.toString()`
    
- **`Consumer<T>`** – performs action, no return
    
    Example: `x -> System.out.println(x)`
    
- **`Supplier<T>`** – provides a value
    
    Example: `() -> "EY"`
    

You can also define custom functional interfaces using `@FunctionalInterface`.

---

## 88. Why do we use functional interfaces in Java 8?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Functional interfaces enable **lambda expressions** and **clean functional programming**. They help write **shorter, more readable, and reusable** code — especially for tasks like filtering, mapping, and iterating over collections.

**Use Case in My Project:**

I used `Predicate` in stream filters to validate consultant attributes, and `Consumer` for processing approval steps in a pipeline.

---

## 89. What is Optional and why do we use it?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

`Optional` is a container that may or may not hold a non-null value.

It helps **avoid `NullPointerException`** by forcing explicit checks.

**Example:**

```java
Optional<String> name = Optional.ofNullable(input);
name.ifPresent(System.out::println);

```

**Use in Project:**

I used `Optional` to safely handle API response fields before processing approval logic.

---

## 90. How does Optional help avoid NPE?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Instead of checking for `null` manually, wrap the value in `Optional` and use safe methods like `isPresent()`, `ifPresent()`, `orElse()`.

---

**Example Without Optional (prone to NPE):**

```java
String name = user.getName(); // may throw NPE if user is null

```

**With Optional (safe):**

```java
Optional<String> name = Optional.ofNullable(user.getName());
name.ifPresent(n -> System.out.println(n)); // prints if value is present

```

Or:

```java
String result = Optional.ofNullable(user.getName())
                        .orElse("Default Name");

```

---

This way, your code is **null-safe and cleaner**. Want to see a use case from your approval flow project?

---

## 91. How do Java 8 Streams improve performance?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Streams improve performance by using:

1. **Lazy evaluation** – Operations are only executed when needed.
2. **Pipelining** – Multiple operations (like `filter → map → collect`) are fused into one pass.
3. **Parallel streams** – Use multiple threads for faster processing on large data.

---

**Example:**

```java
list.parallelStream()
    .filter(x -> x > 10)
    .map(x -> x * 2)
    .collect(Collectors.toList());

```

**Use in Project:**

I used streams to filter and transform consultant data efficiently before sending it for approval.

string str=

{"one_two","one_two_three","two","two_three"}

WAP to count the occurence in java tell me the approcah as first along with code

---

## 92. How did you use OOPs concepts in your project?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

1. **Encapsulation** – Used private fields and public getters/setters in approval request and user data models to protect internal state.
2. **Inheritance** – Common logic for approval flows (like logging, audit, validations) was inherited by specific pattern classes (Pattern 2, 3, 4).
3. **Polymorphism** – Overrode approval methods based on pattern type (e.g., `advanceApproval()` for Pattern 2, 3, and 4 differed).
4. **Abstraction** – Defined interfaces for notification and approval logic, so different implementations (email, UI triggers) could plug in easily.

---

## 93. Can we override non-abstract methods in Java?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

✅ Yes, we **can override non-abstract methods**, as long as they are **not `final`, `private`, or `static`**.

---

**Example:**

```java
class Parent {
    void show() {
        System.out.println("Parent show");
    }
}

class Child extends Parent {
    @Override
    void show() {
        System.out.println("Child show");
    }
}

```

**But we cannot override:**

- `final` methods → compile-time error
- `private` methods → not inherited
- `static` methods → method hiding, not true overriding

Let me know if you want to see a real use of this from your approval project.

---

## 94. If we override a method, can we change its return type?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

✅ Yes, but only to a **covariant return type** — meaning the return type can be a **subclass** of the original method’s return type.

---

**Example:**

```java
class Parent {
    Number getValue() { return 10; }
}

class Child extends Parent {
    @Override
    Integer getValue() { return 20; } // valid: Integer is a subclass of Number
}

```

---

🔸 **Not allowed:**

You **cannot change** the return type to an **unrelated type** — that will cause a compile-time error.

---

## 95. Why does an abstract class have a constructor if it can’t be instantiated?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

An abstract class **can't be instantiated**, but its **constructor runs** when a **subclass object is created**.

It's used to **initialize common fields** or **set up resources** needed by all subclasses.

---

---

## 96. What Does "Visibility" in volatile Mean?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

**Visibility** means:

When one thread **modifies** a variable, **other threads immediately see the updated value** — without needing synchronization.

---

---

## 97. Why This Happens?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

Because Java threads may **cache variables locally** (in CPU cache or registers).

`volatile` tells the JVM:

> “Always read/write the latest value from main memory.”
> 

---

---

## 98. Why volatile?

*Source: [`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*

- Ensures that when one thread updates `isRunning`,
    
    all other threads see the **latest value immediately**.
    
- Prevents stale reads due to thread-local caching.

---

Let me know if you want to pair this with `synchronized` or `AtomicBoolean` for full control.

---

## 99. What is a Maven build?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A Maven build is the process where **Maven compiles code, runs tests, packages the application, and manages dependencies** using `pom.xml`.

It ensures **consistent builds across environments**.

---

---

## 100. What does mvn clean install do?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `clean` → deletes the `target` folder
- `install` → compiles code, runs tests, packages the app, and installs the artifact into **local Maven repository**

👉 Used before deploying or sharing artifacts.

---

---

## 101. How do you push code to production?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Typical real-time flow:

1. Commit code → Git
2. Create PR → Code review
3. CI pipeline runs (build + tests)
4. Artifact created (JAR/WAR/Docker image)
5. Deployed via **Jenkins / GitHub Actions / Azure DevOps**
6. Production deployment (Blue-Green / Rolling)
7. Smoke tests + monitoring

---

---

## 102. What is code coverage?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Code coverage measures **how much of the code is executed by tests**.

Example tools: **JaCoCo, SonarQube**

---

---

## 103. What is line coverage?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Line coverage shows **percentage of code lines executed** during tests.

---

---

## 104. How do you improve code coverage when build fails?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Add missing unit tests
- Cover edge cases & exception paths
- Mock external dependencies
- Refactor complex methods
- Exclude non-testable code (DTOs, configs)

---

---

## 105. How do you verify a method is called twice in Mockito?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```java
verify(service, times(2)).process();

```

---

---

## 106. In which situations do you use PowerMock?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Used when mocking:

- `static` methods
- `final` classes/methods
- private methods
- constructors

⚠️ Used only for **legacy code** (avoid in new code).

---

---

## 107. Difference between final keyword and final variable?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `final variable` → value cannot change
- `final method` → cannot be overridden
- `final class` → cannot be inherited

---

---

## 108. What is Garbage Collection in Java?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Automatic process where JVM **reclaims unused memory** by removing unreachable objects.

---

---

## 109. How do you ensure Garbage Collection is working correctly?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Enable GC logs
- Monitor heap usage
- Use tools like **VisualVM / JConsole**
- No frequent Full GCs
- Stable memory after GC

---

---

## 110. How do you debug and fix OutOfMemoryError?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Steps:

1. Analyze heap dump
2. Identify memory leaks
3. Check large collections
4. Tune JVM heap size
5. Fix object retention issues

---

---

## 111. What are atomic variables in Java?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Thread-safe variables that perform **lock-free operations**

Example: `AtomicInteger`, `AtomicLong`

---

---

## 112. What is the volatile keyword?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Ensures **visibility of variable changes** across threads.

Does NOT provide atomicity.

---

---

## 113. Difference between volatile and synchronized?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

| volatile | synchronized |
| --- | --- |
| Visibility only | Visibility + atomicity |
| No locking | Uses lock |
| Faster | Slower |

---

---

## 114. How do you avoid performance issues caused by synchronization?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Use atomic classes
- Reduce synchronized scope
- Use concurrent collections
- Prefer lock-free algorithms

---

---

## 115. What is a BlockingQueue?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A thread-safe queue where:

- Producer waits if full
- Consumer waits if empty

---

---

## 116. Where do you use BlockingQueue in real applications?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Producer-consumer systems
- Thread pools
- Message processing
- Background job queues

---

---

## 117. Difference between HashMap and Hashtable?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

| HashMap | Hashtable |
| --- | --- |
| Not synchronized | Synchronized |
| Allows null | No null |
| Faster | Slower |

---

---

## 118. Why does Hashtable not allow null?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

To avoid ambiguity between **null key/value** and **method return value** in synchronized access.

---

---

## 119. What is load factor in HashMap?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Load factor decides **when resizing happens**.

---

---

## 120. What does default load factor 0.75 mean?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

When map is **75% full**, it resizes to maintain performance.

---

---

## 121. Difference between UNION and UNION ALL?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `UNION` → removes duplicates
- `UNION ALL` → keeps duplicates (faster)

---

---

## 122. Difference between LEFT JOIN and RIGHT JOIN?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- LEFT JOIN → all rows from left table
- RIGHT JOIN → all rows from right table

---

---

## 123. When do you use LEFT JOIN?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

When you want **all records from primary table**, even if no match exists.

---

---

## 124. How do you find records without relationship?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```sql
SELECT a.*
FROM tableA a
LEFT JOIN tableB b ON a.id = b.id
WHERE b.id IS NULL;

```

---

---

## 125. How do you handle NULL values in SQL?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `COALESCE()`
- `NVL()` (Oracle)
- `CASE WHEN`

---

---

## 126. How do you map values like A → Apple?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```sql
CASE code
  WHEN 'A' THEN 'Apple'
  WHEN 'B' THEN 'Banana'
END

```

---

---

## 127. How do you define relationships in Hibernate?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Using annotations:

- `@OneToOne`
- `@OneToMany`
- `@ManyToOne`
- `@ManyToMany`

---

---

## 128. How do you remove duplicates in SQL?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```sql
SELECT DISTINCT column FROM table;

```

or using `ROW_NUMBER()`.

---

---

## 129. Types of relationships in Hibernate?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- One-to-One
- One-to-Many
- Many-to-One
- Many-to-Many

---

---

## 130. Constructor vs Setter Injection?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

| Constructor | Setter |
| --- | --- |
| Mandatory dependencies | Optional dependencies |
| Immutable | Mutable |
| Preferred | Less preferred |

---

---

## 131. What happens if you don’t use @Autowired?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Spring won’t inject dependencies → **NullPointerException** (unless using constructor injection).

---

---

## 132. Constructor injection without @Autowired?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

If only **one constructor exists**, Spring auto-injects it.

---

---

## 133. Java 7 → Java 8 migration changes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Lambda expressions
- Streams API
- Functional interfaces
- Default methods
- Date/Time API

---

---

## 134. Ways to ensure thread safety?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- synchronized
- Locks
- Atomic variables
- Immutable objects
- ThreadLocal
- Concurrent collections

---

---

## 135. What is ThreadLocal?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Stores **thread-specific data**.

Used in:

- User sessions
- Transaction context
- Security context

---

---

## 136. Longest substring without repeating characters (Java logic)?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Use **sliding window + HashSet / Map**

Time complexity: **O(n)**

---

---

---

## 137. What is Object-Oriented Programming (OOPS)?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

OOPS is a programming paradigm that organizes software using **objects** that represent real-world entities and focus on **data + behavior together**.

---

---

## 138. What is a class in Java?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A class is a **blueprint** that defines variables (data) and methods (behavior).

---

---

## 139. What is an object in Java?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

An object is a **runtime instance of a class**.

---

---

## 140. Difference between class and object

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- **Class** → blueprint
- **Object** → real instance created from class

---

---

## 141. How do you achieve encapsulation in Java?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Make variables `private`
- Provide access using `public getters/setters`

---

---

## 142. What is abstraction?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Hiding implementation details and showing **only essential behavior**.

---

---

## 143. What is inheritance?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

One class **acquires properties and methods** of another class.

---

---

## 144. What is method overloading?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Same method name, **different parameters**, same class.

---

---

## 145. What is method overriding?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Subclass provides **specific implementation** of parent method.

---

---

## 146. Can we override static methods?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

❌ No. Static methods belong to class, not object.

---

---

## 147. What is dynamic method dispatch?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Method call is resolved **at runtime** based on object type.

---

---

## 148. What is the final keyword in OOPS?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `final variable` → constant
- `final method` → cannot override
- `final class` → cannot extend

---

---

## 149. What is constructor?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A special method used to **initialize objects**.

---

---

## 150. What is constructor overloading?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Multiple constructors with **different parameters** in same class.

---

---

## 151. Can a constructor be private?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

✅ Yes — used in **Singleton design pattern**.

---

---

## 152. What is an interface?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A contract that defines **what a class must do**, not how.

---

---

## 153. Can interface have methods with body?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

✅ Yes (Java 8+): `default` and `static` methods.

---

---

## 154. What is association?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Relationship where objects **use each other**.

---

---

## 155. What is IS-A relationship?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Inheritance relationship

Example: Dog IS-A Animal

---

---

## 156. What is HAS-A relationship?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Association relationship

Example: Car HAS-A Engine

---

---

## 157. What is tight coupling?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Classes are **highly dependent** on each other.

---

---

## 158. What is loose coupling?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Classes depend on **abstractions**, not implementations.

---

---

## 159. What is object cloning?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Creating an **exact copy** of an object using `clone()`.

---

---

## 160. Why Java doesn’t support multiple inheritance with classes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

To avoid **Diamond Problem** and ambiguity.

---

---

## 161. What is instanceof keyword?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Checks whether an object belongs to a specific class/interface.

---

---

## 162. What is garbage collection in OOPS?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Automatic memory cleanup of **unused objects** by JVM.

---

---

## 163. Can we override private methods?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

❌ No. Private methods are not visible to subclasses.

---

---

## 164. What is covariant return type?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Overridden method can return **child class object**.

---

---

## 165. What is a design pattern?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Reusable solution to **common software design problems**.

---

---

## 166. What is singleton class?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A class that allows **only one object**.

---

---

## 167. How to create immutable class?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Make class `final`
- Fields `private final`
- No setters
- Initialize via constructor

---

---

## 168. Why OOPS is important?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Code reusability
- Maintainability
- Scalability
- Real-world modeling

---

---

---

## 169. Why does a Java app behave differently in prod vs local?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Because prod differs in **data volume, concurrency, JVM flags, GC, CPU, memory limits, network latency, and external dependencies**.

Most “prod-only bugs” are **timing, GC, or resource contention issues**.

---

---

## 170. How does JVM decide object allocation and promotion?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Objects allocated in **Eden**
- Survive GC → move to **Survivor**
- Survive multiple cycles → promoted to **Old Gen**
    
    Promotion depends on **age, size, and survivor space pressure**.
    

---

---

## 171. What happens during a Stop-The-World GC pause?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- All application threads are **paused**
- JVM identifies live objects
- Reclaims or moves memory
- Threads resume
    
    STW affects **latency**, not correctness.
    

---

---

## 172. Why is volatile not sufficient for thread safety?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

`volatile` guarantees **visibility**, not **atomicity**.

Compound operations (read-modify-write) can still race.

---

---

## 173. When does synchronized become a scalability problem?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

When:

- High contention
- Long critical sections
- Many threads competing
    
    Threads block → **context switching overhead** increases.
    

---

---

## 174. How can HashMap break in multithreaded environments?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Concurrent resize can cause:

- **Infinite loops**
- Data corruption
    
    Because HashMap is **not thread-safe**.
    

---

---

## 175. How does Java Memory Model guarantee visibility?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Through:

- `volatile`
- `synchronized`
- `final` fields
- Happens-before rules
    
    These enforce **memory barriers**.
    

---

---

## 176. What is false sharing?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Multiple threads modify **different variables** that share the **same CPU cache line**, causing cache invalidation.

Avoid using:

- Padding
- `@Contended`
- Proper data layout

---

---

## 177. Why does double-checked locking fail without volatile?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Because of **instruction reordering**:

- Reference assigned before object fully constructed
- Another thread sees a partially initialized object

---

---

## 178. How does JVM detect and report deadlocks?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

JVM tracks lock ownership.

Detected deadlocks are reported via:

- `jstack`
- JVM thread dumps

---

---

## 179. Why can thread pools silently degrade performance?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Because:

- Queues grow
- Threads are blocked
- Tasks pile up
    
    System looks “healthy” but **latency explodes**.
    

---

---

## 180. What happens if a task throws exception in ExecutorService?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Exception is swallowed
- Thread stays alive
- Failure visible only via `Future.get()` or logs

---

---

## 181. How do you safely shut down a thread pool?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```java
shutdown();
awaitTermination();
shutdownNow(); // if needed

```

Always handle **interrupts properly**.

---

---

## 182. Why does GC tuning improve latency but hurt throughput?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Frequent GC → shorter pauses → **more CPU spent on GC**

Trade-off:

- Low latency
- Lower overall work done

---

---

## 183. How does G1 GC choose regions?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

G1 selects regions with **highest garbage-to-cost ratio** to meet **pause-time goals**.

---

---

## 184. Why can OOM occur even with free heap?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Fragmentation
- Metaspace exhaustion
- Direct memory leaks
- Native memory limits

---

---

## 185. How do you find memory leaks in a live JVM?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Heap dump
- Analyze object retention
- Look for **growing references**
    
    Tools: VisualVM, MAT, JProfiler
    

---

---

## 186. Why is finalize() dangerous?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Unpredictable
- Delays GC
- Can resurrect objects
    
    Deprecated due to **non-determinism**.
    

---

---

## 187. How does class loading work in large apps?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Bootstrap → Platform → Application
- Custom classloaders per module
    
    Can cause **class visibility issues**.
    

---

---

## 188. Why does ClassCastException occur in modular systems?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Same class loaded by **different classloaders** → JVM treats them as different types.

---

---

## 189. How does Java handle instruction reordering?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

JVM and CPU reorder instructions for performance, but **JMM rules prevent illegal reordering** across synchronization boundaries.

---

---

## 190. When does autoboxing hurt performance?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

In:

- Tight loops
- Collections
- High-frequency arithmetic
    
    Creates excessive temporary objects.
    

---

---

## 191. Why is String immutable and how does it help concurrency?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Thread-safe by design
- Safe caching
- Enables string pool
- Prevents data races

---

---

## 192. How does JVM optimize hot code paths?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- JIT compilation
- Method inlining
- Loop unrolling
- Escape analysis

---

---

## 193. What is escape analysis?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Determines if object:

- Escapes method/thread
    
    If not → allocate on **stack** or eliminate object.
    

---

---

## 194. Why doesn’t JVM exit after main() finishes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Because:

- Non-daemon threads still running
- Thread pools
- GC / background threads

---

---

## 195. How do you debug high CPU with low traffic?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Thread dumps
- Look for spin loops
- Lock contention
- GC thrashing
- Misconfigured thread pools

---

---

## 196. What Java design decision caused a real production issue?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

**Mixing transactions with external calls** → partial failures & data inconsistency.

Fix was **design change**, not code change.

---

###

---

## 197. What Interviewers Look For (5+ Years)

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Not memorized JVM flags, but **your approach**:

- How do you identify a bottleneck?
- How do you distinguish CPU vs IO issues?
- How do you detect memory leaks?
- How does GC affect latency?
- What tools have you used in production?

👉 They test **thinking, not syntax**.

---

---

## 198. How do you prevent double booking?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Atomic state transition in Redis
- Unique constraint in DB as final guard

---

---

## 199. What if payment fails?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Release Redis hold or let TTL expire
- No DB write without payment success

---

---

## 200. What if Redis goes down?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- **Correctness > Availability**
- Fail fast or fall back to throttled DB mode
- Rebuild Redis state from DB

---

---

## 201. How do you ensure idempotency?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Every request has an `idempotency_key`
- Store `key → result`
- Repeated requests return the same result (no double charge)

---

---

## 202. What is the Input?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `List`, `Set`, `Map`, `Array`
- `String`
- `Integer`, custom objects

---

## 203. What is the Output?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `List`, `Set`, `Map`
- `Optional<T>`
- Single value (`int`, `long`, `double`, `String`)

---

## 204. What operation is needed?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- **Filter** → remove elements
- **Transform** → change data
- **Group** → categorize
- **Aggregate** → count / sum / max / min

👉 If you identify input + output correctly, **half the problem is solved**.

---

---

## 205. How do you identify and fix memory leaks?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

**Identify**

- Heap dumps (VisualVM, MAT)
- Growing object counts
- Long-lived references

**Common Causes**

- Static references
- Unremoved listeners
- ThreadLocal misuse
- Caches without eviction

**Fix**

- Clear references
- Use weak references
- Proper lifecycle cleanup

---

---

## 206. When should virtual threads NOT be used?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- CPU-bound workloads
- Long `synchronized` blocks
- Native blocking calls (thread pinning)

---

---

## 207. How does Garbage Collection impact performance?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Impacts **latency (pause time)** and **throughput**
- Tuned via:
    - Heap sizing
    - GC selection (G1, ZGC)
    - Reducing object allocation

👉 Many prod issues blamed on code are actually **GC issues**.

---

---

## 208. How Spring manages transactions

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Uses **AOP proxies**
- `@Transactional`:
    - Opens transaction before method
    - Commits or rolls back after execution
- Rollback depends on exception type and boundary

---

---

## 209. What makes a senior Java engineer stand out?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Explains **trade-offs**, not just answers
- Understands JVM internals
- Designs for **scale & failure**
- Writes clean, testable, maintainable code

---

Below is a **complete, interview-ready answer pack** for **Java 8, Collections, Spring Boot, JPA, and REST**, written the way **senior interviewers expect you to explain**.

Clear, practical, and example-driven.

---

---

## 210. What if @FunctionalInterface is not used?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Code still works
- Annotation is **optional**
- But compiler won’t warn you if multiple abstract methods are added accidentally

👉 Best practice: **always use it**

---

---

## 211. What is Optional?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A container that represents **presence or absence of a value**.

**Common Methods**

- `isPresent()`
- `orElse()`
- `orElseGet()`
- `orElseThrow()`
- `ifPresent()`

**Where to use**

- Return types
- Stream results

❌ Avoid in fields & method parameters

---

---

## 212. What is @PatchMapping?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Used for **partial updates**.

Example:

```java
PATCH /users/1 { "email": "new@mail.com" }

```

---

---

## 213. What is Many-to-One mapping?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Many entities refer to **one parent entity**.

Example:

Many employees → One department

---

---

## 214. Why prefer Streams over loops?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Declarative style
- Less boilerplate
- Easy parallelization
- Better readability

---

---

## 215. When should we avoid Optional?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Entity fields
- Method parameters
- Serialization models

---

---

## 216. How Java 8 improves readability & performance?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Lambdas reduce boilerplate
- Streams express intent clearly
- Parallel streams improve I/O scalability
- Optional reduces null checks

---

##

---

## 217. How Spring manages transactions internally

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Uses **AOP proxies**
- `@Transactional`:
    - Opens transaction before method
    - Commits on success
    - Rolls back based on exception rules and boundaries

---

---

## 218. What are virtual threads in Java 21 and when should they be preferred?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Virtual threads are **lightweight JVM-managed threads** designed for massive concurrency.

✅ Prefer for **I/O-bound workloads** (DB calls, REST calls).

❌ Avoid for CPU-bound tasks or long `synchronized` blocks.

---

---

## 219. What are records and their limitations?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Records are **immutable data carriers** with auto-generated constructor, equals, hashCode.

**Limitations**:

- Fields are final
- Cannot extend other classes
- Not suitable for mutable entities

---

---

## 220. What is JPA and how is it different from Hibernate?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- **JPA** → A **specification** (rules & APIs for ORM)
- **Hibernate** → An **implementation** of JPA (plus extra features)

👉 JPA defines *what*, Hibernate defines *how*.

---

---

## 221. What is an Entity?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

An entity is a **persistent Java object** mapped to a database table.

**Requirements:**

- Annotated with `@Entity`
- Must have a primary key (`@Id`)
- Must have a no-args constructor
- Must not be final

---

---

## 222. What is persistence.xml? Is it required in Spring Boot?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Defines persistence unit, DB config
- ❌ **Not required in Spring Boot**
- Spring Boot auto-configures via `application.yml/properties`

---

---

## 223. What is EntityManager?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Core JPA interface
- Manages:
    - Entity lifecycle
    - Persistence context
    - Queries
    - Transactions

---

---

## 224. What is a Persistence Context?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A **first-level cache** that tracks managed entities.

👉 One entity instance per DB row per context.

---

---

## 225. What is dirty checking?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Hibernate tracks changes to managed entities and **automatically updates DB** at flush/commit time.

---

---

## 226. What happens when entity becomes detached?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Changes are **not persisted**
- Must use `merge()` to reattach

---

---

## 227. When are changes flushed to DB?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Transaction commit
- Explicit `flush()`
- Before query execution (sometimes)

---

---

## 228. How does JPA detect changes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Snapshot comparison
- Bytecode enhancement (Hibernate)

---

---

## 229. When to use @EntityGraph?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Override fetch strategy dynamically
- Avoid N+1 without changing mapping

---

---

## 230. What is JPQL?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Object-oriented query language operating on **entities**, not tables.

---

---

## 231. When Should You Use Microservices Architecture?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

1. **When the application grows large and complex**
    
    Breaking it into smaller, independent services makes development, testing, and maintenance easier.
    
2. **When multiple teams work in parallel**
    
    Independent services allow teams to develop, deploy, and own features without blocking each other.
    
3. **When different parts need independent scaling**
    
    You can scale only the high-traffic services instead of scaling the entire application.
    
4. **When high availability and fault tolerance are critical**
    
    Failure in one service does not bring down the entire system.
    
5. **When moving to cloud or containerized environments**
    
    Microservices align well with Docker, Kubernetes, and cloud-native platforms.
    
6. **When faster and frequent releases are required**
    
    CI/CD pipelines work better with small, independently deployable services.

---

## 232. Code reviews – what do you check?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

They want **maturity**, not nitpicking.

Mention:

- Readability
- Naming
- SOLID principles
- Edge cases
- Performance impact
- Test coverage

---

---

## 233. What is Microservice Architecture?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Microservices architecture is a design style where an application is built as a **collection of small, independent services**, each responsible for a specific business capability and deployable independently.

---

---

## 234. Why do companies move from monolith to microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Faster development & releases
- Independent scaling
- Better fault isolation
- Team autonomy

---

---

## 235. What is REST API in microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

REST APIs expose **service functionality over HTTP** using standard methods like GET, POST, PUT, DELETE.

---

---

## 236. What is service-to-service communication?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

How microservices talk to each other, either:

- **Synchronous** (REST, Feign)
- **Asynchronous** (Kafka, messaging)

---

---

## 237. What is Service Discovery and why is it needed?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Service discovery helps services **find each other dynamically**, since IPs/ports change in cloud environments.

Examples: Eureka, Consul, Kubernetes DNS.

---

---

## 238. What is API Gateway? Why not call services directly?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

API Gateway acts as a **single entry point** that handles:

- Authentication
- Routing
- Rate limiting
- Logging

👉 Calling services directly increases coupling and security risk.

---

---

## 239. How do microservices communicate?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- **REST / Feign** → synchronous calls
- **Kafka / Messaging** → asynchronous, event-driven

Best systems use **both**, based on use case.

---

---

## 240. What is Load Balancing in microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Distributes traffic across multiple instances to improve:

- Availability
- Performance
- Fault tolerance

Can be client-side or server-side.

---

---

## 241. What is Centralized Configuration?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Stores configuration in one place (Git, Config Server) so services can:

- Share configs
- Change config without redeploy

---

---

## 242. How do you handle inter-service failures?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Timeouts
- Retries (with backoff)
- Circuit breakers
- Fallback responses

---

---

## 243. What is Circuit Breaker pattern?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Stops calling a failing service after repeated errors, allowing it time to recover and preventing cascading failures.

---

---

## 244. What is Distributed Tracing?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Tracks a single request **across multiple services** using trace IDs.

Tools: Zipkin, Jaeger.

---

---

## 245. How do you secure microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Authentication (OAuth2, JWT)
- Authorization
- mTLS
- API Gateway security
- Network policies

---

---

## 246. What is Event-Driven Microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Services communicate by **publishing and consuming events** instead of direct calls, improving decoupling and scalability.

---

---

## 247. How do you manage transactions in microservices?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Avoid distributed DB transactions.

Use:

- Event-based approach
- Saga pattern
- Compensation logic

---

---

## 248. What is Saga Pattern?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A sequence of **local transactions**, where each step has a **compensating action** if something fails.

---

---

## 249. One microservice is slow — how will you debug?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Check metrics & logs
- Analyze latency (DB, external calls)
- Use distributed tracing
- Check thread pool & GC

---

---

## 250. How do you handle failure of one service without impacting others?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Circuit breaker
- Fallback responses
- Async communication
- Graceful degradation

---

---

## 251. How will you scale only one microservice?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Deploy multiple instances of that service
- Use load balancer / Kubernetes HPA
- No need to scale entire system

---

---

## 252. How do you track a request across services?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Correlation ID / Trace ID
- Distributed tracing tools (Zipkin, Jaeger)

---

---

## 253. Database per service – why recommended?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Prevents tight coupling
- Independent schema changes
- Better fault isolation

---

---

## 254. How do you deploy microservices independently?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- CI/CD per service
- Containerization (Docker)
- Orchestration (Kubernetes)
- Versioned APIs

Below is a **senior-level, interview-ready answer pack** for all **50 advanced Java Backend questions**.

Each answer is **concise, technically accurate, and focused on “how it works internally + why it matters”**—exactly what interviewers expect.

---

---

## 255. How does Spring Boot auto-configuration work internally?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Uses `@EnableAutoConfiguration` → `AutoConfigurationImportSelector` → loads auto-configs from

`META-INF/spring.factories` / `AutoConfiguration.imports`, applied conditionally using `@ConditionalOnClass`, `@ConditionalOnBean`, etc.

---

---

## 256. What happens during application startup lifecycle?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

1. Bootstrap ApplicationContext
2. Load environment & configs
3. Component scan
4. Auto-configuration
5. Bean instantiation & dependency injection
6. BeanPostProcessors
7. Context refresh → app ready

---

---

## 257. What is a proxy in Spring AOP?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

A wrapper object that intercepts method calls to apply cross-cutting concerns (transactions, logging, security).

---

---

## 258. How does @Transactional work internally?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Implemented via AOP proxy
- Opens transaction before method
- Commits or rolls back based on exceptions & propagation rules

---

---

## 259. 1⃣4⃣ What Makes a Senior Java Engineer Stand Out?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Explains **trade-offs**, not just definitions
- Understands JVM & runtime behavior
- Designs for **scale and failure**
- Writes clean, testable, maintainable code

---

---

---

## 260. Where do Spring Boot logs go in Docker?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- By default → **STDOUT / STDERR**
- Docker captures logs, not files
- Best practice: **log to console**, not to `/logs/*.log`

👉 Enables centralized logging (ELK, CloudWatch).

---

---

## 261. How do you view logs of a running container?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```bash
docker logs <container-id>
docker logs -f <container-id>

```

---

---

## 262. How do you enable remote debugging?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Run container with JVM debug options:

```bash
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005

```

Expose port:

```bash
-p 8080:8080 -p 5005:5005

```

---

---

## 263. What happens when a Spring Boot container crashes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Container **stops immediately**
- Logs are preserved
- Orchestrator (Docker/K8s) may restart it

---

---

## 264. How do you restart containers automatically?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```bash
--restart=always
--restart=on-failure

```

In Kubernetes → handled by **controller**.

---

---

## 265. Why container-aware JVM settings are needed?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Older JVMs assumed **host memory** → incorrect heap sizing.

Java 11+ supports:

```
-XX:+UseContainerSupport

```

(enabled by default)

---

---

## 266. How do you tune memory in Docker?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```bash
-Xms256m
-Xmx512m
-XX:MaxMetaspaceSize=128m

```

Never rely on defaults in production.

---

---

## 267. How do you Dockerize Spring Boot?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

**Dockerfile (multi-stage):**

```docker
FROM maven:3.9-jdk-17 AS build
COPY . .
RUN mvn clean package

FROM eclipse-temurin:17-jre
COPY --from=build target/app.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]

```

---

---

## 268. How do you version Docker images?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```
myapp:1.0.0
myapp:1.1.0
myapp:commit-sha

```

---

---

## 269. How do you push images to registry?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 repo/myapp:1.0
docker push repo/myapp:1.0

```

---

---

## 270. How do you roll back?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Redeploy **previous image version**
- No rebuild required
- Kubernetes → `kubectl rollout undo`

---

---

## 271. What changes when Spring Boot runs in Kubernetes?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- No fixed IPs
- Config via ConfigMaps
- Secrets via Secrets
- Health checks mandatory

---

---

## 272. How does Actuator help?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- `/health/liveness`
- `/health/readiness`
- Metrics for autoscaling
- JVM stats for monitoring

---

---

## 273. What exactly is the Spring Framework?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Spring is a **lightweight Java framework** that helps build enterprise applications by managing **object creation, dependencies, and cross-cutting concerns** like transactions and security.

---

---

## 274. What makes Spring Boot different?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Spring Boot **removes configuration pain** using:

- Auto-configuration
- Embedded servers
- Starter dependencies

---

---

## 275. What is REST API?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Stateless, resource-based communication over HTTP.

---

---

## 276. What is JPA?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

ORM **specification**, not implementation.

---

---

## 277. Why is String immutable?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Thread-safe
- Enables String pool
- Secure (used in URLs, class loading)
- HashCode caching

---

---

## 278. Why main() is static?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

JVM must call it **without creating an object**.

---

---

## 279. Can static methods be overridden?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

❌ No — they are **hidden**, not overridden.

---

---

## 280. Why wait/notify need synchronized?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

They operate on **monitor lock**.

---

---

## 281. What is Spring Boot and why is it used?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Spring Boot is an opinionated framework built on Spring that **simplifies application development** by providing auto-configuration, embedded servers, and production-ready features.

---

---

## 282. Difference between Spring and Spring Boot

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

| Spring | Spring Boot |
| --- | --- |
| Manual configuration | Auto-configuration |
| External server | Embedded server |
| More boilerplate | Minimal boilerplate |

---

---

## 283. What is Auto-Configuration?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Automatically configures beans based on:

- Classpath
- Existing beans
- Properties
    
    Uses conditional annotations internally.
    

---

---

## 284. Explain @SpringBootApplication

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

It combines:

- `@Configuration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

---

---

## 285. How do you override default configurations?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Add properties in `application.yml`
- Use profiles
- Define your own beans

---

---

## 286. What is @SpringBootApplication composed of?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

`@Configuration + @EnableAutoConfiguration + @ComponentScan`

---

---

## 287. Explain @EnableAutoConfiguration

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

Enables Spring Boot to configure beans automatically using conditional logic.

---

---

## 288. Difference (again)

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

`@RestController = @Controller + @ResponseBody`

---

---

## 289. Optional – is it useful?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

- Yes, for **return values**
- No, for fields/params

---

## 290. Can streams be reused?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

❌ No – terminal operation consumes stream

---

---

## 291. 8⃣ One slow microservice impacting system – what to do?

*Source: [`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*

1. Identify bottleneck (CPU, DB, network)
2. Add timeouts + circuit breaker
3. Enable caching
4. Async communication where possible
5. Scale only that service
6. Add fallback responses

👉 Prevent **cascading failures**.

---

---

## 292. You need to handle 1 million requests per second. How would you scale your backend architecture?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To handle 1 million requests per second, I would consider the following strategies:

- **Load Balancing:** Use a load balancer to distribute incoming requests across multiple instances of my service. A round-robin or least-connections strategy can be implemented.
- **Horizontal Scaling:** Add more instances of the service across multiple servers. This can be achieved using container orchestration tools like Kubernetes.
- **Caching:** Implement caching using tools like Redis or Memcached to reduce database load. Cache frequently accessed data to speed up response times.
- **Asynchronous Processing:** Use message queues (e.g., RabbitMQ, Kafka) to process requests asynchronously. This allows the system to queue requests and handle them at a rate the backend can manage without dropping requests.
- **Optimized Database Access:** Use a NoSQL database for high-speed reads/writes or partitioning/sharding of relational databases to ensure no single database becomes a bottleneck.
- **CDN Usage:** Use Content Delivery Networks (CDNs) for static content to offload traffic from the backend.

---

## 293. Design a simple service that asynchronously processes tasks using Spring Boot.

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To design an asynchronous processing service in Spring Boot, I would use Spring’s **`@Async`** annotation along with a thread pool. Here is a basic outline of the implementation:

1. **Enable Async Support:** Use **`@EnableAsync`** in the configuration class.

`@Configuration
@EnableAsync
public class AsyncConfig {
@Bean
public Executor taskExecutor() {
ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
executor.setCorePoolSize(5);
executor.setMaxPoolSize(10);
executor.setQueueCapacity(25);
executor.initialize();
return executor;
}
}`

1. **Create Service:** Define a service that contains an asynchronous method.

`@Service
public class TaskService {
@Async
public void processTask(String taskId) {
// Simulate a long-running task
try {
Thread.sleep(5000); // Simulates processing time
} catch (InterruptedException e) {
Thread.currentThread().interrupt();
}
System.out.println("Processed task with ID: " + taskId);
}
}`

1. **Controller:** Expose an endpoint to trigger the asynchronous task.

```

@RestController
public class TaskController {
@Autowired
private TaskService taskService;
@PostMapping("/tasks")
public ResponseEntity<String> createTask(@RequestBody String taskId) {
    taskService.processTask(taskId);
    return ResponseEntity.accepted().body("Task is being processed.");
}}
```

---

## 294. You have a distributed system where one microservice must call another but should retry on failure. How would you implement this in Spring Boot?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To implement retry logic in Spring Boot for calls between microservices, I would use Spring Retry or Resilience4j. Here's how to do it with Spring Retry:

1. **Add Dependency:** Include Spring Retry dependency in the **`pom.xml`**.

<dependency>
<groupId>org.springframework.retry</groupId>
<artifactId>spring-retry</artifactId>
</dependency>

1. **Define a Service to Call Another Microservice (continued):**

```jsx
@Service
public class RemoteService {
    @Retryable(maxAttempts = 3, backoff = @Backoff(delay = 2000))
    public ResponseEntity<String> callOtherService(String url) {
        // Code to make a REST call to another microservice
        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.getForEntity(url, String.class);
    }

    @Recover
    public ResponseEntity<String> recoverFromFailure(Exception e, String url) {
        // Handle the failure scenario here, for example, return a default response or log the error
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE)
                             .body("Unable to reach the service at: " + url);
    }
}

```

1. **Calling the Remote Service:**

In your controller or another service, you would call the **`callOtherService`** method to handle the retry logic automatically.

```jsx
@RestController
public class MyController {
    @Autowired
    private RemoteService remoteService;

    @GetMapping("/call")
    public ResponseEntity<String> callOtherService() {
        String url = "http://other-microservice/api/resource";
        return remoteService.callOtherService(url);
    }
}
```

---

## 295. 5 You deployed a Spring Boot service, but it crashes with an "Out of Memory" error. How do you debug this?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

Debugging an "Out of Memory" (OOM) error in a Spring Boot service involves several steps to identify the root cause and implement corrective actions. Here’s a structured approach to debugging this issue:

**Debugging Steps for "Out of Memory" Errors**

1. **Check the Logs:**
    - Start by checking the application logs to capture any stack trace or error messages before the OOM error occurs. This can give insights into what the application was doing at the time of the crash.
2. **Analyze JVM Heap Dump:**
    - Generate a heap dump at the time of the OOM error. You can do this by adding the JVM option:
        
        ```
        Copy code
        -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=path/to/dump
        ```
        
    - After the crash, analyze the heap dump using tools like **Eclipse MAT (Memory Analyzer Tool)** or **VisualVM**. Look for:
        - Memory usage trends over time.
        - Objects that occupy a significant portion of the heap.
        - Any potential memory leaks (e.g., retained objects that should have been collected).
3. **Monitor Memory Usage:**
    - Use monitoring tools like **Prometheus**, **Grafana**, **JConsole**, or **Spring Boot Actuator** to monitor memory consumption in real-time. This can help identify patterns and determine if the memory usage is stable, increasing over time, or spiking during certain operations.
4. **Tune JVM Options:**
    - Adjust the JVM heap size settings (**`Xms`** and **`Xmx`**). For example:
        
        ```
        Copy code
        java -Xms512m -Xmx2048m -jar your-app.jar
        ```
        
    - Ensure you are allocating enough memory based on the application’s requirements and the overall system capacity.
5. **Check for Memory Leaks:**
    - Identify common sources of memory leaks such as:
        - Static collections that grow indefinitely.
        - Unclosed database connections, file streams, or other resources.
        - Thread-local variables that are not cleaned up properly.
        - Event listeners not being removed when no longer needed.
6. **Inspect Application Code:**
    - Review your code for patterns that may lead to excessive memory usage, such as:
        - Large object creation (e.g., reading large files into memory).
        - Inefficient data structures (e.g., using **`ArrayList`** when a **`LinkedList`** would suffice).
        - Unbounded caching without eviction policies.
7. **Profile the Application:**
    - Use profiling tools such as **YourKit**, **JProfiler**, or **VisualVM** to analyze memory allocation and find hotspots in the code where memory usage spikes.
8. **Implement Garbage Collection Logging:**
    - Enable garbage collection (GC) logging to understand how the garbage collector is managing memory. This can be done by adding:
        
        ```
        Copy code
        -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -Xloggc:path/to/gc.log
        ```
        
    - Analyze the generated GC logs for:
        - Frequency of GC events.
        - Time taken for GC.
        - Amount of memory freed by GC.
9. **Check External Dependencies:**
    - If your service interacts with external systems (databases, APIs, etc.), ensure that those components are not causing memory overhead, for example, by returning excessively large data sets.
10. **Review the Deployment Environment:**
    - Ensure that the environment hosting your Spring Boot service (e.g., a VM, Docker container, or Kubernetes pod) has sufficient memory allocated and that it isn't constrained by resource limits.

💡 Java Interview Series: Deep Dive into Java 8 Features

Welcome back to the Java Interview Series! Today, we’ll explore Java 8, one of the most revolutionary versions of Java, introducing functional programming and more. Let’s break it down into interview-ready concepts!

- --

🌟 Topic 1: Lambda Expressions

What are Lambda Expressions?

They provide a way to write short, anonymous functions.

Syntax: (parameters) -> {body}

Example:

// Traditional way

Runnable runnable = new Runnable() {

@Override

public void run() {

System.out.println("Hello, World!");

}

};

// Using Lambda

Runnable lambdaRunnable = () -> System.out.println("Hello, World!");

Common Interview Questions:

1️⃣ What are Lambda Expressions, and why are they used?

2️⃣ Can Lambda Expressions access local variables? (Yes, but they must be effectively final.)

- --

🌟 Topic 2: Stream API

What is the Stream API?

A powerful tool for processing collections in a functional way.

Key Operations:

Intermediate Operations: filter(), map(), sorted().

Terminal Operations: forEach(), collect(), reduce().

Example:

List<String> names = Arrays.asList("John", "Jane", "Jack", "Jill");

[names.stream](http://names.stream/)

()

.filter(name -> name.startsWith("J"))

.sorted()

.forEach(System.out::println);

Common Interview Questions:

1️⃣ Difference between map() and flatMap().

2️⃣ How does lazy evaluation work in Streams?

- --

🌟 Topic 3: Functional Interfaces

What are Functional Interfaces?

Interfaces with only one abstract method, used with Lambda Expressions.

Example: Runnable, Comparator, Supplier.

Custom Functional Interface Example:

@FunctionalInterface

interface Calculator {

int add(int a, int b);

}

Calculator calculator = (a, b) -> a + b;

System.out.println(calculator.add(5, 3));

- --

🌟 Topic 4: Optional API

What is Optional?

A container for handling null values gracefully.

Example:

Optional<String> optionalName = Optional.ofNullable(null);

optionalName.ifPresentOrElse(

System.out::println,

() -> System.out.println("Name is not present")

);

Common Questions:

1️⃣ What problem does Optional solve?

2️⃣ How does Optional.orElse() differ from Optional.orElseGet()?

---

## 296. · What are the possible causes of memory leaks in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

·       How to find which objects are causing the memory leak?
·       How to use a profiler (like JVisualVM, YourKit) to detect leaks?

**Answer to the Interview Question**

When a Spring Boot microservice running on Kubernetes crashes with an **`OutOfMemoryError`**, it suggests that there may be memory leaks or inefficient memory usage in your application. Here’s how to address the possible causes and identify the leaks.

**1. Possible Causes of Memory Leaks in Java**

Memory leaks in Java can occur due to various reasons, including but not limited to:

- **Static References:** Improper use of static fields that hold onto objects longer than necessary can lead to leaks (e.g., static collections or caches).
- **Event Listeners:** Failing to unregister event listeners or callbacks can prevent garbage collection of objects that are no longer needed.
- **Thread Local Variables:** Not cleaning up ThreadLocal variables can cause memory leaks in multi-threaded environments.
- **Unclosed Resources:** Resources such as database connections, file streams, or network sockets that are not closed properly can lead to memory issues.
- **Large Caches:** Implementing caching mechanisms without eviction policies can lead to a gradual increase in memory usage.
- **Incorrect Object Lifecycle Management:** Retaining references to objects longer than needed, especially in long-lived classes or singleton beans.

---

## 297. How to Find Which Objects Are Causing the Memory Leak

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To identify which objects are causing the memory leak:

- **Heap Dumps:** Generate a heap dump when the memory usage is high or when the **`OutOfMemoryError`** occurs. You can do this by adding the following JVM option:

```jsx
-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/path/to/dump
```

- **Analyze Heap Dumps:** Use tools like Eclipse Memory Analyzer (MAT), JVisualVM, or YourKit to analyze the heap dump. Look for:
    - **Dominators Tree:** This helps identify the largest objects in memory and their retainers.
    - **Histogram:** Check for classes with a high number of instances or a large amount of memory allocated.
    - **Paths to GC Roots:** Analyze which objects are preventing others from being garbage-collected.

---

## 298. How to Use a Profiler (like JVisualVM, YourKit) to Detect Leaks

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

Using a profiler such as JVisualVM or YourKit can be greatly beneficial in detecting memory leaks:

**Using JVisualVM:**

1. **Launch JVisualVM:**
    - Start JVisualVM from the command line or IDE, and connect it to your running Spring Boot application (you may need to add a JMX option to your JVM).
2. **Monitor Memory Usage:**
- Navigate to the “Monitor” tab to view real-time memory usage and the number of loaded classes. Observe the usage pattern over time.
1. **Take a Heap Dump:**
    - When you notice high memory usage, take a heap dump by clicking on the "Heap Dump" button.
2. **Analyze Heap Dump:**
    - Open the heap dump in JVisualVM. Use the “Classes” and “Instances” views to investigate the memory consumption.
    - You can also use the “Profiler” tab to perform live memory profiling, where you can see which methods allocate the most memory.

**Using Your Kit:**

1. **Start YourKit Profiler:**
    - Start YourKit and attach it to your Spring Boot application.
2. **Record Memory Usage:**
    - Use the built-in profiling options to monitor memory allocation and garbage collection activity. You can set the profiler to record CPU and memory usage continuously.
3. **Identify Memory Leaks:**
    - Analyze the component that consumes the most memory and identify high-instance classes.
    - Use the “Memory” and “CPU” tabs to pinpoint any abnormal allocations or retained objects that may suggest leaks.

---

## 299. · How can you profile CPU usage in a running application?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

When a microservice begins consuming high CPU (90%) without an increase in incoming traffic, it’s crucial to investigate the issue to identify and fix the root cause. Here's how to approach it:

---

## 300. How to Investigate and Identify the Root Cause

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

- **Monitor Application Metrics:**
    - Use monitoring tools (such as Prometheus, Grafana, or application performance monitoring tools like New Relic, Datadog, etc.) to view metrics such as CPU usage, memory usage, and thread counts over time.
    - Look for any anomalies, spikes, or patterns that could correlate with the increased CPU usage.
- **Check Application Logs:**
    - Review the application logs for any unusual error messages, warnings, or exceptions that may indicate unexpected behavior or performance issues.
    - Look for recent changes to the application or any dependencies that could cause increased CPU load.
- **Examine Thread Activity:**
    - Use Java Thread Dumps to analyze what threads are doing while the CPU is high. You can capture thread dumps using tools like **`jstack`** or **`jcmd`**.
    - Look for threads that are consuming a lot of CPU and analyze their stack traces to determine what operations they are performing.

---

## 301. What Could Cause a Thread to Enter an Infinite Loop?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

Several factors can lead to a thread entering an infinite loop:

- **Logic Errors:** Bugs in the code where the termination condition for a loop is never met (e.g., a "while" loop that doesn't have a proper exit condition).
- **Race Conditions:** Concurrency issues that might lead to a situation where shared state doesn't change as expected, causing code to indefinitely wait or loop.
- **Improper Error Handling:** If the code catches an exception but doesn't handle it properly, it may inadvertently enter a repeat loop without appropriate break conditions.
- **External Dependencies:** Dependence on external services or APIs that may not be responding and lead to repeated retry logic without a proper exit condition, thus causing loops.

---

## 302. · What Spring mechanisms help break circular dependencies?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**
    
    When a Spring Boot application fails to start due to a **`BeanCurrentlyInCreationException`** stemming from a circular dependency, it indicates that two or more beans are referencing each other in a way that creates a loop. Here’s how to debug and fix this issue, along with the Spring mechanisms that can help break circular dependencies.

---

## 303. How to Debug and Fix This Issue

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Debugging Steps:**
    
    - **Identify the Circular Dependency:**
        - Review your application’s logs. When the application fails to start, the logs usually contain a stack trace that shows the beans involved in the circular dependency. Look for lines indicating which bean is currently being created.
    - **Inspect Your Code:**
        - Check the constructors or methods of the involved beans for autowired dependencies. Pay special attention to how the dependencies are structured.
        - Example: If **`ClassA`** depends on **`ClassB`**, and **`ClassB`** also depends on **`ClassA`**, this creates a circular dependency.
    - **Use `@Lazy` Annotations:**
        - As a quick fix, you can use the **`@Lazy`** annotation on one of the beans. This instructs Spring to inject a proxy instead of the actual bean, delaying its initialization until it's actually needed.

```jsx
@Service
public class ClassA {
    private final ClassB classB;

    @Autowired
    public ClassA(@Lazy ClassB classB) {
        this.classB = classB;
    }

    // ...
}
```

**Fixing the Issue:**

- **Refactor Your Code:**
    - Refactoring the beans to eliminate the circular dependency is the best long-term solution.
    - Consider introducing a new intermediary service to handle the interactions between the two conflicting beans or restructuring the way dependencies are handled.
    - Example:
        - If **`ClassA`** and **`ClassB`** both depend on methods from each other, you might extract the shared logic into a third class, **`ClassC`**, that both **`ClassA`** and **`ClassB`** can depend on without directly referencing each other.
        
    
    **Use Setter Injection:**
    
    - If feasible, you can switch from constructor injection to setter injection. This allows Spring to create the beans without requiring immediate availability of the other beans.

```jsx
@Service
public class ClassA {
    private ClassB classB;

    @Autowired
    public void setClassB(ClassB classB) {
        this.classB = classB;
    }

    // ...
}
```

---

## 304. · How can you avoid deadlocks in database transactions?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

When a Spring Boot application occasionally freezes and stops processing requests, one possible cause could be a deadlock situation, where two or more threads are waiting for each other to release resources. Here’s how to detect deadlocks, use diagnostic tools like **`jstack`**, and avoid deadlocks in database transactions.

---

## 305. How to Detect a Deadlock in Java

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To detect a deadlock in Java:

- **Thread Dumps:** The most common method to detect a deadlock is through thread dumps. A thread dump provides detailed information about the state of each thread in the JVM, including stacks, the resources they are holding, and the resources they are waiting for.
- **Java Management Extensions (JMX):** JMX can be used to monitor the Java application and check for deadlocks. You can access the **`ThreadMXBean`** and call **`findDeadlockedThreads()`** to identify any threads participating in a deadlock.
- **Monitoring Tools:** Utilize monitoring tools like Java VisualVM or JConsole, which can show live thread state information. Often, these tools will provide visual indicators when a deadlock is present.

---

## 306. How Can You Use jstack to Diagnose the Issue?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**`jstack`** is a command-line tool that can be used to print Java thread stack traces for a given Java process. Here’s how you can use it to diagnose deadlocks:

1. **Identify the Process ID (PID):**
    - First, find the PID of your running Spring Boot application using commands like **`jps`** or through your application’s logs.

**Run `jstack`:**

- Execute **`jstack`** with the PID of your Java application:

```jsx
jstack <PID>
```

1. **Analyze the Output:**
    - The output will show you the stack traces of all threads. Look for threads that are in a **`BLOCKED`** state and examine the **`java.lang.Object.wait()`** calls. In the stack trace, it will indicate which monitors (locks) each thread is waiting for and which thread is holding that lock.
    - Identify any cycles in the resource wait (i.e., Thread A is waiting for Thread B’s lock, and Thread B is waiting for Thread A’s lock) to confirm a deadlock.
2. **Deadlock Information:**
    - If a deadlock is detected, the **`jstack`** output typically includes a section indicating it, like “Found one Java-level deadlock.”

---

## 307. · How can Redis help in rate limiting?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

Implementing a rate limiter is an effective strategy to prevent API abuse in a Spring Boot application. Here's how you can implement it, the algorithms you could use, and how Redis can assist in the process.

---

## 308. How Would You Implement a Rate Limiter in Spring Boot?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

To implement a rate limiter in Spring Boot, you can use different approaches. One common approach is to create an interceptor that will check the request rate per user or IP address. Here’s a high-level guide on how to do it:

- **Use Filters or Interceptors:**
    - Implement a filter or interceptor that intercepts incoming requests.
    - Extract the relevant key for rate limiting (like user ID or IP address) from the request.
- **Store Rate Limit Data:**
    - Maintain a data structure (in-memory, database, or cache) that tracks the request counts and timestamps against the identified key (like user ID or IP).
- **Check the Request Count:**
    - On each incoming request, check the current request count against the allowed rate limit. If the request count exceeds the limit, respond with an appropriate HTTP status code (like 429 Too Many Requests).
- **Reset Counts:**
    - Implement logic to reset counts at the appropriate intervals. This can be done using scheduled tasks.

**Example using Spring's `Servlet Filter`:**

```jsx
@Component
public class RateLimitFilter implements Filter {

    private final RateLimiter rateLimiter; // Initialize your rate limiter

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        String userId = ...; // extract user identifier, e.g., from headers or query parameters
        if (!rateLimiter.allowRequest(userId)) {
            ((HttpServletResponse) response).sendError(HttpStatus.TOO_MANY_REQUESTS.value(), "Rate limit exceeded");
            return;
        }

        chain.doFilter(request, response);
    }
}
```

---

## 309. Which Algorithms Would You Use? (Token Bucket vs. Leaky Bucket)

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Token Bucket:**

- **How It Works:** Each user has a "bucket" that holds tokens. On each request, a token is removed from the bucket, and if there are no tokens available, the request is denied. Tokens are added back to the bucket at a fixed rate.
- **Advantages:** This allows for bursts of traffic up to the number of tokens in the bucket but maintains a smooth average rate.
- **Use Case:** Best for scenarios where you want to allow for sporadic bursts of requests while ensuring the request rate over time does not exceed a certain limit.

**Leaky Bucket:**

- **How It Works:** The leaky bucket algorithm processes requests at a constant rate, regardless of arrival rate—if requests come in too quickly, they overflow and are discarded.
- **Advantages:** This approach smooths out bursts by enforcing a maximum rate limit, which can provide a more consistent flow of requests.
- **Use Case:** Ideal for scenarios where you want to ensure smooth processing and don’t want to accept bursts.

**Recommendation:** The **Token Bucket** algorithm is often more flexible and generally preferred in REST APIs as it allows flexibility in request bursts while adhering to a strict average rate limit.

---

## 310. · How do you handle sudden traffic spikes?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

When expecting over 1 million requests per second during peak load, designing a scalable and resilient system is crucial. Here are strategies to scale your system, implement effective caching mechanisms, and handle sudden traffic spikes.

---

## 311. How Do You Scale Your System?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Horizontal Scaling:**

- **Microservices Architecture:** Break the application into microservices that can be deployed independently. Each microservice can handle specific functionalities, allowing for more granular scaling.
- **Load Balancing:** Use load balancers to distribute incoming requests evenly across multiple instances of services. Implement sticky sessions if necessary, or leverage header-based routing for canary releases.

**Auto-Scaling:**

- **Cloud Infrastructure:** Utilize cloud service providers (such as AWS, Google Cloud, or Azure) to set up auto-scaling groups. Configure rules to automatically scale the number of instances based on predefined metrics (e.g., CPU or memory utilization, request latency).
- **Container Orchestration:** Use Kubernetes or a similar orchestration tool to manage the deployment of microservices. Kubernetes can auto-scale pods based on resource utilization.

**Database Scaling:**

- **Database Sharding:** Split the database into smaller, manageable pieces (shards) to distribute the load. Each shard can support a portion of the total requests based on some sharding logic (e.g., user ID).
- **Replica Sets:** Deploy read replicas to distribute read traffic from the database, allowing write operations to be handled by a primary database instance while reads are spread across the replicas.

---

## 312. What Caching Mechanisms Would You Implement?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**In-Memory Caching:**

- **Use Caching Frameworks:** Implement caching solutions like Redis or Memcached to cache frequently accessed data in memory. This drastically reduces database load and speeds up response times.
- **Cache Patterns:**
    - **Cache-aside:** Only load data into the cache when required, allowing for dynamic caching.
    - **Write-Through or Write-Behind Caching:** Ensure that when data is written to the database, it is also updated in the cache, helping maintain cache coherence.

**Content Delivery Network (CDN):**

- **Static Content Caching:** Use a CDN to cache static assets (images, stylesheets, scripts) at edge locations, reducing latency and load on the origin server.
- **APIs:** If applicable, utilize CDN services that support dynamic content caching for API responses.

**Application-Level Caching:**

- **Local Caching**: Use simple in-memory caching in the application itself (e.g., using **`ConcurrentHashMap`**) for transient data that doesn’t need to be persisted and is frequently accessed.

---

## 313. · How to implement a resumable upload?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

When dealing with large file uploads (1GB+), it’s important to design a solution that ensures efficient handling, minimizes service disruption, and enhances user experience. Here’s how to approach this scenario.

---

## 314. What’s the Best Way to Handle File Uploads Efficiently?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Asynchronous Uploads:**

- Utilize asynchronous processing to handle file uploads. Instead of blocking the service, accept the file upload request quickly and process the file in the background.
- This can be achieved by implementing a queueing mechanism (using RabbitMQ, Kafka, etc.) to manage file upload tasks without overloading the server.

**Chunked Uploads:**

- Implement chunked file uploads, where large files are split into smaller parts (chunks) that can be uploaded individually. This not only improves the upload experience but also allows for easier error recovery, as users can retry only the failed chunks without starting the upload from scratch.

**Stream Processing:**

- Use streaming techniques (e.g., leveraging input streams) to read and write files in chunks directly to the storage solution, which minimizes memory usage on the application server.

**Content Delivery:**

- Ensure that the files are uploaded to locations that provide low latency and high availability, which may involve considering geographical locations of the storage solution.

---

## 315. Would You Use S3, MinIO, or Another Storage Solution?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Amazon S3:**

- Amazon S3 is a popular choice for file uploads, especially for large files, due to its scalability, durability, and built-in redundancy features.
- It supports multipart uploads, which is particularly useful for handling files larger than 5GB, allowing uploads to be divided into smaller parts.

**MinIO:**

- MinIO is a high-performance, self-hosted alternative to S3 that provides an S3-compatible API. It’s suitable for environments where you require on-premises storage solutions or want to avoid vendor lock-in.
- MinIO also supports multipart uploads, giving you similar functionality as S3.

**Other Solutions:**

- Depending on specific requirements (e.g., cost, on-prem infrastructure), you might evaluate alternatives such as Azure Blob Storage, Google Cloud Storage, or various object storage solutions.

**Recommendation:**

- The choice between S3 and MinIO largely depends on cloud dependency needs versus control over your storage infrastructure. S3 is generally the go-to for cloud-native applications, while MinIO is often favored for on-prem solutions or hybrid architectures.

---

## 316. · How do you fix the memory leak?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

---

## 317. What is Wrong with This Code?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

The code provided has a memory leak due to the static **`List<String> cache`** that retains references to an ever-increasing amount of data (1,000,000 strings in this case) each time the **`addData()`** method is called. Since **`cache`** is a static variable, it persists for the lifetime of the application and continues to grow indefinitely with each invocation of **`addData()`**, leading to excessive memory consumption.

**Key Points:**

- **Static Variable:** The use of a static variable means that the data stored in **`cache`** will remain in memory until the application terminates, preventing garbage collection of older data.
- **No Eviction Logic:** There is no mechanism to remove or manage the size of the **`cache`**. As a result, it leads to excessive memory usage which cannot be reclaimed, ultimately causing an **`OutOfMemoryError`**.

---

## 318. · How would you make it thread-safe?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

---

## 319. Why Is the Code Not Thread-Safe?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

The provided **`Counter`** class is not thread-safe due to the way the **`increment()`** method modifies the shared variable **`count`**. Here’s a breakdown of the key issues:

1. **Non-Atomic Operation:**
    - The operation **`count++`** is not atomic. It consists of three distinct operations:
        - Reading the current value of **`count`**.
        - Incrementing that value.
        - Writing the new value back to **`count`**.
2. **Race Conditions:**
    - In a multi-threaded environment, if multiple threads invoke **`increment()`** concurrently, they may read, modify, and write back the value of **`count`** simultaneously. This can lead to lost updates and incorrect counts. For example, if two threads read the same value of **`count`**, both increment it, and then write back the same incremented value, one increment will effectively be lost.

---

## 320. · How can you optimize it using pagination?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

**Answer to the Interview Question**

---

## 321. Why Is This Method Slow for Large Datasets?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

The **`getAllUsers()`** method retrieves all users from the database using **`userRepository.findAll()`**. This approach can be slow for large datasets due to several reasons:

1. **Memory Consumption:**
    - When retrieving a large number of records (potentially hundreds of thousands or millions), all user objects are loaded into memory at once. This can lead to high memory usage, and if the dataset is larger than the available heap space, it may result in an **`OutOfMemoryError`**.
2. **Performance Degradation:**
    - The time taken to read all the records from the database and convert them into Java objects grows linearly with the number of records. As the dataset grows, this delay can become significant, potentially leading to slow response times.
3. **Network Latency:**
    - If the JSON response containing all user data is large, it can create delays in network transmission. The server will need to serialize all the user objects into JSON, and the client will take longer to receive and process the response.
4. **Database Load:**
    - A request for all user data can put unnecessary load on the database, especially if multiple users make similar requests simultaneously. This can impact the overall performance of the application, especially during peak usage times.

---

## 322. What is the Purpose of the Static Keyword in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

The **`static`** keyword in Java serves several purposes:

- **Shared Among All Instances:** It allows the variable or method to be shared among all instances of a class rather than having a separate copy for each instance.
- **Class-Level Access:** Static members belong to the class itself rather than to any specific instance. This means that they can be accessed without needing an object of the class.
- **Memory Management:** Static variables reduce memory usage since they are allocated memory once per class rather than for each object instance.
- **Utility or Helper Methods:** Static methods are often used for utility or helper methods that do not require any object state to be manipulated.

---

## 323. How is a Static Variable Different from an Instance Variable?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

- **Scope:**
    - **Static Variable:** A static variable is associated with the class itself and is shared across all instances of the class. There is only one copy of a static variable, regardless of how many objects of the class are created.
    - **Instance Variable:** An instance variable is associated with a specific object of the class. Each instance has its own copy of instance variables.
- **Memory Allocation:**
    - **Static Variable:** Memory for static variables is allocated when the class is loaded into memory and they are stored in the **Heap** memory.
    - **Instance Variable:** Memory for instance variables is allocated when an object is created and they are stored in the **Heap** memory as part of the object.
- **Access:**
    - **Static Variable:** Accessed using the class name (e.g., **`ClassName.staticVariable`**).
    - **Instance Variable:** Accessed using the object reference (e.g., **`objectName.instanceVariable`**).

---

## 324. Can a Static Method Access Non-Static Members of a Class? Why or Why Not?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

No, a static method cannot access non-static (instance) members of a class directly. The reason is:

- **Static Context:** Static methods belong to the class itself and do not have a reference to any specific instance of the class. Since non-static members are bound to a particular instance, there is no implicit reference (like **`this`**) available for static methods to access those instance members.
- **Object Reference Required:** If you need to access non-static members from a static method, you must create an instance of the class and use that instance to access the non-static members. For example:

```jsx
public class MyClass {
    private int instanceVariable = 10; // Instance variable

    public static void staticMethod() {
        MyClass obj = new MyClass(); // Creating an instance
        System.out.println(obj.instanceVariable); // Accessing instance variable
    }
}
```

---

## 325. What is the Difference Between a Static Block and a Constructor in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

- **Purpose:**
    - **Static Block:** A static block is used for static initialization of a class. It runs once when the class is loaded into memory, and it's typically used to initialize static variables or execute startup tasks.
    - **Constructor:** A constructor is used for initializing instance variables when an object of the class is created. It is invoked every time a new object is created.
- **Execution Timing:**
    - **Static Block:** Executes only once when the class is loaded (before any instances are created).
    - **Constructor:** Executes every time a new instance of the class is created.
- **Context:**
    - **Static Block:** Only has access to static members of the class.
    - **Constructor:** Can access both static and instance members of the class.

Example of a static block and constructor:

```jsx
public class MyClass {
    static int staticVariable;

    static {
        // Static block
        staticVariable = 5;
        System.out.println("Static block executed.");
    }

    public MyClass() {
        // Constructor
        System.out.println("Constructor executed.");
    }
}
```

---

## 326. How is Memory Allocated for Static Variables in Java? Where Are They Stored?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

- **Memory Allocation**: Static variables are allocated memory when the class is loaded into the Java Virtual Machine (JVM). This happens before any objects of that class are created, during the class loading process.
- **Storage Location**: Static variables are stored in the **Method Area** (part of the JVM memory structure) as part of the class's metadata. This area is distinct from the memory allocated for instance variables, which are stored on the heap as part of the object.

In summary:

- **Static Variables:**
    - **Associated with the Class:** There is one static variable per class, shared by all instances of that class.
    - **Memory Location:** Stored in the **Method Area** of the JVM memory model.
    - **Lifecycle:** Initialized when the class is loaded and retain their value throughout the program’s execution until the class is unloaded (usually when the application terminates).
    - **Access:** Can be accessed using the class name (e.g., **`ClassName.staticVariable`**).
- **Instance Variables:**
    - **Associated with Instances (Objects):** Each object of the class has its own copy of instance variables, leading to different values across different instances.
    - **Memory Location:** Stored in the **Heap** memory as part of the object's state.
    - **Lifecycle:** Initialized when a new instance of the class is created, and their values can persist throughout the lifetime of that object.
    - **Access:** Accessed using object references (e.g., **`objectName.instanceVariable`**).

---

## 327. What Are the Characteristics of a Static Variable in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

1. **Class-Level Scope:** Static variables belong to the class rather than instances of the class. There is only one copy of a static variable shared among all instances of that class.
2. **Memory Allocation:** Memory for static variables is allocated when the class is loaded into memory, specifically in the Method Area of the Java Virtual Machine (JVM).
3. **Lifetime:** The lifetime of a static variable lasts as long as the class is loaded in memory. The variable retains its value until the class is unloaded (typically when the application stops).
4. **Access:** Static variables can be accessed directly through the class name (e.g., **`ClassName.staticVariable`**) without needing to instantiate an object of the class.
5. **Initialization:** Static variables are initialized when the class is loaded and can be initialized in a static block, at the point of declaration, or in a static method.
6. **Shared Among Instances:** Since there is only one copy of the static variable, if it is modified by one instance of the class, the new value is reflected in all instances.

---

## 328. When Should You Use Static Variables in an Application?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

You should use static variables in the following scenarios:

1. **Shared Constants:** When you want to define constants that should be the same across all instances (e.g., mathematical constants, configuration values).

```jsx
public class MathConstants {
    public static final double PI = 3.14159;
}
```

**Class-Level State:** When you need to maintain a counter or any status information that should be shared among instances of a class (e.g., counting how many objects of a class have been created).

```jsx
public class Counter {
    private static int count = 0;

    public Counter() {
        count++; // Increment the count for each new instance
    }

    public static int getCount() {
        return count;
    }
}
```

1. **Utility or Helper Methods:** In utility classes, where you want to group related functions together without requiring instantiation.
2. **Configuration Variables:** When you need a class-wide configuration that should be consistent among all instances.

---

## 329. Can a Static Variable Be Marked as Final? What Does It Mean?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

Yes, a static variable can be marked as **`final`**. When a static variable is declared as **`final`**, it means that the variable can only be assigned once and cannot be changed afterwards.

**Characteristics of a `final` static variable:**

- **Initialization**: It must be initialized when it's declared or in a static initialization block.
- **Immutability**: The value cannot be modified after it has been initialized.

**Example:**

```jsx
public class Example {
    public static final int CONSTANT_VALUE = 10;

    public void changeConstant() {
        // CONSTANT_VALUE = 20; // This will cause a compilation error
    }
}
```

In this example, **`CONSTANT_VALUE`** is a static final variable that acts like a constant and cannot be changed after being assigned.

---

## 330. How Do Static Variables Behave in a Multi-Threaded Environment? How Can You Handle Thread Safety?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

In a multi-threaded environment, static variables can lead to concurrency issues. Since static variables are shared among all threads, if multiple threads manipulate the same static variable simultaneously, it can result in inconsistent or unexpected behavior due to race conditions.

**Handling Thread Safety with Static Variables:**

1. **Synchronized Methods:** Use synchronized methods to restrict access to static variables. This ensures that only one thread can execute the synchronized method at a time.

```jsx
public class ThreadSafeCounter {
    private static int count = 0;

    public static synchronized void increment() {
        count++;
    }

    public static synchronized int getCount() {
        return count;
    }
}
```

1. In this example, both **`increment()`** and **`getCount()`** methods are synchronized, which keeps the operations atomic and ensures thread safety when accessing or modifying the **`count`**.
2. **Synchronized Blocks**: For more granular control over which parts of the code need to be synchronized, you can use synchronized blocks instead of synchronizing the entire method.

```jsx
public class ThreadSafeCounter {
    private static int count = 0;

    public static void increment() {
        synchronized (ThreadSafeCounter.class) {
            count++;
        }
    }

    public static int getCount() {
        synchronized (ThreadSafeCounter.class) {
            return count;
        }
    }
}
```

**Atomic Variables**: Use classes from the **`java.util.concurrent.atomic`** package, like **`AtomicInteger`**, to handle thread-safe operations without explicit synchronization. These classes use low-level atomic operations, which provide better performance under high contention.

```jsx
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicCounter {
    private static AtomicInteger count = new AtomicInteger(0);

    public static void increment() {
        count.incrementAndGet(); // Atomically increments by one
    }

    public static int getCount() {
        return count.get();
    }
}
```

**Using Locks**: If you need more control over concurrency, you can use **`ReentrantLock`** for fine-grained locking and better performance in scenarios where contention is expected to be high.

```jsx
import java.util.concurrent.locks.ReentrantLock;

public class LockingCounter {
    private static int count = 0;
    private static final ReentrantLock lock = new ReentrantLock();

    public static void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }

    public static int getCount() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }
}
```

---

## 331. Why Can’t a Static Method Access Non-Static Variables or Methods Directly?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

A static method cannot access non-static variables or methods directly because:

- **Static Context vs. Instance Context**: Static methods belong to the class itself rather than any specific instance of the class. This means they do not have access to instance-specific ("non-static") data, which requires a reference to an object.
- **No Implicit `this` Reference**: Non-static methods and variables require an implicit reference to the object instance (accessed using **`this`**). Since static methods do not have this reference, they cannot access instance variables or methods directly.

```jsx
class MyClass {
    private int instanceVariable = 10;

    public static void staticMethod() {
        // This will cause a compile-time error
        // System.out.println(instanceVariable);
    }
}
```

---

## 332. Can a Static Method Be Overridden in Java? Why or Why Not?

*Source: [`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*

No, a static method cannot be overridden in Java. The reason is:

- **Static vs. Instance**: Static methods are associated with the class level, while instance methods are associated with an instance of the class. Static methods are determined at compile time and do not partake in method resolution through dynamic (runtime) polymorphism.
- **Hiding Instead of Overriding**: If a static method in a subclass has the same name and signature as a static method in the superclass, it is said to be hiding, not overriding. The method that gets called is based on the reference type, not the object type.

**Example:**

```jsx
class Parent {
    static void staticMethod() {
        System.out.println("Static method in Parent");
    }
}

class Child extends Parent {
    static void staticMethod() {
        System.out.println("Static method in Child");
    }
}

// Output
Parent obj = new Child();
obj.staticMethod(); // Outputs: "Static method in Parent"
```

[Shiva kumar satakuri linkedin java interview questions](java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)

---

## 333. Which Versions of Java Have You Worked On?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In my experience, I have worked with the following versions of Java:

- **Java SE 8:** I appreciate its introduction of significant features like Lambda expressions, the Stream API for processing sequences of elements, and the Date and Time API for better date and time handling.
- **Java SE 11:** I used this version predominantly in production environments due to its Long-Term Support (LTS) status. Key features include the introduction of the **`var`** keyword for local variable type inference and the incorporation of several new utilities and enhancements to existing libraries.
- **Java SE 17:** Another LTS version that I have utilized, which includes improvements in pattern matching for **`instanceof`**, sealed classes for better type control, and other enhancements.
- **Java SE 21:** I have recently started exploring features from this version as it includes exciting developments like record patterns, improved performance enhancements, and new APIs.

---

## 334. What Are the Features of Java 21?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Java 21, released in September 2023, introduced several noteworthy features and enhancements:

- **Pattern Matching for Switch (Preview Feature):** This allows developers to use patterns in switch expressions and statements, enabling more concise and safer code by handling multiple types and structures.
- **Record Patterns (Preview Feature):** It enhances Java's pattern matching capabilities, allowing developers to match records in a more expressive way, simplifying the deconstruction of record types.
- **Virtual Threads (Preview Feature):** Introduces lightweight, non-blocking threads that simplify concurrent programming and improve scalability.
- **Scoped Values (Preview Feature):** Provides a new way to define values that are scoped to a particular control flow, enhancing the management of data in concurrent applications.
- **New APIs and Language Enhancements:** Various enhancements to existing APIs, including improvements in the **`java.util`** package, the introduction of new language features, and updates to the JVM.
- **Performance Improvements:** Ongoing optimizations that enhance the performance of Java applications, including garbage collector improvements and reductions in memory footprint.

---

## 335. How Does a Concurrent HashMap Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A **`ConcurrentHashMap`** is a thread-safe implementation of the **`Map`** interface in Java, designed for concurrent access and high performance. Here’s how it works:

- **Segmented Locking:**
    - The **`ConcurrentHashMap`** uses a technique called segmented locking or fine-grained locking. Instead of synchronizing the entire map, it divides the map into segments (buckets). Each segment can be locked independently, allowing multiple threads to access different segments simultaneously. This improves concurrency and performance.
- **Lock-Free Reads:**
    - Reads from a **`ConcurrentHashMap`** are lock-free and do not require any locking mechanism. This allows for high-performance read operations, which is beneficial when multiple threads are coming in to read data.
- **Concurrent Updates:**
    - Write operations (such as **`put`**, **`remove`**, and **`replace`**) are still thread-safe and can acquire locks only on the required segments, minimizing performance bottlenecks. However, they may block each other when trying to modify the same segment, thus providing a balance between safety and performance.
- **Size Operations:**
    - The method **`size()`** is designed to give an approximate size of the map, as maintaining an exact count could lead to performance overhead. This allows the operation to run efficiently, even with concurrent modifications.
- **Null Values:**
    - **`ConcurrentHashMap`** does not allow **`null`** keys and values, which helps avoid ambiguity in a concurrent environment while maintaining consistency in operations.
- **Atomic Operations:**
    - It provides atomic operations like **`putIfAbsent()`**, **`remove()`**, and **`replace()`**. These methods ensure that certain conditions are met when operating on the map and are implemented using lock-free techniques where possible.

---

## 336. Which is More Efficient: Synchronized HashMap or ConcurrentHashMap? Why?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**ConcurrentHashMap is more efficient than a synchronized HashMap.**

1. **Granular Locking**:
    - **`ConcurrentHashMap`** uses a technique called segmented locking or fine-grained locking, allowing multiple threads to operate on different segments of the map concurrently. This segments the internal structure of the map, which means that a thread can work with one segment without blocking other threads that want to access different segments.
    - In contrast, a synchronized **`HashMap`** uses a single lock for the entire map, which means all thread access is serialized. This can lead to significant contention and bottlenecks when multiple threads try to read or write simultaneously.
2. **Performance**:
    - Because **`ConcurrentHashMap`** allows concurrent read and write operations and does not lock the entire structure during read operations, it typically offers better performance in multi-threaded applications, especially where reads are common.
    - Synchronized **`HashMap`** can severely degrade performance as the number of threads increases due to the locking overhead.
3. **Functional Differences**:
    - **`ConcurrentHashMap`** does not allow **`null`** keys or values, and this guarantees the integrity of the data structure in concurrent scenarios. Synchronized **`HashMap`**, on the other hand, does allow nulls, which can lead to ambiguity.

---

## 337. What is a Linked List?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A **linked list** is a data structure that consists of a sequence of elements, where each element is a separate object. Each element (commonly referred to as a "node") contains two parts:

- **Data:** The value or information stored in the node.
- **Pointer (or Reference):** A reference to the next node in the sequence.

Linked lists can be:

- **Singly Linked List:** Each node points to the next node, and the last node points to null.
- **Doubly Linked List:** Each node has two references, one to the next node and one to the previous node.
- **Circular Linked List:** The last node points back to the first node instead of pointing to null.

---

## 338. How Does a Linked List Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A linked list works by using nodes linked together in a sequence:

- **Insertion:** When inserting a new node, you just need to update the pointer of the node that precedes the new node to point to the new node, and the new node's pointer should point to the next node in the sequence. This allows for efficient inserts without needing to shift other elements (as in an array).
- **Deletion:** For deletion, you adjust the pointers of the neighboring nodes to bypass the node being deleted, allowing the memory used by the deleted node to be reclaimed by the garbage collector (in languages with automatic memory management) or manually deallocated.
- **Traversal:** To access elements, you start from the head (first node) and traverse the list by following the next pointers until you reach a node that points to null (or the end of the list).

---

## 339. How Do You Implement a Linked List?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Here is a simple implementation of a singly linked list in Java:

```jsx
class LinkedList {
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head; // Head of the list
    
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode; // Inserting the first node
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next; // Traverse to the end of the list
            }
            current.next = newNode; // Add the new node at the end
        }
    }

    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next; // Move to the next node
        }
        System.out.println("null"); // End of the list
    }

    public void delete(int data) {
        if (head == null) return; // List is empty

        if (head.data == data) {
            head = head.next; // Remove the head node
            return;
        }

        Node current = head;
        while (current.next != null) {
            if (current.next.data == data) {
                current.next = current.next.next; // Bypass the node to delete
                return;
            }
            current = current.next;
        }
    }

    // Additional methods for searching, updating, etc. can be implemented here
}
```

---

## 340. How to Insert Elements in the Middle of a Linked List?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

To insert an element in the middle of a linked list, you need to:

1. **Traverse to the Desired Position:** Start at the head of the list and navigate to the node just before the desired insertion point. You need to maintain a reference to the previous node.
2. **Create a New Node:** Create a new node containing the data you want to insert.
3. **Adjust Pointers:**
    - Set the new node's **`next`** pointer to point to the current node (which is currently at the desired position).
    - Set the previous node's **`next`** pointer to point to the new node, effectively inserting it into the list.

```jsx
class LinkedList {
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    // Method to insert a node at a specific position
    public void insertAt(int data, int position) {
        Node newNode = new Node(data);

        if (position == 0) {
            // Insert at head
            newNode.next = head;
            head = newNode;
            return;
        }

        Node current = head;
        for (int i = 0; i < position - 1; i++) {
            if (current == null) {
                throw new IndexOutOfBoundsException("Position exceeds list size");
            }
            current = current.next;
        }

        newNode.next = current.next; // Point new node to next node
        current.next = newNode;       // Point previous node to new node
    }

    // Method to display the linked list
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}
```

---

## 341. Have You Ever Worked on Multi-Threading?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Yes, I have experience working with multi-threading in Java. In my projects, I have used multi-threading to perform concurrent tasks to improve application performance and responsiveness. For example, I have implemented multi-threading for:

- **Parallel Processing:** Handling multiple independent tasks simultaneously, such as processing multiple user requests or background jobs to optimize resource utilization.
- **Executor Framework:** Utilizing the Executor framework to manage thread pools, including creating thread pools for executing tasks asynchronously and efficiently.
- **Synchronization:** Implementing synchronization techniques to handle shared resources safely, avoiding race conditions and ensuring data consistency.

---

## 342. What is an Executor Framework?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

The **Executor framework** in Java provides a high-level mechanism for managing concurrent tasks. It simplifies the process of using threads, allowing developers to manage thread creation, execution, and lifecycle more effectively. The main components of the Executor framework include:

- **Executor Interface:** The simplest interface with a single method **`execute(Runnable command)`** for running tasks.
- **ExecutorService Interface:** Extends the Executor interface and adds methods for managing the lifecycle and returning results of asynchronous computations.
- **ThreadPoolExecutor:** A commonly used implementation of **`ExecutorService`** that creates and manages a pool of threads for executing tasks.
- **ScheduledExecutorService:** Extends **`ExecutorService`** and allows scheduling of tasks to run after a specified delay or periodically.

The framework promotes a task-based approach instead of explicitly managing thread creation and lifecycle, improving performance and resource management.

---

## 343. How and Where Did You Use a CompletableFuture?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

I have used **CompletableFuture** in scenarios where I needed to handle asynchronous programming more easily and manage the completion of multiple tasks. Some specific cases include:

1. **Asynchronous Computations:** When performing tasks that are independent and can run concurrently, such as fetching data from multiple APIs, I used **`CompletableFuture`** to execute these tasks asynchronously and combine their results.

```jsx
CompletableFuture<DataType1> future1 = CompletableFuture.supplyAsync(() -> {
    // Task to fetch data from API 1
});

CompletableFuture<DataType2> future2 = CompletableFuture.supplyAsync(() -> {
    // Task to fetch data from API 2
});

CompletableFuture<ResultType> combinedFuture = future1.thenCombine(future2, (data1, data2) -> {
    // Combine results from both futures
});
```

1. **Chaining Tasks:** By using methods like **`thenApply`**, **`thenAccept`**, or **`thenCompose`**, I was able to create a pipeline of tasks that would execute in sequence, depending on the results of previous tasks.
2. **Error Handling:** With **`CompletableFuture`**, I implemented error handling through methods like **`exceptionally`** and **`handle`**. This allows me to manage failures in asynchronous computations gracefully without breaking the flow of the application.

```jsx
CompletableFuture<DataType1> future = CompletableFuture.supplyAsync(() -> {
    // Some computation that may fail
    if (conditionFails) {
        throw new RuntimeException("Error occurred!");
    }
    return result;
}).exceptionally(ex -> {
    // Handle the exception, return a default value or perform some logging
    System.out.println("Handling error: " + ex.getMessage());
    return defaultValue;
});
```

1. **Combining Multiple Futures:** When I needed to wait for multiple futures to complete before proceeding, I used **`allOf`** or **`anyOf`** methods to aggregate results effectively. This allowed me to execute subsequent logic only once all necessary tasks were completed.

```jsx
CompletableFuture<Void> allOf = CompletableFuture.allOf(future1, future2);
allOf.thenRun(() -> {
    // All tasks are completed, proceed with the next steps
    System.out.println("All tasks completed!");
});
```

---

## 344. What is the Memory in Which Objects are Created in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In Java, objects are primarily created in the **Heap Memory**. Here are the details of memory allocation for objects:

1. **Heap Memory:**
    - **Dynamic Memory Allocation:** The heap is where all class instances (objects) and arrays are stored. Memory for these objects is allocated dynamically at runtime when they are instantiated using the **`new`** keyword.
    - **Garbage Collection:** Objects in the heap are eligible for garbage collection when there are no more references to them. The Java Garbage Collector automatically frees up memory by reclaiming space from unreachable objects.
2. **Memory Structure:**
    - The heap is typically divided into two parts:
        - **Young Generation:** Where newly created objects are allocated. It includes the Eden space and two survivor spaces. Objects that survive young generation collections may move to the old generation.
        - **Old Generation:** Where long-lived objects that survive multiple garbage collections reside.
3. **Stack Memory:**
    - While objects themselves are stored in the heap, variables of primitive types and references to objects are stored in **Stack Memory**. Each thread has its own stack memory, containing method calls, local variables, and references to objects in the heap.

---

## 345. What is a Bean in Spring Boot?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In Spring Boot (and Spring in general), a **bean** is an object that is instantiated, assembled, and managed by the Spring IoC (Inversion of Control) container. Beans are the backbone of a Spring application and typically represent business components, services, or repositories.

---

## 346. How Does the IoC Container Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

The **IoC (Inversion of Control) container** is a core component of the Spring framework responsible for managing the beans in a Spring application. Here's how it works:

1. **Configuration**: The IoC container needs a configuration source that defines the beans and their dependencies. This can be done through XML, Java annotations (using **`@Configuration`**), or Java-based configuration with **`@Bean`** methods.
2. **Container Initialization**: When the Spring application starts, the IoC container is initialized. During this phase, it reads the configuration file or class and prepares to create the beans as defined.
3. **Bean Instantiation**: The container creates instances of the defined beans and resolves their dependencies. This is done using reflection to call the constructors and inject any required dependencies.
4. **Bean Lifecycle Management**: The container manages the complete lifecycle of the bean, from creation to destruction. It can handle initialization callbacks (using **`@PostConstruct`** or **`InitializingBean`**) and destruction callbacks (using **`@PreDestroy`** or **`DisposableBean`**).
5. **Dependency Injection**: The IoC container injects the required dependencies into beans. This can be done via constructor injection, setter injection, or field injection. By controlling the dependencies, Spring promotes loose coupling and easier management of complex applications.

**Example of IoC with Constructor Injection:**

```jsx
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class OrderService {
    private final UserService userService;

    @Autowired
    public OrderService(UserService userService) {
        this.userService = userService;
    }
}
```

---

## 347. In Which Memory Do Spring Beans Are Created?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Spring beans are primarily created in the **Heap Memory** of the Java Virtual Machine (JVM). Here’s how and where they are stored:

1. **Heap Memory**: When a Spring application is running, all beans declared will reside in the heap memory and are eligible for garbage collection when they are no longer referenced.
2. **Bean Scope**:
    - Beans can have various scopes (e.g., singleton, prototype, request, session):
        - **Singleton:** A single instance per Spring container. The same bean reference is returned every time it is requested from the container.
        - **Prototype:** A new instance is created each time the bean is requested.
        - **Request:** A new bean instance is created for each HTTP request (used in web applications).
        - **Session:** A new bean instance is created for each HTTP session (used in web applications).
3. **Memory Management**: The management of heap memory and the lifecycle of beans is handled by the Spring IoC container, which allocates memory for the beans when they are instantiated and deallocates it when they are no longer needed.

---

## 348. Write a program to sort all elements in ascending order and all zeros must be put at the end. Make sure that the solution is optimal in terms of time complexity?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

To sort an array such that all non-zero elements are in ascending order, and all zeros are moved to the end, you can implement an optimal solution with a time complexity of O(n). Here’s a step-by-step approach using a two-pass technique:

**Algorithm:**

1. **Traverse the Array:**
    - Use a separate list to store non-zero elements.
2. **Count Zeros:**
    - Count the number of zeros present in the array.
3. **Sort Non-Zero Elements:**
    - Sort the list of non-zero elements.
4. **Construct Final Array:**
    - Append the counted zeros to the end of the sorted non-zero elements.

Here’s the implementation in Java:

```jsx
import java.util.Arrays;

public class SortArray {
    public static void main(String[] args) {
        int[] arr = {0, 3, 5, 0, 2, 0, 1, 4};
        sortAndMoveZeros(arr);
        System.out.println(Arrays.toString(arr)); // Output: [1, 2, 3, 4, 5, 0, 0, 0]
    }

    public static void sortAndMoveZeros(int[] arr) {
        // Step 1: Create a list to hold non-zero elements
        int[] nonZeroElements = new int[arr.length];
        int nonZeroCount = 0;

        // Step 2: Traverse the array and collect non-zero elements
        for (int num : arr) {
            if (num != 0) {
                nonZeroElements[nonZeroCount++] = num;
            }
        }

        // Step 3: Sort the non-zero elements
        Arrays.sort(nonZeroElements, 0, nonZeroCount); // Sort only the non-zero part

        // Step 4: Fill the original array with sorted non-zero elements and zeros at the end
        int index = 0;
        for (int i = 0; i < nonZeroCount; i++) {
            arr[index++] = nonZeroElements[i];
        }
        
        // Fill the remaining part of the array with zeros
        while (index < arr.length) {
            arr[index++] = 0;
        }
    }
}
```

**Explanation of the Code:**

1. **Array Traversal:**
    - The code first traverses the input array, storing all non-zero elements in a separate array called **`nonZeroElements`**. It also counts the number of non-zero elements.
2. **Sorting:**
    - Once non-zero elements are collected, **`Arrays.sort()`** is called to sort the non-zero elements in ascending order.
    1. **Final Array Construction:**
    - The original array is then filled with the sorted non-zero elements followed by the necessary number of zeros, ensuring all zeros are at the end.
    
**Complexity Analysis:**
    
    - **Time Complexity:** O(n) for the first pass to collect non-zeros, O(k log k) for sorting the **`k`** non-zero elements, where **`k`** is the count of non-zero elements. In the worst case, if all elements are non-zero, this would still be O(n log n). However, since we know we are primarily focused on keeping zeros at the end, the practical complexity remains efficient.
    - **Space Complexity:** O(n) for storing non-zero elements, which is acceptable given the constraints.

---

## 349. What is @Transactional and How Does It Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**`@Transactional`** is an annotation in the Spring framework used to manage transaction boundaries declaratively. It is part of Spring's transaction management feature, allowing developers to define the scope of a transactional operation easily. This annotation can be applied at the class or method level.

**Key Concepts of @Transactional:**

1. **Transaction Management:**
    - A transaction is a sequence of operations that are executed as a single unit of work. If any operation fails, the entire transaction can be rolled back, ensuring data integrity.
2. **Propagation:**
    - The **`propagation`** attribute of **`@Transactional`** specifies how the transaction behaves in relation to existing transactions. Common options include:
        - **`REQUIRED`** (default): Joins an existing transaction or creates a new one if none exists.
        - **`REQUIRES_NEW`**: Always begins a new transaction, suspending the current one.
3. **Isolation Levels:**
    - The **`isolation`** attribute defines how transaction integrity is visible to other transactions. Spring supports different isolation levels like **`READ_COMMITTED`**, **`SERIALIZABLE`**, etc.
4. **Rollback Rules:**
    - The **`rollbackFor`** and **`noRollbackFor`** attributes specify which exceptions should trigger a rollback of the transaction.
5. **Default Behavior:**
    - By default, Spring will rollback on unchecked exceptions (i.e., **`RuntimeException`** and subclasses) but not on checked exceptions.

**How It Works:**

When a method is annotated with **`@Transactional`**, Spring performs the following:

1. **Transaction Creation:**
    - When the method is invoked, Spring checks if there is an existing transaction. If not, it creates a new transaction.
2. **Execution of Business Logic:**
    - The method’s business logic is executed. If an unchecked exception occurs, the transaction will be marked for rollback.
3. **Transaction Commit/Rollback:**
    - If the method completes successfully, Spring commits the transaction. If it encounters an exception indicated as a rollback condition, it rolls back the changes.

---

## 350. How Will Transactions Behave When There Are Multiple Operations?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

If your transaction consists of multiple parts, such as:

1. **Insert an Entity**
2. **Call a Third-Party API with the Primary Key**
3. **Update the Same Row That Was Inserted**

Here's how the transaction would behave with respect to each operation:

1. **Transactional Scope:**
    - Assuming the entire sequence (insert, API call, and update) is annotated with **`@Transactional`**, all operations are part of the same transaction context.
    
2. **Insert Operation:**
    - When the entity is inserted, the primary key (if generated) is created, and the state is stored in the database but not yet committed.
3. **API Call:**
    - While calling a third-party API, if the API call fails (throws an unchecked exception) or if there's a timeout, the transaction is marked for rollback. No changes made during the transaction, including the insert operation, will be committed.
4. **Update Operation:**
    - If the API call succeeds and the update is performed, both the insert and the update changes are still pending commit. If everything goes well, Spring will commit all changes at the end. If any error occurs before the transaction completes, none of the changes will reflect in the database.
5. **Exception Handling:**
    - If you need to handle exceptions properly, and prevent rolling back on certain exceptions (like those thrown by the API call), you can use the **`noRollbackFor`** attribute:

```jsx
@Transactional(noRollbackFor = ApiException.class)
public void manageData() {
    // Insert operation
    myRepository.save(entity);

    // Call to third-party service
    thirdPartyService.callApi(entity.getId());

    // Update operation
    myRepository.update(entity);
}
```

**Summary**

The **`@Transactional`** annotation in Spring manages transactions declaratively, ensuring atomicity and data integrity in operations. When performing multiple operations in a transaction, if any part fails, Spring handles the rollback automatically, ensuring no partial updates are applied. This behavior is essential for maintaining a consistent state in applications that interact with databases and external systems. Understanding transaction management is crucial for building reliable Java applications. If you have further questions or need clarifications on any related topics, feel free to ask!

---

## 351. What components have you used in AWS and Azure?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

When discussing components used in AWS (Amazon Web Services) and Azure (Microsoft Azure), it's important to specify both Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) offerings and how they fit into your projects. Here's a structured response that highlights key components:

**AWS Components**

1. **Compute Services:**
    - **Amazon EC2 (Elastic Compute Cloud):** Used for scalable virtual server instances for hosting applications.
    - **AWS Lambda:** Serverless computing that enables running code in response to events without provisioning servers.
2. **Storage Services:**
    - **Amazon S3 (Simple Storage Service):** Used for scalable object storage for backups, static websites, and media hosting.
    - **Amazon EBS (Elastic Block Store):** Provides block-level storage volumes for use with EC2 instances.
3. **Database Services:**
    - **Amazon RDS (Relational Database Service):** Managed database service for relational databases like MySQL, PostgreSQL, and SQL Server.
    - **Amazon DynamoDB:** NoSQL database service for low-latency and high-throughput applications.
4. **Networking:**
    - **Amazon VPC (Virtual Private Cloud):** Used to create isolated networks within the AWS cloud.
    - **AWS Route 53:** Scalable Domain Name System (DNS) service for routing users to applications.
5. **Monitoring and Management:**
    - **Amazon CloudWatch:** Monitoring and logging service to observe resource utilization, application performance, and operational health.
    - **AWS CloudTrail:** Tracks user activity and API usage across AWS infrastructure for compliance and auditing purposes.
6. **Deployment and CI/CD:**
    - **AWS CodePipeline:** Continuous integration and continuous delivery (CI/CD) service for automating release pipelines.
    - **AWS Elastic Beanstalk:** Platform for deploying and managing applications without worrying about the underlying infrastructure.

**Azure Components**

1. **Compute Services:**
    - **Azure Virtual Machines:** Provisioning scalable virtualized server instances.
    - **Azure Functions:** Serverless computing solution for running event-driven code.
2. **Storage Services:**
    - **Azure Blob Storage:** Used for storing unstructured data, such as images, videos, and backups.
    - **Azure Files:** Managed file shares in the cloud, accessible via the SMB protocol.
3. **Database Services:**
    - **Azure SQL Database:** Managed relational database service based on SQL Server.
    - **Azure Cosmos DB:** Globally distributed NoSQL database service for building modern applications.
4. **Networking:**
    - **Azure Virtual Network (VNet):** Used to create isolated networks within Azure for security and organization.
    - **Azure DNS:** Hosting domain names for your applications and enabling DNS resolution.
5. **Monitoring and Management:**
    - **Azure Monitor:** Offers comprehensive monitoring and diagnostics across applications and services.
    - **Azure Log Analytics:** Aggregates and analyzes data gathered from various sources for insights and alerts.
6. **Deployment and CI/CD:**
    - **Azure DevOps Services:** Provides tools for version control, CI/CD pipelines, testing, and collaboration.
    - **Azure App Service:** Hosting platform for building web apps, mobile app backends, and RESTful APIs.

**Conclusion**

In my experience, I have utilized these components in various projects aimed at building scalable applications, enhancing performance, and ensuring high availability. I have effectively managed infrastructure and services in both AWS and Azure, adapting to the specific requirements of each application.

If you would like more specific examples of how I've used these services in my work or have any further questions, please feel free to ask!

---

## 352. Design an ordering system. Which type of databases will you use?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Designing an ordering system requires careful consideration of various components, including user requirements, scalability, performance, and data management. Below is a high-level overview of how to design such a system, along with recommendations for the types of databases to use.

**High-Level Design of an Ordering System**

**Components of the Ordering System:**

1. **User Interface:**
    - Web and/or mobile application for users to browse products, place orders, and view order history.
2. **Order Processing:**
    - Service that manages the logic related to order creation, updates, payment processing, and notification.
3. **Inventory Management:**
    - Service to handle product availability, stock levels, and reordering processes.
4. **Payment Gateway:**
    - Integration with external payment services to handle transactions securely.
5. **Notification Service:**
    - Service to send notifications via email, SMS, or push notifications regarding order status updates.
6. **Admin Dashboard:**
    - Interface for administrators to manage products, view orders, and analyze sales metrics.

**Database Selection**

When designing the ordering system, the choice of databases will depend on the specific requirements, such as scalability, data consistency, and the types of queries being executed. Here’s how you could organize the data:

1. **Relational Database (e.g., PostgreSQL, MySQL):**
    - **Use Case:** This can serve as the main database for handling structured data such as user information, product details, orders, and transactions. These databases offer:
        - Strong ACID (Atomicity, Consistency, Isolation, Durability) compliance, which is crucial for order processing.
        - Well-defined relationships between entities (Users, Orders, Products).
    - **Example Schema:**
        - **User Table:** Stores user details (user ID, name, email, etc.).
        - **Product Table:** Stores product details (product ID, name, description, price, stock level).
        - **Order Table:** Stores order details (order ID, user ID, total amount, order status, timestamps).
        - **Order Item Table:** Stores the individual items in each order (order item ID, order ID, product ID, quantity).
2. **NoSQL Database (e.g., MongoDB, DynamoDB):**
    - **Use Case:** This can complement the relational database, especially for handling unstructured data, such as user activity logs, product reviews, or shopping cart data. NoSQL databases provide:
        - Flexibility in data models, which allows for rapid changes without requiring schema migrations.
        - Scalability and high availability for handling a large amount of data.
    - **Example Usage:** Store documents relevant to user sessions (e.g., shopping cart) or product recommendations based on user behavior.
3. **Caching Layer (e.g., Redis or Memcached):**
    - **Use Case:** Use caching to improve performance and reduce load on the relational database for frequently accessed data, such as product details and user sessions. This can be critical for quick response times and high concurrency when users retrieve product data.
    - **Benefits:** Reduces database queries and serves data quickly, enhancing the overall performance of the ordering system
    

**Other Considerations**

- **Transaction Management:**
    - Ensure that order creation and payment processes are handled in a transactional manner to maintain data consistency.
- **Microservices Architecture:**
    - Consider adopting a microservices architecture to separate the ordering service, payment service, and inventory service. Each service can use its own database tailored to its specific needs.
- **Scalability and Redundancy:**
    - Design the system to easily scale horizontally to handle increased load. Use load balancers and replicas to ensure high availability and redundancy.
- **Data Backup and Recovery:**
    - Implement regular data backups and recovery strategies to prevent data loss, especially for critical transaction data.

**Conclusion**

The ordering system can be efficiently designed using a combination of relational and NoSQL databases, coupled with caching mechanisms. This hybrid approach allows the system to leverage the strengths of each database type, ensuring robustness, scalability, and high performance while managing structured and unstructured data effectively. If you have any specific requirements or want to explore certain areas in more detail, feel free to ask!

---

## 353. What Are the Mistakes You Have Made While Learning?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

While learning, I've encountered several mistakes that have significantly contributed to my personal and professional growth. Here are a few:

- **Underestimating the Basics:** In the early stages of learning programming and frameworks, I tended to rush through foundational concepts to get to advanced topics. This often resulted in confusion later on when I faced issues that could have been resolved with a stronger grasp of the basics. I learned that a solid understanding of fundamental concepts is crucial for solving more complex problems effectively.
- **Neglecting Documentation:** Initially, I would often neglect official documentation for libraries or frameworks, preferring to rely on tutorials or examples. While these resources can be helpful, I realized that understanding the official documentation greatly improves my knowledge and helps me utilize the technology more effectively. I now make it a habit to refer to documentation for any new technology I encounter.
- **Not Seeking Help:** There were times when I struggled with a problem for too long without reaching out for help. I tended to try to solve everything on my own, which sometimes resulted in wasted time and frustration. I've since learned the importance of engaging with peers, mentoring, and online communities to find solutions quickly and share knowledge.
- **Ignoring Best Practices:** In my early projects, I sometimes did not follow best coding practices or design patterns, thinking they were not critical in smaller projects. However, as projects grew more complex, this led to issues with maintainability and scalability. This mistake taught me the value of adhering to best practices from the start.

---

## 354. What Are the Challenges You Have Taken Up in the Last 6 Months?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In the last six months, I have actively sought out challenges that have pushed me to grow, both technically and personally:

- **Learning a New Framework:** I took on the challenge of learning **Spring Boot** (or any relevant framework or technology). This involved building a small project from scratch, which helped deepen my understanding of microservices architecture, dependency injection, and RESTful API design.
- **Contributing to Open Source:** I contributed to an open-source project that involved bug fixes and feature enhancements. This experience taught me about collaborating with other developers, understanding project workflows, and navigating version control systems like Git effectively.
- **Leading a Team Project:** I was given the opportunity to lead a small team of developers for a project aimed at optimizing our existing application. This role required me to manage tasks, facilitate communication, and ensure that we met our deadlines. It was a valuable experience in leadership and teamwork.
- **Improving Code Review Practices:** I took on the challenge of not only participating in code reviews but also refining our team's code review process to ensure higher code quality. This included creating guidelines for code quality, writing better commit messages, and encouraging constructive feedback among team members.
- **Exploring Cloud Technologies:** To stay current with industry trends, I dedicated time to learning about cloud platforms, specifically **AWS** and **Azure**. I completed several hands-on projects focusing on deploying applications in a cloud environment, which improved my understanding of cloud services and DevOps practices.

**Conclusion**

Reflecting on mistakes made while learning has allowed me to grow and be more efficient in my approach to development. Moreover, embracing challenges over the past six months has helped me enhance my technical skills, improve my teamwork abilities, and become a more confident developer. I'm always eager to learn from experiences and take on new challenges moving forward.

---

## 355. Did You Ever Receive Any Constructive Feedback from Your Management? Give an Example.

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Yes, I have received constructive feedback from my management during my time in [current/previous job]. One instance that stands out was after a major project delivery. My manager highlighted that while my technical skills were strong, there were areas where I could improve communication with stakeholders throughout the project lifecycle.

**Example:** During one particular project, I tended to focus heavily on development without providing frequent updates to the stakeholders. My manager encouraged me to set up regular check-ins and progress updates. This feedback helped me understand the importance of transparency and keeping all parties informed. Since then, I started scheduling weekly updates, which not only improved stakeholder satisfaction but also facilitated early detection of any potential issues.

---

## 356. Do You Know HTML? What About CSS?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Yes, I have a working knowledge of both HTML and CSS.

- **HTML:** I am familiar with HTML5, and I am comfortable with structuring web pages using various HTML elements. I understand the semantic structure and accessibility considerations, and I can create forms, tables, and other interactive elements.
- **CSS:** I also have a solid understanding of CSS, including CSS3 features such as Flexbox and Grid for layout design. I am skilled in styling web pages, creating responsive designs, and using preprocessors such as SASS or LESS. I aim to apply best practices to ensure cross-browser compatibility and efficient styles.

---

## 357. Why Are You Looking for a Change?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

I am looking for a change because I am eager to further advance my career and take on new challenges that align with my long-term professional goals. While I have learned and grown in my current role, I feel that I have reached a point where I am ready to take on more responsibility and contribute to larger projects.

I am particularly interested in opportunities that allow me to work with cutting-edge technologies and methodologies, as well as roles that value collaboration and innovation. I am drawn to your organization because of [mention a specific reason related to the company, such as its commitment to technology, innovative projects, company values, or professional development opportunities].

**Conclusion**

By structuring your responses in a clear and concise manner, you can effectively convey your experiences, skills, and motivations to potential employers. Tailoring your answers to highlight your strengths and align them with the organization's goals will help leave a positive impression during the interview process. If you have further questions or need additional clarification on any topics, feel free to ask!

---

## 358. How Good Are You with Java Data Structures?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

I have a solid understanding of Java data structures and their implementations. I am comfortable with various data structures, including lists, sets, maps, and queues. I have utilized these collections in numerous projects to efficiently manage and manipulate data while ensuring optimal performance based on the specific requirements of each application

---

## 359. What is a Set?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In Java, a **Set** is a collection that does not allow duplicate elements. It models the mathematical set abstraction and is an interface in the Java Collections Framework. Key characteristics of a Set include:

- **No Duplicates:** A Set automatically ensures that no two elements are the same. If you attempt to add a duplicate element, it will not be added.
- **Unordered:** The elements in a Set are not stored in any particular order. Thus, the order of iteration may differ from the order in which elements were added.
- **Common Implementations:** The commonly used implementations of the Set interface are **`HashSet`**, **`LinkedHashSet`**, and **`TreeSet`**.

---

## 360. What is a TreeSet?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A **TreeSet** is a specific implementation of the Set interface that uses a binary search tree (specifically a Red-Black tree) to store its elements. Here are some key characteristics of a TreeSet:

- **Sorted Order:** Elements in a TreeSet are sorted in their natural order, or according to a provided comparator at the time of creation. This allows for ordered traversal of elements.
- **No Duplicates:** Similar to other sets, TreeSet does not allow duplicate elements. If you try to add a duplicate, it will simply ignore the new entry.
- **Performance:**
    - The basic operations (such as add, remove, and contains) have a time complexity of O(log n) due to the underlying tree structure, which provides efficient searching and sorting.
    - **NavigableSet Interface:** TreeSet implements the **`NavigableSet`** interface, allowing you to perform navigation operations like getting the greatest or least element, subsetting, and more advanced querying that other Set implementations may not provide.
    
    **Example of Using TreeSet:**
    
    ```jsx
    import java.util.TreeSet;
    
    public class TreeSetExample {
        public static void main(String[] args) {
            TreeSet<Integer> treeSet = new TreeSet<>();
            
            // Adding elements
            treeSet.add(10);
            treeSet.add(5);
            treeSet.add(15);
            treeSet.add(10); // Duplicate, will be ignored
         
            // Display the elements in sorted order
            System.out.println("TreeSet: " + treeSet); // Output: TreeSet: [5, 10, 15]
        }
    }
    ```

---

## 361. How Do floor() and ceiling() Methods Work in a TreeSet?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

In a **`TreeSet`**, which implements the **`NavigableSet`** interface, the methods **`floor()`** and **`ceiling()`** are used to retrieve elements based on ordering:

- **`floor(E e)`**: This method returns the greatest element in the set that is less than or equal to the given element. If there is no such element, it returns **`null`**.
    
    **Example:**
    
    ```jsx
    TreeSet<Integer> treeSet = new TreeSet<>();
    treeSet.add(10);
    treeSet.add(20);
    treeSet.add(30);
    
    Integer value1 = treeSet.floor(25); // Returns 20
    Integer value2 = treeSet.floor(10); // Returns 10
    Integer value3 = treeSet.floor(5); // Returns null
    ```
    
    **`ceiling(E e)`**: This method returns the smallest element in the set that is greater than or equal to the given element. If there is no such element, it returns **`null`**.
    
    **Example:**
    
    ```jsx
    Integer value4 = treeSet.ceiling(25); // Returns 30
    Integer value5 = treeSet.ceiling(20); // Returns 20
    Integer value6 = treeSet.ceiling(35); // Returns null
    ```
    
    Both methods utilize the sorted nature of the **`TreeSet`** to perform efficient searches

---

## 362. What is a List? What Are the Different Kinds of Lists in Java?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A **List** in Java is an ordered collection that can contain duplicate elements. Lists provide control over the position of each element and allow for retrieval, insertion, and removal by index.
    
**Different Kinds of Lists in Java:**
    
    1. **ArrayList:**
        - A resizable array implementation of the List interface. It allows for fast random access and dynamically adjusts its size. It is not synchronized, making it suitable for use in single-threaded scenarios.
        - **Performance:** Faster for random access and iteration, but slower for inserting and deleting elements compared to linked lists.

```jsx
List<String> arrayList = new ArrayList<>();
arrayList.add("A");
arrayList.add("B");
```

**LinkedList:**

- A doubly linked list implementation of the List interface. It allows for insertion and removal of elements from both ends and is more efficient for such operations than ArrayList.
- **Performance:** Slower for random access due to traversal but faster for inserts and deletes at the beginning or middle of the list.

```jsx
List<String> linkedList = new LinkedList<>();
linkedList.add("A");
linkedList.add("B");
```

**Vector:**

- Synchronized dynamic array implementation that is similar to ArrayList. It is thread-safe, making it suitable for use in multi-threaded environments but at the cost of performance due to synchronization overhead.

```jsx
List<String> vectorList = new Vector<>();
vectorList.add("A");
vectorList.add("B");
```

**Stack:**

- A subclass of Vector that implements a last-in, first-out (LIFO) data structure.

```jsx
Stack<Integer> stack = new Stack<>();
stack.push(1);
stack.push(2);
```

---

## 363. When to Use a Linked List? When to Use an ArrayList?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**When to Use a Linked List:**

- **Frequent Insertions/Deletions:** If your application requires frequent additions or deletions of elements beyond the last position (especially at the beginning or middle of the list), a **`LinkedList`** is more efficient due to its ability to rearrange pointers without shifting elements.
- **Memory Considerations:** When the size of the list is highly variable and unpredictable, using a **`LinkedList`** can be more memory efficient as it does not require contiguous memory space.
- **Implementation of Queues:** If you are implementing a queue data structure, **`LinkedList`** provides a natural way to do so as it can efficiently handle both ends (insertion and deletion).

---

## 364. What is a HashMap? How Does It Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**HashMap** is a part of the Java Collections Framework and is an implementation of the **`Map`** interface. It is used to store key-value pairs, allowing for efficient retrieval of values based on their corresponding keys.

**Key Characteristics of HashMap:**

1. **Key-Value Pairing:** Each entry in a HashMap consists of a key and a value, where the key must be unique.
2. **No Duplicates:** A HashMap does not allow duplicate keys. If the same key is inserted again, it will overwrite the existing key-value pair.
3. **Dynamic Resizing:** HashMap automatically resizes when the number of entries exceeds a certain threshold (generally when the number of entries exceeds the current capacity multiplied by the load factor).
4. **Order of Elements:** The elements are not stored in any specific order. The order may even change when new entries are added.

---

## 365. How Does It Work?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

1. **Hash Function:**
    - HashMap uses a hash function to compute an index (hash code) for each key. The key is processed by the hash function, which determines where to store the value in the underlying array.
2. **Buckets:**
    - The underlying structure of a HashMap is an array of buckets. Each bucket can hold multiple entries (key-value pairs) that hash to the same index.
3. **Collision Resolution:**
    - If two keys hash to the same index (a collision), the HashMap handles it using a linked list or, beginning with Java 8, a balanced tree (e.g., Red-Black Tree) if the number of collisions at a single index exceeds a certain threshold (typically, when the number of entries in a bucket exceeds 8).
    - This helps keep the performance of the HashMap efficient during lookups, insertions, and deletions.
4. **Load Factor and Capacity:**
    - The load factor is a measure of how full the HashMap can get before it needs to resize. The default load factor is 0.75, meaning the map will resize when it reaches 75% of its capacity.
    - When resizing occurs, the new capacity is usually double the current capacity.
5. **Access Time Complexity:**
    - The average time complexity for operations (insertion, deletion, and retrieval) is O(1), assuming a good hash function that evenly distributes the keys across the buckets. However, in the worst case (e.g., when many collisions occur), the time complexity can degrade to O(n).

---

## 366. What is a Red-Black Tree? What Do You Know About Its Implementation?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

A **Red-Black Tree** is a type of self-balancing binary search tree that ensures that the tree remains approximately balanced during insertions and deletions. It reduces the worst-case time complexity for operations (search, insert, delete) to O(log n).

**Characteristics of a Red-Black Tree:**

1. **Node Coloration:**
    - Each node is colored either red or black, which helps maintain the balance of the tree.
2. **Properties:**
    - The root must always be black.
    - Red nodes cannot have red children (i.e., no two reds in a row).
    - Every path from a node to its descendant **`null`** nodes must have the same number of black nodes.
    - A newly inserted node is always red.
3. **Balancing:**
    - The properties of the Red-Black Tree allow it to maintain balance during insertions and deletions through a series of rotations and color flips, which preserves the tree's properties while keeping the access time efficient.

**Implementation of Red-Black Tree:**

The implementation of a Red-Black Tree includes several operations:

1. **Insertion:**
    - Insert a new node like in a regular binary search tree. After insertion, adjust the tree by performing rotations and recoloring to maintain Red-Black properties.
2. **Deletion:**
    - Similar to insertion, delete a node from the tree and then rebalance it with rotations and recoloring as necessary.
3. **Traversal:**
    - In-order traversal can be done, producing a sorted list of elements.

Here’s a very simplified structure for a Red-Black Tree node in Java:

```jsx
class RedBlackNode {
    int data;
    boolean isRed; // true if the node is red
    RedBlackNode left;
    RedBlackNode right;
    RedBlackNode parent;

    public RedBlackNode(int data) {
        this.data = data;
        this.isRed = true; // New nodes are red by default
        this.left = null;
        this.right = null;
        this.parent = null;
    }
}
```

**Conclusion**

- **HashMap**: A HashMap provides an efficient key-value storage mechanism with average-case time complexity for basic operations (insert, delete, lookup) of O(1), making it suitable for applications requiring fast access to data. However, it is important to take care when choosing a good hash function to minimize collisions and ensure optimal performance. HashMap manages collisions using linked lists or trees (Red-Black Trees) when the number of entries in a bucket exceeds a certain threshold, enhancing performance and maintaining efficiency even with a large number of entries.
- **Red-Black Tree**: A Red-Black Tree is a versatile dictionary implementation that maintains a balanced binary search tree structure, ensuring O(log n) time complexity for search, insertion, and deletion operations. Its properties prevent degeneration of the tree's height and guarantee balanced access times. The use of red and black coloring, along with rotations and color changes, allows it to rebalance itself effectively during modifications, making it an excellent structure for ordered data storage, such as in data sets requiring sorting or range queries.

---

## 367. What are you learning currently? What all topics of system design are you aware of?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

When discussing your current learning focus and your knowledge of system design, it’s beneficial to articulate both what you are actively studying and the breadth of your understanding of system design concepts. Here’s how you can frame your response:

---

## 368. What Are You Learning Currently?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Currently, I am focusing on enhancing my skills in **cloud architecture** and **microservices design**. Given the increasing importance of cloud-native applications, I am learning about:

- **Microservices Architecture:** Understanding how to design, develop, and deploy microservices, including the best practices for building scalable and maintainable services.
- **Containerization and Orchestration:** Gaining hands-on experience with Docker and Kubernetes to better understand how to manage, scale, and deploy applications in containerized environments.
- **GraphQL vs. REST:** Exploring different API design patterns, focusing on when to use GraphQL over REST for optimal client-server interaction.
- **Event-Driven Architecture:** Learning how to implement event-driven systems using frameworks like Kafka and RabbitMQ to ensure decoupled communication between services.

---

## 369. How do you learn something when you find a knowledge gap?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**1. Identify the Gap Clearly**

I first take time to precisely identify what it is that I don’t understand or where my knowledge is lacking. This includes determining the specific topics or skills that I need to improve.

**2. Set Learning Goals**

I define clear and achievable learning goals. For example, if I want to learn a new framework, I might set a goal to complete a tutorial or build a small project within a specific timeframe.

**3. Gather Resources**

I gather a variety of resources to aid my learning, including:

- **Books and E-books:** I look for highly recommended texts in the subject area.
- **Online Courses:** Platforms like Coursera, Udemy, or Pluralsight offer structured learning paths.
- **Documentation:** Official language or framework documentation is invaluable for in-depth understanding.
- **Tutorials and Blogs:** I seek out articles or video tutorials for practical insights and examples.

**4. Engage with the Community**

I participate in online forums (such as Stack Overflow, Reddit, or technology-specific discussion groups) or attend local meetups and workshops. Engaging with others allows me to gain different perspectives and ask questions that can clarify my understanding.

**5. Practice Through Projects**

To solidify my learning, I apply what I’ve learned by:

- **Building Small Projects:** Creating a small application or tool related to the topic helps me apply concepts in a practical context.
- **Contributing to Open Source:** Finding projects that need help allows me to learn from real-world code and collaborate with other developers.

**6. Seek Feedback and Mentorship**

After completing a project or learning exercise, I seek feedback from peers or mentors in the field. Gaining constructive criticism helps in identifying areas that might still need improvement.

**7. Review and Reflect**

I take the time to review what I have learned and reflect on how it applies to my work. I often summarize key points, create mind maps, or teach the concepts to someone else, which solidifies my understanding.

**8. Stay Updated**

Finally, I recognize that technology and best practices are always evolving. Therefore, I try to stay current by subscribing to relevant newsletters, blogs, and participating in continuous education opportunities.

---

## 370. What do you know about web hooks? Have you ever used them?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

**Webhooks** are a way for applications to provide real-time information to other applications by sending HTTP POST requests to predefined URLs when specific events occur. They are essentially user-defined HTTP callbacks that are triggered by some event (such as changes in data) and allow for event-driven communication between different systems.

**Key Characteristics of Webhooks:**

1. **Event-Driven:** Webhooks are initiated by events occurring in a system. For example, when a user uploads a file, a webhook can trigger a notification to another service.
2. **Real-Time Notifications:** They enable real-time communication between services, allowing systems to react immediately to changes or events.
3. **Easy to Implement:** Generally, implementing a webhook involves defining a URL endpoint in the receiving application and configuring the sending application to make an HTTP request to that URL whenever the specified event occurs.
4. **No Polling Required:** Unlike APIs that often require you to poll for updates, webhooks push updates to you when they occur, reducing the need for continuous requests and improving efficiency.
5. **HTTP Methods:** Typically, webhooks use HTTP POST requests, but they can also be implemented with other HTTP methods.

**Example Use Cases for Webhooks:**

- **Payment Processing:** When a payment is completed (e.g., via Stripe), Stripe can send a webhook to your application to notify you of the transaction status.
- **CI/CD Pipelines:** A CI/CD tool can send webhooks to notify a version control system (like GitHub) when a build completes.
- **Chat Notifications:** When a user sends a message in a chat application, the system can send a webhook to a bot or another service for processing.

---

## 371. Have You Ever Used Webhooks?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*

Yes, I have used webhooks in several projects to enable real-time data synchronization and notifications between different systems. Here are a couple of examples:

1. **Payment Gateway Integration:**
    - In a recent project, I integrated a payment processing system (e.g., Stripe) with our application. I set up webhooks to listen for events such as **`payment_intent.succeeded`** or **`payment_failed`**. When the payment status changes, Stripe sends a POST request to our specified webhook URL, allowing our system to update the order status accordingly.
2. **Real-Time Updates in Microservices:**
    - In another project involving microservices architecture, I used webhooks to facilitate communication between services. For instance, when a user updates their profile in one service, a webhook is triggered to notify the notification service to send an alert when the profile update is successful.

---

## 372. What is a Deadlock?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

Occurs when two or more threads hold locks and wait for each other in a **circular dependency**, causing all to freeze.

---

---

## 373. Difference Between HashMap and WeakHashMap

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Answer (Interview-Ready):**

> HashMap holds strong references to keys/values — entries remain in memory until explicitly removed.
> 
> 
> `WeakHashMap` uses **WeakReferences for keys**, which means entries can be **garbage collected** when the key is no longer in ordinary use.
> 

🔹 **Key Differences**:

| Feature | `HashMap` | `WeakHashMap` |
| --- | --- | --- |
| Key Reference | Strong | Weak (GC can reclaim when no strong refs) |
| Entry Lifetime | Until manually removed | Auto-removed when key is weakly reachable |
| GC Involvement | Not affected | Dependent on GC |
| Thread Safety | Not thread-safe | Not thread-safe |

**Real-world Use Cases**:

- Use `HashMap` for **general-purpose, non-GC-sensitive** mappings.
- Use `WeakHashMap` for things like **caching, metadata, or registry objects**, where you want entries to disappear when the key is no longer in use.

**Example**:

```jsx
Map<MyObject, String> cache = new WeakHashMap<>();

```

Given a large dataset (millions of records), how would you efficiently search for duplicate transactions?

---

## 374. Design an In-Memory Key-Value Store with TTL (Time To Live)

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Answer (Interview-Ready):**

> I’d design a store with concurrent access, TTL support, and automatic expiry.
> 
> 
> Core components would include a `ConcurrentHashMap` and a priority queue or scheduler for TTL handling.
> 

🔹 **Key Features**:

- `put(key, value, ttlInMillis)`
- `get(key)`
- Expired keys are either:
    - Removed lazily during `get`
    - Or proactively removed using a **background cleanup thread**

🔹 **Data Structure**:

```jsx
class Entry {
    String value;
    long expiryTime;
}
ConcurrentHashMap<String, Entry> store = new ConcurrentHashMap<>();
PriorityQueue<Entry> ttlQueue = new PriorityQueue<>((a, b) -> Long.compare(a.expiryTime, b.expiryTime));

```

🔹 **Approach**:

- When adding an entry, calculate expiry time (`System.currentTimeMillis() + ttl`)
- Background thread checks the earliest expiry (using `ttlQueue`) and removes expired entries from map.
- On `get`, check if current time > expiry → return null and delete.

🔹 **Optional Enhancements**:

- Use `ScheduledExecutorService` instead of a custom thread
- Support persistence or eviction policies (LRU)
- Expose metrics (memory usage, TTL hits)

**Bonus**: Libraries like **Caffeine** already do this and are highly optimized.

Multithreading & Concurrency

---

## 375. How Would You Design a Thread Pool From Scratch?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Answer (Interview-Ready):**

> A thread pool is designed to reuse a fixed number of threads to execute tasks, rather than creating a new thread for each task.
> 
> 
> Key goals are **resource reuse**, **load control**, and **task scheduling**.
>

---

## 376. How Does Java Handle False Sharing in Multi-core Processors?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Answer (Interview-Ready):**

> False sharing happens when threads on different cores modify variables that reside on the same CPU cache line, causing performance degradation due to unnecessary cache invalidations.
>

---

## 377. Question 1: What are the main drawbacks of using synchronized methods?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

Using `synchronized` methods in Java is the simplest way to handle thread-safety, but it comes with some important drawbacks:

1. **No Flexibility**:
    
    `synchronized` is a blocking mechanism with no built-in support for advanced control like try-lock or timed lock attempts. You can't try acquiring a lock without getting stuck.
    
2. **Can't Interrupt**:
    
    If a thread is waiting for a lock via `synchronized`, it cannot be interrupted. This limits responsiveness in multi-threaded applications.
    
3. **No Fairness or Priority Handling**:
    
    There's no way to control the order in which threads acquire the lock—leading to potential starvation.
    
4. **Coarse-Grained Locking**:
    
    It can sometimes lead to unnecessary locking if the scope is too wide (e.g., locking an entire method).
    
5. **No Condition Support**:
    
    You can't use multiple condition variables or fine-grained signaling like `await()`, `signal()`, or `signalAll()` which are useful in complex thread coordination.

---

## 378. Question 2: How does ReentrantLock improve performance and flexibility?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

`ReentrantLock` from `java.util.concurrent.locks` improves over `synchronized` in several ways:
    
    1. **Try and Timeout**:
        
        You can attempt to acquire the lock using `tryLock()` or `tryLock(timeout)` — improving responsiveness and avoiding deadlock.
        
    2. **Interruptibility**:
        
        Threads waiting on a `ReentrantLock` can be interrupted using `lockInterruptibly()`.
        
    3. **Fairness**:
        
        It supports **fair locking**, meaning threads acquire the lock in the order they requested it (FIFO), avoiding starvation.
        
    4. **Multiple Conditions**:
        
        Supports multiple `Condition` objects for more granular signaling between threads, improving complex thread interactions.
        
    5. **Explicit Locking**:
        
        Since locking and unlocking are explicit (`lock()` / `unlock()`), developers have more control over synchronization scope.

---

## 379. How would you design an API Gateway to handle dynamic routing and security policies?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

To design a robust **API Gateway** with **dynamic routing** and **security policy enforcement**, I'd follow a microservices-friendly and scalable approach:

---

## 380. What are the challenges of handling pagination in REST APIs for massive datasets?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

When handling **pagination at scale**, especially with **millions of records**, several challenges arise:

---

## 381. How would you manage API timeouts and retries in a distributed system?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

In a distributed system, **timeouts and retries** are critical for reliability and resilience. Here's how I approach them:

---

## 382. What’s the best way to implement WebSockets in a fintech application?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

WebSockets are great for **real-time updates** like trades, balances, or FX rates in fintech. Here's how I’d implement them securely and at scale:

---

## 383. How would you enforce idempotency in payment APIs?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

Idempotency is crucial in fintech to **avoid duplicate payments** during retries. Here's how I enforce it:

---

## 384. Design a high-throughput, low-latency order-matching system for a stock exchange

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

A **stock exchange order-matching engine** must be ultra-fast and highly reliable. Here’s a breakdown of how I’d approach it:

---

---

## 385. How would you ensure data integrity in a multi-region database setup?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

Multi-region databases are essential for global availability, but they introduce complexity in maintaining consistency. Here's how I'd ensure **data integrity**:

---

---

## 386. Write Fencing & Versioning:

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

- Use **optimistic locking / version numbers** to prevent stale writes.
- Enforce **linearizability** in critical paths (e.g., balance updates, orders).

---

---

## 387. Want to go next level?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

You can offer to sketch out:

- **Order-matching pseudocode using TreeMap in Java**
- A **multi-region write-safe schema design** (e.g., user wallet or payment ledger)
- Or even talk about **Paxos vs Raft** if asked about consensus protocols.

---

## 388. Explain Leader Election. How would you implement it in a microservices-based system?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Leader Election** is the process of designating one node (service instance) as the **"coordinator" or "primary"**, responsible for certain tasks (e.g., scheduling, resource locking, background jobs) while others stay passive or standby.

---

---

## 389. What are the trade-offs between CQRS and traditional CRUD systems?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

CQRS (Command Query Responsibility Segregation) **separates read and write models**, while traditional CRUD merges them in a single model.

---

---

## 390. How does a Distributed Message Queue like Kafka handle backpressure?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

Backpressure happens when **producers push faster than consumers can process**. Kafka handles it via **built-in flow control + buffering**.

---

---

## 391. Why a Hash Map?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

1. **Flexibility**:
    - **Hash Maps** provide **O(1)** average-time complexity for **insertion**, **deletion**, and **lookup** operations.
    - You can use **hash maps** to implement complex data structures:
        - **Sets**: By using the hash map's keys, you can simulate sets.
        - **Stacks/Queues**: Using keys for indices, you can implement a stack or queue with custom logic.
        - **Graphs**: You can represent a graph by using hash maps to store adjacency lists.
2. **Real-World Use Cases**:
    - **Caching**: A hash map is ideal for implementing **LRU (Least Recently Used)** caches where you store recently accessed data.
    - **Counting and Frequency**: You can use hash maps for counting occurrences of elements in a stream, such as counting words in a document or tracking elements in an inventory system.
    - **Mapping**: Any problem involving a **key-value pair** is perfectly suited for a hash map, including database indexing, configuration settings, and managing users with unique identifiers.
3. **Adaptability**:
    - With a **HashMap**, you can build other abstract data structures and adapt to various problem types (e.g., adjacency lists for graphs, frequency counters, etc.).

---

---

## 392. Why Remove Checked Exceptions?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

1. **Excessive Boilerplate**:
    - Java forces developers to handle checked exceptions, leading to unnecessary `try-catch` blocks and the need to declare exceptions in method signatures, which can clutter the code.
2. **Readability**:
    - Checked exceptions often obscure the logic of the program and make it harder to follow. Unchecked exceptions, on the other hand, allow the developer to focus on the actual business logic.
3. **Overuse**:
    - Developers sometimes overuse checked exceptions for cases that could be handled more cleanly with runtime exceptions or other error-handling approaches.
4. **Alternative Approaches**:
    - Languages like **Scala** and **Kotlin** (which runs on the JVM) don’t enforce checked exceptions and offer more flexible error-handling strategies, leading to cleaner code.
    - Java has introduced alternatives like **`Optional`**, **`CompletableFuture`**, and **`Result`**, which can make error handling more graceful and functional.

---

---

## 393. What is a Circuit Breaker?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

- A circuit breaker acts like an electrical circuit breaker in the physical world. It detects failures in a system, "opens" (stops sending requests to a failing service), and prevents further strain on the service, giving it time to recover.
- Once the service becomes healthy again, the circuit breaker "closes" and starts accepting requests.

**The typical behavior of a circuit breaker involves three states:**

1. **Closed**: The circuit is closed by default, meaning requests are flowing to the service. The circuit breaker monitors the service for failures.
2. **Open**: If the failure threshold is reached (e.g., multiple failed requests), the circuit breaker opens, and no further requests are sent to the service until it's deemed healthy again.
3. **Half-Open**: After a configured recovery time, the circuit breaker allows a limited number of requests to go through to test if the service has recovered. If the requests succeed, the circuit breaker closes. If they fail, it remains open.

---

## 394. Why Use Circuit Breakers?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

- **Prevent System Collapse**: When one service fails, it can trigger a cascade of failures across other services. Circuit breakers prevent this by isolating the failing service.
- **Improve Resilience**: They allow the system to gracefully degrade by providing **fallback mechanisms** (e.g., returning cached data or default responses).
- **Manage Dependencies**: Services can avoid overloading a downstream service that is experiencing issues.

---

## 395. How It Works:

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

- **Sending Messages**: A verticle can send a message to the event bus using `eventBus.send(address, message)`. The message can be any serializable object.
- **Receiving Messages**: A verticle can register a handler to receive messages from an address using `eventBus.consumer(address, handler)` for subscription-based communication.
- **Example**:

```jsx
// Sending a message to an address
vertx.eventBus().send("my.address", "Hello!");

// Receiving the message on a different verticle
vertx.eventBus().consumer("my.address", message -> {
    System.out.println("Received message: " + message.body());
});

```

---

## 396. How would you use Vert.x reactive programming to handle high-concurrency tasks?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Interview-Ready Answer:**

> “Vert.x uses a reactive, non-blocking model that allows handling high-concurrency tasks on a small number of threads through its event loop and Reactive APIs like RxJava, Mutiny, or Reactor.
> 

Here's how I would use Vert.x for high-concurrency:

🔹 **Verticles & Event Loop**:

I would split my logic into **verticles**—each component runs on a dedicated event loop. Since Vert.x uses very few threads (e.g., 2 * number of CPU cores), I’d avoid blocking calls and offload those to worker verticles.

🔹 **Reactive Programming**:
Using **Vert.x RxJava** or **Mutiny** extensions, I can compose async calls like DB queries, HTTP calls, and file reads using `flatMap`, `zip`, or `onItem().transform()`—this makes my code composable and clean.

🔹 **Backpressure-aware**:
Reactive streams like `Flowable` (RxJava) help control backpressure when dealing with large streaming data like live feeds or telemetry.

🔹 **Real Example**:

```jsx
eventBus.consumer("process.data", message -> {
    myReactiveService.processData(message.body())
        .subscribe(result -> {
            message.reply(result);
        }, err -> {
            message.fail(500, err.getMessage());
        });
});

```

By avoiding thread-per-request and using **reactive chains**, Vert.x handles **tens of thousands** of concurrent events efficiently on minimal threads.”

---

---

## 397. Explain how Vert.x handles non-blocking I/O and why it’s beneficial.

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Interview-Ready Answer:**

> “Vert.x is built on top of Netty, which is a high-performance NIO (Non-blocking I/O) framework. It uses a single-threaded event loop model where each thread handles multiple connections without blocking.
> 

🔸 **How It Works**:

- Incoming requests/events are queued in the **event loop**.
- Instead of blocking the thread waiting for I/O (e.g., DB, file, HTTP), Vert.x uses **callbacks** or **futures/promises** to resume execution when the operation completes.

🔸 **Why It’s Beneficial**:

1. **Massive concurrency**: You don’t need 1 thread per connection. One thread can handle thousands of sockets.
2. **Scalability**: Reduced context switching and memory overhead lead to better performance under high load.
3. **Resilience**: Since threads are never blocked, the system remains responsive even under peak load.

🔸 **Example**:

```jsx
webClient.get(8080, "localhost", "/data")
    .send()
    .onSuccess(response -> {
        // non-blocking response processing
    });

```

In summary, **non-blocking I/O** in Vert.x means **fewer threads, better throughput**, and **cost-efficient scaling**—making it ideal for microservices and real-time apps.”

---

---

## 398. How would you implement a distributed task scheduler using Vert.x and Redis?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

**Interview-Ready Answer:**

> “To implement a distributed task scheduler using Vert.x and Redis, I’d combine Vert.x’s Timer APIs with Redis locks to ensure only one instance processes a scheduled job in a cluster.
>

---

## 399. How would you design a rate-limiting mechanism for a public API?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “To protect a public API from abuse and ensure fair usage, I’d design a rate-limiting system using a distributed in-memory store like Redis, implementing an algorithm like Token Bucket or Leaky Bucket.”
> 

---

---

## 400. Why Redis?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

- **Distributed**: Works across multiple nodes/services.
- **Fast**: Sub-millisecond reads/writes.
- **Atomic**: Use Lua scripts for consistent updates.

---

---

## 401. What’s the difference between synchronous and asynchronous APIs?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “The difference lies in how the request is handled and when the client receives the response.”
> 

---

---

## 402. How would you design a payment gateway to handle high traffic?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “Designing a payment gateway for high traffic involves availability, idempotency, security, and low latency. I'd break it down into modular, resilient microservices with asynchronous processing and strong consistency where required.”
> 

---

---

## 403. Explain the role of message queues like Kafka or RabbitMQ in a distributed system.

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “Message queues like Kafka or RabbitMQ decouple producers and consumers in a distributed system, improving scalability, resilience, and asynchronous processing.”
> 

---

---

## 404. How would you troubleshoot a failing API in production?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “When an API fails in production, I follow a layered debugging approach — starting from monitoring, isolating the failure, and then deep-diving into logs, metrics, and dependencies.”
> 

---

---

## 405. How does event-driven architecture work with Kafka?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “In an event-driven architecture with Kafka, services communicate by publishing and consuming events instead of making direct API calls. This leads to loose coupling, scalability, and async workflows.”
> 

---

---

## 406. Redis vs. Memcached: Which one do you pick for caching, and why?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “I’d pick Redis for most real-world systems due to its rich data structures, persistence options, and pub/sub support.”
> 

---

---

## 407. How do you monitor and troubleshoot issues in a microservices architecture?

*Source: [`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

> “Monitoring in microservices is all about observability — logs, metrics, and traces. I use a combination of centralized tools and standardized practices.”
> 

---

---

## Question bank (no recorded answers)

Prompts collected from the notes that have no written answer yet:

- How does HashMap store data? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- What happens during collision? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- Why resizing is expensive? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- What causes frequent GC? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- Are streams lazy? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- Are streams reusable? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- Are parallel streams always faster? — *[`01-java/code-decode/java-printable-notes-by-code-decode.md`](../01-java/code-decode/java-printable-notes-by-code-decode.md)*
- Main Question: When was the last time you took the initiative on something? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Main Question: Were you solely responsible for your tasks? What sort of team interactions were involved in getting your work to production? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Main Question: How was the architecture for your tasks usually decided? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- When to Use Which? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Could you take us through your last role and explain what you did there? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Could you highlight an initiative you started without being asked to do? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- When was the last time you did something to make the culture more fun? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Which is the biggest project you have led? What were the challenges you faced? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Could you explain a time when a good developer was under-performing, what did you do to resolve situation? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Could you explain a time you wanted to make a difference to how a team works, i.e. WIP limits. How did you make this happen? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Remote working - how do you keep the team motivated when the team is working remotely? How often do you communicate with them? Do you feel it makes things easier/harder/better/worse, and how? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Do you tend to use much inheritance in practice, or do you favor composition? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Can you tell me about the last time you implemented a class hierarchy from scratch? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- How do you approach designing class relationships when building a new feature or module? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- What are some downsides of inheritance, and how do you handle them? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Can you describe the Exception hierarchy? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Can you give some real-world examples of checked and unchecked exceptions? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Is there anything wrong with doing a catch (Throwable)? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- When was the last time you created and threw a custom exception? Was it checked or unchecked? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Do you prefer checked or unchecked exceptions, and why? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- What happens if you never catch a runtime exception? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- What are the performance implications (Big O) of common operations like get(), add(), and remove()? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Can you give a real-world scenario where a LinkedList would outperform an ArrayList? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Why is get(index) slower in a LinkedList? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- What happens when you frequently insert in the middle or start of the list? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Are there any memory or cache locality concerns? — *[`01-java/elsevier/java-interview-questions-from-elsevier.md`](../01-java/elsevier/java-interview-questions-from-elsevier.md)*
- Why Use Optional in Java 8? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Can We Override Non-Abstract Methods? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Can We Change Return Type While Overriding? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Which functional interface was introduced in Java 8? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- How does ConcurrentHashMap work internally to achieve concurrency? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- What is the Singleton design pattern? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- How does it make the Singleton thread-safe? Suppose there is a fixed thread pool with 20 threads—how does it work in that case? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- How is the Singleton safe from cloning? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- What are the different operators in Stream? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Is the table huge? Add pagination or limit query scope: — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Describe the internal workings of HashMap. What occurs when two keys share the same hash code? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Define String, StringBuilder, and StringBuffer. Which is preferable in multithreaded code and why? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- What sets an abstract class apart from an interface in Java 8+? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- How does Java manage memory (Heap, Stack, Garbage Collection)? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- How does the synchronized keyword function? When is ReentrantLock preferred? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Explore the Streams API. How does map() differ from flatMap()? — *[`01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md`](../01-java/linkedin-candidates/interview-questions-collected-by-the-linkedin-cand.md)*
- Why HashSet? → O(1) lookup — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- How do you identify a bottleneck? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- How do you distinguish CPU vs IO issues? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- How do you detect memory leaks? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- How does GC affect latency? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- What tools have you used in production? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Same transaction? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Separate transaction? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Liveness: Should be restarted? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Do you understand your project end-to-end, or only your module? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Do you own problems, or just execute tasks? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- Why microservices? — *[`01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md`](../01-java/linkedin-final/java-interview-final-from-linkedin-for-the-develop.md)*
- · How would you implement it? — *[`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*
- The following code is not thread-safe. Why? — *[`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*
- · What’s wrong with this implementation? — *[`01-java/linkedin/java-linkedin-interview-questions.md`](../01-java/linkedin/java-linkedin-interview-questions.md)*
- Design a drug information catalog system where doctors can login and check details of new drugs, their prices, and vendors. Vendors must register the drugs in the system which will be reviewed and approved by the admin team. Explain the design in detail, the APIs you create, along with the front and back end tech stack that you are going to use? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest.md)*
- If Java didn’t have the synchronized keyword, how would you implement thread safety? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- How would you store a billion records in memory while ensuring efficient search operations? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Explain Java’s ClassLoader in a way that a 10-year-old could understand. — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- What exactly happens inside the JVM when a NullPointerException is thrown? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Design a Traffic Management System for a City with Self-Driving Cars — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- If You Had to Reduce API Response Time by 50% in a Large-Scale System, Where Would You Start? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- How would you design a video streaming platform that adapts in real-time to network conditions? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Can you sort an array faster than O(n log n)? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- You have an infinite stream of numbers. How would you efficiently find the median at any point? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- If you could only use one data structure for every problem, which one would it be and why? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- How would you explain recursion to someone who has never coded before? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- If you could remove one feature from Java, what would it be and why? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Tell me something interesting about technology that isn’t on your resume. — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- How would you debug a memory leak in a production Java application? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Explain CAP theorem and its relevance to distributed systems. — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Explain circuit breakers and how you’d implement them using Hystrix in a microservices architecture. — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- How does the Vert.x Event Bus work for inter-component communication? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- What’s the difference between Vert.x and traditional blocking frameworks like Spring Boot? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Why Use Message Queues? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Define what a "duplicate" means — same transaction ID? Same amount + timestamp? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Why Two Heaps?: — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Is it global or region-specific? All users or one client? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Is a downstream service (like payment gateway, auth provider) failing? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Is the container or pod crashing (OOMKilled, high CPU)? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Is DB under heavy load or locked up? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*
- Any recent config changes or new deployments? — *[`01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md`](../01-java/linkedin/java-linkedin-interview-questions/shiva-kumar-satakuri-linkedin-java-interview-quest/ms-ruby-paypal.md)*

