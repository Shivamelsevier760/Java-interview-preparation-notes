# LeetCode Java interview questions

### ✅ **Q1: What Java version do you use?**

**A:**

> I primarily work with Java 17, which is the current LTS version. It brings performance optimizations and several useful language enhancements over Java 8 and 11.
> 

---

### ✅ **Q2: What new features were introduced in Java 17?**

**A:**

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

### 🚀 Bonus Tip for Interviews:

If asked about Java 8 or 11 features (especially in legacy codebases), just say:

> “Java 8 introduced Streams, Lambdas, and Optionals — revolutionizing how we write functional-style code. Java 11 added features like var in lambda params, HttpClient, and string utility methods. But in my day-to-day, I now lean into Java 17 features like sealed types and pattern matching.”
> 

✅ **Q1: Filter Emp list where name starts with your first name using Streams**

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

### ✅ Sample Output:

```

Emp{id=1, name='Amit Sharma'}
Emp{id=3, name='Amit Yadav'}

```

## ✅ **Q2: Sort the list in reverse order (by name)**

### 🔸 Option 1: Using `.sorted()` with Comparator (Streams)

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

## 🧠 Bonus: Comparator Explained Simply

- **Comparator using method reference**: `Comparator.comparing(Emp::getName)`
- **Reversed**: just chain `.reversed()`
- **Lambda style**: `(a, b) -> a.name.compareTo(b.name)`

## ✅ **Q1: What map implementations do you know in Java?**

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

## ✅ **Q2: How does HashMap work internally?**

You nailed most of it, just needs a tidy summary:

> HashMap uses an array of buckets. When we insert a key-value pair:
> 
> - It calls `hashCode()` on the key to find the index
> - If there's a collision, it uses chaining (a linked list or a tree) to store multiple entries in that bucket
> - `equals()` is used to compare keys in the same bucket

---

## ✅ **What is chaining?**

> Chaining means storing multiple key-value pairs in the same bucket using a LinkedList (pre-Java 8), or a balanced binary tree (like Red-Black Tree) if too many collisions occur (Java 8+).
> 

---

## ✅ **Follow-up: What's the time complexity of insertion with chaining?**

- **Best case** (good hashing, low collisions): `O(1)`
- **Worst case** (bad hash, all keys in one bucket):
    - LinkedList: `O(m)` where `m` is number of items in the bucket
    - Tree (Java 8+): `O(log m)`

---

## 🧠 **Why was the interviewer hinting "tree"?**

Because **Java 8 introduced self-balancing Red-Black Trees** in `HashMap` to handle high-collision buckets efficiently.

**Trigger point:**

> When a bucket contains > 8 entries, and the total number of buckets is > 64, Java converts that bucket from a LinkedList to a Red-Black Tree.
> 

That improves worst-case complexity from `O(m)` to `O(log m)` for lookups and insertions.

---

## ✅ How to explain this in the next interview:

> In earlier versions, HashMap used linked lists for collisions. From Java 8 onward, it switches to Red-Black Trees for better performance in high-collision scenarios, reducing the time complexity from O(m) to O(log m).
> 

## ✅ **Q1: What version of Spring Boot do you use?**

**A:**

> I currently work with Spring Boot 3.3, which is aligned with Spring Framework 6 and uses Jakarta EE 10 under the hood. It brings improved native support (GraalVM), better observability, and support for newer Java versions like Java 17 and 21.
> 

---

## ✅ **Q2: What is Dependency Injection in Spring Boot? What are the advantages?**

**A:**

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

## ✅ Follow-up: **What is a Singleton in Spring?**

**A:**

> A singleton bean is created only once per Spring container, and the same instance is reused across the app. By default, all Spring beans are singletons unless explicitly scoped differently.
> 

---

## ✅ **Q3: If a prototype bean is autowired inside a singleton, will it act like prototype?**

**A (Correct):**

> No, it won’t behave like a prototype. The prototype bean will be created once at startup, when the singleton is created. After that, the same instance is reused by the singleton.
> 

This is because:

- Spring injects the prototype **only once during singleton creation**
- The prototype scope doesn’t apply dynamically unless manually handled

---

### 🚀 **How to get prototype behavior inside a singleton?**

You can use:

### ✅ **Option 1: `ObjectFactory` or `Provider`**

```
@Autowired
private ObjectFactory<MyPrototypeBean> prototypeFactory;

public void someMethod() {
    MyPrototypeBean instance = prototypeFactory.getObject(); // new instance each time
}

```

### ✅ **Option 2: `@Lookup` method**

```
@Lookup
public MyPrototypeBean getPrototypeBean() {
    return null; // Spring overrides this method at runtime
}

```

## ✅ **Q: What types of databases have you used?**

**A:**

> I’ve worked with PostgreSQL (relational), MongoDB (NoSQL/document-oriented), and SAP HANA (in-memory relational DB used often in enterprise scenarios).
> 
> 
> PostgreSQL and HANA follow SQL standards, while MongoDB uses a flexible document model and JSON-like queries.
> 

---

### ✅ Follow-up: *Is HANA SQL or NoSQL?*

**A:**

> HANA is a relational (SQL-based) database, but it's designed for high-performance, in-memory processing. It also supports advanced analytics, JSON-like structures, and can handle both OLTP and OLAP workloads. So it's SQL but optimized for modern, high-speed data processing.
> 

---

## ✅ **SQL Challenge: Count male and female employees from a table with `id` and `gender`**

**Correct Query:**

```jsx
SELECT gender, COUNT(id) AS count
FROM emp
GROUP BY gender;

```

✅ **Explanation:**

- `GROUP BY gender` groups rows by gender type (`M`/`F`)
- `COUNT(id)` counts how many rows per gender
- This returns two rows: one for males, one for females (assuming only those two genders)

### 🔁 Follow-up: “I said I can do it in two separate queries…”

That’s okay — a lot of devs think that way when anxious. But you can mention:

> I initially thought of running two separate queries like:
> 

```jsx
SELECT COUNT(*) FROM emp WHERE gender = 'M';
SELECT COUNT(*) FROM emp WHERE gender = 'F';

```

## ✅ **Q1: Longest Common Prefix Among Words**

**Example:**

```java

Input: ["flower", "flow", "flight"]
Output: "fl"

```

### 🔹 Brute-force approach:

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

### 🔹 Trie-based approach:

- Build a Trie with all words
- Walk down from root until you hit a branch (more than 1 child) or end of word

✅ **Time complexity:** Still O(m * n) but more scalable if reused or extended

> 💡 Bonus: Interviewers love it when you say:
"I’d prefer the simple iterative approach unless prefix queries are frequent, in which case I’d use a Trie."
> 

---

## ✅ **Q2: Longest Common Substring Among Words**

**Note:** This is **not prefix** — substring can appear *anywhere* in all strings.

### 🔹 Brute-force idea:

- Compare every substring of the shortest word with all others — **O(n * m^2)** — not efficient

---

### 🔹 Optimal approach: Dynamic Programming (2-string version)

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

## ✅ **1. Tell me about a time you faced a challenge and what you learned from it**

**Great structure (STAR):**

- **S** (Situation): Set the stage
- **T** (Task): What you had to achieve
- **A** (Action): What *you* did
- **R** (Result): Outcome + Learning

### 💬 Sample Polished Answer:

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

## ✅ **2. This job can be very monotonous. How do you deal with it?**

This is a test for **self-motivation** and **mental resilience**. STAR works well again.

### 💬 Sample Polished Answer:

> In one of my previous projects, I was maintaining a legacy Spring Boot system with repetitive tasks like debugging similar null-pointer exceptions or updating outdated dependencies.
> 
> 
> Instead of getting stuck in the monotony, I created **internal tooling scripts and documentation** to automate repetitive steps — like generating debug reports or smoke tests. I also scheduled **weekly self-learning hours** to explore topics like **Vert.x and reactive streams**, which made me better prepared for modern systems.
> 
> What I’ve learned is that monotony often reveals patterns, and automating those patterns or using that time to skill up can make a routine job feel more **impactful and future-focused**.
> 

👉 **Key takeaway**: I thrive in repetitive work by automating, upskilling, and keeping a long-term perspective.

## ✅ **1. How do you stay up to date and relevant in the field?**

### 💬 Sample Answer:

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

## ✅ **2. What do you think about GenAI?**

### 💬 Sample Answer:

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