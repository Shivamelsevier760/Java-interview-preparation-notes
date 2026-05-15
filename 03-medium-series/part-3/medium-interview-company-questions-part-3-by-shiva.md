# Medium interview company questions part 3 by Shivam Srivastava

# **BirlaSoft Java Developer Interview**

## **1. What is Polymorphism in Java?**

Polymorphism in Java is one of the four fundamental OOP (Object-Oriented Programming) concepts (along with inheritance, encapsulation, and abstraction).

The term literally means “many forms,” and that’s exactly what it allows: the ability of an object, method, or function to behave differently based on the context.

In simple terms, Polymorphism lets you perform the same action in different ways.

## **Types:**

**1. Compile-Time Polymorphism (aka Method Overloading):**

- Achieved by overloading methods (same name, different parameters).
- Happens at compile time (hence the name).

```
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

double add(double a, double b) {
        return a + b;
    }
}
```

Here, the method `add()` behaves differently based on the type/number of arguments.

**2. Run-Time Polymorphism (aka Method Overriding):**

- Achieved through inheritance.
- The subclass provides a specific implementation of a method that’s already defined in its superclass.
- Decided at runtime using dynamic method dispatch.

```
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks");
    }
}
public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();  // Upcasting
        a.sound();             // Output: Dog barks
    }
}
```

Even though `a` is of type `Animal`, the `Dog`'s version of `sound()` is called at runtime.

## **Usefulness:**

- Makes code flexible and extensible.
- Promotes loose coupling and scalability.
- Reduces code duplication.

## **2. Explain Method Overriding.**

Method Overriding means providing a new implementation for a method in the subclass that is already defined in the parent class.

This enables runtime polymorphism — the ability to call the overridden method based on the actual object type, not the reference type.

## **Example:**

```
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
public class Main {
    public static void main(String[] args) {
        Animal obj = new Dog();  // Upcasting
        obj.sound();             // Output: Dog barks
    }
}
```

## **Features:**

- Method name, return type, and parameters must match exactly.
- Must occur between superclass and subclass.
- Use `@Override` annotation for better readability and compile-time checks.
- Polymorphism is enabled — i.e., decision made at runtime.
- Only instance methods can be overridden.

## **Rules of Method Overriding:**

1. Same method signature (name + parameters + return type).
2. Static, final, or private methods cannot be overridden.
3. Access modifier in the child must be same or more accessible:
- `protected` → can be `protected` or `public`
- `public` → must remain `public`

4. Overriding method cannot throw broader checked exceptions than the overridden one.

5. Constructors cannot be overridden.

6. If parent method returns a class type, overriding can return a subtype (called covariant return type).

## **Use Cases:**

- **Framework callbacks** (Spring Boot lifecycle hooks like `onStart`, `destroy`)
- **UI handling** (Android’s `onClick`, `onCreate`, etc.)
- **API design** — Different business logic per customer/role using subclassing
- **Game development** — Base class `Character` has method `attack()`, each subclass overrides it

## **Advantages:**

- Enables runtime polymorphism
- Increases flexibility and extensibility
- Promotes code reuse by inheriting and customizing only the required part
- Essential for interface and abstract class implementations

## **Disadvantages:**

- Can cause confusion in large inheritance trees
- Maintenance issues if superclass methods change
- Risk of violating Liskov Substitution Principle
- Can lead to tight coupling between parent and child classes.

## **3. Can we override the static method?**

**No, static methods cannot be overridden in Java.**

In Java:

- Static methods belong to the class, not to instances.
- Method overriding is a concept that applies to instance methods, resolved at runtime using the actual object type.
- Static methods are resolved at compile-time using the reference type, not the object.

If a subclass defines a static method with the **same signature** as a static method in the parent class, it’s not overriding — it’s called **method hiding**.

## **Example:**

```
class Parent {
    static void display() {
        System.out.println("Parent static method");
    }
}

class Child extends Parent {
    static void display() {
        System.out.println("Child static method");
    }
}
public class Main {
    public static void main(String[] args) {
        Parent obj = new Child();
        obj.display(); // Output: Parent static method
    }
}
```

- Even though `obj` is referring to a `Child` object, the call is resolved based on the reference type, which is `Parent`.
- Hence, the output is `"Parent static method"`, not `"Child static method"`.

## **4. Why are strings immutable in Java?**

In Java, `String` is immutable, meaning once a `String` object is created, it cannot be changed.

Any operation that appears to modify a string (like `concat()`, `substring()`, `replace()`, etc.) actually creates a new string object.

Here are the core reasons why:

## **1. Security**

1. Strings are heavily used in security-sensitive operations, such as:
- File paths
- Network connections (URLs, IPs)
- Database credentials
- Class loading (`Class.forName("com.example.MyClass")`)

2. If `String` were mutable, someone could change the content after security checks (e.g., swap `"admin"` with `"hacker"` mid-process), opening up a huge vulnerability.

## **2. String Pooling (Memory Optimization)**

- Java maintains a String Constant Pool to reuse common string literals.
- **Example:**

```
String a = "hello";
String b = "hello";

System.out.println(a == b); // true (same reference)
```

- This is only possible because strings are immutable. If one reference could change the value, it would corrupt the pool.

## **3. Thread Safety**

- Immutability means no thread can modify a `String` object — making it thread-safe by default.
- No need to use synchronization when multiple threads are using the same string — this improves performance.

## **4. Caching HashCode**

- `String`'s `hashCode()` is frequently used in hash-based collections like `HashMap`, `HashSet`.
- Since the value doesn’t change, the hashCode can be cached, speeding up lookups.

```
private int hash; // cached hashCode in String class
```

## **5. Safe Sharing Across Code**

- You can freely share a string without worrying that someone else’s code might modify it.
- This promotes reliable, defensive programming.

**If You Need a Mutable Version, Java provides:**

- `StringBuilder` – non-thread-safe but faster
- `StringBuffer` – thread-safe but slower

## **Example**

```
String s = "Java";
s.concat(" Rocks");
System.out.println(s); // Output: Java (not "Java Rocks")
```

Because `concat()` returned a new string. The original string `s` is untouched.

## **5. How to create an Immutable class in Java?**

I have already written a detailed article on the same. This would be one of the best article you’ll find on this topic:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/0meNk/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

## **6. Suppose you’ve a list of objects. How to change this list of objects to immutable?**

If you have a `List<Object>` and you want to make sure no one can modify it, below are the recommended ways:

## **Approach 1: `Collections.unmodifiableList(`)**

```
List<String> originalList = new ArrayList<>();
originalList.add("Java");
originalList.add("Python");

List<String> immutableList = Collections.unmodifiableList(originalList);
// immutableList.add("C++"); // Throws UnsupportedOperationException
```

The *reference* is immutable, but **not the objects inside the list.**So if your list has mutable objects, someone could still modify them.

## **Approach 2: `List.of(...)` (Java 9+)**

```
List<String> immutableList = List.of("Java", "Python", "C++");
// immutableList.add("Go");
// Throws UnsupportedOperationException
```

Cleaner and concise. Also does not allow nulls and throws exception if modified.

## **Approach 3: Deep Immutability (if list contains mutable objects)**

If your list contains custom objects, you must deep-copy them into immutable versions:

```
List<Person> mutableList = new ArrayList<>();
mutableList.add(new Person("John", 25));

// Convert to deeply immutable list
List<Person> immutableList = Collections.unmodifiableList(
    mutableList.stream()
               .map(person -> new Person(person.getName(), person.getAge()))
               .collect(Collectors.toList())
);
```

Here `Person` must be an immutable class.

**Just FYI**,

> Just making the list unmodifiable is shallow immutability.If objects inside it are mutable, someone can still do:
> 

```
immutableList.get(0).setAge(100); // still modifies the state!
```

> So always pair this with immutable object design.
> 

## **7. How do you achieve deep cloning?**

Deep cloning in Java means creating a completely independent copy of an object, including all objects referenced by it (and their references too), so that changes in the cloned object do not affect the original one at all.

There are multiple ways to achieve deep cloning:

## **1. Using Serialization (for simple POJOs)**

```
ByteArrayOutputStream bos = new ByteArrayOutputStream();
ObjectOutputStream out = new ObjectOutputStream(bos);
out.writeObject(original);

ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
ObjectInputStream in = new ObjectInputStream(bis);
MyObject deepCopy = (MyObject) in.readObject();
```

**Note:** The class and all its fields must implement `Serializable`.

## **2. Manual Deep Copy (Recommended for control & performance)**

Write a custom `clone()` or a copy constructor:

```
class Address {
    String city;
    Address(String city) {
        this.city = city;
    }

Address(Address other) {
        this.city = new String(other.city);
    }
}
class Person {
    String name;
    Address address;
    Person(String name, Address address) {
        this.name = name;
        this.address = address;
    }
    Person(Person other) {
        this.name = new String(other.name);
        this.address = new Address(other.address);
    }
}
```

## **3. Using Apache Commons `SerializationUtils`**

```
Person cloned = SerializationUtils.clone(original);
```

You just need to add:

```
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.x</version>
</dependency>
```

## **4. Using JSON Libraries (Quick & Dirty Way)**

Serialize to JSON and deserialize back (deep copy achieved):

```
ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(original);
MyObject cloned = mapper.readValue(json, MyObject.class);
```

Works well for DTOs or data-heavy objects.

## **8. What is the contract between equals and hashcode method?**

> This questions was also asked in Collabera Interview (Question - 3). So, this is an important question.
> 

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

## **9. Is it possible to insert a duplicate key in a HashMap?**

No, we cannot insert a duplicate key in a `HashMap`.

If you try to put the same key again:

```
Map<String, String> map = new HashMap<>();
map.put("language", "Java");
map.put("language", "Python");
```

The second `put()` doesn’t insert a new key — it overwrites the value for the existing key `"language"`.

**Output**:

```
System.out.println(map.get("language")); // Output: Python
```

The key `"language"` exists only once in the map, with the value `"Python"` now.

**So, internally:**

- `HashMap` checks if the key already exists (using `hashCode()` and `equals()`).
- If it does, it updates the value.
- If not, it adds a new key-value pair.

## **10. Can you have null as a key in HashMap?**

Yes, absolutely — a `HashMap` can have one `null` key.

Java’s `HashMap` allows:

- One `null` key
- Multiple `null` values

```
Map<String, String> map = new HashMap<>();
map.put(null, "first");
map.put(null, "second");
System.out.println(map.get(null)); // Output: second
```

So just like any other key, if you put the `null` key again, it’ll overwrite the previous value.

## **Internally:**

- `null` is treated as a special case.
- `HashMap` uses index 0 of the bucket array for it.
- Since `null` can’t call `.hashCode()`, it’s handled separately in the implementation.

## **11. What are the advantages and disadvantages of using Hibernate?**

Below are the advantages and disadvantages of using Hibernate:

## **Advantages:**

**1. Eliminates Boilerplate JDBC Code:** You don’t have to write repetitive `Connection`, `ResultSet`, or `Statement` code. Just define your entities and let Hibernate handle the rest.

**2. Database Independence:** Write once, run on any DB. Hibernate abstracts SQL differences, so switching from MySQL to Oracle, for example, is much easier.

**3. Automatic Table Mapping:**Using annotations or XML, you map Java classes to DB tables without needing SQL DDL manually.

**4. Caching for Better Performance:** Built-in first-level cache and optional second-level cache (EHCache, etc.) reduce DB hits.

**5. Lazy Loading & Fetching Strategies:** Efficient fetching of related entities only when needed.

**6. HQL (Hibernate Query Language):** A powerful, object-oriented query language similar to SQL but works on entity objects instead of tables.

**7. Transaction Management:** Integrates well with JTA, Spring, and others for clean, declarative transactions.

## **Disadvantages:**

**1. Learning Curve:** Understanding HQL, mappings, annotations, cascading, and lazy loading can be tricky for beginners.

**2. Debugging is Harder:** You lose visibility over raw SQL; Hibernate-generated queries can be complex and hard to debug.

**3. Performance Issues:** Incorrect use of lazy/eager fetching or N+1 select problems can seriously hurt performance.

**4. Too Much Abstraction:** It hides SQL — great until you need fine-grained control or tuning, then it becomes painful.

**5. Heavyweight:** For small projects, Hibernate can feel bloated compared to using simple JDBC or JDBI.

**6. Magic Behavior:** Sometimes, Hibernate behaves in unexpected ways due to caching, session management, or proxies — especially annoying in large, complex applications.

## **12. How to enhance the performance of Hibernate queries?**

Below are a list of practical ways to boost Hibernate performance:

## **1. Enable and Configure Connection Pooling**

Use connection pools like HikariCP (preferred), C3P0, or Apache DBCP.

Example (for HikariCP in `hibernate.cfg.xml` or `application.properties`):

```
hibernate.hikari.maximumPoolSize=20
hibernate.hikari.minimumIdle=5
hibernate.hikari.idleTimeout=30000
hibernate.hikari.connectionTimeout=30000
hibernate.hikari.maxLifetime=1800000
```

**Tip:** HikariCP is faster and more lightweight than C3P0.

## **2. Use Fetch Type Wisely**

- Use `LAZY` loading for large associations.
- Use `EAGER` only when you always need the related data.

```
@OneToMany(fetch = FetchType.LAZY)
private List<Order> orders;
```

## **3. Batch Processing for Inserts/Updates**

Helps when saving/updating large collections.

```
hibernate.jdbc.batch_size=50
hibernate.order_inserts=true
hibernate.order_updates=true
```

Make sure your entity has `@BatchSize(size = 50)` for collections.

## **4. Use Second-Level Cache**

Caches objects across sessions.

```
hibernate.cache.use_second_level_cache=true
hibernate.cache.region.factory_class=org.hibernate.cache.ehcache.EhCacheRegionFactory
```

Use libraries like Ehcache or Infinispan.

## **5. Avoid N+1 Select Problem**

Use `JOIN FETCH` or `@Fetch(FetchMode.JOIN)` to load collections efficiently.

```
@Fetch(FetchMode.JOIN)
@OneToMany(fetch = FetchType.LAZY)
private List<Order> orders;
```

Or via HQL:

```
SELECT c FROM Customer c JOIN FETCH c.orders
```

## **6. Use Projections (DTOs) Instead of Whole Entities**

If you only need a few fields, don’t fetch the whole entity.

```
SELECT new com.example.CustomerDTO(c.name, c.email) FROM Customer c
```

## **7. Use Native SQL for Complex Queries**

Hibernate’s HQL is great, but if a query is too slow or complex — drop to native SQL when needed.

```
@Query(value = "SELECT * FROM employee WHERE salary > ?", nativeQuery = true)
List<Employee> findHighEarners(BigDecimal threshold);
```

## **8. Tune Hibernate Properties**

```
hibernate.show_sql=false        # Disable in prod!
hibernate.format_sql=false
hibernate.generate_statistics=false
hibernate.use_sql_comments=false
```

## **9. Monitor & Profile**

Use tools like:

- Hibernate Statistics (`SessionFactory.getStatistics()`)
- JProfiler / VisualVM
- SQL logs

## **13. What is a dialect in Hibernate?**

In Hibernate, a dialect is basically a bridge between Hibernate and your database.

A dialect is a class in Hibernate that tells it how to generate SQL for a particular type of database (e.g., MySQL, Oracle, PostgreSQL, etc.).

## **Need:**

Different databases have different:

- SQL syntax (`LIMIT` vs `ROWNUM`)
- Data types (`AUTO_INCREMENT` vs `SEQUENCE`)
- Functions (`NOW()` vs `SYSDATE`)

Hibernate needs to know which flavor of SQL to generate. That’s what the dialect is for.

## **Example:**

```
<property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>
```

For PostgreSQL:

```
<property name="hibernate.dialect">org.hibernate.dialect.PostgreSQLDialect</property>
```

For Oracle:

```
<property name="hibernate.dialect">org.hibernate.dialect.Oracle10gDialect</property>
```

## **If you don’t set it correctly:**

- Hibernate might generate invalid SQL
- Or use wrong types (e.g., `VARCHAR2` vs `TEXT`)
- You might see runtime errors or schema mismatches

## **Hibernate takes care of:**

- Generating correct SQL queries
- Creating schema correctly (DDL)
- Handling data type mappings

**14. What are the differences between get() and load() method in Hibernate?**

![](https://df5byh02ambd3x.archive.ph/0meNk/83b4cf01d1f27ef858df8262546b4d6cc3fe8ba6.webp)

**15. What are the differences between save() and merge() method?**

![](https://df5byh02ambd3x.archive.ph/0meNk/4b1da36608486251c50e8c1f505a1c63463a1e72.webp)

## **16. How to implement HTTPS?**

To implement HTTPS in your web application, you’re essentially enabling secure communication over HTTP by using SSL/TLS certificates.

Here’s a step-by-step guide to implement HTTPS:

## **1. Obtain an SSL Certificate**

- You can get one from a trusted Certificate Authority (CA) (like Let’s Encrypt, DigiCert, GoDaddy, etc.).
- Or generate a self-signed certificate for testing (not recommended for production).

## **2. Install the SSL Certificate**

**For Apache:**

- Enable `mod_ssl`:

```
sudo a2enmod ssl
```

- Update your site config to include:

```
<VirtualHost *:443>
    ServerName yourdomain.com
    SSLEngine on
    SSLCertificateFile /path/to/cert.pem
    SSLCertificateKeyFile /path/to/key.pem
    SSLCertificateChainFile /path/to/chain.pem
</VirtualHost>
```

**For Nginx:**

```
server {
    listen 443 ssl;
    server_name yourdomain.com;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
}
```

**For Spring Boot:**

- Place `.p12` or `.jks` keystore in resources.
- Add to `application.properties`:

```
server.port=8443
server.ssl.key-store=classpath:keystore.p12
server.ssl.key-store-password=password
server.ssl.key-store-type=PKCS12
server.ssl.key-alias=alias
```

## **3. Redirect HTTP to HTTPS**

You should force redirection from HTTP to HTTPS:

- In Apache or Nginx, use a redirect rule.
- In Spring Boot, create a redirect configuration bean using Tomcat customizers.

## **4. Test Your Setup**

- Visit your domain and check the padlock icon.
- Use tools like SSL Labs to test your certificate.

## **17. What are the types of IOC containers?**

In Spring, there are two main types of IoC (Inversion of Control) containers, both of which are part of the Spring Framework and responsible for managing the lifecycle and dependencies of beans.

They are:

## **1. BeanFactory**

1. Basic container.
2. Provides lazy initialization (bean is created only when requested).
3. Lightweight, so suitable for simple applications or when memory is a concern.
4. Interface: `org.springframework.beans.factory.BeanFactory`
5. Used internally by other containers.

**Example:**

```
BeanFactory factory = new XmlBeanFactory(new FileSystemResource("beans.xml"));
```

## **2. ApplicationContext**

1. More advanced container and widely used.
2. Eagerly loads all singleton beans at startup (by default).
3. Supports internationalization, event propagation, AOP, and integration with Spring MVC.
4. Sub-interfaces include:
- `ClassPathXmlApplicationContext`
- `FileSystemXmlApplicationContext`
- `AnnotationConfigApplicationContext`
- `WebApplicationContext` (used in Spring web apps)

**Example:**

```
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```

## **18. Why dependency injection is useful?**

Dependency Injection (DI) is useful because it makes your code loosely coupled, easier to maintain, testable, and flexible.

## **1. Loose Coupling**

- Objects don’t create their dependencies; they get them from the outside.
- This reduces direct dependency and makes classes easier to change or replace.

**Without DI:**

```
Car car = new Car(); // Tight coupling
```

**With DI:**

```
@Autowired
private Car car; // Spring injects the dependency
```

## **2. Better Testability**

- You can easily pass mock objects during unit testing.

```
Car car = new MockCar(); // in test
```

## **3. Improved Maintainability**

- Changing a dependency doesn’t require changes in the dependent class.
- Updates are localized and easier to manage.

## **4. Reusability**

- Components can be reused in other contexts without rewriting or copying code.

## **5. Scalability and Configuration Flexibility**

- Dependencies can be injected based on configurations (e.g., different DBs for dev and prod).

## **19. Explain @Controller annotation.**

The `@Controller` annotation in Spring is used to mark a Java class as a web controller, which means it’s ready to handle HTTP requests in a Spring MVC web application.

## **Features:**

- It’s part of the `org.springframework.stereotype` package.
- Tells Spring to treat the class as a web layer component.
- It’s automatically detected during component scanning.
- Methods inside the class typically return view names (like a JSP or Thymeleaf template).

## **Example:**

```
@Controller
public class HomeController {

@RequestMapping("/home")
    public String showHomePage() {
        return "home"; // View name, resolved to home.jsp or home.html
    }
}
```

## **Working:**

1. Spring Boot auto-scans `@Controller` classes.
2. Maps incoming HTTP requests (e.g., `/home`) to controller methods.
3. Returns the view name to a ViewResolver to generate the final HTML.

**20. What are the differences between @Controller and `@RestController?`**

![](https://df5byh02ambd3x.archive.ph/0meNk/f67e723ea65c4e6d162ee5ddd344ebcc3c2eaa01.webp)

## **21. Explain @RequestMapping annotation.**

The `@RequestMapping` annotation in Spring is used to map web requests to specific handler methods in controller classes.

It tells Spring which URL path, HTTP method, and optionally headers, parameters, and content types a method should respond to.

## **Basic Usage:**

```
@RequestMapping("/hello")
public String hello() {
    return "hello"; // returns view name
}
```

## **Attributes:**

![](https://df5byh02ambd3x.archive.ph/0meNk/3fddfbd75898b22d788cc50934ec59b70b54be04.webp)

## **Example:**

```
@RequestMapping(value = "/user", method = RequestMethod.GET, params = "id")
public String getUser(@RequestParam int id) {
    // fetch user logic
    return "user";
}
```

## **Modern Alternatives:**

In Spring 4+, you can use more specific annotations:

- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@DeleteMapping`

They are just shortcuts for `@RequestMapping(method = ...)`

# **TCS Java Developer Interview — 3**

## For 4+ Years of Experience

**For context, he has over 4 years of experience in Java, Spring Boot, Microservices, and related technologies.**

I’ll break this down in 2 parts:

1. Interview Process
2. Interview Questions

This is how it went:

# **1. Interview Process:**

The process was smooth, just as you’d expect from a top-tier company like TCS.

- He applied through a job post on LinkedIn.
- The TCS HR team reached out to schedule the interview.
- After sharing the required details, the interview was scheduled for few days later.

On the day of the interview:

- The interviewer joined the call on time.
- They exchanged pleasantries and got straight into technical questions.
- Both the HR and the interviewer were professional and courteous throughout.

# **2. Interview Questions:**

Below are some of the technical questions he was asked. I’ve merged similar questions and follow-up queries for clarity.

I’ll include textbook explanations for all the answers to help anyone preparing for interviews.

## **1. How to create a thread? What is the most recommended way to create a thread?**

There are multiple ways to create a thread, but some methods are more efficient and easier to manage than others.

## **1. By Extending the `Thread` Class**

This is one of the oldest ways to create a thread. You extend the `Thread` class and override its `run()` method.

**Example:**

```
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running!");
    }
}
public class Main {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();  // Starts the thread and calls run()
    }
}
```

**Drawbacks:**

- You can’t extend any other class (Java supports only single inheritance).
- Not very flexible for complex tasks.

## **2. By Implementing the `Runnable` Interface**

This is a **recommended** approach, as it gives you more flexibility. You implement the `Runnable` interface and define the `run()` method.

**Example:**

```
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread is running!");
    }
}

public class Main {
    public static void main(String[] args) {
        MyRunnable myRunnable = new MyRunnable();
        Thread t1 = new Thread(myRunnable);
        t1.start();  // Starts the thread and calls run()
    }
}
```

Why Runnable is better:

- You can extend other classes (since `Runnable` is an interface).
- More flexible (can be used in `ExecutorService`, for example).

## **3. Using the `ExecutorService` (Modern and Most Recommended)**

This is part of the java.util.concurrent package and is **the most recommended** way for managing threads, especially for larger applications.

It provides a higher-level replacement for managing thread pools, scheduling tasks, and shutting down threads.

**Example:**

```
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);  // Thread pool with 2 threads
        executor.submit(() -> {
            System.out.println("Thread is running using ExecutorService!");
        });
        executor.shutdown();
    }
}
```

Why **ExecutorService** is best:

- **Thread pooling**: It handles a pool of threads, so you don’t need to manage them manually.
- **Scalability**: Great for handling large numbers of concurrent tasks.
- **Easy to shut down**: Gracefully manage thread lifecycles.

## **Most Recommended Way:**

- `ExecutorService` (via `Executors.newFixedThreadPool()` or similar) is the most modern and efficient way to create and manage threads in Java.
- `Runnable` is a good option if you need more control or have simpler use cases.
- `Thread` subclassing is mostly avoided now due to its limited flexibility.

## **2. What is a deadlock and How can it be avoided?**

A deadlock is a situation where two or more threads are blocked forever, each waiting for the other to release a lock.

**Think of it like this:**

- Thread A has Lock 1, and wants Lock 2.
- Thread B has Lock 2, and wants Lock 1.
- Both are stuck. No one moves. This is deadlock.

## **Example:**

```
class DeadlockDemo {
    private final Object lock1 = new Object();
    private final Object lock2 = new Object();

    public void methodA() {
        synchronized(lock1) {
            System.out.println("Thread A: Holding lock1...");
            try { Thread.sleep(100); } catch (Exception e) {}
            synchronized(lock2) {
                System.out.println("Thread A: Holding lock2...");
            }
        }
    }
    public void methodB() {
        synchronized(lock2) {
            System.out.println("Thread B: Holding lock2...");
            try { Thread.sleep(100); } catch (Exception e) {}
            synchronized(lock1) {
                System.out.println("Thread B: Holding lock1...");
            }
        }
    }
}
```

Run `methodA()` in one thread and `methodB()` in another → deadlock risk.

## **How to Avoid Deadlock:**

1. **Lock ordering:** Always acquire locks in the same order across all threads.
2. **Try-and-timeout using `tryLock()` (from `ReentrantLock`)**: Avoid blocking forever – back off if lock isn’t acquired.

```
if (lock1.tryLock(100, TimeUnit.MILLISECONDS))
  {
  if (lock2.tryLock(100, TimeUnit.MILLISECONDS))
    {
    // safe code
     }
}
```

**3. Minimize lock scope:** Keep synchronized blocks small and specific.

**4. Avoid nested locks if not needed:** Don’t lock inside a lock unless you absolutely have to.

**5. Use concurrency utilities** **like `java.util.concurrent.locks:`**They give more control than plain `synchronized`.

## **3. Explain different states of a thread.**

Below are main states of threads, and understanding them is key to mastering multithreading:

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/95980f8e98ca3b0208ca4bc3e187529182aafac5.webp)

## **4. Once a thread is terminated, can we restart a thread?**

No, once a thread is terminated, it cannot be restarted.

In Java, a thread goes through several states:

```
NEW → RUNNABLE → RUNNING → TERMINATED
```

Once it reaches TERMINATED, it’s dead. The thread object can’t be started again using `.start()` — doing so throws an exception.

## **Example:**

```
Thread t = new Thread(() -> System.out.println("Running"));
t.start();       // First start is fine
t.join();        // Wait for it to finish
t.start();       // IllegalThreadStateException
```

**5. What are the differences between throw vs throws?**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/e5f2acf5eeb60275cd7c6cc7b8c3fc69fd8792eb.webp)

## **6. What are the types of Exceptions in Java?**

Java exceptions fall into two main categories under the `Throwable` class:

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/fbe5ea0811ead2206dc1d4f1e581766a1474b6b5.webp)

```
Throwable
├── Exception         --> Recoverable issues
│   ├── Checked       --> Must handle (compile-time)
│   └── Unchecked     --> Runtime exceptions (optional to handle)
└── Error             --> Unrecoverable issues (like JVM crash)
```

## **1. Checked Exceptions (Compile-Time)**

These must be either caught or declared in the method signature using `throws`.**Examples:**

- `IOException`
- `SQLException`
- `FileNotFoundException`
- `ParseException`

```
public void readFile() throws IOException {
    FileReader fr = new FileReader("file.txt");
}
```

## **2. Unchecked Exceptions (Runtime)**

These are not checked at compile-time. They’re due to logic errors or bad data.**Examples:**

- `NullPointerException`
- `ArrayIndexOutOfBoundsException`
- `ArithmeticException`
- `IllegalArgumentException`

```
int x = 10 / 0; // ArithmeticException
```

## **3. Errors (System-level, serious issues)**

You shouldn’t handle these in code. They indicate critical failures like memory issues.**Examples:**

- `StackOverflowError`
- `OutOfMemoryError`
- `VirtualMachineError`

```
public void recursive() {
    recursive(); // StackOverflowError
}
```

## **7. Explain try-with-resource in Java.**

`try-with-resources` is a try block that automatically closes resources (like files, streams, DB connections) once you're done using them.

## **Syntax:**

```
try (ResourceType resource = new ResourceType()) {
    // Use the resource
} catch (Exception e) {
    // Handle exceptions
}
```

- No need for finally block
- Resource is closed automatically
- Resource must implement `AutoCloseable` (or `Closeable`)

## **Example:**

```
import java.io.*;

public class TryWithResourcesExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
            String line = br.readLine();
            System.out.println(line);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

- No need to manually close `br`.
- Even if an exception occurs, it’ll still be closed properly.

## **Usefulness:**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/3455cb09d2474d684edfb852dca9ec63eb7f9ddc.webp)

## **Resource Types:**

Any class that implements **`AutoCloseable`** or **`Closeable`** (like `FileReader`, `BufferedReader`, `Connection`, etc.)

**8. What are the differences between == vs .equals() method?**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/0e89a6d6a3b1f2001983a0df660c6a5cc7fd096f.webp)

## **9. What are the differences between Abstract class vs Interface. Also, Explain when to use what?**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/0fe0cf1eb078de68b4897d533b494bcc86150a30.webp)

## **Use Abstract Class when:**

- You want to share code (implementation) between several related classes.
- You need non-static, non-final fields.
- You expect that future versions of your class hierarchy might change the shared logic.
- You’re building a template pattern, where some methods are implemented and others are abstract.

**Example:**

```
public abstract class Animal {
    public void eat() {
        System.out.println("Eating...");
    }
    public abstract void makeSound();
}
```

## **Use Interface when:**

- You want to define a contract that multiple unrelated classes can implement.
- You want to achieve multiple inheritance of types.
- You need to ensure a class must implement certain behavior, regardless of hierarchy.
- You’re working with API design, where you expose capabilities but not logic.

**Example:**

```
public interface Flyable {
    void fly();
}
```

## **10. What is Dependency Injection and How does SpringBoot support it?**

Dependency Injection is a design pattern used to implement Inversion of Control (IoC).

It allows a class to receive its dependencies from external sources, rather than creating them itself.

This makes your code:

- Loosely coupled
- Easier to test
- More maintainable

## **Types:**

Spring Boot (and Spring Framework) supports three types of DI:

**1. Constructor Injection (Best Practice):**

```
@Component
public class Car {
    private final Engine engine;

@Autowired
    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

- Injects dependencies via the constructor.
- Immutable and great for unit testing.
- Spring Boot 2.6+ doesn’t even need `@Autowired` here if there's only one constructor!

**2. Setter Injection:**

```
@Component
public class Car {
    private Engine engine;

@Autowired
public void setEngine(Engine engine) {
        this.engine = engine;
    }
}
```

- Injects via a setter method.
- Useful when the dependency is **optional** or can change after object creation.

**3. Field Injection (Not Recommended for production):**

```
@Component
public class Car {
    @Autowired
    private Engine engine;
}
```

- Shortest, but hard to test, and tightly couples your code with Spring.
- Not ideal for clean code or testing.

## **How Spring Boot Supports Dependency Injection:**

Spring Boot builds on Spring’s IoC container, which:

1. Scans your application for `@Component`, `@Service`, `@Repository`, and `@Controller` classes.
2. Registers them as beans in the ApplicationContext.
3. Automatically injects the required dependencies into beans using annotations like `@Autowired`, `@Inject`, or constructor-based DI.

## **Working:**

- Spring Boot uses Component Scanning (`@ComponentScan`) to detect and register beans.
- Dependency injection is handled by the Spring IoC container.
- You can define beans manually using `@Bean` inside a `@Configuration` class too.

```
@Configuration
public class AppConfig {
    @Bean
    public Engine engine() {
        return new Engine();
    }
}
```

## **Benefits:**

- Encourages modular, testable code
- Avoids hard-coded dependencies
- Enables easy mocking of components in unit tests
- Clean separation of concerns
- Reduces boilerplate

## **11. What is Circular Dependency and How does SpringBoot handle it?**

A circular dependency occurs when two or more beans depend on each other, either directly or indirectly, in such a way that it creates a loop.

This leads to a situation where Spring cannot resolve the dependencies and inject them properly.

Circular dependencies can be problematic because they create an infinite loop of dependency resolution, causing the Spring context to fail to initialize.

**For example:**

- Bean A depends on Bean B.
- Bean B depends on Bean A.

This circular reference makes it impossible for Spring to figure out which bean should be created first.

## **How Spring Boot Handles Circular Dependencies:**

Spring Boot (and the underlying Spring Framework) provides a few mechanisms to handle circular dependencies:

## **1. Setter Injection**

- Setter injection is one of the easiest ways to resolve circular dependencies. When a circular dependency is detected, Spring Boot can resolve it by using setter-based injection.
- With setter injection, Spring can instantiate the beans and then inject their dependencies using setters after both beans are created. This avoids the problem of circular references during bean creation.

**Example:**

```
@Component
public class A {
    private B b;

@Autowired
    public void setB(B b) {
        this.b = b;
    }
}
@Component
public class B {
    private A a;
    @Autowired
    public void setA(A a) {
        this.a = a;
    }
}
```

Here, Spring Boot will create both beans first and inject the dependencies using setters after instantiation, resolving the circular reference.

## **2. Using `@Lazy` Annotation**

- Spring also provides the `@Lazy` annotation to resolve circular dependencies.
- The `@Lazy` annotation tells Spring to initialize a bean only when it is actually needed (lazy initialization). This can help resolve the circular dependency by delaying the creation of one of the beans until the other is fully created.

**Example:**

```
@Component
public class A {
    private B b;

@Autowired
public A(@Lazy B b) {
        this.b = b;
    }
}
@Component
public class B {
    private A a;
    @Autowired
    public B(@Lazy A a) {
        this.a = a;
    }
}
```

By using `@Lazy`, Spring Boot defers the instantiation of one of the beans, allowing it to avoid the circular dependency at startup.

## **3. Constructor Injection (Potential Issue)**

- Constructor injection is the most preferred way in Spring because it promotes immutability and ensures that dependencies are provided at the time of bean creation.
- However, with circular dependencies, constructor injection can create issues. Since both beans need each other to be instantiated, it creates a deadlock.
- To resolve this, Spring will not allow circular dependencies with constructor injection by default and will throw an exception (`BeanCurrentlyInCreationException`).

**Example of the issue**:

```
@Component
public class A {
    private B b;

    @Autowired
    public A(B b) {
        this.b = b;
    }
}
@Component
public class B {
    private A a;
    @Autowired
    public B(A a) {
        this.a = a;
      }
}
```

This will cause a circular dependency and Spring will fail to start the application with an error like:

```
org.springframework.beans.factory.BeanCurrentlyInCreationException: Error creating bean with name 'A'
```

## **4. ApplicationContextAware or Programmatic Lookup**

- As a last resort, if you can’t resolve the circular dependency via DI (Dependency Injection), you can inject the `ApplicationContext` and look up beans programmatically.
- This is generally not recommended, as it couples your beans to the Spring container and defeats the purpose of DI, but it can help in some complex scenarios.

**Example:**

```
@Component
public class A implements ApplicationContextAware {
    private B b;

@Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.b = applicationContext.getBean(B.class);
    }
}
@Component
public class B {
    private A a;
    @Autowired
    public B(A a) {
        this.a = a;
    }
}
```

## **How to Avoid Circular Dependencies in Spring Boot:**

While Spring Boot provides ways to handle circular dependencies, they should generally be avoided because they can lead to a more complex and fragile application architecture. Here are a few best practices to avoid circular dependencies:

1. **Refactor the code**: Often, circular dependencies are a sign that the design needs to be revisited. Try to refactor the classes to avoid direct dependencies.
2. **Use interfaces**: Introduce interfaces and apply the Dependency Inversion Principle (DIP) to decouple classes.
3. **Use event-driven architecture**: Sometimes, introducing an event-driven approach can help break the circular dependency cycle.
4. **Split responsibilities**: Divide classes into smaller, more cohesive units so that dependencies are minimized.

**12. What are the differences between CRUD Repository vs JPA Repository?**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/cc9edbb4a23f1b353ca125ce232bb5e0c6dd6c2a.webp)

## **13. What are some best practices for tuning performance of your SpringBoot application?**

Tuning the performance of a Spring Boot application is crucial to ensure it handles high loads efficiently, minimizes resource consumption, and delivers faster responses. Here are some best practices you can follow:

## **1. Use Connection Pooling**

- Instead of creating a new connection for each database interaction, use connection pooling.
- Spring Boot supports this with libraries like HikariCP (which is the default in Spring Boot 2.x).
- This reduces the overhead of establishing new database connections.
- **Configuration Example:**

```
spring.datasource.hikari.maximum-pool-size=10
spring.datasource.hikari.connection-timeout=30000
```

## **2. Enable HTTP/2**

- HTTP/2 improves the performance of web applications by enabling multiplexing (multiple requests in a single connection), header compression, and stream prioritization.
- **Configuration Example:**

```
server.http2.enabled=true
```

## **3. Optimize Caching**

- Use caching to reduce unnecessary database calls and improve response times.
- Spring Boot provides integration with caching solutions like EhCache, Redis, and Caffeine.
- **Enable Cache:**

```
@EnableCaching
```

## **4. Profile Database Queries**

- Use tools like Spring Data JPA’s Query Log, Hibernate’s SQL logging, or Query Performance Analyzer to monitor and optimize slow queries.
- **Configuration Example:**

```
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.properties.hibernate.use_sql_comments=true
```

## **5. Asynchronous Processing**

- Make use of asynchronous processing for long-running tasks.
- Spring provides the `@Async` annotation to execute tasks in a separate thread, improving the responsiveness of the application.
- **Example:**

```
@Async
public Future<String> processTask()
{
  // long-running task
}
```

## **6. Enable Gzip Compression**

- Enable Gzip compression for HTTP responses to reduce the size of data sent to the client, improving load times.
- **Configuration Example:**

```
server.compression.enabled=true
server.compression.mime-types=text/html,text/xml,application/json
```

## **7. Optimize Spring Boot’s Auto-Configuration**

- Spring Boot automatically configures beans based on the project’s classpath. This can be inefficient if you don’t need certain configurations.
- You can exclude unnecessary auto-configurations using `@EnableAutoConfiguration(exclude = { … })` or by specifying properties in `application.properties`.
- **Example:**

```
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
```

## **8. Monitor with Actuator**

- Use Spring Boot Actuator to monitor the health and performance of your application in real time.
- It provides useful endpoints to track metrics, health checks, and more.
- **Enable:**

```
management.endpoints.web.exposure.include=health,metrics,info
```

## **9. Use the Right Garbage Collection Algorithm**

- The choice of Garbage Collection (GC) algorithm can significantly affect the performance of a Java application.
- For high-performance, low-latency applications, consider using G1GC or ZGC.
- **Example:**

```
-XX:+UseG1GC
```

## **10. Profile and Optimize Code**

- Use tools like Spring Boot DevTools, JProfiler, or VisualVM to monitor JVM performance, memory usage, thread states, and database connections.
- Regularly profile your application for hotspots and refactor code that consumes excessive resources.

## **11. Limit the Size of HTTP Requests and Responses**

- Set size limits on HTTP requests to prevent large payloads from overwhelming the server and impacting performance.
- **Example:**

```
server.tomcat.max-http-post-size=10485760
```

## **12. Use Content Delivery Networks (CDNs)**

- Offload static resources (images, CSS, JavaScript) to a CDN to reduce the load on your server and improve client-side performance.

## **13. Tune the JVM Heap Size**

- Properly set the heap size for your application based on your workload and available resources. This can prevent excessive garbage collection pauses and out-of-memory errors.
- **Example:**

```
-Xmx2g -Xms2g
```

## **14. Use Spring Profiles for Environment-specific Configurations**

- Use Spring Profiles to define different configurations for different environments (e.g., development, testing, production). This allows for optimized configurations in production while retaining flexibility during development.

## **15. Thread Pool and Concurrency Tuning**

- If your application processes tasks asynchronously or in parallel, fine-tune your thread pools to handle the correct number of threads based on your hardware resources and workload.
- **Example:**

```
spring.task.execution.pool.core-size=5
spring.task.execution.pool.max-size=20
```

## **16. Leverage Distributed Tracing**

- For microservices-based architectures, use distributed tracing solutions like Spring Cloud Sleuth to monitor the flow of requests across services and identify bottlenecks.

## **14. How would you divide your monolithic application into a microservice application?**

Dividing a monolithic application into microservices is a complex task that needs strategy, patience, and a deep understanding of the current system.

Here’s how we can go about it step by step:

## **1. Understand the Monolith Thoroughly**

Before we split anything:

- Identify modules, components, and responsibilities.
- Map dependencies between modules (data, logic, communication).
- Understand domain boundaries (use Domain-Driven Design if possible).

**Tools:** Use static code analyzers, dependency graphs, and architecture diagrams.

## **2. Identify Bounded Contexts / Domains**

This is crucial. We want to slice our app along business capabilities.

**For example:**

- In an e-commerce app: `Order`, `Customer`, `Product`, `Inventory`, and `Shipping` can be separate domains.
- Use DDD (Domain Driven Design) to define Bounded Contexts — these become your candidate microservices.

## **3. Choose the First Service to Extract**

Start small. Pick:

- A low-risk, well-understood, and loosely coupled module.
- Something that provides clear business value and can be deployed independently (e.g., `User Profile`, `Notification`, or `Authentication`).

## **4. Define APIs and Contracts**

Microservices need to talk to each other via APIs:

- Define REST, GraphQL, or gRPC contracts.
- Use OpenAPI/Swagger for documentation.
- Ensure backward compatibility for smooth migration.

## **5. Extract the Module**

- Pull the selected functionality into a new project.
- Migrate its data if necessary, or start with shared database/table (temporarily).
- Rewire the monolith to call the service via API instead of local method calls.

## **6. Set Up Infrastructure Essentials**

- Service registry (like Consul, Eureka).
- API Gateway (like Kong, Zuul, Spring Cloud Gateway).
- Centralized configuration (e.g., Spring Cloud Config, Consul).
- Logging (e.g., ELK stack, Fluentd, Grafana Loki).
- Monitoring and tracing (Prometheus, Jaeger, Zipkin).

## **7. Deploy and Test the Service Independently**

- CI/CD pipeline per microservice.
- Containerize (Docker), and use orchestration (Kubernetes, ECS).
- Test integration with the rest of the system.

## **8. Repeat Iteratively**

- Keep extracting services one by one.
- Gradually reduce the monolith’s responsibilities.
- Eventually, the monolith becomes a **thin shell**, or gets retired.

## **Pitfalls to Avoid:**

- **Premature decomposition** — don’t split before understanding boundaries.
- **Too fine-grained services** — leads to high inter-service communication cost.
- **Data inconsistency** — use eventual consistency and domain events.
- **Overcomplicating with orchestration** — prefer choreography where possible.

**15. What are the differences between Synchronous vs Asynchronous communication in microservices?**

![](https://d6ncjpxdq5d5dm.archive.ph/9JBXy/ec4f978fcd3ee279b3bc9b3bcb52098ea9410e6a.webp)

## **16. Write a program to find the list of unique words from a sentence?**

```
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class UniqueWordsFinder {
    public static void main(String[] args) {
        String sentence = "Java is simple and Java is powerful";
        // Convert sentence to lower case, split into words, filter distinct and collect
        List<String> uniqueWords = Stream.of(sentence.toLowerCase().split("\\s+"))
                                         .distinct()
                                         .collect(Collectors.toList());
        System.out.println("Unique words: " + uniqueWords);
    }
}
```

## **Output:**

For the input sentence:

```
Java is simple and Java is powerful
```

Output will be:

```
Unique words: [java, is, simple, and, powerful]
```

# **Java Code Based Tricky Interview Questions — 5**

## **1. If the `userService` is up but returns HTTP 500 for some IDs, will the fallback be triggered?**

```
@FeignClient(name = "userService", fallback = UserFallback.class)
public interface UserClient {
    @GetMapping("/user/{id}")
    User getUser(@PathVariable String id);
}
```

## **Answer:**

- **Not necessarily** — fallback behavior depends on the circuit breaker mechanism used.
- By default, Feign with Hystrix or Resilience4j triggers fallbacks for certain exceptions.
- In Hystrix, HTTP 500 typically triggers fallback because it throws a runtime `FeignException`.
- In Resilience4j, you may need to explicitly configure which exceptions trigger the fallback.
- Ensure that the circuit breaker library is properly configured (e.g., Resilience4j setup in `application.yml`).
- In your fallback class, consider handling specific exceptions like `FeignException.InternalServerError` if needed.

## **2. What issues might arise under concurrent access?**

```
@RestController
public class CounterController {
    private int counter = 0;

@GetMapping("/increment")
    public int increment() {
        return counter++;
    }
}
```

## **Answer:**

- The `counter++` operation is not thread-safe.
- Under concurrent access, race conditions can occur, leading to inconsistent or incorrect counter values.
- To handle this, use thread-safe constructs like `AtomicInteger` or synchronize the method.

## **3. Why might “LazyService initialized” not print during application startup?**

```
@Service
@Lazy
public class LazyService {
    public LazyService() {
        System.out.println("LazyService initialized");
    }
}
```

## **Answer:**

- The `@Lazy` annotation delays bean initialization until it's needed.
- If `LazyService` is never injected or called, it won't be initialized, and the constructor message won't print.

## **4. Design a microservice to handle uploading large files (e.g., 100MB+) with high concurrency.**

## **Answer:**

**1. Stream the file instead of loading it into memory:**

Avoid loading the entire file into memory by using streaming:

```
@RestController
public class FileUploadController {

@PostMapping("/upload")
    public ResponseEntity<String> handleUpload(@RequestParam("file") MultipartFile file) throws IOException {
        try (InputStream inputStream = file.getInputStream()) {
            // Stream to cloud storage or disk
            Files.copy(inputStream, Paths.get("/tmp/" + file.getOriginalFilename()), StandardCopyOption.REPLACE_EXISTING);
        }
        return ResponseEntity.ok("File uploaded successfully");
    }
}
```

**2. Use Amazon S3 Presigned URLs for direct client upload:**

Offload the file transfer from your app server by giving clients a secure presigned URL to upload directly to S3.

```
@Service
public class S3Service {

private final AmazonS3 s3Client = AmazonS3ClientBuilder.defaultClient();
    public String generatePresignedUrl(String filename) {
        Date expiration = new Date(System.currentTimeMillis() + 1000 * 60 * 10); // 10 mins
        GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest("your-bucket", filename)
                .withMethod(HttpMethod.PUT)
                .withExpiration(expiration);
        return s3Client.generatePresignedUrl(request).toString();
    }
}
```

Client can then use a simple `PUT` to upload directly to S3.

**3. Send file metadata to a queue for asynchronous processing:**

Use RabbitMQ or Kafka to decouple file processing from the upload logic.

```
@Service
public class UploadMetadataPublisher {

@Autowired
    private RabbitTemplate rabbitTemplate;
    public void publishMetadata(FileMetadata metadata) {
        rabbitTemplate.convertAndSend("file-upload-exchange", "file.upload.routingKey", metadata);
    }
}
```

Where `FileMetadata` might be a simple POJO with details like filename, user, upload time, etc.

**4. Use Spring WebFlux for better scalability (non-blocking I/O):**

Reactive programming helps handle thousands of concurrent requests efficiently:

```
@RestController
public class ReactiveUploadController {

@PostMapping(value = "/upload-reactive", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public Mono<String> upload(@RequestPart("file") FilePart filePart) {
        return filePart.transferTo(Paths.get("/tmp/" + filePart.filename()))
                       .thenReturn("Reactive upload complete");
    }
}
```

This ensures no thread is blocked while uploading large files.

**5. Implement backpressure and resilience:**

To prevent overload during high concurrency:

- Use Resilience4j to configure rate limiting and backpressure.
- Add `RateLimiter`, `Bulkhead`, or `CircuitBreaker`.

Example (in `application.yml`):

```
resilience4j.ratelimiter:
  instances:
    fileUploadLimiter:
      limitForPeriod: 100
      limitRefreshPeriod: 1s
      timeoutDuration: 500ms
```

Apply it via annotations or programmatically using decorators.

## **5. With a circuit breaker configured as follows:**

```
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)
    .slidingWindowSize(5)
    .build();
```

## **If 3 out of 5 calls fail, what happens?**

## **Answer:**

- The failure rate is 60%, exceeding the 50% threshold. The circuit breaker will open, preventing further calls until it transitions to half-open after a wait duration.

## **6. Are `withdraw()` and `deposit()` methods transactional?**

```
@Service
public class BankService {
    @Transactional
    public void transfer() {
        withdraw();
        deposit();
    }

@Transactional
    public void withdraw() { ... }
    @Transactional
    public void deposit() { ... }
}
```

## **Answer:**

- **No.** Internal method calls within the same class bypass Spring’s proxy mechanism, so `@Transactional` annotations on `withdraw()` and `deposit()` won't be effective.
- To ensure transactional behavior, these methods should be in separate beans.

## **7. How can you implement per-user rate limiting in a distributed microservices environment?**

## **Answer:**

- Use a distributed cache like Redis to track request counts per user.
- Implement algorithms like Token Bucket or Leaky Bucket.
- Use Redis commands like `INCR` with expiration to count requests.
- Employ libraries like Bucket4j or integrate with API gateways that support rate limiting.

**Example**

```
@Service
public class RateLimiterService {

@Autowired
    private StringRedisTemplate redisTemplate;
    private static final int MAX_REQUESTS = 100;
    private static final Duration WINDOW_DURATION = Duration.ofMinutes(1);
    public boolean isAllowed(String userId) {
        String key = "rate_limit:" + userId;
        Long count = redisTemplate.opsForValue().increment(key);
        if (count == 1) {
            // Set TTL only when key is first created
            redisTemplate.expire(key, WINDOW_DURATION);
        }
        return count <= MAX_REQUESTS;
    }
}
```

## **8. What happens when an exception is thrown?**

```
@KafkaListener(topics = "orders")
public void listen(String message) {
    throw new RuntimeException("Processing failed");
}
```

## **Answer:**

- The message processing fails, and the offset isn’t committed. Kafka will retry the message delivery, potentially leading to repeated failures.
- To handle this, implement error handling strategies like Dead Letter Topics (DLT) or configure retry policies.

## **9. Why might this Dockerfile fail during build?**

```
FROM openjdk:17
COPY target/app.jar app.jar
CMD ["java", "-jar", "app.jar"]
```

## **Answer:**

- If `target/app.jar` doesn't exist or is misnamed, the `COPY` command will fail.
- Ensure that the JAR file is correctly built and the path is accurate. Alternatively, use a wildcard:

```
COPY target/*.jar app.jar
```

**10. Implement a simple round-robin load balancer in Java.
Answer:**

```jsx
public class RoundRobinLoadBalancer {
    private List<String> servers = List.of("http://s1", "http://s2", "http://s3");
    private AtomicInteger index = new AtomicInteger(0);

public String getNextServer() {
        return servers.get(index.getAndUpdate(i -> (i + 1) % servers.size()));
    }
}
```

## **11. Why does “Attempting…” print only once?**

```
RetryTemplate template = new RetryTemplate();
template.execute(context -> {
    System.out.println("Attempting...");
    throw new RuntimeException("Failure");
});
```

## **Answer:**

- Without a configured `RetryPolicy`, `RetryTemplate` defaults to a single attempt.
- To enable retries, set a `RetryPolicy`:

```
template.setRetryPolicy(new SimpleRetryPolicy(3));
```

## **12. How do you implement rollback in a Saga pattern using orchestration?**

## **Answer:**

- Use a central orchestrator to manage the sequence of service calls.
- If a step fails, the orchestrator invokes compensating transactions for previous steps.
- For example, if payment processing fails, the orchestrator triggers a refund or order cancellation.

## **13. Why might this call hang longer than expected?**

```
RestTemplate restTemplate = new RestTemplateBuilder()
    .setConnectTimeout(Duration.ofSeconds(1))
    .build();

restTemplate.getForObject("http://slow-service.com", String.class);
```

## **Answer:**

- Only the connection timeout is set. The read timeout isn’t configured, so the call may hang during data retrieval.
- Set the read timeout as well:

```
.setReadTimeout(Duration.ofSeconds(1))
```

## **14.Which thread runs this?**

```
@GetMapping("/async")
public CompletableFuture<String> go() {
    return CompletableFuture.supplyAsync(() -> Thread.currentThread().getName());
}
```

## **Answer:**

- Runs in ForkJoinPool.commonPool. Not the servlet thread.
- **For control:** use a custom Executor:

```
Executors.newFixedThreadPool(10)
```

**15. Write Redis-based distributed lock logic for a scheduled task.
Answer:**

```jsx
public boolean acquireLock(String key) {
    String val = UUID.randomUUID().toString();
    return Boolean.TRUE.equals(
        redisTemplate.opsForValue().setIfAbsent(key, val, Duration.ofSeconds(30))
    );
}

@Scheduled(fixedRate = 60000)
public void task() {
    if (acquireLock("job-lock")) {
        // safe to run task
    }
}
```

# **Java Code Based Tricky Interview Questions — 4**

## **1. You are given an array `height[]` where `height[i]` represents the elevation at position `i`. Write a function to compute how much water can be trapped after raining.**

**Input:** `[0,1,0,2,1,0,1,3,2,1,2,1]`**Expected Output:** `6`

## **Solution:**

```
public class TrappingRainWater {
    public static int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;

    while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) leftMax = height[left];
                else water += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
    public static void main(String[] args) {
        int[] heights = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.println("Trapped Water: " + trap(heights));
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(1)`

## **2. Given a string `s` containing just `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.**

**Input:** `"(()())"`**Expected Output:** `6`

## **Solution:**

```
public class LongestValidParentheses {
    public static int longestValidParentheses(String s) {
        int maxLen = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1); // base for first valid substring

    for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) stack.push(i);
                else maxLen = Math.max(maxLen, i - stack.peek());
            }
        }
        return maxLen;
    }
    public static void main(String[] args) {
        System.out.println(longestValidParentheses("(()())")); // 6
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(n)`

## **3. Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the median of the two sorted arrays in `O(log (m+n))` time.**

**Input:** `[1, 3], [2]`**Expected Output:** `2.0`

## **Solution:**

```
public class MedianSortedArrays {
    public static double findMedianSortedArrays(int[] A, int[] B) {
        if (A.length > B.length) return findMedianSortedArrays(B, A);

        int m = A.length, n = B.length;
        int low = 0, high = m;

        while (low <= high) {
            int i = (low + high) / 2;
            int j = (m + n + 1) / 2 - i;

            int maxLeftA = (i == 0) ? Integer.MIN_VALUE : A[i - 1];
            int minRightA = (i == m) ? Integer.MAX_VALUE : A[i];

            int maxLeftB = (j == 0) ? Integer.MIN_VALUE : B[j - 1];
            int minRightB = (j == n) ? Integer.MAX_VALUE : B[j];

            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                if ((m + n) % 2 == 0)
                    return ((double)Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2;
                else
                    return Math.max(maxLeftA, maxLeftB);
            } else if (maxLeftA > minRightB) {
                high = i - 1;
            } else {
                low = i + 1;
            }
        }
        throw new IllegalArgumentException();
    }

    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[]{1,3}, new int[]{2})); // 2.0
    }
}
```

**Time Complexity:** `O(log(min(m,n)))`**Space Complexity:** `O(1)`

## **4. Design an algorithm to serialize and deserialize a binary tree. You must ensure that the tree can be reconstructed exactly from the serialized string.**

## **Solution:**

```
import java.util.*;

public class Codec {
    public String serialize(TreeNode root) {
        if (root == null) return "null";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }

    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>(Arrays.asList(data.split(",")));
        return build(nodes);
    }

    private TreeNode build(Queue<String> nodes) {
        String val = nodes.poll();
        if (val.equals("null")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = build(nodes);
        node.right = build(nodes);
        return node;
    }

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int x) { val = x; }
    }

    public static void main(String[] args) {
        Codec codec = new Codec();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        String serialized = codec.serialize(root);
        TreeNode deserialized = codec.deserialize(serialized);
        System.out.println("Serialized: " + serialized);
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(n)`

## **5. Given a `beginWord`, `endWord`, and a dictionary `wordList`, return the length of the shortest transformation sequence such that:**

## **Only one letter can be changed at a time.**

## **Each transformed word must exist in the word list.**

**Input**:

```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
```

**Expected Output:** 5

**Output Explanation:**

The shortest transformation is:

```
"hit" → "hot" → "dot" → "dog" → "cog"
```

Length = 5 (number of words in sequence)

## **Solution:**

```
public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        if (!dict.contains(endWord)) return 0;

        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        int level = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                String word = queue.poll();
                char[] chars = word.toCharArray();

                for (int i = 0; i < chars.length; i++) {
                    char orig = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String next = new String(chars);
                        if (next.equals(endWord)) return level + 1;
                        if (dict.contains(next)) {
                            queue.add(next);
                            dict.remove(next);
                        }
                    }
                    chars[i] = orig;
                }
            }
            level++;
        }
        return 0;
    }
}
```

**Time Complexity:** `O(N * L^2)`**Space Complexity:** `O(N * L)`Where `N` is the number of words and `L` is word length.

## **6. Place `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all distinct solutions to the N-Queens puzzle.**

**Input:** n = 4

**Expected Output: [2 Valid Configurations]**

```
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]
```

## **Solution:**

```
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        solve(0, n, new int[n], res);
        return res;
    }

    private void solve(int row, int n, int[] pos, List<List<String>> res) {
        if (row == n) {
            List<String> board = new ArrayList<>();
            for (int i : pos) {
                char[] line = new char[n];
                Arrays.fill(line, '.');
                line[i] = 'Q';
                board.add(new String(line));
            }
            res.add(board);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isValid(row, col, pos)) {
                pos[row] = col;
                solve(row + 1, n, pos, res);
            }
        }
    }

    private boolean isValid(int row, int col, int[] pos) {
        for (int i = 0; i < row; i++) {
            if (pos[i] == col || Math.abs(pos[i] - col) == row - i) return false;
        }
        return true;
    }
}
```

**Time Complexity:** `O(N!)`**Space Complexity:** `O(N)`

## **7. Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest product and return that product.**

**Input:** nums = [2, 3, -2, 4]**Expected Output:** 6

## **Solution:**

```
public class MaxProductSubarray {
    public int maxProduct(int[] nums) {
        int max = nums[0], min = nums[0], res = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int tempMax = max;
            max = Math.max(nums[i], Math.max(nums[i] * max, nums[i] * min));
            min = Math.min(nums[i], Math.min(nums[i] * tempMax, nums[i] * min));
            res = Math.max(res, max);
        }
        return res;
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(1)`

## **8. You are given an array `nums[]` and an integer `k`. Find the maximum element in every sliding window of size `k`.**

**Input:** nums = [1,3,-1,-3,5,3,6,7], k = 3

**Expected Output:** [3,3,5,5,6,7]

## **Solution:**

```
public class SlidingWindowMax {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0 || k == 0) return new int[0];
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> dq = new LinkedList<>();

        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && dq.peek() < i - k + 1)
                dq.poll();

            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i])
                dq.pollLast();

            dq.offer(i);
            if (i >= k - 1) result[i - k + 1] = nums[dq.peek()];
        }
        return result;
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(k)`

## **9. Given a node from an undirected graph, clone the graph and return the cloned node. Each node contains a value and a list of its neighbors.**

## **Solution:**

```
class Node {
    public int val;
    public List<Node> neighbors;
    public Node(int val) {
        this.val = val;
        neighbors = new ArrayList<>();
    }
}

public class CloneGraph {
    private Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (visited.containsKey(node)) return visited.get(node);

        Node clone = new Node(node.val);
        visited.put(node, clone);
        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        return clone;
    }
}
```

**Time Complexity:** `O(n)`**Space Complexity:** `O(n)`

## **10. Implement a Trie (Prefix Tree) with three methods:**

- `insert(word)`
- `search(word)`
- `startsWith(prefix)`

## **Solution:**

```
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

public class Trie {
    private final TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null)
                node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private TrieNode searchPrefix(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx];
        }
        return node;
    }
}
```

**Time Complexity:** `O(m)` per operation (m = word length)

**Space Complexity:** O(n * m)

## **11. Implement a regular expression matching with support for `'.'` and `'*'`.**

## **`a) '.'` matches any single character.**

## **`b) '*'` matches zero or more of the preceding element.**

**Input:** s = “aab”, p = “c*a*b”**Expected Output:** true**Output Explanation:** ‘c*’ can be empty, ‘a*’ can match “aa”, and ‘b’ matches ‘b’

## **Solution:**

```
public class RegexMatch {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;

        for (int j = 1; j <= p.length(); j++) {
            if (p.charAt(j-1) == '*') dp[0][j] = dp[0][j-2];
        }

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                char sc = s.charAt(i-1), pc = p.charAt(j-1);
                if (pc == '.' || pc == sc) dp[i][j] = dp[i-1][j-1];
                else if (pc == '*') {
                    dp[i][j] = dp[i][j-2]; // zero occurrence
                    if (p.charAt(j-2) == '.' || p.charAt(j-2) == sc)
                        dp[i][j] |= dp[i-1][j];
                }
            }
        }

        return dp[s.length()][p.length()];
    }
}
```

**Time Complexity:** O(m × n)

**Space Complexity:** O(m × n)

## **12. Given a array of Strings that may contain duplicates, return all possible subsets (the power set), ensuring no duplicate subsets are returned.**

**Input:** String[] nums = {“a”, “b”, “b”};

**Expected Output:**

```
[
  [],
  ["a"],
  ["a", "b"],
  ["a", "b", "b"],
  ["b"],
  ["b", "b"]
]
```

## **Solution:**

```
public class SubsetsWithDup {
    public List<List<String>> subsetsWithDup(String[] nums) {
        Arrays.sort(nums);
        List<List<String>> res = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int start, String[] nums, List<String> temp, List<List<String>> res) {
        res.add(new ArrayList<>(temp));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i].equals(nums[i-1])) continue;
            temp.add(nums[i]);
            backtrack(i+1, nums, temp, res);
            temp.remove(temp.size()-1);
        }
    }
}
```

**Time Complexity:** O(2ⁿ × n)

**Space Complexity:** O(2ⁿ × n)

## **13.Given a string `num` that contains only digits and an integer `target`, return all possible expressions by adding the binary operators `'+'`, `'-'`, and `'*'` between digits so that the resulting expression evaluates to the target.**

**Input:**

```
String num = "123";
int target = 6;
```

**Expected Output:**

```
["1+2+3", "1*2*3"]
```

## **Solution:**

```
public class ExpressionOperators {
    public List<String> addOperators(String num, int target) {
        List<String> res = new ArrayList<>();
        backtrack(res, "", num, target, 0, 0, 0);
        return res;
    }

    private void backtrack(List<String> res, String path, String num, int target, int pos, long eval, long multed) {
        if (pos == num.length()) {
            if (eval == target) res.add(path);
            return;
        }

        for (int i = pos; i < num.length(); i++) {
            if (i != pos && num.charAt(pos) == '0') break;
            long curr = Long.parseLong(num.substring(pos, i + 1));
            if (pos == 0) {
                backtrack(res, path + curr, num, target, i + 1, curr, curr);
            } else {
                backtrack(res, path + "+" + curr, num, target, i + 1, eval + curr, curr);
                backtrack(res, path + "-" + curr, num, target, i + 1, eval - curr, -curr);
                backtrack(res, path + "*" + curr, num, target, i + 1, eval - multed + multed * curr, multed * curr);
            }
        }
    }
}
```

**Time Complexity:** O(4ⁿ )

**Space Complexity:** O(4ⁿ * n)

# **Java Code Based Tricky Interview Questions — 3**

## **1. What will be the output of the following code?**

```
interface A {
    int X = 10;
}
class B implements A {
    static int X = 20;
}
public class Main {
    public static void main(String[] args) {
        System.out.println(A.X);
        System.out.println(B.X);
    }
}
```

## **Answer**

```
10
20
```

- **Interfaces store variables as `public static final`**, meaning `A.X` is a constant.
- `B.X` **hides** `A.X`, but doesn't override it.

## **2. What will be the output of the following code?**

```
import java.util.concurrent.*;
public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(1);
        executor.submit(() -> System.out.println(Thread.currentThread().getName()));
        executor.submit(() -> System.out.println(Thread.currentThread().getName()));
        executor.shutdown();
    }
}
```

## **Answer**

```
pool-1-thread-1
pool-1-thread-1
```

- **Thread pools reuse threads**, so both tasks run on the same thread.

## **3. Why does the following never terminate?**

```
class A {
    private static boolean flag = true;

    public static void main(String[] args) {
        new Thread(() -> {
            while (flag) { }
        }).start();
        flag = false;
    }
}
```

## **Answer**

JVM optimizes the loop by caching `flag`, so the change is never seen by the thread.**Fix**: Use `volatile` → `private static volatile boolean flag = true;`

## **4. What will be the output?**

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(List.of(10, 5, 20));
        System.out.println(pq.poll());
    }
}
```

## **Answer**

Runtime Error (`UnsupportedOperationException`) due to List.of() being immutable.

- `List.of(10, 5, 20)` creates an **immutable list**.
- `PriorityQueue<>(List.of(10, 5, 20))` **compiles successfully**, but it tries to **modify** the list internally.
- Since `List.of()` creates an **unmodifiable** list, it throws **`UnsupportedOperationException` at runtime**.

## **5. Predict the output:**

```
public class Main {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer x = 128, y = 128;

        System.out.println(a == b);
        System.out.println(x == y);
    }
}
```

## **Answer**

```
true
false
```

- `Integer` values **from -128 to 127** are cached, so `a == b` is **true**.
- `x == y` compares two different objects.

## **6. Will transactions work in this code?**

```
@Service
public class MyService {
    @Async
    @Transactional
    public void doSomething() {
        // DB Operation
    }
}
```

## **Answer**

**Transaction will not work!**

- `@Async` runs in a **different thread**, so the original transaction is **lost**.
- **Fix**: Use **TransactionSynchronizationManager**

## **7. Why does this code always return the same prototype bean?**

```
@Component
class A {
    @Autowired
    private B b;
}
@Component
@Scope("prototype")
class B { }
```

## **Answer**

- Spring injects dependencies at startup, so the same instance of `B` is injected every time.
- **Fix**: Use `ObjectFactory<B>` or `Provider<B>`.

## **8. What happens if the fallback method itself fails in `@CircuitBreaker`?**

```
@CircuitBreaker(name = "myService", fallbackMethod = "fallback")
public String callService() {
    throw new RuntimeException("Service Down");
}
public String fallback(Throwable t) {
    throw new RuntimeException("Fallback Failed!");
}
```

## **Answer**

**Unrecoverable failure.**

- The entire request **fails**, causing **cascading failures**.
- **Fix**: Return a **default response** in the fallback.

## **9. What will be the output of below code?**

```
public class Main {
    String str = "Hello";
    {
        str = null;
    }
    public static void main(String[] args) {
        Main obj = new Main();
        System.out.println(obj.str.length());
    }
}
```

## **Answer**

**NullPointerException**

- The instance initializer block `{ str = null; }` executes **before** the constructor.
- By the time `str.length()` runs, `str` is `null`.

## **10. What will be the output of below code?**

```
public class Main {
    public static void main(String[] args) {
        System.out.println("String[] main");
    }
public static void main(Object args) {
        System.out.println("Object main");
    }
}
```

## **Answer**

```
String[] main
```

- The JVM only calls `main(String[] args)`, ignoring `main(Object args)`.

## **11. What will be the output of below code?**

```
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.put(null, "NullValue");
        map.put(1, "NewOne");
        System.out.println(map.size() + " " + map.get(null));
    }
}
```

## **Answer**

```
2 NullValue
```

- `map.put(1, "NewOne")` **overwrites** the previous key.
- `null` is a valid key in `HashMap`.

## **12. What will be the output of below code?**

```
public class Main {
    static int count = 0;
    public static void main(String[] args) {
        new Thread(() -> {
            while (count < 5) {
                System.out.print(count);
            }
        }).start();
        new Thread(() -> count++).start();
    }
}
```

## **Answer**

**Infinite Loop (or unpredictable output)**

- **No `volatile` keyword**, so `count` updates may never be seen by other threads.
- **Fix:**
    
    `static volatile int count = 0;`
    

## **13. What will be the output of below code?**

```
class A {
    static void show() {
        System.out.println("A");
    }
}
class B extends A {
voidshow() {
        System.out.println("B");
    }
}
public class Main {
    public static void main(String[] args) {
        A obj = new B();
        obj.show();
    }
}
```

## **Answer**

```
A
```

- **Static methods in Java are not overridden; they are hidden.**
- The method `show()` in `B` is not overriding `show()` in `A` but **hiding** it.
- **Method invocation is based on the reference type for static methods, not runtime polymorphism.**
- Since `obj` is of type `A`, `A.show()` is called, even though `obj` holds an instance of `B`.

## **14. What will be the output of below code?**

```
public class Main {
    public static void main(String[] args) {
        final int x;
        System.out.println(x);
    }
}
```

## **Answer**

**Compilation Error**

- `final` variables **must be initialized before use**.

## **15. What will be the output of below code?**

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        TreeSet<String> set = new TreeSet<>(Comparator.reverseOrder());
        set.add("A");
        set.add("B");
        set.add(null);
        System.out.println(set);
    }
}
```

## **Answer**

**NullPointerException**

- `TreeSet` **does not allow `null` values** with a custom comparator.

## **16. What will be the output of below code?**

```
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> list = List.of("A", "B", "C");
        list.add("D");
    }
}
```

## **Answer**

**UnsupportedOperationException**

- `List.of()` **creates an immutable list**, so modification is forbidden.

## **17. What will be the output of below code?**

```
class Parent {
    Parent() {
        System.out.println("Parent");
    }
}
class Child extends Parent {
    Child() {
        System.out.println("Child");
    }
}
public class Main {
    public static void main(String[] args) {
        new Child();
    }
}
```

## **Answer**

```
Parent
Child
```

- **Super constructors always run first.**

## **18. What will be the output of below code?**

```
class A extends B { }
class B extends A { }

public class Main {
    public static void main(String[] args) {
        A a = new A();
    }
}
```

## **Answer**

**Compilation Error**

- Cyclic inheritance is illegal in Java.

## **19. What will be the output of below code?**

```
@Service
public class A {
    @Autowired
    private B b;
}
@Service
public class B {
    @Autowired
    private A a;
}
```

## **Answer**

**Circular Dependency Error**

- Spring cannot resolve mutual dependencies unless one is marked as `@Lazy`.

## **20. What will be the output of below code?**

```
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        Optional<String> opt = Optional.of(null);
    }
}
```

## **Answer**

**NullPointerException**

- `Optional.of()` **does not allow `null`**. Use `Optional.ofNullable()` instead.

## **21. What will be the output of below code?**

```
class Task implements Runnable {
    public void run() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.out.println("Interrupted!");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new Task());
        t.start();
        t.interrupt();
    }
}
```

## **Answer**

```
Interrupted!
```

- `interrupt()` **wakes up** a sleeping thread.

## **22. What will be the output of below code?**

```
enum Color {
    RED, BLUE, GREEN;

    Color() {
        System.out.println("Constructor");
    }
}
public class Main {
    public static void main(String[] args) {
        Color c = Color.RED;
    }
}
```

## **Answer**

```
Constructor
Constructor
Constructor
```

- **Enum constructors run once per value!**

## **23. What will be the output of below code?**

```
public class Main {
    public static int test() {
        try {
            return 10;
        } finally {
            return 20;
        }
    }

public static void main(String[] args) {
        System.out.println(test());
    }
}
```

## **Answer**

```
20
```

- `finally` **overrides** the `return` statement.

# **Java Code Based Tricky Interview Questions — 2**

## **1. What will be the output of the following code?**

```
public class StringTest {
    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = "he" + "llo";  // Compiler optimization
        String s3 = new String("hello"); // Creates a new object
        String s4 = s3.intern(); // Gets reference from the string pool

        System.out.println(s1 == s2); // (A)
        System.out.println(s1 == s3); // (B)
        System.out.println(s1.equals(s3)); // (C)
        System.out.println(s1 == s4); // (D)
    }
}
```

## **Answer:**

```
true
false
true
true
```

- (A) `true`: The compiler optimizes `"he" + "llo"` to `"hello"`, which is stored in the String Pool.
- (B) `false`: `new String("hello")` creates a new object in the heap, so it’s a different reference.
- (C) `true`: `.equals()` checks content, not references, and both have `"hello"`.
- (D) `true`: `.intern()` forces `s3` to refer to the String Pool version of `"hello"`, which is `s1`.

## **2. What will be the output of below code?**

```
class Parent {
    static void display() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    static void display() {
        System.out.println("Child");
    }
}
public class Test {
    public static void main(String[] args) {
        Parent obj = new Child();
        obj.display();
    }
}
```

## **Answer:**

```
Parent
```

- Static methods do not follow polymorphism. They are resolved at compile-time based on the reference type.
- Here, `obj` is of type `Parent`, so `Parent.display()` is called.

## **3. What will be the output of below code?**

```
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running...");
    }

public static void main(String[] args) {
        MyThread t = new MyThread();
        t.run();  // (A)
        t.start(); // (B)
    }
}
```

## **Answer:**

```
Thread running...
Thread running...
```

- (A) `t.run();` is a normal method call, so it runs on the main thread.
- (B) `t.start();` starts a new thread, which also prints `"Thread running..."`.

## **4. What will the below code print?**

```
import java.util.HashMap;

public class Test {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put(null, 1);
        map.put(null, 2);
        System.out.println(map.get(null));
    }
}
```

## **Answer:**

```
2
```

- `HashMap` allows one `null` key, and the latest value overwrites the previous one.

## **5. Will the below code compile?**

```
final class Immutable {
    private final int data;

    Immutable(int data) {
        this.data = data;
    }
    public int getData() {
        return data;
    }
}
public class Test {
    public static void main(String[] args) {
        Immutable obj = new Immutable(10);
        obj.data = 20;  // Compilation error?
    }
}
```

## **Answer:**

**Compilation Error:** `"data has private access in Immutable"`

- `final` fields cannot be modified after initialization.
- The only way to set `data` is through the constructor.

## **6. What will happen in the below code?**

```
class DeadlockExample {
    public static void main(String[] args) {
        final Object lock1 = new Object();
        final Object lock2 = new Object();

        Thread t1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1 locked lock1");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock2) {
                    System.out.println("Thread 1 locked lock2");
                }
            }
        });
        Thread t2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2 locked lock2");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock1) {
                    System.out.println("Thread 2 locked lock1");
                }
            }
        });
        t1.start();
        t2.start();
    }
}
```

## **Answer:**

**Deadlock Occurs**

- Each thread locks one resource and waits for the other indefinitely.

## **7. Can you count word occurrences?**

```
import java.util.*;
import java.util.stream.*;

public class WordCount {
    public static void main(String[] args) {
        String text = "apple banana apple orange banana apple";
        Map<String, Long> wordCounts = Arrays.stream(text.split(" "))
            .collect(Collectors.groupingBy(w -> w, Collectors.counting()));
        System.out.println(wordCounts);
    }
}
```

## **Answer:**

```
{apple=3, banana=2, orange=1}
```

- Streams split the string and count occurrences.

## **8. Find the missing number in an array from `1` to `N` with one number missing.**

```
public class MissingNumber {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 5}; // Missing number is 4
        System.out.println(findMissingNumber(arr, 5));
    }

    static int findMissingNumber(int[] arr, int n) {
        int xor1 = 1;
        for (int i = 2; i <= n; i++) xor1 ^= i;
        int xor2 = arr[0];
        for (int i = 1; i < arr.length; i++) xor2 ^= arr[i];
        return xor1 ^ xor2;
    }
}
```

## **Answer:**

```
4
```

- XOR is fastest for finding missing numbers.

## **9. What will the below code print?**

```
public class IntegerTest {
    public static void main(String[] args) {
        Integer a = 100, b = 100;
        Integer x = 200, y = 200;

    System.out.println(a == b); // (A)
        System.out.println(x == y); // (B)
    }
}
```

## **Answer:**

```
true
false
```

- Java caches `Integer` values from -128 to 127.

## **10. What will the output of below code?**

```
public class FinallyTest {
    public static void main(String[] args) {
        System.out.println(test());
    }

    static int test() {
        try {
            return 1;
        } finally {
            return 2;
        }
    }
}
```

## **Answer:**

```
2
```

- The `finally` block overrides the return statement in `try`.

**11. Write a Java function to reverse a string without using `StringBuilder` or `StringBuffer`.
Output:**

`Input: "hello"Output: "olleh"`
**Answer:**

```jsx
public class ReverseString {
    public static String reverse(String str) {
        char[] chars = str.toCharArray();
        int left = 0, right = str.length() - 1;

        while (left < right) {
            // Swap characters
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
        return new String(chars);
    }

    public static void main(String[] args) {
        System.out.println(reverse("hello"));
    }
}
```

**12. Write a Java program to find the first non-repeating character in a given string.
Output:**

`Input: "swiss"Output: 'w'`
**Answer:**

```jsx
import java.util.*;

public class FirstNonRepeating {
    public static char firstUniqueChar(String str) {
        Map<Character, Integer> freqMap = new LinkedHashMap<>();
        for (char ch : str.toCharArray()) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }
        for (char ch : freqMap.keySet()) {
            if (freqMap.get(ch) == 1) {
                return ch;
            }
        }
        return '_'; // If no unique character found
    }
    public static void main(String[] args) {
        System.out.println(firstUniqueChar("swiss"));
    }
}
```

**13. Write a Java function to find the longest palindromic substring in a given string.
Output:**

`Input: "babad"Output: "bab" or "aba"`
**Answer:**

```jsx
public class LongestPalindrome {
    public static String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);  // Odd length
            int len2 = expandAroundCenter(s, i, i + 1); // Even length
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private static int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
    public static void main(String[] args) {
        System.out.println(longestPalindrome("babad"));
    }
}
```

**14. Write a Java function to find the missing number in an array containing numbers from `1` to `N` with one number missing.
Output:**

`Input: [1, 2, 4, 5]Output: 3`
**Answer:**

```jsx
public class MissingNumber {
    public static int findMissingNumber(int[] arr, int n) {
        int xor1 = 1;
        for (int i = 2; i <= n; i++) {
            xor1 ^= i;
        }

int xor2 = arr[0];
        for (int i = 1; i < arr.length; i++) {
            xor2 ^= arr[i];
        }
        return xor1 ^ xor2;
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5}; // Missing number is 3
        System.out.println(findMissingNumber(arr, 5));
    }
}
```

**15. Design and implement an LRU (Least Recently Used) cache with `get(key)` and `put(key, value)`.
Answer:**

```jsx
import java.util.*;

class LRUCache {
    private final int capacity;
    private final Map<Integer, Integer> cache;
    private final LinkedHashMap<Integer, Integer> order;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.order = new LinkedHashMap<>(capacity, 0.75f, true);
    }
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        order.get(key); // Moves key to the end as most recently used
        return cache.get(key);
    }
    public void put(int key, int value) {
        if (cache.size() >= capacity) {
            int oldestKey = order.keySet().iterator().next();
            cache.remove(oldestKey);
            order.remove(oldestKey);
        }
        cache.put(key, value);
        order.put(key, value);
    }
}
public class Test {
    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 10);
        cache.put(2, 20);
        System.out.println(cache.get(1)); // 10
        cache.put(3, 30); // Removes key 2
        System.out.println(cache.get(2)); // -1 (not found)
    }
}
```

**16. Write a custom stack class that supports push, pop, top, and getMin() in O(1) time.
Answer:**

```jsx
import java.util.Stack;

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    public void push(int x) {
        stack.push(x);
        if (minStack.isEmpty() || x <= minStack.peek()) {
            minStack.push(x);
        }
    }
    public void pop() {
        if (stack.pop().equals(minStack.peek())) {
            minStack.pop();
        }
    }
    public int top() {
        return stack.peek();
    }
    public int getMin() {
        return minStack.peek();
    }
}

public class Test {
    public static void main(String[] args) {
        
        MinStack stack = new MinStack();
        stack.push(5);
        stack.push(3);
        stack.push(7);
        System.out.println(stack.getMin()); // 3
        stack.pop();
        System.out.println(stack.getMin()); // 3
        stack.pop();
        System.out.println(stack.getMin()); // 5
    }
}
```

# **Java 8 Code Based Tricky Interview Questions**

# **1. What will be the output of the following code, and how does lazy evaluation impact performance?**

```
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Stream.of("A", "B", "C", "D")
              .filter(s -> {
                  System.out.println("Filtering: " + s);
                  return s.equals("C");
              })
              .findFirst()
              .ifPresent(System.out::println);
    }
}
```

## **Answer:**

```
Filtering: A
Filtering: B
Filtering: C
C
```

- **Lazy Evaluation**: `findFirst()` short-circuits the stream. As soon as `"C"` is found, no further elements are processed.
- **Performance Improvement**: If the stream had a large dataset, this optimization prevents unnecessary filtering operations.
- **Edge Case**: If the stream didn't contain `"C"`, no output would be printed.

# **2. What will be the output of this code? What happens if we swap `peek()` and `limit()`?**

```
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        IntStream.range(1, 10)
                 .peek(System.out::print)
                 .limit(5)
                 .forEach(System.out::print);
    }
}
```

## **Answer:**

```
1122334455
```

- **Lazy Execution**: `peek(System.out::print)` executes before `limit(5)`.
- **Effect of Swapping**: If `limit(5)` comes before `peek(System.out::print)`, only 5 numbers will be printed once, reducing redundant operations.
- **Performance Tip**: Avoid unnecessary `peek()` calls before filtering or limiting a stream.

# **3. What will be the output of this code? What is the performance issue here?**

```
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        System.out.println(getValue(Optional.of("Java 8")));
        System.out.println(getValue(Optional.empty()));
    }

    private static String getValue(Optional<String> optional) {
        return optional.orElse(getExpensiveComputation());
    }

    private static String getExpensiveComputation() {
        System.out.println("Computing expensive value...");
        return "Default";
    }
}
```

## **Answer:**

```
Computing expensive value...
Java 8
Computing expensive value...
Default
```

- `orElse()` always evaluates `getExpensiveComputation()`, even if the optional has a value.
- **Performance Tip**: Use `orElseGet()` instead to avoid unnecessary computation:

```
return optional.orElseGet(() -> getExpensiveComputation());
```

- **Edge Case**: If `getExpensiveComputation()` involved database calls or heavy computation, this inefficiency could impact performance.

# **4. What will be the output, and how does `nullsLast()` change behavior?**

```
import java.util.Arrays;
import java.util.List;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("Banana", null, "Apple", "Mango");
        list.sort(Comparator.nullsFirst(Comparator.naturalOrder()));
        System.out.println(list);
    }
}
```

## **Answer:**

```
[null, Apple, Banana, Mango]
```

- `nullsFirst()` moves `null` values to the beginning.
- **Changing to `nullsLast()` would push `null` values to the end:**

```
[Apple, Banana, Mango, null]
```

- **Edge Case**: If there were multiple `null` values, sorting order would remain unchanged for them.

# **5. Program to find duplicate elements from this list:**

```
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 8);
```

**Expected Output:** `[2, 3, 8]`

## **Program:**

```
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 8);

        Map<Integer, Long> frequency = numbers.stream()
                .collect(Collectors.groupingBy(n -> n, Collectors.counting()));

        List<Integer> duplicates = frequency.entrySet().stream()
                .filter(entry -> entry.getValue() > 1)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        System.out.println(duplicates);
    }
}
```

- Uses `Collectors.groupingBy()` for O(n) efficiency instead of using `HashSet`.
- **Edge Case:** If the list is empty, the solution still works, returning `[]`.

# **6. Find the First Non-Repeating Character in the below String:**

```
String input = "Java articles are awesome";
```

**Expected Output:** `J`

## **Program:**

```
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        String input = "Java articles are awesome";

        Character result = input.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
                .entrySet()
                .stream()
                .filter(e -> e.getValue() == 1)
                .map(Map.Entry::getKey)
                .findFirst()
                .orElse(null);

        System.out.println(result);
    }
}
```

- Uses `LinkedHashMap` to maintain order.
- Handles cases like spaces and punctuation correctly.
- Edge Case: If all characters are repeating, it returns `null`.

# **7. Find the Second-Highest Number from the below List and avoid Sorting when unnecessary.**

```
List<Integer> numbers = Arrays.asList(10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100);
```

**Expected Output:** `90`

## **Program:**

```
import java.util.List;
public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = List.of(10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100);
        int max = Integer.MIN_VALUE, secondMax = Integer.MIN_VALUE;
        for (int num : numbers) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax && num != max) {
                secondMax = num;
            }
        }
        System.out.println(secondMax);
    }
}
```

- O(n) time complexity (better than sorting O(n log n)).
- Handles duplicate max values correctly.

# **8. What will be the output of this code?**

```
import java.util.stream.Stream;
public class Main {
    public static void main(String[] args) {
        Stream<String> stream = Stream.of("one", "two", "three")
                .map(s -> {
                    System.out.println("Mapping: " + s);
                    return s.toUpperCase();
                });
        System.out.println("Stream created!");
        stream.forEach(System.out::println);
    }
}
```

## **Answer:**

```
Stream created!
Mapping: one
ONE
Mapping: two
TWO
Mapping: three
THREE
```

- Intermediate operations (`map()`) are lazy and won’t execute until a terminal operation (`forEach()`) is called.
- **Edge Case:** If there were no terminal operation, the program would print only “Stream created!”

# **9. What will be the output of this code?**

```
import java.util.stream.IntStream;
public class Main {
    public static void main(String[] args) {
        IntStream.range(1, 6)
                .parallel()
                .forEach(System.out::println);
    }
}
```

## **Answer (Order is not guaranteed):**

```
2
4
1
3
5
```

(or any random order)

- `parallel()` makes the stream run in multiple threads.
- `forEach()` doesn’t preserve order when executed in parallel.
- **Edge Case:** Using `.forEachOrdered(System.out::println)` will preserve order despite parallel execution.

# **10. What happens if we try to use a stream twice?**

```
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Stream<String> stream = Stream.of("apple", "banana", "cherry");

        stream.forEach(System.out::println);  // Works fine
        stream.forEach(System.out::println);  // What happens here?
    }
}
```

## **Answer (Expected Error):**

```
Exception in thread "main" java.lang.IllegalStateException: stream has already been operated upon or closed
```

- Streams cannot be reused once a terminal operation is performed.
- **Fix:** Convert the stream into a list (`List<String> list = stream.collect(Collectors.toList());`) before reusing it.

# **11.Predict the output when we filter out `null` values.**

```
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("A", null, "B", "C", null, "D");
        List<String> filteredList = list.stream()
                .filter(s -> s != null)
                .collect(Collectors.toList());
        System.out.println(filteredList);
    }
}
```

## **Answer:**

```
[A, B, C, D]
```

- `filter(s -> s != null)` removes all `null` values from the stream.
- **Edge Case:** If the list contains only `null` values, the output would be `[]`.

# **12. What happens when two elements map to the same key?**

```
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "cherry", "apricot");
        Map<Character, String> map = words.stream()
                .collect(Collectors.toMap(word -> word.charAt(0), word -> word));
        System.out.println(map);
    }
}
```

## **Answer (Expected Error):**

```
Exception in thread "main" java.lang.IllegalStateException: Duplicate key A (attempted merging values "apple" and "apricot")
```

- `apple` and `apricot` both have the key `'A'`, causing a `DuplicateKeyException`.
- **Fix:** Use a merge function to handle duplicates:

```
Map<Character, String> map = words.stream()
    .collect(Collectors.toMap(word -> word.charAt(0), word -> word, (existing, replacement) -> existing));
```

This keeps the first value and ignores duplicates.

# **SQL Code Based Tricky Interview Questions**

# **1. Predict the Output: Self-Join Puzzle**

## **Given the following table `Employee`:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/efcd307e7628fc95640a493a22eb72a6be91faab.webp)

## **Query:**

```
SELECT E1.EmpName AS Employee, E2.EmpName AS Manager
FROM Employee E1
LEFT JOIN Employee E2 ON E1.ManagerID = E2.EmpID
WHERE E2.ManagerID IS NOT NULL;
```

## **Answer:**

- The output will be:

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/b1b0b68df9ffb949bbd24262cf984b298f905a37.webp)

## **Explanation:**

- The `LEFT JOIN` combines each employee with their manager.
- `WHERE E2.ManagerID IS NOT NULL` filters out cases where the manager is `NULL`.
- John’s manager is Mike, whose `ManagerID` is **3** (not NULL), so only this row remains.

# **2. Predict the Output: COUNT vs DISTINCT COUNT Trap**

## **Given the following table `Orders`:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/b10e0fcf85afbbf059fa69eb46541a343ad90b17.webp)

## **Query:**

```
SELECT COUNT(ProductID) AS TotalCount,
       COUNT(DISTINCT ProductID) AS DistinctCount
FROM Orders;
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/01b00f0b21b5771fe4d0dfa89f5429d548d8bd04.webp)

## **Explanation:**

- `COUNT(ProductID)` counts all non-NULL values → **4 rows**.
- `COUNT(DISTINCT ProductID)` counts unique product IDs → {1, 2} → **2 distinct values**.

# **3. Predict the Output: Grouping Misunderstanding**

## **Given the table `Sales`:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/981d71e54efe8e35f8d00b72b40155da8f207564.webp)

## **Query:**

```
SELECT ProductID, SUM(Amount)
FROM Sales
WHERE Amount > 400
GROUP BY ProductID;
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/4d0f914197ef8f4cc4115ee554e7204c0ce8bf40.webp)

## **Explanation:**

- Only `SaleID = 1` meets the `WHERE Amount > 400` condition.
- The other amounts are excluded from the result set before grouping.

# **4. Predict the Output: NULL in Comparison**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/da92b557140116d9fe3f4235934930b971a5853d.webp)

## **Query:**

```
SELECT *
FROM table
WHERE Value != 100;
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/48fe5a26a6e9c5a6d42e4eea005745ae511cd755.webp)

## **Explanation:**

- `NULL` values are ignored because `NULL != 100` evaluates to **UNKNOWN**, not **TRUE**.

# **5. Predict the Output: HAVING vs WHERE Confusion**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/6f0d4ae681c3d94d5627d53edf374b6fc3e6e725.webp)

## **Query:**

```
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employee
WHERE Salary > 1000
HAVING AVG(Salary) > 1000;
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/9c67d5a090f60b855f1a4b82fd482e2a3df4d061.webp)

## **Explanation:**

- The `WHERE` clause filters out `Salary <= 1000` before the `AVG()` calculation.
- Since `HR` gets excluded before aggregation, only IT remains.

# **6. Predict the Output: NULL Trap in Aggregate**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/92e0fd581502291dd52d789b706a8d2ca23a35e7.webp)

## **Query:**

```
SELECT SUM(Value) AS Total
FROM table;
```

## **Answer: Total 30**

## **Explanation:**

- `SUM()` ignores `NULL` values during aggregation.

# **7. Predict the Output: JOIN Order Trap**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/1937eb38ab58ff1104c495eabf39aed771471950.webp)

## **Query:**

```
SELECT *
FROM A
INNER JOIN B ON A.ID = B.ID
WHERE A.Value = 'X';
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/ad27cc0b31abadc7f4db8cbe228c859ffe12e291.webp)

## **Explanation:**

- Only IDs that match in both tables are included in an `INNER JOIN`.

# **8. Predict the Output: ORDER BY with NULLS FIRST/LAST**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/8ef7176f1b7a58f02d906ca5b22ebf273f998da8.webp)

## **Query:**

```
SELECT *
FROM table
ORDER BY Value DESC NULLS FIRST;
```

## **Answer:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/4a9c7c16c8e51c4bc078e550d755b3f4cbcae1f6.webp)

## **Explanation:**

- `NULLS FIRST` puts `NULL` values at the top, followed by descending order.

# **9. Predict the Output: CROSS JOIN Count Puzzle**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/c0c3d2901976a7ff209b598fac66c47b10bb6cd3.webp)

## **Query:**

```
SELECT COUNT(*)
FROM table1
CROSS JOIN table2;
```

## **Answer:`4` (2 × 2)**

## **Explanation:**

- CROSS JOIN = Cartesian product.
- 2 rows in table1 × 2 rows in table2 = **4 rows**.

# **10. Predict the Output: Mysterious Cartesian Product**

## **Given:**

![](https://d2jwys97bgbqkm.archive.ph/XIDXK/c0c3d2901976a7ff209b598fac66c47b10bb6cd3.webp)

## **Query:**

```
SELECT A.*
FROM table1 A, table2 B;
```

## **Answer: `4 rows` (2 × 2)**

## **Explanation:**

- Implicit `CROSS JOIN` creates a Cartesian product.

# **11. Write a query to find the 3rd highest salary from an `Employee` table without using `LIMIT`.**

## **Answer:**

```
SELECT Salary
FROM (
    SELECT Salary,
           DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) AS RankedSalaries
WHERE rnk = 3;
```

## **Explanation:**

- `DENSE_RANK()` creates a ranking of salaries in descending order.
- The subquery assigns a rank to each salary.
- The outer query filters for the 3rd highest salary.

# **12. Write a query to find the second-highest salary in each department from the `Employee` table.**

## **Answer:**

```
SELECT Department, Salary AS SecondHighestSalary
FROM (
    SELECT Department, Salary,
           DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS rnk
    FROM Employee
) AS RankedSalaries
WHERE rnk = 2;
```

## **Explanation:**

- `DENSE_RANK()` assigns the same rank to equal values, ensuring correct handling of ties.

# **13. Write a query to remove duplicates from a table without using `DISTINCT`.**

## **Answer:**

```
WITH CTE AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY column1, column2, column3 ORDER BY id) AS rn
    FROM table
)
DELETE FROM table
WHERE id IN (
    SELECT id FROM CTE WHERE rn > 1
);
```

## **Explanation:**

- `ROW_NUMBER()` assigns a unique rank to duplicates.
- Rows with `rn > 1` are deleted, keeping the first occurrence.

# **14. Write a query to find employees who logged in for 3 consecutive days.**

## **Answer:**

```
SELECT EmployeeID, LoginDate
FROM (
    SELECT EmployeeID, LoginDate,
           LAG(LoginDate, 1) OVER (PARTITION BY EmployeeID ORDER BY LoginDate) AS prev_day,
           LAG(LoginDate, 2) OVER (PARTITION BY EmployeeID ORDER BY LoginDate) AS prev_2_days
    FROM EmployeeLogin
) AS t
WHERE LoginDate = prev_day + INTERVAL 1 DAY
  AND prev_day = prev_2_days + INTERVAL 1 DAY;
```

## **Explanation:**

- `LAG()` checks the previous two login dates.
- If they form a consecutive sequence, they are included in the result.

# **15. Write a query to calculate the cumulative sum of sales, resetting when the value becomes negative.**

## **Answer:**

```
WITH SalesData AS (
    SELECT SaleID, Amount,
           SUM(CASE WHEN Amount < 0 THEN 1 ELSE 0 END) OVER (ORDER BY SaleID) AS reset_flag
    FROM Sales
)
SELECT SaleID, Amount,
       SUM(Amount) OVER (PARTITION BY reset_flag ORDER BY SaleID) AS CumulativeSum
FROM SalesData;
```

## **Explanation:**

- `CASE` creates a reset flag when the value is negative.
- `SUM()` partitions the data based on the reset flag.

# **16. Write a query to find the median value in a table.**

## **Answer:**

```
WITH RankedValues AS (
    SELECT Value,
           RANK() OVER (ORDER BY Value) AS rn,
           COUNT(*) OVER () AS cnt
    FROM table
)
SELECT AVG(Value) AS Median
FROM RankedValues
WHERE rn IN (FLOOR((cnt + 1) / 2), CEIL((cnt + 1) / 2));
```

## **Explanation:**

- `RANK()` ensures ties are handled correctly.
- `FLOOR` and `CEIL` select the middle values when the count is even.

# **17. Write a query to calculate a running total of sales for each month using a window function.**

## **Answer:**

```
SELECT SaleID, Month,
       SUM(SaleAmount) OVER (PARTITION BY Month ORDER BY SaleID) AS RunningTotal
FROM Sales;
```

## **Explanation:**

- `SUM()` creates a running total within each month.
- `PARTITION BY` resets the total at the start of each new month.

# **18. Write a query to find the department with the highest total salary using window functions.**

## **Answer:**

```
WITH DeptTotal AS (
    SELECT Department, SUM(Salary) AS TotalSalary
    FROM Employee
    GROUP BY Department
)
SELECT Department, TotalSalary
FROM (
    SELECT Department, TotalSalary,
           RANK() OVER (ORDER BY TotalSalary DESC) AS rnk
    FROM DeptTotal
) AS RankedDepartments
WHERE rnk = 1;
```

## **Explanation:**

- The total salary is calculated for each department.
- `RANK()` assigns a rank based on total salary.
- The highest-ranked department is returned.

# **19. Write a query to find missing values in a sequential column of IDs.**

## **Answer:**

```
SELECT t1.ID + 1 AS MissingID
FROM table t1
LEFT JOIN table t2 ON t1.ID + 1 = t2.ID
WHERE t2.ID IS NULL;
```

## **Explanation:**

- The query checks for missing `ID` values using a `LEFT JOIN`.

# **20. Write a query to find overlapping date ranges from a `Bookings` table.**

## **Answer:**

```
SELECT t1.*, t2.*
FROM Bookings t1
JOIN Bookings t2
ON t1.BookingID != t2.BookingID
AND t1.StartDate <= t2.EndDate
AND t1.EndDate >= t2.StartDate;
```

## **Explanation:**

- The query checks if one booking’s date range overlaps with another’s using a `JOIN`.

# **Citi Bank Java Developer Interview — 2**

## **1. What do you understand by Stream not storing elements?**

When we say “Stream does not store elements” in Java, it means: Streams don’t hold or contain data.

Instead, they operate on data from a source (like a collection, array, or I/O channel) and process elements on demand — i.e., lazily.

## **In contrast to a `Collection`:**

A `List` or `Set` stores elements in memory — you can retrieve them anytime.

```
List<Integer> list = List.of(1, 2, 3);
System.out.println(list.get(0)); // 1 — stored in memory
```

## **But with a `Stream`:**

A `Stream` just represents a pipeline of operations to be performed on elements from a source.

```
Stream<Integer> stream = list.stream().filter(n -> n % 2 == 1);
```

At this point, nothing has been executed yet. The Stream is just a blueprint.

```
stream.forEach(System.out::println); // Now the pipeline executes
```

Even then, the elements are not stored in the stream itself — they’re pulled one-by-one from the source and passed through the pipeline.

## **2. What is Parallel Stream?**

A Parallel Stream is a special kind of Java Stream that splits the data processing across multiple threads to perform operations in parallel, rather than sequentially.

It uses multiple CPU cores to process elements concurrently, which can significantly improve performance on large datasets — if used correctly.

## **Creation:**

You can convert any regular stream into a parallel stream like this:

```
List<Integer> list = List.of(1, 2, 3, 4, 5);

// Sequential stream
list.stream().forEach(System.out::println);
// Parallel stream
list.parallelStream().forEach(System.out::println);
```

Or:

```
list.stream().parallel().forEach(System.out::println);
```

## **Working:**

- Parallel streams use the Fork/Join Framework introduced in Java 7 (`ForkJoinPool.commonPool()`).
- The stream divides the source into multiple substreams.
- Each substream is processed in a separate thread.
- The results are combined in the end.

## **Caveats:**

- Order is not guaranteed in operations like `forEach()`. Use `forEachOrdered()` if order matters — but it may reduce performance.
- Not all operations benefit from parallelism (e.g., I/O-bound tasks, small datasets).
- Overhead of thread creation and merging results can cancel out the speed gains if the dataset is small.
- Be careful with shared mutable state — it can lead to race conditions and unpredictable behavior.

## **Use Cases:**

Use them only when:

- The task is CPU-bound, not I/O-bound.
- The data size is large enough to justify parallelism.
- The operations are stateless and independent (no shared mutable variables).
- You don’t care about execution order (or you explicitly preserve it with `.forEachOrdered()`).

## **Example:**

```
List<Integer> numbers = IntStream.range(1, 1_000_000)
    .boxed()
    .collect(Collectors.toList());

long count = numbers.parallelStream()
    .filter(n -> n % 2 == 0)
    .count();
System.out.println("Even numbers count: " + count);
```

This processes the filtering of even numbers in parallel, which can be much faster than sequentially, depending on the machine.

**3. Name few Intermediate methods.**

![](https://d27i2bp36bga4q.archive.ph/7a2Ma/f34a7be70aa83318cf1556b933f1d6414908e5f3.webp)

## **4. What Predicate does Filter() accepts?**

The `filter()` method in Java Streams accepts a `Predicate<T>` functional interface, where `T` is the type of elements in the stream.

It’s a functional interface with this method:

```
@FunctionalInterface
public interface Predicate<T> {
    boolean test(T t);
}
```

So, it takes an input of type `T` and returns a `boolean`. In the context of `filter()`, it tells the stream whether to keep or discard an element.

## **Example:**

```
List<Integer> numbers = List.of(1, 2, 3, 4, 5);

numbers.stream()
       .filter(n -> n % 2 == 0) // <-- Predicate<Integer>
       .forEach(System.out::println);
```

Here, `n -> n % 2 == 0` is a Predicate, and it filters only even numbers.

**You can also use method references or predefined predicates:**

```
Predicate<String> isLong = str -> str.length() > 5;

List<String> words = List.of("hello", "elephant", "dog");
words.stream()
     .filter(isLong) // Only "elephant"
     .forEach(System.out::println);
```

## **5. Suppose we have a method in a super class throws file not found exception. Now it’s sub class with same method overrides and throw IO Exception, will it work fine or error?**

Here:

- Superclass method: throws `FileNotFoundException`
- Subclass method (overriding): throws `IOException`

So, when overriding a method, the subclass cannot declare a broader (more general) checked exception than the method in the superclass.

It can throw a narrower exception (i.e., subclass of the original), but not a broader one.

So:

- `FileNotFoundException` is a subclass of `IOException`.
- That means `IOException` is broader than `FileNotFoundException`.

## **So, in our case:**

**Code:**

```
class SuperClass {
    void readFile() throws FileNotFoundException {
        // ...
    }
}

class SubClass extends SuperClass {
    @Override
    void readFile() throws IOException { // Compilation Error!
        // ...
    }
}
```

## **Compilation Error:**

We’re trying to throw a broader exception (`IOException`) than the superclass (`FileNotFoundException`) — Java won’t allow it.

## **Correct Way:**

Either throw the same or narrower exception, like:

```
@Override
void readFile() throws FileNotFoundException { } // OK
```

Or:

```
@Override
void readFile() throws EOFException { } // Also OK (more specific)
```

Or:

```
@Override
void readFile() { } // Also OK (no exception at all)
```

## **6. If we have two interfaces, implementing two identical default methods. We have a class implementing both these interfaces. How can you ensure the call the specific default method of the interfaces.**

This is a classic Java 8 diamond problem scenario with default methods:

We have:

- Two interfaces: `A` and `B`
- Both define identical default methods (same name & signature)
- A class `C` implements both interfaces

## **Problem:**

When class `C` tries to inherit both default methods, Java gets confused — which one should it use?

## **Solution:**

You need to override the method in class `C` and explicitly specify which interface's method you want to call using:

```
InterfaceName.super.methodName();
```

## **Example:**

```
interface A {
    default void sayHello() {
        System.out.println("Hello from A");
    }
}

interface B {
    default void sayHello() {
        System.out.println("Hello from B");
    }
}
class C implements A, B {
    @Override
    public void sayHello() {
        A.super.sayHello(); // You choose explicitly
        // Or use B.super.sayHello(); if needed
    }
}
```

## **7. When to use LinkedList over an ArrayList?**

## **Use `LinkedList` when:**

**1. You frequently insert or delete elements from the beginning or middle**

- `LinkedList` excels at insertion/deletion because it just re-links nodes.
- `ArrayList` has to shift elements, which is slower.

```
list.add(0, "newItem"); // Fast in LinkedList
```

**2. You need a Queue or Deque (double-ended queue)**

- `LinkedList` implements `Deque` — great for queue-like behavior (FIFO/LIFO).
- It supports efficient `addFirst()`, `removeLast()`, etc.

## **Avoid `LinkedList` when:**

**1. You need fast random access**

- `LinkedList.get(index)` is O(n) (traverses from start/end)
- `ArrayList.get(index)` is O(1) — super fast!

```
list.get(1000); // Slow in LinkedList, instant in ArrayList
```

**2. Memory matters**

- `LinkedList` stores extra node pointers (`prev`, `next`) → more memory per element.
- `ArrayList` is more memory-efficient.

**8. Write a program to remove elements on a specific condition from a collection while an iteration is ongoing.**

```jsx
import java.util.*;

public class SafeRemoveExample {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6));
        Iterator<Integer> iterator = numbers.iterator();

        while (iterator.hasNext()) {
            Integer number = iterator.next();
            if (number % 2 == 0) {
                iterator.remove(); // Safe removal
            }
        }
        
        System.out.println("After removal: " + numbers);
    }
}
```

**Output:**

`After removal: [1, 3, 5]`
**Don’t do this:**

```jsx
for (Integer number : numbers) {
    if (number % 2 == 0) {
        numbers.remove(number); // ConcurrentModificationException!
    }
}
```

## **9. In a class, we are overriding hashcode method and explicitly returning 0 every time. How will it impact the application?**

If `hashCode()` always returns `0:`

```
@Override
public int hashCode() {
    return 0; // Every object's hash is the same
}
```

Your program will still run.

But…

**1. All elements go into the same bucket**

- `HashMap` uses `hashCode()` to determine which bucket an entry goes into.
- If `hashCode()` is always `0`, everything lands in the same bucket (say, bucket[0]).

**2. From O(1) to O(n)**

- Normally, `HashMap` gives you constant time lookup (`O(1)`).
- But when all elements are in one bucket, it becomes a linked list or tree, and access degrades to O(n) — very slow as data grows.

**3. Equals() must still be used**

- With same hash codes, `equals()` is called to check for actual match.
- So: `hashCode()` gives the bucket → `equals()` confirms match.

## **Example:**

```
Map<MyObject, String> map = new HashMap<>();
map.put(new MyObject(1), "One");
map.put(new MyObject(2), "Two");
map.put(new MyObject(3), "Three");
```

If all these `MyObject` instances return `0` for `hashCode()`:

- They all land in the same bucket.
- Lookup now has to linearly compare each object using `equals()` — slow.

**So, while it’s not a compile-time error, the app:**

- Will run much slower
- Will consume more CPU during lookups
- Might even time out or degrade at scale

## **10. What do you understand by concurrency?**

In Java, concurrency refers to the ability to run multiple tasks simultaneously or overlapping in time in such a way that it makes optimal use of available resources (like CPU cores).

Java provides several mechanisms to manage concurrency, from low-level thread management to high-level abstractions like the Executor framework.

Let’s dive deeper into how concurrency is achieved in Java and the tools it offers to handle concurrent tasks.

## **Concepts:**

1. **Thread**:
- A thread is the smallest unit of execution in a program. Java provides built-in support for multithreading, which allows multiple threads to run concurrently.
- Java’s `Thread` class is used to create and control threads.

**2. Runnable Interface**:

- The `Runnable` interface is often used to define the task a thread will perform. It contains the `run()` method, which is executed when the thread starts.
- Using `Runnable` is preferable when a task doesn't need to inherit from `Thread`, allowing your class to extend something else.

## **Creating Threads in Java**

1. **By Extending the `Thread` Class**:

```
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}
public class ThreadExample {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start(); // Starts the thread
    }
}
```

**2. By Implementing the `Runnable` Interface**:

```
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread is running");
    }
}

public class RunnableExample {
    public static void main(String[] args) {
        MyRunnable task = new MyRunnable();
        Thread t1 = new Thread(task);
        t1.start(); // Starts the thread
    }
}
```

## **Executor Framework (Higher-Level Concurrency Management)**

Instead of manually managing threads, the Executor framework allows for more flexible and scalable thread management. It provides an abstraction over the `Thread` class, making it easier to manage thread pools and schedule tasks asynchronously.

1. **ExecutorService**:
- `ExecutorService` is a higher-level replacement for `Thread` and allows you to manage and control thread execution.

```
import java.util.concurrent.*;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        Runnable task = () -> System.out.println("Task executed by: " + Thread.currentThread().getName());
        executor.submit(task); // Submit task for execution
        executor.submit(task);
        executor.shutdown(); // Gracefully shut down the executor
    }
}
```

In this example, we create a thread pool of 2 threads and submit two tasks to be executed by those threads.

## **Synchronization and Thread Safety**

When multiple threads share resources (e.g., modifying a variable or accessing a database), synchronization is necessary to prevent race conditions (when threads interfere with each other).

1. **`synchronized` Keyword**:
- The `synchronized` keyword ensures that only one thread can access a block of code at a time.

```
class Counter {
    private int count = 0;

public synchronized void increment() {
        count++; // Only one thread can execute this at a time
    }
    public int getCount() {
        return count;
    }
}
public class SynchronizationExample {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) counter.increment();
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) counter.increment();
        });
        t1.start();
        t2.start();
        t1.join(); // Wait for threads to finish
        t2.join();
        System.out.println("Final Count: " + counter.getCount());
    }
}
```

In this example, even though multiple threads are incrementing the counter, synchronization ensures that the increment operation is thread-safe.

## **Other Concurrency Utilities**

1. **`CountDownLatch`**:
- A `CountDownLatch` allows one or more threads to wait until a set of operations (usually performed by other threads) completes.

```
import java.util.concurrent.CountDownLatch;
public class CountDownLatchExample {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(3);
        Runnable task = () -> {
            try {
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " completed.");
                latch.countDown();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        };
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        Thread t3 = new Thread(task);
        t1.start();
        t2.start();
        t3.start();
        latch.await(); // Wait for all threads to complete
        System.out.println("All threads are done!");
    }
}
```

**`2. CyclicBarrier`**:

- A `CyclicBarrier` allows a group of threads to wait for each other to reach a common barrier point before continuing.

```
import java.util.concurrent.CyclicBarrier;

public class CyclicBarrierExample {
    public static void main(String[] args) throws InterruptedException {
        CyclicBarrier barrier = new CyclicBarrier(3, () -> System.out.println("All threads have arrived"));
        Runnable task = () -> {
            try {
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " reached barrier.");
                barrier.await(); // Wait for other threads
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
        };
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        Thread t3 = new Thread(task);
        t1.start();
        t2.start();
        t3.start();
    }
}
```

## **11. What do you understand by Facade design pattern?**

The Facade Design Pattern is a structural design pattern that provides a simplified interface to a complex subsystem.

It acts like a front-facing interface that hides all the inner workings of a system and exposes only what is necessary to the client.

Think of it like a hotel reception — you don’t need to know how room booking, housekeeping, and dining work internally. You just go to the reception (facade), and they take care of everything behind the scenes.

## **Structure in Code**

Let’s simulate that:

**Complex subsystem:**

```
class DVDPlayer {
    void on() { System.out.println("DVD Player on"); }
    void play() { System.out.println("DVD Player playing"); }
}

class Projector {
    void on() { System.out.println("Projector on"); }
}
class Amplifier {
    void on() { System.out.println("Amplifier on"); }
}
```

**Facade class:**

```
class HomeTheaterFacade {
    private DVDPlayer dvd;
    private Projector projector;
    private Amplifier amp;

    public HomeTheaterFacade(DVDPlayer dvd, Projector projector, Amplifier amp) {
        this.dvd = dvd;
        this.projector = projector;
        this.amp = amp;
    }
    public void watchMovie() {
        System.out.println("Get ready to watch a movie...");
        amp.on();
        projector.on();
        dvd.on();
        dvd.play();
    }
}
```

## **Client code:**

```
public class FacadePatternDemo {
    public static void main(String[] args) {
        DVDPlayer dvd = new DVDPlayer();
        Projector projector = new Projector();
        Amplifier amp = new Amplifier();

        HomeTheaterFacade homeTheater = new HomeTheaterFacade(dvd, projector, amp);
        homeTheater.watchMovie();  // One simple call hides all complexity
    }
}
```

## **Use Cases:**

- When you want to provide a simple interface to a complex system.
- When you want to decouple clients from subsystem implementations.
- When working with legacy code, and you want to wrap it neatly.
- To organize code better and improve readability.

## **Benefits**

- Hides the complexity of the system.
- Improves code maintainability and readability.
- Reduces dependencies between client and subsystem.
- Encourages loose coupling.

## **Drawbacks**

- Overuse might lead to a god-object-like facade with too many responsibilities.
- Might hide important subsystem features if not thoughtfully designed.

## **12. What is Atomic Integer class?**

`AtomicInteger` is a class in `java.util.concurrent.atomic` package that provides lock-free, thread-safe operations on a single `int` value.

In multithreaded environments, when multiple threads try to read-modify-write a shared integer (e.g., incrementing a counter), race conditions can occur. `AtomicInteger` solves this problem without using synchronization (i.e., no `synchronized` block or method).

It uses low-level atomic CPU instructions like compare-and-swap (CAS) under the hood for high performance.

## **Example: Classic vs Atomic**

**Problem with normal `int` counter:**

```
class Counter {
    int count = 0;

    void increment() {
        count++; // Not thread-safe
    }
}
```

In a multithreaded environment, `count++` is not atomic — it's a 3-step operation: read → increment → write.

## **Solution with `AtomicInteger`:**

```
import java.util.concurrent.atomic.AtomicInteger;

class AtomicCounter {
    AtomicInteger count = new AtomicInteger(0);
    void increment() {
        count.incrementAndGet(); // Thread-safe and atomic
    }
}

```

## **Use Cases**

- When you need a shared counter in a concurrent environment.
- When you want performance better than using synchronized blocks.
- When using lock-free algorithms.

## **Example:**

```
public class AtomicDemo {
    private static AtomicInteger counter = new AtomicInteger(0);

    public static void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.incrementAndGet();
            }
        };
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Final Count: " + counter.get()); // Always 2000
    }
}
```

## **13. Suppose you have to design a system like Uber, so how will you go about it?**

We can start with some high level design like below:

## **Designing a System Like Uber (Ride-Hailing Platform)**

Let’s break it down step by step.

## **1. High-Level Goals**

- Match riders with nearby drivers.
- Real-time location tracking.
- Handle bookings, cancellations, payments.
- Scale to millions of users.
- Ensure low latency + high availability.

## **2. Actors in the System**

- Rider
- Driver
- Admin (optional)

## **3. Core Components**

**Client-side:**

- Mobile apps for drivers and riders.
- Location permission, push notifications, maps integration.

**Backend services:**

- Authentication service (OAuth, tokens)
- User management service (profiles, history)
- Ride-matching service (find nearby drivers)
- Real-time location tracking
- Trip management service (booking, start/stop ride)
- Payment service (wallets, cards, billing)
- Notifications service (SMS, in-app, email)

## **4. ️Database Design (simplified)**

**Tables**:

- `Users` → id, name, phone, user_type (rider/driver)
- `Drivers` → id, status (online/offline), location, vehicle details
- `Rides` → ride_id, rider_id, driver_id, start_time, end_time, status, fare
- `Payments` → payment_id, ride_id, amount, payment_method

Use normalized relational DB (like PostgreSQL) for transactional dataand NoSQL (like MongoDB / Redis) for fast location + session data.

## **5. Real-time Location Tracking**

Use:

- GPS from client device
- Periodically push location to backend.
- Store in Redis / GeoHash / Google S2

***Matching engine uses these coordinates to find nearest drivers.***

## **6. Ride Matching Logic**

- Rider requests ride → sends current location.
- Backend fetches drivers within X km using GeoQuery.
- Send request to drivers via WebSocket / Push.
- First to accept → ride is assigned.

Handle edge cases: no drivers found, retries, timeouts.

## **7. Scalability and Load Handling**

- Use Microservices Architecture
- API Gateway for routing
- Kafka for asynchronous processing (e.g., location events)
- Load balancers in front of all services
- Horizontal scaling (auto-scaling EC2 pods, containers)

## **8. Communication Between Services**

- REST + gRPC for sync calls.
- Kafka / RabbitMQ for async events like:
- Driver location updates
- Ride started / ended
- Payment success

## **9. Security**

- HTTPS for all communication
- JWT tokens for user auth
- Role-based access (driver vs rider)
- Input validation to prevent injection/abuse

## **10. Monitoring and Logging**

- ELK stack or Grafana + Prometheus for metrics
- Logs: user activity, ride flow, payments
- Alerting system for failures / slow responses

## **11. Optional Enhancements**

- Surge pricing logic (based on demand/supply)
- Ride rating system
- Scheduled rides
- Loyalty programs
- Fraud detection
- AI-based estimated arrival time (ETA) prediction

# **Citi Bank Java Developer Interview**

## For 6+ Years of Experience: Part 1

## **1. What are the best principles to follow while coding?**

Below are some of the best principles to follow while coding:

- **Write clean, readable code** — clarity over cleverness.
- **Follow SOLID principles**, especially Single Responsibility and Open/Closed.
- **Keep methods small and focused** — ideally doing one thing.
- **Avoid duplication** — apply DRY without over-engineering.
- **Use meaningful names** for variables, methods, and classes.
- **Write unit tests** and ensure code is testable.
- **Fail fast and handle errors properly** — don’t suppress exceptions.
- **Refactor regularly**, not just when there’s a bug.
- **Maintain consistency** with naming, formatting, and design patterns.
- **Avoid premature optimization** — first make it work, then make it better.
- **Use version control wisely** — meaningful commit messages and atomic commits.
- **Comment only when necessary** — let the code explain itself, and document “why”, not “what”.
- **Understand the business logic** behind the code — don’t just code blindly.

## **2. Explain the internal working of ConcurrentHashMap.**

`ConcurrentHashMap` is a thread-safe collection designed for high concurrency with better performance than `Hashtable` or `Collections.synchronizedMap`.

## **Internal Working:**

- It uses an array of Nodes (`Node<K, V>[] table`) like a regular `HashMap`.
- It does not use segment locking (unlike Java 7).
- Uses fine-grained locking (on individual buckets/nodes).
- Read operations are lock-free.
- Write/update operations use CAS and `synchronized` blocks on the node level.
- If too many entries end up in the same bucket, it uses a Red-Black Tree for faster access.

## **Operations working:**

## **`1. get(key)`:**

- Uses hash to locate the bucket.
- Traverses the chain/tree in that bucket.
- No locking — just volatile reads.

```
public V get(Object key) {
    int hash = spread(key.hashCode());
    Node<K,V>[] tab = table;
    Node<K,V> e = tabAt(tab, (tab.length - 1) & hash);
    while (e != null) {
        if (e.hash == hash && (e.key.equals(key)))
            return e.val;
        e = e.next;
    }
    return null;
}
```

## **`2. put(key, value)`:**

- Calculates hash and index.
- If the bucket is empty, uses CAS to insert the new node.
- If not, locks the bucket (`synchronized` on the first node) and inserts.
- If entries exceed threshold, resizes.
- If the chain is too long, transforms it into a tree.

```
public V put(K key, V value) {
    return putVal(spread(key.hashCode()), key, value, false);
}

private final V putVal(int hash, K key, V value, boolean onlyIfAbsent) {
    for (;;) {
        Node<K,V>[] tab = table;
        int i = (tab.length - 1) & hash;
        Node<K,V> f = tabAt(tab, i);
        if (f == null) {
            if (casTabAt(tab, i, null, new Node<>(hash, key, value, null)))
                break;
        } else {
            synchronized (f) {
                // safe insertion under lock
                // also handles treeify if needed
            }
            break;
        }
    }
    return null;
}
```

## **Resize Operation:**

- Resize happens in a distributed way using multiple threads (unlike `HashMap`).
- Each thread helps transfer part of the table.
- Uses `ForwardingNode` to indicate a bucket is being moved.

## **Advantages:**

- High concurrency with minimal locking.
- Lock-free reads → better performance for read-heavy applications.
- Uses CAS (Compare-And-Swap) for atomic operations.
- Treeification ensures performance doesn’t degrade with hash collisions.

**3. What are the differences between Drop vs Truncate and Delete?**

![](https://d9b7jaj92i1k2y.archive.ph/amNlX/06ccffeea5a99ff1bb000e13cbd02bd8c7972d7e.webp)

## **4. What are One-to-One, One-to-Many, Many-to-One, and Many-to-Many relationships in DB design?**

Below are the details of the relationships in DB design:

## **1. One-to-One (1:1)**

- Each row in Table A is linked to only one row in Table B, and vice versa.
- Often used to split optional or sensitive data into a separate table.

**Example:**`User` ↔ `UserProfile`Each user has exactly one profile.

```
User(id, name)
UserProfile(id, user_id [unique, FK], address)
```

## **2. One-to-Many (1:N)**

- A row in Table A can be linked to multiple rows in Table B, but each row in B refers to one row in A.
- Most common relationship type.

**Example:**`Department` → `Employee`One department can have many employees.

```
Department(id, name)
Employee(id, name, department_id [FK])
```

## **3. Many-to-One (N:1)**

- This is just the reverse view of One-to-Many.
- Many rows in Table A relate to one row in Table B.

**Example:**Many employees → one department (same as above).

## **4. Many-to-Many (M:N)**

- Rows in Table A can relate to many rows in Table B, and vice versa.
- Requires a junction/bridge table to model.

**Example:**`Student` ↔ `Course`A student can enroll in many courses, and each course can have many students.

```
Student(id, name)
Course(id, name)
Student_Course(student_id [FK], course_id [FK]) -- Junction table
```

## **5. How do you ensure safe concurrent updates in real-time systems?**

Real-time systems demand high throughput, low latency, and consistency under concurrency.

Here’s how we handle it:

## **1. Optimistic Locking (Recommended for most real-time use cases)**

- Each record carries a version/timestamp.
- Before writing, compare the version.
- If it matches → update.
- Else → reject or retry.

It’s non-blocking and works well in systems with low write collision.

```
UPDATE orders
SET status = 'SHIPPED', version = version + 1
WHERE id = 101 AND version = 3;
```

If `version` has changed → no rows affected → retry logic kicks in.

## **2. Pessimistic Locking for Critical Sections**

Use `SELECT ... FOR UPDATE` or JPA's `PESSIMISTIC_WRITE` when:

- High risk of collisions.
- Need to ensure strong consistency (e.g., updating account balance).

```
SELECT * FROM accounts WHERE id = 101 FOR UPDATE;
```

## **3. Atomic Operations / CAS (Compare and Swap)**

For in-memory counters or high-frequency updates (e.g., like count, leaderboard):

Use atomic variables or Redis INCR:

```
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
```

Or in Redis:

```
INCR leaderboard:player123:score
```

These are lock-free and thread-safe.

## **4. Concurrent Data Structures in Java**

To avoid `ConcurrentModificationException`:

- Use `ConcurrentHashMap` for maps.
- Use `CopyOnWriteArrayList` for read-heavy lists.
- Or wrap with `Collections.synchronizedMap()` etc.

```
ConcurrentHashMap<String, Integer> liveScores = new ConcurrentHashMap<>();
liveScores.put("IND", 300);
```

Iterate using `.entrySet().iterator()` safely.

## **5. MVCC (Multiversion Concurrency Control)**

Used by DBs like PostgreSQL and Oracle.

- Writers don’t block readers.
- Readers get a snapshot.
- Ensures real-time consistency without hard locks.

## **6. In-Memory DBs / Caches with Locking Semantics**

Tools like Redis can be used with Redlock (distributed lock):

```
SET key "value" NX PX 3000
```

- NX → Only set if not exists (no overwrite).
- PX → Expiry in milliseconds.
- Ensures atomic, time-bound lock across services.

## **6. Suppose you have a DB server in multiple time zones. How will you handle time zones for queries that are supposed to run at a specific time?**

To handle time zones effectively in a database server with multiple time zones, ensuring queries run at specific times, we can follow these strategies:

## **1. Store all Timestamps in UTC**

- Storing in UTC prevents time zone confusion, making it easier to compare timestamps from different time zones.
- **SQL Example:**Always store timestamps as UTC to maintain consistency across all time zones.

```
-- Store UTC timestamp for a scheduled task
INSERT INTO scheduled_jobs (job_id, run_time_utc)
VALUES (101, '2025-04-12T04:30:00Z');
```

## **2. Convert Local Time to UTC Before Storing**

- User inputs are often in their local time zone, but we need to convert that time to UTC before saving it to the database.
- **Java Example:** Convert local time to UTC before storing it in the DB.

```
// Convert local time (Asia/Kolkata) to UTC
ZonedDateTime localTime = ZonedDateTime.of(2025, 4, 12, 10, 0, 0, 0, ZoneId.of("Asia/Kolkata"));
ZonedDateTime utcTime = localTime.withZoneSameInstant(ZoneId.of("UTC"));

// Store utcTime.toInstant() to the database
```

## **3. Convert UTC to Local Time in Queries**

- When fetching records for a specific time zone, convert the UTC time stored in the database to the user’s local time.
- **SQL Example:** Convert a UTC timestamp to a specific time zone (e.g., Asia/Kolkata or America/Los_Angeles).

```
-- Convert UTC timestamp to IST (Asia/Kolkata)
SELECT run_time_utc AT TIME ZONE 'UTC' AT TIME ZONE 'Asia/Kolkata' AS run_time_ist
FROM scheduled_jobs;

-- Convert UTC timestamp to PST (America/Los_Angeles)
SELECT run_time_utc AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles' AS run_time_pst
FROM scheduled_jobs;
```

## **4. Use Timezone-Aware Scheduling (For Cron Jobs)**

- Use UTC for scheduling and convert local time to UTC when defining the cron job.
- **Spring Boot Example:**

```
// Schedule a job to run at 10:00 AM IST (converted to 4:30 AM UTC)
@Scheduled(cron = "0 30 4 * * *", zone = "UTC")
public void runJob() {
    // Job logic here
}
```

## **5. Synchronize Server Clocks with NTP**

- Ensure consistent timekeeping across all servers to avoid time drift.
- Linux Command to Sync Time:

```
# Sync system time using NTP
sudo timedatectl set-ntp true
```

## **6. Handling Daylight Saving Time (DST)**

- Some time zones have daylight saving time shifts (e.g., US time zones). Using time zones like `America/New_York` accounts for DST automatically.
- **Java Example:**

```
// Convert UTC to a timezone-aware time considering DST
ZonedDateTime utcTime = ZonedDateTime.of(2025, 4, 12, 4, 30, 0, 0, ZoneId.of("UTC"));
ZonedDateTime localTime = utcTime.withZoneSameInstant(ZoneId.of("America/New_York"));
```

## **7. Can you set a Default time zone for an entire application?**

Yes, you can set a default time zone for an entire application to ensure consistent time handling across different parts of your application.

## **1. Set Default Time zone in Java**

In Java, you can set the default time zone for the entire application using `TimeZone.setDefault()`:

```
import java.util.TimeZone;

public class Application {
    public static void main(String[] args) {
        // Set default timezone for the entire application
        TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
        // Verify the default timezone
        System.out.println("Default Timezone: " + TimeZone.getDefault().getID());
    }
}
```

- This ensures that all operations involving time (like `Date`, `Calendar`, and `ZonedDateTime`) will use the default time zone unless explicitly overridden.

## **2. Set Default Time zone in Spring Boot**

In a Spring Boot application, you can configure the default time zone globally by setting it in the `application.properties` or `application.yml` file:

**Using `application.properties`:**

```
# Set the default timezone to UTC
spring.jackson.time-zone=UTC
```

**Using `application.yml`:**

```
spring:
  jackson:
    time-zone: UTC
```

- This ensures that all JSON serialization/deserialization uses the default timezone. You can also configure the default timezone for other components globally through the configuration.

Alternatively, you can set it in the main Spring Boot class:

```
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.TimeZone;
@SpringBootApplication
public class Application implements CommandLineRunner {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
    @Override
    public void run(String... args) {
        // Set default timezone for the entire application
        TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
        System.out.println("Default Timezone: " + TimeZone.getDefault().getID());
    }
}
```

## **3. Set Default Timezone in Databases**

If you’re working with databases, it’s important to ensure your database and application are aligned with the default time zone:

**MySQL:**

- You can set the default time zone in MySQL by running the following query:

```
SET GLOBAL time_zone = '+00:00';  -- Set to UTC
```

- This ensures all timestamps in the database are stored in UTC and avoids timezone issues when querying or updating data.

**PostgreSQL:**

- For PostgreSQL, you can set the timezone for your session with:

```
SET TIMEZONE='UTC';
```

- Ensures that queries and stored data are processed in the correct timezone.

## **4. Set Time zone in Docker Containers**

If your application runs in Docker, you can set the default time zone by specifying the timezone during container startup:

```
docker run -e TZ=UTC my-app
```

- This ensures the container runs with the correct system time.

## **8. What is Inversion of Control?**

Inversion of Control (IoC) is a design principle in software engineering where the control of object creation, configuration, and management is transferred from the application code to an external system or framework.

This principle helps decouple components, making the system more modular, flexible, and testable.

In a traditional application, the flow of control is straightforward: you, the developer, call methods and manage object creation and their dependencies directly.

With IoC, the control is inverted. Instead of the application managing the creation and life cycle of its objects, an external component (such as a framework or container) takes responsibility for it.

## **Concepts:**

1. **Dependency Injection (DI)**:
- DI is one of the most common forms of IoC. It involves passing (or injecting) dependencies to an object at runtime rather than allowing the object to create the dependency itself.
- It allows objects to rely on abstractions instead of concrete implementations, making the system more flexible and easier to test.

**2. Event Handling**:

- In an event-driven application, the flow of control is inverted in the sense that the program’s execution flow is determined by events (user actions, messages, etc.), rather than a predefined sequence of instructions.

**3. Service Locator Pattern**:

- IoC can also be implemented using a service locator pattern, where a central registry manages the creation and retrieval of services, allowing decoupling between the caller and the service.

## **Working:**

1. **Traditional Flow (Without IoC)**:
- The application creates the object and manages its dependencies directly.

```
public class Car {
    private Engine engine;

    public Car() {
        this.engine = new Engine(); // Dependency created inside the class
    }
}
```

**2. With IoC (Using Dependency Injection)**:

- The framework or container creates and injects the `Engine` dependency into the `Car` class. The application no longer manages object creation.

```
public class Car {
    private Engine engine;

    // Dependency injected by an external IoC container
    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

## **Types:**

1. **Constructor Injection**: Dependencies are provided through the constructor.

```
public class Car {
    private Engine engine;

    // Constructor Injection
    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

**2. Setter Injection**: Dependencies are provided through setter methods after the object is constructed.

```
public class Car {
    private Engine engine;

    // Setter Injection
    public void setEngine(Engine engine) {
        this.engine = engine;
    }
}
```

**3. Interface Injection**: The class provides an injector method via an interface that the client class must implement.

## **Advantages:**

1. **Loose Coupling**:
- Classes are no longer tightly coupled to their dependencies. This makes the system more flexible, modular, and easier to change.

**2. Easier Testing**:

- By using IoC, it becomes easier to mock or stub dependencies for unit testing, as you can inject mock implementations of services instead of relying on real ones.

**3. Flexibility**:

- IoC allows easier configuration changes. For example, swapping out the `Engine` implementation for another one becomes simple without changing the `Car` class.

**4. Improved Code Maintainability**:

- With IoC, components are loosely coupled, making it easier to modify and maintain code over time.

## **Common Frameworks Implementing IoC:**

1. **Spring Framework** (Java)
- The Spring IoC container manages objects and their dependencies. It automatically handles the creation and injection of dependencies.

```
@Component public class Car {
     private Engine engine;

    @Autowired
    public Car(Engine engine) {
         this.engine = engine;
    }
 }
```

**2. Google Guice** (Java)

- Another popular framework for dependency injection that provides an IoC container.

## **9. What do you understand by error: “Application Context is not loading in runtime”?**

The error “Application Context is not loading in runtime” typically occurs in Spring-based applications, especially when using Spring Framework for dependency injection and other aspects of application context management.

This error can happen due to various reasons, often related to issues during the application startup.

## **Common Causes:**

1. **Configuration Issues:**
- The Spring `ApplicationContext` might not be able to load because the configuration files (e.g., `applicationContext.xml` or Java-based configuration) are missing, incorrectly defined, or have errors in them.
- **Example:** Missing or incorrect bean definitions, or a misconfigured Spring context (for example, if annotations like `@ComponentScan` are not set up properly).

**2. Component Scanning Issues:**

- If Spring is unable to find the necessary components or beans due to improper package scanning, it won’t be able to load the context. This can happen if you don’t specify the correct base package in `@ComponentScan` or misconfigure it in XML configuration.
- **Solution:** Make sure the base packages in `@ComponentScan` are correctly specified.

```
@SpringBootApplication(scanBasePackages = "com.example")
```

**3. Circular Dependencies:**

- If there are circular dependencies between beans, the Spring context may fail to load. This typically happens when Bean A depends on Bean B and vice versa.
- **Solution:** Resolve the circular dependency by refactoring the code or using `@Lazy` annotation to break the dependency cycle.

**4. Bean Creation Failures:**

- If one or more beans fail to be created during the initialization of the Spring context (e.g., due to incorrect constructor parameters, missing required dependencies, or errors in bean initialization), the context will fail to load.
- **Solution:** Check your logs for any `BeanCreationException` or similar exceptions. Ensure that all beans are properly defined and dependencies are correctly injected.

**5. Missing Spring Boot Starter Dependencies (in case of Spring Boot):**

- If you’re using Spring Boot and the application context isn’t loading, it could be because you’re missing necessary Spring Boot starter dependencies in your `pom.xml` or `build.gradle`.
- **Solution:** Verify that you have all required dependencies.

```
<dependency>
     <groupId>org.springframework.boot</groupId>
     <artifactId>spring-boot-starter</artifactId>
</dependency>
```

**6. Invalid Property Configurations:**

- If your application is dependent on external property files (`application.properties` or `application.yml`), and any of the required properties are missing or have invalid values, the application context might fail to load.
- **Solution:** Double-check your property configurations and ensure all required properties are present and correct.

**7. Version Mismatch or Incompatible Dependencies:**

- Mismatched versions of Spring Framework or Spring Boot and their dependencies can cause context loading failures. For example, an incompatible version of Spring Data or Spring Security could lead to this error.
- **Solution:** Ensure all Spring dependencies are compatible with each other, particularly if you’re using external libraries.

**8. ApplicationContext Not Properly Initialized (Manual Context Initialization Issues):**

- If you’re manually initializing the `ApplicationContext` in your application (rather than relying on Spring Boot's auto-configuration), you might encounter issues where the context isn't being loaded properly due to incorrect initialization.
- **Solution:** Ensure that you’re correctly initializing the `ApplicationContext`. For example:

```
AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
```

## **10. Suppose with the previous error you also get the error message: Unsatisfied dependency. What could be the reason for it?**

The error **“Unsatisfied dependency”** along with **“Application Context is not loading in runtime”** typically occurs when Spring is unable to inject the required dependencies into a bean during the application context initialization.

This error can happen for several reasons:

## **Common Causes:**

1. **Missing or Incorrect Bean Definitions:**
- If the bean you are trying to inject is not defined in the Spring context or has incorrect configuration, Spring won’t be able to inject it. This can happen if you forget to define the bean in a configuration file or annotate the class with an appropriate annotation like `@Component`, `@Service`, `@Repository`, or `@Configuration`.
- **Solution**: Ensure that all the required beans are properly defined and annotated, or listed in your XML configuration if you’re using XML-based configuration.

```
@Service
public class MyService {
     // bean definition
}
```

**2. Bean Not Available in Context:**

- The dependency that is being injected might not be available in the application context at the time of injection. This can happen when the class is not being scanned or registered in the Spring context, which is common in cases where the base package for `@ComponentScan` is not set properly.
- **Solution**: Ensure the class containing the required bean is in the correct package or is included in the `@ComponentScan` base package. For example:

```
@SpringBootApplication(scanBasePackages = "com.example")
```

**3. Ambiguous Bean Injection (Multiple Candidates):**

- If there are multiple beans of the same type in the context and Spring is unsure which one to inject, this can lead to an unsatisfied dependency error. For example, if two beans of type `MyService` are defined, Spring won’t know which one to inject.
- **Solution**: Use `@Qualifier` to specify which bean should be injected when there are multiple beans of the same type.

```
@Autowired
@Qualifier("myServiceImpl")
private MyService myService;
```

**4. Missing Constructor or Setter for Injection:**

- If you’re using constructor injection or setter injection, the dependency may not be injected properly if the required constructor or setter method is missing or misconfigured.
- **Solution**: Ensure that your class has the necessary constructor or setter for injection. For constructor injection, ensure that the constructor is annotated with `@Autowired` (if you're using Spring 4.3 or below, otherwise it's not needed).

```
@Service
public class MyService {
      private final MyRepository myRepository;

      @Autowired
      public MyService(MyRepository myRepository) {
         this.myRepository = myRepository;
  }
}
```

**5. Incorrect Scope or Proxy Issues:**

- If you’re using scoped beans (e.g., `@RequestScope`, `@SessionScope`, etc.) and injecting them into singleton beans, it may lead to issues where the dependency cannot be satisfied, since Spring won't be able to properly manage the lifecycle of the scoped beans.
- **Solution**: Ensure that beans with different scopes are injected correctly. If you need to inject a scoped bean into a singleton bean, consider using `@Lazy` or a proxy to resolve the issue.

**6. Component Scanning Exclusion:**

- Sometimes, Spring configuration might explicitly exclude certain packages or classes from component scanning, causing dependencies to be missing when Spring tries to inject them.
- **Solution**: Verify that your component scanning is configured correctly and that no packages or classes are excluded unintentionally.

**7. Context Initialization Order:**

- If you’re manually initializing the `ApplicationContext` (or using `@TestConfiguration` in test contexts), the order in which beans are loaded can affect dependency injection. If Spring tries to inject a dependency before the required bean is available, it will fail.
- **Solution**: Check the initialization sequence and ensure that all beans are loaded before they are needed for injection.

**8. Dependency on a Non-Spring Bean:**

- If your class depends on a non-Spring managed bean, Spring won’t be able to inject it and will throw an unsatisfied dependency error.
- **Solution**: Make sure all dependencies injected into Spring beans are managed by Spring. If necessary, wrap external dependencies into Spring beans using `@Component`, `@Service`, or another appropriate annotation.

## **Example of “Unsatisfied Dependency” Error and Resolution:**

**Example Error:**

```
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'myService': Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'myRepository': Injection of autowired dependencies failed
```

**Solution:**

1. Verify that `MyRepository` is a valid Spring bean (`@Repository` or `@Component`).
2. Ensure that `MyRepository` is available in the package scanned by Spring (`@ComponentScan`).
3. Ensure there is no ambiguity in bean definitions (i.e., only one bean of type `MyRepository` exists).
4. Check the constructor or setter of `MyService` and ensure that `MyRepository` is properly injected.

## **11. What is a Stream in Java?**

A Stream in Java is a sequence of elements that supports functional-style operations for processing data.

It was introduced in Java 8 as part of the java.util.stream package and allows for concise, readable, and efficient manipulation of collections (like `List`, `Set`, etc.).

## **Characteristics:**

1. **Not a Data Structure**
- A stream is *not* a data structure or a collection. It doesn’t store elements.
- Instead, it *conveys* elements from a data source (like a collection, array, or I/O channel) through a pipeline of operations.

**2. Functional in Nature**

- You can perform operations like map, filter, reduce, and more using lambda expressions or method references.

**3. Lazy Evaluation**

- Intermediate operations (like `map()` or `filter()`) are **lazy**. They are not executed until a terminal operation like `collect()` or `forEach()` is invoked.

**4. Can be Parallel or Sequential**

- You can process streams in parallel using `parallelStream()`, which helps utilize multicore processors.

## **Types:**

1. **Sequential Stream** — Processes elements one by one (default).
2. **Parallel Stream** — Processes elements concurrently (using multiple threads).

## **Common Stream Operations:**

**a. Intermediate Operations (return a Stream):**

- `filter(Predicate)` – filters elements.
- `map(Function)` – transforms elements.
- `sorted()` – sorts elements.
- `distinct()` – removes duplicates.

**b. Terminal Operations (return a result or side-effect):**

- `collect(Collectors.toList())` – collects results.
- `forEach(Consumer)` – performs an action for each element.
- `reduce(BinaryOperator)` – reduces to a single value.
- `count()` – counts elements.

## **Example:**

```
List<String> names = Arrays.asList("John", "Jane", "Jack", "Jill");

List<String> filteredNames = names.stream()
    .filter(name -> name.startsWith("J"))
    .map(String::toUpperCase)
    .sorted()
    .collect(Collectors.toList());
System.out.println(filteredNames);
// Output: [JACK, JANE, JILL, JOHN]
```

## **Advantages:**

- More readable and concise code (compared to for-loops).
- Encourages functional programming style.
- Allows easy chaining of operations.
- Supports parallel processing.

## **When Not to Use Streams:**

- When performance tuning matters and you need full control over iteration.
- When you need indexed access to elements (like accessing list[i]).
- For operations that cause side effects or rely on mutation (streams are best for stateless operations).

**12. What are the differences between Stream vs Collections.**

![](https://d9b7jaj92i1k2y.archive.ph/amNlX/f27173c9a0e6505d6a6a26f6ce19bb190f9faaf9.webp)