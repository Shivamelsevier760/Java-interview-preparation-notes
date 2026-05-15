# Medium interview company questions part 4 by Shivam Srivastava

# **Collabera Java Developer Interview**

## For 5+ Years of Experience

## **1. What is Garbage Collector in Java?**

> This question was also asked in the TCS Interview (Question 6). So, this is an important question.
> 

The Garbage Collector in Java is an automatic memory management feature that helps in reclaiming memory used by objects that are no longer referenced in the program.

It is part of the Java runtime environment and is responsible for cleaning up memory by deleting objects that are no longer reachable.

## **Working**

1. **Automatic Memory Management:**Java programs create objects dynamically, and once an object is no longer used or referenced, it becomes eligible for garbage collection. The garbage collector automatically identifies such objects and reclaims the memory allocated to them.
2. **Heap Memory:**Java uses heap memory for storing objects. The garbage collector primarily works in the heap area, where objects reside. It scans this area and collects objects that are no longer reachable from the root (e.g., active threads, static variables, etc.).
3. **Roots:**The roots are the active references that are used in the program. These include local variables in methods, static variables, and active threads. Anything not reachable from these roots is considered eligible for garbage collection.

## **Types**

Java provides different algorithms and strategies for garbage collection, and they may vary in terms of performance and suitability for various use cases:

1. **Mark-and-Sweep:**This is the most basic algorithm. It consists of two phases:
- **Mark Phase:** Identifies all reachable objects from the roots.
- **Sweep Phase:** Frees the memory occupied by objects that are no longer reachable.

**2. Generational Garbage Collection:**In this approach, the heap is divided into several generations:

- **Young Generation:** Where new objects are created. It is the first place the garbage collector looks for objects to collect.
- **Old Generation (Tenured Generation):** Where objects that have survived multiple garbage collection cycles are moved. It is collected less frequently.
- **Permanent Generation:** Holds metadata related to classes and methods (In Java 8 and later, it was replaced by the Metaspace).
- Most objects in Java are short-lived and thus frequently collectable, which is why young generation collection is done often.

**3. Minor GC vs. Major GC:**

- **Minor GC:** Refers to the collection in the young generation.
- **Major GC (Full GC):** Involves both young and old generations and is more expensive in terms of time and resources.

## **When is Garbage Collection Triggered:**

The Java garbage collector works automatically, and you usually don’t need to manually trigger it. It is triggered when:

- The heap is full and there is no more space to allocate new objects.
- Memory usage crosses certain thresholds set by the JVM.
- Explicitly calling `System.gc()` (though it is not recommended, as the JVM is free to ignore this request).

## **Advantages:**

- **Automatic Memory Management:** Java handles memory management automatically, reducing the chances of memory leaks.
- **No Explicit Deallocation:** You don’t have to worry about explicitly freeing memory, as it’s handled by the garbage collector.
- **Helps Prevent Memory Leaks:** It prevents programs from consuming unnecessary memory due to unreferenced objects lingering in memory.

## **Disadvantages:**

- **Performance Overhead:** Garbage collection takes time and can cause application pauses, especially during full GCs or major collections.
- **Unpredictability:** It is not guaranteed when garbage collection will occur, which can make the performance of your application unpredictable.
- **Can’t Control the Exact Timing:** Developers have no direct control over when garbage collection occurs, which may lead to delays in memory reclamation.

## **Example:**

```
public class GarbageCollectionExample {

// An example class with a constructor
    static class Example {
        int value;
        Example(int value) {
            this.value = value;
        }
        // Method to simulate object usage
        void show() {
            System.out.println("Value: " + value);
        }
        // Overriding finalize method (deprecated in Java 9)
        @Override
        protected void finalize() throws Throwable {
            System.out.println("Garbage collection is triggered for object: " + this);
        }
    }
    public static void main(String[] args) {
        Example obj1 = new Example(10);
        Example obj2 = new Example(20);
        obj1.show();
        obj2.show();
        // Making obj1 eligible for garbage collection
        obj1 = null;
        // Requesting garbage collection (not guaranteed to run immediately)
        System.gc();
        // Making obj2 eligible for garbage collection
        obj2 = null;
        // Requesting garbage collection again
        System.gc();
    }
}
```

## **Output:**

```
Value: 10
Value: 20
Garbage collection is triggered for object: GarbageCollectionExample$Example@15db9742
Garbage collection is triggered for object: GarbageCollectionExample$Example@6d06d69c
```

## **2. What is the daemon thread?**

A daemon thread is a background thread that runs in support of user threads.

It is terminated automatically by the Java Virtual Machine (JVM) when all user (non-daemon) threads have finished execution.

You must call `setDaemon(true)` before starting the thread.

## **Features**

- Runs in the background to perform supporting tasks.
- JVM does not wait for daemon threads before shutting down.
- Must be set as daemon before calling `start()`.
- Threads created by a daemon thread are also daemon threads.
- Cannot be used for tasks that must complete (like saving data).
- Lifecycle depends on user threads.

## **Use Cases**

- Garbage collection (internally handled by JVM)
- Background logging
- Monitoring system health or application metrics
- Running cleanup jobs or file watchers
- Sending heartbeat or status pings periodically

## **Advantages**

- Ideal for lightweight background tasks.
- JVM handles cleanup; no need to manage thread shutdown explicitly.
- Helps reduce resource usage.
- Supports smooth termination of the application.

## **Disadvantages**

- No guarantee of task completion — may be killed abruptly.
- Not suitable for critical operations (e.g., saving files or sending reports).
- Difficult to debug due to silent termination.
- Lives and dies with user threads — no independent lifecycle control.

## **Example**

```
public class DaemonExample {
    public static void main(String[] args) {
        Thread daemonThread = new Thread(() -> {
            while (true) {
                System.out.println("Daemon thread running...");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        daemonThread.setDaemon(true); // Must be set before starting the thread
        daemonThread.start();
        try {
            Thread.sleep(3000);
            System.out.println("Main thread finished.");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

**Output:**

```
Daemon thread running...
Daemon thread running...
Daemon thread running...
Main thread finished.
```

After the main thread ends, the JVM exits, and the daemon thread is terminated — even though it’s still in an infinite loop.

## **3. What is the Contract Between `equals()` and `hashCode()` in Java?**

Java defines a strict contract between `equals()` and `hashCode()` to ensure consistent behavior when objects are stored in hash-based collections like `HashMap`, `HashSet`, or `Hashtable`.

The Contract goes like:

1. If two objects are equal (i.e., `a.equals(b)` returns `true`), then their hash codes must also be equal (`a.hashCode() == b.hashCode()`).
2. If two objects have the same hash code, they are not necessarily equal. (`a.hashCode() == b.hashCode()` does not imply `a.equals(b)`).
3. If `equals()` is overridden, you must override `hashCode()` to maintain the contract.
4. Both `equals()` and `hashCode()` should return the same result unless the object is modified.

## **Importance:**

Violating the contract causes unexpected behavior in collections like `HashMap` or `HashSet`. **For example:**

- If two equal objects have different hash codes, they may go into different buckets and be treated as unequal, breaking lookups.

## **Example**

```
class Person {
    int id;
    String name;

    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Person)) return false;
        Person p = (Person) o;
        return id == p.id && name.equals(p.name);
    }
    @Override
    public int hashCode() {
        return id * 31 + name.hashCode();
    }
}
```

Now `equals()` and `hashCode()` are consistent with each other. Equal objects must have equal hash codes but unequal objects can still have the same hash code.

## **4. How can you make an object a key in a HashMap?**

To use a custom object as a key in a `HashMap`, you must override `equals()` and `hashCode()` properly.

## **Why:**

- `HashMap` uses the `hashCode()` to locate the bucket.
- Then it uses `equals()` to compare keys inside that bucket.
- Without proper overrides, different instances with the same data will be treated as different keys.

## **Steps to Make a Custom Object a Valid Key**

1. Override `equals()` to define logical equality based on relevant fields.
2. Override `hashCode()` to return consistent hash codes for equal objects.
3. Ensure immutability of the key’s fields used in `equals()` and `hashCode()` (optional but recommended).

## **Example**

```
import java.util.*;

class Person {
    int id;
    String name;
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Person)) return false;
        Person p = (Person) o;
        return id == p.id && Objects.equals(name, p.name);
    }
    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
}
public class Main {
    public static void main(String[] args) {
        Map<Person, String> map = new HashMap<>();
        map.put(new Person(1, "John"), "Developer");
        System.out.println(map.get(new Person(1, "John"))); // Output: Developer
    }
}
```

**Without `equals()` and `hashCode():`**

If you skip overriding them, the above `get()` call would return `null`—because even though the data is the same, the hash code and equality are not.

## **5. Explain Singleton design pattern.**

Singleton ensures that only one instance of a class is created throughout the application and provides a global access point to that instance.

## **Characteristics**

- Only one object exists for the class.
- Controlled access via a static method (`getInstance()`).
- Constructor is made private to prevent external instantiation.
- Used when a single shared resource is needed.

## **Use Cases**

- Logger
- Configuration or Properties manager
- Database connection pool manager
- Caching
- Thread pools

## **Implementation (Lazy Initialization — Thread Safe)**

```
public class Singleton {
    private static Singleton instance;

    private Singleton() {
        // private constructor
    }
    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

## **Double-Checked Locking: Thread-Safe + Performance**

```
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}
      public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## **Advantages**

- Controlled access to a single instance
- Saves memory and resources
- Useful for shared configurations or services

## **Disadvantages**

- Hard to test (due to global state)
- Can introduce hidden dependencies
- Breaks Single Responsibility Principle (if not implemented carefully)
- In multi-threaded cases, needs synchronization

If you are interested in learning about Singleton design pattern in detail, I have written a detailed article on the same:

[**Is Your Code Lacking Leadership?See how Singleton brings clarity and control to your code.**medium.com](https://archive.ph/o/xuMbF/https://medium.com/java-and-beyond/is-your-code-lacking-leadership-14215d3fc215)

## **6. How to stop Cloneable in a Singleton design pattern.**

To prevent someone from breaking Singleton design pattern by cloning the object using the `Cloneable` interface, we must override the `clone()` method.

## **Problem: Cloning Breaks Singleton**

```
Singleton s1 = Singleton.getInstance();
Singleton s2 = (Singleton) s1.clone(); // s1 ≠ s2 — breaks Singleton!
```

## **Solution: Override `clone()` and Throw Exception**

```
@Override
protected Object clone() throws CloneNotSupportedException {
    throw new CloneNotSupportedException("Cloning of this singleton is not allowed");
}
```

This ensures that no second instance is created via cloning.

## **Example**

```
public class Singleton implements Cloneable {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException("Cannot clone singleton object");
    }
}
```

## **Alternative Approach: Safe Clone Handling**

If you must implement `Cloneable` (e.g., forced by an interface), return the same instance:

```
@Override
protected Object clone() {
    return instance;
}
```

But best practice is to block cloning altogether using exception.

## **7. Explain Chain of Responsibility design pattern.**

The Chain of Responsibility is a behavioral design pattern where a request is passed along a chain of handlers, and each handler decides whether to process it or pass it to the next one.

## **Concepts**

1. Decouples sender and receiver of a request.
2. Each handler in the chain has a reference to the next handler.
3. Request is processed by first handler that can handle it.

## **Structure**

```
abstract class Handler {
    protected Handler next;

public void setNext(Handler next) {
        this.next = next;
    }
    public abstract void handleRequest(String request);
}
```

## **Example**

```
class Manager extends Handler {
    public void handleRequest(String request) {
        if (request.equals("low")) {
            System.out.println("Manager handled: " + request);
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

class Director extends Handler {
    public void handleRequest(String request) {
        if (request.equals("medium")) {
            System.out.println("Director handled: " + request);
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}
class CEO extends Handler {
    public void handleRequest(String request) {
        System.out.println("CEO handled: " + request);
    }
}
// Usage
Handler manager = new Manager();
Handler director = new Director();
Handler ceo = new CEO();
manager.setNext(director);
director.setNext(ceo);
manager.handleRequest("medium"); // Output: Director handled: medium
```

## **Use Cases**

- Logging frameworks (different levels: INFO, DEBUG, ERROR)
- UI event handling (mouse click passed to components)
- Access control / filtering
- Workflow systems

## **Advantages**

- Reduces tight coupling between sender and receiver
- Easy to add or remove handlers
- Promotes single responsibility per handler

## **Disadvantages**

- Can be hard to debug, especially if chain is long
- No guarantee the request will be handled if chain breaks

## **8. Explain SOLID principles.**

SOLID is an acronym for five core object-oriented design principles that help make software more maintainable, scalable, testable, and robust.

These principles promote clean architecture and are especially useful when working on large systems with evolving requirements.

They were introduced by Robert C. Martin and are considered best practices for designing well-structured, loosely coupled systems in OOP.

## **1. Single Responsibility Principle (SRP)**

A class should have only one reason to change — it should perform only one responsibility.

If a class has multiple responsibilities (e.g., business logic and database operations), a change in one responsibility may break or affect others.

**Example:**

```
// Violates SRP
class Invoice {
    void calculateTotal() { /* logic */ }
    void printInvoice() { /* print logic */ }
    void saveToDB() { /* database logic */ }
}

// Follows SRP
class InvoiceCalculator {
    void calculateTotal() { /* logic */ }
}
class InvoicePrinter {
    void printInvoice() { /* print logic */ }
}
class InvoiceRepository {
    void saveToDB() { /* database logic */ }
}
```

## **2. Open/Closed Principle (OCP)**

Software entities (classes, modules, functions) should be open for extension but closed for modification.

You shouldn’t have to modify existing code to add new behavior — just extend it. This helps avoid bugs in stable code.

**Example:**

```
abstract class Shape {
    abstract double area();
}
class Circle extends Shape {
    double radius;
    Circle(double radius) { this.radius = radius; }
    double area() { return Math.PI * radius * radius; }
}
class Rectangle extends Shape {
    double length, width;
    Rectangle(double l, double w) { this.length = l; this.width = w; }
    double area() { return length * width; }
}
```

## **3. Liskov Substitution Principle (LSP)**

Subtypes must be substitutable for their base types without altering correctness.

If a subclass breaks the expectations of the parent class, you’ve violated LSP. This often leads to unexpected behavior.

**Example:**

```
class Bird {
    void eat() { System.out.println("Bird is eating"); }
}

class FlyingBird extends Bird {
    void fly() { System.out.println("Flying bird"); }
}
class Sparrow extends FlyingBird {}
class Ostrich extends Bird {} // Ostrich can't fly - and that's okay here
```

## **4. Interface Segregation Principle (ISP)**

Clients shouldn’t be forced to depend on interfaces they don’t use.

Smaller, more specific interfaces lead to better design. Large interfaces cause implementing classes to add unnecessary or dummy methods.

**Example:**

```
interface Workable {
    void work();
}

interface Feedable {
    void eat();
}
class Human implements Workable, Feedable {
    public void work() { System.out.println("Human working"); }
    public void eat() { System.out.println("Human eating"); }
}
class Robot implements Workable {
    public void work() { System.out.println("Robot working"); }
}
```

## **5. Dependency Inversion Principle (DIP)**

High-level modules should not depend on low-level modules. Both should depend on abstractions.

DIP promotes loose coupling, making your code easier to test, reuse, and extend.

Instead of wiring dependencies manually, inject them using interfaces or constructors.

**Example:**

```
interface MessageService {
    void sendMessage(String message);
}

class EmailService implements MessageService {
    public void sendMessage(String message) {
        System.out.println("Email sent: " + message);
    }
}
class Notification {
    private final MessageService service;
    public Notification(MessageService service) {
        this.service = service;
    }
    void notifyUser(String msg) {
        service.sendMessage(msg);
    }
}
```

## **9. What are Default methods?**

Default methods were introduced in Java 8 to allow interfaces to have method implementations without breaking existing code.

They help in evolving interfaces over time while maintaining backward compatibility.

## **Features**

- Defined using the `default` keyword in an interface.
- Allow interfaces to have method bodies (i.e., implementation).
- Don’t force implementing classes to override them.
- Help extend APIs without affecting old implementations.

## **Use Cases**

- To add new methods to interfaces without breaking existing classes.
- For code reusability in interfaces.
- To implement mixin-like behavior.

## **Syntax**

```
interface MyInterface {
    default void show() {
        System.out.println("Default implementation");
    }
}
```

## **Example**

```
interface Vehicle {
    default void start() {
        System.out.println("Vehicle is starting...");
    }
}

class Car implements Vehicle {
    // Inherits default method
}
public class Main {
    public static void main(String[] args) {
        Vehicle car = new Car();
        car.start(); // Output: Vehicle is starting...
    }
}
```

## **Conflict Scenario**

If a class implements two interfaces with the same default method, it must override the method to resolve conflict.

```
interface A {
    default void greet() {
        System.out.println("Hello from A");
    }
}

interface B {
    default void greet() {
        System.out.println("Hello from B");
    }
}
class MyClass implements A, B {
    public void greet() {
        // Must override to resolve conflict
        A.super.greet(); // or B.super.greet()
    }
}
```

## **Limitations**

- You can’t create default constructors.
- Default methods can’t override `Object` methods (`toString()`, `hashCode()` etc.).
- Don’t support fields or state like abstract classes.

## **10. What is SQL Injection?**

SQL Injection is a security vulnerability that allows attackers to manipulate SQL queries by injecting malicious input.

It usually occurs when untrusted data is concatenated directly into SQL statements due to improper input validation.

It is generally caused or unsafe string concatenation in SQL queries.

## **Example: Vulnerable Code**

```
String user = "admin";
String pass = "123";

String query = "SELECT * FROM users WHERE username = '" + user + "' AND password = '" + pass + "'";
// If attacker inputs: user = ' OR '1'='1', they can bypass login
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

If `user = ' OR '1'='1`, the final query becomes:

```
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '123';
```

This always returns true and bypasses authentication.

## **Consequences**

- Unauthorized access to user accounts
- Data leakage or loss
- Database manipulation or deletion
- Full server compromise (in some cases)

## **Prevention**

- Use Prepared Statements (Recommended)

```
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement ps = conn.prepareStatement(query);
ps.setString(1, user);
ps.setString(2, pass);
ResultSet rs = ps.executeQuery();
```

- **Validate and sanitize inputs —** Only allow expected characters (e.g., no SQL keywords or special symbols where not needed).
- **Use ORM tools** like Hibernate which abstract direct SQL usage.
- **Least privilege principle** — Don’t give DB users full permissions.

## **11. How do microservices communicate with each other?**

> This question was also asked in Accenture Interview (Question 15). So, this is an important question.
> 

Microservices communicate using different mechanisms depending on the system’s architecture, performance needs, and reliability requirements.

These mechanisms can be broadly categorized into synchronous and asynchronous communication.

## **1. Synchronous Communication (HTTP/REST or gRPC)**

## **HTTP/REST APIs:**

- Microservices often expose RESTful APIs and call each other using HTTP.
- It’s the most common and language-independent communication style.

**Example:**

```
// Using Java and Spring Boot (RestTemplate)
RestTemplate restTemplate = new RestTemplate();
String response = restTemplate.getForObject("http://order-service/orders/123", String.class);
```

**Advantages:**

- Simple and widely supported
- Language agnostic
- Easy to test and debug

## **gRPC (Google Remote Procedure Call):**

- A high-performance, open-source RPC framework using HTTP/2 and Protocol Buffers.
- Supports bi-directional streaming and is more efficient than REST.

**Advantages:**

- Faster communication (binary format)
- Supports contract-first API development
- Ideal for microservices requiring low latency

## **2. Asynchronous Communication (Message Brokers / Event Queues)**

Services communicate via messages passed through a message broker, enabling loose coupling and fault tolerance.

## **Message Queues (RabbitMQ, ActiveMQ):**

**Example:**

```
// Pseudocode to publish a message to RabbitMQ
channel.basicPublish("", "queue_name", null, "New Order Created".getBytes());
```

**Advantages:**

- Decouples services
- More scalable and fault-tolerant
- Services don’t need to be online at the same time

## **Event Streaming (Apache Kafka):**

Microservices publish and subscribe to events. Suitable for systems with high throughput requirements.

**Example:**

```
// Kafka producer in Java
producer.send(new ProducerRecord<>("order-events", "OrderCreated:123"));
```

**Advantages:**

- High performance for event-driven systems
- Durable and scalable
- Enables real-time analytics

## **3. Event-Driven Communication**

Services emit and consume events like “UserCreated” or “OrderPlaced”.

**Advantages:**

- Highly decoupled architecture
- Easy to scale and maintain
- Perfect for loosely-coupled microservices

## **4. Remote Procedure Call (RPC)**

One microservice directly invokes methods on another service over the network.

**JSON-RPC / XML-RPC:**

Uses HTTP to send a serialized request payload (in JSON or XML) to invoke methods.

**gRPC (as mentioned above):**

Efficient and typed RPC with better performance and developer tooling.

## **5. Service Discovery**

Services are often deployed dynamically. To handle this, service discovery tools help microservices find each other.

**Examples**:

- Eureka (by Netflix)
- Consul (by HashiCorp)

**How it works:**

- Services register themselves
- Other services query the registry to locate them

## **6. API Gateway for Aggregation**

An API Gateway acts as a single entry point to a set of microservices and can route or aggregate requests.

**Example Use Case:**

A mobile app calls a single endpoint `/user/dashboard`, which internally aggregates calls to `user-profile`, `orders`, and `notifications` services.

**Advantages:**

- Centralizes routing, authentication, and throttling
- Reduces client-side complexity

## **7. Circuit Breaker Pattern**

Used to handle failures in service-to-service communication.

**Example Tools:**

- Hystrix
- Resilience4j

**How it helps:**

- Detects failure in a service call
- Stops repeated failing requests to prevent cascading failure
- Automatically retries after a cooldown period

**12. What are the differences between Stream vs Parallel Stream?*This question was also asked in [EY Interview (Question 6).](https://archive.ph/o/xuMbF/https://medium.com/coding-odyssey/ey-java-developer-interview-18f86c1e856e) So, this is an important question.***

![](https://ddxhi9hzrw0bfk.archive.ph/xuMbF/9e852adc9e7af2ce0d50d65d0bc09d74cd876ebf.webp)

## **13. If I make a variable static, will it take part in the serialization process?**

No, static variables do not take part in the serialization process.

- Serialization is the process of converting an object’s state into a byte stream so it can be persisted or transferred.
- Static variables belong to the class, not to any specific instance.
- Since serialization is all about saving the state of an object instance, and static variables are not part of the object’s state, they are ignored during serialization.

## **Example:**

```
import java.io.*;

class Student implements Serializable {
    int id;
    String name;
    static String school = "ABC School"; // Static variable
    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
public class TestSerialization {
    public static void main(String[] args) throws Exception {
        Student s1 = new Student(1, "John");
        // Serialize
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("student.txt"));
        out.writeObject(s1);
        out.close();
        // Change static value after serialization
        Student.school = "XYZ School";
        // Deserialize
        ObjectInputStream in = new ObjectInputStream(new FileInputStream("student.txt"));
        Student s2 = (Student) in.readObject();
        in.close();
        System.out.println(s2.id);      // 1
        System.out.println(s2.name);    // John
        System.out.println(Student.school); // XYZ School (not ABC School)
    }
}
```

## **Output:**

```
1
John
XYZ School
```

## **14. Explain Internal working of Hashset.**

`HashSet` is a collection class in Java that stores unique elements. Internally, it uses a `HashMap` to store its elements.

It does not maintain insertion order and allows only one null element.

## **Internal Working:**

1. **Backed by a HashMap**
- `HashSet` internally creates a `HashMap` instance.
- Every element added to the `HashSet` is stored as a key in the `HashMap`.
- A dummy value (like `PRESENT`, usually a static final object) is used for all keys.

```
private transient HashMap<E,Object> map;
private static final Object PRESENT = new Object();
```

**2. Adding Elements**

- When you add an element to a `HashSet`, it does this under the hood:

```
map.put(element, PRESENT);
```

- If the key already exists, the `put()` method returns the old value and does not insert the duplicate.

**3. Hashing & Bucketing**

- The key (your element) is hashed using its `hashCode()`, then the bucket is determined.
- If two elements have the same hash, collision resolution (via linked list or tree in Java 8+) is used.

**4. Uniqueness:**

Uniqueness is maintained by:

- Checking if the key already exists via `equals()` and `hashCode()`.
- So, it’s important to override these methods in your class if you’re using custom objects.

## **Example:**

```
import java.util.HashSet;

class Student {
    int id;
    String name;
    Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
    // Must override hashCode and equals to ensure uniqueness
    @Override
    public int hashCode() {
        return id;
    }
    @Override
    public boolean equals(Object obj) {
        Student s = (Student) obj;
        return this.id == s.id;
    }
}
public class TestHashSet {
    public static void main(String[] args) {
        HashSet<Student> set = new HashSet<>();
        set.add(new Student(1, "John"));
        set.add(new Student(1, "John"));
        System.out.println("Set size: " + set.size()); // Output: 1
    }
}
```

## **15. How can you make a HashMap synchronised?**

By default, `HashMap` is not synchronized, meaning:

- It is not safe to use in multi-threaded environments where multiple threads access and modify it concurrently.
- This can lead to data inconsistency, race conditions, or even infinite loops during iteration (due to structural changes).

## **Making HashMap Synchronised:**

The simplest way to make a `HashMap` thread-safe is by wrapping it with `Collections.synchronizedMap()`.

```
Map<K, V> syncMap = Collections.synchronizedMap(new HashMap<>());
```

**Note:** For safe iteration, you must manually synchronize the block:

```
synchronized (syncMap) {
    for (Map.Entry<K, V> entry : syncMap.entrySet()) {
        // thread-safe iteration
    }
}
```

## **Example:**

```
import java.util.*;

public class SynchronizedHashMapExample {
    public static void main(String[] args) {
        // Option 1: Synchronized HashMap
        Map<String, String> syncMap = Collections.synchronizedMap(new HashMap<>());
        syncMap.put("A", "Apple");
        syncMap.put("B", "Banana");
        synchronized (syncMap) {
            for (Map.Entry<String, String> entry : syncMap.entrySet()) {
                System.out.println(entry.getKey() + " = " + entry.getValue());
            }
        }
    }
}
```

## **16. What is Collections Class?**

The `Collections` class in Java is a utility class that belongs to the `java.util` package.

- It cannot be instantiated.
- It provides static methods to operate on or return collections such as List, Set, and Map.
- Think of it as a helper toolbox for collection-related operations like sorting, searching, shuffling, synchronizing, etc.

## **Features**

1. Utility methods for common operations on collections.
2. Can be used to create read-only, synchronized, or empty collections.
3. Works only with Collection implementations, not with arrays (for arrays, use `Arrays` class).

## **Example**

```
import java.util.*;

public class CollectionsClassExample {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Banana");
        fruits.add("Apple");
        fruits.add("Mango");
        // Sort the list
        Collections.sort(fruits);
        System.out.println("Sorted List: " + fruits); // [Apple, Banana, Mango]
        // Reverse the list
        Collections.reverse(fruits);
        System.out.println("Reversed List: " + fruits); // [Mango, Banana, Apple]
        // Shuffle the list
        Collections.shuffle(fruits);
        System.out.println("Shuffled List: " + fruits); // Random order
        // Get min and max
        System.out.println("Min: " + Collections.min(fruits));
        System.out.println("Max: " + Collections.max(fruits));
        // Frequency
        fruits.add("Apple");
        System.out.println("Frequency of Apple: " + Collections.frequency(fruits, "Apple"));
        // Synchronized list
        List<String> syncList = Collections.synchronizedList(fruits);
    }
}
```

# **Mastercard Java Developer Interview**

## For 6+ Years of Experience

## **1. Explain any three microservice design patterns.**

Below are three commonly used microservice design patterns:

## **1. API Gateway Pattern**

**Problem it solves:**In a microservices architecture, each service has its own endpoint. But exposing all those endpoints directly to clients (like browsers or mobile apps) can be complex and insecure.

**Solution:**Use an API Gateway as a single entry point for all client requests. The gateway then routes the requests to the appropriate backend microservices.

**Benefits:**

- Centralized authentication, rate limiting, and logging
- Reduces round trips for the client by aggregating responses from multiple services
- Shields internal services from direct exposure

**Example:**Netflix uses Zuul as an API Gateway. AWS uses API Gateway to expose services securely.

## **2. Circuit Breaker Pattern**

**Problem it solves:**In a distributed system, if one service fails or is slow, it can cause cascading failures across other services.

**Solution:**Use a Circuit Breaker that monitors the calls to a remote service. If failures go beyond a threshold, it opens the circuit and returns fallback responses instead of calling the failed service again.

**Benefits:**

- Prevents the system from being overloaded
- Enables quick failure responses to the client
- Allows time for the failing service to recover

**Example:**Netflix’s Hystrix library implements this pattern.

## **3. Database per Service Pattern**

**Problem it solves:**In microservices, each service should be loosely coupled. Sharing a common database creates tight coupling and can lead to data management issues.

**Solution:**Each microservice has **its own dedicated database**, and it manages its own schema and data independently.

**Benefits:**

- Decouples services at the data layer
- Easier to scale services individually
- Promotes data ownership and security

**Challenges:**

- Managing data consistency across services becomes tricky (solved using patterns like Saga)

## **2. Explain Circuit Breaker Design Pattern.**

> This question was asked in both first and second rounds at Capgemini Interview, TCS Interview and CGI Interview. So, this is an important question.
> 

In a microservices architecture, a Circuit Breaker is a design pattern used to detect failures in a system and prevent them from propagating to other parts of the system.

It helps in improving the system’s resilience by allowing the system to recover from failures gracefully.

The main goal is to prevent a system from repeatedly making calls to a service that is failing and causing additional load or cascading failures.

## **Working:**

1. **Closed State**:
- In the closed state, the circuit breaker allows all requests to go through to the service.
- If the service responds successfully, everything continues as normal.
- If the service fails a number of times (typically due to timeouts or exceptions), the circuit breaker moves to the open state.

**2. Open State**:

- When the failure threshold is exceeded, the circuit breaker “opens” and all requests are rejected.
- During this time, instead of making the request, the circuit breaker returns a fallback response or performs other recovery mechanisms.
- After a certain “cooldown” period, the circuit breaker will move to the half-open state.

**3. Half-Open State**:

- In the half-open state, the circuit breaker allows a limited number of requests to pass through to check if the issue is resolved.
- If the service is working fine, the circuit breaker goes back to the closed state.
- If the service is still failing, the circuit breaker goes back to the open state.

## **Components:**

1. **Failure Threshold**: The number of failures after which the circuit breaker will open.
2. **Timeouts**: Time window after which the circuit breaker switches back from the open to the half-open state.
3. **Fallback Mechanism**: In case of failure, a fallback response can be provided, such as cached data or default values.

## **Advantages:**

1. **Prevents cascading failures**: By stopping the flow of requests to a failing service, you prevent further damage or system overload.
2. **Improves resilience**
    
    : The system can recover more gracefully by falling back to alternative paths.
    
3. **Better resource management**: The system avoids overloading failing services and uses resources more efficiently.

## **3. Explain Bounded Context in Microservices.**

Bounded Context is a core concept from Domain-Driven Design (DDD). It refers to a well-defined boundary within which a particular domain model is applicable and consistent.

In a microservices architecture, each microservice is treated as a Bounded Context, meaning it owns its data, business logic, and responsibilities, without overlapping with other services.

## **Principles**

- Each service has clear ownership over its domain.
- No shared databases between services.
- Services communicate via APIs or event messaging.
- Changes in one context shouldn’t break others.

## **Advantages**

- Promotes loose coupling between services
- Supports independent deployment and scaling
- Improves code maintainability
- Prevents data inconsistency
- Enables cross-functional teams to own different parts of the system

## **Disadvantages**

- **Data duplication** — Services may store overlapping data
- **Complex integration** — Coordination across services can be tricky
- **Hard to define boundarie**s — Especially when domain knowledge is weak
- Testing across services is more complex
- Refactoring is harder if context boundaries are incorrectly drawn initially

## **Example**

In an e-commerce application, you might split functionality into different bounded contexts:

- `User Service` → Manages registration, login, and profiles
- `Product Service` → Handles inventory, pricing, and descriptions
- `Order Service` → Responsible for placing, tracking, and managing orders

Each service has its own database, API, and logic, and they communicate via APIs or events.

## **Example Code (Java + Spring Boot)**

**`UserService` – Owns user data and logic**

```
@RestController
@RequestMapping("/users")
public class UserController {

@Autowired
    private UserService userService;
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUser(@PathVariable Long id) {
        User user = userService.getUserById(id);
        return ResponseEntity.ok(new UserDTO(user));
    }
}
public class UserDTO {
    private Long id;
    private String name;
    // constructor, getters
}
```

**Own DB (users table):**

```
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);
```

**`OrderService` – Calls UserService via REST**

```
@RestController
@RequestMapping("/orders")
public class OrderController {

@Autowired
    private OrderService orderService;
    @PostMapping
    public ResponseEntity<String> placeOrder(@RequestBody OrderRequest request) {
        boolean userExists = orderService.verifyUser(request.getUserId());
        if (!userExists) {
            return ResponseEntity.badRequest().body("Invalid user");
        }
        orderService.createOrder(request);
        return ResponseEntity.ok("Order placed successfully");
    }
}
public boolean verifyUser(Long userId) {
    String url = "http://USER-SERVICE/users/" + userId;
    try {
        ResponseEntity<UserDTO> response = restTemplate.getForEntity(url, UserDTO.class);
        return response.getStatusCode() == HttpStatus.OK;
    } catch (HttpClientErrorException.NotFound e) {
        return false;
    }
}
```

## **4. Explain API Gateway.**

I have already written a detailed article with additional interview questions on API Gateways. I recommend you to please go through the it:

[**API Gateway with Spring Boot: Deep Dive with Interview QuestionsA Comprehensive Guide**medium.com](https://archive.ph/o/ckOOF/https://medium.com/coding-odyssey/api-gateway-with-spring-boot-deep-dive-with-interview-questions-1a65954ad5f3)

## **5. Suppose we have multiple microservices and we jump from one microservice to another. How the other microservices maintain sessions?**

In a microservices architecture, traditional server-side session handling (like `HttpSession`) doesn’t scale well across multiple services.

So instead of maintaining state on the server, microservices use stateless authentication, usually through JWT (JSON Web Tokens).

## **Working**

1. Login Request is sent to an `AuthService`.
2. `AuthService` verifies credentials and returns a JWT token.
3. The client stores this token (e.g., in browser localStorage).
4. The client sends the token in the `Authorization` header (Bearer token) with every request to any microservice.
5. Each microservice validates the token and extracts user data from it — no need for shared sessions.

This way, every microservice can independently validate who the user is without calling the authentication service again.

## **Advantages**

- Stateless and scalable
- No need for session replication or shared session stores
- Token contains all required user context (user ID, roles, etc.)
- Easy to pass between services (via HTTP headers or service-to-service communication)

## **Code Example**

**Step 1: User logs in via `AuthService`**

```
@PostMapping("/login")
public ResponseEntity<?> login(@RequestBody AuthRequest request) {
    if (authenticate(request)) {
        String token = jwtUtil.generateToken(request.getUsername());
        return ResponseEntity.ok(new AuthResponse(token));
    }
    return ResponseEntity.status(401).body("Unauthorized");
}
```

**Step 2: JWT Token Generation**

```
public String generateToken(String username) {
    return Jwts.builder()
        .setSubject(username)
        .setIssuedAt(new Date())
        .setExpiration(new Date(System.currentTimeMillis() + 3600000)) // 1 hour
        .signWith(SignatureAlgorithm.HS256, "secretKey")
        .compact();
}
```

**Step 3: Every microservice validates JWT**

```
public boolean validateToken(String token) {
    try {
        Jwts.parser().setSigningKey("secretKey").parseClaimsJws(token);
        return true;
    } catch (Exception e) {
        return false;
    }
}
```

**Step 4: Use Filter to secure microservices**

```
@Component
public class JwtFilter extends OncePerRequestFilter {
    @Autowired
    private JwtUtil jwtUtil;

    protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain) {
        String header = req.getHeader("Authorization");
        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            if (jwtUtil.validateToken(token)) {
                // token is valid → set security context
            }
        }
        chain.doFilter(req, res);
    }
}
```

## **6. What is Event Sourcing?**

Event Sourcing is a design pattern where state changes in an application are captured as a sequence of immutable events, instead of storing only the latest state in a database.

## **Traditional vs Event Sourcing**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/546fc0923d925977054e57ffee0c32d822aca54e.webp)

## **Working:**

1. An action happens (e.g., user places an order).
2. The system generates an event (e.g., `OrderPlaced`).
3. This event is stored in an append-only event store.
4. The current state is reconstructed by replaying events in order.
5. Optionally, you use projections to build queryable views from events.

## **Advantages:**

- **Auditability**: Complete history of what happened.
- **Debugging & Time Travel**: Replay events to understand system behavior at any point.
- **Scalability**: Works well with CQRS (Command Query Responsibility Segregation).
- **Flexibility**: Can rebuild state in different ways from the same events.

## **Disadvantages:**

- Increased complexity in design and debugging.
- Handling schema changes in old events can be tricky.
- Querying current state directly is not trivial — you rely on projections.

## **Example**

Let’s take a bank account example:

```
// Event interface
public interface AccountEvent {}

// Event classes
public class MoneyDeposited implements AccountEvent {
    private final int amount;
    public MoneyDeposited(int amount) { this.amount = amount; }
    public int getAmount() { return amount; }
}
public class MoneyWithdrawn implements AccountEvent {
    private final int amount;
    public MoneyWithdrawn(int amount) { this.amount = amount; }
    public int getAmount() { return amount; }
}
// Account Aggregate
public class BankAccount {
    private int balance = 0;
    public void apply(AccountEvent event) {
        if (event instanceof MoneyDeposited deposit)
            balance += deposit.getAmount();
        else if (event instanceof MoneyWithdrawn withdraw)
            balance -= withdraw.getAmount();
    }
    public int getBalance() { return balance; }
}
```

You store each event (deposit, withdrawal), and rebuild balance by replaying them.

## **7. How to scale your microservices application?**

> This question was also asked in the TCS Interview. So, this is an important question.
> 

Scaling a microservices application involves handling increased load efficiently while maintaining performance, reliability, and cost-effectiveness.

Below are key strategies to scale a microservices-based application:

## **1. Horizontal Scaling (Scaling Out)**

- Add more instances of a microservice.
- Use load balancers (e.g., Nginx, HAProxy) to distribute traffic evenly.
- **Example**: Running multiple instances of an authentication service behind a load balancer.

## **2. Vertical Scaling (Scaling Up)**

- Increase resources (CPU, RAM) of existing instances.
- Works for monolithic parts but has limitations compared to horizontal scaling.

## **3. Load Balancing**

- Distribute requests among multiple instances.
- Can be client-side, server-side, or DNS-based.
- **Tools:** Nginx, AWS ALB/ELB, Kubernetes Ingress.

## **4. API Gateway**

- Acts as an entry point for all requests.
- Provides rate limiting, caching, authentication, and logging.
- **Examples**: Kong, Netflix Zuul, Apigee, AWS API Gateway.

## **5. Containerization and Orchestration**

- Containers (Docker) ensure lightweight, consistent deployments.
- Kubernetes or Docker Swarm automate scaling and self-healing.

## **6. Database Scaling**

- **Read Replicas** → Scale read-heavy operations.
- **Sharding** → Distribute data across multiple databases.
- **Caching** (Redis, Memcached) → Reduce database load.

## **7. Asynchronous Processing**

- Use message queues (RabbitMQ, Kafka) for decoupling services.
- Implement event-driven architecture for handling background tasks.

## **8. Auto-scaling**

- Dynamically increase/decrease instances based on demand.
- **Tools:** Kubernetes Horizontal Pod Autoscaler (HPA), AWS Auto Scaling.

## **9. Distributed Logging and Monitoring**

- Centralized monitoring helps in debugging and performance optimization.
- **Tools**: ELK Stack, Prometheus, Grafana, Jaeger (tracing).

## **10. Fault Tolerance & Circuit Breaker Pattern**

- Prevent cascading failures with circuit breakers (Resilience4j, Netflix Hystrix).
- Implement retries and failover mechanisms.

## **11. Edge Computing**

- Move processing closer to users (e.g., AWS Lambda, CloudFront).

## **8. What is the default message size in Kafka?**

The default maximum message size in Apache Kafka is: *1 MB.*

This is enforced through two main configurations:

- On the **broker side**: `message.max.bytes`
- On the **producer side**: `max.request.size`

## **Default Configuration Values**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/27c5b917bae140db645d934d5259a30a235f4f9c.webp)

## **Working**

1. A producer sends messages to a Kafka topic.
2. Kafka will reject any message larger than:
- `max.request.size` on the producer
- or `message.max.bytes` on the broker — whichever is smaller.

3. The consumer must also have `fetch.message.max.bytes` high enough to receive large messages.

## **Messages Larger Than 1 MB:**

You must update all three configs to send messages larger than 1 MB:

## **Broker:**

```
message.max.bytes = 10485760   # 10 MB
```

## **Producer:**

```
props.put("max.request.size", 10485760);  // 10 MB
```

## **Consumer:**

```
props.put("fetch.message.max.bytes", 10485760);  // 10 MB
```

All three must be updated, or the system will throw an error.

## **9. What parameters are to be configured for a flow of message from Producer to Broker to Consumer in Kafka?**

To ensure a smooth flow of messages from Producer ➝ Broker ➝ Consumer in Apache Kafka, each component must be properly configured.

These configurations help manage message size, reliability, batching, buffering, and performance.

## **Producer-Side Parameters**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/d23943b3d042bfbb95f5e6a1049ddca6b808bf11.webp)

## **Broker-Side Parameters**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/c76f59e83eb57419957ac95a956a77fabf5a247f.webp)

## **Consumer-Side Parameters**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/f9d3eb9ef57d1aeb9b5de52a070741ac45aed0e7.webp)

## **Flow:**

1. **Producer** sends data using batching, compression, and buffering.
2. **Broker** receives data, handles message persistence and replication based on its limits.
3. **Consumer** fetches messages based on fetch size, offset handling, and group coordination.

## **10. If message is beyond the default size, what happens in Kafka?**

When a message sent to Kafka exceeds the configured size limits, the system will reject the message, and an error will be thrown — either by the producer, broker, or consumer, depending on where the limit is violated.

## **What Happens When a Limit is Exceeded?**

**Case 1: Message too large on Producer**

- Kafka producer throws an exception:**`RecordTooLargeException`**
- **Reason**: The message (or batch) exceeds `max.request.size`.

**Case 2: Message rejected by Broker**

- Producer receives a **`RecordTooLargeException`** from the broker.
- **Reason:** The broker’s `message.max.bytes` is smaller than the producer’s message size.

**Case 3: Consumer can’t fetch large messages**

- The consumer fails to receive the message if its `fetch.message.max.bytes` or `max.partition.fetch.bytes` is too low.
- You may see partial fetches or missing records.

## **Handling larger messages:**

To support larger messages, all three components must be reconfigured:

**Producer**:

```
props.put("max.request.size", 10485760);  // 10 MB
```

**Broker (`server.properties`):**

```
message.max.bytes = 10485760  # 10 MB
```

**Consumer:**

```
props.put("fetch.message.max.bytes", 10485760);  // 10 MB
props.put("max.partition.fetch.bytes", 10485760); // Optional
```

**Note**: All values should be set in sync. If even one is lower, message transfer will fail.

## **11.What is replication factor in Kafka? Give its use cases.**

In Kafka, the replication factor defines how many copies of each partition are maintained across different brokers in a Kafka cluster.

**For example:**If a topic has 3 partitions and replication factor = 2, Kafka will store 2 copies of each partition (one leader + one follower), across different brokers.

## **Importance:**

The replication factor is critical for high availability and fault tolerance. If one broker goes down, Kafka can still serve data from the replica on another broker.

## **Key Concepts**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/c4046975e7dc0828b40717c17327a1b0c8dfe30a.webp)

## **Working**

1. When you create a topic, you specify:
- Number of partitions
- Replication factor (e.g., 2 or 3)

2. Kafka distributes replicas of each partition to different brokers.

3. One replica is chosen as leader, others act as followers.

4. Producers write to the leader.

5. Consumers read from the leader.

6. If the leader fails, Kafka automatically promotes a follower as the new leader (if it’s in-sync).

## **Use Cases**

![](https://dc8nfgjm01zxrb.archive.ph/ckOOF/b0beb64afb441be8f486e3249a4fab03dd3dd331.webp)

## **12. What is fault tolerance? Is it possible to implement fault tolerance using replication factor.**

Fault tolerance refers to a system’s ability to continue operating correctly even when some of its components fail.In distributed systems like Kafka, fault tolerance ensures that the system remains available and consistent despite broker failures, hardware crashes, or network issues.

## **Fault Tolerance in Kafka**

Kafka achieves fault tolerance primarily through:

- Replication of partitions across multiple brokers
- Leader election when a broker goes down
- In-Sync Replica (ISR) monitoring to ensure consistent data copies
- Acknowledgment configurations (acks) to ensure delivery guarantees

## **Implementation:**

Fault tolerance is implemented using the replication factor.

1. Each Kafka partition is replicated based on the configured replication factor (e.g., 3).
2. Kafka ensures that replicas are placed on different brokers.
3. One replica acts as the leader; others are followers (in the ISR set).
4. If the leader broker fails, Kafka automatically promotes a follower to be the new leader.
5. The system remains available to producers and consumers — no data loss, no downtime (if properly configured).

## **Example**

Let’s say:

- A topic has replication factor = 3
- Partition `P0` is stored on `Broker-1` (leader), `Broker-2`, and `Broker-3`

If `Broker-1` crashes:

- Kafka elects `Broker-2` (if in ISR) as the new leader
- Producers/Consumers switch to the new leader
- No data loss or interruption

# **Final Thoughts**

This was very clearly a project interview as the focus was based only on Microservices and Kafka (which could be the dominant technology used in the projects).

# **EY Java Developer Interview**

**1. What are the differences between Spring MVC vs Spring Boot?**

![](https://d346qdrwq5qz9y.archive.ph/rtVp3/48f41e03c7707069370d358af3c469f7305a7a84.webp)

## **2. How to change server in Spring Boot?**

To Change Server from Tomcat to Jetty or Undertow:

## **1. Change it for Maven**

**Change to Jetty:**

```
<dependencies>
    <!-- Remove Tomcat -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-tomcat</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
<!-- Add Jetty -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-jetty</artifactId>
    </dependency>
</dependencies>
```

**Change to Undertow:**

```
<!-- Exclude Tomcat -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<!-- Include Undertow -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-undertow</artifactId>
</dependency>
```

## **2. Change it for Gradle:**

```
dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web') {
        exclude group: 'org.springframework.boot', module: 'spring-boot-starter-tomcat'
    }

implementation 'org.springframework.boot:spring-boot-starter-jetty'  // or undertow
}
```

## **3. Explain some REST Methods.**

Below are some of the common REST (or HTTP) methods:

## **1. GET**

- **Purpose:** Fetch data from the server.
- **Example:** `GET /users/123`
- **Use Case:** Retrieve user details with ID 123.
- **Idempotent:** Yes (Calling it multiple times gives the same result)

## **2. POST**

- **Purpose:** Create a new resource on the server.
- **Example:** `POST /users`
- **Use Case:** Add a new user by sending user data in the request body.
- **Idempotent:** No (Calling it multiple times may create duplicate resources)

## **3. PUT**

- **Purpose:** Update a resource completely (or create it if it doesn’t exist).
- **Example:** `PUT /users/123`
- **Use Case:** Replace the entire user details of user ID 123.
- **Idempotent:** Yes (Same data sent again won’t change result)

## **4. PATCH**

- **Purpose:** Update a part of the resource.
- **Example:** `PATCH /users/123`
- **Use Case:** Change just the email of the user ID 123.
- **Idempotent:** Yes (if patching with same data repeatedly)

## **5. DELETE**

- **Purpose:** Remove a resource from the server.
- **Example:** `DELETE /users/123`
- **Use Case:** Delete user with ID 123.
- **Idempotent:** Yes (Once deleted, future delete calls don’t affect state)

## **4. Explain PATCH Method.**

The PATCH method is used to partially modify an existing resource on the server. Instead of sending the entire resource like `PUT`, you send only the fields you want to update.

## **Characteristics:**

- **Partial Update:** Only the specified fields are modified.
- **Does not replace the whole resource.**
- **Efficient for bandwidth:** Smaller payloads compared to `PUT`.
- **Idempotent (ideally):** Repeating the same `PATCH` request should result in the same resource state (if the operation doesn't depend on timestamps or server-side logic). PATCH is not always idempotent if your server logic involves state change (like timestamps, counters, etc.).

## **Example:**

**Let’s say we have a user:**

```
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}
```

Now, we want to update only the email.

**Endpoint:** `PATCH /users/123`**Request Body:**

```
{
  "email": "newemail@example.com"
}
```

**Result:**Only the email is updated. Other fields (like name and phone) remain unchanged.

## **Use case**

- Updating a single attribute like a password or profile picture.
- Modifying just the status of an order.
- Changing settings without affecting other configurations.

## **JSON Patch (RFC 6902)**

Some APIs use a specific format called JSON Patch, which allows multiple operations in one request.

**Example:**

```
[
  { "op": "replace", "path": "/email", "value": "new@example.com" },
  { "op": "remove", "path": "/phone" }
]
```

This instructs the server to:

- Replace the email
- Remove the phone number

This approach is more structured and gives more control but requires additional parsing on the backend.

## **5. What are some of the features of Java 8?**

Java 8 was a major release and brought a ton of powerful features that modernized the language. Below are some of the most important features:

## **1. Lambda Expressions**

- **Purpose:** Enable functional programming by treating code as data.
- **Syntax Example:**

```
(a, b) -> a + b
```

- **Use Case:** You can pass behavior (functions) as parameters.

## **2. Functional Interfaces**

- **Definition:** An interface with a single abstract method.
- **Example:**

```
@FunctionalInterface
interface Calculator
{
     int operate(int a, int b);
}
```

- **Java 8 includes built-in ones** like `Predicate`, `Function`, `Supplier`, and `Consumer`.

## **3. Stream API**

- **Purpose:** Process collections of data in a functional-style pipeline.
- **Example:**

```
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.stream()
     .filter(name -> name.startsWith("A"))
     .forEach(System.out::println);
```

- **Supports:** Filtering, mapping, sorting, reducing, and more.

## **4. Default and Static Methods in Interfaces**

- **Purpose:** Add methods to interfaces without breaking existing implementations.
- **Example:**

```
interface MyInterface {
    default void show() {
        System.out.println("Default method");
    }

    static void display() {
        System.out.println("Static method");
    }
}
```

## **5. Method References**

- Shortcut for calling a method using `::` operator.
- **Example:**

```
list.forEach(System.out::println);
```

## **6. Optional Class**

- Avoid `NullPointerException` by using a container object that may or may not contain a non-null value.
- **Example:**

```
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(System.out::println);
```

## **7. New Date and Time API (java.time package)**

- More powerful, immutable, and thread-safe than `java.util.Date`.
- **Example:**

```
LocalDate today = LocalDate.now();
LocalDate birthday = LocalDate.of(1990, Month.JANUARY, 1);
```

## **8. Collectors and the Collect API**

- Used with streams to accumulate elements into collections, strings, or summary statistics.
- **Example:**

```
List<String> list = names.stream()
                          .filter(name -> name.length() > 3)
                          .collect(Collectors.toList());
```

## **9. Nashorn JavaScript Engine**

- Allows execution of JavaScript code from Java.
- **Example:**

```
ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
engine.eval("print('Hello from JavaScript')");
```

## **10. Parallel Streams**

- Process data **concurrently** using multiple threads.
- Just change `.stream()` to `.parallelStream()`:

```
list.parallelStream().forEach(System.out::println);
```

**6. What are the differences between Stream vs Parallel Stream?**

![](https://d346qdrwq5qz9y.archive.ph/rtVp3/5199aaf6a5550d22135dc388b5bf81f2ee782356.webp)

## **7. Explain Intermediate Operations.**

Intermediate operations are the transformations applied to a stream before the final result is obtained. They don’t produce a final result on their own — they just prepare the data.

They’re always followed by a terminal operation like `collect()`, `forEach()`, or `count()`.

## **Features:**

- They are lazy — meaning, nothing happens until a terminal operation is called.
- They return a new stream instead of modifying the original one.
- You can chain multiple intermediate operations.

## **Common Intermediate Operations:**

![](https://d346qdrwq5qz9y.archive.ph/rtVp3/29d574ed6f8452eabb3fa97bc5a76332af3997c7.webp)

## **Example:**

```
List<String> names = List.of("Alice", "Bob", "Alex", "Anna");

names.stream()
     .filter(name -> name.startsWith("A"))      // keeps "Alice", "Alex", "Anna"
     .map(String::toUpperCase)                  // transforms to uppercase
     .sorted()                                  // sorts the names
     .forEach(System.out::println);             // terminal operation
```

The operations `filter`, `map`, and `sorted` are intermediate. Only `forEach` triggers their execution.

**8. What are the differences between Map vs FlatMap?**

![](https://d346qdrwq5qz9y.archive.ph/rtVp3/fce8a53eae7a13648d9a7be5770b7428986abb0f.webp)

## **9. What are Default methods and How to implement it in functional interface?**

In Java 8 and later, default methods allow you to add method implementations inside interfaces without affecting the classes that already implement them.

Before Java 8, interfaces could only have abstract methods (i.e., no body). But with default methods, you can now have concrete methods (with body) in interfaces.

## **Need:**

1. To add new functionality to interfaces without breaking existing code.
2. To support multiple inheritance of behavior in interfaces.
3. To enable functional programming patterns (like in functional interfaces).

## **Syntax:**

```
interface MyInterface {
    default void greet() {
        System.out.println("Hello from default method!");
    }
}
```

Any class implementing `MyInterface` will inherit the `greet()` method automatically, unless it overrides it.

## **Using Default Methods in a Functional Interface**

A functional interface is an interface with exactly one abstract method. But it can have multiple default or static methods.

## **Example:**

```
@FunctionalInterface
interface Calculator {
    int operate(int a, int b); // abstract method

default void printInfo() {
        System.out.println("This is a functional interface with a default method.");
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator add = (a, b) -> a + b;
        System.out.println("Result: " + add.operate(5, 3));
        add.printInfo(); // calling the default method
    }
}
```

## **10. What is Transient Keyword?**

In Java, the `transient` keyword is used to mark a variable as non-serializable — meaning, it will not be saved when an object is serialized.

In other words, transient variables are not saved when an object is serialized to a stream and are ignored when the object is later deserialized.

## **Use cases**

You use `transient` when you don't want a variable's value to be serialized, typically for:

1. **Sensitive Data:** Variables containing sensitive data (e.g., passwords, encryption keys) that should not be saved to a file.
2. **Volatile Data:** Variables that are computed dynamically or are not needed after the object is deserialized (e.g., UI-related variables).
3. **Non-Serializable Objects:** If a field is not serializable, you can mark it as `transient` to avoid `NotSerializableException`.

## **Example**

```
import java.io.*;

class User implements Serializable {
    String username;
    transient String password; // will NOT be serialized
    User(String username, String password) {
        this.username = username;
        this.password = password;
    }
}
```

If you serialize this `User` object, only `username` will be stored; `password` will be ignored.

**When an object is deserialized:**

- The `transient` field is restored to its default value (e.g., `null` for objects, `0` for int, `false` for boolean).

## **11. What is an `Externalizable` Interface?**

The `Externalizable` interface is part of Java’s serialization mechanism. It gives complete control over the serialization process, unlike the `Serializable` interface where the JVM automatically serializes all non-transient fields.

When you implement `Externalizable`, you decide how the object is saved and restored by implementing two methods:

- `writeExternal(ObjectOutput out)`
- `readExternal(ObjectInput in)`

## **Use cases:**

Use it when:

- You want fine-grained control over what data gets serialized.
- You want to improve performance by serializing only the necessary fields.
- You need custom logic for serialization/deserialization.

## **Example:**

```
import java.io.*;
class Employee implements Externalizable {
    private String name;
    private int age;
    private transient double salary; // transient, won't be handled automatically
    // No-arg constructor is mandatory
    public Employee() {
        System.out.println("No-arg constructor called");
    }
    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }
    // Serialization logic
    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(name);
        out.writeInt(age);
        out.writeDouble(salary); // manually serializing even the transient field
    }
    // Deserialization logic
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        name = in.readUTF();
        age = in.readInt();
        salary = in.readDouble(); // manually reading it back
    }
    @Override
    public String toString() {
        return "Employee{name='" + name + "', age=" + age + ", salary=" + salary + "}";
    }
}
```

**12. Write a program to find even numbers from list.**

```jsx
import java.util.Arrays;
import java.util.List;

public class EvenNumbersStream {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(10, 15, 22, 33, 40, 55, 60);

        System.out.println("Even numbers from the list:");
        numbers.stream()
               .filter(num -> num % 2 == 0)
               .forEach(System.out::println);
    }
}
```

## **13. What is the internal working of the filter method?**

The `filter()` method is an intermediate operation in the Java Stream API that returns a new stream consisting of the elements that match a given predicate (condition).

**Example:**

```
list.stream()
    .filter(e -> e % 2 == 0)
    .forEach(System.out::println);
```

## **Internal Working of `filter():`**

**1. Stream is Lazy**

- The `filter()` method doesn’t evaluate anything immediately.
- It only stores the operation and the predicate in an internal pipeline.
- Execution happens only when a terminal operation like `forEach()`, `collect()`, or `count()` is invoked.

**2. Pipeline Formation**

- Streams in Java are processed using a pipeline of operations.
- When `filter()` is called, it creates a new stream that remembers the filtering logic.
- Think of it like building a chain of processing steps.

**3. Spliterator Behind the Scenes**

- Internally, streams use a `Spliterator` (an advanced iterator) to traverse and split the data efficiently—especially for parallel streams.

**4. Predicate Testing**

- When the stream is consumed (e.g., via `forEach`), the filter logic is applied element by element.
- Each element is passed to the predicate function.
- If the result is `true`, the element is passed to the next stage in the pipeline.
- If `false`, it is skipped.

## **Simplified Internal Pseudocode:**

```
for (T element : source) {
    if (predicate.test(element)) {
        downstreamConsumer.accept(element);
    }
}
```

# **Final Thoughts**

This was a pretty basic interview with one or two deeper questions thrown in. Overall, it felt well-suited for someone with around 2–3 years of experience, as it focused primarily basics of the core concepts.

# **Scenario Based Interview Question — 4**

# **Scenario:**

You have a requirement to maintain a history of insertion, modification, and deletion to the “Customer” table. How will you go about accomplishing this?

# **Approach:**

We will accomplish this goal using **event-driven architecture with Kafka and database triggers**.

## **1. Real-Time Tracking Using PostgreSQL Triggers + Kafka**

- A PostgreSQL trigger is set up on the `customer` table to track changes (INSERT, UPDATE, DELETE).
- The trigger publishes changes using the LISTEN/NOTIFY mechanism.
- A Spring Boot listener (`CustomerChangeListener`) continuously listens for these database changes.
- When a change occurs, it is converted into a structured event and published to Apache Kafka via the `KafkaProducerService`.

## **2. Event-Driven Processing Using Kafka (Pub-Sub Model)**

- A Kafka topic (`customer_events`) is used to handle the event stream of customer changes.
- The Kafka producer (`KafkaProducerService`) publishes customer change events.
- A Kafka consumer (`KafkaConsumerService`) listens for new events.
- When an event is received, it is persisted into a MongoDB history collection (`customer_history`).

## **3. Persisting Change History in MongoDB**

- MongoDB (`customer_history` collection) is used to store all historical customer changes.
- Each record stores who changed what, when, and why, ensuring a complete audit trail.
- This allows easy querying for audit logs, tracking, and compliance.

# **Implementation**

Let’s start with the coding portion now:

## **1. Project Structure:**

Your project structure would be:

![](https://d5a5lc4p74x2q0.archive.ph/4hbId/43ddc8e9c0e0528a8c1a85ac4da7cad59b040216.webp)

Plus, the DB files.

## **2. Project Setup**

Update the Maven `pom.xml` with all necessary dependencies:

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>
 <parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.4.4</version>
  <relativePath/>
<!-- lookup parent from com.example.customertracking.repository -->
 </parent>
 <groupId>com.example</groupId>
 <artifactId>customer-tracking</artifactId>
 <version>0.0.1-SNAPSHOT</version>
 <name>customer-tracking</name>
 <description>Customer tracking project</description>
 <url/>
 <licenses>
  <license/>
 </licenses>
 <developers>
  <developer/>
 </developers>
 <scm>
  <connection/>
  <developerConnection/>
  <tag/>
  <url/>
 </scm>
 <properties>
  <java.version>17</java.version>
 </properties>
 <dependencies>
  <!-- Spring Boot Starter -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-web</artifactId>
  </dependency>

  <!-- PostgreSQL Driver -->
  <dependency>
   <groupId>org.postgresql</groupId>
   <artifactId>postgresql</artifactId>
  </dependency>

  <!-- Spring Data JPA -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-data-jpa</artifactId>
  </dependency>

  <!-- Spring Data MongoDB -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-data-mongodb</artifactId>
  </dependency>

  <!-- Apache Kafka Dependencies -->
  <dependency>
   <groupId>org.springframework.kafka</groupId>
   <artifactId>spring-kafka</artifactId>
  </dependency>

  <!-- Lombok (For Reducing Boilerplate Code) -->
  <dependency>
   <groupId>org.projectlombok</groupId>
   <artifactId>lombok</artifactId>
   <scope>provided</scope>
  </dependency>
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-aop</artifactId>
  </dependency>

  <!-- Spring Boot DevTools (For Development) -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-devtools</artifactId>
   <scope>runtime</scope>
   <optional>true</optional>
  </dependency>

  <!-- Spring Boot Actuator (For Monitoring) -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-actuator</artifactId>
  </dependency>

  <!-- Spring Boot Test -->
  <dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-test</artifactId>
   <scope>test</scope>
  </dependency>

  <!-- Spring Kafka Test -->
  <dependency>
   <groupId>org.springframework.kafka</groupId>
   <artifactId>spring-kafka-test</artifactId>
   <scope>test</scope>
  </dependency>
  <dependency>
   <groupId>javax.annotation</groupId>
   <artifactId>javax.annotation-api</artifactId>
   <version>1.2</version>
  </dependency>
 </dependencies>

 <build>
 <plugins>
  <!-- Spring Boot Maven Plugin -->
  <plugin>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-maven-plugin</artifactId>
  </plugin>

  <!-- Compiler Plugin -->
  <plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-compiler-plugin</artifactId>
   <version>3.8.1</version>
   <configuration>
    <source>${java.version}</source>
    <target>${java.version}</target>
   </configuration>
  </plugin>
 </plugins>
 </build>
</project>
```

## **3. Application.properties Configuration**

The updated application.properties file is as below:

```
# ===============================
# Spring Boot Configurations
# ===============================

# Server Port
server.port=8080

# ===============================
# Database Configuration (PostgreSQL)
# ===============================
spring.datasource.url=jdbc:postgresql://localhost:5433/springbootrest
spring.datasource.username=springuser
spring.datasource.password=password
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# ===============================
# MongoDB Configuration (For History Tracking)
# ===============================
spring.data.mongodb.uri=mongodb://localhost:27017/customer_history
spring.data.mongodb.database=customer_history

# ===============================
# Kafka Configuration
# ===============================

# Kafka Bootstrap Server (Change if using a remote broker)
spring.kafka.bootstrap-servers=localhost:9092

# Producer Configuration
spring.kafka.producer.key-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.producer.value-serializer=org.apache.kafka.common.serialization.StringSerializer

# Consumer Configuration
spring.kafka.consumer.group-id=customer-history-group
spring.kafka.consumer.auto-offset-reset=earliest
spring.kafka.consumer.key-deserializer=org.apache.kafka.common.serialization.StringDeserializer
spring.kafka.consumer.value-deserializer=org.apache.kafka.common.serialization.StringDeserializer

# Enable Scheduling (needed for @Scheduled annotation)
spring.task.scheduling.enabled=true
```

**4. Main Application file : CustomerTrackingApplication.java**

```jsx
package com.example.customertracking;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CustomerTrackingApplication {

 private static final Logger logger = LoggerFactory.getLogger(CustomerTrackingApplication.class);

 public static void main(String[] args) {
  SpringApplication.run(CustomerTrackingApplication.class, args);
  logger.info("Customer History Service is running...");
 }
}
```

## **5. Controller Package**

**CustomerController.java file:**

```
package com.example.customertracking.controller;

import com.example.customertracking.model.Customer;
import com.example.customertracking.service.CustomerService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping("/customers")
@RequiredArgsConstructor
public class CustomerController {
    private final CustomerService customerService;

    @PostMapping
    public ResponseEntity<Customer> createCustomer(@RequestBody Customer customer) {
        Customer savedCustomer = customerService.saveCustomer(customer);
        return ResponseEntity
                .created(URI.create("/customers/" + savedCustomer.getId()))
                .body(savedCustomer);
    }

    @GetMapping
    public ResponseEntity<List<Customer>> getAllCustomers() {
        List<Customer> customers = customerService.getAllCustomers();
        return customers.isEmpty() ? ResponseEntity.noContent().build() : ResponseEntity.ok(customers);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCustomer(@PathVariable Long id) {
        if (!customerService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        customerService.deleteCustomer(id);
        return ResponseEntity.noContent().build();
    }

    @PutMapping("/{id}")
    public ResponseEntity<Customer> updateCustomer(@PathVariable Long id, @RequestBody Customer customer) {
        if (!customerService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }

        Customer updatedCustomer = customerService.updateCustomer(id, customer);
        return ResponseEntity.ok(updatedCustomer);
    }
}
```

## **6. Service Package**

**CustomerService.java file:**

```
package com.example.customertracking.service;

import com.example.customertracking.kafka.KafkaProducerService;
import com.example.customertracking.model.Customer;
import com.example.customertracking.model.CustomerHistory;
import com.example.customertracking.repository.CustomerRepository;
import lombok.RequiredArgsConstructor;
import org.apache.kafka.common.errors.ResourceNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class CustomerService {
    private final CustomerRepository customerRepository;
    private final KafkaProducerService kafkaProducerService;

    @Transactional
    public Customer saveCustomer(Customer customer) {
        return customerRepository.save(customer);
    }

    public List<Customer> getAllCustomers() {
        return customerRepository.findAll();
    }

    public boolean existsById(Long id) {
        return customerRepository.existsById(id);
    }

    @Transactional
    public void deleteCustomer(Long id) {
        Optional<Customer> customerOpt = customerRepository.findById(id);
        if (customerOpt.isPresent()) {
            customerRepository.deleteById(id);
        }
    }

    public Customer updateCustomer(Long id, Customer customer) {
        Customer existingCustomer = customerRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id " + id));

        // Update the existing customer fields
        existingCustomer.setName(customer.getName());
        existingCustomer.setEmail(customer.getEmail());
        existingCustomer.setPhone(customer.getPhone());

        // Save and return the updated customer
        return customerRepository.save(existingCustomer);
    }
}
```

## **7. DB Trigger**

Now for the DB part, follow the below steps:

**1. Create the `customer_history` Table:**

Since PostgreSQL does not keep track of old values, we need a **history table** to store changes.

```
CREATE TABLE customer_history (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    action_type VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**2. Create the Trigger:**

Attach the function to the `customer` table so that it **automatically executes on every change**.

```
CREATE TRIGGER customer_changes_trigger
AFTER INSERT OR UPDATE OR DELETE ON customer
FOR EACH ROW EXECUTE FUNCTION track_customer_changes();
```

**3. Create the Trigger Function:**

This function **captures every change** in the `customer` table and logs it in `customer_history`.

```
CREATE OR REPLACE FUNCTION track_customer_changes()
RETURNS TRIGGER AS $$
BEGIN
    -- Track INSERT operation
    IF TG_OP = 'INSERT' THEN
        INSERT INTO customer_history (customer_id, name, email, phone, action_type)
        VALUES (NEW.id, NEW.name, NEW.email, NEW.phone, 'INSERT');

    -- Track UPDATE operation
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO customer_history (customer_id, name, email, phone, action_type)
        VALUES (NEW.id, NEW.name, NEW.email, NEW.phone, 'UPDATE');

    -- Track DELETE operation
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO customer_history (customer_id, name, email, phone, action_type)
        VALUES (OLD.id, OLD.name, OLD.email, OLD.phone, 'DELETE');
    END IF;

    -- Publish event to Kafka (Using PostgreSQL's NOTIFY for external handling)
    PERFORM pg_notify('customer_changes', json_build_object(
        'customerId', COALESCE(NEW.id, OLD.id),
        'name', COALESCE(NEW.name, OLD.name),
        'email', COALESCE(NEW.email, OLD.email),
        'phone', COALESCE(NEW.phone, OLD.phone),
        'action', TG_OP
    )::text);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

## **8. Listener Package**

**CustomerChangeListner.java file:**

```
package com.example.customertracking.listener;

import com.example.customertracking.kafka.KafkaProducerService;
import com.example.customertracking.model.CustomerHistory;
import lombok.RequiredArgsConstructor;
import org.postgresql.PGNotification;
import org.postgresql.PGConnection;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.time.LocalDateTime;

@Component
@RequiredArgsConstructor
public class CustomerChangeListener {

    @Value("${spring.datasource.url}")
    private String dbUrl;

    @Value("${spring.datasource.username}")
    private String dbUser;

    @Value("${spring.datasource.password}")
    private String dbPassword;

    private final KafkaProducerService kafkaProducerService;
    private Connection conn;
    private PGConnection pgConn;

    @PostConstruct
    public void init() {
        try {
            conn = DriverManager.getConnection(dbUrl, dbUser, dbPassword);
            pgConn = conn.unwrap(PGConnection.class);
            Statement stmt = conn.createStatement();
            stmt.execute("LISTEN customer_changes");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Scheduled(fixedRate = 5000) // Poll every 5 seconds
    public void listenToPostgresTriggers() {
        try {
            PGNotification[] notifications = pgConn.getNotifications();
            if (notifications != null) {
                for (PGNotification notification : notifications) {
                    String payload = notification.getParameter();
                    System.out.println("Received DB Change: " + payload);

                    // Convert payload to CustomerHistory object
                    CustomerHistory history = parsePayload(payload);

                    // Send to Kafka
                    kafkaProducerService.sendCustomerEvent(history);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private CustomerHistory parsePayload(String payload) {
        // Assuming payload is a comma-separated string: "id,name,email,phone,action"
        String[] parts = payload.split(",");

        if (parts.length < 5) {
            throw new IllegalArgumentException("Invalid payload format: " + payload);
        }

        Long customerId = Long.parseLong(parts[0].trim());
        String name = parts[1].trim();
        String email = parts[2].trim();
        String phone = parts[3].trim();
        String action = parts[4].trim();

        return new CustomerHistory(null, customerId, name, email, phone, action, LocalDateTime.now());
    }
}
```

## **9. Kafka Service Package**

**KafkaProducerService.java file:**

```
package com.example.customertracking.kafka;

import com.example.customertracking.model.CustomerHistory;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;

import java.util.concurrent.CompletableFuture;

@Service
@RequiredArgsConstructor
public class KafkaProducerService {
    private static final Logger logger = LoggerFactory.getLogger(KafkaProducerService.class);
    private static final String TOPIC_NAME = "customer_events";

    private final KafkaTemplate<String, CustomerHistory> kafkaTemplate;

    public void sendCustomerEvent(CustomerHistory history) {
        CompletableFuture<SendResult<String, CustomerHistory>> future = kafkaTemplate.send(TOPIC_NAME, history);

        future.whenComplete((result, exception) -> {
            if (exception == null) {
                logger.info("Message sent successfully: {} with offset {}", history, result.getRecordMetadata().offset());
            } else {
                logger.error("Failed to send message: {}", exception.getMessage(), exception);
            }
        });
    }
}
```

**KafkaConsumerService.java file:**

```
package com.example.customertracking.kafka;

import com.example.customertracking.model.CustomerHistory;
import com.example.customertracking.repository.CustomerHistoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
@RequiredArgsConstructor
public class KafkaConsumerService {
    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumerService.class);
    private final CustomerHistoryRepository historyRepository;

    @KafkaListener(topics = "customer_events", groupId = "customer-group", containerFactory = "kafkaListenerContainerFactory")
    public void consume(CustomerHistory history) {
        logger.info("Received customer event: {}", history);

        try {
            historyRepository.save(history);
            logger.info("Customer history saved successfully: {}", history);
        } catch (Exception e) {
            logger.error("Error saving customer history: {}", e.getMessage(), e);
        }
    }
}
```

## **10. Kafka Config Package**

**KafkaConfig.java file:**

```
package com.example.customertracking.config;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class KafkaConfig {

    @Bean
    public NewTopic customerEventsTopic() {
        return new NewTopic("customer_events", 3, (short) 1); // Topic name, number of partitions, replication factor
    }
}
```

**KafkaProducerConfig.java file:**

```
package com.example.customertracking.config;

import com.example.customertracking.model.CustomerHistory;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;
import org.springframework.kafka.support.serializer.JsonSerializer;

import java.util.HashMap;
import java.util.Map;

@Configuration
public class KafkaProducerConfig {

    @Bean
    public ProducerFactory<String, CustomerHistory> producerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");  // Replace with your actual Kafka broker address
        config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);

        // Configure value serializer with error handling, JSON serializer for CustomerHistory
        JsonSerializer<CustomerHistory> jsonSerializer = new JsonSerializer<>();
        jsonSerializer.setAddTypeInfo(true); // This ensures type info is added (optional based on your needs)

        config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, jsonSerializer);

        return new DefaultKafkaProducerFactory<>(config);
    }

    @Bean
    public KafkaTemplate<String, CustomerHistory> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}
```

**KafkaConsumerConfig.java file:**

```
package com.example.customertracking.config;

import com.example.customertracking.model.CustomerHistory;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.core.ConsumerFactory;
import org.springframework.kafka.core.DefaultKafkaConsumerFactory;
import org.springframework.kafka.support.serializer.ErrorHandlingDeserializer;
import org.springframework.kafka.support.serializer.JsonDeserializer;

import java.util.HashMap;
import java.util.Map;

@Configuration
public class KafkaConsumerConfig {

    @Bean
    public ConsumerFactory<String, CustomerHistory> consumerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); // Make sure to replace with the actual broker address in production
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "customer-group");
        config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);

        // Using ErrorHandlingDeserializer for more robust error handling in deserialization
        JsonDeserializer<CustomerHistory> jsonDeserializer = new JsonDeserializer<>(CustomerHistory.class);
        jsonDeserializer.setRemoveTypeHeaders(false); // Keeps the type information, useful for advanced scenarios
        jsonDeserializer.addTrustedPackages("*"); // Trust all packages; consider narrowing this in production

        config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ErrorHandlingDeserializer.class);
        config.put(ErrorHandlingDeserializer.VALUE_DESERIALIZER_CLASS, jsonDeserializer);

        return new DefaultKafkaConsumerFactory<>(config, new StringDeserializer(), jsonDeserializer);
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, CustomerHistory> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, CustomerHistory> factory = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(3); // You can adjust concurrency based on your needs (e.g., number of partitions)
        return factory;
    }
}
```

## **11. Repository Package**

**CustomerRepository.java file:**

```
package com.example.customertracking.repository;

import com.example.customertracking.model.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {
}
```

**CustomerHistoryRepository.java file:**

```
package com.example.customertracking.repository;

import com.example.customertracking.model.CustomerHistory;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface CustomerHistoryRepository extends MongoRepository<CustomerHistory, String> {

}
```

## **12. Model Package**

**Customer.java file:**

```
package com.example.customertracking.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "customers")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    private String phone;
}
```

**CustomerHistory.java file:**

```
package com.example.customertracking.model;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Document(collection = "customer_history")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class CustomerHistory {
    @Id
    private String id;
    private Long customerId;
    private String name;
    private String email;
    private String phone;
    private String action; //INSERT, UPDATE, DELETE
    private LocalDateTime timestamp;
}
```

# **Application Flow**

Here’s the **entire application flow step-by-step** for the Customer History Tracking system, from the initial request to updating the customer and ensuring the data is logged in both PostgreSQL and MongoDB via Kafka.

## **1. Project Initialization**

When you run the application (`mvn spring-boot:run` or `java -jar target/customer-history-service.jar`), Spring Boot starts up and initializes the following:

- **PostgreSQL connection**: Establishes a connection to the PostgreSQL database.
- **MongoDB connection**: Sets up a connection to MongoDB for history storage.
- **Kafka producer and consumer**: Initializes Kafka producers and consumers for real-time message handling.
- **REST API endpoints**: Exposes the API for CRUD operations on customers.

## **2. Customer Operations Flow**

The system handles **Create**, **Update**, and **Delete** operations as follows:

## **A. Insert a New Customer**

**Step 1: User Makes an API Request**

- The user sends a **POST** request to the API to add a new customer:

```
POST /customers
Content-Type: application/json
{
    "name": "Shivam Srivastava",
    "email": "shivam@example.com",
    "phone": "9876543210"
}
```

**Step 2: Spring Boot Controller Handles Request**

- `CustomerController.createCustomer()` receives this request and calls `CustomerService.saveCustomer()`.

**Step 3: Customer Service Saves to PostgreSQL**

- The `saveCustomer()` method saves the new customer to PostgreSQL using `CustomerRepository.save(customer)`.
- PostgreSQL generates a new unique ID for the customer (e.g., `id=1`).

**Step 4: Database Trigger Fires**

- The PostgreSQL trigger `customer_changes_trigger` fires **AFTER INSERT** on the `customer` table.
- The trigger inserts the new record into the `customer_history` table and sends a notification via `pg_notify` with a message about the inserted record.

**Step 5: CustomerChangeListener Listens for Notification**

- The `CustomerChangeListener` listens for PostgreSQL notifications every 5 seconds using a scheduled task (`listenToPostgresTriggers()`).
- When it detects a new notification, it receives the data about the customer and the `INSERT` action.

**Step 6: Parse Payload and Send to Kafka**

- The `CustomerChangeListener` parses the payload (e.g., customer details) and creates a `CustomerHistory` object.
- The `CustomerHistory` object, with `action = "INSERT"`, is then sent to the Kafka producer.

**Step 7: Kafka Consumer Saves History to MongoDB**

- The Kafka consumer (`KafkaConsumerService`) listens for incoming messages from Kafka.
- It processes the message and stores the customer history in MongoDB with the timestamp and action type (`INSERT`).

## **B. Update an Existing Customer**

**Step 1: User Updates Customer via API**

- The user sends a **PUT** request to update a customer’s information:

```
PUT /customers/1
Content-Type: application/json
{
    "name": "Shivam S",
    "email": "shivam.s@example.com",
    "phone": "9876543210"
}
```

**Step 2: Controller Calls CustomerService.saveCustomer()**

- The `CustomerController.updateCustomer()` method calls `CustomerService.saveCustomer()`.
- The existing customer with `id=1` is fetched, and the new details are updated in PostgreSQL.

**Step 3: PostgreSQL Trigger Detects UPDATE**

- The PostgreSQL trigger `customer_changes_trigger` fires **AFTER UPDATE** when the customer data changes.
- The trigger inserts a new record into the `customer_history` table with the `UPDATE` action type.

**Step 4: CustomerChangeListener Listens for Notification**

- The `CustomerChangeListener` receives a notification about the `UPDATE` action with the new customer details.

**Step 5: Parse Payload and Send to Kafka**

- The `CustomerChangeListener` parses the payload (e.g., updated customer details) and creates a `CustomerHistory` object with `action = "UPDATE"`.
- It sends this object to the Kafka producer.

**Step 6: Kafka Consumer Saves Update to MongoDB**

- The Kafka consumer listens to the Kafka topic, processes the update event, and stores the updated customer information in MongoDB.
- Both the original and updated customer records are stored in MongoDB for full history tracking.

## **C. Delete a Customer**

**Step 1: User Deletes Customer via API**

- The user sends a **DELETE** request to remove a customer:

```
DELETE /customers/1
```

**Step 2: PostgreSQL Removes Customer**

- The `CustomerController.deleteCustomer()` method calls `CustomerRepository.deleteById(1)` to delete the customer from PostgreSQL.

**Step 3: PostgreSQL Trigger Detects DELETE**

- The PostgreSQL trigger `customer_changes_trigger` fires **AFTER DELETE** and inserts a `DELETE` record into the `customer_history` table.
- The `pg_notify` sends a notification with the `DELETE` action.

**Step 4: CustomerChangeListener Listens for Notification**

- The `CustomerChangeListener` receives the notification for the `DELETE` action.

**Step 5: Parse Payload and Send to Kafka**

- The `CustomerChangeListener` parses the payload and creates a `CustomerHistory` object with `action = "DELETE"`.
- This object is sent to Kafka.

**Step 6: Kafka Consumer Saves Deletion to MongoDB**

- The Kafka consumer processes the deletion event and stores it in MongoDB.
- MongoDB now keeps a history of customer deletions, ensuring full historical tracking.

## **3. MongoDB Storage**

MongoDB stores all changes (insert, update, delete) in the `customer_history` collection.

**Example MongoDB records**:

```
[
  {
    "_id": "66432ac1ef98",
    "customerId": 1,
    "name": "Shivam Srivastava",
    "email": "shivam@example.com",
    "phone": "9876543210",
    "action": "INSERT",
    "timestamp": "2025-03-30T12:41:10"
  },
  {
    "_id": "66432ac1ef99",
    "customerId": 1,
    "name": "Shivam S",
    "email": "shivam.s@example.com",
    "phone": "9876543210",
    "action": "UPDATE",
    "timestamp": "2025-03-30T12:46:11"
  },
  {
    "_id": "66432ac1efa0",
    "customerId": 1,
    "name": "Shivam S",
    "email": "shivam.s@example.com",
    "phone": "9876543210",
    "action": "DELETE",
    "timestamp": "2025-03-30T12:48:31"
  }
]
```

# **Testing the Application**

To test the flow, follow these steps:

1. **Start the application** using `mvn spring-boot:run` or `java -jar`.
2. **Test CRUD operations** via Postman or any API client
- **Create a new customer** using `POST /customers`.
- **Update a customer** using `PUT /customers/{id}`.
- **Delete a customer** using `DELETE /customers/{id}`.

**3. Verify PostgreSQL**:

- Check the `customer_history` table for logs of changes.

**4. Verify MongoDB**:

- Check the `customer_history` collection for the history of changes.

**5. Check Kafka**:

- Use Kafka’s monitoring tools to verify that messages are being sent and received correctly.

# **Final Thoughts:**

This article took the longest amount of time to write compared to all the articles I’ve written so far, mainly due to the setup of MongoDB and Kafka. It was my first time working with MongoDB, and I’m still relatively new to Kafka as well.

The code is up and running smoothly on my local machine.

# **JP Morgan Java Developer Interview — 2**

**1. Write a program to remove empty strings from an array of Strings.**

```jsx
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class RemoveEmptyAndNullStrings {
    public static void main(String[] args) {
        String[] arr = {"Hello", "", "World", null, "Java", "", "Streams", null};
        // Remove empty and null strings using Java 8 Streams
        List<String> filteredList = Arrays.stream(arr)
                                          .filter(str -> str != null && !str.isEmpty()) // Exclude nulls and empty strings
                                          .collect(Collectors.toList());
        System.out.println(filteredList);
    }
}
```

**Output:**

`[Hello, World, Java, Streams]`

## **2. Explain CyclicBarrier and CountDownLatch.**

`CyclicBarrier` and `CountDownLatch` are synchronization aids in Java's `java.util.concurrent` package, but they serve different purposes.

## **️1. CyclicBarrier**

`CyclicBarrier` is a synchronization mechanism that allows multiple threads to wait at a common point until a predefined number of threads reach that point.

**Features**:

- **Reusable** → Once the required number of threads reach the barrier, it resets automatically.
- **Optional Runnable Task** → You can execute a task once all threads reach the barrier.
- **Waits for a Specific Number of Threads** → Unlike `CountDownLatch`, which counts down, `CyclicBarrier` waits for a fixed number of threads.

**Example**:

```
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class CyclicBarrierExample {
    public static void main(String[] args) {
        int numThreads = 3;
        CyclicBarrier barrier = new CyclicBarrier(numThreads, () -> System.out.println("All threads reached the barrier!"));
        for (int i = 0; i < numThreads; i++) {
            new Thread(new Worker(barrier)).start();
        }
    }
    static class Worker implements Runnable {
        private final CyclicBarrier barrier;
        Worker(CyclicBarrier barrier) {
            this.barrier = barrier;
        }
        @Override
        public void run() {
            System.out.println(Thread.currentThread().getName() + " is working...");
            try {
                Thread.sleep(1000); // Simulating work
                System.out.println(Thread.currentThread().getName() + " reached the barrier");
                barrier.await(); // Wait at the barrier
                System.out.println(Thread.currentThread().getName() + " passed the barrier!");
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
        }
    }
}
```

**Output**:

```
Thread-0 is working...
Thread-1 is working...
Thread-2 is working...
Thread-0 reached the barrier
Thread-1 reached the barrier
Thread-2 reached the barrier
All threads reached the barrier!
Thread-0 passed the barrier!
Thread-1 passed the barrier!
Thread-2 passed the barrier!
```

**Use case:**

- When you need multiple threads to start executing together after reaching a common point.
- When the same barrier needs to be reused multiple times (e.g., in iterative tasks like simulations).

## **2. CountDownLatch**

`CountDownLatch` is a synchronization mechanism that blocks threads until the count reaches zero.

**Features:**

- **One-Time Use** → Unlike `CyclicBarrier`, it cannot be reused.
- **CountDown Mechanism** → The count starts from a given number and decreases each time `countDown()` is called.
- **Waiting Thread Unblocks When Count Reaches Zero** → Threads calling `await()` will wait until the count hits zero.

**Example**:

```
import java.util.concurrent.CountDownLatch;

public class CountDownLatchExample {
    public static void main(String[] args) {
        int numWorkers = 3;
        CountDownLatch latch = new CountDownLatch(numWorkers);
        for (int i = 0; i < numWorkers; i++) {
            new Thread(new Worker(latch)).start();
        }
        try {
            latch.await(); // Wait for all workers to finish
            System.out.println("All workers finished. Main thread proceeds.");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    static class Worker implements Runnable {
        private final CountDownLatch latch;
        Worker(CountDownLatch latch) {
            this.latch = latch;
        }
        @Override
        public void run() {
            System.out.println(Thread.currentThread().getName() + " is working...");
            try {
                Thread.sleep(1000); // Simulating work
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + " finished work.");
            latch.countDown(); // Decrease the latch count
        }
    }
}
```

**Output**:

```
Thread-0 is working...
Thread-1 is working...
Thread-2 is working...
Thread-0 finished work.
Thread-1 finished work.
Thread-2 finished work.
All workers finished. Main thread proceeds.
```

**Use case:**

- When a thread (e.g., main thread) needs to wait for other threads to finish before continuing.
- One-time synchronization, such as ensuring a service is fully initialized before proceeding.

## **Differences:**

![](https://d57vksw1yqkm6c.archive.ph/Ybzb5/711caac80ca124086a1a548bf4c2b51f66e2dfc8.webp)

## **3. What is CompletableFuture?**

`CompletableFuture` is a powerful feature introduced in Java 8 (`java.util.concurrent`) that represents a future result of an asynchronous computation.

It provides a flexible way to write non-blocking, asynchronous code using functional programming constructs.

## **Features**

- **Asynchronous Execution** → Tasks run independently without blocking the main thread.
- **Chaining** → Supports method chaining with `.thenApply()`, `.thenAccept()`, etc.
- **Composing Futures** → Combines multiple `CompletableFuture` instances using `.thenCompose()`, `.thenCombine()`.
- **Exception Handling** → Provides built-in error handling via `.exceptionally()` and `.handle()`.
- **Parallel Execution** → Supports executing multiple tasks in parallel using `.allOf()` and `.anyOf()`.

## **Example of CompletableFuture**

```
import java.util.concurrent.CompletableFuture;

public class CompletableFutureExample {
    public static void main(String[] args) {
        CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
            try { Thread.sleep(1000); } catch (InterruptedException e) { e.printStackTrace(); }
            return "Hello, World!";
        });
        future.thenAccept(result -> System.out.println("Result: " + result));
        // Keep the main thread alive to see async output (only needed in standalone Java applications)
        try { Thread.sleep(1500); } catch (InterruptedException e) { e.printStackTrace(); }
    }
}
```

**Output**:

```
Result: Hello, World!
```

- The `supplyAsync()` method runs the task asynchronously.
- The `.thenAccept()` method is called when the computation completes.

## **CompletableFuture Chaining**

`CompletableFuture` allows chaining multiple tasks sequentially using `.thenApply()` and `.thenCompose()`.

**Example**:

```
import java.util.concurrent.CompletableFuture;

public class CompletableFutureChaining {
    public static void main(String[] args) {
        CompletableFuture.supplyAsync(() -> "Java")
            .thenApply(str -> str + " Future")  // Transforms result
            .thenApply(String::toUpperCase)    // Converts to uppercase
            .thenAccept(System.out::println);  // Consumes result
    }
}
```

**Output**:

```
JAVA FUTURE
```

- **`thenApply()`** modifies the result.
- **`thenAccept()`** consumes the result without returning anything.

## **Combining Multiple CompletableFutures:**

You can execute multiple `CompletableFuture` tasks in **parallel** and combine their results.

**Example**:

```
import java.util.concurrent.CompletableFuture;

public class CompletableFutureCombine {
    public static void main(String[] args) {
        CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> "Hello");
        CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> "World");
        future1.thenCombine(future2, (res1, res2) -> res1 + " " + res2)
               .thenAccept(System.out::println);
    }
}
```

**Output**:

```
Hello World
```

- **`thenCombine()`** combines results from two futures when both complete.

## **Exceptions Handling**

To handle exceptions, use `.exceptionally()` or `.handle()`.

**Example**:

```
import java.util.concurrent.CompletableFuture;

public class CompletableFutureException {
    public static void main(String[] args) {
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
            if (Math.random() > 0.5) throw new RuntimeException("Something went wrong!");
            return 42;
        });
        future.exceptionally(ex -> {
            System.out.println("Error: " + ex.getMessage());
            return -1; // Default fallback value
        }).thenAccept(System.out::println);
    }
}
```

- **`exceptionally()`** handles errors and returns a fallback value.

## **Running Multiple Tasks in Parallel:**

If you have multiple independent tasks, you can use `.allOf()` and `.anyOf()`.

**Example**

```
import java.util.concurrent.CompletableFuture;

public class CompletableFutureAllOf {
    public static void main(String[] args) {
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            CompletableFuture.runAsync(() -> System.out.println("Task 1")),
            CompletableFuture.runAsync(() -> System.out.println("Task 2")),
            CompletableFuture.runAsync(() -> System.out.println("Task 3"))
        );
        allFutures.join(); // Waits for all tasks to complete
        System.out.println("All tasks finished!");
    }
}
```

- **`allOf()`** waits for all tasks to complete before proceeding.

## **CompletableFuture vs Future:**

![](https://d57vksw1yqkm6c.archive.ph/Ybzb5/e400acbda5ddef9825a1750de757238d856d4a38.webp)

## **Use Case:**

- When you need asynchronous or parallel execution.
- When you need chained transformations.
- When you need error handling without try-catch blocks.
- When combining results from multiple parallel tasks.

## **4. Write a program to reverse an integer array without any inbuilt functions.**

```
public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        reverseArray(arr);  // Call the function to reverse the array

        // Print the reversed array
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

public static void reverseArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            // Swap arr[left] and arr[right]
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            // Move pointers
            left++;
            right--;
        }
    }
}
```

**Output**:

```
5 4 3 2 1
```

**Time Complexity:** `O(N)` (linear, since we swap `N/2` times).**Space Complexity:** `O(1)` (no extra space used).

## **5. What will happen if we insert the same key in the hashmap?**

If you insert the same key into a `HashMap` in Java, it will overwrite the existing value associated with that key.

## **Internal Working:**

1. The `HashMap` calculates the hash code of the key.
2. It finds the bucket (index in the array) where the key-value pair should be stored.
3. If the key already exists, the new value replaces the old value.
4. The `put(K key, V value)` method returns the previous value associated with that key (or `null` if it was not present).

## **Example:**

```
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        // Insert key-value pairs
        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(1, "Cherry"); // Overwrites "Apple"
        System.out.println(map);
    }
}
```

**Output**:

```
{1=Cherry, 2=Banana}
```

- `1="Apple"` was replaced by `1="Cherry"`.

## **6. What is a WeakHashmap?**

A `WeakHashMap` in Java is a special type of `Map` where the keys are stored as weak references.

This means that if a key is no longer strongly referenced elsewhere, the garbage collector (GC) can automatically remove that entry from the map when GC runs.

## **Example:**

```
import java.util.WeakHashMap;

public class WeakHashMapExample {

    public static void main(String[] args) {

        WeakHashMap<Object, String> weakMap = new WeakHashMap<>();
        Object key1 = new Object();  // Strong reference
        Object key2 = new Object();
        weakMap.put(key1, "Value1");
        weakMap.put(key2, "Value2");

        System.out.println("Before GC: " + weakMap);
        key2 = null;  // Remove strong reference to key2
        System.gc();   // Suggest GC to run (not guaranteed)

        // Allow time for GC to possibly run
        try { Thread.sleep(1000); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("After GC: " + weakMap);
    }
}
```

**Expected Output (May Vary)**

```
Before GC: {java.lang.Object@6bc7c054=Value1, java.lang.Object@232204a1=Value2}
After GC: {java.lang.Object@6bc7c054=Value1}
```

- `key2` is removed automatically because it is no longer strongly referenced.
- `key1` remains because we still have a strong reference to it.

**Takeaway:**

- Garbage collection is not instant — it happens when the JVM decides.
- Calling `System.gc();` only suggests GC to run but does not force it.

## **Internal Working**

`WeakHashMap` uses WeakReferences to store keys. When the GC determines that a key has no strong references, it marks the entry for removal.

This happens via an internal ReferenceQueue, which helps track garbage-collected keys.

**Example**:

```
import java.lang.ref.WeakReference;
public class WeakReferenceExample {
    public static void main(String[] args) {
        Object obj = new Object();
        WeakReference<Object> weakRef = new WeakReference<>(obj);
        System.out.println("Before GC: " + weakRef.get()); // Object exists
        obj = null;  // Remove strong reference
        System.gc(); // Suggest GC
        try { Thread.sleep(1000); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("After GC: " + weakRef.get()); // Likely null
    }
}
```

- `weakRef.get()` returns the object only if it has not been garbage-collected.
- Once GC runs, `weakRef.get()` returns `null`, indicating that the object has been collected.

## **Use Cases**

- **Caching** → When values should be removed when keys are no longer needed.
- **Avoiding Memory Leaks** → Automatically removes unused keys, preventing memory bloat.
- **Reference-sensitive Data Structures** → When objects should be automatically cleaned up.

## **Differences Between `HashMap` and `WeakHashMap`**

![](https://d57vksw1yqkm6c.archive.ph/Ybzb5/224f2e5d6b6de9a19485ca17c9c9e50cd6c205c8.webp)

## **7. What is an IdentityHashMap?**

An IdentityHashMap is a specialized implementation of `Map` that compares keys using reference equality (`==`) instead of object equality (`equals()`).

This means that two keys are considered equal only if they are the same object in memory (i.e., they have the same reference), even if `equals()` returns `true` for them.

## **Differences Between `HashMap` and `IdentityHashMap`**

![](https://d57vksw1yqkm6c.archive.ph/Ybzb5/6124d5f27d3be70254a3a4c7a20db31bf29d8e6c.webp)

- In `HashMap`, two different objects with the same `equals()` result are treated as the same key.
- In `IdentityHashMap`, they are considered different keys unless they point to the same memory reference.

## **Example:**

```
import java.util.IdentityHashMap;
import java.util.Map;

public class IdentityHashMapExample {

   public static void main(String[] args) {

        Map<String, String> hashMap = new java.util.HashMap<>();
        Map<String, String> identityMap = new IdentityHashMap<>();

        String key1 = new String("Java");  // New object
        String key2 = new String("Java");  // Another new object with same value

        hashMap.put(key1, "HashMap Value");
        hashMap.put(key2, "HashMap New Value");  // Overwrites key1 since equals() is used

        identityMap.put(key1, "IdentityMap Value");
        identityMap.put(key2, "IdentityMap New Value");  // Treated as a new entry since == is used

        System.out.println("HashMap: " + hashMap);
        System.out.println("IdentityHashMap: " + identityMap);
    }
}
```

## **Expected Output**

```
HashMap: {Java=HashMap New Value}
IdentityHashMap: {Java=IdentityMap Value, Java=IdentityMap New Value}
```

- In `HashMap`, both `key1` and `key2` are treated as equal (`.equals()` returns `true`), so the second insertion overwrites the first.
- In `IdentityHashMap`, `key1` and `key2` are different object references, so they are treated as separate entries.

## **Use Cases:**

- **Reference-sensitive Caching** → When keys should be treated as different objects even if they are logically equal.
- **Serialization Mechanisms** → When tracking actual object references rather than values.
- **Performance Optimization** → In scenarios where `.equals()` checks are expensive.

## **8. Write a program to find out the middle element of the linkedlist.**

The below program uses the **slow and fast pointer technique** (also known as Floyd’s Tortoise and Hare algorithm), which efficiently finds the middle node in **O(n)** time with **O(1)** space.

```
class Node {
    int data;
    Node next;

Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedListMiddle {
    Node head;
    // Method to add elements to the linked list
    public void add(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = new Node(data);
    }

   // Method to find the middle element
    public int findMiddle() {
        if (head == null) {
            throw new IllegalStateException("LinkedList is empty");
        }
        Node slow = head;
        Node fast = head;

        // Move 'fast' two steps and 'slow' one step at a time
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.data; // 'slow' now points to the middle node
    }

    public static void main(String[] args) {
        LinkedListMiddle list = new LinkedListMiddle();
        list.add(1);
        list.add(5);
        list.add(3);
        list.add(7);
        list.add(1);
        System.out.println("Middle Element: " + list.findMiddle());
        // Output: 3
    }
}
```

## **Explanation**

1. **Two Pointer Technique**
- `slow` moves one step at a time.
- `fast` moves two steps at a time.
- When `fast` reaches the end, `slow` is at the middle.

**2. Time Complexity:** **O(n)** (Single traversal)

**3. Space Complexity:** **O(1)** (Only pointers are used)

## **9. What are rules for Instance variable?**

Instance variables in Java are non-static fields that belong to an object (instance of a class). They are declared inside a class but outside any method, constructor, or block.

## **1.Rules for Declaring Instance Variables**

1. **Declared inside a class but outside methods**

```
class Example {
      int x;  // ✅ Valid instance variable
}
```

- You cannot declare an instance variable inside a method.

```
class Example {
     void method() {
         int y;  // ❌ This is a local variable, not an instance variable
  }
}
```

**2. Can have access modifiers** (`public`, `private`, `protected`, or default)

```
class Example {
     private int age;  // ✅ Allowed
}
```

**3. Can have any data type** (primitive or reference type)

```
class Example {
    int num;        // ✅ Primitive type
    String name;    // ✅ Reference type
}
```

**4. Can declare a variable as `static`, but then it stops being an instance variable and becomes a class variable.**

```
class Example {
     static int count;  // ✅ This is a class variable, NOT an instance variable
}
```

## **2. Rules for Initialization & Default Values**

1. **Instance variables are initialized automatically with default values**

```
class Example {
     int x;          // Default value: 0
     boolean flag;   // Default value: false
     String name;    // Default value: null
}
```

**2. You can initialize instance variables explicitly**

```
class Example {     int x = 10;  // ✅ Allowed }
```

**3. Instance variables are initialized when an object is created**

```
class Example {
     int x;
     Example() {
         x = 20;  // ✅ Allowed inside constructor
  }
}
```

## **3. Rules for Access & Scope**

1. **Each object gets its own copy** of instance variables

```
class Example {
     int x = 5;
}

public class Main {
     public static void main(String[] args) {
         Example obj1 = new Example();
         Example obj2 = new Example();
          obj1.x = 10;  // Only affects obj1
         System.out.println(obj2.x); // Output: 5
    }
}
```

**2. Instance variables exist as long as the object exists**

- They are stored in the heap memory and are garbage collected when the object is destroyed.

**3. Can be accessed using `this` keyword**

```
class Example {
     int x;

    Example(int x) {
         this.x = x;  // Refers to the instance variable
   }
}
```

## **4. Restrictions on Instance Variables**

1. Can declare a variable as `static`, but it won’t be an instance variable anymore—it will be a class variable.
2. Cannot be declared inside a method (use local variables instead).
3. Cannot be accessed from a static context without an instance.

```
class Example {
     int x = 10;

     static void display()
     {
         System.out.println(x);  // ❌ Compilation error (needs an instance)
     }
}
```

## **10. In the main method, if we declare a variable and not initialize it. What will it print?**

In Java, local variables (including those declared inside the `main` method) do not get default values and must be explicitly initialized before use.

If you declare a variable in the `main` method and try to print it without initializing it, you will get a compilation error.

## **Example:**

```
public class Main {
    public static void main(String[] args) {
        int x;  // Declared but not initialized
        System.out.println(x);  // ❌ Compilation Error: variable x might not have been initialized
    }
}
```

## **Compilation Error Reason:**

- Local variables (inside a method) are not automatically initialized.
- Unlike instance variables (which get default values like `0`, `false`, or `null`), local variables must be explicitly assigned a value before use.

## **11. Predict the Output**

```
import java.util.ArrayList;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        List<Short> A = new ArrayList<>();

        for (short i = 0; i < 100; i++) {
            A.add(i);  // Add current value to the list

            if (A.size() > 1) {  // Ensure more than 1 element exists before removing
                A.remove(A.size() - 1);  // Remove the last (most recently added) element
            }
        }

        System.out.println(A);  // Print the list after the loop completes
    }
}
```

## **Step-by-Step Execution:**

1. **List Initialization:**
- `A` is an empty `ArrayList<Short>`.

**2. Loop Execution (`i = 0 to 99`):**

**a) Iteration 1 (`i = 0`):**

- `A.add(0) → A = [0]`
- The list size is `1`, so the `if` condition is not executed.

**b) Iteration 2 (`i = 1`):**

- `A.add(1) → A = [0, 1]`
- The list size is now `2`, so `A.remove(1)` removes the last element → `A = [0]`.

**c) Iteration 3 (`i = 2`):**

- `A.add(2) → A = [0, 2]`
- The list size is now `2`, so `A.remove(1)` removes the last element → `A = [0]`.

**d) Iteration 4 (`i = 3`):**

- `A.add(3) → A = [0, 3]`
- The list size is now `2`, so `A.remove(1)` removes the last element → `A = [0]`.

**This pattern repeats for all iterations up to `i = 99`**.

- Every iteration adds an element (`A.add(i)`) and then immediately removes it (`A.remove(A.size() - 1)`).
- The list always remains `[0]` throughout the loop.

## **Output:**

After the loop completes, the list still contains **only one element `[0]`**.

```
[0]
```

**12. Suppose you have 2 tables Department and Employees. Now, write a query to find the number of employees working in each department.**

```jsx
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM Department d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

# **UBS Java Developer Interview**

## **1. How to create a spring boot project from scratch?**

I have already written a detailed article on the same. I would recommend you to go through this:

[**Create a Spring Boot Rest API Project From ScratchFor Beginners**medium.com](https://archive.ph/o/0GR7C/https://medium.com/coding-odyssey/create-a-spring-boot-rest-api-project-from-scratch-937737b490f7)

## **2. What is the security used in current your project?**

We use **OAuth 2.0 with JWT** for authentication and authorization.

The authentication is handled by an Identity Provider (IdP), and once a user is authenticated, they receive an access token (JWT), which is used to access protected resources.

We have implemented Spring Security along with the OAuth2 Resource Server to validate JWTs. The system is stateless, and we use role-based access control (RBAC) to manage permissions.

## **Authentication & Authorization Flow:**

1. The client authenticates with the Identity Provider (e.g., Keycloak, Okta, Azure AD).
2. Upon successful authentication, the IdP issues a JWT access token and a refresh token.
3. The client includes the JWT in the Authorization header of API requests:

```
Authorization: Bearer <access_token>
```

4. The backend validates the JWT and allows or denies access based on roles and claims.

## **Spring Security Configuration (JWT Validation)**

We use `spring-boot-starter-oauth2-resource-server` for token validation.

## **1. Dependencies (Maven)**

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

## **2. Configuring JWT Validation (`application.yml`)**

```
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://your-idp.com
```

Here, the `issuer-uri` is the endpoint from our IdP, which provides the public key for verifying JWT signatures.

## **Role-Based Authorization**

We use **method-level security** to restrict access based on roles.

## **3. Enabling Method Security (`@PreAuthorize`)**

```
@RestController
@RequestMapping("/api")
public class SecureController {

@GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<String> getAdminData() {
        return ResponseEntity.ok("This is Admin Data");
    }
    @GetMapping("/user")
    @PreAuthorize("hasRole('USER')")
    public ResponseEntity<String> getUserData() {
        return ResponseEntity.ok("This is User Data");
    }
}
```

- Only users with the `ADMIN` role can access `/admin`.
- Users with the `USER` role can access `/user`.

## **4. JWT Structure Example (Decoded)**

The JWT contains user claims, including roles:

```
{
  "sub": "user123",
  "roles": ["ROLE_ADMIN"],
  "exp": 1713952400
}
```

The backend extracts and validates these roles before granting access.

## **5. Token Expiry & Refresh Mechanism**

- The access token is valid for 15–30 minutes.
- The refresh token is stored securely and used to get a new access token without requiring re-authentication.

## **6. Why OAuth2 + JWT?**

- Stateless authentication (no session storage required)
- Scalable (ideal for microservices)
- Secure (signed and encrypted tokens prevent tampering)
- Interoperability (works with third-party IdPs like Google, Okta, Keycloak)

## **7. How is JWT Validated in Spring Boot?**

Spring Security automatically validates the JWT signature and extracts claims. However, if needed, we can manually extract claims like this:

```
import org.springframework.security.oauth2.jwt.Jwt;
import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationToken;

@RestController
public class JwtController {
    @GetMapping("/token-details")
    public Map<String, Object> getTokenDetails(JwtAuthenticationToken token) {
        Jwt jwt = token.getToken();
        return jwt.getClaims(); // Returns all claims in the JWT
    }
}
```

## **3. How do the requests flow from the controller in OAuth2 + JWT Authentication?**

When a request is made to a secured endpoint in the Spring Boot application, the flow follows these steps:

## **1. Client Sends a Request with JWT**

- The client (frontend or another microservice) includes the JWT access token in the request’s `Authorization` header.
- Example request:

```
GET /api/admin Host: your-api.com Authorization: Bearer <access_token>
```

## **2. Spring Security Filters the Request**

- Spring Security has a built-in OAuth2 Resource Server that automatically intercepts requests.
- The `BearerTokenAuthenticationFilter` extracts the JWT from the `Authorization` header.

## **3. Token Validation**

- Spring Security decodes and verifies the JWT signature using the Identity Provider’s public key (local validation).
- If introspection is enabled, Spring Security sends the token to the IdP for validation (remote validation).
- If using local validation, Spring Security decodes the token and verifies the signature using the public key from the IdP.
- The token is parsed to extract claims like `roles`, `username`, and `expiry`.

## **4. Authorization Decision**

- Once validated, Spring Security applies role-based access control (RBAC).
- If the request is for a role-protected endpoint, Spring Security checks the `@PreAuthorize` annotation.
- By default, Spring Security expects roles to be prefixed with `ROLE_` (e.g., `ROLE_ADMIN`). If your JWT only contains `ADMIN`, configure Spring Security to interpret roles correctly.

## **5. Request Reaches the Controller**

- If authentication and authorization pass, the request proceeds to the controller method.
- Example:

```
@GetMapping("/admin")
@PreAuthorize("hasRole('ADMIN')")
public ResponseEntity<String> getAdminData() {
    return ResponseEntity.ok("This is Admin Data");
}
```

- If the user has the required role (`ADMIN`), the method executes.

## **6. Response is Sent Back**

- The controller returns a response (`ResponseEntity`), which is sent back to the client.

## **Error Handling**

If something fails, Spring Security automatically handles errors:

- **401 Unauthorized** → Invalid or expired token.
- **403 Forbidden** → Token is valid, but the user lacks the required role.

## **4. What is the Response if a GET Call Finds No Entity?**

If a GET request does not find any entity, the response should follow RESTful best practices:

## **1. HTTP 404 Not Found (Recommended for Missing Resources)**

- If the requested resource does not exist (e.g., fetching a user by ID that doesn’t exist), return:

```
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "Resource not found",
  "message": "User with ID 123 does not exist"
}
```

The requested entity does not exist, so returning `404 Not Found` is the correct semantic response.

## **2. HTTP 200 OK with an Empty Array (Recommended for Empty Collections)**

- If the endpoint is meant to return a list and no records exist, return `200 OK` with an empty array (`[]`) instead of `204 No Content`.

```
HTTP/1.1 200 OK Content-Type: application/json  []
```

- Returning `200 OK` with an empty array allows clients to handle responses consistently.
- It avoids confusion because `204 No Content` has no body, making it harder for clients to distinguish between "no data" and an actual error.

## **3. HTTP 204 No Content (Alternative, Less Preferred for Lists)**

- `204 No Content` can still be used, but it's less common for empty lists.

```
HTTP/1.1 204 No Content
```

- While valid, it does not provide a response body, making it harder for clients to differentiate between “no data” and a failed request.
- **Better alternative:** Use `200 OK` with an empty list `[]`.

## **Which One to Use:**

- **Use `404 Not Found`** → If the requested single resource does not exist.
- **Use `200 OK` + `[]`** → If the request is for a list, but no records exist.
- **Use `204 No Content` (only if necessary)** → If you want to explicitly indicate no content, but be aware of client-side handling issues.

## **5. How have you implemented the Authorization?**

## **1. Role-Based Access Control (RBAC) in Spring Security**

Spring Security allows authorization based on user roles stored in JWT claims. Roles can be enforced:

- At the method level (`@PreAuthorize`, `@PostAuthorize`)
- At the request level (`SecurityFilterChain`)

## **a) Method-Level Authorization (`@PreAuthorize`)**

You can restrict access at the method level using `@PreAuthorize`:

```
@GetMapping("/admin")
@PreAuthorize("hasAuthority('ROLE_ADMIN')") // FIX: Use 'hasAuthority' to match JWT
public ResponseEntity<String> getAdminData() {
    return ResponseEntity.ok("This is Admin Data");
}
```

## **b) Request-Level Authorization (SecurityFilterChain)**

To enforce role-based authorization at the request level:

```
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/admin/**").hasAuthority("ROLE_ADMIN")   // Admin-only
            .requestMatchers("/user/**").hasAnyAuthority("ROLE_USER", "ROLE_ADMIN") // Users & Admins
            .anyRequest().authenticated()  // All other requests must be authenticated
        )
        .oauth2ResourceServer(OAuth2ResourceServerConfigurer::jwt); // Enable JWT auth
    return http.build();
}
```

## **2. Role Extraction from JWT**

JWT should store roles under `authorities` instead of `roles`, so Spring Security can automatically pick them up.

## **JWT Payload Example**

```
{
  "sub": "user123",
  "authorities": ["ROLE_ADMIN", "ROLE_USER"],
  "exp": 1712345678
}
```

## **3. Role Hierarchy (Optional)**

If an `ADMIN` should inherit `MANAGER` and `USER` permissions, define a role hierarchy:

```
@Bean
RoleHierarchy roleHierarchy() {
    RoleHierarchyImpl hierarchy = new RoleHierarchyImpl();
    hierarchy.setHierarchy("ROLE_ADMIN > ROLE_MANAGER \n ROLE_MANAGER > ROLE_USER");
    return hierarchy;
}
```

This means:

- `ROLE_ADMIN` has all `ROLE_MANAGER` permissions.
- `ROLE_MANAGER` has all `ROLE_USER` permissions.

## **4. Restricting Access Based on Return Values (`@PostAuthorize`)**

To allow users to access only their own data, use `@PostAuthorize`:

```
@GetMapping("/orders/{orderId}")
@PostAuthorize("returnObject.owner == authentication.name")
public Order getOrder(@PathVariable Long orderId) {
    return orderService.getOrderById(orderId);
}
```

Make sure your JWT contains:

```
{
  "sub": "john.doe",
  "authorities": ["ROLE_USER"]
}
```

## **5. Database-Based Authorization (If Roles are Stored in DB)**

If roles are stored in a database, load them dynamically:

```
@Service
public class CustomUserDetailsService implements UserDetailsService {
    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User not found"));
        List<GrantedAuthority> authorities = user.getRoles().stream()
            .map(role -> new SimpleGrantedAuthority(role.getName())) // FIX: Store 'ROLE_ADMIN' directly in DB
            .collect(Collectors.toList());
        return new org.springframework.security.core.userdetails.User(
            user.getUsername(),
            user.getPassword(),
            authorities
        );
    }
}
```

- Ensure the database stores `ROLE_ADMIN` instead of `ADMIN`, so no `"ROLE_"` prefix is needed in Java.

## **6. What are some of the features of Java 8 in brief?**

Java 8 introduced several major features that significantly enhanced the language.

## **1. Lambda Expressions**

- Enables functional-style programming by passing behavior as parameters.
- Example:

```
List<String> names = Arrays.asList("John", "Doe", "Alice");
names.forEach(name -> System.out.println(name)); // Using lambda
```

## **2. Functional Interfaces**

- Introduced `@FunctionalInterface` annotation to define interfaces with a single abstract method (SAM).
- Example:

```
@FunctionalInterface
interface MyFunction {
     int add(int a, int b);
}
```

## **3. Streams API**

- Provides efficient operations on collections using functional programming.
- Example:

```
List<String> names = List.of("Alice", "Bob", "Charlie");
names.stream().filter(name -> name.startsWith("A")).forEach(System.out::println);
```

## **4. Default & Static Methods in Interfaces**

- Allows adding methods to interfaces without breaking existing implementations.
- Example:

```
interface MyInterface {

      default void show() {
         System.out.println("Default method in interface");
  }
}
```

## **5. Optional Class**

- Helps avoid `NullPointerException` by providing a container for possibly absent values.
- Example:

```
Optional<String> name = Optional.ofNullable(null);
System.out.println(name.orElse("Default Name")); // Avoids NPE
```

## **6. java.time API (New Date-Time API)**

- Replaces `java.util.Date` and `Calendar` with a more robust API.
- Example:

```
LocalDate today = LocalDate.now(); System.out.println(today);
```

## **7. Collectors API**

- Provides utilities for collecting stream results into collections or other forms.
- Example:

```
List<String> names = List.of("John", "Jane", "Jack");
List<String> upperNames = names.stream().map(String::toUpperCase).collect(Collectors.toList());
```

## **8. Method References**

- Simplifies lambda expressions by referring to existing methods.
- Example:

```
names.forEach(System.out::println); // Instead of names.forEach(name -> System.out.println(name));
```

## **9. Nashorn JavaScript Engine (Deprecated in Java 11)**

- Allowed executing JavaScript code within Java.
- Example:

```
ScriptEngineManager manager = new ScriptEngineManager();
ScriptEngine engine = manager.getEngineByName("JavaScript");
engine.eval("print('Hello from JavaScript')");
```

## **10. Parallel Streams**

- Provides parallel processing for large datasets.
- Example:

```
names.parallelStream().forEach(System.out::println);
```

## **7. How to get current timestamp in java 8?**

In Java 8, you can get the current timestamp using the `java.time` package, which provides a better alternative to `java.util.Date`.

## **1. Using `Instant.now()` (Best for Timestamps)**

If you need an instantaneous point in time (UTC-based timestamp):

```
import java.time.Instant;

public class TimestampExample {
    public static void main(String[] args) {
        Instant timestamp = Instant.now();
        System.out.println("Current Timestamp: " + timestamp);
    }
}
```

**Output (ISO 8601 format, UTC timezone):**

```
Current Timestamp: 2025-03-22T12:34:56.789Z
```

## **2. Using `LocalDateTime.now()` (Without Timezone)**

If you need the current date and time but without timezone information:

```
import java.time.LocalDateTime;
public class TimestampExample {
    public static void main(String[] args) {
        LocalDateTime dateTime = LocalDateTime.now();
        System.out.println("Current Date-Time: " + dateTime);
    }
}
```

**Output:**

```
Current Date-Time: 2025-03-22T18:05:30.123
```

## **3. Using `ZonedDateTime.now()` (With Timezone)**

If you need the current date-time with a specific timezone:

```
import java.time.ZonedDateTime;
import java.time.ZoneId;

public class TimestampExample {
    public static void main(String[] args) {
        ZonedDateTime zonedDateTime = ZonedDateTime.now(ZoneId.of("Asia/Kolkata"));
        System.out.println("Current Date-Time in IST: " + zonedDateTime);
    }
}
```

**Output (IST timezone):**

```
Current Date-Time in IST: 2025-03-22T18:05:30.123+05:30[Asia/Kolkata]
```

## **4. Using `System.currentTimeMillis()` (Epoch Timestamp)**

If you need the epoch timestamp in milliseconds (since January 1, 1970, UTC):

```
public class EpochTimeExample {
    public static void main(String[] args) {
        long epochMillis = System.currentTimeMillis();
        System.out.println("Current Epoch Time (ms): " + epochMillis);
    }
}
```

**Output:**

```
Current Epoch Time (ms): 1711234567890
```

## **Which One to Use:**

![](https://d1gq162ryfrcll.archive.ph/0GR7C/757890f6fb077ff24bd461baf68e80db4f779589.webp)

## **8. Suppose you have a List of employees with name and age. Write a program to filter employees with age > 50.**

Here’s a Java 8 program that filters employees with `age > 50` using Streams and Lambda expressions:

```
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Employee {
    private String name;
    private int age;
    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    @Override
    public String toString() {
        return "Employee{name='" + name + "', age=" + age + "}";
    }
}

public class EmployeeFilterExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Aman", 45),
            new Employee("Bobby", 55),
            new Employee("Chandan", 60),
            new Employee("Dinesh", 35),
            new Employee("Eva", 70)
        );

        // Filter employees with age > 50
        List<Employee> filteredEmployees = employees.stream()
            .filter(emp -> emp.getAge() > 50) // Lambda to filter employees
            .collect(Collectors.toList());

        // Print the filtered employees
        filteredEmployees.forEach(System.out::println);
    }
}
```

## **Output:**

```
Employee{name='Bobby', age=55}
Employee{name='Chandan', age=60}
Employee{name='Eva', age=70}
```

## **9. Write a program to remove duplicate elements from list using stream API.**

There are 2 cases to remove duplicate elements from a list:

## **1. Removing Duplicates from a List of Numbers**

```
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class RemoveDuplicatesExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(10, 20, 30, 10, 20, 40, 50, 30, 60);

        // Remove duplicates using Stream API
        List<Integer> uniqueNumbers = numbers.stream()
            .distinct()  // Removes duplicates
            .collect(Collectors.toList());

        // Print unique numbers
        System.out.println("Unique Numbers: " + uniqueNumbers);
    }
}
```

## **Output:**

```
Unique Numbers: [10, 20, 30, 40, 50, 60]
```

## **2. Removing Duplicates from a List of Custom Objects**

If you want to remove duplicates based on a specific field (like **ID**), use `Collectors.toMap()`.

```
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    private String name;
    private int id;
    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public int getId() {
        return id;
    }
    @Override
    public String toString() {
        return "Employee{id=" + id + ", name='" + name + "'}";
    }
}
public class RemoveDuplicateEmployees {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Amit", 1),
            new Employee("Priya", 2),
            new Employee("Rahul", 3),
            new Employee("Amit", 1), // Duplicate ID
            new Employee("Sneha", 4),
            new Employee("Priya", 2)  // Duplicate ID
        );
        // Remove duplicates based on Employee ID
        List<Employee> uniqueEmployees = employees.stream()
            .collect(Collectors.toMap(Employee::getId, e -> e, (existing, replacement) -> existing))
            .values()
            .stream()
            .collect(Collectors.toList());
        // Print unique employees
        uniqueEmployees.forEach(System.out::println);
    }
}
```

## **Output:**

```
Employee{id=1, name='Amit'}
Employee{id=2, name='Priya'}
Employee{id=3, name='Rahul'}
Employee{id=4, name='Sneha'}
```

## **10. How to setup a database connection for rest API project?**

Again, You can refer to the below article. I have created and established a new connection to DB from scratch.

[**Create a Spring Boot Rest API Project From ScratchFor Beginners**medium.com](https://archive.ph/o/0GR7C/https://medium.com/coding-odyssey/create-a-spring-boot-rest-api-project-from-scratch-937737b490f7)

## **11. Explain EntityManagerFactory.**

In Java Persistence API (JPA), `EntityManagerFactory` is a crucial component for managing entity managers and interacting with the database efficiently.

- It is a factory class that creates `EntityManager` instances.
- It is heavyweight and should be created only once per persistence unit.
- It manages the persistence unit, including the database connection, configurations, and entity mappings.

## **Working:**

- When an application starts, it creates an `EntityManagerFactory` using `Persistence.createEntityManagerFactory("persistence-unit-name")`.
- This factory produces multiple `EntityManager` instances for handling database operations.
- When the application shuts down, the factory should be closed to free resources.

## **Code Example:**

```
import javax.persistence.*;.

public class EntityManagerFactoryExample {
    public static void main(String[] args) {
        // Create EntityManagerFactory (One-time creation)
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("my-persistence-unit");
        // Create EntityManager (Used for DB operations)
        EntityManager em = emf.createEntityManager();
        // Begin transaction
        em.getTransaction().begin();
        // Persist an entity (Example: Employee)
        Employee employee = new Employee(101, "Amit", "IT");
        em.persist(employee);
        // Commit transaction
        em.getTransaction().commit();
        // Close EntityManager
        em.close();
        // Close EntityManagerFactory (Cleanup)
        emf.close();
    }
}
```

## **12. Explain @Transactional annotation.**

In Spring, the `@Transactional` annotation is used for transaction management in database operations.

It ensures that a method executes within a single transaction, meaning that either all changes are committed or none are applied (rollback).

- It is a declarative transaction management annotation in Spring.
- It ensures ACID (Atomicity, Consistency, Isolation, Durability) compliance in database operations.
- It automatically rolls back the transaction if an unchecked exception (`RuntimeException` or `Error`) occurs.
- It is applied at the service layer (not recommended for DAO or controller layers).

## **Working:**

- When a method is annotated with `@Transactional`, Spring creates a proxy that manages the transaction.
- Before execution, it begins a transaction.
- If the method executes successfully, it commits the transaction.
- If a `RuntimeException` is thrown, it rolls back the transaction.

## **Code Example:**

```
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import jakarta.persistence.*;

@Service
public class EmployeeService {
    @PersistenceContext
    private EntityManager entityManager;
    @Transactional
    public void createEmployee() {
        Employee emp1 = new Employee(101, "Amit", "IT");
        entityManager.persist(emp1);  // Insert operation
        Employee emp2 = new Employee(102, "Raj", "HR");
        entityManager.persist(emp2);  // Insert operation
        if (emp1.getName().equals("Amit")) {
            throw new RuntimeException("Simulating an error"); // This will trigger rollback
        }
    }
}
```

**Expected Behavior:**

- If `RuntimeException` occurs, both inserts (`emp1` & `emp2`) are **rolled back**.
- If no exception occurs, both employees are **persisted** in the database.

## **Transaction Rollback Rules:**

Exception Type Transaction Rollback:

`RuntimeException` / `Error` : Yes (Automatic Rollback)

`Checked Exception` (`Exception`) : No (Must be configured manually)

**How to Rollback on Checked Exceptions?**

```
@Transactional(rollbackFor = Exception.class)
public void updateEmployee() throws Exception {
    // Now the transaction will rollback for checked exceptions too
}
```

## **13. How to Connect to Two Different Databases in the Same Spring Boot Project?**

In Spring Boot, you can configure multiple data sources to connect to two different databases within the same project. This is useful when you need to access two independent databases for different purposes.

We will configure two data sources:

1. **Primary Database** (`MySQL`)
2. **Secondary Database** (`PostgreSQL`)

## **Step-by-Step Implementation**

## **Step 1: Add Dependencies in `pom.xml`**

```
<dependencies>
    <!-- Spring Boot Starter JPA -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
<!-- MySQL Driver -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    <!-- PostgreSQL Driver -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

## **Step 2: Configure `application.properties`**

```
# Primary DataSource (MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/primarydb
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.jpa.hibernate.ddl-auto=update

# Secondary DataSource (PostgreSQL)
spring.secondary.datasource.url=jdbc:postgresql://localhost:5432/secondarydb
spring.secondary.datasource.username=postgres
spring.secondary.datasource.password=admin
spring.secondary.datasource.driver-class-name=org.postgresql.Driver
spring.secondary.jpa.hibernate.ddl-auto=update
```

## **Step 3: Create Primary DataSource Configuration**

```
@Configuration
@EnableTransactionManagement
@EnableJpaRepositories(
        basePackages = "com.example.repository.primary",
        entityManagerFactoryRef = "primaryEntityManager",
        transactionManagerRef = "primaryTransactionManager"
)
public class PrimaryDBConfig {

    @Primary
    @Bean(name = "primaryDataSource")
    @ConfigurationProperties(prefix = "spring.datasource")
    public DataSourceProperties primaryDataSourceProperties() {
        return new DataSourceProperties();
    }

    @Primary
    @Bean(name = "primaryDataSource")
    public DataSource primaryDataSource(@Qualifier("primaryDataSourceProperties") DataSourceProperties properties) {
        return properties.initializeDataSourceBuilder().build();
    }
}
```

- `@Primary` ensures that this is the **default** data source.
- Specifies the `repository` and `entity` package locations.

## **Step 4: Create Secondary DataSource Configuration**

```
@Configuration
@PropertySource("classpath:application-secondary.properties")
@EnableTransactionManagement
@EnableJpaRepositories(
        basePackages = "com.example.repository.secondary",
        entityManagerFactoryRef = "secondaryEntityManager",
        transactionManagerRef = "secondaryTransactionManager"
)
public class SecondaryDBConfig {

    @Bean(name = "secondaryDataSourceProperties")
    @ConfigurationProperties(prefix = "spring.secondary.datasource")
    public DataSourceProperties secondaryDataSourceProperties() {
        return new DataSourceProperties();
    }

    @Bean(name = "secondaryDataSource")
    public DataSource secondaryDataSource(@Qualifier("secondaryDataSourceProperties") DataSourceProperties properties) {
        return properties.initializeDataSourceBuilder().build();
    }
}
```

- No `@Primary` annotation here, since it's the **secondary** database.
- Defines the repository and entity package locations for **PostgreSQL**.

## **Step 5: Define Entity Classes**

## **Primary Database Entity (`Employee` - MySQL)**

```
import jakarta.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;
    // Getters and Setters
}
```

## **Secondary Database Entity (`Order` - PostgreSQL)**

```
import jakarta.persistence.*;

@Entity
@Table(name = "orders")
public class Order {
@Id
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "order_seq")
@SequenceGenerator(name = "order_seq", sequenceName = "order_sequence", allocationSize = 1)
private Long id;
    private Long id;
    private String product;
    private double price;
    // Getters and Setters
}
```

## **Step 6: Create Repository Interfaces**

## **Primary Database Repository (MySQL)**

```
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.model.primary.Employee;

@Repository
public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}
```

## **Secondary Database Repository (PostgreSQL)**

```
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.model.secondary.Order;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
}
```

## **Step 7: Use Both Databases in Service Layer**

```
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class DatabaseService {
    private final EmployeeRepository employeeRepository;
    private final OrderRepository orderRepository;
    public DatabaseService(EmployeeRepository employeeRepository, OrderRepository orderRepository) {
        this.employeeRepository = employeeRepository;
        this.orderRepository = orderRepository;
    }
    @Transactional(transactionManager = "primaryTransactionManager")
    public void saveEmployee(Employee employee) {
        employeeRepository.save(employee);
    }
    @Transactional(transactionManager = "secondaryTransactionManager")
    public void saveOrder(Order order) {
        orderRepository.save(order);
    }
}
```

**14. Suppose you have a list of employees having name, emp id and company name. Can you group the employees with the company name.**

```jsx
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    private String name;
    private int empId;
    private String company;
    public Employee(String name, int empId, String company) {
        this.name = name;
        this.empId = empId;
        this.company = company;
    }
    public String getCompany() {
        return company;
    }
    @Override
    public String toString() {
        return "Employee{name='" + name + "', empId=" + empId + "}";
    }
}
public class EmployeeGrouping {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
                new Employee("Amit", 101, "TCS"),
                new Employee("Priya", 102, "Infosys"),
                new Employee("Ravi", 103, "TCS"),
                new Employee("Neha", 104, "Wipro"),
                new Employee("Suresh", 105, "Infosys"),
                new Employee("Meena", 106, "HCL"),
                new Employee("Vikram", 107, "Wipro")
        );
        // Group employees by company name
        Map<String, List<Employee>> groupedByCompany = employees.stream()
                .collect(Collectors.groupingBy(Employee::getCompany));
 
         // Print the grouped employees
        groupedByCompany.forEach((company, empList) -> {
            System.out.println("Company: " + company);
            empList.forEach(System.out::println);
            System.out.println();
        });
    }
}
```

**Output:**

```jsx
Company: TCS
Employee{name='Amit', empId=101}
Employee{name='Ravi', empId=103}

Company: Infosys
Employee{name='Priya', empId=102}
Employee{name='Suresh', empId=105}

Company: Wipro
Employee{name='Neha', empId=104}
Employee{name='Vikram', empId=107}

Company: HCL
Employee{name='Meena', empId=106}
```

## **15. How to manage the performance of APIs?**

Below are some key strategies to optimize and manage API performance effectively:

## **1. Use Efficient Database Queries**

**Optimize Queries:**

- Avoid N+1 query problems by using `JOIN` or `FETCH` in JPA.
- Use indexes on frequently queried columns.
- Cache frequently accessed data to reduce DB calls.

**Example:**

```
@Query("SELECT e FROM Employee e JOIN FETCH e.department WHERE e.id = :id")
Employee findByIdWithDepartment(@Param("id") Long id);
```

**Use Connection Pooling** (`HikariCP` is the best choice for Spring Boot).

```
spring.datasource.hikari.maximum-pool-size=10
spring.datasource.hikari.minimum-idle=5
```

## **2. Implement Caching**

- Use Redis or In-Memory Cache for frequent API responses.
- Reduces unnecessary DB hits and improves response time.

**Example (Using Spring Boot & Redis):**

```
@Cacheable(value = "employees", key = "#id")
public Employee getEmployeeById(Long id) {
    return employeeRepository.findById(id).orElse(null);
}
```

## **3. Asynchronous Processing & Background Jobs**

Use async execution for heavy processing tasks to prevent blocking API requests.

**Example (Using `@Async` in Spring Boot):**

```
@Async
public CompletableFuture<String> processHeavyTask() {
    return CompletableFuture.supplyAsync(() -> {
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return "Task Completed";
    });
}
```

**Why:**

- The API immediately returns a response without waiting for the process to complete.
- Users don’t experience delays.

## **4. Use Pagination & Limit Data Fetching**

- Fetching large datasets slows down APIs and increases memory usage.
- Always paginate API responses.

**Example:**

```
@GetMapping("/employees")
public Page<Employee> getEmployees(@RequestParam int page, @RequestParam int size) {
    return employeeRepository.findAll(PageRequest.of(page, size));
}
```

**Why:**

- Improves response time.
- Reduces load on the database.

## **5. Enable GZIP Compression**

- Reduce API response size by enabling GZIP compression.
- Saves bandwidth and speeds up client-server communication.

**Enable in `application.properties`:**

```
server.compression.enabled=true
server.compression.mime-types=application/json
```

## **6. Use Content Delivery Networks (CDNs) for Static Resources**

- For static assets (images, CSS, JS), use a CDN to reduce server load.
- CDNs store cached copies of data closer to users, improving response time.

**Example:**

- Use Cloudflare, AWS CloudFront, or Akamai.

## **7. Rate Limiting & Throttling**

- Prevent API abuse and DDoS attacks by limiting requests per user.
- Implement Spring Boot Rate Limiting using Bucket4j or Redis.

**Example (Using Bucket4j for rate limiting):**

```
@RateLimiter(name = "employeeApi")
@GetMapping("/employees")
public List<Employee> getEmployees() {
    return employeeService.getAllEmployees();
}

public ResponseEntity<String> rateLimitFallback(Exception e) {
    return ResponseEntity.status(HttpStatus.TOO_MANY_REQUESTS).body("Too many requests, please try again later.");
}
```

**Why:**

- Prevents system overload.
- Ensures fair resource distribution.

## **8. Use API Gateway for Load Balancing**

- Distribute traffic across multiple instances using API Gateways like Kong, AWS API Gateway, or Nginx.
- Helps in load balancing, authentication, and caching.

**Example (Using Spring Cloud Gateway):**

```
spring:
  cloud:
    gateway:
      routes:
        - id: employee-service
          uri: lb://EMPLOYEE-SERVICE
          predicates:
            - Path=/employees/**
```

**Why:**

- Ensures high availability.
- Distributes load efficiently.

## **9. Use Efficient Serialization (JSON/Binary Formats)**

- Use JSON compression to reduce payload size.
- Consider Protobuf or MessagePack for better performance in high-throughput APIs.

**Example (Using Protobuf in Spring Boot):**

```
message Employee {
    int32 id = 1;
    string name = 2;
    string department = 3;
}
```

- Protobuf is smaller & faster than JSON.
- Reduces network latency.

## **10. Monitor & Analyze API Performance**

Use APM tools to monitor API performance:

- Prometheus + Grafana 📈
- New Relic, Datadog, or AWS CloudWatch
- Spring Boot Actuator

**Enable Spring Boot Actuator for monitoring:**

```
management.endpoints.web.exposure.include=metrics,health
```

**Monitor:**

- API response times
- CPU & memory usage
- Error rates & slow queries

## **16. How do microservices communicate with each other?**

> This question was asked in Accenture Interview (Question 15) and Deloitte Interview (Question 4) as well. So, this is an important question.
> 

In microservices, services communicate using different methods depending on the use case, performance needs, and architecture.

1. **Synchronous Communication**:
- **REST (HTTP)**: Services expose REST APIs for lightweight, language-agnostic communication. Example:

```
@RestController public class ProductController {

@GetMapping("/product/{id}")
public String getProduct(@PathVariable String id) {
         return "Product Details for ID: " + id;
}
}
```

- **gRPC**: A high-performance alternative to REST using HTTP/2 and Protocol Buffers. It supports bi-directional streaming and better efficiency.

**2. Asynchronous Communication**:

- **Message Brokers**: Services use queues or streams (e.g., Kafka, RabbitMQ) to exchange messages. Example:

```
@Service public class OrderService {
     @Autowired
     private KafkaTemplate<String, String> kafkaTemplate;

     public void sendOrderEvent(String order) {
         kafkaTemplate.send("order_topic", order);
     }
}
```

- **Event-Driven**: Events (e.g., `OrderCreated`) trigger other services to react. Suitable for loosely coupled architectures.

**3. Service Discovery**:

- Tools like **Eureka** and **Consul** help microservices find each other dynamically. Example: Services register with Eureka, and clients query the registry for instances.

**4. Remote Procedure Calls (RPC)**:

- **gRPC** or **JSON-RPC** enables efficient service-to-service communication using method calls.

**5. API Gateway**:

- Acts as a single entry point for clients. Aggregates responses from multiple microservices. Example: Netflix’s Zuul or Spring Cloud Gateway.

**6. Fault Tolerance (Circuit Breakers)**:

- Circuit breakers like **Hystrix** detect failures and prevent cascading effects by stopping communication temporarily.

These mechanisms ensure scalability, fault tolerance, and efficiency in a distributed system.

## **17. How is the load balancer implemented in Azure DevOps?**

A Load Balancer ensures that incoming traffic is distributed evenly across multiple instances of an application, improving availability, reliability, and scalability.

In Azure DevOps, you can implement a Load Balancer using Azure Load Balancer, Azure Application Gateway, or Azure Front Door.

## **1. Azure Load Balancer (Layer 4 — Transport Layer)**

- Distributes incoming traffic across multiple Virtual Machines (VMs) or containers
- Works at Layer 4 (TCP/UDP) of the OSI model
- Supports high availability & failover

**Example: Deploying an App Behind an Azure Load Balancer**

```
- task: AzureResourceManagerTemplateDeployment@3
  inputs:
    deploymentScope: 'Resource Group'
    azureResourceManagerConnection: 'MyAzureSubscription'
    resourceGroupName: 'my-resource-group'
    templateLocation: 'Linked artifact'
    csmFile: 'load-balancer-template.json'
    deploymentMode: 'Incremental'
```

The ARM template (`load-balancer-template.json`) will create:

- Public Load Balancer
- Backend Pool with VMs
- Health Probes for monitoring VM availability

## **2. Azure Application Gateway (Layer 7 — HTTP/HTTPS)**

- Works at Layer 7 (Application Layer)
- Supports URL-based routing, SSL termination, Web Application Firewall (WAF)
- Ideal for web applications, API gateways, and microservices

**Example: Deploying a Web App with Application Gateway**

```
- task: AzureCLI@2
  inputs:
    azureSubscription: 'MyAzureSubscription'
    scriptType: 'bash'
    scriptLocation: 'inlineScript'
    inlineScript: |
      az network application-gateway create \
        --name myAppGateway \
        --resource-group my-resource-group \
        --sku WAF_v2 \
        --public-ip-address myPublicIP \
        --frontend-port 443 \
        --backend-pool-name myBackendPool \
        --backend-address myAppService.azurewebsites.net
```

The **Application Gateway** will:

- Route traffic based on URL path or hostname
- Terminate SSL connections to offload encryption
- Provide DDoS protection & Web Application Firewall (WAF)

## **3. Azure Front Door (Global Load Balancer)**

- Distributes traffic globally across multiple regions
- Works at Layer 7 and supports caching, SSL offloading, & geo-routing
- Best for multi-region deployments & content delivery

**Example: Creating a Global Load Balancer with Azure Front Door**

```
- task: AzureCLI@2
  inputs:
    azureSubscription: 'MyAzureSubscription'
    scriptType: 'bash'
    scriptLocation: 'inlineScript'
    inlineScript: |
      az afd profile create --resource-group my-resource-group --profile-name myFrontDoor
      az afd endpoint create --resource-group my-resource-group --profile-name myFrontDoor --endpoint-name myEndpoint
      az afd route create --resource-group my-resource-group --profile-name myFrontDoor --endpoint-name myEndpoint --route-name myRoute --origin-group myBackendPool --https-redirect enabled
```

The Azure Front Door will:

- Direct traffic to the nearest data center
- Provide caching & CDN features
- Improve latency & performance for global users

## **4. Implementing Load Balancing in Kubernetes (AKS)**

If using Azure Kubernetes Service (AKS), you can implement a load balancer via:

- Internal Load Balancer (private traffic)
- External Load Balancer (public traffic)

**Example: Creating a LoadBalancer Service in AKS**

```
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

This exposes the application via an Azure Load Balancer

## **18. If I have a variable of datatype CLOB in Oracle DB, what will be it’s corresponding datatype in postgres?**

In Oracle DB, the `CLOB` (Character Large Object) data type is used to store large amounts of text data. When migrating to PostgreSQL, the equivalent data type would be:

1. **`TEXT` (Recommended)**
- `TEXT` in PostgreSQL can store unlimited text data (up to 1 GB per field).
- It behaves similarly to `CLOB` in Oracle and is optimized for performance.
- Unlike `VARCHAR(n)`, `TEXT` has no strict size limit.

**Example:**

```
CREATE TABLE my_table (
     id SERIAL PRIMARY KEY,
     my_text_column TEXT
);
```

**`2. BYTEA` (If Storing Large Encoded Data)**

- If the CLOB contains binary-encoded data (e.g., XML, JSON, logs) that must be stored in a large format, `BYTEA` can also be used.
- However, for plain text, `TEXT` is the preferred choice.

**`3. VARCHAR(n)` (Not Recommended for Large Text Data)**

- While `VARCHAR(n)` can be used, it has a length constraint, making it less suitable for CLOB-sized data.

## **19. Explain Generics and its use cases in brief.**

Generics in Java allow us to create classes, interfaces, and methods that operate on parameterized types. This provides compile-time type safety and code reusability.

Generics enable a type (class or method) to operate on different data types while maintaining type safety.

## **Example Without Generics (Type Casting Required)**

```
import java.util.ArrayList;

public class WithoutGenerics {
    public static void main(String[] args) {
        ArrayList list = new ArrayList();  // No type specified
        list.add("Hello");
        list.add(123);  // Accidental addition of an Integer

        String str = (String) list.get(0);  // Explicit casting required
        String str2 = (String) list.get(1); // Error: ClassCastException at runtime
    }
}
```

**Problem:**

- No compile-time type checking (mixing different types is possible).
- Requires explicit casting, which can lead to runtime errors.

## **Example With Generics**

```
import java.util.ArrayList;
public class WithGenerics {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();  // Type-safe
        list.add("Hello");
        // list.add(123);  // Compilation error 🚀
        String str = list.get(0);  // No casting required
        System.out.println(str);   // Output: Hello
    }
}
```

## **Advantages:**

- Compile-time type checking (prevents runtime errors).
- No need for explicit type casting.
- Code reusability with different data types.

## **Use Cases:**

- **Collections (Lists, Maps, Sets)** — Ensures type safety.
- **Utility Methods** — Generic algorithms (sorting, searching).
- **Custom Data Structures** — Generic classes (Stacks, Queues).
- **Dependency Injection** — Type-safe service providers.
- **Bounded Types** — Enforce constraints for valid types.

## **20. What do you understand by code reusability?**

Code reusability means writing code in a way that it can be used multiple times without modification.

Instead of duplicating logic across different parts of a program, reusable code is structured so that it can be called whenever needed, making development more efficient, maintainable, and scalable.

For example, using functions/methods, classes, inheritance, interfaces, generics, and design patterns all contribute to reusability.

## **Example: Using a Method for Reusability**

Instead of writing the same logic multiple times, we encapsulate it in a method:

```
public class ReusabilityExample {
    public static int add(int a, int b) {
        return a + b;
    }

public static void main(String[] args) {
        System.out.println(add(5, 10)); // 15
        System.out.println(add(20, 30)); // 50
    }
}
```

Here, the `add()` method is reusable, preventing redundant code.

## **Example: Reusability with Inheritance**

If multiple classes need the same functionality, we can define it in a parent class and reuse it in child classes:

```
class Vehicle {
    public void start() {
        System.out.println("Vehicle is starting...");
    }
}

class Car extends Vehicle {
    public void honk() {
        System.out.println("Car is honking...");
    }
}
public class InheritanceExample {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.start(); // Inherited from Vehicle
        myCar.honk();  // Specific to Car
    }
}
```

Here, `Car` reuses the `start()` method from `Vehicle` instead of redefining it.

## **Advantages:**

- **Less duplication** → Reduces redundant code
- **Easier maintenance** → Fix issues in one place instead of multiple
- **Scalability** → Makes it easier to expand functionality
- **Cleaner, more readable code**

## **21. How to implement multi threading?**

In Java, multithreading is implemented using the `Thread` class or the `Runnable` interface. It allows concurrent execution of multiple tasks, improving performance and responsiveness.

## **1. Extending the `Thread` Class**

```
class MyThread extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() + " - Count: " + i);
            try {
                Thread.sleep(1000); // Simulate work
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadExample {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();

        t1.start(); // Starts a new thread
        t2.start(); // Another thread
    }
}
```

**Pros**: Simple to implement**Cons**: Can’t extend other classes (Java doesn’t support multiple inheritance)

## **2. Implementing `Runnable` Interface**

```
class MyRunnable implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() + " - Count: " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
public class RunnableExample {
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyRunnable());
        Thread t2 = new Thread(new MyRunnable());
        t1.start();
        t2.start();
    }
}
```

**Pros**: Allows multiple inheritance (since we implement an interface)

## **3. Using `ExecutorService` (Thread Pool)**

For better thread management in large-scale applications:

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Task implements Runnable {
    public void run() {
        System.out.println(Thread.currentThread().getName() + " is executing task.");
    }
}
public class ExecutorExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            executor.execute(new Task());
        }

        executor.shutdown();
    }
}
```

**Pros**: Better performance, avoids creating too many threads

## **4. Using `Callable` (Returning a Value from a Thread)**

Unlike `Runnable`, `Callable` can return a result:

```
import java.util.concurrent.*;
class MyTask implements Callable<String> {
    public String call() {
        return "Task Completed!";
    }
}
public class CallableExample {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<String> result = executor.submit(new MyTask());

        System.out.println(result.get()); // Waits for result
        executor.shutdown();
    }
}
```

**Pros**: Can return values and handle exceptions

## **22. Explain ExecutorService.**

In Java, ExecutorService is part of the `java.util.concurrent` package and provides a better way to manage multiple threads efficiently.

Instead of manually creating and managing threads, ExecutorService handles thread creation, execution, and reuse, improving performance and resource management.

ExecutorService:

- **Manages thread pools** instead of creating new threads every time
- **Improves performance** by reusing threads
- **Prevents excessive thread creation**, avoiding memory issues
- **Provides control** over thread execution, scheduling, and termination

## **1. Creating an `ExecutorService` (Thread Pools)**

## **Fixed Thread Pool**

A fixed number of threads are created and reused.

```
import java.util.concurrent.*;

public class FixedThreadPoolExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3); // 3 threads in pool
        for (int i = 1; i <= 5; i++) {
            executor.execute(() -> System.out.println(Thread.currentThread().getName() + " executing task"));
        }
        executor.shutdown(); // Shutdown after task completion
    }
}
```

**Best for**: Tasks with a known number of threads needed

## **Cached Thread Pool**

Creates new threads as needed and reuses idle ones.

```
ExecutorService executor = Executors.newCachedThreadPool();
```

**Best for**: Large number of short-lived tasks

## **Single Thread Executor**

Executes tasks sequentially using a **single thread**.

```
ExecutorService executor = Executors.newSingleThreadExecutor();
```

**Best for**: Tasks that need to be executed in order

## **Scheduled Thread Pool:**

Schedules tasks to run after a delay or at a fixed rate.

```
import java.util.concurrent.*;

public class ScheduledExecutorExample {
    public static void main(String[] args) {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
        scheduler.schedule(() -> System.out.println("Delayed Task Executed"), 3, TimeUnit.SECONDS);

        scheduler.shutdown();
    }
}
```

**Best for**: Scheduled or periodic tasks (like cron jobs)

## **2. Submitting Tasks to `ExecutorService`**

## **Using `execute()`**

Used for `Runnable` tasks (does not return a value).

```
executor.execute(() -> System.out.println("Runnable Task"));
```

## **Using `submit()`**

Used for `Callable` tasks (returns a result).

```
Future<Integer> result = executor.submit(() -> 10 + 20);
System.out.println(result.get()); // Output: 30
```

## **3. Shutting Down `ExecutorService`**

After submitting tasks, it’s important to **shut down** the executor.

```
executor.shutdown(); // Stops accepting new tasks but completes ongoing ones

executor.shutdownNow(); // Attempts to stop running tasks immediately
```

# **Final Thoughts**

This seemed a very scattered interview. The interviewer sometimes asked questions about complete implementation and sometimes very surface level theory questions.

The interviewee was not able to clear the interview due to the implementation from scratch questions.