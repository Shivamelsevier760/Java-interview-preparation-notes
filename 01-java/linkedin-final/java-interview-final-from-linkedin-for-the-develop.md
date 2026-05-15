# Java interview final from linkedin for the developer real time

---

## 1. What is a Maven build?

A Maven build is the process where **Maven compiles code, runs tests, packages the application, and manages dependencies** using `pom.xml`.

It ensures **consistent builds across environments**.

---

## 2. What does `mvn clean install` do?

- `clean` → deletes the `target` folder
- `install` → compiles code, runs tests, packages the app, and installs the artifact into **local Maven repository**

👉 Used before deploying or sharing artifacts.

---

## 3. How do you push code to production?

Typical real-time flow:

1. Commit code → Git
2. Create PR → Code review
3. CI pipeline runs (build + tests)
4. Artifact created (JAR/WAR/Docker image)
5. Deployed via **Jenkins / GitHub Actions / Azure DevOps**
6. Production deployment (Blue-Green / Rolling)
7. Smoke tests + monitoring

---

## 4. What is code coverage?

Code coverage measures **how much of the code is executed by tests**.

Example tools: **JaCoCo, SonarQube**

---

## 5. What is line coverage?

Line coverage shows **percentage of code lines executed** during tests.

---

## 6. How do you improve code coverage when build fails?

- Add missing unit tests
- Cover edge cases & exception paths
- Mock external dependencies
- Refactor complex methods
- Exclude non-testable code (DTOs, configs)

---

## 7. How do you verify a method is called twice in Mockito?

```java
verify(service, times(2)).process();

```

---

## 8. In which situations do you use PowerMock?

Used when mocking:

- `static` methods
- `final` classes/methods
- private methods
- constructors

⚠️ Used only for **legacy code** (avoid in new code).

---

## 9. Difference between `final` keyword and final variable?

- `final variable` → value cannot change
- `final method` → cannot be overridden
- `final class` → cannot be inherited

---

## 10. What is Garbage Collection in Java?

Automatic process where JVM **reclaims unused memory** by removing unreachable objects.

---

## 11. How do you ensure Garbage Collection is working correctly?

- Enable GC logs
- Monitor heap usage
- Use tools like **VisualVM / JConsole**
- No frequent Full GCs
- Stable memory after GC

---

## 12. How do you debug and fix OutOfMemoryError?

Steps:

1. Analyze heap dump
2. Identify memory leaks
3. Check large collections
4. Tune JVM heap size
5. Fix object retention issues

---

## 13. What are atomic variables in Java?

Thread-safe variables that perform **lock-free operations**

Example: `AtomicInteger`, `AtomicLong`

---

## 14. What is the `volatile` keyword?

Ensures **visibility of variable changes** across threads.

Does NOT provide atomicity.

---

## 15. Difference between `volatile` and `synchronized`?

| volatile | synchronized |
| --- | --- |
| Visibility only | Visibility + atomicity |
| No locking | Uses lock |
| Faster | Slower |

---

## 16. How do you avoid performance issues caused by synchronization?

- Use atomic classes
- Reduce synchronized scope
- Use concurrent collections
- Prefer lock-free algorithms

---

## 17. What is a BlockingQueue?

A thread-safe queue where:

- Producer waits if full
- Consumer waits if empty

---

## 18. Where do you use BlockingQueue in real applications?

- Producer-consumer systems
- Thread pools
- Message processing
- Background job queues

---

## 19. Difference between HashMap and Hashtable?

| HashMap | Hashtable |
| --- | --- |
| Not synchronized | Synchronized |
| Allows null | No null |
| Faster | Slower |

---

## 20. Why does Hashtable not allow null?

To avoid ambiguity between **null key/value** and **method return value** in synchronized access.

---

## 21. What is load factor in HashMap?

Load factor decides **when resizing happens**.

---

## 22. What does default load factor 0.75 mean?

When map is **75% full**, it resizes to maintain performance.

---

## 23. Difference between UNION and UNION ALL?

- `UNION` → removes duplicates
- `UNION ALL` → keeps duplicates (faster)

---

## 24. Difference between LEFT JOIN and RIGHT JOIN?

- LEFT JOIN → all rows from left table
- RIGHT JOIN → all rows from right table

---

## 25. When do you use LEFT JOIN?

When you want **all records from primary table**, even if no match exists.

---

## 26. How do you find records without relationship?

```sql
SELECT a.*
FROM tableA a
LEFT JOIN tableB b ON a.id = b.id
WHERE b.id IS NULL;

```

---

## 27. How do you handle NULL values in SQL?

- `COALESCE()`
- `NVL()` (Oracle)
- `CASE WHEN`

---

## 28. How do you map values like A → Apple?

```sql
CASE code
  WHEN 'A' THEN 'Apple'
  WHEN 'B' THEN 'Banana'
END

```

---

## 29. How do you define relationships in Hibernate?

Using annotations:

- `@OneToOne`
- `@OneToMany`
- `@ManyToOne`
- `@ManyToMany`

---

## 30. How do you remove duplicates in SQL?

```sql
SELECT DISTINCT column FROM table;

```

or using `ROW_NUMBER()`.

---

## 31. Types of relationships in Hibernate?

- One-to-One
- One-to-Many
- Many-to-One
- Many-to-Many

---

## 32. Constructor vs Setter Injection?

| Constructor | Setter |
| --- | --- |
| Mandatory dependencies | Optional dependencies |
| Immutable | Mutable |
| Preferred | Less preferred |

---

## 33. What happens if you don’t use `@Autowired`?

Spring won’t inject dependencies → **NullPointerException** (unless using constructor injection).

---

## 34. Constructor injection without `@Autowired`?

If only **one constructor exists**, Spring auto-injects it.

---

## 35. Java 7 → Java 8 migration changes?

- Lambda expressions
- Streams API
- Functional interfaces
- Default methods
- Date/Time API

---

## 36. Ways to ensure thread safety?

- synchronized
- Locks
- Atomic variables
- Immutable objects
- ThreadLocal
- Concurrent collections

---

## 37. What is ThreadLocal?

Stores **thread-specific data**.

Used in:

- User sessions
- Transaction context
- Security context

---

## 38. Longest substring without repeating characters (Java logic)?

Use **sliding window + HashSet / Map**

Time complexity: **O(n)**

---

---

# 📄 **JAVA / SPRING / SQL – 1-PAGE REVISION SHEET**

## 🔹 Maven & CI/CD

- **Maven Build** → Compile + Test + Package using `pom.xml`
- **`mvn clean install`** → Cleans target + builds + runs tests + installs to local repo
- **Production Deployment** → Git → PR → CI (tests) → Artifact → CD (Blue-Green / Rolling)

---

## 🔹 Testing & Coverage

- **Code Coverage** → % of code executed by tests
- **Line Coverage** → Lines executed
- **Improve Coverage** → Add tests, mock dependencies, cover edge cases
- **Mockito verify twice**
    
    ```java
    verify(service, times(2)).method();
    
    ```
    
- **PowerMock** → Mock static, final, private (legacy code only)

---

## 🔹 Java Keywords & Memory

- **final variable** → value cannot change
- **final method** → cannot override
- **final class** → cannot extend
- **Garbage Collection** → JVM frees unused objects automatically
- **OOM Debug** → Heap dump + memory leak analysis

---

## 🔹 Concurrency

- **Atomic Variables** → Lock-free thread safety
- **volatile** → Visibility only
- **synchronized** → Visibility + atomicity
- **Avoid sync issues** → Atomic classes, concurrent collections
- **BlockingQueue** → Producer-Consumer pattern
- **ThreadLocal** → Thread-specific data (security, transactions)

---

## 🔹 Collections

- **HashMap vs Hashtable**
    - HashMap → Faster, allows null
    - Hashtable → Thread-safe, no null
- **Load Factor (0.75)** → Resize when 75% full

---

## 🔹 SQL

- **UNION** → Removes duplicates
- **UNION ALL** → Faster, keeps duplicates
- **LEFT JOIN** → All left + matched right
- **Find unmatched rows**
    
    ```sql
    LEFT JOIN ... WHERE right.id IS NULL
    
    ```
    
- **Handle NULL** → `COALESCE`, `CASE`
- **Mapping values**
    
    ```sql
    CASE WHEN 'A' THEN 'Apple' END
    
    ```
    
- **Remove duplicates** → `DISTINCT`, `ROW_NUMBER()`

---

## 🔹 Spring & Hibernate

- **Relationships** → One-to-One, One-to-Many, Many-to-One, Many-to-Many
- **Constructor Injection** → Preferred, mandatory deps
- **No @Autowired** → Injection fails (except single constructor)
- **Java 8 Migration** → Lambdas, Streams, Date API

---

# 💻 **Q40 – Longest Substring Without Repeating Characters (Java)**

### 🔹 Problem

Find the length of the **longest substring** without repeating characters.

---

## 🔹 Approach (Sliding Window – Interview Friendly)

- Use **two pointers**
- Use **HashSet** to track unique characters
- Move window forward when duplicate found
- Time Complexity → **O(n)**

---

## 🔹 Step-by-Step Java Code (Explained Line by Line)

```java
import java.util.HashSet;
import java.util.Set;

public class LongestSubstring {

    public static int longestUniqueSubstring(String s) {

        // HashSet to store unique characters
        Set<Character> set = new HashSet<>();

        int left = 0;        // left pointer of window
        int maxLength = 0;  // result

        // right pointer moves forward
        for (int right = 0; right < s.length(); right++) {

            char current = s.charAt(right);

            // If duplicate found, remove from left
            while (set.contains(current)) {
                set.remove(s.charAt(left));
                left++;
            }

            // Add current character
            set.add(current);

            // Update maximum length
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String input = "abcabcbb";
        System.out.println(longestUniqueSubstring(input)); // Output: 3
    }
}

```

---

## 🔹 Example Walkthrough

Input: `"abcabcbb"`

| Window | Substring | Length |
| --- | --- | --- |
| 0–2 | abc | 3 |
| 1–3 | bca | 3 |
| 2–4 | cab | 3 |

✅ **Answer = 3**

---

## 🔹 Interview Follow-up Answers

- **Why HashSet?** → O(1) lookup
- **Time Complexity?** → O(n)
- **Space Complexity?** → O(min(n, charset))

---

---

### 🧵 **What really happens when `Thread.start()` is called? (Interview Answer)**

When we call `Thread.start()`, **JVM does not directly call `run()`**.

Internally, `start()` invokes a **native method called `start0()`**.

What `start0()` does:

- Requests the **OS to create a new native (platform) thread**
- OS allocates a **new call stack** and **program counter**
- JVM schedules the thread for execution
- **Only then** JVM invokes the `run()` method on the **new thread**

This is why:

- Calling `start()` creates a **new thread**
- Calling `run()` directly behaves like a **normal method call** (no new thread)

👉 Threads in Java are called **platform threads** because **thread creation and scheduling are managed by the OS**.

---

### 🔑 **One-Line Interview Punch**

> start() creates a new OS-level thread via start0(), and run() executes on that new thread—not the current one.
> 

---

---

# 🔷 OOPS – INTERVIEW READY ANSWERS (1–2 lines each)

---

## 1. What is Object-Oriented Programming (OOPS)?

OOPS is a programming paradigm that organizes software using **objects** that represent real-world entities and focus on **data + behavior together**.

---

## 2. Four pillars of OOPS

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

## 3. What is a class in Java?

A class is a **blueprint** that defines variables (data) and methods (behavior).

---

## 4. What is an object in Java?

An object is a **runtime instance of a class**.

---

## 5. Difference between class and object

- **Class** → blueprint
- **Object** → real instance created from class

---

## 6. What is encapsulation?

Wrapping **data and methods together** and restricting direct access to data.

---

## 7. How do you achieve encapsulation in Java?

- Make variables `private`
- Provide access using `public getters/setters`

---

## 8. What is abstraction?

Hiding implementation details and showing **only essential behavior**.

---

## 9. Abstract class vs Interface

| Abstract Class | Interface |
| --- | --- |
| Can have variables | Only constants |
| Can have constructors | No constructors |
| Supports partial abstraction | Full abstraction |

---

## 10. What is inheritance?

One class **acquires properties and methods** of another class.

---

## 11. Types of inheritance in Java

- Single
- Multilevel
- Hierarchical
    
    (Java does NOT support multiple inheritance with classes)
    

---

## 12. What is polymorphism?

Ability of an object to take **many forms**.

---

## 13. Compile-time vs Runtime polymorphism

- **Compile-time** → Method overloading
- **Runtime** → Method overriding

---

## 14. What is method overloading?

Same method name, **different parameters**, same class.

---

## 15. What is method overriding?

Subclass provides **specific implementation** of parent method.

---

## 16. Can we override static methods?

❌ No. Static methods belong to class, not object.

---

## 17. What is dynamic method dispatch?

Method call is resolved **at runtime** based on object type.

---

## 18. What is the final keyword in OOPS?

- `final variable` → constant
- `final method` → cannot override
- `final class` → cannot extend

---

## 19. What is constructor?

A special method used to **initialize objects**.

---

## 20. Types of constructors

- Default constructor
- Parameterized constructor

---

## 21. What is constructor overloading?

Multiple constructors with **different parameters** in same class.

---

## 22. Can a constructor be private?

✅ Yes — used in **Singleton design pattern**.

---

## 23. Use of `this` keyword

Refers to **current object** and resolves variable ambiguity.

---

## 24. Use of `super` keyword

Refers to **parent class** variables, methods, or constructor.

---

## 25. Access modifiers in Java

- private
- default
- protected
- public

---

## 26. Default vs Protected

- **Default** → same package only
- **Protected** → same package + subclasses

---

## 27. What is an interface?

A contract that defines **what a class must do**, not how.

---

## 28. Can interface have methods with body?

✅ Yes (Java 8+): `default` and `static` methods.

---

## 29. Multiple inheritance & Java support

Java supports multiple inheritance **via interfaces only**, not classes.

---

## 30. What is association?

Relationship where objects **use each other**.

---

## 31. Association vs Aggregation vs Composition

| Type | Meaning |
| --- | --- |
| Association | Loose relation |
| Aggregation | HAS-A (weak) |
| Composition | HAS-A (strong, lifecycle dependent) |

---

## 32. What is IS-A relationship?

Inheritance relationship

Example: Dog IS-A Animal

---

## 33. What is HAS-A relationship?

Association relationship

Example: Car HAS-A Engine

---

## 34. What is tight coupling?

Classes are **highly dependent** on each other.

---

## 35. What is loose coupling?

Classes depend on **abstractions**, not implementations.

---

## 36. What is object cloning?

Creating an **exact copy** of an object using `clone()`.

---

## 37. Shallow copy vs Deep copy

- **Shallow** → copies references
- **Deep** → copies actual objects

---

## 38. Why Java doesn’t support multiple inheritance with classes?

To avoid **Diamond Problem** and ambiguity.

---

## 39. What is `instanceof` keyword?

Checks whether an object belongs to a specific class/interface.

---

## 40. What is garbage collection in OOPS?

Automatic memory cleanup of **unused objects** by JVM.

---

## 41. Can we override private methods?

❌ No. Private methods are not visible to subclasses.

---

## 42. Can we change return type while overriding?

❌ No, except **covariant return types**.

---

## 43. What is covariant return type?

Overridden method can return **child class object**.

---

## 44. Abstraction vs Encapsulation

- **Abstraction** → hides implementation
- **Encapsulation** → hides data

---

## 45. Real-world example of polymorphism

Same **payment method** → Credit Card / UPI / Net Banking.

---

## 46. Real-world example of inheritance

Vehicle → Car → ElectricCar

---

## 47. What is a design pattern?

Reusable solution to **common software design problems**.

---

## 48. What is singleton class?

A class that allows **only one object**.

---

## 49. How to create immutable class?

- Make class `final`
- Fields `private final`
- No setters
- Initialize via constructor

---

## 50. Why OOPS is important?

- Code reusability
- Maintainability
- Scalability
- Real-world modeling

---

---

## 1. Why does a Java app behave differently in prod vs local?

Because prod differs in **data volume, concurrency, JVM flags, GC, CPU, memory limits, network latency, and external dependencies**.

Most “prod-only bugs” are **timing, GC, or resource contention issues**.

---

## 2. How does JVM decide object allocation and promotion?

- Objects allocated in **Eden**
- Survive GC → move to **Survivor**
- Survive multiple cycles → promoted to **Old Gen**
    
    Promotion depends on **age, size, and survivor space pressure**.
    

---

## 3. What happens during a Stop-The-World GC pause?

- All application threads are **paused**
- JVM identifies live objects
- Reclaims or moves memory
- Threads resume
    
    STW affects **latency**, not correctness.
    

---

## 4. Why is `volatile` not sufficient for thread safety?

`volatile` guarantees **visibility**, not **atomicity**.

Compound operations (read-modify-write) can still race.

---

## 5. When does `synchronized` become a scalability problem?

When:

- High contention
- Long critical sections
- Many threads competing
    
    Threads block → **context switching overhead** increases.
    

---

## 6. How can HashMap break in multithreaded environments?

Concurrent resize can cause:

- **Infinite loops**
- Data corruption
    
    Because HashMap is **not thread-safe**.
    

---

## 7. ConcurrentHashMap vs synchronizedMap (internal)

- `synchronizedMap` → single global lock
- `ConcurrentHashMap` → **lock striping / CAS / fine-grained locking**
    
    Result: much better scalability.
    

---

## 8. How does Java Memory Model guarantee visibility?

Through:

- `volatile`
- `synchronized`
- `final` fields
- Happens-before rules
    
    These enforce **memory barriers**.
    

---

## 9. What is false sharing?

Multiple threads modify **different variables** that share the **same CPU cache line**, causing cache invalidation.

Avoid using:

- Padding
- `@Contended`
- Proper data layout

---

## 10. Why does double-checked locking fail without `volatile`?

Because of **instruction reordering**:

- Reference assigned before object fully constructed
- Another thread sees a partially initialized object

---

## 11. How does JVM detect and report deadlocks?

JVM tracks lock ownership.

Detected deadlocks are reported via:

- `jstack`
- JVM thread dumps

---

## 12. Why can thread pools silently degrade performance?

Because:

- Queues grow
- Threads are blocked
- Tasks pile up
    
    System looks “healthy” but **latency explodes**.
    

---

## 13. What happens if a task throws exception in ExecutorService?

- Exception is swallowed
- Thread stays alive
- Failure visible only via `Future.get()` or logs

---

## 14. How do you safely shut down a thread pool?

```java
shutdown();
awaitTermination();
shutdownNow(); // if needed

```

Always handle **interrupts properly**.

---

## 15. Why does GC tuning improve latency but hurt throughput?

Frequent GC → shorter pauses → **more CPU spent on GC**

Trade-off:

- Low latency
- Lower overall work done

---

## 16. How does G1 GC choose regions?

G1 selects regions with **highest garbage-to-cost ratio** to meet **pause-time goals**.

---

## 17. Why can OOM occur even with free heap?

- Fragmentation
- Metaspace exhaustion
- Direct memory leaks
- Native memory limits

---

## 18. How do you find memory leaks in a live JVM?

- Heap dump
- Analyze object retention
- Look for **growing references**
    
    Tools: VisualVM, MAT, JProfiler
    

---

## 19. Strong vs Weak vs Soft vs Phantom references

- **Strong** → never GCed
- **Weak** → GCed quickly
- **Soft** → GCed under memory pressure
- **Phantom** → post-GC cleanup tracking

---

## 20. Why is `finalize()` dangerous?

- Unpredictable
- Delays GC
- Can resurrect objects
    
    Deprecated due to **non-determinism**.
    

---

## 21. How does class loading work in large apps?

- Bootstrap → Platform → Application
- Custom classloaders per module
    
    Can cause **class visibility issues**.
    

---

## 22. Why does ClassCastException occur in modular systems?

Same class loaded by **different classloaders** → JVM treats them as different types.

---

## 23. How does Java handle instruction reordering?

JVM and CPU reorder instructions for performance, but **JMM rules prevent illegal reordering** across synchronization boundaries.

---

## 24. When does autoboxing hurt performance?

In:

- Tight loops
- Collections
- High-frequency arithmetic
    
    Creates excessive temporary objects.
    

---

## 25. Why is String immutable and how does it help concurrency?

- Thread-safe by design
- Safe caching
- Enables string pool
- Prevents data races

---

## 26. How does JVM optimize hot code paths?

- JIT compilation
- Method inlining
- Loop unrolling
- Escape analysis

---

## 27. What is escape analysis?

Determines if object:

- Escapes method/thread
    
    If not → allocate on **stack** or eliminate object.
    

---

## 28. Why doesn’t JVM exit after `main()` finishes?

Because:

- Non-daemon threads still running
- Thread pools
- GC / background threads

---

## 29. How do you debug high CPU with low traffic?

- Thread dumps
- Look for spin loops
- Lock contention
- GC thrashing
- Misconfigured thread pools

---

## 30. What Java design decision caused a real production issue?

**Mixing transactions with external calls** → partial failures & data inconsistency.

Fix was **design change**, not code change.

---

### 

## 📌 **Java Performance Tuning – Core Learning Summary**

### 🔹 1. Golden Rule of Performance Tuning

**Never optimize without data.**

Most mistakes happen because developers:

- Guess the bottleneck
- Optimize the wrong layer
- Focus only on code, not runtime behavior

👉 Performance tuning is a **system-level activity**, not just a coding task.

---

### 🔹 2. Key Areas That Impact Java Performance

**1️⃣ JVM Configuration**

- Heap size
- Garbage Collector choice
- Thread stack size

**2️⃣ Memory Management**

- High object creation rate
- Memory leaks
- Large or growing collections

**3️⃣ CPU Utilization**

- Thread contention
- Excessive synchronization
- Infinite or busy loops

**4️⃣ IO Operations**

- Database queries
- Network calls
- File system access

👉 Most real production issues are **IO or memory related**, not CPU.

---

### 🔹 3. Code-Level Practices That Actually Matter

- Avoid unnecessary object creation
- Prefer primitives over wrappers
- Use `StringBuilder` in loops
- Cache expensive operations
- Always close resources
- Use connection pools correctly

👉 **Clean, simple code usually performs better.**

---

### 🔹 4. JVM & GC Awareness (Very Important)

You don’t need to tune GC daily, but you must understand:

- Heap vs Stack
- Young Gen vs Old Gen
- Minor vs Major GC
- Stop-The-World pauses

👉 Many “random production issues” are actually **GC problems misdiagnosed as code bugs**.

---

### 🔹 5. Tools Every Java Developer Should Know

- JVisualVM
- JConsole
- Java Flight Recorder (JFR)
- Java Mission Control (JMC)
- Application logs
- APM tools (Dynatrace, New Relic, AppDynamics)

👉 **Tools provide facts. Assumptions create confusion.**

---

### 🔹 6. What Interviewers Look For (5+ Years)

Not memorized JVM flags, but **your approach**:

- How do you identify a bottleneck?
- How do you distinguish CPU vs IO issues?
- How do you detect memory leaks?
- How does GC affect latency?
- What tools have you used in production?

👉 They test **thinking, not syntax**.

---

### 🔹 7. Full-Stack Perspective on Performance

Performance is end-to-end:

- Slow backend → poor frontend UX
- Slow DB → slow APIs
- Poor thread handling → scalability issues

👉 Performance tuning is a **cross-layer responsibility**.

Here’s a **clean, senior-level learning + interview summary** you can remember and reuse confidently:

---

## 🎟️ **The Core System Design Pattern Behind Booking Systems**

### 🔑 The Real Problem (Not UI or Payments)

Booking systems are about **handling extreme concurrency on limited inventory** without overselling, while keeping latency low.

> Millions of users → few seats → same millisecond.
> 

---

## 1️⃣ The Core Challenge

- High write contention
- Race conditions
- Hot database rows
- Zero tolerance for double booking (trust killer)

---

## 2️⃣ Three Non-Negotiable Guarantees

- ✅ **No overselling** – each seat sold once
- ✅ **Fairness** – first-come-first-serve (bot-aware)
- ✅ **Low latency** – handle 100k–1M RPS (< 2s response)

---

## 3️⃣ Booking Is a State Machine

Seats move through **well-defined states**:

```
AVAILABLE → HELD → CONFIRMED

```

- **HELD** is temporary (payment window)
- If payment fails → seat returns to AVAILABLE
- All services must agree on state instantly

---

## 4️⃣ The Winning Architecture: Redis + Database

### 🔥 Level 1: Redis (Concurrency Control)

- Redis holds **seat availability**
- Atomic operations (`SETNX` / Lua scripts)
- Only one request can move:
    
    ```
    AVAILABLE → HELD
    
    ```
    
- TTL (e.g. 5 minutes) automatically releases unpaid holds
- Handles **99% of traffic**

---

### 🔥 Level 2: Database (Final Authority)

- DB only sees **CONFIRMED** writes
- Uses:
    - Unique constraints `(event_id, seat_id)`
    - Or optimistic locking
- Acts as **source of truth + safety net**

---

## 5️⃣ How Key Interview Questions Are Answered

### ❓ How do you prevent double booking?

- Atomic state transition in Redis
- Unique constraint in DB as final guard

---

### ❓ What if payment fails?

- Release Redis hold or let TTL expire
- No DB write without payment success

---

### ❓ What if Redis goes down?

- **Correctness > Availability**
- Fail fast or fall back to throttled DB mode
- Rebuild Redis state from DB

---

### ❓ How do you ensure idempotency?

- Every request has an `idempotency_key`
- Store `key → result`
- Repeated requests return the same result (no double charge)

---

## 🧠 One-Line Interview Takeaway

> Modern booking systems rely on Redis-based atomic holds + DB-level guarantees, treating booking as a state machine, not a simple insert.
> 

---

---

# ✈️ **Java 8 Stream API – Problem Solving Approach**

## 1️⃣ Start With the Problem (Before Writing Code)

Always ask **these 3 questions first**:

### ✅ What is the **Input**?

- `List`, `Set`, `Map`, `Array`
- `String`
- `Integer`, custom objects

### ✅ What is the **Output**?

- `List`, `Set`, `Map`
- `Optional<T>`
- Single value (`int`, `long`, `double`, `String`)

### ✅ What operation is needed?

- **Filter** → remove elements
- **Transform** → change data
- **Group** → categorize
- **Aggregate** → count / sum / max / min

👉 If you identify input + output correctly, **half the problem is solved**.

---

## 2️⃣ Remember the Golden Stream Flow

```
Source → Intermediate → Terminal

```

⚠️ **No terminal operation = no execution**

Example:

```java
list.stream()        // source
    .filter(...)     // intermediate
    .map(...)        // intermediate
    .collect(...);   // terminal (executes stream)

```

---

## 3️⃣ Core Methods You MUST Remember (Interview Essentials)

### 🔹 Filtering

```java
filter(Predicate)

```

Removes unwanted elements.

---

### 🔹 Mapping / Transformation

```java
map(Function)        // one-to-one
flatMap(Function)   // flatten nested data

```

Example:

- `map()` → `User → name`
- `flatMap()` → `List<List<T>> → Stream<T>`

---

### 🔹 Sorting

```java
sorted()
sorted(Comparator)

```

---

### 🔹 Terminal Operations (Execution Point)

```java
forEach()
collect()
count()
findFirst()
findAny()
anyMatch()
allMatch()
noneMatch()

```

---

### 🔹 Convert Stream to Collection

```java
collect(Collectors.toList())
collect(Collectors.toSet())
collect(Collectors.toMap())

```

---

### 🔹 Grouping & Counting

```java
Collectors.groupingBy()
Collectors.counting()

```

---

## 4️⃣ Optional – VERY Important

Many stream operations return `Optional`:

```java
findFirst()
max()
min()

```

👉 Always handle `Optional` safely:

```java
optional.orElse(...)
optional.ifPresent(...)

```

---

## 5️⃣ Lambda Writing Tips (Cleaner Code)

❌ Bad:

```java
x -> { return x * 2; }

```

✅ Good:

```java
x -> x * 2

```

✅ Best (Method Reference):

```java
System.out::println
String::length

```

---

## 6️⃣ Common Stream Pattern (90% Problems)

```java
filter()
→ map()
→ collect()
→ groupingBy()

```

If stuck, **start with this mental template**.

---

## 7️⃣ Stream Operations Cheat Sheet (Quick Recall)

### 🔸 Filtering & Slicing

- `filter`
- `distinct`
- `limit`
- `skip`
- `takeWhile` (Java 9+)
- `dropWhile` (Java 9+)

---

### 🔸 Mapping & Transformation

- `map`
- `mapToInt / mapToLong / mapToDouble`
- `flatMap`
- `flatMapToInt / Long / Double`

---

### 🔸 Sorting

- `sorted`
- `sorted(Comparator)`

---

### 🔸 Debugging

- `peek()` → **debug only**, not business logic

---

### 🔸 Stateful / Advanced

- `boxed()`
- `unordered()`
- `parallel()`
- `sequential()`

---

### 🔸 Terminal Operations

- `forEach`
- `forEachOrdered`
- `reduce`
- `collect`

---

### 🔸 Matching (Short-Circuit)

- `anyMatch`
- `allMatch`
- `noneMatch`

---

### 🔸 Finding & Counting

- `findFirst`
- `findAny`
- `count`

---

### 🔸 Min / Max

- `min`
- `max`

---

### 🔸 Primitive Stream Terminals

- `sum`
- `average`
- `summaryStatistics`

---

## 🧠 **Interview One-Liner**

> When solving Stream API problems, I first identify input and output, decide the operation type, follow the source–intermediate–terminal flow, and build the solution incrementally using filter, map, and collect.
> 

---

## ✅ **Senior Java Interview – Refined Answers & Talking Points**

---

### 1. ConcurrentHashMap vs SynchronizedMap

- **ConcurrentHashMap**
    - Fine-grained locking + CAS
    - Concurrent reads and writes
    - High scalability under contention
- **SynchronizedMap**
    - Single global lock
    - All operations block each other
    - Poor performance under load

👉 *Use ConcurrentHashMap in high-concurrency systems.*

---

### 2. How do you identify and fix memory leaks?

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

### 3. Thread vs ExecutorService vs Virtual Threads

- **Thread** → Heavy, OS-managed
- **ExecutorService** → Thread pooling + lifecycle control
- **Virtual Threads (Java 21+)** → Lightweight, JVM-managed, massive concurrency

👉 *Use virtual threads for high I/O concurrency.*

---

### 4. When should virtual threads NOT be used?

- CPU-bound workloads
- Long `synchronized` blocks
- Native blocking calls (thread pinning)

---

### 5. How does Garbage Collection impact performance?

- Impacts **latency (pause time)** and **throughput**
- Tuned via:
    - Heap sizing
    - GC selection (G1, ZGC)
    - Reducing object allocation

👉 Many prod issues blamed on code are actually **GC issues**.

---

### 6. synchronized vs Lock

- **synchronized**
    - Simpler
    - JVM-managed
- **Lock**
    - `tryLock()`
    - Fairness
    - Interruptible waits

👉 *Use Lock when you need control.*

---

### 7. equals() and hashCode() contract

- Equal objects **must** have same hashCode
- Poor hashCode → HashMap collisions → performance degradation

---

### 8. How Spring manages transactions

- Uses **AOP proxies**
- `@Transactional`:
    - Opens transaction before method
    - Commits or rolls back after execution
- Rollback depends on exception type and boundary

---

### 9. Designing a scalable Java application

- Stateless services
- Caching (Redis, Caffeine)
- Async processing
- Connection pooling
- Observability (metrics, tracing)
- Horizontal scaling

---

### 10. Optional vs null

- **Optional**
    - Explicit absence
    - Avoids NPE
- ❌ Don’t use Optional as:
    - Fields
    - Method parameters

---

### 11. Handling high traffic in Java APIs

- Load balancing
- Caching
- Async queues
- Rate limiting
- Proper thread model (virtual threads for I/O)

---

### 12. Fail-fast vs Fail-safe iterators

- **Fail-fast**
    - Throws `ConcurrentModificationException`
- **Fail-safe**
    - Iterates over copy
    - Example: `CopyOnWriteArrayList`

---

### 13. Choosing the right data structure

Based on **access pattern**:

- Fast lookup → `HashMap`
- Ordered data → `TreeMap`
- Frequent reads → `ArrayList`
- Frequent inserts → `LinkedList`

---

### 14. What makes a senior Java engineer stand out?

- Explains **trade-offs**, not just answers
- Understands JVM internals
- Designs for **scale & failure**
- Writes clean, testable, maintainable code

---

Below is a **complete, interview-ready answer pack** for **Java 8, Collections, Spring Boot, JPA, and REST**, written the way **senior interviewers expect you to explain**.

Clear, practical, and example-driven.

---

# 🔹 **Java 8 & Core Java**

## 1. Major features introduced in Java 8

- Lambda Expressions
- Functional Interfaces
- Stream API
- Optional
- Default & static methods in interfaces
- New Date & Time API
- Parallel streams & concurrency improvements

---

## 2. Converting pre–Java 8 code to Lambda (Example)

### Pre–Java 8

```java
Runnable r = new Runnable() {
    public void run() {
        System.out.println("Hello");
    }
};

```

### Java 8 (Lambda)

```java
Runnable r = () -> System.out.println("Hello");

```

👉 Lambda replaces **anonymous inner classes**.

---

## 3. What if `@FunctionalInterface` is not used?

- Code still works
- Annotation is **optional**
- But compiler won’t warn you if multiple abstract methods are added accidentally

👉 Best practice: **always use it**

---

## 4. What is a Functional Interface?

An interface with **exactly one abstract method**.

### Predefined Functional Interfaces

- `Predicate<T>` → boolean test
- `Function<T, R>` → transform
- `Consumer<T>` → no return
- `Supplier<T>` → returns value

---

## 5. Java 8 improvements in multithreading

- Lambda-based Runnable
- Parallel Streams
- `CompletableFuture`
- Functional style concurrency
- Improved ForkJoinPool usage

---

## 6. Differences in Collections methods (Java 8 additions)

- `forEach()`
- `removeIf()`
- `replaceAll()`
- `computeIfAbsent()`
- Stream support (`stream()`)

---

## 7. Stream API Intermediate Operations

Intermediate operations **do not execute immediately**.

### Examples

```java
list.stream()
    .filter(x -> x > 10)
    .map(x -> x * 2)
    .sorted();

```

Common intermediate ops:

- `filter`
- `map`
- `flatMap`
- `sorted`
- `distinct`
- `limit`

---

## 8. What is Optional?

A container that represents **presence or absence of a value**.

### Common Methods

- `isPresent()`
- `orElse()`
- `orElseGet()`
- `orElseThrow()`
- `ifPresent()`

### Where to use

- Return types
- Stream results

❌ Avoid in fields & method parameters

---

# 🔹 **Collections & Streams**

## 9. Collection vs Collections

| Collection | Collections |
| --- | --- |
| Interface | Utility class |
| Data structure | Helper methods |
| `List`, `Set` | `sort()`, `reverse()` |

---

## 10. Merge two lists using Java 8 Streams

```java
List<Employee> empList3 =
    Stream.concat(empList1.stream(), empList2.stream())
          .collect(Collectors.toList());

```

---

# 🔹 **Spring Boot & JPA**

## 11. Spring Boot annotations used (with purpose)

- `@SpringBootApplication` → bootstraps app
- `@RestController` → REST APIs
- `@Service` → business logic
- `@Repository` → DB operations
- `@Autowired` → dependency injection
- `@Transactional` → transaction management

---

## 12. What is `@PatchMapping`?

Used for **partial updates**.

Example:

```java
PATCH /users/1 { "email": "new@mail.com" }

```

---

## 13. `@Primary` vs `@Qualifier`

- `@Primary` → default bean
- `@Qualifier` → explicit bean selection

---

## 14. `@Component` vs `@Configuration`

- `@Component` → regular Spring bean
- `@Configuration` → defines **bean factory methods**

---

## 15. Types of beans in Spring

- Singleton (default)
- Prototype
- Request
- Session
- Application

---

## 16. Session bean types in Spring Boot

- Singleton
- Prototype
- Request-scoped
- Session-scoped

---

## 17. What is Many-to-One mapping?

Many entities refer to **one parent entity**.

Example:

Many employees → One department

---

## 18. Attributes in `@ManyToOne`

```java
@ManyToOne(fetch = FetchType.LAZY, optional = false)
@JoinColumn(name = "dept_id")

```

- `fetch` → performance
- `optional` → null constraint
- `@JoinColumn` → FK mapping

---

# 🔹 **REST API Scenario**

## 19. API Design

```
/employee/details/123?city=kolkata

```

- `123` → PathVariable (employeeId)
- `city` → RequestParam (filter)

---

## 20. Treat 123 as employeeId

```java
@PathVariable Long employeeId

```

---

## 21. Complete Spring Boot REST Controller

```java
@RestController
@RequestMapping("/employee")
public class EmployeeController {

    @GetMapping("/details/{id}")
    public ResponseEntity<Employee> getEmployeeDetails(
            @PathVariable("id") Long employeeId,
            @RequestParam(required = false) String city) {

        Employee emp = employeeService.findByIdAndCity(employeeId, city);
        return ResponseEntity.ok(emp);
    }
}

```

---

## 22. Line-by-Line Explanation

- `@RestController` → REST endpoints
- `@RequestMapping` → base path
- `@GetMapping` → HTTP GET
- `@PathVariable` → dynamic URL value
- `@RequestParam` → query parameter
- `ResponseEntity` → HTTP status + body

---

# 💡 **Depth-Checking Questions**

## Why prefer Streams over loops?

- Declarative style
- Less boilerplate
- Easy parallelization
- Better readability

---

## When should we avoid Optional?

- Entity fields
- Method parameters
- Serialization models

---

## Common REST API design mistakes

- Using verbs instead of nouns
- Incorrect HTTP status codes
- Exposing internal IDs blindly
- Not handling errors properly

---

## How Java 8 improves readability & performance?

- Lambdas reduce boilerplate
- Streams express intent clearly
- Parallel streams improve I/O scalability
- Optional reduces null checks

---

## 

## ✅ **Senior Java Interview – Crisp Answers**

### 1. ConcurrentHashMap vs SynchronizedMap

- **ConcurrentHashMap**
    - Fine-grained locking + CAS
    - Concurrent reads and concurrent writes on different segments
    - High scalability under contention
- **SynchronizedMap**
    - Single global lock
    - All operations block each other
    - Poor performance under load

👉 Use **ConcurrentHashMap** in multi-threaded systems.

---

### 2. Identifying & fixing memory leaks in Java

**Identify**

- Heap dump analysis (VisualVM, MAT)
- Growing object counts after GC
- Retained references

**Common causes**

- Static references
- Unremoved listeners
- ThreadLocal misuse
- Unbounded caches

**Fix**

- Clear references
- Proper lifecycle cleanup
- Use weak references where appropriate

---

### 3. Thread vs ExecutorService vs Virtual Threads

- **Thread** → Heavy, OS-managed, expensive per thread
- **ExecutorService** → Thread pooling, lifecycle & resource management
- **Virtual Threads (Java 21+)** → Lightweight, JVM-managed, ideal for massive I/O concurrency

---

### 4. When should virtual threads NOT be used?

- CPU-bound workloads
- Long `synchronized` blocks
- Native blocking calls (cause thread pinning)

---

### 5. How does Garbage Collection impact performance?

- Affects **latency (GC pauses)** and **throughput**
- Tuned via:
    - Heap sizing
    - GC selection (G1, ZGC)
    - Reducing object allocation
- Many prod issues blamed on code are actually **GC issues**

---

### 6. synchronized vs Lock

- **synchronized**
    - Simpler, JVM-managed
    - Automatic lock release
- **Lock**
    - `tryLock()`, fairness
    - Interruptible waits
    - More control

👉 Use **Lock** when advanced control is needed.

---

### 7. equals() and hashCode() contract

- If two objects are **equal**, they **must** have the same `hashCode`
- Poor `hashCode` → collisions → degraded `HashMap` performance

---

### 8. How Spring manages transactions internally

- Uses **AOP proxies**
- `@Transactional`:
    - Opens transaction before method
    - Commits on success
    - Rolls back based on exception rules and boundaries

---

### 9. Designing a scalable Java application

- Stateless services
- Caching (Redis, Caffeine)
- Async processing
- Connection pooling
- Observability (metrics, tracing)
- Horizontal scaling

---

### 10. Optional vs null

- **Optional**
    - Explicitly represents absence
    - Reduces NullPointerExceptions
- ❌ Avoid Optional as:
    - Fields
    - Method parameters

---

### 11. Handling high traffic in Java APIs

- Load balancing
- Caching
- Async queues
- Rate limiting
- Proper thread model (virtual threads for I/O)

---

### 12. Fail-fast vs Fail-safe iterators

- **Fail-fast**
    - Throws `ConcurrentModificationException`
    - Example: `ArrayList`
- **Fail-safe**
    - Iterates on a copy
    - Example: `CopyOnWriteArrayList`

---

### 13. Choosing the right data structure

Based on **access pattern**:

- Fast lookup → `HashMap`
- Ordered data → `TreeMap` / `TreeSet`
- Frequent reads → `ArrayList`
- Frequent inserts/removals → `LinkedList`

---

### 14. What makes a senior Java engineer stand out?

- Explains **trade-offs**, not just definitions
- Understands JVM & runtime behavior
- Designs for **scale and failure**
- Writes clean, testable, maintainable code

---

# 🔹 **Java**

### 1. What are virtual threads in Java 21 and when should they be preferred?

Virtual threads are **lightweight JVM-managed threads** designed for massive concurrency.

✅ Prefer for **I/O-bound workloads** (DB calls, REST calls).

❌ Avoid for CPU-bound tasks or long `synchronized` blocks.

---

### 2. Sealed classes vs enums

- **Sealed classes** → restrict which classes can extend them (flexible hierarchy)
- **Enums** → fixed set of constants (limited behavior)
    
    👉 Sealed classes are more powerful and extensible than enums.
    

---

### 3. What are records and their limitations?

Records are **immutable data carriers** with auto-generated constructor, equals, hashCode.

**Limitations**:

- Fields are final
- Cannot extend other classes
- Not suitable for mutable entities

---

### 4. CompletableFuture vs ExecutorService

- **ExecutorService** → manages threads
- **CompletableFuture** → async, non-blocking, composable pipelines
    
    👉 CompletableFuture is better for async workflows.
    

---

### 5. Pattern matching improvement

Simplifies type checks and casting:

```java
if (obj instanceof String s) {
    System.out.println(s.length());
}

```

Less boilerplate, safer code.

---

### 6. HashMap internal working & collisions

- Uses **array of buckets**
- Hash → index
- Collisions handled via **LinkedList → Tree (Red-Black Tree)** when threshold exceeded

---

### 7. Fail-fast vs fail-safe iterators

- **Fail-fast** → throws `ConcurrentModificationException`
- **Fail-safe** → iterates over a copy (e.g., `CopyOnWriteArrayList`)

---

### 8. G1 GC vs ZGC

- **G1** → balanced throughput & latency
- **ZGC** → ultra-low latency (<10ms), higher memory usage

---

### 9. Optional.orElse vs orElseGet

- `orElse()` → value computed **always**
- `orElseGet()` → value computed **lazily**
    
    👉 Use `orElseGet()` for expensive defaults.
    

---

# 🔹 **Spring & Spring Boot**

### 10. Spring Boot auto-configuration

Uses `@EnableAutoConfiguration` + conditional annotations + classpath scanning to auto-configure beans.

---

### 11. Constructor vs field injection

- **Constructor** → immutable, testable (preferred)
- **Field** → hidden dependencies (not recommended)

---

### 12. Global exception handling

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handle(Exception e) {
        return ResponseEntity.badRequest().body(e.getMessage());
    }
}

```

---

### 13. Spring Profiles (real world)

Used for **env-specific configs** (`dev`, `test`, `prod`).

---

### 14. Transaction propagation

- `REQUIRED` → join existing
- `REQUIRES_NEW` → new transaction
- `MANDATORY`, `NESTED` → special cases

---

### 15. Securing REST APIs with JWT

- Authenticate user
- Issue JWT
- Validate JWT in Spring Security filter
- Stateless auth

---

### 16. Spring Boot Actuator

Provides **health, metrics, logs, readiness/liveness endpoints**.

---

### 17. Kafka consumer with Spring Boot

Use `@KafkaListener` + consumer groups + offset management.

---

# 🔹 **Microservices**

### 18. Microservices vs monolith

- Independent scaling
- Faster deployments
- Fault isolation

---

### 19. Saga pattern

Manages **distributed transactions** using compensating actions.

---

### 20. Circuit breakers

Fail fast after failures → recover after cooldown (Resilience4j).

---

### 21. Eventual consistency

Data becomes consistent **over time**, managed via events and retries.

---

# 🔹 **Coding Questions**

### 22. First non-repeating character

```java
public static char firstNonRepeat(String s) {
    Map<Character, Integer> map = new LinkedHashMap<>();
    for (char c : s.toCharArray())
        map.put(c, map.getOrDefault(c, 0) + 1);
    return map.entrySet().stream()
              .filter(e -> e.getValue() == 1)
              .map(Map.Entry::getKey)
              .findFirst().orElse('_');
}

```

---

### 23. Linked list cycle detection (Floyd’s Algorithm)

```java
boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

```

---

### 24. Longest substring without repeating characters

```java
int longest(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0, max = 0;
    for (int right = 0; right < s.length(); right++) {
        while (set.contains(s.charAt(right)))
            set.remove(s.charAt(left++));
        set.add(s.charAt(right));
        max = Math.max(max, right - left + 1);
    }
    return max;
}

```

---

# 🔹 **Others**

### 25. 3rd highest salary

```sql
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

```

---

### 26. Kafka partitions & replication

Partitions enable **parallelism**, replication ensures **fault tolerance**.

---

### 27. Consumer group

Distributes partitions among consumers for scalability.

---

### 28. Docker image vs container

- Image → blueprint
- Container → running instance

---

### 29. Multi-stage Docker build

Reduces image size by separating build & runtime stages.

---

### 30. Deployment vs StatefulSet

- Deployment → stateless
- StatefulSet → stable identity & storage

---

### 31. Liveness vs readiness probes

- Liveness → restart container
- Readiness → traffic routing

---

### 32. Idempotency in REST

Same request → same result (idempotency keys).

---

### 33. API versioning

Ensures backward compatibility (`/v1`, headers).

---

### 34. Horizontal Pod Autoscaling

Scales pods based on CPU/memory/custom metrics.

---

### 35. Dead-letter queue

Stores failed messages for retry or analysis.

---

### 36. Securing secrets

Use **Vault, KMS, Secrets Manager**, never hardcode.

---

### 37. Sync REST vs async messaging

- REST → immediate response
- Messaging → decoupled, resilient, scalable

---

## 

# 🟢 Core JPA Fundamentals

## 1. What is JPA and how is it different from Hibernate?

- **JPA** → A **specification** (rules & APIs for ORM)
- **Hibernate** → An **implementation** of JPA (plus extra features)

👉 JPA defines *what*, Hibernate defines *how*.

---

## 2. Main components of JPA architecture

- Entity
- EntityManager
- Persistence Context
- Query / JPQL
- Transaction Manager
- DataSource

---

## 3. What is an Entity?

An entity is a **persistent Java object** mapped to a database table.

### Requirements:

- Annotated with `@Entity`
- Must have a primary key (`@Id`)
- Must have a no-args constructor
- Must not be final

---

## 4. Role of @Entity, @Table, @Id

- `@Entity` → Marks class as JPA entity
- `@Table` → Maps entity to DB table
- `@Id` → Identifies primary key

---

## 5. What is persistence.xml? Is it required in Spring Boot?

- Defines persistence unit, DB config
- ❌ **Not required in Spring Boot**
- Spring Boot auto-configures via `application.yml/properties`

---

## 6. What is EntityManager?

- Core JPA interface
- Manages:
    - Entity lifecycle
    - Persistence context
    - Queries
    - Transactions

---

## 7. EntityManager vs Hibernate Session

- `EntityManager` → JPA standard
- `Session` → Hibernate specific
- Internally, EntityManager delegates to Session

---

## 8. What is a Persistence Context?

A **first-level cache** that tracks managed entities.

👉 One entity instance per DB row per context.

---

## 9. Lifecycle of a JPA entity

```
Transient →Managed →Detached →Removed

```

---

## 10. What is dirty checking?

Hibernate tracks changes to managed entities and **automatically updates DB** at flush/commit time.

---

# 🟢 Entity Lifecycle & State Management

## 11. Entity States

- **Transient** → New, not tracked
- **Managed** → Tracked by persistence context
- **Detached** → Not tracked
- **Removed** → Scheduled for delete

---

## 12. What happens when entity becomes detached?

- Changes are **not persisted**
- Must use `merge()` to reattach

---

## 13. persist() vs merge() vs save()

- `persist()` → New entity only
- `merge()` → Copies state to managed entity
- `save()` → Hibernate-specific (persist + merge behavior)

---

## 14. When are changes flushed to DB?

- Transaction commit
- Explicit `flush()`
- Before query execution (sometimes)

---

## 15. flush() vs commit()

- `flush()` → Syncs SQL with DB
- `commit()` → Ends transaction + flushes

---

## 16. Updating entity without save()

Works if entity is **managed** (dirty checking).

---

## 17. How does JPA detect changes?

- Snapshot comparison
- Bytecode enhancement (Hibernate)

---

# 🟢 Mapping Annotations & Relationships

## 18. Relationship annotations

- `@OneToOne`
- `@OneToMany`
- `@ManyToOne`
- `@ManyToMany`

---

## 19. Owning side of relationship

- Side with **foreign key**
- Uses `@JoinColumn`

---

## 20. mappedBy vs @JoinColumn

- `mappedBy` → Inverse side
- `@JoinColumn` → Owning side

---

## 21. Bidirectional mapping

Both entities reference each other using mappedBy.

---

## 22. Default fetch types

- `@OneToMany` → **LAZY**
- `@ManyToOne` → **EAGER**

---

## 23. Problems with bidirectional relationships

- Infinite JSON recursion
- N+1 queries
- Complex state management

---

## 24. Cascading

Automatically propagates operations.

### Types:

- PERSIST
- MERGE
- REMOVE
- REFRESH
- DETACH
- ALL

---

## 25. CascadeType.ALL vs orphanRemoval

- `Cascade.ALL` → propagates operations
- `orphanRemoval=true` → deletes child when removed from parent

---

## 26. Avoid infinite recursion

- `@JsonIgnore`
- `@JsonManagedReference / @JsonBackReference`
- DTO mapping (best)

---

## 27. Composite primary keys

- `@Embeddable + @EmbeddedId`
- or `@IdClass`

---

# 🟢 Fetching Strategies

## 28. Lazy loading

Data fetched **on demand**

---

## 29. Eager loading

Data fetched **immediately**

---

## 30. N+1 select problem

One query for parent + N queries for children.

---

## 31. Solving N+1

- `JOIN FETCH`
- `@EntityGraph`
- Batch fetching

---

## 32. JOIN vs JOIN FETCH

- `JOIN` → joins for filtering
- `JOIN FETCH` → joins + loads data

---

## 33. Accessing lazy collection outside transaction

Throws **LazyInitializationException**

---

## 34. LazyInitializationException

Occurs when persistence context is closed before lazy loading.

---

## 35. Fetch strategy & performance

- EAGER → memory & performance issues
- LAZY → safer default

---

## 36. When to use @EntityGraph?

- Override fetch strategy dynamically
- Avoid N+1 without changing mapping

---

# 🟢 JPQL & Queries

## 37. What is JPQL?

Object-oriented query language operating on **entities**, not tables.

---

## 38. JPQL vs Native query

- JPQL → DB independent
- Native → DB specific, faster in some cases

---

## 39. JPQL Join

```java
SELECT e FROM Employee e JOIN e.department d

```

---

## 40. Named Query

Predefined JPQL query for reuse and performance.

---

## 41. Pagination in JPA

```java
query.setFirstResult(offset);
query.setMaxResults(limit);

```

---

## 42. Dynamic queries

- Criteria API
- QueryDSL
- Specifications

---

## 43. Criteria API

Type-safe dynamic query builder.

### Pros:

- Compile-time safety

### Cons:

- Verbose
- Hard to read

---

## 44. Projections in JPQL

```java
SELECTnewcom.dto.EmpDTO(e.name, e.salary)
FROM Employee e

```

---

## 45. Fetching selected columns

- Constructor expressions
- Interface-based projections (Spring Data)

---

# 

Below is a **concise, senior-level learning & interview guide** to all the topics you listed.

Think of this as a **distributed systems + Java backend master map** — short, clear, and explainable.

---

# 🌍 Distributed Systems & Java – Core Concepts Cheat Sheet

---

## 1. CAP Theorem

A distributed system can guarantee **only two** of:

- **Consistency** – all nodes see the same data
- **Availability** – every request gets a response
- **Partition Tolerance** – system works despite network splits

👉 In practice, systems choose **CP or AP**.

---

## 2. Consistency Models

- **Strong consistency** – read always gets latest write
- **Eventual consistency** – data converges over time
- **Read-after-write** – user sees own updates
- **Causal consistency** – related updates stay ordered

---

## 3. Distributed System Architectures

- Monolith
- Microservices
- Event-driven
- Peer-to-peer
- Master–worker

---

## 4. Socket Programming (TCP/IP & UDP)

- **TCP** – reliable, ordered, connection-oriented
- **UDP** – fast, connectionless, no guarantee
    
    Used in low-level networking, games, streaming.
    

---

## 5. HTTP & RESTful APIs

- Stateless communication
- Resource-based URLs
- Uses HTTP verbs (GET, POST, PUT, DELETE)

---

## 6. RPC (gRPC, Thrift, RMI)

- Method-based communication
- Faster than REST
- Strong contracts (IDL)
- gRPC uses HTTP/2 + Protobuf

---

## 7. Message Queues

- Decouple producers & consumers
- Async communication
- Kafka (streaming), RabbitMQ (queue), JMS (API)

---

## 8. Java Concurrency

- **ExecutorService** – thread pooling
- **Future** – async result
- **ForkJoinPool** – divide & conquer tasks

---

## 9. Thread Safety & Synchronization

- synchronized
- locks
- atomic variables
- immutable objects

---

## 10. Java Memory Model (JMM)

Defines **visibility, ordering, atomicity** across threads

Uses happens-before rules.

---

## 11. Distributed Databases

- Cassandra → AP
- MongoDB → CP/AP configurable
- HBase → CP
    
    Designed for scalability & fault tolerance.
    

---

## 12. Data Sharding & Partitioning

- Split data horizontally
- Improves scalability
- Adds complexity (joins, transactions)

---

## 13. Caching Mechanisms

- Redis, Memcached → distributed cache
- Ehcache → in-process
    
    Reduces latency & DB load.
    

---

## 14. Zookeeper (Coordination)

Used for:

- Leader election
- Distributed locks
- Configuration management

---

## 15. Consensus Algorithms

- **Paxos** – complex, theoretical
- **Raft** – simpler, production-friendly
    
    Ensures agreement among nodes.
    

---

## 16. Distributed Locks

- Zookeeper – strong consistency
- Redis – fast, needs careful setup (Redlock)

---

## 17. Spring Boot & Spring Cloud

- Config management
- Service discovery
- Circuit breakers
- Distributed tracing

---

## 18. Service Discovery

- Dynamic service registration & lookup
- Eliminates hardcoded endpoints

---

## 19. API Gateways

- Single entry point
- Routing, auth, rate limiting
- NGINX, Zuul, Spring Cloud Gateway

---

## 20. Inter-service Communication

- REST → simple, synchronous
- gRPC → fast, contract-based
- Kafka → async, event-driven

---

## 21. Circuit Breaker & Retry

- Prevent cascading failures
- Fail fast
- Auto-recovery after cooldown

---

## 22. Load Balancing

- Distributes traffic
- Client-side or server-side
- Improves availability & throughput

---

## 23. Failover Mechanisms

- Detect failure
- Switch to healthy node
- Ensures high availability

---

## 24. Distributed Transactions

- **2PC** – strong consistency, slow
- **Saga** – eventual consistency, scalable

---

## 25. Logging & Distributed Tracing

- Centralized logs
- Trace request across services
- Correlate using trace/span IDs

---

## 26. Monitoring & Metrics

- CPU, memory, latency, errors
- Observability = metrics + logs + traces

---

## 27. Alerting Systems

- Notify on SLA breach
- Based on thresholds & anomalies

---

## 28. Authentication & Authorization

- OAuth → delegated auth
- JWT → stateless tokens

---

## 29. Encryption (SSL/TLS)

- Data-in-transit protection
- Certificates + public/private keys

---

## 30. Rate Limiting & Throttling

- Prevent abuse
- Protect downstream systems
- Token bucket / leaky bucket

---

## 31. Apache Kafka (Streaming)

- Partitioned log
- High throughput
- Durable event storage

---

## 32. Apache Zookeeper

- Distributed coordination backbone
- Used by Kafka, HBase, etc.

---

## 33. In-memory Data Grids

- Distributed memory store
- Shared state & fast access

---

## 34. Akka (Actor Model)

- Message-based concurrency
- No shared state
- Fault tolerance via supervision

---

## 35. Event-Driven Architecture

- Event sourcing → store events
- CQRS → separate read/write models
- High scalability & auditability

---

## 36. Cluster Management (Kubernetes)

- Container orchestration
- Auto-scaling
- Self-healing

---

## 37. Cloud-Native Development

- Managed services
- Elastic scaling
- Serverless (functions as a service)

---

## 38. Distributed Data Processing

- Batch + stream processing
- Parallel execution
- Fault tolerance

---

## 39. GraphQL

- Client-driven queries
- Reduces over/under fetching
- Strong schema

---

## 40. JVM Tuning for Distributed Systems

- Heap sizing
- GC selection
- Thread tuning
- Memory leak prevention

---

## 🧠 Final Interview Takeaway

> Distributed systems are about trade-offs, failure handling, and observability, not just technology choices.
> 

---

Here’s a **clean, learning-focused + interview-ready summary** of how `@Transactional` really works — easy to remember, easy to explain.

---

## 🔹 `@Transactional` — What It *Really* Does

`@Transactional` defines a **logical unit of work** where multiple DB operations behave as **one atomic action**:

- ✅ All succeed → **COMMIT**
- ❌ Any failure → **ROLLBACK**

---

## 🔹 How Spring Implements `@Transactional`

Spring does **not** add magic inside your method. It uses:

- **AOP + Proxy**
- **Transaction Manager**
- **Database commit / rollback**

That’s why these rules exist:

- ✅ Works only on **public methods**
- ❌ **Self-invocation** (internal method calls) bypass transactions
- 🔄 By default, rollback happens only for **RuntimeException**

👉 These are **design constraints**, not bugs.

---

## 🔹 Isolation Levels — Why They Matter

When multiple users hit the DB concurrently, these problems occur:

- **Dirty Read** → reading uncommitted data
- **Non-Repeatable Read** → same row, different values
- **Phantom Read** → new rows appear mid-transaction

### Isolation levels control this trade-off:

| Isolation Level | Prevents | Cost |
| --- | --- | --- |
| READ_COMMITTED | Dirty reads | Low |
| REPEATABLE_READ | Non-repeatable reads | Medium |
| SERIALIZABLE | All issues | High (locking) |

👉 **Higher isolation = safer data, slower performance**

---

## 🔹 Transaction Propagation — The Real Brain 🧠

Propagation defines **what happens when one transactional method calls another**.

### Most commonly used:

- **REQUIRED** *(default)*
    
    → Join existing transaction or create a new one
    
- **REQUIRES_NEW**
    
    → Suspend current, start a new transaction
    
- **MANDATORY**
    
    → Must already have a transaction
    
- **NEVER**
    
    → Must run without a transaction
    

---

## 🔹 Real-World Example

**PaymentService → AuditService**

- Same transaction?
    
    → Audit rolls back if payment fails
    
- Separate transaction?
    
    → Audit logs even if payment fails
    

👉 **Propagation decides business correctness.**

---

## 🧠 One-Line Learning Takeaway

> @Transactional is not just an annotation — it’s about proxies, boundaries, isolation trade-offs, and propagation decisions.
> 

---

---

# 🔥 TOP 30 Java Stream API Coding Problems (With Solutions)

---

## 🧠 STRING-BASED STREAM PROBLEMS

### 1️⃣ First non-repeated character

```java
char result = str.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(c -> c, LinkedHashMap::new, Collectors.counting()))
    .entrySet().stream()
    .filter(e -> e.getValue() == 1)
    .map(Map.Entry::getKey)
    .findFirst().orElse('_');

```

---

### 2️⃣ First repeated character

```java
char result = str.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(c -> c, LinkedHashMap::new, Collectors.counting()))
    .entrySet().stream()
    .filter(e -> e.getValue() > 1)
    .map(Map.Entry::getKey)
    .findFirst().orElse('_');

```

---

### 3️⃣ All non-repeated characters

```java
List<Character> list =
str.chars().mapToObj(c -> (char) c)
   .collect(Collectors.groupingBy(c -> c, Collectors.counting()))
   .entrySet().stream()
   .filter(e -> e.getValue() == 1)
   .map(Map.Entry::getKey)
   .toList();

```

---

### 4️⃣ Character frequency count

```java
Map<Character, Long> map =
str.chars().mapToObj(c -> (char) c)
   .collect(Collectors.groupingBy(c -> c, Collectors.counting()));

```

---

### 5️⃣ Anagram check

```java
boolean isAnagram =
str1.chars().sorted().boxed().toList()
.equals(str2.chars().sorted().boxed().toList());

```

---

### 6️⃣ Reverse each word

```java
String result =
Arrays.stream(sentence.split(" "))
      .map(w -> new StringBuilder(w).reverse().toString())
      .collect(Collectors.joining(" "));

```

---

### 7️⃣ Longest word

```java
String longest =
Arrays.stream(sentence.split(" "))
      .max(Comparator.comparingInt(String::length))
      .orElse("");

```

---

### 8️⃣ Remove duplicate characters

```java
String result =
str.chars().distinct()
   .mapToObj(c -> String.valueOf((char) c))
   .collect(Collectors.joining());

```

---

### 9️⃣ Sort characters alphabetically

```java
String result =
str.chars().sorted()
   .mapToObj(c -> String.valueOf((char) c))
   .collect(Collectors.joining());

```

---

### 🔟 Count vowels & consonants

```java
long vowels =
str.toLowerCase().chars()
   .filter(c -> "aeiou".indexOf(c) != -1)
   .count();

```

---

## 🔢 NUMBER-BASED STREAM PROBLEMS

### 1️⃣1️⃣ Duplicate numbers

```java
Set<Integer> dup =
list.stream()
    .filter(n -> Collections.frequency(list, n) > 1)
    .collect(Collectors.toSet());

```

---

### 1️⃣2️⃣ Unique numbers

```java
list.stream().distinct().toList();

```

---

### 1️⃣3️⃣ Second highest number

```java
int second =
list.stream().distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1).findFirst().orElse(0);

```

---

### 1️⃣4️⃣ Max & Min

```java
int max = list.stream().max(Integer::compare).get();
int min = list.stream().min(Integer::compare).get();

```

---

### 1️⃣5️⃣ Sum of numbers

```java
int sum = list.stream().mapToInt(Integer::intValue).sum();

```

---

### 1️⃣6️⃣ Count even & odd

```java
Map<Boolean, Long> map =
list.stream().collect(Collectors.partitioningBy(n -> n % 2 == 0, Collectors.counting()));

```

---

### 1️⃣7️⃣ Sort ascending & descending

```java
list.stream().sorted().toList();
list.stream().sorted(Comparator.reverseOrder()).toList();

```

---

### 1️⃣8️⃣ Numbers starting with 1

```java
list.stream()
    .map(String::valueOf)
    .filter(s -> s.startsWith("1"))
    .map(Integer::valueOf)
    .toList();

```

---

### 1️⃣9️⃣ Remove duplicates

```java
list.stream().distinct().toList();

```

---

### 2️⃣0️⃣ Average

```java
double avg = list.stream().mapToInt(Integer::intValue).average().orElse(0);

```

---

## 👨‍💻 EMPLOYEE / OBJECT-BASED (INTERVIEW FAVORITE)

Assume:

```java
class Employee {
  int id;
  String name;
  String dept;
  double salary;
  int age;
}

```

---

### 2️⃣1️⃣ Group by department

```java
Map<String, List<Employee>> map =
emps.stream().collect(Collectors.groupingBy(Employee::getDept));

```

---

### 2️⃣2️⃣ Highest salary employee

```java
Employee e =
emps.stream().max(Comparator.comparing(Employee::getSalary)).get();

```

---

### 2️⃣3️⃣ Average salary per department

```java
Map<String, Double> map =
emps.stream().collect(Collectors.groupingBy(
Employee::getDept, Collectors.averagingDouble(Employee::getSalary)));

```

---

### 2️⃣4️⃣ Sort by salary then name

```java
emps.stream()
    .sorted(Comparator.comparing(Employee::getSalary)
    .thenComparing(Employee::getName))
    .toList();

```

---

### 2️⃣5️⃣ Salary greater than X

```java
emps.stream().filter(e -> e.getSalary() > x).toList();

```

---

### 2️⃣6️⃣ Youngest / Oldest

```java
Employee youngest = emps.stream().min(Comparator.comparing(Employee::getAge)).get();
Employee oldest   = emps.stream().max(Comparator.comparing(Employee::getAge)).get();

```

---

### 2️⃣7️⃣ Count per department

```java
Map<String, Long> map =
emps.stream().collect(Collectors.groupingBy(Employee::getDept, Collectors.counting()));

```

---

### 2️⃣8️⃣ Department with max employees

```java
String dept =
emps.stream().collect(Collectors.groupingBy(Employee::getDept, Collectors.counting()))
.entrySet().stream().max(Map.Entry.comparingByValue()).get().getKey();

```

---

### 2️⃣9️⃣ Second highest salary employee

```java
Employee e =
emps.stream().sorted(Comparator.comparing(Employee::getSalary).reversed())
.skip(1).findFirst().get();

```

---

### 3️⃣0️⃣ List → Map (id, name)

```java
Map<Integer, String> map =
emps.stream().collect(Collectors.toMap(Employee::getId, Employee::getName));

```

---

Here’s a **clean, learning-oriented + interview-ready summary** of **Serverless Spring Boot on AWS**, focused on *architecture and trade-offs*.

---

## ☁️ Serverless Spring Boot on AWS — Architecture Explained

### 🔹 Core Idea

A traditional **Spring Boot REST application** can run **fully serverless** on AWS by deploying it on **AWS Lambda behind API Gateway**, instead of EC2/ECS.

Using **AWS Serverless Java Container**, existing Spring MVC controllers work **without code changes**, while AWS handles:

- Scaling
- Availability
- Infrastructure

---

## 🔹 Key Architecture Components

### 1️⃣ API Gateway (Front Door)

Handles:

- Routing HTTP requests
- Authentication & authorization
- Rate limiting & throttling
- Request validation

👉 Acts as the **managed API layer**.

---

### 2️⃣ AWS Lambda (Execution Layer)

- Spring Boot runs **on-demand**
- No servers to manage
- No cost when idle
- Automatic scaling per request

👉 Execution is **event-driven**, not always-on.

---

### 3️⃣ Cold Start Optimization (Critical for Java)

Handled using:

- **Java 17**
- **Lambda SnapStart**
- Reduced Spring auto-configuration
- Smaller dependency footprint

👉 Minimizes startup latency, which is the main Java serverless challenge.

---

### 4️⃣ Data Layer

Common patterns:

- **DynamoDB** → fully serverless, low latency
- **Aurora Serverless** → relational workloads
- **RDS Proxy** → connection pooling for Lambda

👉 Prevents DB connection exhaustion under scale.

---

### 5️⃣ Observability

- **CloudWatch Logs** → centralized logging
- **CloudWatch Metrics** → latency, errors, cold starts
- Optional tracing with X-Ray

👉 Essential because debugging serverless is log-driven.

---

## 🔹 Why This Architecture Works Well

### ✅ Benefits

- True **auto-scaling**
- **Pay-per-use** pricing
- High availability by default
- Strong security governance
- No server maintenance

### ⚠️ Trade-offs

- Cold start latency (needs tuning)
- Not ideal for long-running or CPU-heavy workloads
- Debugging relies heavily on logs & metrics

---

## 🔹 Ideal Use Cases

- Microservices
- Event-driven systems
- APIs with bursty or unpredictable traffic
- Cost-sensitive workloads

---

## 🧠 One-Line Takeaway

> Serverless Spring Boot on AWS shifts responsibility from infrastructure management to architecture, cold-start optimization, and observability, enabling scalable and cost-efficient systems.
> 

---

---

## ✅ **When Should You Use Microservices Architecture?**

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
    

## ✅ **When Should You Use Microservices Architecture?**

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

## 🔹 Communication & Networking

**1. Synchronous vs Asynchronous communication**

- **Synchronous**: Caller waits for response (REST).
- **Asynchronous**: Caller doesn’t block (Kafka, queues).

---

**2. REST vs gRPC**

- **REST**: JSON, HTTP/1.1, human-readable, slower.
- **gRPC**: Protobuf, HTTP/2, binary, faster, strongly typed.

---

**3. HTTP/2 vs HTTP/3**

- **HTTP/2**: Multiplexing over TCP.
- **HTTP/3**: Runs over QUIC (UDP), faster connection recovery.

---

**4. Connection pooling & why needed**

Reuses DB connections to avoid expensive creation and exhaustion.

---

**5. HikariCP internal working**

- Fast, lightweight pool
- Uses minimal locking
- Validates connections lazily
- Maintains optimal pool size

---

## 🔹 Threads & Concurrency

**6. Thread pool & tuning**

Manages reusable threads.

Tune via pool size, queue size, rejection policy.

---

**7. ForkJoinPool**

Work-stealing pool for divide-and-conquer parallel tasks.

---

**8. Garbage Collection in JVM**

Automatically frees unreachable objects using generational GC.

---

**9. G1 GC vs ZGC**

- **G1**: Balanced latency & throughput.
- **ZGC**: Ultra-low latency (<10ms), more memory usage.

---

## 🔹 Memory & JVM Internals

**10. Memory leak in Java**

Objects referenced but never used → heap grows endlessly.

---

**11. OOM vs StackOverflowError**

- **OOM**: Heap/Metaspace exhausted.
- **StackOverflow**: Deep or infinite recursion.

---

**12. ClassLoader hierarchy**

Bootstrap → Platform → Application → Custom loaders.

---

**13. Metaspace**

Stores class metadata (replaced PermGen). Uses native memory.

---

**14. JIT Compiler**

Compiles hot bytecode to native machine code at runtime.

---

**15. Escape Analysis**

Detects if objects can be stack-allocated or eliminated.

---

## 🔹 Async & Reactive

**16. CompletableFuture chaining**

Compose async tasks using `thenApply`, `thenCompose`, `thenAccept`.

---

**17. Reactive backpressure**

Consumer controls producer speed to avoid overload.

---

## 🔹 Architecture Patterns

**18. Event sourcing**

Store state as a sequence of events, not rows.

---

**19. CQRS**

Separate read and write models for scalability.

---

## 🔹 Databases

**20. Database sharding**

Split data horizontally across nodes.

---

**21. Read replica**

Read-only DB copy for scaling reads.

---

**22. Eventual vs Strong consistency**

- **Strong**: Always latest data.
- **Eventual**: Consistent over time.

---

**23. Two-Phase Commit (2PC)**

Distributed transaction protocol (slow, blocking).

---

## 🔹 JPA & Persistence

**24. ID generation strategies**

AUTO, IDENTITY, SEQUENCE, TABLE.

---

**25. Optimistic locking (version column)**

Uses `@Version` to detect concurrent updates.

---

**26. Soft delete**

Mark records as deleted instead of removing (e.g., `is_deleted`).

---

**27. Audit logging design**

Store who/when/what changed using DB tables or events.

---

## 🔹 Scalability & Reliability

**28. API rate limiting with Redis**

Use counters or token bucket stored in Redis.

---

**29. Token bucket vs Leaky bucket**

- **Token**: Allows bursts.
- **Leaky**: Smooth, constant rate.

---

**30. Distributed cache coherence**

Ensures all cache nodes see consistent data.

---

**31. Hazelcast**

In-memory distributed data grid.

---

## 🔹 Kafka

**32. Message ordering in Kafka**

Guaranteed **per partition**, not globally.

---

**33. Kafka partition rebalance**

Redistributes partitions when consumers change.

---

**34. Dead Letter Queue (DLQ)**

Stores failed messages for later analysis.

---

## 🔹 Resilience Patterns

**35. Retry with exponential backoff**

Retries with increasing delay to reduce pressure.

---

**36. Timeout vs Circuit Breaker**

- **Timeout**: Limits wait time.
- **Circuit Breaker**: Stops calls after failures.

---

**37. Graceful degradation**

System continues with reduced functionality.

---

**38. Fallback mechanism**

Alternative response when primary fails.

---

## 🔹 Deployment & Ops

**39. Readiness vs Liveness**

- **Readiness**: Can receive traffic
- **Liveness**: Should be restarted?

---

**40. Blue-green vs Rolling deployment**

- **Blue-green**: Instant switch
- **Rolling**: Gradual update

---

## 🔹 Microservices Infra

**41. Sidecar pattern**

Attach helper container (logging, proxy, security).

---

**42. Service discovery**

Dynamic lookup of service instances.

---

**43. API throttling**

Limits request rate to protect systems.

---

## 🔹 Security

**44. Zero Trust Security**

Never trust—always verify, even inside network.

---

**45. mTLS**

Mutual TLS: both client and server authenticate.

---

**46. Secrets management**

Secure storage of credentials (Vault, KMS).

---

## 🔹 DevOps & Product Control

**47. Config hot reload**

Update config without restart.

---

**48. Feature toggle**

Enable/disable features at runtime.

---

**49. Chaos engineering**

Intentionally inject failures to test resilience.

---

## 🔹 System Design

**50. Designing fault-tolerant microservices**

- Stateless services
- Retries + circuit breakers
- Caching
- Observability
- Graceful degradation

---

---

## 🔹 Round 2: Managerial / Techno-Managerial Interview

**Focus:** *Real-world experience, decision-making, ownership, and teamwork*

👉 Less theory, more **how you think and act in real projects**

---

## 1️⃣ Project & Technical Discussion

### What the interviewer is checking

- Do you **understand your project end-to-end**, or only your module?
- Do you **own problems**, or just execute tasks?

### How to answer well

**Explain your current project architecture**

- Start high-level → client → API → service → DB → integrations
- Mention tech stack and why it was chosen

> “We have a Spring Boot microservices-based system, exposed via REST APIs, deployed on cloud, with Redis for caching and Kafka for async communication…”
> 

---

**Your role & responsibilities**

- Be specific
- Mention **design + development + support**

> “I was responsible for API design, implementing business logic, handling performance issues, and supporting P1 incidents.”
> 

---

**Biggest technical challenge**

Use **STAR method**:

- Situation
- Task
- Action
- Result

> Example: performance issue, concurrency bug, memory leak, transaction issue
> 

---

**Handling production issues / P1 defects**

They expect:

- Calm approach
- Ownership
- Communication

Good answer includes:

- Logs + metrics first
- Rollback / feature flag if needed
- Root cause analysis
- Permanent fix

---

**Performance improvements**

Mention **measurable impact**:

- Reduced API latency
- Added caching
- Fixed N+1 queries
- Optimized DB indexes

---

## 2️⃣ Design & Decision Making

### Scalable REST API

They expect **design thinking**, not code.

Mention:

- Stateless APIs
- Pagination
- Caching
- Rate limiting
- Proper HTTP status codes

---

### Handling concurrent user requests

Strong answers include:

- Thread pools
- DB locking strategy (optimistic)
- Idempotency
- Async processing

---

### Application security

Mention:

- Authentication & authorization
- Input validation
- HTTPS
- Secure headers
- JWT / OAuth

---

### Microservices experience

Be honest. Even partial experience is fine.

They look for:

- Why microservices?
- Trade-offs
- Challenges (network calls, debugging)

---

### Inter-service communication

Mention:

- REST for sync
- Kafka / messaging for async
- Retry + circuit breaker

---

## 3️⃣ Code Quality & Process

### Code reviews – what do you check?

They want **maturity**, not nitpicking.

Mention:

- Readability
- Naming
- SOLID principles
- Edge cases
- Performance impact
- Test coverage

---

### AI usage (Copilot, etc.)

Answer positively but responsibly:

> “We use AI tools for boilerplate or suggestions, but final logic, security, and design decisions are always reviewed manually.”
> 

---

### Clean & maintainable code

Mention:

- Small methods
- Clear naming
- Separation of concerns
- Refactoring mindset

---

### Unit testing (JUnit / Mockito)

They expect basics:

- Mock dependencies
- Test happy + negative paths
- Focus on business logic

---

### Task estimation & deadlines

Good answer:

- Break tasks into smaller units
- Buffer for unknowns
- Communicate early if blocked

---

## 4️⃣ Team & Behavioral

### Handling team conflict

They look for **emotional maturity**.

Good approach:

- Listen first
- Discuss facts, not people
- Involve lead if needed

---

### Mentoring juniors

Mention:

- Code reviews
- Pair programming
- Explaining “why”, not just “what”

---

### Agile / Scrum experience

Mention:

- Sprint planning
- Daily standups
- Retrospectives
- Story estimation

---

### Handling pressure during tight releases

They want **stability**, not heroics.

Mention:

- Prioritization
- Team coordination
- Staying calm
- Post-release cleanup

---

## 🧠 One-Line Interview Takeaway

> This round is about how reliable you are as an engineer and teammate, not how many APIs or annotations you remember.
> 

---

# 🟢 Beginner Level

### 1. What is Microservice Architecture?

Microservices architecture is a design style where an application is built as a **collection of small, independent services**, each responsible for a specific business capability and deployable independently.

---

### 2. Monolithic vs Microservices – key differences

| Monolithic | Microservices |
| --- | --- |
| Single deployable unit | Multiple independent services |
| Tight coupling | Loose coupling |
| Scale whole app | Scale individual services |
| Slower releases | Faster, independent releases |

---

### 3. Why do companies move from monolith to microservices?

- Faster development & releases
- Independent scaling
- Better fault isolation
- Team autonomy

---

### 4. Advantages of microservices

- Independent deployment
- Better scalability
- Technology flexibility
- Improved fault tolerance

---

### 5. What is REST API in microservices?

REST APIs expose **service functionality over HTTP** using standard methods like GET, POST, PUT, DELETE.

---

### 6. What is service-to-service communication?

How microservices talk to each other, either:

- **Synchronous** (REST, Feign)
- **Asynchronous** (Kafka, messaging)

---

# 🟡 Intermediate Level

### 7. What is Service Discovery and why is it needed?

Service discovery helps services **find each other dynamically**, since IPs/ports change in cloud environments.

Examples: Eureka, Consul, Kubernetes DNS.

---

### 8. What is API Gateway? Why not call services directly?

API Gateway acts as a **single entry point** that handles:

- Authentication
- Routing
- Rate limiting
- Logging

👉 Calling services directly increases coupling and security risk.

---

### 9. How do microservices communicate?

- **REST / Feign** → synchronous calls
- **Kafka / Messaging** → asynchronous, event-driven

Best systems use **both**, based on use case.

---

### 10. What is Load Balancing in microservices?

Distributes traffic across multiple instances to improve:

- Availability
- Performance
- Fault tolerance

Can be client-side or server-side.

---

### 11. What is Centralized Configuration?

Stores configuration in one place (Git, Config Server) so services can:

- Share configs
- Change config without redeploy

---

### 12. How do you handle inter-service failures?

- Timeouts
- Retries (with backoff)
- Circuit breakers
- Fallback responses

---

# 🔵 Advanced Level

### 13. What is Circuit Breaker pattern?

Stops calling a failing service after repeated errors, allowing it time to recover and preventing cascading failures.

---

### 14. What is Distributed Tracing?

Tracks a single request **across multiple services** using trace IDs.

Tools: Zipkin, Jaeger.

---

### 15. How do you secure microservices?

- Authentication (OAuth2, JWT)
- Authorization
- mTLS
- API Gateway security
- Network policies

---

### 16. What is Event-Driven Microservices?

Services communicate by **publishing and consuming events** instead of direct calls, improving decoupling and scalability.

---

### 17. How do you manage transactions in microservices?

Avoid distributed DB transactions.

Use:

- Event-based approach
- Saga pattern
- Compensation logic

---

### 18. What is Saga Pattern?

A sequence of **local transactions**, where each step has a **compensating action** if something fails.

---

# 🟣 Scenario-Based Questions (Interview Favorites)

### 19. One microservice is slow — how will you debug?

- Check metrics & logs
- Analyze latency (DB, external calls)
- Use distributed tracing
- Check thread pool & GC

---

### 20. How do you handle failure of one service without impacting others?

- Circuit breaker
- Fallback responses
- Async communication
- Graceful degradation

---

### 21. How will you scale only one microservice?

- Deploy multiple instances of that service
- Use load balancer / Kubernetes HPA
- No need to scale entire system

---

### 22. How do you track a request across services?

- Correlation ID / Trace ID
- Distributed tracing tools (Zipkin, Jaeger)

---

### 23. Database per service – why recommended?

- Prevents tight coupling
- Independent schema changes
- Better fault isolation

---

### 24. How do you deploy microservices independently?

- CI/CD per service
- Containerization (Docker)
- Orchestration (Kubernetes)
- Versioned APIs

Below is a **senior-level, interview-ready answer pack** for all **50 advanced Java Backend questions**.

Each answer is **concise, technically accurate, and focused on “how it works internally + why it matters”**—exactly what interviewers expect.

---

# ✅ Java Backend Interview – 50 Advanced Answers

*(Spring Boot + Microservices)*

---

## 🌱 Spring Boot Core

### 1. How does Spring Boot auto-configuration work internally?

Uses `@EnableAutoConfiguration` → `AutoConfigurationImportSelector` → loads auto-configs from

`META-INF/spring.factories` / `AutoConfiguration.imports`, applied conditionally using `@ConditionalOnClass`, `@ConditionalOnBean`, etc.

---

### 2. What happens during application startup lifecycle?

1. Bootstrap ApplicationContext
2. Load environment & configs
3. Component scan
4. Auto-configuration
5. Bean instantiation & dependency injection
6. BeanPostProcessors
7. Context refresh → app ready

---

### 3. @ComponentScan vs @EnableAutoConfiguration

- **@ComponentScan** → finds user-defined beans
- **@EnableAutoConfiguration** → configures framework beans automatically

---

### 4. BeanFactory vs ApplicationContext

- **BeanFactory** → lazy, minimal
- **ApplicationContext** → eager, supports AOP, events, i18n (used in real apps)

---

### 5. Circular dependency & resolution

Occurs when A → B → A.

Fix via:

- Setter injection
- `@Lazy`
- Refactoring (best)

---

### 6. Thread safety of singleton beans

Spring does **not** make beans thread-safe.

Beans should be **stateless** or handle synchronization explicitly.

---

## 🧩 AOP & Transactions

### 7. What is a proxy in Spring AOP?

A wrapper object that intercepts method calls to apply cross-cutting concerns (transactions, logging, security).

---

### 8. JDK Proxy vs CGLIB

- **JDK Proxy** → interfaces only
- **CGLIB** → subclass-based, works without interfaces

---

### 9. How does `@Transactional` work internally?

- Implemented via AOP proxy
- Opens transaction before method
- Commits or rolls back based on exceptions & propagation rules

---

### 10. Transaction propagation & isolation

- **Propagation** → how transactions join/suspend (`REQUIRED`, `REQUIRES_NEW`)
- **Isolation** → data visibility (`READ_COMMITTED`, `SERIALIZABLE`)

---

### 11. Handling distributed transactions

Avoid 2PC when possible.

Prefer **Saga pattern** with event-driven compensation.

---

### 12. Saga pattern

Sequence of **local transactions** with **compensating actions** on failure.

---

## 🗄️ JPA & Hibernate

### 13. First-level vs Second-level cache

- **L1** → persistence context (per session)
- **L2** → shared across sessions (Redis/Ehcache)

---

### 14. Dirty checking

Hibernate tracks entity state changes and auto-updates DB at flush/commit.

---

### 15. N+1 problem & fix

Occurs when fetching parents + lazy children.

Fix using:

- `JOIN FETCH`
- `@EntityGraph`
- Batch fetching

---

### 16. Pagination at DB level

Uses `LIMIT / OFFSET` or **keyset pagination** for large datasets.

---

### 17. Optimistic vs pessimistic locking

- **Optimistic** → version column, better scalability
- **Pessimistic** → DB locks, safer under contention

---

## 🌐 System Design & Security

### 18. Designing high-availability systems

- Stateless services
- Load balancing
- Auto-scaling
- Failover
- Observability

---

### 19. Load balancing at application level

Distributes traffic across instances using client-side (Ribbon) or server-side (NGINX, ALB) strategies.

---

### 20. API Gateway

Single entry point handling:

- Routing
- Authentication
- Rate limiting
- Logging

---

### 21. OAuth2 flow (internals)

Client → Authorization Server → Access Token → Resource Server

Separates authentication from authorization.

---

### 22. JWT lifecycle

Issued → used for auth → expires → refreshed

Stateless, verified via signature.

---

### 23. Preventing SQL Injection & XSS

- Prepared statements / ORM
- Input validation
- Output encoding
- CSP headers

---

### 24. CORS & browser enforcement

Browser restricts cross-origin calls unless server sends valid CORS headers.

---

### 25. Spring Security filter chain

A chain of filters handling:

Authentication → Authorization → CSRF → Session management

---

### 26. Idempotency in REST

Same request → same result.

Critical for retries (`PUT`, `DELETE`, payments).

---

### 27. Versioned APIs

- URI versioning (`/v1`)
- Header-based
- Maintain backward compatibility

---

### 28. Eventual consistency

System becomes consistent **over time**, common in distributed systems.

---

### 29. CAP theorem

You can guarantee only **2 of 3**:

Consistency, Availability, Partition Tolerance.

---

## 📬 Kafka & Reactive

### 30. Kafka message durability

- Append-only logs
- Replication
- ISR acknowledgements

---

### 31. Consumer group

Consumers share partitions to scale consumption.

---

### 32. Exactly-once processing

Achieved via:

- Idempotent producers
- Transactions
- Offset management

---

### 33. WebClient vs RestTemplate

- **RestTemplate** → blocking (deprecated)
- **WebClient** → non-blocking, reactive

---

### 34. Backpressure

Mechanism where consumer controls producer speed to avoid overload.

---

### 35. Mono vs Flux

- **Mono** → 0 or 1 value
- **Flux** → 0 to N values

---

### 36. Non-blocking IO scalability

Threads aren’t blocked → fewer threads → more concurrent users.

---

## ☸️ Kubernetes & Resilience

### 37. Pod scaling in Kubernetes

Managed via controllers + metrics + autoscalers.

---

### 38. HPA

Horizontal Pod Autoscaler scales pods based on CPU/memory/custom metrics.

---

### 39. Service mesh

Infrastructure layer (Istio/Linkerd) for:

- Traffic control
- Security
- Observability

---

### 40. Circuit breaker (internal)

Tracks failures → opens circuit → fails fast → retries after cooldown.

---

### 41. Bulkhead pattern

Isolates resources to prevent cascading failures.

---

## 🧠 Caching & Ops

### 42. Redis caching strategies

- Cache-aside
- Write-through
- Write-behind

---

### 43. Cache eviction policies

LRU, LFU, FIFO, TTL-based.

---

### 44. TTL

Time after which cached data expires automatically.

---

### 45. Debugging memory leaks

- Heap dumps
- Retained object analysis
- Reference chain inspection

---

### 46. Heap dump analysis

Use MAT/VisualVM to find:

- Dominator objects
- GC roots
- Retained size

---

### 47. Tracing slow APIs

- APM tools
- Logs + metrics
- Thread dumps
- Distributed tracing

---

### 48. Distributed tracing

Tracks requests across services using trace/span IDs (Zipkin, Jaeger).

---

### 49. Blue-green vs canary deployment

- **Blue-green** → instant switch
- **Canary** → gradual rollout

---

### 50. Zero-downtime deployments

- Rolling updates
- Load balancers
- Backward-compatible DB changes
- Feature toggles

---

## 

Here’s a **polished, senior-level, interview-ready version** of your content — tightened language, clearer trade-offs, and easy to speak confidently.

---

# ✅ **Java Interview – Senior Level (Concise & Impactful Answers)**

---

### 1️⃣ ConcurrentHashMap vs SynchronizedMap

- **ConcurrentHashMap**
    - Fine-grained locking + CAS
    - Concurrent reads and concurrent writes (on different segments)
    - Scales well under high contention
- **SynchronizedMap**
    - Single global lock
    - All operations block each other
    - Poor scalability

👉 **Use ConcurrentHashMap for multi-threaded systems.**

---

### 2️⃣ Identifying & Fixing Memory Leaks

**Identify**

- Heap dumps (VisualVM, MAT)
- Objects growing after GC
- Retained reference chains

**Common causes**

- Static references
- Unremoved listeners
- ThreadLocal misuse
- Unbounded caches

**Fix**

- Clear references
- Proper lifecycle cleanup
- Use weak/soft references when appropriate

---

### 3️⃣ Thread vs ExecutorService vs Virtual Threads

- **Thread** → Heavy, OS-managed, expensive
- **ExecutorService** → Thread pooling + lifecycle management
- **Virtual Threads (Java 21+)** → Lightweight, JVM-managed, ideal for massive I/O concurrency

---

### 4️⃣ When NOT to use Virtual Threads

- CPU-bound workloads
- Long `synchronized` sections
- Native blocking calls (thread pinning)

---

### 5️⃣ GC Impact on Performance

- Affects **latency (GC pauses)** and **throughput**
- Improve predictability via:
    - Right heap sizing
    - Proper GC choice (G1, ZGC)
    - Reducing object allocation
- Many prod issues blamed on code are actually **GC issues**

---

### 6️⃣ synchronized vs Lock

- **synchronized**
    - Simple, JVM-managed
    - Automatic lock release
- **Lock**
    - `tryLock()`, fairness
    - Interruptible waits
    - More control

👉 Use **Lock** when advanced behavior is required.

---

### 7️⃣ equals() & hashCode() Contract

- Equal objects **must** have the same `hashCode`
- Poor `hashCode` → collisions → degraded `HashMap` performance

---

### 8️⃣ Spring Transaction Management (Internal)

- Implemented using **AOP proxies**
- `@Transactional`:
    - Opens transaction before method
    - Commits on success
    - Rolls back based on exception type & boundaries

---

### 9️⃣ Designing a Scalable Java Application

- Stateless services
- Caching (Redis, Caffeine)
- Async processing
- Connection pooling
- Observability (metrics, tracing)
- Horizontal scaling

---

### 🔟 Optional vs null

- **Optional**
    - Explicitly represents absence
    - Reduces NPEs
- ❌ Avoid using Optional as:
    - Entity fields
    - Method parameters

---

### 1️⃣1️⃣ Handling High Traffic in Java APIs

- Load balancing
- Caching
- Async queues
- Rate limiting
- Correct thread model (virtual threads for I/O)

---

### 1️⃣2️⃣ Fail-Fast vs Fail-Safe Iterators

- **Fail-fast**
    - Throws `ConcurrentModificationException`
    - Example: `ArrayList`
- **Fail-safe**
    - Iterates over a copy
    - Example: `CopyOnWriteArrayList`

---

### 1️⃣3️⃣ Choosing the Right Data Structure

Based on **access pattern**:

- Fast lookup → `HashMap`
- Ordered data → `TreeMap` / `TreeSet`
- Read-heavy → `ArrayList`
- Frequent inserts/removals → `LinkedList`

---

### 1️⃣4️⃣ What Makes a Senior Java Engineer Stand Out?

- Explains **trade-offs**, not just definitions
- Understands JVM & runtime behavior
- Designs for **scale and failure**
- Writes clean, testable, maintainable code

---

---

# 🚀 Spring Boot with Docker – Real-Time Interview Q&A

---

## 1️⃣ Logging, Monitoring & Debugging

### ➤ Where do Spring Boot logs go in Docker?

- By default → **STDOUT / STDERR**
- Docker captures logs, not files
- Best practice: **log to console**, not to `/logs/*.log`

👉 Enables centralized logging (ELK, CloudWatch).

---

### ➤ How do you view logs of a running container?

```bash
docker logs <container-id>
docker logs -f <container-id>

```

---

### ➤ How do you enable remote debugging?

Run container with JVM debug options:

```bash
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005

```

Expose port:

```bash
-p 8080:8080 -p 5005:5005

```

---

### ➤ What happens when a Spring Boot container crashes?

- Container **stops immediately**
- Logs are preserved
- Orchestrator (Docker/K8s) may restart it

---

### ➤ How do you restart containers automatically?

```bash
--restart=always
--restart=on-failure

```

In Kubernetes → handled by **controller**.

---

## 2️⃣ Performance & Production

### ➤ JVM memory behavior inside Docker

- JVM sees **container memory limits**, not host
- Without tuning → OOM or underutilization

---

### ➤ Why container-aware JVM settings are needed?

Older JVMs assumed **host memory** → incorrect heap sizing.

Java 11+ supports:

```
-XX:+UseContainerSupport

```

(enabled by default)

---

### ➤ Impact of Docker on Spring Boot startup time

- Slight overhead due to:
    - Image size
    - Cold filesystem
- Optimized using:
    - Layered JARs
    - Minimal base images (distroless)

---

### ➤ How do you tune memory in Docker?

```bash
-Xms256m
-Xmx512m
-XX:MaxMetaspaceSize=128m

```

Never rely on defaults in production.

---

### ➤ Spring Boot on VM vs Docker

| VM | Docker |
| --- | --- |
| Heavy OS | Lightweight |
| Slow scaling | Fast scaling |
| Manual setup | Immutable infra |

---

## 3️⃣ CI/CD & DevOps Perspective

### ➤ How do you Dockerize Spring Boot?

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

### ➤ How do you version Docker images?

```
myapp:1.0.0
myapp:1.1.0
myapp:commit-sha

```

---

### ➤ latest vs version tags

- `latest` → ambiguous, unsafe
- Version tags → **reliable rollbacks**

👉 Never deploy `latest` in prod.

---

### ➤ How do you push images to registry?

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 repo/myapp:1.0
docker push repo/myapp:1.0

```

---

### ➤ How do you roll back?

- Redeploy **previous image version**
- No rebuild required
- Kubernetes → `kubectl rollout undo`

---

## 4️⃣ Kubernetes Follow-Up (Very Common)

### ➤ Docker vs Kubernetes

- Docker → container runtime
- Kubernetes → container orchestration

---

### ➤ What changes when Spring Boot runs in Kubernetes?

- No fixed IPs
- Config via ConfigMaps
- Secrets via Secrets
- Health checks mandatory

---

### ➤ Liveness vs Readiness probes

- **Liveness** → restart container
- **Readiness** → remove from traffic

---

### ➤ How does Actuator help?

- `/health/liveness`
- `/health/readiness`
- Metrics for autoscaling
- JVM stats for monitoring

---

### ➤ Making Spring Boot cloud-native

- Externalized config
- Stateless services
- Actuator + probes
- Graceful shutdown
- Observability

---

## 5️⃣ Scenario-Based (Interview Gold ⭐)

### ➤ Container running but API not accessible

Check:

- Port mapping (`p`)
- Server port mismatch
- Firewall / security group
- App binding to `localhost` instead of `0.0.0.0`

---

### ➤ Works locally but fails in Docker

Common reasons:

- Missing env variables
- File path issues
- OS case sensitivity
- Java version mismatch

---

### ➤ DB works locally but fails in Docker

- `localhost` inside container ≠ host
- Use:
    - Service name
    - Docker network
    - Host alias

---

### ➤ Container keeps restarting

Steps:

1. Check logs
2. Look for OOM
3. Check health probes
4. Verify startup dependencies

---

### ➤ Running multiple Spring Boot instances

```bash
docker run -p 8081:8080 myapp
docker run -p 8082:8080 myapp

```

In Kubernetes → replicas + service.

---

## 🎯 One-Line Interview Takeaway

> Dockerizing Spring Boot is not about writing a Dockerfile — it’s about memory tuning, observability, immutability, and failure handling.
> 

---

---

# 🔹 Spring Core (Advanced Java – Essential)

### ✔ What exactly is the Spring Framework?

Spring is a **lightweight Java framework** that helps build enterprise applications by managing **object creation, dependencies, and cross-cutting concerns** like transactions and security.

---

### ✔ Key modules of Spring

- **Core / Beans / Context** → IoC & DI
- **AOP** → logging, transactions
- **JDBC / ORM** → DB access
- **Web / MVC** → REST & web apps
- **Security** → authentication & authorization

---

### ✔ Inversion of Control (IoC)

IoC means **Spring controls object creation**, not the developer.

You define *what* you need, Spring decides *how and when*.

---

### ✔ Dependency Injection (DI) & purpose

DI means **dependencies are injected**, not created manually.

This improves **testability, loose coupling, and maintainability**.

---

### ✔ Types of DI in Spring

- Constructor Injection ✅ (recommended)
- Setter Injection
- Field Injection ❌ (not preferred)

---

### ✔ BeanFactory vs ApplicationContext

- **BeanFactory** → basic, lazy
- **ApplicationContext** → full-featured (AOP, events, i18n)
    
    👉 Real applications use **ApplicationContext**.
    

---

### ✔ Spring Beans

Objects managed by Spring container.

---

### ✔ Spring Bean lifecycle

```
Instantiate → Inject dependencies → PostConstruct → Ready → PreDestroy

```

---

### ✔ @Component & stereotypes

- `@Component` → generic bean
- `@Service` → business logic
- `@Repository` → DB layer + exception translation
- `@Controller` → MVC controller

👉 Functionally same, **semantically different**.

---

### ✔ @Autowired

Spring resolves dependencies by:

1. Type
2. Name
3. Qualifier (if ambiguity)

---

### ✔ Constructor vs Setter Injection

- **Constructor** → mandatory deps, immutable
- **Setter** → optional deps

---

### ✔ @Qualifier vs @Primary

- `@Qualifier` → explicit bean selection
- `@Primary` → default choice

---

### ✔ Bean Scopes

- Singleton (default)
- Prototype
- Request / Session (web)

---

# 🔹 Spring Boot (Highly Important)

### ✔ What makes Spring Boot different?

Spring Boot **removes configuration pain** using:

- Auto-configuration
- Embedded servers
- Starter dependencies

---

### ✔ Spring vs Spring Boot

| Spring | Spring Boot |
| --- | --- |
| Manual config | Auto config |
| External server | Embedded server |
| Boilerplate | Convention over config |

---

### ✔ @SpringBootApplication

Combination of:

- `@Configuration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

---

### ✔ Auto-configuration

Spring Boot checks:

- Classpath
- Existing beans
- Properties
    
    Then configures beans **conditionally**.
    

---

### ✔ Starter dependencies

Opinionated dependency bundles

(e.g. `spring-boot-starter-web`).

---

### ✔ application.properties vs yml

- `.properties` → simple
- `.yml` → hierarchical, cleaner for large configs

---

### ✔ Default port

`8080` → configurable via:

```
server.port=9090

```

---

### ✔ Embedded server

Tomcat/Jetty bundled inside app → run as **jar**.

---

### ✔ Embedded vs External server

Embedded is **simpler, portable, cloud-ready**.

---

### ✔ How Spring Boot reduces boilerplate

- Auto config
- Starters
- Defaults
- Embedded server

---

# 🔹 REST API (Real-World Focus)

### ✔ What is REST API?

Stateless, resource-based communication over HTTP.

---

### ✔ REST vs SOAP

- REST → lightweight, JSON
- SOAP → XML, heavyweight

---

### ✔ @RestController

`@Controller + @ResponseBody`

---

### ✔ @RequestMapping vs @GetMapping

- `@RequestMapping` → generic
- `@GetMapping` → HTTP-specific (cleaner)

---

### ✔ @PathVariable vs @RequestParam

- PathVariable → mandatory resource identifier
- RequestParam → optional filters

---

### ✔ @RequestBody

Maps JSON request → Java object.

---

### ✔ PUT vs PATCH

- PUT → full update
- PATCH → partial update

---

### ✔ HTTP Status Codes

- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
- 500 Server Error

---

### ✔ ResponseEntity

Gives control over **status, headers, body**.

---

# 🔹 Spring Data JPA / Hibernate

### ✔ What is JPA?

ORM **specification**, not implementation.

---

### ✔ JPA vs Hibernate

- JPA → standard
- Hibernate → implementation + extras

---

### ✔ ORM fundamentals

Maps Java objects → DB tables.

---

### ✔ @Id & @GeneratedValue

Defines primary key and generation strategy.

---

### ✔ save() vs saveAndFlush()

- save() → delayed DB write
- saveAndFlush() → immediate flush

---

### ✔ JpaRepository

CRUD + pagination + sorting.

---

### ✔ CrudRepository vs JpaRepository

JpaRepository is **superset**.

---

### ✔ @Transactional

Defines transaction boundary using **AOP proxies**.

---

### ✔ FetchType

- LAZY → fetch on demand (recommended)
- EAGER → fetch immediately

---

### ✔ N+1 Problem

One query for parent + N queries for children.

Fix using:

- JOIN FETCH
- @EntityGraph

---

# 🔹 Exception Handling & Validation

### ✔ @ExceptionHandler

Handles exceptions locally.

---

### ✔ @ControllerAdvice

Global exception handling.

---

### ✔ @Valid

Triggers Bean Validation.

---

### ✔ Bean Validation

JSR-380 annotations:

- @NotNull
- @Size
- @Email

---

# 🔹 Configuration & Profiles

### ✔ Spring Profiles

Environment-specific config:

- dev
- test
- prod

---

### ✔ @Value

Injects property values.

---

### ✔ @Configuration

Defines config class.

---

### ✔ @Bean vs @Component

- @Bean → method-level
- @Component → class-level

---

# 🔹 Security & Microservices Basics

### ✔ Spring Security

Framework for authentication & authorization.

---

### ✔ Auth vs Authorization

- Auth → who are you
- Authorization → what can you access

---

### ✔ JWT basics

Stateless token with claims.

---

### ✔ CORS

Browser security rule for cross-origin requests.

---

### ✔ Microservices

Independent, deployable services.

---

### ✔ Eureka & Config Server

- Eureka → service discovery
- Config Server → centralized config

---

# 🔹 Project-Based Questions (MOST IMPORTANT)

### ✔ Explain project structure

Controller → Service → Repository → DB

---

### ✔ Request flow

Client → Controller → Service → Repository → DB → Response

---

### ✔ Exception handling

Global `@ControllerAdvice`

---

### ✔ MySQL integration

- DataSource config
- JPA repositories
- Transaction management

---

---

# 🔹 Core Java & JVM

### JVM Architecture

- **ClassLoader** → loads bytecode
- **Runtime Data Areas** → Heap, Stack, Metaspace
- **Execution Engine** → Interpreter + JIT
- **GC** → automatic memory management

👉 Interviewers want to see you understand **how Java runs**, not just syntax.

---

### Java Memory Model (JMM)

Defines **visibility, ordering, and atomicity** between threads.

Explains *why* `volatile`, `synchronized`, and `final` matter in concurrency.

---

### Heap vs Stack

- **Heap** → objects, shared across threads
- **Stack** → method calls, local variables, thread-specific

---

### Garbage Collection & GC Types

- **Young GC / Old GC**
- **G1, ZGC, Parallel GC**

👉 GC affects **latency & throughput**, not just memory.

---

### Stop-the-World (STW)

All application threads pause while GC works.

Too many STW pauses = **production latency spikes**.

---

### Memory Leaks

Objects are still referenced but never used.

Common causes:

- Static references
- Listeners not removed
- ThreadLocal misuse

---

### Reference Types

- **Strong** → normal objects
- **Soft** → cache-friendly
- **Weak** → GC-friendly mappings
- **Phantom** → cleanup hooks

---

### ClassLoader & Types

- Bootstrap
- Platform
- Application
- Custom

ClassLoader issues = **ClassCastException in prod**.

---

# 🔹 Multithreading & Concurrency

### Process vs Thread

- Process → heavy, isolated
- Thread → lightweight, shared memory

---

### Thread Lifecycle

New → Runnable → Running → Blocked → Terminated

---

### Runnable vs Callable

- Runnable → no result
- Callable → returns value + throws exception

---

### Synchronization

Controls **critical sections** to prevent race conditions.

Overuse leads to **performance bottlenecks**.

---

### Deadlock vs Race Condition

- **Deadlock** → threads wait forever
- **Race** → incorrect results due to timing

---

### volatile

Guarantees **visibility**, not atomicity.

---

### wait() vs sleep()

- `wait()` → releases lock
- `sleep()` → does NOT release lock

---

### Executor Framework

Manages thread lifecycle and reuse.

Preferred over manual thread creation.

---

### Thread Pools

Avoid thread explosion.

Must be sized based on:

- CPU-bound vs IO-bound tasks

---

### submit() vs execute()

- `execute()` → fire-and-forget
- `submit()` → returns `Future`

---

### Future vs CompletableFuture

- **Future** → blocking
- **CompletableFuture** → async, non-blocking pipelines

---

### Fork/Join Framework

Work-stealing for **divide-and-conquer algorithms**.

---

### Concurrent Collections

Thread-safe without full locking

(e.g., ConcurrentHashMap).

---

# 🔹 Collections & Immutability

### HashMap vs ConcurrentHashMap

- HashMap → not thread-safe
- ConcurrentHashMap → CAS + fine-grained locking

---

### Fail-fast vs Fail-safe

- Fail-fast → throws exception
- Fail-safe → works on copy

---

### Immutability

Immutable objects:

- Thread-safe
- Cache-friendly
- Easier to reason about

---

# 🔹 Advanced Concepts

### Reflection

Inspect & modify classes at runtime.

Powerful but **slow and risky**.

---

### Annotations

Metadata for framework behavior

(e.g., Spring, JPA).

---

### Serialization

Convert object → byte stream.

Used in caching, messaging.

---

### transient

Excludes fields from serialization.

---

### Externalization

Manual control over serialization process.

---

# 🔹 Design Patterns

### What is a Design Pattern?

Reusable solution to a **common design problem**.

---

### Singleton Pattern

One instance per JVM.

---

### Breaking Singleton

- Reflection
- Serialization
- Cloning

---

### Preventing Singleton Break

- Enum Singleton
- Defensive coding

---

### Factory Pattern

Creates objects without exposing instantiation logic.

---

### Builder Pattern

Creates complex objects step-by-step (immutable objects).

---

# 🔹 Database & ORM

### JDBC

Low-level DB API.

---

### Steps to Connect DB

1. Load driver
2. Create connection
3. Execute query
4. Process result
5. Close resources

---

### Statement vs PreparedStatement

- Statement → SQL injection risk
- PreparedStatement → safe + faster

---

### Connection Pooling

Reuses DB connections to improve performance.

---

### ORM

Maps objects ↔ tables.

---

### Hibernate

ORM implementation of JPA.

---

### Hibernate vs JDBC

- Hibernate → productivity + caching
- JDBC → fine-grained control + performance

---

# 🔹 Web Services & Performance

### REST API

Stateless, resource-based HTTP services.

---

### REST vs SOAP

- REST → lightweight, JSON
- SOAP → heavy, XML

---

### Java Performance Tuning

- JVM tuning
- GC tuning
- Caching
- Thread pool tuning
- DB optimization

---

---

# 🟢 EASY — Foundations (with common traps)

### JDK vs JRE vs JVM

- **JVM** → runs bytecode
- **JRE** → JVM + core libraries
- **JDK** → JRE + development tools

👉 Trap: JVM ≠ JDK

---

### Why is String immutable?

- Thread-safe
- Enables String pool
- Secure (used in URLs, class loading)
- HashCode caching

---

### `==` vs `.equals()`

- `==` → reference comparison
- `.equals()` → content comparison

👉 Trap: String literals may look equal with `==`

---

### Heap vs Stack

- **Heap** → objects, shared
- **Stack** → method calls, thread-local

---

### Class loading in Java

- Bootstrap → Platform → Application → Custom
    
    👉 Same class name + different ClassLoader = different class
    

---

### Access modifiers

| Modifier | Scope |
| --- | --- |
| private | class |
| default | package |
| protected | package + subclass |
| public | everywhere |

---

### Why main() is static?

JVM must call it **without creating an object**.

---

### Overloading vs Overriding

- Overloading → compile-time
- Overriding → runtime (polymorphism)

---

### `final`

- variable → cannot change
- method → cannot override
- class → cannot extend

---

### Abstract class vs Interface

- Abstract → state + behavior
- Interface → contract
    
    Java supports multiple inheritance via interfaces.
    

---

# 🟡 MEDIUM — Real Interview Filter

### Internal working of HashMap

- Array of buckets
- hash → index
- Collision → LinkedList → Tree (Java 8+)

---

### HashMap vs Hashtable

- HashMap → not thread-safe
- Hashtable → synchronized, slow, legacy

---

### HashMap resizing

- Happens when size > capacity × loadFactor
- Rehashing is expensive

---

### Importance of hashCode()

Poor hashCode → collisions → performance degradation.

---

### ArrayList vs LinkedList

- ArrayList → fast read
- LinkedList → fast insert/delete (but poor cache locality)

---

### Fail-fast vs Fail-safe

- Fail-fast → throws exception
- Fail-safe → works on copy

---

### Garbage Collection

Automatic memory cleanup of unreachable objects.

---

### Checked vs Unchecked exceptions

- Checked → compile-time
- Unchecked → runtime

👉 Trap: Not all runtime exceptions should be ignored.

---

### Can static methods be overridden?

❌ No — they are **hidden**, not overridden.

---

### throw vs throws

- throw → explicitly throw exception
- throws → declare possibility

---

### Serialization (when to avoid)

Avoid when:

- Performance-sensitive
- Security-critical
- Version changes often

---

### Comparable vs Comparator

- Comparable → natural ordering
- Comparator → custom ordering

---

### transient

Field not serialized.

---

### Java Memory Model (JMM)

Defines **visibility, ordering, atomicity**.

---

### StringBuilder vs StringBuffer

- StringBuilder → fast, not thread-safe
- StringBuffer → synchronized, slow

---

# 🔴 HARD — Offer-Deciding Questions

### equals()–hashCode() contract

Equal objects **must** have same hashCode.

---

### Reference types

- Strong → normal
- Soft → cache
- Weak → GC-friendly
- Phantom → post-GC cleanup

---

### ConcurrentHashMap internals

- CAS
- Fine-grained locking
- No full-map lock

---

### Happens-before relationship

Guarantees visibility & ordering between threads.

---

### volatile vs synchronized

- volatile → visibility
- synchronized → visibility + atomicity

---

### ClassLoader hierarchy

Key reason behind **ClassCastException in prod**.

---

### Private constructors

Used in:

- Singleton
- Utility classes
- Factory pattern

---

### Overriding finalize()

Dangerous:

- Unpredictable
- Object resurrection
- Deprecated

---

### Deadlock vs Livelock vs Starvation

- Deadlock → waiting forever
- Livelock → active but no progress
- Starvation → never gets CPU

---

### ThreadLocal internals

Per-thread map → memory leak risk if not cleaned.

---

### Callable vs Runnable

- Callable → returns value + throws exception
- Runnable → no return

---

### Why wait/notify need synchronized?

They operate on **monitor lock**.

---

### Escape analysis

Allows:

- Stack allocation
- Lock elimination

---

### Young vs Old GC

- Young → frequent, fast
- Old → slow, expensive

---

### Immutability benefits

- Thread-safe
- Cache-friendly
- No synchronization needed

---

### Double-checked locking

Fails without `volatile` due to reordering.

---

### Common OOM scenarios

- Heap leak
- Metaspace leak
- Direct memory leak
- Thread explosion

---

### Custom ClassLoader

Used in:

- App servers
- Plugins
- Isolation

---

### Parallel GC vs G1

- Parallel → throughput
- G1 → predictable latency

---

### synchronized (bytecode level)

Uses **monitorenter / monitorexit**.

---

### Reflection risks

- Breaks encapsulation
- Performance hit
- Security issues

---

### String.intern()

Moves string to pool — can cause memory pressure.

---

### False sharing

Multiple threads update same cache line → performance hit.

---

### AtomicInteger vs synchronized counter

- Atomic → CAS, lock-free
- synchronized → blocking

---

### Thread-safety issues in collections

Non-thread-safe collections can:

- Corrupt data
- Cause infinite loops
- Crash prod systems

---

Below is a **senior-level, real-world, interview-ready answer set**.

Each answer focuses on **how it’s actually done in production**, not textbook theory.

---

# ✅ Spring Boot – Real-Time Interview Questions & Answers

---

## 1️⃣ Handling different configs (dev / test / prod)

- Use **Spring Profiles**
- Separate config files:
    - `application-dev.yml`
    - `application-test.yml`
    - `application-prod.yml`
- Activate via:

```bash
-Dspring.profiles.active=prod

```

👉 In large systems: **Spring Cloud Config / Kubernetes ConfigMaps**

---

## 2️⃣ Database connection pooling

- Default: **HikariCP**
- Configure via:

```yaml
spring.datasource.hikari.maximum-pool-size: 20
spring.datasource.hikari.minimum-idle: 5

```

👉 Tune based on DB capacity, not blindly increasing.

---

## 3️⃣ Global exception handling in REST APIs

- Use `@RestControllerAdvice`
- Centralized error responses
- Map exceptions → HTTP status codes
    
    👉 Keeps controllers clean and consistent.
    

---

## 4️⃣ Securing APIs (JWT / OAuth2)

- **JWT**: Stateless token validation via filter
- **OAuth2**: External auth server (Keycloak, Okta)
- Use Spring Security filter chain
    
    👉 Always separate **authentication** and **authorization**.
    

---

## 5️⃣ Large file uploads

- Configure multipart limits:

```
spring.servlet.multipart.max-file-size=50MB

```

- Stream files (don’t load fully into memory)
- Upload directly to **S3 / Blob storage**

---

## 6️⃣ Using Spring Boot Actuator in production

- Enable selectively:

```
management.endpoints.web.exposure.include=health,metrics

```

- Use for:
    - Health checks
    - Metrics
    - Readiness / liveness probes

---

## 7️⃣ Logging for production debugging

- Log to **STDOUT**
- Structured logs (JSON)
- Correlation IDs
- Centralized logging (ELK / CloudWatch)
    
    👉 Never rely on local log files in containers.
    

---

## 8️⃣ API versioning strategies

- URL versioning: `/api/v1/users`
- Header-based versioning
- Backward compatibility is key
    
    👉 Avoid breaking changes.
    

---

## 9️⃣ Optimizing Spring Boot startup time

- Reduce auto-configurations
- Lazy initialization
- Smaller dependency set
- JVM tuning
    
    👉 Important for containers & serverless.
    

---

## 🔟 Transaction management

- Use `@Transactional`
- Proper propagation & isolation
- Avoid calling external services inside transactions
    
    👉 Transactions are **boundaries**, not magic.
    

---

# 🔥 Advanced Real-Time Questions

---

## 1️⃣1️⃣ Caching (Redis / Ehcache)

- Cache-aside pattern
- TTL + eviction policies
- Use Redis for distributed cache
    
    👉 Always plan cache invalidation.
    

---

## 1️⃣2️⃣ Handling CORS

- Configure via Spring Security:

```java
CorsConfigurationSource

```

- Or controller-level `@CrossOrigin`
    
    👉 CORS is enforced by browsers, not servers.
    

---

## 1️⃣3️⃣ API rate limiting

- Redis + token bucket
- API Gateway (preferred)
- Prevent abuse & traffic spikes

---

## 1️⃣4️⃣ Microservice communication

- REST / Feign → sync
- Kafka / messaging → async
- Retries + timeouts + circuit breakers

---

## 1️⃣5️⃣ Handling service downtime

- Circuit breakers
- Fallback responses
- Graceful degradation
    
    👉 Never let one failure cascade.
    

---

## 1️⃣6️⃣ Circuit breaker implementation

- Use Resilience4j
- Failure thresholds
- Open → half-open → closed states

---

## 1️⃣7️⃣ Schema changes without downtime

- Backward-compatible DB changes
- Expand → migrate → contract
- Avoid destructive changes

---

## 1️⃣8️⃣ Monitoring memory & performance

- JVM metrics
- GC logs
- Heap dumps
- APM tools
    
    👉 Most prod issues are **runtime-related**, not code bugs.
    

---

## 1️⃣9️⃣ Securing configs & secrets

- Never hardcode secrets
- Use:
    - Vault
    - KMS
    - Kubernetes Secrets
        
        👉 Config ≠ secrets.
        

---

## 2️⃣0️⃣ Rollback scenarios

- Redeploy previous artifact
- Feature toggles
- DB rollbacks via scripts
    
    👉 Rollback should be **fast and safe**.
    

---

# 🔥 Real-Time Debugging & Deployment

---

## 2️⃣1️⃣ Debugging prod without stopping server

- Logs
- Metrics
- Thread dumps
- Heap dumps
- Feature flags

---

## 2️⃣2️⃣ Zero-downtime deployments

- Rolling updates
- Blue-green
- Canary releases
- Readiness probes

---

## 2️⃣3️⃣ Failed Kafka message handling

- Retry with backoff
- Dead Letter Queue (DLQ)
- Idempotent consumers

---

## 2️⃣4️⃣ Distributed transactions

- Avoid 2PC
- Use **Saga pattern**
- Event-driven compensation

---

## 2️⃣5️⃣ Tracing requests across microservices

- Correlation / Trace IDs
- Distributed tracing (Zipkin, Jaeger)
- Centralized observability

---

## 

---

### 🚨 Hard Truth About “Senior” Backend Roles

Writing REST controllers **does not differentiate you anymore**.

Modern backend engineers are expected to **design, scale, debug, and secure distributed systems in production** — not just ship CRUD APIs.

If you’re aiming for (or claiming) a **Senior Backend role**, you’re expected to be solid in:

---

## ✅ What Seniors Are Expected to Know (Baseline, Not Bonus)

### 🌍 Distributed Systems (Real Trade-offs)

- CAP theorem & consistency models
- Knowing **what you sacrifice and why**, not definitions

### ⚙️ Java Concurrency & JVM Internals

- Java Memory Model (JMM)
- ExecutorService, ForkJoinPool
- GC behavior & tuning
- Thread safety under load

### 🧩 Microservices & Cloud-Native Architecture

- Service boundaries & failure isolation
- Horizontal scaling strategies
- Cloud-first design thinking

### 📬 Messaging, Caching & Scalability

- Kafka (including Schema Registry)
- Redis caching strategies
- Rate limiting & backpressure

### 🛡️ Resilience by Design

- Circuit breakers (Resilience4j)
- Timeouts, retries, fallbacks
- Blast radius control

### 🔁 Distributed Transactions

- Saga pattern (orchestration vs choreography)
- Why 2PC doesn’t scale

### ☸️ Platform Engineering

- Kubernetes fundamentals
- API Gateways (Spring Cloud Gateway)
- Service discovery & config management

### 🔐 Security (Non-Negotiable)

- OAuth2 & JWT
- Token lifecycle & common attack vectors
- SSL/TLS & secure communication

### 📊 Observability

- Metrics (Prometheus)
- Logs (ELK)
- Tracing (OpenTelemetry, Grafana)
- Debugging production issues without guesswork

---

## ❌ If Your Daily Work Is Still Limited To:

- CRUD APIs
- Annotations & configs
- “It works on my machine”

Then you’re **mid-level**, regardless of your title.

---

## 🧠 What Real Seniors Actually Think About

- Failure modes
- Latency vs throughput
- Cost vs reliability
- Scaling behavior under load
- Blast radius when things go wrong

---

---

# ✅ Spring Boot Annotations – What You MUST Know (Mid → Senior)

## 🔹 Core Annotations

### ✅ `@SpringBootApplication`

- **Entry point of a Spring Boot app**
- Combines:
    - `@Configuration`
    - `@EnableAutoConfiguration`
    - `@ComponentScan`

👉 Tells Spring Boot: *“Start here, scan beans, auto-configure everything.”*

---

### ✅ `@Configuration`

- Marks a class as a **Java-based configuration**
- Used to define beans using `@Bean`

👉 Preferred over XML configuration.

---

### ✅ `@Bean`

- Used inside `@Configuration` classes
- Explicitly creates and registers a bean

👉 Used when:

- You don’t own the class (3rd-party lib)
- You need custom initialization

---

## 🔹 Stereotype Annotations (Layered Design)

### ✅ `@Component`

- Generic Spring-managed bean
- Base stereotype

---

### ✅ `@Service`

- Business logic layer
- Same as `@Component` technically, but **semantic meaning matters**

👉 Helps readability + AOP (transactions).

---

### ✅ `@Repository`

- Data access layer
- Adds **exception translation** (JPA exceptions → Spring exceptions)

👉 Always use for DAO / Repository classes.

---

## 🔹 Dependency Injection

### ✅ `@Autowired`

- Injects dependencies automatically
- Resolution order:
    1. By type
    2. By name
    3. By `@Qualifier`

👉 **Constructor injection is recommended**.

---

### ✅ `@Qualifier`

- Used when **multiple beans of same type** exist
- Explicitly tells Spring which one to inject

---

### ✅ `@Primary`

- Marks a bean as **default choice**
- Used when you don’t want to repeat `@Qualifier` everywhere

---

## 🔹 Web / REST Annotations

### ✅ `@RestController`

- Combines:
    - `@Controller`
    - `@ResponseBody`
- Used for REST APIs returning JSON

---

### ✅ `@RequestMapping`

- Generic request mapping
- Can map:
    - URL
    - HTTP method
    - Headers
    - Content type

---

### ✅ HTTP Method Mappings

- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@DeleteMapping`

👉 Cleaner, HTTP-specific alternatives to `@RequestMapping`.

---

### ✅ `@PathVariable`

- Reads values from URL path

```java
/users/{id}

```

---

### ✅ `@RequestParam`

- Reads query parameters

```java
/users?id=10

```

---

### ✅ `@RequestBody`

- Maps JSON request body → Java object
- Uses Jackson internally

👉 Required for POST/PUT APIs.

---

## 🔹 JPA / Database

### ✅ `@Entity`

- Maps a Java class to a database table
- Managed by JPA/Hibernate

---

### ✅ `@Id`

- Marks primary key

---

### ✅ `@GeneratedValue`

- Auto-generates primary key values
- Strategies: `IDENTITY`, `SEQUENCE`, `AUTO`

---

### ✅ `@Transactional`

- Defines **transaction boundary**
- Uses **AOP proxy**
- Commits or rolls back automatically

👉 Should be used at **service layer**, not controller.

---

## 🔹 Exception Handling

### ✅ `@ExceptionHandler`

- Handles specific exceptions
- Can be used at controller level

---

### ✅ `@ControllerAdvice`

- **Global exception handler**
- Keeps controllers clean
- Central place for error responses

👉 Always preferred in real projects.

---

## 🔹 Configuration & Profiles

### ✅ `@Value`

- Injects values from `application.properties / yml`

```java
@Value("${server.port}")

```

---

### ✅ `@ConfigurationProperties`

- Type-safe configuration binding
- Better than multiple `@Value` annotations

👉 Preferred for large configs.

---

### ✅ `@Profile`

- Activates beans only for specific environments

```java
@Profile("dev")

```

👉 Used for **dev / test / prod separation**.

---

---

# ✅ Spring Boot Interview Questions & Answers (Complete)

---

## 🟢 Spring Boot Basics

### 1. What is Spring Boot and why is it used?

Spring Boot is an opinionated framework built on Spring that **simplifies application development** by providing auto-configuration, embedded servers, and production-ready features.

---

### 2. Difference between Spring and Spring Boot

| Spring | Spring Boot |
| --- | --- |
| Manual configuration | Auto-configuration |
| External server | Embedded server |
| More boilerplate | Minimal boilerplate |

---

### 3. What is Auto-Configuration?

Automatically configures beans based on:

- Classpath
- Existing beans
- Properties
    
    Uses conditional annotations internally.
    

---

### 4. Spring Boot Starters (examples)

Predefined dependency bundles:

- `spring-boot-starter-web`
- `spring-boot-starter-data-jpa`
- `spring-boot-starter-security`

---

### 5. Explain `@SpringBootApplication`

It combines:

- `@Configuration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

---

### 6. Role of `application.properties / yml`

Central place for:

- Configuration
- Environment settings
- Externalized values

---

### 7. How do you override default configurations?

- Add properties in `application.yml`
- Use profiles
- Define your own beans

---

### 8. Spring Boot CLI

Command-line tool to run Groovy-based Spring Boot apps quickly (rarely used in production).

---

### 9. Advantages of Spring Boot

- Faster development
- Embedded servers
- Auto-configuration
- Production-ready features

---

### 10. Dependency management in Spring Boot

Managed via **starters + BOM** → no version conflicts.

---

## 🟢 Web & REST

### 11. `@RestController` vs `@Controller`

- `@Controller` → returns views
- `@RestController` → returns JSON (`@ResponseBody` included)

---

### 12. `@RequestMapping`, `@GetMapping`, `@PostMapping`

- `@RequestMapping` → generic
- Others → HTTP-specific & cleaner

---

### 13. What is `@SpringBootApplication` composed of?

`@Configuration + @EnableAutoConfiguration + @ComponentScan`

---

### 14. `@Component` vs `@Service` vs `@Repository` vs `@Controller`

Same technically, different **semantic roles**:

- Service → business logic
- Repository → DB + exception translation

---

### 15. Explain `@EnableAutoConfiguration`

Enables Spring Boot to configure beans automatically using conditional logic.

---

### 16. `@ConfigurationProperties`

Type-safe binding of properties to POJO.

---

### 17. `@Bean` vs `@Component`

- `@Bean` → method-level, manual control
- `@Component` → class-level, auto-scan

---

### 18. `@ConditionalOnProperty`

Loads a bean only if a property exists or matches a value.

---

### 19. `@Value`

Injects individual property values.

---

### 20. Custom annotations

Create using:

```java
@Target
@Retention
@Documented

```

Often used with AOP.

---

## 🟢 JPA & Database

### 21. Datasource configuration

Via:

```yaml
spring.datasource.url
spring.datasource.username
spring.datasource.password

```

---

### 22. Spring Boot JPA integration

Auto-configures:

- DataSource
- EntityManager
- TransactionManager

---

### 23. Spring Data JPA

Abstraction over JPA that provides **CRUD, pagination, and query methods**.

---

### 24. Custom query using `@Query`

```java
@Query("SELECT u FROM User u WHERE u.email=?1")

```

---

### 25. Repository differences

- CrudRepository → basic CRUD
- PagingAndSortingRepository → pagination
- JpaRepository → full features

---

### 26. Pagination & sorting

Using `PageRequest.of(page, size, Sort.by())`.

---

### 27. Role of EntityManager

Manages persistence context and entity lifecycle.

---

### 28. Transaction management

Handled using `@Transactional` via **AOP proxies**.

---

### 29. LAZY vs EAGER

- LAZY → fetch on demand (recommended)
- EAGER → fetch immediately

---

### 30. DB migrations (Flyway/Liquibase)

Version-controlled schema changes applied automatically at startup.

---

## 🟢 REST APIs & Validation

### 31. Creating REST APIs

Using:

- `@RestController`
- Mapping annotations
- DTOs

---

### 32. Difference (again)

`@RestController = @Controller + @ResponseBody`

---

### 33. ResponseEntity

Wraps response body, status, headers.

---

### 34. Exception handling in REST

Use:

- `@ExceptionHandler`
- `@ControllerAdvice`

---

### 35. Global exception handling

Centralized error handling using `@ControllerAdvice`.

---

### 36. CORS handling

Via:

- `@CrossOrigin`
- Spring Security config

---

### 37. Validation (JSR-303)

Using `@Valid` + annotations like `@NotNull`, `@Size`.

---

### 38. File uploads

Use `MultipartFile` and configure size limits.

---

### 39. Sync vs Async REST

- Sync → blocking
- Async → `@Async`, `CompletableFuture`

---

### 40. Securing REST APIs

Using:

- Spring Security
- JWT / OAuth2
- Filters

---

## 🟢 Production & Ops

### 41. Spring Boot Actuator

Provides:

- Health checks
- Metrics
- Readiness/liveness

---

### 42. Monitoring

Using:

- Actuator
- Prometheus
- Grafana
- Logs

---

### 43. Spring Boot DevTools

Improves dev experience:

- Auto restart
- Live reload

---

### 44. `@Configuration` vs `@EnableAutoConfiguration`

- Configuration → manual bean definitions
- EnableAutoConfiguration → automatic setup

---

### 45. Logging in Spring Boot

Uses SLF4J + Logback by default.

Logs go to console (STDOUT).

---

### 46. Profiles

Environment-specific configuration:

```
dev / test / prod

```

---

### 47. Scheduled tasks

Using `@EnableScheduling` + `@Scheduled`.

---

### 48. Messaging integration

- Kafka → `@KafkaListener`
- RabbitMQ → `@RabbitListener`

---

### 49. Deployment

- Jar (preferred)
- Docker
- Kubernetes
- Cloud platforms

---

### 50. Jar vs War

- **Jar** → embedded server (recommended)
- **War** → external server

---

## 🔹 Core Java (Depth Expected)

### HashMap internals (Java 8+)

- Array + buckets
- Collisions → LinkedList → **Red-Black Tree** (after threshold)
- Improves worst-case lookup from **O(n) → O(log n)**

### ConcurrentHashMap vs SynchronizedMap

- ConcurrentHashMap → CAS + bucket-level locking
- SynchronizedMap → full map lock (contention)

### equals() & hashCode()

- Equal objects **must** have same hashCode
- Poor hashCode → performance collapse in HashMap

### Garbage Collection

- Young / Old Gen
- G1, ZGC focus on **latency predictability**
- GC tuning is about **trade-offs**, not max heap

### CompletableFuture vs Future

- Future → blocking
- CompletableFuture → async pipelines, non-blocking

### Immutability

- Thread-safe
- Cache-friendly
- Easier reasoning in concurrency

### ThreadLocal

- Per-thread state (security context, request id)
- Risk: **memory leaks** if not cleared

### volatile vs synchronized

- volatile → visibility only
- synchronized → visibility + atomicity + ordering

---

## 🔹 Java 8 – Streams & FP

### map vs flatMap

- map → 1-to-1
- flatMap → flatten nested structures

### Parallel streams – when NOT to use

- IO-bound tasks
- Shared mutable state
- Low CPU cores

### Optional – is it useful?

- Yes, for **return values**
- No, for fields/params

### Stream vs Collection

- Collection → data
- Stream → computation

### Can streams be reused?

❌ No – terminal operation consumes stream

---

## 🔹 Spring Core & Boot

### @Component vs @Service vs @Repository

- Same technically
- Semantic meaning + AOP behavior (exception translation)

### Spring Boot startup flow

1. Load environment
2. Auto-configuration
3. Bean creation
4. Embedded server start

### @Autowired – internals

- Dependency resolution by type → name → qualifier

### BeanFactory vs ApplicationContext

- ApplicationContext = enterprise features (AOP, events)

### Auto-configuration

- Conditional on classpath, beans, properties

### @Transactional internals

- Proxy + AOP
- Rollback on RuntimeException by default

### Propagation

- REQUIRED, REQUIRES_NEW, MANDATORY, NEVER
- Defines **transaction boundaries across services**

---

## 🔹 Microservices Architecture

### Monolith vs Microservices (real issues)

- Microservices add:
    - Network latency
    - Distributed failures
    - Observability complexity

### Inter-service communication

- REST → sync
- gRPC → high performance
- Kafka → async & decoupled

### REST vs gRPC

- REST → human-friendly
- gRPC → low latency, schema-based

### Config management

- Spring Cloud Config / Kubernetes ConfigMaps

### Service discovery

- Dynamic lookup instead of hardcoded URLs

### Distributed transactions

- 2PC doesn’t scale
- Use **Saga**

### Saga

- Choreography → event-based
- Orchestration → central coordinator

### Data consistency

- Eventual consistency
- Idempotency
- Compensation actions

---

## 🔹 Spring Cloud

### Config Server

- Centralized configuration
- Environment-specific configs

### Eureka

- Client-side service discovery
- Heartbeats + registry

### API Gateway

- Routing, auth, rate limiting
- Spring Cloud Gateway > Zuul (reactive, faster)

### Circuit Breaker (Resilience4j)

- Prevent cascading failures
- States: closed → open → half-open

### Rate limiting

- Token bucket / Redis / API Gateway

### Fallbacks

- Graceful degradation, not silent failure

---

## 🔹 Database & Persistence

### RDBMS vs NoSQL

- RDBMS → strong consistency, transactions
- NoSQL → scalability, flexibility

### Indexing

- Speeds reads, slows writes
- Always validate with query plans

### N+1 problem

- Fix with JOIN FETCH / EntityGraph

### Lazy vs Eager

- Lazy by default in microservices

### Locking

- Optimistic → high read
- Pessimistic → critical writes

### DB per microservice

- Isolation + scalability
- Harder reporting & joins

---

## 🔹 Messaging & Event-Driven

### Kafka vs RabbitMQ

- Kafka → streaming, high throughput
- RabbitMQ → message routing

### Ordering

- Guaranteed **per partition**

### Idempotency

- Same message processed multiple times safely

### Retry & failure

- Retry + backoff
- DLQ

### Delivery semantics

- At-least-once (most common)
- Exactly-once (complex, costly)

---

## 🔹 Security

### JWT flow

- Auth → token → stateless validation

### OAuth2 vs JWT

- OAuth2 → authorization framework
- JWT → token format

### Inter-service security

- mTLS
- Token propagation

### CSRF

- Browser-only issue
- Use stateless APIs

### Secrets

- Vault / KMS / Kubernetes Secrets
- Never in code

---

## 🔹 Performance & Scalability

### Horizontal vs Vertical

- Horizontal preferred for cloud systems

### Bottleneck identification

- CPU, memory, IO, DB, locks

### Caching

- Cache-aside pattern
- TTL + eviction strategy

### Load balancing

- Client-side vs server-side

### High availability

- No single point of failure
- Health checks + replicas

---

## 🔹 Monitoring & Observability

### Centralized logging

- ELK, CloudWatch

### Distributed tracing

- OpenTelemetry, Zipkin, Jaeger

### Metrics

- Prometheus + Grafana

### Production monitoring

- Logs + metrics + traces together

---

## 🔹 System Design (Offer-Deciding)

### Order / Payment / URL Shortener

Interviewers look for:

- Data consistency
- Failure handling
- Scaling strategy
- Trade-offs

### CAP theorem (real world)

- You always choose **which one to sacrifice**
- Different choices per system

---

## 

---

# 🔹 Core Java & Coding

## 1️⃣ HashMap vs ConcurrentHashMap – production usage

**HashMap**

- Not thread-safe
- Faster in **single-threaded** or read-only scenarios
- Used in request-scoped/local computations

**ConcurrentHashMap**

- Thread-safe using **CAS + fine-grained locking**
- Allows concurrent reads & limited concurrent writes
- Used in **shared caches, in-memory state, rate limiters**

👉 **Rule**: If shared across threads → `ConcurrentHashMap`.

---

## 2️⃣ First non-repeating character (Java code)

```java
public static Character firstNonRepeating(String str) {
    Map<Character, Long> freq =
        str.chars()
           .mapToObj(c -> (char) c)
           .collect(Collectors.groupingBy(
               c -> c, LinkedHashMap::new, Collectors.counting()));

    return freq.entrySet()
               .stream()
               .filter(e -> e.getValue() == 1)
               .map(Map.Entry::getKey)
               .findFirst()
               .orElse(null);
}

```

👉 Uses `LinkedHashMap` to preserve insertion order.

---

## 3️⃣ equals() & hashCode() impact on performance

- Hash-based collections (HashMap, HashSet) rely on **hashCode**
- Poor hashCode → collisions → LinkedList / Tree traversal
- Can degrade from **O(1) → O(n)**

👉 Always override **both** together and keep hashCode well-distributed.

---

## 4️⃣ Garbage Collection & memory leak troubleshooting

**GC basics**

- Young Gen → frequent, fast
- Old Gen → expensive
- G1/ZGC optimize **latency**

**Finding memory leaks**

- Heap dump (VisualVM / MAT)
- Look for:
    - Growing collections
    - Static references
    - ThreadLocal leaks
- Fix by clearing references and proper lifecycle management

---

# 🔹 Spring Boot & Microservices

## 5️⃣ Spring Boot auto-configuration (internals)

- Based on:
    - Classpath
    - Existing beans
    - Properties
- Uses `@ConditionalOnClass`, `@ConditionalOnMissingBean`

👉 Convention-over-configuration.

---

## 6️⃣ Global exception handling in REST APIs

- Use `@RestControllerAdvice`
- Map exceptions → consistent error responses
- Keeps controllers clean

---

## 7️⃣ Designing for high concurrency

- Stateless services
- Proper thread pool sizing
- Non-blocking I/O where possible
- Caching (Redis)
- Avoid synchronized blocks
- DB connection pool tuning

---

## 8️⃣ One slow microservice impacting system – what to do?

1. Identify bottleneck (CPU, DB, network)
2. Add timeouts + circuit breaker
3. Enable caching
4. Async communication where possible
5. Scale only that service
6. Add fallback responses

👉 Prevent **cascading failures**.

---

# 🔹 SQL & Performance

## 9️⃣ Second highest salary query

```sql
SELECT MAX(salary)
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);

```

---

## 🔟 How indexes work & when they hurt

**Indexes help**

- Speed up reads
- Reduce full table scans

**Indexes hurt when**

- High write volume
- Low-cardinality columns
- Too many indexes

👉 Always validate with **EXPLAIN PLAN**.

---

## 1️⃣1️⃣ Identifying slow queries in production

- Enable slow query logs
- APM tools (New Relic, Dynatrace)
- Database monitoring
- Analyze execution plans

---

# 🔹 Real Production Scenarios

## 1️⃣2️⃣ Debugging live issues when logs aren’t clear

- Metrics (CPU, memory, GC)
- Thread dumps
- Heap dumps
- Distributed tracing
- Feature flags for isolation

👉 Logs alone are never enough in prod.

---

## 1️⃣3️⃣ CPU spike after deployment – steps

1. Roll back immediately (if critical)
2. Compare configs & JVM flags
3. Check infinite loops / thread leaks
4. Analyze GC behavior
5. Review recent code changes

---

## 1️⃣4️⃣ Handling rollback after failed release

- Redeploy previous stable artifact
- Feature toggles
- Database backward-compatible changes
- Blue-green / canary deployments

👉 Rollback must be **fast, predictable, and tested**.

---

##