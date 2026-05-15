# Interview questions collected by the linkedin candidates

1 List of string sort using the number of vowels counting in java

```java
import java.util.*; // Import utility classes for List and Comparator

public class VowelSort {
    public static void main(String[] args) {
        // Create a list of strings to be sorted
        List<String> words = Arrays.asList("apple", "banana", "grape", "orange");

        // Sort the list using a custom comparator that compares vowel counts
        words.sort(Comparator.comparingInt(VowelSort::countVowels));

        // Print the sorted list
        System.out.println(words); // Output: [grape, apple, banana, orange]
    }

    // Method to count vowels in a given string
    static int countVowels(String str) {
        int count = 0; // Initialize vowel count

        // Convert string to lowercase and loop through each character
        for (char c : str.toLowerCase().toCharArray()) {
            // Check if the character is a vowel
            if ("aeiou".indexOf(c) != -1) {
                count++; // Increment count if it's a vowel
            }
        }

        return count; // Return the total number of vowels
    }
}

```

1. We have a set of users and role permissions defined. You need to build a Spring Boot project with a local SQL database containing the users. I need a working set of CRUD APIs to manage permissions, map them to users, and manage user roles. One user can have multiple roles, so you need to establish this relationship using Hibernate and connect it to the local database. The APIs should allow CRUD operations on users and roles, including attaching and removing roles from users, by ID or by name. The project should expose these functionalities as REST APIs in Java Spring Boot.

Here's a concise plan with code snippets to help you build the Spring Boot project where:

- A **user can have multiple roles**
- You’ll perform **CRUD operations on roles**
- You’ll **assign/remove roles** for users
- All data is stored in a **local SQL DB**
- Uses **Hibernate (JPA)** for relationships
- Expose **REST APIs** for everything

User.java

```java
@Entity
public class User {
    @Id @GeneratedValue
    private Long id;
    private String name;

    @ManyToMany
    @JoinTable(
        name = "user_roles",
        joinColumns = @JoinColumn(name = "user_id"),
        inverseJoinColumns = @JoinColumn(name = "role_id")
    )
    private Set<Role> roles = new HashSet<>();

    // Getters, Setters, Constructors
}

```

Role.java

```java
@Entity
public class Role {
    @Id @GeneratedValue
    private Long id;
    private String name;

    // Getters, Setters, Constructors
}

```

Repositories

```java
public interface UserRepository extends JpaRepository<User, Long> {}

public interface RoleRepository extends JpaRepository<Role, Long> {
    Optional<Role> findByName(String name);
}

```

Service Layer (Example: RoleService)

```java
@Service
public class RoleService {
    @Autowired private RoleRepository roleRepo;

    public Role create(Role role) { return roleRepo.save(role); }
    public List<Role> getAll() { return roleRepo.findAll(); }
    public Role getById(Long id) { return roleRepo.findById(id).orElseThrow(); }
    public Role getByName(String name) { return roleRepo.findByName(name).orElseThrow(); }
    public void delete(Long id) { roleRepo.deleteById(id); }
}

```

User Role Assignment Methods In `UserService`:

```java
@Autowired private UserRepository userRepo;
@Autowired private RoleRepository roleRepo;

public User assignRole(Long userId, Long roleId) {
    User user = userRepo.findById(userId).orElseThrow();
    Role role = roleRepo.findById(roleId).orElseThrow();
    user.getRoles().add(role);
    return userRepo.save(user);
}

public User removeRole(Long userId, Long roleId) {
    User user = userRepo.findById(userId).orElseThrow();
    Role role = roleRepo.findById(roleId).orElseThrow();
    user.getRoles().remove(role);
    return userRepo.save(user);
}

```

### 5. Controllers

### `RoleController`

```java
@RestController
@RequestMapping("/roles")
public class RoleController {
    @Autowired private RoleService roleService;

    @PostMapping public Role create(@RequestBody Role r) { return roleService.create(r); }
    @GetMapping public List<Role> getAll() { return roleService.getAll(); }
    @GetMapping("/{id}") public Role get(@PathVariable Long id) { return roleService.getById(id); }
    @GetMapping("/name/{name}") public Role getByName(@PathVariable String name) { return roleService.getByName(name); }
    @DeleteMapping("/{id}") public void delete(@PathVariable Long id) { roleService.delete(id); }
}

```

UserRoleController

```java
@RestController
@RequestMapping("/users")
public class UserRoleController {
    @Autowired private UserService userService;

    @PostMapping("/{userId}/roles/{roleId}") // Assign role
    public User assign(@PathVariable Long userId, @PathVariable Long roleId) {
        return userService.assignRole(userId, roleId);
    }

    @DeleteMapping("/{userId}/roles/{roleId}") // Remove role
    public User remove(@PathVariable Long userId, @PathVariable Long roleId) {
        return userService.removeRole(userId, roleId);
    }
}

```

6. application.properties (for MySQL/PostgreSQL/Local DB)

```java
spring.datasource.url=jdbc:mysql://localhost:3306/your_db
spring.datasource.username=root
spring.datasource.password=your_password
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

```

TSYS Java developer interview Questions

1. Which functional interface was introduced in Java 8?

In Java 8, several **functional interfaces** were introduced (in the `java.util.function` package) to support **lambda expressions** and functional-style programming. Here are the main ones:

---

### **Core Functional Interfaces in Java 8**

| Interface | Input | Output | Description |
| --- | --- | --- | --- |
| **`Function<T, R>`** | T | R | Takes a value and returns a result. |
| **`Consumer<T>`** | T | void | Performs an operation on the given argument, no return. |
| **`Supplier<T>`** | None | T | Provides a result without taking any input. |
| **`Predicate<T>`** | T | boolean | Tests a condition and returns true/false. |

### **Examples**

### 1. **Function**

```java
Function<String, Integer> lengthFunc = str -> str.length();
System.out.println(lengthFunc.apply("TSYS"));  // Output: 4

```

2. **Consumer**

```java
Consumer<String> printer = msg -> System.out.println("Hello, " + msg);
printer.accept("Shivam");  // Output: Hello, Shivam

```

**3. Supplier**

```java
Supplier<Double> randomSupplier = () -> Math.random();
System.out.println(randomSupplier.get());  // Output: (some random number)

```

4. **Predicate**

```java
Predicate<Integer> isEven = num -> num % 2 == 0;
System.out.println(isEven.test(10));  // Output: true

```

### **ther Useful Functional Interfaces**

- **BiFunction<T, U, R>**: Takes two inputs and returns a result.
- **BiConsumer<T, U>**: Takes two inputs, returns nothing.
- **UnaryOperator<T>**: A Function where input and output are the same type.
- **BinaryOperator<T>**: Takes two same-type inputs and returns the same type.

1. What is callable in java 

### **`Callable` in Java**

`Callable` is a **functional interface** introduced in Java 5 (not Java 8), but it's often used in **concurrent programming**, especially with **Executors**.

---

### **Key Points about `Callable`**

| Feature | Description |
| --- | --- |
| **Package** | `java.util.concurrent` |
| **Method** | `T call() throws Exception` |
| **Returns** | A result of type `T` |
| **Can Throw** | Checked exceptions |

---

### **Difference Between `Callable` and `Runnable`**

| Feature | `Runnable` | `Callable` |
| --- | --- | --- |
| Return value | No | Yes (generic type) |
| Exception | Cannot throw checked | Can throw checked exceptions |
| Method | `run()` | `call()` |

```java
import java.util.concurrent.*;

public class CallableExample {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();

        Callable<String> task = () -> {
            Thread.sleep(1000);
            return "Hello from Callable!";
        };

        Future<String> future = executor.submit(task);

        // Do something else if needed...

        String result = future.get();  // Blocks until result is available
        System.out.println(result);    // Output: Hello from Callable!

        executor.shutdown();
    }
}

```

### When to Use `Callable`

- When you need to **return a result from a thread**
- When you need to **handle exceptions from threads**
- For tasks involving **delayed or parallel execution**

1. What is concurrency and multithreading

### **Multithreading vs Concurrency**

| Aspect | **Multithreading** | **Concurrency** |
| --- | --- | --- |
| **Definition** | Running multiple threads in the **same process** | Handling multiple tasks **at the same time** (may or may not be in parallel) |
| **Goal** | Better CPU utilization, responsiveness | Efficient task management and resource sharing |
| **Example** | A web server using a thread per client | Switching between client requests quickly, even with one thread |
| **Key Java Support** | `Thread`, `Runnable`, `ExecutorService` | `synchronized`, `volatile`, thread pools, `Callable`, `Future`, `CompletableFuture`, etc. |

### **n Simple Terms:**

- **Multithreading** = actually running **multiple threads**.
- **Concurrency** = the idea that you're working on **many things at once**, even if just one CPU core.

### **Java Tools for Both**

### 1. **Thread**

```java
Thread t = new Thread(() -> System.out.println("Running in thread"));
t.start();

```

### 2. **Runnable / Callable with ExecutorService**

```java
ExecutorService executor = Executors.newFixedThreadPool(2);
executor.submit(() -> System.out.println("Runnable task"));
executor.shutdown();

```

### 3. **synchronized**

```java
synchronized void increment() {
    count++;
}

```

### 4. **volatile**

```java
volatile boolean flag = true;

```

1. **difference between concurrent execution and multithreaded execution** in Java

Scenario: You want to download 3 files.

1. Sequential (No concurrency, no multithreading)

```java
public class SequentialDownload {
    public static void main(String[] args) {
        FileDownloader.download("File1");
        FileDownloader.download("File2");
        FileDownloader.download("File3");
    }
}

class FileDownloader {
    public static void download(String fileName) {
        System.out.println("Downloading " + fileName);
        try { Thread.sleep(1000); } catch (InterruptedException e) {}
        System.out.println("Finished " + fileName);
    }
}

```

output  :

Downloading File1
Finished File1
Downloading File2
Finished File2
Downloading File3
Finished File3

Takes ~3 seconds total. No concurrency here — one file at a time.

Concurrent via Multithreading

```java
public class ConcurrentDownload {
    public static void main(String[] args) {
        Thread t1 = new Thread(new FileDownloader("File1"));
        Thread t2 = new Thread(new FileDownloader("File2"));
        Thread t3 = new Thread(new FileDownloader("File3"));

        t1.start();
        t2.start();
        t3.start();
    }
}

class FileDownloader implements Runnable {
    private String fileName;

    public FileDownloader(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void run() {
        System.out.println("Downloading " + fileName);
        try { Thread.sleep(1000); } catch (InterruptedException e) {}
        System.out.println("Finished " + fileName);
    }
}

```

output : 

Downloading File1
Downloading File2
Downloading File3
Finished File2
Finished File1
Finished File3

Takes ~1 second total. All downloads run **concurrently using multiple threads**.

1. Difference Between `HashMap` and `ConcurrentHashMap`

| Feature | `HashMap` | `ConcurrentHashMap` |
| --- | --- | --- |
| **Thread-safe** | **No** | **Yes** |
| **Performance in multi-threading** | Causes issues (e.g., race conditions, `ConcurrentModificationException`) | Safe for use by multiple threads |
| **Null keys/values** | Allows **1 null key** and multiple null values | **Does not allow** null keys or values |
| **Locking Mechanism** | No internal locking | Uses **bucket-level locking** (since Java 8: lock splitting + CAS) |
| **Fail-fast behavior** | Iterators throw `ConcurrentModificationException` if modified during iteration | Iterators are **weakly consistent** (don’t throw exceptions) |
| **Use case** | Single-threaded or externally synchronized | Multi-threaded environments (web apps, APIs, background tasks) |

Example of Thread Issue with `HashMap`

```java
Map<String, String> map = new HashMap<>();

Thread t1 = new Thread(() -> map.put("A", "1"));
Thread t2 = new Thread(() -> map.put("B", "2"));

t1.start();
t2.start();

```

This might work — **or might corrupt the map**, depending on timing.

Same with `ConcurrentHashMap`

```java
Map<String, String> map = new ConcurrentHashMap<>();

Thread t1 = new Thread(() -> map.put("A", "1"));
Thread t2 = new Thread(() -> map.put("B", "2"));

t1.start();
t2.start();

```

Safe and reliable. No corruption, even with multiple threads.

---

### **Summary**

Use:

- `HashMap` → for **non-threaded** code
- `ConcurrentHashMap` → for **multi-threaded** environments, like web servers or background jobs

1. How does ConcurrentHashMap work internally to achieve concurrency?

### **How `ConcurrentHashMap` Works Internally (Java 8+)**

In Java 8, `ConcurrentHashMap` uses a combination of:

- **Bucket-level locking** (lock splitting)
- **CAS (Compare-And-Swap)** for basic operations
- **Segmented structure** replaced by **array of Nodes + fine-grained locking**

---

### **Key Concepts**

### 1. **No Global Lock**

- Unlike `Collections.synchronizedMap()`, it doesn't lock the whole map.
- Instead, it locks only a **small portion** (a bin/bucket or a node) when needed.

### 2. **CAS for Non-Blocking Reads/Writes**

- Uses **Compare-And-Swap** for atomic updates without locking.
- Example: `putIfAbsent()` is implemented using CAS for atomic safety.

### 3. **Buckets = Nodes in an Array**

- Internally, it's like an array of buckets: `Node<K,V>[] table`
- Each bucket can hold a linked list (or a tree if hash collisions occur).

### 4. **Synchronized Only When Needed**

- Writes like `put()` **synchronize only on the bucket** being modified.
- Multiple threads can safely write to different buckets **concurrently**.

### 5. **Reads are Lock-Free**

- `get()` is **non-blocking** — it doesn’t acquire a lock.
- Reads are thread-safe due to volatile variables and memory visibility guarantees.

### 6. **TreeBin for Hash Collisions**

- If too many keys hash to the same bucket (threshold > 8), it becomes a **TreeBin** (red-black tree) for performance.
- Even the tree is handled with fine-grained locks.

ConcurrentHashMap
└── Node<K,V>[] table (like HashMap)
├── [0] -> Node(key1, val1) -> Node(key2, val2)
├── [1] -> TreeBin (Red-Black Tree)
├── [2] -> null
└── [n] -> Node(keyX, valX)

Each array index can be accessed/modified independently using locks or CAS, allowing **high concurrency**.

---

### **Summary**

- Uses **fine-grained locking** and **non-blocking algorithms**
- Much **faster and scalable** than a synchronized `HashMap`
- Safe for **concurrent access** without external synchronization

1. Why `HashMap` Is Not Thread-Safe

`HashMap` is designed for **single-threaded use**, and **doesn't use any synchronization internally**.

### Here's what can go wrong in multi-threaded environments:

---

### **1. Data Corruption (Race Conditions)**

If two threads call `put()` at the same time:

- They may **overwrite** each other’s data.
- Intermediate states may be seen.
- Internal array (`Node[] table`) may get corrupted.

---

### **2. Infinite Loops / CPU Spike (Pre-Java 8)**

In older Java versions, concurrent `put()` operations could:

- Cause a **circular linked list** inside a bucket (when resizing occurs)
- Lead to an **infinite loop** during iteration — 100% CPU usage

### **3. `ConcurrentModificationException`**

Even during simple iteration:

```java
for (Map.Entry<K,V> e : map.entrySet()) {
    map.put(newKey, newValue);  // Throws exception
}

```

You get a **fail-fast error** if the map is modified while iterating — not thread-safe.

---

### **No Safeguards Against:**

- Simultaneous reads and writes
- Hash collisions under load
- Iterator consistency

---

### **Conclusion:**

**`HashMap` is not thread-safe** because:

- No synchronization or locks are used
- Internal structure (array, linked list, etc.) can be corrupted
- Iterators fail fast on concurrent modification

---

**Fixes:**

- Use `Collections.synchronizedMap(new HashMap<>())` (adds external locking)
- Or better: use **`ConcurrentHashMap`** — designed for concurrency with internal lock splitting and CAS.

1. POST API which accepts a query parameter, one path parameter, and one request header in a POST mapping in Java.

Absolutely! Here's a simple **Java Spring Boot** example of a **POST API** that accepts:

- One **path parameter**
- One **query parameter**
- One **request header**

---

### **Example:**

Let’s say you want an API like this:

```
POST /user/123?status=active
Header: X-App-Version: v1.2

```

Spring Boot Controller Code:

```java
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
public class UserController {

    @PostMapping("/{userId}")
    public String handleUserRequest(
            @PathVariable("userId") String userId,                          // Path param
            @RequestParam("status") String status,                         // Query param
            @RequestHeader("X-App-Version") String appVersion              // Header
    ) {
        return "User ID: " + userId +
               ", Status: " + status +
               ", App Version: " + appVersion;
    }
}

```

### **How to Call This API:**

- **URL:** `POST /user/123?status=active`
- **Header:** `X-App-Version: v1.2`

1. POST API which accepts a query parameter, one path parameter, one request header, and a PDF file, and returns a PNG file, implemented using POST mapping in Java.

Perfect — you want to build a **POST API** in **Spring Boot** that:

- Accepts a **PDF file** (multipart/form-data)
- Accepts a **path param**, a **query param**, and a **request header**
- **Returns a PNG** file as a response

Controller :

```java
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;

@RestController
@RequestMapping("/file")
public class FileController {

    @PostMapping(value = "/{userId}", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<byte[]> convertPdfToPng(
            @PathVariable String userId,                              // Path param
            @RequestParam("status") String status,                    // Query param
            @RequestHeader("X-App-Version") String appVersion,        // Header
            @RequestParam("file") MultipartFile file                  // PDF file
    ) {
        try {
            // Simulate converting PDF to PNG (just for example)
            // In real use, you’d use libraries like PDFBox or iText + ImageIO

            byte[] pngBytes = dummyConvertToPng(file); // Placeholder for real logic

            return ResponseEntity.ok()
                    .contentType(MediaType.IMAGE_PNG)
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"converted.png\"")
                    .body(pngBytes);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(null);
        }
    }

    // Dummy converter: in real case, convert PDF to PNG using a library
    private byte[] dummyConvertToPng(MultipartFile file) throws IOException {
        // For now, just return the PDF bytes as placeholder
        return file.getBytes();  // Replace with actual image conversion logic
    }
}

```

### **API Request Format**

- **URL:** `POST /file/123?status=active`
- **Header:** `X-App-Version: v1.0`
- **Body:** `multipart/form-data` with a key named `file` and a PDF file

---

### **How to Really Convert PDF to PNG?**

You can use:

- **Apache PDFBox** to render pages to image
- **iText + Java2D**
- Or **Ghostscript (external tool)**

1. What is the Singleton design pattern?

The **Singleton Design Pattern** is one of the **creational patterns** that ensures a **class has only one instance** and provides a **global point of access** to that instance.

### **Key Characteristics:**

1. **Single Instance**: Only one instance of the class is created throughout the application's lifecycle.
2. **Global Access**: Provides a global point to access the instance, typically through a static method.

### **Common Uses:**

- **Logging**: A logging class that should only have one instance.
- **Configuration Settings**: Centralized configuration management.
- **Database Connection Pooling**: A single connection manager for all database interactions.

---

### **Steps to Implement Singleton Pattern:**

### **1. Eager Initialization (Thread-safe)**

In this approach, the instance is created **when the class is loaded** (i.e., during class initialization).

```java
public class Singleton {
    // Eager initialization
    private static final Singleton instance = new Singleton();

    // Private constructor to prevent instantiation from outside
    private Singleton() {}

    // Static method to get the single instance
    public static Singleton getInstance() {
        return instance;
    }
}

```

### **2. Lazy Initialization (Thread-Safe)**

Here, the instance is created **only when it is first requested**. We need to ensure thread safety when multiple threads attempt to access the instance simultaneously.

```java
public class Singleton {
    // Volatile ensures visibility across threads
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) { // Double-checked locking
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}

```

### **3. Bill Pugh Singleton (Best Practice)**

This uses a **static inner class** to implement the Singleton in a **thread-safe** and **lazy-loaded** manner.

```java
public class Singleton {
    private Singleton() {}

    // Static inner class responsible for holding the Singleton instance
    private static class SingletonHelper {
        // The instance is created when this class is loaded
        private static final Singleton instance = new Singleton();
    }

    // Public method to get the instance
    public static Singleton getInstance() {
        return SingletonHelper.instance;
    }
}

```

**Why it’s good:**

- The **instance is created lazily** (only when `getInstance()` is called for the first time).
- It’s **thread-safe** because the **inner static class** is loaded only
- when it’s referenced, and the class loader ensures thread safety.
- **No synchronization** needed, making it more efficient than other methods.

---

### **When to Use Singleton Pattern:**

- **One Instance**: When you need **one instance** of a class to manage the shared resource (e.g., logging, configuration).
- **Global Access**: If you need a **global point of access** to an object.
- **State Sharing**: If you want to **share state** across different parts of the system.

---

### **Disadvantages:**

- **Global State**: Makes testing and maintenance harder since the instance is global.
- **Hidden Dependencies**: Other classes may rely on the Singleton, but this dependency is hidden.

1. Code Implementation for the singleton class

Sure! Below is the **core implementation** of a Singleton class in Java. I'll demonstrate a **thread-safe** Singleton using the **Bill Pugh Singleton Design Pattern**, which is often considered the best approach.

### **Bill Pugh Singleton Implementation:**

This implementation uses a **static inner class** to achieve **lazy initialization** and **thread safety** without using synchronization.

```java
public class Singleton {

    // Private constructor to prevent instantiation from other classes
    private Singleton() {}

    // Static inner class responsible for holding the Singleton instance
    private static class SingletonHelper {
        // This is where the Singleton instance is created
        private static final Singleton INSTANCE = new Singleton();
    }

    // Public method to provide access to the instance
    public static Singleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}

```

### **Explanation:**

1. **Private Constructor**:
    
    The `Singleton` constructor is **private** to prevent instantiation from outside the class.
    
2. **Static Inner Class**:
    
    The `SingletonHelper` class is **static**, which ensures it is only loaded when `getInstance()` is called for the first time. This means the Singleton is created **lazily**, only when it's needed.
    
3. **Singleton Instance**:
    
    The `INSTANCE` field inside `SingletonHelper` is where the actual **Singleton instance** is created. This is thread-safe due to the class loader mechanism. The instance will only be created once, even in a multi-threaded environment.
    
4. **Global Access**:
    
    The `getInstance()` method provides the **global access point** to the Singleton instance.
    

```java
public class Main {
    public static void main(String[] args) {
        // Access the Singleton instance
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();

        // Check if both instances are the same
        System.out.println(singleton1 == singleton2); // This should print true
    }
}

```

### **Why This Approach is Thread-Safe:**

- The **static inner class** is only loaded when the `getInstance()` method is called. This ensures that the **Singleton instance** is created only once, even in a multi-threaded environment, without the need for synchronization or locks.

---

### **Advantages of this Approach:**

- **Thread-safe** without synchronization.
- **Lazy initialization** — the Singleton is created only when needed.
- **No need for `synchronized`** blocks, making it more efficient than other methods like double-checked locking.

Yes — the **Bill Pugh Singleton** implementation **is thread-safe**, and here’s **why**:

---

### **Why Bill Pugh Singleton Is Thread-Safe**

### 1. **Classloader Guarantees**

- The **static inner class (`SingletonHelper`)** is **not loaded** into memory until it's actually referenced.
- When `getInstance()` is called for the first time, the JVM loads the `SingletonHelper` class **once and only once**, in a **thread-safe** manner — guaranteed by the **Java ClassLoader**.

### 2. **No Synchronization Needed**

- Unlike double-checked locking, you don’t need `synchronized` blocks.
- It’s **more efficient**, as no thread waits once the instance is initialized.

```java
public class Singleton {
    private Singleton() {} // private constructor

    private static class SingletonHelper {
        private static final Singleton INSTANCE = new Singleton(); // thread-safe
    }

    public static Singleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}

```

- The Singleton instance is created **only when** `SingletonHelper.INSTANCE` is first accessed.
- The JVM ensures that the static field is initialized **once** and is **visible to all threads** (because it's a final static field).

---

### **In Simple Terms:**

- It’s **lazy-loaded**
- It’s **thread-safe**
- It avoids **explicit synchronization**
- It’s **efficient**

1. How does it make the Singleton thread-safe? Suppose there is a fixed thread pool with 20 threads—how does it work in that case?

## **So — How Is Bill Pugh Singleton Thread-Safe Even with a 20-Thread Pool?**

Let’s say you have a fixed thread pool of 20 threads — and all 20 threads **simultaneously** call:

```java
Singleton instance = Singleton.getInstance();

```

### **What Actually Happens Behind the Scenes:**

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
    
    ## **So, Even with 20 Threads:**
    
    - Only **one thread** will trigger the actual class loading of `SingletonHelper`.
    - The other 19 threads will **wait silently** during the classloading process — **they don’t see a partially constructed object**.
    - Once done, **all threads get the exact same Singleton object**.
    
    ---
    
    ## **How JVM Makes This Possible**
    
    The magic lies in:
    
    - **ClassLoader’s thread safety guarantees**
    - **Final static field initialization** (memory visibility is guaranteed for all threads)
    - **Happens-before relationship** established by class initialization rules in Java Memory Model (JMM)
    
    ---
    
    ### **TL;DR:**
    
    Even if **all 20 threads** try to access `Singleton.getInstance()` at once:
    
    - **Only one thread** will initialize the Singleton (via class loading)
    - The rest will wait and then get the same instance
    - **No race conditions, no broken state, no synchronization overhead**

1. How is the Singleton safe from cloning?

### **Short Answer:**

**It’s not safe from cloning unless you explicitly protect it.**

By default, if your Singleton class **implements `Cloneable`**, then calling `clone()` can break Singleton — it will return a **new object**, violating the Singleton rule.

---

### **How to Make Singleton Safe from Cloning**

You prevent cloning by **overriding `clone()`** in your Singleton class and throwing an exception.

Update Your Singleton Class Like This:

```java
public class Singleton implements Cloneable {

    private Singleton() {}

    private static class SingletonHelper {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return SingletonHelper.INSTANCE;
    }

    // Prevent cloning
    @Override
    protected Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException("Singleton: Cloning not allowed");
    }
}

```

Without This Protection:

```java
Singleton s1 = Singleton.getInstance();
Singleton s2 = (Singleton) s1.clone(); // NEW INSTANCE created!
System.out.println(s1 == s2); // false – Singleton is broken!

```

1. Let's say an Employee object has fields like id, name, age, and department. Your employee list consists of these Employee objects. You need to first group the employees based on their department, and then within each department group, further group them based on their age. For example, group the employees in the HR and IT departments first by department, and then group them by age within each department using the Stream API.

### **Problem:**

You have a list of `Employee` objects with fields:

- `id`
- `name`
- `age`
- `department`

You need to:

1. Group employees **by department** (e.g., HR, IT)
2. Inside each department group, further group employees **by age**

```java
Map<String, Map<Integer, List<Employee>>> groupedData = 
    employeeList.stream()
        .collect(Collectors.groupingBy(
            Employee::getDepartment,                        // First group by department
            Collectors.groupingBy(Employee::getAge)         // Then group by age inside each department
        ));

```

This gives you a **nested map structure** like:

```java
{
  "HR": {
    25: [Emp1, Emp2],
    30: [Emp3]
  },
  "IT": {
    22: [Emp4],
    25: [Emp5, Emp6]
  }
}

```

### **Full Working Example:**

### **1. Employee Class:**

```java
public class Employee {
    private int id;
    private String name;
    private int age;
    private String department;

    // Constructor
    public Employee(int id, String name, int age, String department) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.department = department;
    }

    // Getters
    public int getId() { return id; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getDepartment() { return department; }
}

```

2. Grouping Logic:

```java
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Employee> employeeList = List.of(
            new Employee(1, "Alice", 25, "HR"),
            new Employee(2, "Bob", 30, "HR"),
            new Employee(3, "Charlie", 25, "HR"),
            new Employee(4, "David", 22, "IT"),
            new Employee(5, "Eva", 25, "IT"),
            new Employee(6, "Frank", 25, "IT")
        );

        Map<String, Map<Integer, List<Employee>>> grouped = employeeList.stream()
            .collect(Collectors.groupingBy(
                Employee::getDepartment,
                Collectors.groupingBy(Employee::getAge)
            ));

        // Print the grouped map
        grouped.forEach((dept, ageMap) -> {
            System.out.println("Department: " + dept);
            ageMap.forEach((age, employees) -> {
                System.out.println("  Age: " + age);
                employees.forEach(e -> System.out.println("    " + e.getName()));
            });
        });
    }
}

```

Output:

```java
Department: HR
  Age: 25
    Alice
    Charlie
  Age: 30
    Bob
Department: IT
  Age: 22
    David
  Age: 25
    Eva
    Frank

```

1. What are the different operators in Stream?

## **1. Intermediate Operations**

These **return a Stream** (they’re lazy — nothing executes until a terminal operation is called).

| Operator | Description |
| --- | --- |
| `.filter()` | Filters elements based on a predicate (e.g. `e -> e.getAge() > 25`) |
| `.map()` | Transforms each element (e.g. `e -> e.getName()`) |
| `.flatMap()` | Flattens nested structures (e.g. List<List<String>> to List<String>) |
| `.distinct()` | Removes duplicates using `equals()` and `hashCode()` |
| `.sorted()` | Sorts stream elements (with or without comparator) |
| `.limit(n)` | Limits the number of elements |
| `.skip(n)` | Skips the first `n` elements |
| `.peek()` | Used for debugging — performs an action on each element |

## **2. Terminal Operations**

These **trigger** the stream processing and return a final result (or side effect).

| Operator | Description |
| --- | --- |
| `.forEach()` | Iterates over each element (used for side effects) |
| `.collect()` | Collects results into List, Set, Map, etc. |
| `.toArray()` | Converts the stream into an array |
| `.reduce()` | Reduces the stream to a single value (e.g., sum) |
| `.count()` | Returns the count of elements |
| `.min()` / `.max()` | Finds the min or max element using a comparator |
| `.anyMatch()` | Checks if **any** element matches a condition |
| `.allMatch()` | Checks if **all** elements match a condition |
| `.noneMatch()` | Checks if **no** elements match a condition |
| `.findFirst()` | Returns the **first** element (optional) |
| `.findAny()` | Returns **any** element (useful in parallel streams) |

Example for Each Type:

```java
List<String> names = List.of("Alice", "Bob", "Charlie", "Bob");

names.stream()
    .filter(name -> name.startsWith("B"))         // intermediate
    .distinct()                                   // intermediate
    .map(String::toUpperCase)                     // intermediate
    .sorted()                                     // intermediate
    .forEach(System.out::println);                // terminal

```

1. Solid principles in Java

## **SOLID Principles in Java**

### **S – Single Responsibility Principle (SRP)**

**A class should have only one reason to change.**

- Each class should do **only one job**.
- Keeps classes focused and reduces coupling.

**Example:**

```java
class ReportPrinter {
    public void printReport() { /* printing logic */ }
}

class ReportSaver {
    public void saveToFile() { /* save logic */ }
}

```

**Why?** Don't let one class handle both printing and saving — separate concerns!

---

### **O – Open/Closed Principle (OCP)**

**Software entities should be open for extension but closed for modification.**

- Add new behavior **without modifying existing code**.
- Use **interfaces** or **abstract classes** + **polymorphism**.

```java
interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    public void send(String message) { /* email logic */ }
}

class SMSNotification implements Notification {
    public void send(String message) { /* SMS logic */ }
}

```

Now we can add more notification types without changing existing code.

---

### **L – Liskov Substitution Principle (LSP)**

**Subtypes must be substitutable for their base types.**

- A child class should behave like its parent without breaking the program.
- Don’t override methods in a way that breaks expected behavior.

**Bad Example:**

```java
class Bird {
    void fly() {}
}

class Ostrich extends Bird {
    void fly() { throw new UnsupportedOperationException(); } // Violates LSP
}

```

**Fix:** Refactor base class so it makes sense to all children.

---

### **I – Interface Segregation Principle (ISP)**

**Clients should not be forced to implement interfaces they do not use.**

- Break large interfaces into **smaller, role-specific interfaces**.

**Bad:**

```java
interface Animal {
    void fly();
    void run();
    void swim();
}

```

**Good:**

```java
interface Runnable {
    void run();
}

interface Swimmable {
    void swim();
}

```

Now classes only implement what they actually need.

---

### **D – Dependency Inversion Principle (DIP)**

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

- Don’t hardcode dependencies — depend on **interfaces or abstract classes**.

**Bad:**

```java
class OrderService {
    private EmailSender emailSender = new EmailSender();
}

```

**Good:**

```java
class OrderService {
    private NotificationSender sender;

    public OrderService(NotificationSender sender) {
        this.sender = sender;
    }
}

```

## **How to Remember SOLID:**

- **S**ingle job
- **O**pen to extend, closed to change
- **L**et subclasses behave properly
- **I**nterfaces should be focused
- **D**epend on abstraction

1. You have a sentence. Using a lambda expression, write code to count how many words are in the sentence.

Eureka forbes java developer interview experience

How would you scale this API for Astrotalk?

### ✅ Interview-Ready Answer:

**To scale the API for Astrotalk**, which deals with real-time consultations, user matchmaking, chat, and payments:

1. **Use API Gateway + Load Balancer**
    - Route and balance traffic across multiple backend instances.
    - Handle throttling, rate limits, and auth centrally.
2. **Decompose into Microservices**
    - Separate services for User, Astrologer, Chat, Session Booking, Payment.
    - Each service can scale independently based on load.
3. **Use Caching (Redis)**
    - Cache frequently accessed astrologer profiles, availability, and FAQs.
    - Reduces DB hits and improves latency.
4. **Async Messaging (Kafka)**
    - For chat logs, notifications, and analytics — ensures non-blocking flow.
    - Smooth handling of spikes during events or promotions.
5. **Database Scaling**
    - Use read replicas and sharding for user/session data.
    - Choose DBs per service: PostgreSQL for transactions, MongoDB for chat.
6. **Auto-Scaling with Kubernetes**
    - Scale up/down containers based on CPU/RAM usage dynamically.
7. **Monitoring + Alerting**
    - Prometheus + Grafana + Alertmanager to monitor performance.

How many parallel chats were happening in Astrotalk?”

### ✅ Interview-Ready Answer:

**The number of parallel chats in Astrotalk depends on active astrologers and user traffic.**

Assuming:

- ~10,000 active users during peak hours
- Avg chat session = 20 mins
- ~5,000 astrologers online

👉 **Estimated parallel chats = 5,000 – 8,000** during peak load.

To support this:

- Use **WebSocket servers** (like Netty) behind a **load balancer**.
- Maintain chat state in **Redis** or **Cassandra**.
- Use **Kafka** for chat logging asynchronously.

---

You can add:

> “We would horizontally scale WebSocket/chat services across nodes and ensure sticky sessions or use token-based session persistence for seamless experience.”
> 

What would be the MySQL schema (entities) for the chat support system in Astrotalk?

To support 1-to-1 chats between users and astrologers, we can design these main tables:

**Users**

```java
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  name VARCHAR(100),
  role ENUM('USER', 'ASTROLOGER'),
  created_at DATETIME
);

```

. **ChatSessions**

```java
CREATE TABLE chat_sessions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  astrologer_id BIGINT,
  started_at DATETIME,
  ended_at DATETIME,
  status ENUM('ACTIVE', 'COMPLETED'),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (astrologer_id) REFERENCES users(id)
);

```

Messages

```java
CREATE TABLE messages (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  session_id BIGINT,
  sender_id BIGINT,
  message_text TEXT,
  message_type ENUM('TEXT', 'IMAGE', 'SYSTEM'),
  sent_at DATETIME,
  FOREIGN KEY (session_id) REFERENCES chat_sessions(id),
  FOREIGN KEY (sender_id) REFERENCES users(id)
);

```

### Optional Tables (for scale and analytics):

- `chat_ratings` – for user feedback after session
- `message_delivery_status` – for tracking delivery/read receipts
- `blocked_users` – prevent abuse

---

### Add-on (if time permits):

> “For scalability, we store metadata in MySQL and offload chat logs to a NoSQL store like MongoDB or archive them in cold storage (S3) via Kafka consumers.”
> 

To link two entities together in **MySQL**, we typically use **foreign keys**. Here's how you explain it in the context of Astrotalk’s chat system:

“We link entities like `users` and `chat_sessions` using foreign keys to maintain relational integrity.”

Example: Linking `users` and `chat_sessions`

```java
CREATE TABLE chat_sessions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  astrologer_id BIGINT,
  started_at DATETIME,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (astrologer_id) REFERENCES users(id)
);

```

- `user_id` and `astrologer_id` are **foreign keys** referencing the `users` table.
- This creates a **one-to-many relationship**: one user can have many chat sessions.

Example: Linking `chat_sessions` and `messages`

```java
CREATE TABLE messages (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  session_id BIGINT,
  sender_id BIGINT,
  message_text TEXT,
  FOREIGN KEY (session_id) REFERENCES chat_sessions(id),
  FOREIGN KEY (sender_id) REFERENCES users(id)
);

```

- One session can have **many messages**.
- Each message is tied to a **sender**, who is a `user`.

---

You can add:

> “Using foreign keys enforces referential integrity and makes JOINs easy for querying session history, user conversations, and message logs.”
> 

“What is the ticketing system pattern for your work?” (like in Astrotalk or Eureka Forbes)

### ✅ Interview-Ready Answer:

**We follow a Service Request (Ticketing) Pattern using Event-Driven Microservices**, where each user issue or consultation request is tracked as a ticket.

---

### 🔄 Key Pattern: **Request → Workflow → Resolution**

---

### 🔹 Step-by-Step Pattern:

1. **Ticket Creation**
    - A ticket is raised via API (`POST /tickets`) for user issues, chat requests, or service appointments.
    - It goes into a `ticket` table with status = `OPEN`.
2. **Event-Driven Flow**
    - After creation, we publish a Kafka event (`ticket.created`).
    - Downstream services like `AssignmentService`, `NotificationService` subscribe and act on it.
3. **Assignment**
    - Based on ticket type, the system assigns it to a support agent, astrologer, or technician using a matching algorithm.
    - Ticket is updated to `ASSIGNED`.
4. **Resolution**
    - The agent interacts with the user (via chat, call, etc.).
    - Ticket status is updated (`IN_PROGRESS`, `RESOLVED`, `CLOSED`).
5. **Audit + SLA**
    - All status changes are logged for SLA tracking.
    - Notification is sent at each stage.

---

### 🧱 Underlying Pattern:

> CQRS + Event Sourcing (lightweight) — for better read/write separation and tracking all ticket lifecycle events.
> 

---

### 🛠 Technologies:

- **DB**: MySQL for ticket metadata
- **Queue**: Kafka for async updates
- **Cache**: Redis for active ticket sessions
- **Notification**: Email/SMS via Notification microservice

---

### Final Line:

> "This pattern ensures decoupled, scalable, and trackable ticket management across services like chat, support, and appointments."
> 

“How are you deciding which admin to assign a ticket to?” (e.g., in chat support, tech support, etc.)

### ✅ Interview-Ready Answer:

**We use a rule-based + load-balanced assignment logic** to decide which admin (or astrologer/support agent) to assign a ticket to.

---

### 🔹 Assignment Logic (Step-by-Step):

1. **Filter Eligible Admins**
    - Filter by **skills**, **ticket type**, **language**, and **availability**.
    - Example: Technical ticket → only L2 admins; Hindi-speaking user → Hindi-speaking admins.
2. **Load Balancing**
    - Among eligible admins, choose the one with **least active tickets** or **lowest recent assignment count**.
    - Implemented using a weighted round-robin or queue-based priority.
3. **Caching for Performance**
    - Admin availability and current load are stored in **Redis** for fast lookup.
4. **Fallback**
    - If no admin is available, assign to a **default queue** or **escalation group**.

---

### 🛠 Implementation Notes:

- Redis Sorted Sets to store admin ID vs. active ticket count.
- Admin info cached in Redis, refreshed every few seconds by a scheduler.
- Assignment decision made by a **dedicated AssignmentService** or background worker (Kafka consumer).

### Example Final Line:

> “This ensures fair load distribution, quick response, and SLA compliance while keeping the system performant at scale.”
> 

**❓“How can we get which admin is available for assignment?”**

### ✅ Interview-Ready Answer:

**We track admin availability using Redis**, updated in near real-time, and query it during ticket or chat assignment.

---

### 🔹 Step-by-Step Process:

1. **Track Admin Status**
    - Each admin’s availability (`AVAILABLE`, `BUSY`, `OFFLINE`) is stored in **Redis**.
    - Status is updated:
        - When they log in/out
        - When a ticket is assigned or closed
        - Via heartbeat (ping every X seconds)
2. **Redis Structure Example**

```java
# Hash: admin:status:<admin_id>
admin:status:101 → AVAILABLE  
admin:status:102 → BUSY  

```

Get Available Admins

```java
Set<String> availableAdmins = redisTemplate.keys("admin:status:*")
    .stream()
    .filter(id -> redisTemplate.get(id).equals("AVAILABLE"))
    .collect(Collectors.toSet());

```

1. **Filter by Skills or Load**
    - Once we have the available admin list, we query metadata (skills, ticket count) from DB or another Redis structure to finalize assignment.

---

### 🛠 Tools:

- Redis (for availability)
- MySQL (for admin profile, history)
- Scheduled job or WebSocket for real-time status sync

---

### Final Line:

> “Using Redis lets us fetch available admins in milliseconds, enabling fast and scalable assignment decisions.”
> 

**“How are you deciding the approval pattern flow for L1/L2 admin?” (e.g., in a multi-level approval workflow)**

### Interview-Ready Answer:

**We decide the approval pattern based on the request type, user role, and business rules**, using a rule engine or pattern-matching logic in our workflow service.

---

### 🔹 Step-by-Step Flow:

1. **Identify the Request Type**
    - Each request (e.g., policy change, high-value order, escalation) has a category or risk level.
2. **Determine Required Approval Pattern**
    - For example:
        - Normal request → L1 approval
        - Sensitive or escalated request → L1 → L2 (multi-step)
    
    Stored as rules in DB or in code:
    

```java
if (request.amount > 50000) {
   pattern = "L1 → L2";
} else {
   pattern = "L1";
}

```

1. **Resolve Approvers Dynamically**
    - Fetch available L1 and L2 admins from DB or directory service.
    - Assign stepwise approval chain using workflow engine.
2. **Track Workflow Progress**
    - Status: `PENDING_L1`, `PENDING_L2`, `APPROVED`, `REJECTED`
    - Move to next level only after current level approves.

---

### 🔁 Example Flow:

- **Request A** → Goes to L1
- L1 Approves → Auto-assign to L2
- L2 Approves → Mark request as `APPROVED`

---

### Final Line:

> “This layered approval pattern allows flexible, rule-driven workflows and ensures sensitive actions are double-checked.”
> 

How do you debug and identify the slowness of an API?

### ✅ Interview-Ready Answer (Structured):

> "To identify and fix slow APIs, I follow a structured approach using profiling, logs, and tracing. Here's how I typically debug API slowness:"
> 

---

### 🔹 1. **Check Logs First**

- Enable **detailed logs** for the slow endpoint.
- Check **start and end timestamps** to measure total response time.
- Identify any **long-running DB queries or external calls** in logs.

> "In Spring Boot, I often use @Slf4j and time-stamped log statements around key blocks."
> 

---

### 🔹 2. **Use Application Performance Monitoring (APM) Tools**

- Tools like **New Relic**, **Datadog**, **Dynatrace**, or **Spring Boot Actuator + Micrometer** can help:
    - Trace request flow
    - Identify bottlenecks (e.g., DB, network, or CPU-bound code)
    - Show % time spent in each layer (Controller, Service, DB)

### 3. **Enable Distributed Tracing**

- In microservices, use **OpenTelemetry** or **Sleuth + Zipkin/Jaeger** for tracing across services.
- This helps you spot if slowness is in:
    - Your service
    - A downstream service
    - Network latency

> “Spring Cloud Sleuth with Zipkin helps trace requests with unique IDs and visualize latency hops.”
> 

---

### 🔹 4. **Profile DB Calls**

- Enable **SQL query logging** (`spring.jpa.show-sql=true`, or use AOP loggers).
- Use **EXPLAIN PLAN** to find slow queries or missing indexes.

> “I use tools like Hibernate Statistics, or pg_stat_statements for PostgreSQL to spot slow queries.”
> 

---

### 🔹 5. **Check Resource Usage**

- Monitor **CPU, memory, thread pools, GC logs**.
- Use tools like:
    - **VisualVM** / **JConsole** / **jstack**
    - **Spring Boot Actuator `/metrics`**

### 6. **Concurrency Issues or Deadlocks**

- Use `jstack` to detect blocked threads.
- Check thread pools (`Tomcat`, `@Async`, Kafka consumers, etc.).

---

### ✅ Final Interview Summary:

> “I start with logs and tracing, then use APM tools to pinpoint where the delay is. Based on whether it’s CPU, DB, or I/O-bound, I optimize queries, add caching, or tune thread pools and service timeouts.”
> 

Let's suppose the DB query is taking time — how do you debug that?”

### Interview-Ready Answer:

> “If the database query is causing the slowness, I follow a DB-first debugging approach to optimize the query, indexing, and data access patterns.”
> 

---

### 🔹 Step-by-Step Debug Strategy:

### 1. **Enable SQL Query Logging**

- In Spring Boot:

```java
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.SQL=DEBUG

```

> “This lets me see exactly which query is slow and how long it takes.”
> 

---

### 2. **Use EXPLAIN PLAN**

- Run the slow SQL manually in your DB (e.g., MySQL, PostgreSQL):

```java
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123 AND status = 'PENDING';

```

> “This shows whether the query is using full table scan or index.”
> 

---

### 3. **Check for Missing Indexes**

- Add indexes on high-selectivity columns used in `WHERE`, `JOIN`, or `ORDER BY`.

```
CREATE INDEX idx_user_status ON orders(user_id, status);

```

> “I check if indexes exist on frequently filtered or joined fields.”
> 

---

### 4. **Check Data Volume**

- Is the table **huge**? Add **pagination** or limit query scope:

```java
SELECT * FROM orders WHERE status = 'PENDING' LIMIT 100 OFFSET 0;

```

> “I always avoid loading 1000s of rows into memory unless needed.”
> 

---

### 5. **Avoid N+1 Problems (Hibernate)**

- Use `@EntityGraph`, `JOIN FETCH`, or `@BatchSize`:

```java
@Query("SELECT u FROM User u JOIN FETCH u.roles WHERE u.id = :id")

```

> “If we’re making one query per record (N+1), I rewrite it with fetch joins or batch fetching.”
> 

---

### 6. **Use Caching for Read-heavy Queries**

- Use Redis or Spring Cache:

```java
@Cacheable("userOrders")
public List<Order> getUserOrders(Long userId) { ... }

```

### . **DB Health Monitoring**

- Check:
    - Long-running connections
    - Slow query log
    - Connection pool size (HikariCP tuning)

> “Sometimes slowness is due to exhausted DB pool, not the query itself.”
> 

---

## ✅ Final Line (Summary for Interview):

> “I analyze the SQL with EXPLAIN, check for missing indexes or N+1 issues, and tune the queries or add caching. This helps reduce response time at the database level, which is often the bottleneck in slow APIs.”
> 

Great follow-up — if you **already added indexes** but the query is **still slow**, then there are deeper issues to investigate.

---

### ✅ Interview-Ready Answer:

> "Even with indexing in place, a query may still be slow due to suboptimal index usage, high data volume, wrong query patterns, or database-level bottlenecks. Here's how I approach this next."
> 

---

## 🔍 Deeper Troubleshooting When Index Is Present But Query Is Still Slow:

---

### 🔹 1. **Check If the Index Is Actually Being Used**

- Use `EXPLAIN` / `EXPLAIN ANALYZE` (PostgreSQL/MySQL) to verify **if your index is being hit**.
    - Sometimes the query planner **ignores the index** if it estimates a full scan is cheaper.
    - **Large result sets** can lead the planner to avoid using the index.

> “I’ve seen cases where a WHERE clause includes functions like LOWER(col) or DATE(col) — those make the index unusable. I rewrite the query to avoid such transformations on indexed columns.”
> 

### 2. **Use Covering Indexes**

- Make sure the index **covers all columns** used in the `WHERE`, `JOIN`, `ORDER BY`, and `SELECT`.
- Otherwise, the DB has to do an **extra table lookup** for the rest of the data.

Example:

```java
-- Instead of indexing only on user_id
CREATE INDEX idx_user_status ON orders (user_id, status, created_at);

```

### 3. **Avoid Complex Functions in WHERE Clause**

- Expressions like `WHERE DATE(created_at) = '2024-07-01'` **disable index use**.
- Instead, use:

```java
WHERE created_at >= '2024-07-01 00:00:00'
  AND created_at < '2024-07-02 00:00:00'

```

### 4. **Check Statistics / Table Bloat**

- In PostgreSQL, run `ANALYZE` and `VACUUM` to update statistics and clean up dead rows.
- In MySQL, run `ANALYZE TABLE` or `OPTIMIZE TABLE`.

> “Stale stats can mislead the query planner into choosing bad plans — I make sure autovacuum is working or manually trigger analyze.”
> 

---

### 🔹 5. **Reduce Result Set Early**

- Use `LIMIT`, proper filtering, or move filters **as early as possible** in joins.
- Avoid SELECT * — fetch only what’s needed.

---

### 🔹 6. **Look at Locks, Blocking, or Contention**

- A slow query might be **waiting for a lock** rather than being slow itself.
- Use:
    - PostgreSQL: `pg_stat_activity`, `pg_locks`
    - MySQL: `SHOW ENGINE INNODB STATUS`

---

### 🔹 7. **Partitioning or Sharding (for large tables)**

- If the table has **millions of rows**, consider **partitioning** by date, region, or tenant.
- Helps the query planner **avoid scanning the entire table**.

### ✅ Final Line (for Interview):

> “When indexing doesn’t help, I dig deeper using EXPLAIN plans, check if the index is actually used, optimize WHERE clauses, and review table statistics. I also monitor locks and slow query logs to identify deeper DB issues.”
> 

If you're asking **“How to get the last page of results quickly in a paginated API or database query”**, here's a structured **interview-ready answer** and the **technical approach** depending on the situation.

---

## ✅ Interview-Style Answer:

> “To fetch the last page quickly, I avoid using OFFSET-based pagination for large datasets and prefer keyset pagination or reverse sorting with LIMIT. OFFSET becomes slower as it skips more rows.”
> 

## Problem with OFFSET Pagination:

```sql
SELECT * FROM orders ORDER BY created_at LIMIT 10 OFFSET 9990;

```

- To get page 1000 (assuming 10 items per page), the DB has to **scan and skip 9990 rows**.
- ❌ **Very slow** for large tables.

---

## ✅ Better Ways to Get the Last Page Quickly:

---

### 🔹 1. **Reverse Sort + LIMIT**

If you're ordering by time or ID:

```sql
-- Get last 10 orders
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 10;

```

> “Sort in reverse and limit the result — fastest for getting the latest or last N items.”
> 

Then on the frontend, reverse the list if needed.

---

### 🔹 2. **Keyset Pagination (Seek Method)**

Instead of using OFFSET, use a reference value like `created_at` or `id`:

```sql
-- Get next 10 items after last seen ID
SELECT * FROM orders
WHERE id < :lastSeenId
ORDER BY id DESC
LIMIT 10;

```

> “Keyset pagination is fast even on very large tables because it uses an indexed filter instead of skipping rows.”
> 

---

### 🔹 3. **Store Total Count and Calculate Page Start**

If you absolutely need page 1000 out of 1000:

```java
-- Precompute total rows
SELECT COUNT(*) FROM orders; -- say 10000 rows

-- Then get the last page manually
SELECT * FROM orders
ORDER BY id ASC
LIMIT 10 OFFSET 9990;

```

> “For admin tools or analytics, I store total count and use OFFSET sparingly — with indexes.”
> 

---

### ✅ Final Interview Line:

> “OFFSET is slow at scale, so I prefer reverse sort with LIMIT or keyset pagination using indexed values. These allow fast access to the last page, even in large datasets.”
> 

Sure! Let’s structure the **business needs** for a **dropshipping application** built with **Spring Boot**, in a way that's clear for both interviews and real-world implementation planning.

---

## ✅ Business Needs for a Dropshipping Application (Spring Boot Backend)

### 🔹 1. **Product Management**

- Add, update, or remove products from catalog.
- Sync product data (name, price, inventory, images) from **third-party suppliers** via APIs.
- Category and brand hierarchy support.

**Entities**: `Product`, `Category`, `Supplier`, `Inventory`

---

### 🔹 2. **Order Management**

- Customers place orders via frontend (React/Angular).
- Orders are automatically forwarded to suppliers.
- Track order lifecycle: `PLACED → CONFIRMED → SHIPPED → DELIVERED`.

**Entities**: `Order`, `OrderItem`, `Customer`, `Shipment`, `Payment`

---

### 🔹 3. **Inventory Sync (Real-Time / Scheduled)**

- Periodic jobs or webhook-based sync to:
    - Update stock levels
    - Reflect price changes

Use: **Spring Scheduler / Quartz Jobs**

---

### 🔹 4. **Payment Integration**

- Integration with payment gateways (Razorpay, Stripe, PayPal).
- Handle success/failure callbacks.
- Record transactions and payment status.

---

### 🔹 5. **Shipping & Tracking**

- Fetch shipping quotes from courier APIs.
- Auto-generate shipping labels.
- Track delivery status via 3rd-party APIs.

**Entities**: `ShippingPartner`, `ShipmentTracking`, `ShippingLabel`

---

### 🔹 6. **Supplier API Integration**

- Use REST clients (e.g. `WebClient`, `RestTemplate`) to:
    - Fetch products
    - Place orders
    - Check fulfillment status

---

### 🔹 7. **Authentication & Authorization**

- Use JWT or OAuth2 for secure API access.
- Admins, customers, and suppliers have separate roles.

**Tech**: Spring Security + JWT

---

### 🔹 8. **Admin Dashboard Features**

- View/manage orders, products, customers.
- View inventory and stock alerts.
- Basic analytics: revenue, orders, top products.

---

### 🔹 9. **Notifications**

- Email/SMS notifications for:
    - Order placed
    - Order shipped/delivered
    - Stock out alerts

Use: Spring Events + Email Service / SMS Gateway.

---

### 🔹 10. **Audit & Logs**

- Log product updates, order status changes.
- Track which admin/user made changes.

---

## ✅ Technical Highlights (Spring Boot Stack)

| Component | Tech Stack / Tools |
| --- | --- |
| Backend Framework | Spring Boot |
| API Security | Spring Security + JWT |
| Scheduling | Spring Scheduler / Quartz |
| DB | MySQL / PostgreSQL |
| Caching | Redis |
| API Clients | WebClient (Spring Reactive) |
| Frontend (optional) | React / Angular |
| Build & Deploy | Docker + Jenkins + CI/CD pipeline |
| Monitoring | Spring Boot Actuator + Prometheus |

---

## 🧠 Optional Features:

- Customer Reviews
- Coupon/discount system
- Wishlist
- Return/Refund management
- Multi-currency, multi-region support

---

### ✅ Final Interview Summary:

> “This dropshipping platform handles catalog sync from suppliers, real-time inventory updates, order forwarding, and shipping tracking via 3rd-party APIs. We use Spring Boot with RESTful architecture, JWT-based auth, and scheduled jobs for background syncing.”
> 

Great! Pagination is a **must-have** feature for performance and scalability in REST APIs. Here’s how to **build a pagination API using Spring Boot and Java**, with **interview-ready explanation + working code**.

---

## ✅ Interview One-Liner:

> “I use Spring Data JPA’s built-in Pageable interface to handle pagination via query parameters like page and size, and return a Page<T> response that includes content and metadata.”
> 

---

## 🧱 Step-by-Step: Build Pagination API in Spring Boot

### 🧾 Suppose You Have an Entity: `Product`

```java
@Entity
public class Product {
    @Id
    private Long id;

    private String name;
    private double price;
    private String category;
}

```

---

### 🔹 1. Create Repository with Paging

```java
public interface ProductRepository extends JpaRepository<Product, Long> {
    Page<Product> findAll(Pageable pageable);
}

```

---

### 🔹 2. Create Controller with Pagination Endpoint

```java
@RestController
@RequestMapping("/api/products")
public class ProductController {

    @Autowired
    private ProductRepository productRepository;

    @GetMapping
    public Page<Product> getProducts(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(defaultValue = "id") String sortBy
    ) {
        Pageable pageable = PageRequest.of(page, size, Sort.by(sortBy));
        return productRepository.findAll(pageable);
    }
}

```

---

### 🔍 Sample API Call:

```
GET /api/products?page=1&size=5&sortBy=price

```

Response:

```json
{
  "content": [ ... 5 products ... ],
  "totalElements": 100,
  "totalPages": 20,
  "number": 1,
  "size": 5
}

```

---

## ✅ Optional: Wrap in Custom Response DTO

To make the response more frontend-friendly:

```java
public class PagedResponse<T> {
    private List<T> content;
    private int pageNumber;
    private int pageSize;
    private long

```

### 

The **Factory Design Pattern** is a creational pattern that provides an interface for creating objects **without specifying their exact class**. It's commonly used in Java and Spring Boot to decouple object creation from implementation.

---

## ✅ Interview One-Liner:

> “The Factory Pattern lets us create objects without exposing the instantiation logic to the client. It provides a common interface and delegates creation to subclasses or factory methods.”
> 

---

## 🎯 When to Use It:

- When the exact type of object to create is **decided at runtime**.
- When object creation logic is **complex or reusable**.
- When you want to **decouple the client** from concrete classes.

---

## ✅ Real-World Analogy:

> Think of a coffee shop. The customer asks for a coffee (Latte, Espresso) and the barista (factory) prepares the correct type — the customer doesn't care how it's made, just gets the right drink.
> 

---

## 🛠️ Example in Java

### 🔹 1. Common Interface:

```java
public interface Notification {
    void notifyUser();
}

```

### 🔹 2. Concrete Classes:

```java
public class EmailNotification implements Notification {
    public void notifyUser() {
        System.out.println("Sending Email Notification");
    }
}

public class SMSNotification implements Notification {
    public void notifyUser() {
        System.out.println("Sending SMS Notification");
    }
}

```

### 🔹 3. Factory Class:

```java
public class NotificationFactory {
    public static Notification createNotification(String type) {
        if ("EMAIL".equalsIgnoreCase(type)) {
            return new EmailNotification();
        } else if ("SMS".equalsIgnoreCase(type)) {
            return new SMSNotification();
        }
        return null;
    }
}

```

### 🔹 4. Client Code:

```java
public class Main {
    public static void main(String[] args) {
        Notification notification = NotificationFactory.createNotification("EMAIL");
        notification.notifyUser();
    }
}

```

---

## ✅ Output:

```
Sending Email Notification

```

---

## ✅ In Spring Boot:

You often use **Spring Beans + Factory pattern** implicitly via `@Component`, `@Service`, and `@Autowired`. But you can still apply it explicitly when:

- Deciding which strategy to use at runtime.
- Building a dynamic service registry.

---

## ✅ Final Interview Summary:

> “Factory Pattern encapsulates object creation logic in one place. It helps in keeping the client code clean, maintainable, and decoupled from specific class implementations.”
> 

Sure! Here's a **simple, real-world example of Factory Design Pattern** in Java using **dummy classes** to make it easy to understand — perfect for interview explanation.

---

## ✅ Scenario: Notification System

You want to send notifications via **Email**, **SMS**, or **Push** — and use a **Factory** to create the appropriate type.

---

### 🔹 Step 1: Create the Interface

```java
public interface Notification {
    void notifyUser();
}

```

---

### 🔹 Step 2: Create Dummy Implementations

```java
public class EmailNotification implements Notification {
    public void notifyUser() {
        System.out.println("📧 Email Notification Sent!");
    }
}

public class SMSNotification implements Notification {
    public void notifyUser() {
        System.out.println("📱 SMS Notification Sent!");
    }
}

public class PushNotification implements Notification {
    public void notifyUser() {
        System.out.println("🔔 Push Notification Sent!");
    }
}

```

---

### 🔹 Step 3: Create the Factory Class

```java
public class NotificationFactory {
    public static Notification createNotification(String type) {
        if ("EMAIL".equalsIgnoreCase(type)) {
            return new EmailNotification();
        } else if ("SMS".equalsIgnoreCase(type)) {
            return new SMSNotification();
        } else if ("PUSH".equalsIgnoreCase(type)) {
            return new PushNotification();
        } else {
            throw new IllegalArgumentException("Unknown notification type: " + type);
        }
    }
}

```

---

### 🔹 Step 4: Use the Factory in a Dummy Main Class

```java
public class FactoryPatternDemo {
    public static void main(String[] args) {
        Notification notification1 = NotificationFactory.createNotification("EMAIL");
        notification1.notifyUser();

        Notification notification2 = NotificationFactory.createNotification("SMS");
        notification2.notifyUser();

        Notification notification3 = NotificationFactory.createNotification("PUSH");
        notification3.notifyUser();
    }
}

```

---

### ✅ Output:

```
📧 Email Notification Sent!
📱 SMS Notification Sent!
🔔 Push Notification Sent!

```

---

## ✅ Final Interview Summary:

> "In this example, the Factory class centralizes object creation logic. The client doesn’t know or care which specific class is being instantiated — it just asks the factory for a Notification, and the correct type is returned."
> 

Let me know if you want a Spring Boot version with `@Component`-based dynamic injection!

Great! Let’s break down the difference between **PUT** and **PATCH** — both are HTTP methods used in **REST APIs** for updating resources, but they behave differently.

---

## ✅ One-Line Interview Answer:

> “PUT replaces the entire resource, while PATCH updates only specific fields — PUT is idempotent, PATCH is partial and flexible.”
> 

---

## 🔍 Key Differences Between PUT and PATCH

| Feature | **PUT** | **PATCH** |
| --- | --- | --- |
| ✅ Purpose | Full update (replace the whole resource) | Partial update (only some fields) |
| ✅ Required fields | All fields usually required | Only fields to update |
| ✅ Overwrites | Entire object | Only specific properties |
| ✅ Idempotent | ✅ Yes (same result if repeated) | ⚠️ Not always guaranteed |
| ✅ Request size | Large (full object) | Small (only fields to update) |
| ✅ Use case | Replacing a user profile completely | Updating only user email or status |

---

## 🧱 Example in REST API

Let’s say we have a `User` resource:

```json
{
  "id": 1,
  "name": "John",
  "email": "john@example.com",
  "status": "ACTIVE"
}

```

---

### 🔹 PUT Request (Full Replace):

```
PUT /api/users/1
Content-Type: application/json

{
  "id": 1,
  "name": "John",
  "email": "john.new@example.com",
  "status": "INACTIVE"
}

```

✅ This **replaces the entire object**. If `status` is missing → might become `null`.

---

### 🔹 PATCH Request (Partial Update):

```
PATCH /api/users/1
Content-Type: application/json

{
  "email": "john.new@example.com"
}

```

✅ Only updates the **email**, all other fields remain unchanged.

---

## ✅ Java/Spring Boot Notes

- Use `@PutMapping` for PUT, `@PatchMapping` for PATCH.
- PATCH usually requires custom merge logic in service layer.

---

### ✅ Final Interview Summary:

> “PUT is used when replacing the entire resource with new data, while PATCH is ideal for updating specific fields. PUT is idempotent and more strict; PATCH is flexible but requires careful field handling.”
> 

### **Core Java Questions**

**Q1: What is the difference between `==` and `.equals()`?**

`==` checks reference equality; `.equals()` checks object content.

**Q2: What is a constructor in Java?**

A special method used to initialize objects. It has the same name as the class and no return type.

**Q3: What is the difference between `ArrayList` and `LinkedList`?**

- `ArrayList`: Fast random access, slow insert/delete.
- `LinkedList`: Slow access, fast insert/delete.

**Q4: What is the purpose of `final` keyword?**

- Final variable: Constant.
- Final method: Can't be overridden.
- Final class: Can't be inherited.

**Q5: What is the difference between `HashMap` and `ConcurrentHashMap`?**

- `HashMap`: Not thread-safe.
- `ConcurrentHashMap`: Thread-safe with better concurrency.

---

### 🔹 **OOPs Concepts**

**Q6: What are the four pillars of OOP?**

Encapsulation, Inheritance, Polymorphism, Abstraction.

**Q7: What is encapsulation?**

Wrapping data and code into a single unit (class), often with private fields and public getters/setters.

**Q8: What is polymorphism?**

One interface, many implementations. Achieved via method overloading and overriding.

---

### 🔹 **Java Multithreading & Concurrency**

**Q9: Difference between `synchronized` and `ReentrantLock`?**

Both ensure thread safety. `ReentrantLock` gives more control (tryLock, fair lock), but needs manual unlock.

**Q10: What is a thread-safe class?**

A class that works correctly when accessed by multiple threads concurrently (e.g., `Vector`, `ConcurrentHashMap`).

---

### 🔹 **Spring & REST**

**Q11: What is Spring Boot?**

A framework for building standalone Spring apps with embedded server and minimal config.

**Q12: How do you create a REST API in Spring Boot?**

Use `@RestController`, `@GetMapping`, `@PostMapping`, etc., with a service layer for logic.

**Q13: What is Dependency Injection?**

Design pattern where objects are injected via constructor/setter to reduce tight coupling.

---

### 🔹 **Database & JPA**

**Q14: What is the difference between `JPA` and `Hibernate`?**

- JPA: Specification.
- Hibernate: Implementation of JPA.

**Q15: How do you handle transactions in Spring?**

Use `@Transactional` annotation.

### Java 8 Features (Most Important)

1. **Lambda Expressions**
    
    Enables functional-style coding:
    
    `list.forEach(item -> System.out.println(item));`
    
2. **Streams API**
    
    Used for processing collections in a declarative way:
    
    `list.stream().filter(x -> x > 5).collect(Collectors.toList());`
    
3. **Functional Interfaces**
    
    Interfaces with a single abstract method. Used with lambdas (e.g. `Runnable`, `Predicate`).
    
4. **Default and Static Methods in Interfaces**
    
    Allows adding new methods to interfaces without breaking existing code.
    
5. **Optional Class**
    
    Helps avoid `NullPointerException`.
    
    Example: `Optional.ofNullable(obj).orElse("default");`
    
6. **Method References**
    
    A shortcut to call methods using `ClassName::methodName`.
    
7. **Date and Time API (`java.time`)**
    
    Immutable and thread-safe date/time handling.
    
    Example: `LocalDate`, `LocalDateTime`.
    

---

### 🔹 Java 9

1. **Module System (Project Jigsaw)**
    
    Introduced modularity with `module-info.java`.
    
    Useful for large enterprise apps.
    
2. **JShell (REPL)**
    
    Interactive Java shell for testing snippets quickly.
    
3. **Stream API Improvements**
    
    Methods like `takeWhile()`, `dropWhile()` added.
    

---

### 🔹 Java 10

1. **Local Variable Type Inference (`var`)**
    
    Example:
    
    `var list = new ArrayList<String>();`
    
2. **Performance and GC Enhancements**
    
    Improved memory and garbage collection handling.
    

---

### 🔹 Java 11

1. **New String Methods**
    - `isBlank()`, `lines()`, `strip()`, `repeat()`.
2. **`HttpClient` API (standardized)**
    
    Replaces legacy `HttpURLConnection` with a modern HTTP client.
    
3. **Run Java File with `java filename.java`**
    
    No need to compile separately for small scripts.
    

### Java 8 to 11 Migration – Key Points

**Q: How do you handle Java 8 to Java 11 migration in a project?**

**Answer:**

I ensured compatibility by updating the `JDK`, resolving removed APIs, and leveraging new features gradually. Focused on:

- Replacing deprecated APIs (e.g., `javax.xml.bind` removed in Java 11).
- Updating `build tools` (e.g., Maven/Gradle to support Java 11).
- Testing all modules with Java 11 for runtime and compilation issues.
- Modularizing code if needed using `module-info.java`.

### Functional Interfaces in Java 8

**Q: What is a functional interface?**

**Answer:**

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

### Why We Use Functional Interfaces

**Q: Why do we use functional interfaces in Java 8?**

**Answer:**

Functional interfaces enable **lambda expressions** and **clean functional programming**. They help write **shorter, more readable, and reusable** code — especially for tasks like filtering, mapping, and iterating over collections.

**Use Case in My Project:**

I used `Predicate` in stream filters to validate consultant attributes, and `Consumer` for processing approval steps in a pipeline.

### Predicate, Consumer, BiConsumer – Explained

**1. `Predicate<T>`**

Takes one input, returns a boolean.

**Use:** Filtering.

👉 `x -> x > 10`

**2. `Consumer<T>`**

Takes one input, returns nothing.

**Use:** Performing an action.

👉 `x -> System.out.println(x)`

**3. `BiConsumer<T, U>`**

Takes two inputs, returns nothing.

**Use:** Processing key-value pairs, like in a map.

👉 `(k, v) -> System.out.println(k + ":" + v)`

---

**Use in Project Example:**

- Used `Predicate` to validate request fields.
- Used `Consumer` for logging actions.
- Used `BiConsumer` to iterate over map of consultants and actions.

### Why Use `Optional` in Java 8?

**Q: What is `Optional` and why do we use it?**

**Answer:**

`Optional` is a container that may or may not hold a non-null value.

It helps **avoid `NullPointerException`** by forcing explicit checks.

**Example:**

```java
Optional<String> name = Optional.ofNullable(input);
name.ifPresent(System.out::println);

```

**Use in Project:**

I used `Optional` to safely handle API response fields before processing approval logic.

### Using `Optional` to Avoid NullPointerException

**Q: How does `Optional` help avoid NPE?**

**Answer:**

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

### How Streams Improve Performance

**Q: How do Java 8 Streams improve performance?**

**Answer:**

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

### ChatGPT said:

Sure! Here's a clean **approach + code** to count the occurrence of each word in the given `String[]` where words are separated by underscores.

---

### 🔹 **Approach:**

1. **Iterate** over each string in the array.
2. **Split** each string using `"_"` as a delimiter.
3. For each word, **store its count** in a `Map<String, Integer>`.
4. Finally, **print the map**.

```java
import java.util.*;

public class WordCount {
    public static void main(String[] args) {
        String[] str = {"one_two", "one_two_three", "two", "two_three"};
        Map<String, Integer> countMap = new HashMap<>();

        for (String s : str) {
            String[] words = s.split("_");
            for (String word : words) {
                countMap.put(word, countMap.getOrDefault(word, 0) + 1);
            }
        }

        // Print the result
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}

```

output : 

one: 2

two: 4

three: 2

Here’s the **Java 8 Stream-based approach** to solve the same problem: counting word occurrences from an array of underscore-separated strings.

---

### 🔹 **Approach (Java 8):**

1. Convert the array to a Stream.
2. Use `flatMap()` to split and flatten all strings by `_`.
3. Use `Collectors.groupingBy()` to count each word.

---

### 🔹 **Java 8 Code:**

```java
import java.util.*;
import java.util.stream.*;

public class WordCountStream {
    public static void main(String[] args) {
        String[] str = {"one_two", "one_two_three", "two", "two_three"};

        Map<String, Long> wordCount = Arrays.stream(str)
            .flatMap(s -> Arrays.stream(s.split("_")))
            .collect(Collectors.groupingBy(
                word -> word,
                Collectors.counting()
            ));

        // Print result
        wordCount.forEach((k, v) -> System.out.println(k + ": " + v));
    }
}

```

---

### 🔹 **Output:**

```
one: 2
two: 4
three: 2

```

### OOPs Concepts Used in My Project

**Q: How did you use OOPs concepts in your project?**

**Answer:**

1. **Encapsulation** – Used private fields and public getters/setters in approval request and user data models to protect internal state.
2. **Inheritance** – Common logic for approval flows (like logging, audit, validations) was inherited by specific pattern classes (Pattern 2, 3, 4).
3. **Polymorphism** – Overrode approval methods based on pattern type (e.g., `advanceApproval()` for Pattern 2, 3, and 4 differed).
4. **Abstraction** – Defined interfaces for notification and approval logic, so different implementations (email, UI triggers) could plug in easily.

### Real-Time OOPs Usage in My Project

**1. Encapsulation**

We had a `ConsultantRequest` class with private fields like `requestId`, `status`, `attributesChanged`, etc.

These were accessed via getters/setters to ensure data consistency during API and DB operations.

**2. Inheritance**

We created a base class `BaseApprovalHandler` containing common methods like `validateRequest()`, `sendNotification()`.

Pattern-specific handlers like `Pattern2Handler`, `Pattern4Handler` extended this class to reuse logic and override only what’s needed.

**3. Polymorphism**

We had a method `advanceApproval()` defined in the base handler.

Each pattern handler (2, 3, 4) had its own version of this method — allowing dynamic behavior based on the pattern.

**4. Abstraction**

An interface `ApprovalProcessor` defined the contract for processing any approval.

Each pattern had its own implementation like `Pattern2Processor`, `Pattern4Processor`.

This made the code loosely coupled and easy to extend.

Absolutely! Here's a **short and clear utility-wise explanation** of the OOP methods you used in your **real-time approval workflow project**, focusing on *how* each method helped in practice:

---

### 🔹 Utility of OOP Methods in Your Project

**1. `validateRequest()` – from `BaseApprovalHandler`**

✔ Ensured input data met business rules before any approval action.

✔ Reused across Pattern 2, 3, and 4 to avoid duplication.

**2. `sendNotification()` – from `BaseApprovalHandler`**

✔ Sent consistent email alerts or system notifications at each approval step.

✔ Abstracted out so pattern-specific logic didn't need to handle messaging.

**3. `advanceApproval()` – Overridden in Pattern2/3/4Handler**

✔ Core method to decide the next approver based on pattern logic.

✔ Polymorphic — each pattern defined its own path (e.g., Pattern 4: Sales Admin → SSO → Senior SSO → CDOT).

**4. `process()` – from `ApprovalProcessor` interface**

✔ Defined a contract for processing any approval request.

✔ Allowed plug-and-play style for different approval flows.

### Can We Override Non-Abstract Methods?

**Q: Can we override non-abstract methods in Java?**

**Answer:**

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

### Can We Change Return Type While Overriding?

**Q: If we override a method, can we change its return type?**

**Answer:**

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

### Covariant Return Type Example

**Definition:**

Covariant return type means the **overridden method** in the subclass can return a **subclass** of the return type declared in the superclass method.

---

**✅ Example:**

```java
class Animal {
    String getType() {
        return "Animal";
    }
}

class Dog extends Animal {
    @Override
    String getType() {
        return "Dog";
    }
}

```

This is **not covariant yet**, because return type is the same.

---

**🔸 Real Covariant Return Type Example:**

```java
class Animal {}

class Dog extends Animal {}

class Parent {
    Animal getAnimal() {
        return new Animal();
    }
}

class Child extends Parent {
    @Override
    Dog getAnimal() {
        return new Dog(); // ✅ Covariant return type
    }
}

```

✔ `Dog` is a subtype of `Animal`, so the override is valid.

```java
// Base class
class Animal {
    public void sound() {
        System.out.println("Animal sound");
    }
}

// Subclass
class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

// Superclass with method returning base type
class AnimalFactory {
    Animal getAnimal() {
        return new Animal();
    }
}

// Subclass with overridden method returning a subtype (covariant)
class DogFactory extends AnimalFactory {
    @Override
    Dog getAnimal() {
        return new Dog(); // ✅ Covariant return type
    }
}

// Test class
public class Main {
    public static void main(String[] args) {
        AnimalFactory factory = new DogFactory();
        Animal animal = factory.getAnimal();
        animal.sound();  // Output: Dog barks
    }
}

```

### Why This Works:

- `Dog` is a **subclass** of `Animal`.
- `DogFactory.getAnimal()` overrides `AnimalFactory.getAnimal()` but returns a **more specific type**.

This is a perfect example of **covariant return type** in object-oriented design, promoting flexibility and better type safety.

Let me know if you want a real-world analogy or how this applies to services or handlers in your project!

### When to Use Abstract Class vs Interface

| **Aspect** | **Abstract Class** | **Interface** |
| --- | --- | --- |
| **Use When** | You want to provide **base behavior** (partial implementation) | You want to define a **contract** only |
| **Methods** | Can have both abstract & non-abstract methods | All methods are abstract (till Java 7), or default/static (Java 8+) |
| **State** | Can have instance variables (fields) | Can't have instance fields (only constants) |
| **Inheritance** | Supports single inheritance | Supports multiple inheritance via interfaces |
| **Constructor** | Can have constructors | Cannot have constructors |

### **When to Use Abstract Class**

- You need **shared code** across related classes.
    
    👉 e.g., `BaseApprovalHandler` with common logic for Pattern 2, 3, 4.
    

### ✅ **When to Use Interface**

- You need to define **common behavior** across **unrelated classes**.
    
    👉 e.g., `ApprovalProcessor`, implemented by different pattern processors.
    

### Use of Constructor in Abstract Class

**Q: Why does an abstract class have a constructor if it can’t be instantiated?**

**Answer:**

An abstract class **can't be instantiated**, but its **constructor runs** when a **subclass object is created**.

It's used to **initialize common fields** or **set up resources** needed by all subclasses.

---

### ✅ Example:

```java
abstract class BaseHandler {
    String handlerType;

    // Constructor in abstract class
    BaseHandler(String type) {
        this.handlerType = type;
        System.out.println("BaseHandler constructor called");
    }
}

class Pattern2Handler extends BaseHandler {
    Pattern2Handler() {
        super("Pattern 2"); // Calls abstract class constructor
        System.out.println("Pattern2Handler constructor called");
    }
}

```

**Output:**

```
BaseHandler constructor called
Pattern2Handler constructor called

```

---

### 🔸 Real Project Use:

In your approval project, if `BaseApprovalHandler` had a constructor to initialize logger, workflow ID, or audit metadata — that would ensure **consistent setup** across all pattern handlers.

Let me know if you want this example framed with your real classes.

You're asking about **volatile** and **synchronized** in Java. Here's a **short and clear comparison**, perfect for interviews:

---

### 🔹 `volatile` vs `synchronized`

| Feature | `volatile` | `synchronized` |
| --- | --- | --- |
| **Purpose** | Ensures visibility of changes to variables across threads | Ensures mutual exclusion (only one thread can access the block) |
| **Thread Safety** | Not fully thread-safe (no atomicity) | Provides full thread safety |
| **Use Case** | For flags or simple read/write variables shared across threads | For critical sections like counters, shared objects |
| **Performance** | Faster, low overhead | Slower due to locking |

---

### ✅ `volatile` Example:

```java
volatile boolean isRunning = true;

```

Use when a **single thread updates** a flag and **others read it**.

---

### ✅ `synchronized` Example:

```java
synchronized void increment() {
    count++;
}

```

Use when multiple threads **modify shared data** and you need **atomicity**.

---

**In your project:**

- You can use `volatile` to control scheduler flags.
- Use `synchronized` when updating approval logs or shared maps.

Let me know if you'd like examples from your approval system or background job code.

### Why `volatile` Is Not Fully Thread-Safe

**Answer:**

`volatile` **only guarantees visibility**, not **atomicity**.

It ensures that:

- When one thread changes a `volatile` variable, other threads **see the updated value immediately**.

But it **does NOT protect compound operations**, like:

- `count++` (read → modify → write)
- `if (flag) { doSomething(); }`

These involve **multiple steps**, which can be **interrupted** by other threads, leading to race conditions.

---

### ❌ Example (Not thread-safe even with `volatile`):

```java
volatile int count = 0;

public void increment() {
    count++; // NOT atomic – can still cause race condition
}

```

To make it thread-safe, you need:

- `synchronized` block
- Or use `AtomicInteger`

---

### ✅ Use `volatile` when:

- One thread writes, others only read (e.g., `volatile boolean isRunning`)

reat! Let's focus on **visibility in `volatile`** — it's the **main purpose** of using `volatile` in Java.

---

### 🔹 What Does "Visibility" in `volatile` Mean?

**Visibility** means:

When one thread **modifies** a variable, **other threads immediately see the updated value** — without needing synchronization.

---

### ✅ Example Without `volatile` (Wrong behavior):

```java
boolean running = true;

public void run() {
    while (running) {
        // do something
    }
}

public void stop() {
    running = false;
}

```

If `run()` is in **Thread A**, and `stop()` is in **Thread B**,

Thread A **may never see** the updated value (`false`) — it might keep looping forever.

---

### ✅ Fixed with `volatile`:

```java
volatile boolean running = true;

```

Now, **when Thread B sets `running = false`**,

**Thread A sees the change immediately** — the **updated value is visible across threads**.

---

### 🔸 Why This Happens?

Because Java threads may **cache variables locally** (in CPU cache or registers).

`volatile` tells the JVM:

> “Always read/write the latest value from main memory.”
> 

---

### 🔑 Summary:

- `volatile` ensures **visibility** of variable updates across threads.
- It does **not ensure atomicity** (e.g., `count++` still needs synchronization).

Let me know if you want an analogy or real use case from your scheduler or approval flags!

### `volatile` in My Project

**Use Case:**

In our approval workflow system, we had background **scheduler jobs** to auto-close pending approvals.

We used a **`volatile boolean isRunning`** flag to **start/stop** the scheduler safely across threads.

---

### ✅ Example:

```java
volatile boolean isRunning = true;

public void runScheduler() {
    while (isRunning) {
        // Check for stale approvals and close them
    }
}

public void stopScheduler() {
    isRunning = false;
}

```

---

### ✅ Why `volatile`?

- Ensures that when one thread updates `isRunning`,
    
    all other threads see the **latest value immediately**.
    
- Prevents stale reads due to thread-local caching.

---

Let me know if you want to pair this with `synchronized` or `AtomicBoolean` for full control.

### Multithreading:

Allows multiple threads to run concurrently, improving performance in I/O or parallel tasks (like background schedulers or batch jobs in your project).

---

### 🔹 `synchronized` – Basic Thread Safety

**How it works:**

- Allows only **one thread** to access a **synchronized block or method** at a time.
- It locks on the **object** (or class, if static).

**Example:**

```java
public synchronized void update() {
    // critical section
}

```

Or:

```java
synchronized (this) {
    // only one thread can enter this block
}

```

### `Lock` Interface – Advanced Control (`ReentrantLock`)

**How it works:**

- Gives **explicit control** over locking and unlocking.
- Supports **tryLock**, **timeout**, and **fairness**.

**Example:**

```java
Lock lock = new ReentrantLock();

lock.lock();
try {
    // critical section
} finally {
    lock.unlock(); // always release the lock
}

```

### `synchronized` vs `Lock`

| Feature | `synchronized` | `Lock` (`ReentrantLock`) |
| --- | --- | --- |
| Basic usage | Easy | More control (e.g., tryLock) |
| Interruptible | ❌ No | ✅ Yes |
| Fairness option | ❌ No | ✅ Yes (`new ReentrantLock(true)`) |
| Manual unlock | ❌ No | ✅ Yes (must call `unlock()`) |

### ✅ Real Project Use:

- Used `synchronized` in scheduler jobs to ensure only one job processed approvals at a time.
- For more complex logic (like shared consultant cache), used `ReentrantLock` to prevent deadlocks and allow timeout.

How can I implement locking in an application where two services are updating the same database at the same time?

### 1. **Application-Level Locking (Java Side)**

Use `ReentrantLock` to ensure only one thread in your application modifies the record at a time.

**✅ Example using `ConcurrentHashMap` + `ReentrantLock`:**

```java
import java.util.concurrent.*;

@Service
public class ApprovalService {

    private final Map<String, ReentrantLock> locks = new ConcurrentHashMap<>();

    public void updateApproval(String requestId) {
        ReentrantLock lock = locks.computeIfAbsent(requestId, id -> new ReentrantLock());

        lock.lock();
        try {
            // safely update the DB for the given requestId
            System.out.println("Updating request: " + requestId);
            // call repository.save() or update query
        } finally {
            lock.unlock();
        }
    }
}

```

**🧠 Use Case:** Ensures two threads/services updating **same ID** will wait for each other.

---

### 🔹 2. **Database-Level Locking (Recommended for Multi-Node Services)**

If **two different services or instances** are accessing the **same DB**, app-level locking **won’t work across JVMs**.

### ✅ Use **Optimistic Locking** (preferred):

- Use a `@Version` field with **JPA/Hibernate**.
- If the version has changed, the update fails — preventing overwrite.

**Entity Example:**

```java
@Entity
public class ApprovalRequest {
    @Id
    private String id;

    @Version
    private int version; // JPA auto-manages this
}

```

If two services read the same row, only the first update will succeed — second will throw `OptimisticLockException`.

---

### ✅ Use **Pessimistic Locking** (when strict locking is needed):

**JPA Example:**

```java
@Lock(LockModeType.PESSIMISTIC_WRITE)
@Query("SELECT a FROM ApprovalRequest a WHERE a.id = :id")
ApprovalRequest lockAndFetch(@Param("id") String id);

```

This will **lock the row** in DB, blocking other transactions until current one finishes.

---

### ✅ Recommendation Based on Scenario:

| Scenario | Solution |
| --- | --- |
| Same JVM / single service | Use `ReentrantLock` or `synchronized` |
| Multi-instance / microservices | Use **Optimistic** or **Pessimistic locking** with DB |
| Distributed locks (across JVMs) | Use **Redis lock** or **Zookeeper lock** (advanced) |

### **1. Application-Level Locking**

Use `ReentrantLock` in Java to prevent concurrent updates on the same record in a single JVM.

Use a `ConcurrentHashMap<id, lock>` to manage locks per request or entity.

---

### 🔹 **2. Optimistic Locking (DB-Level)**

Add a `@Version` field to your JPA entity; Hibernate checks version before update.

If another service already updated, it throws `OptimisticLockException`.

---

### 🔹 **3. Pessimistic Locking (DB-Level)**

Use `@Lock(LockModeType.PESSIMISTIC_WRITE)` to lock the row during read.

Prevents other services from updating the row until the current transaction ends.

How do we use the transaction manager for transaction management, and how do we implement it?

### Using `@Transactional` for Transaction Management

Add `@Transactional` on your **service method** to ensure DB operations are atomic.

Spring uses the configured **transaction manager** (like JPA or JDBC) to begin, commit, or rollback automatically.

```java
@Service
public class ApprovalService {

    @Transactional
    public void processApproval() {
        // step 1: fetch
        // step 2: update status
        // step 3: save log
        // all will commit or rollback together
    }
}

```

### How `@Transactional` Works Internally (2–3 lines)

Spring uses **AOP (Aspect-Oriented Programming)** to wrap the method call in a **proxy**.

When a `@Transactional` method is called, the proxy:

1. **Starts a transaction** before the method.
2. **Commits** it if successful, or **rolls back** if an exception is thrown.
    
    The actual transaction manager (like JPA, JDBC) does the DB-level work.
    

### Role of Spring Boot Starter

**Spring Boot Starters** are pre-configured **dependency bundles** that simplify setup.

For example, `spring-boot-starter-data-jpa` includes everything needed for JPA (Hibernate, DataSource, etc.) — so you don’t manually add each dependency.

### How Spring Boot Bootstraps Configuration

Spring Boot uses **`@SpringBootApplication`** (which includes `@EnableAutoConfiguration`) to **auto-load configurations** based on the classpath.

It reads `application.properties` or `application.yml`, sets up beans, DB, web server, etc., using **SpringFactories mechanism** behind the scenes.

I want to bypass some services for authorization. How can I do that?

### How to Bypass Authentication for Specific Endpoints

Use `WebSecurityConfigurerAdapter` or `SecurityFilterChain` (Spring Boot 2.7+/3.x) to **exclude specific paths**.

```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    return http
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/health", "/public/**").permitAll() // bypass these
            .anyRequest().authenticated()
        )
        .build();
}

```

**Use Case:**

Bypass

```
/login
```

,

```
/docs
```

, or

```
/health
```

endpoints from authentication checks.

technical Questions asked:

1️⃣ Please introduce yourself briefly.

2️⃣ Explain one feature of Java 8.

3️⃣ What happens if a constructor is declared private?

4️⃣ Have you used any Design Patterns? Give an example.

5️⃣ Factory Design Pattern vs Abstract Factory Pattern—what’s the difference?

6️⃣ Best practices for logging exceptions in Java applications?

7️⃣ What does it mean to serialize an Employee object?

8️⃣ Explain ThreadPool and its usage.

9️⃣ What happens if an exception occurs inside a finally block?

🔟 How is Stream API different from traditional loops?

1️⃣1️⃣ Convert a List of Employees to a Map (EmpId → Salary) using Stream API.

1️⃣2️⃣ What are the different Spring bean scopes?

1️⃣3️⃣ Have you worked on any performance improvements? Share examples.

1️⃣4️⃣ How do you perform validation on incoming REST API requests?

1️⃣5️⃣ How to send a JSON response for a custom exception from a service?

1️⃣6️⃣ How to create a custom repository in Spring Data JPA?

1️⃣7️⃣ Fetch a parent and its child records using Spring Data JPA.

1️⃣8️⃣ What are the advantages of microservices?

1️⃣9️⃣ How do you handle distributed transactions across multiple microservices with independent databases?

2️⃣0️⃣ What caching mechanisms have you used?

2️⃣1️⃣ How much data can be stored in a cache?

2️⃣2️⃣ How do you debug memory leaks in a large project?

2️⃣3️⃣ Explain event-driven architecture.

2️⃣4️⃣ What are security best practices for microservices development?

2️⃣5️⃣ How would you introduce session-based authentication into an existing API?

2️⃣6️⃣ What testing methods do you follow after development?

2️⃣7️⃣ What is Mockito Spy and how is it used?

2️⃣8️⃣ Do you have experience with cloud platforms?

2️⃣9️⃣ Can integration testing be done before QA receives your code?

3️⃣0️⃣ Are you familiar with tools for component or integration testing?

3️⃣1️⃣ What are the best coding practices you follow?

3️⃣2️⃣ What is constructor-based dependency injection in Spring?

3️⃣3️⃣ Explain the use of the @Bean annotation in Spring.

3️⃣4️⃣ How do you read a JSON file and extract an object inside the “result” field?

3️⃣5️⃣ How do you map Object1 (100 parameters) to Object2 (20 parameters)?

Multi-threading & concurrency (locks, deadlocks, thread safety)

Memory management (heap vs stack, GC)

Collections internal working (HashMap collisions, ConcurrentHashMap)

Design patterns & low-level design

Spring Boot internals (DI, bean lifecycle)

Databases + SQL optimization

Distributed caching basics

𝐇𝐚𝐬𝐡𝐌𝐚𝐩 (𝐍𝐨𝐧-𝐭𝐡𝐫𝐞𝐚𝐝-𝐬𝐚𝐟𝐞)

Uses array of buckets (Node<K,V>[] table).

Each bucket is a linked list (or balanced tree in Java 8+ when collisions are high).

Hashing: hashCode() → spreads hash → index in bucket.

Collision resolution: Linked List or Tree.

Resize: When load factor exceeds threshold (default 0.75), it doubles size and rehashes.

❌ Not thread-safe → can cause infinite loops or data inconsistency if used in multi-threaded env.

🔹 𝐂𝐨𝐧𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐇𝐚𝐬𝐡𝐌𝐚𝐩 (𝐓𝐡𝐫𝐞𝐚𝐝-𝐬𝐚𝐟𝐞)

Introduced to solve HashMap’s thread-safety issue.

Java 7: Segmented locking (divides buckets into segments, each with its own lock).

Java 8+: Bucket-level locking using CAS + synchronized blocks on nodes instead of entire map.

Uses fine-grained concurrency → multiple threads can operate on different buckets without blocking each other.

Does not allow null keys/values (to avoid ambiguity in multi-threaded env).

🎯 How to explain in interviews:

Start with HashMap basics (bucket, collision, resizing).

Move to its limitations (thread-safety).

Introduce ConcurrentHashMap design (segmentation / bucket-level concurrency).

End with use-cases:

HashMap → single-threaded env (fast, simple).

ConcurrentHashMap → multi-threaded env (safe, scalable).

Core Java & Concurrency

1️⃣ 🏦 Two threads update a bank account balance → how do you ensure consistency?

2️⃣ 🔄 Two threads access a HashMap simultaneously → what happens & how do you fix it?

3️⃣ 💥 Service crashes with OutOfMemoryError in production → how will you debug?

4️⃣ 📂 You need to store millions of records & frequently search → choose HashMap, TreeMap, or ConcurrentHashMap? Why?

5️⃣ 🧩 How would you design a thread-safe Singleton class?

🔹 Exception Handling

6️⃣ ⚠️ A REST API sometimes returns null, sometimes throws exceptions → how do you handle both?

7️⃣ 📢 A checked exception occurs deep in the code → how do you propagate without breaking contracts?

8️⃣ 🔁 A third-party service fails randomly → how would you handle retries & fallbacks?

🔹 SQL & Database

9️⃣ 🚉 Two users try to book the same train seat → how do you ensure only one booking succeeds?

🔟 🐢 A table has millions of rows & queries are slow → how do you optimize performance?

1️⃣1️⃣ 📜 How do you implement efficient pagination without OFFSET slowness?

1️⃣2️⃣ 📝 You need to audit all changes (insert/update/delete) → how would you design it?

🔹 Spring Boot

1️⃣3️⃣ 🔀 If you have two APIs with the same path & method, what will happen?

1️⃣4️⃣ ⏳ A JWT token expires while user is still active → how do you refresh it?

1️⃣5️⃣ 📝 You need to log only certain APIs → use a Filter or Interceptor? Why?

1️⃣6️⃣ 🔄 You face a circular dependency between beans → how do you resolve it?

🔹 Microservices

1️⃣7️⃣ 🛡️ If one microservice goes down → how do you prevent cascading failures?

1️⃣8️⃣ 💳 Payment service double-charges users under high load → how do you debug & fix it?

1️⃣9️⃣ 🔑 How do you ensure idempotency in a payment API?

2️⃣0️⃣ 🔗 You need a distributed transaction across Order, Payment, Inventory → how do you handle it?

2️⃣1️⃣ 📌 How do you manage API versioning without breaking clients?

2️⃣2️⃣ 🐢 One microservice is slow & degrading performance → how do you isolate & fix it?

2️⃣3️⃣ 📈 During Black Friday traffic, how do you scale services to handle 1M+ requests/minute?

1️⃣ Explain OOP concepts with examples.

2️⃣ What are the new features in Java 8?

3️⃣ How do you handle exceptions in Spring Boot?

4️⃣ REST API design best practices.

5️⃣ How do you manage communication between microservices?

6️⃣ SQL query to fetch the 2nd highest salary.

7️⃣ Scenario-based question on project migration.

8️⃣ How do you secure microservices?

9️⃣ Explain the concept of Multithreading.

🔟 Difference between map and flatMap.

1️⃣ What is Spring Boot, and how is it different from Spring Framework?

2️⃣ What are Spring Boot Starters and why are they important?

3️⃣ How does auto-configuration actually work behind the scenes?

4️⃣ Difference between

[**application.properties**](http://application.properties/)

and application.yml?

5️⃣ How do profiles help in managing environments (dev, test, prod)?

6️⃣ How does Spring Boot handle embedded servers like Tomcat or Jetty?

7️⃣ What is Spring Boot Actuator and when should you use it?

8️⃣ Difference between @SpringBootApplication and @EnableAutoConfiguration?

9️⃣ How do you secure a Spring Boot app (basic auth, JWT, OAuth2)?

🔟 How do you monitor & manage a Spring Boot application in production?

1️⃣ What is rate limiting and how do you implement rate limiting in your application?

2️⃣ Suppose a producer sends a huge amount of data to a topic, how can the consumer read/process the data efficiently?

3️⃣ Why did you use Kafka when AWS SNS and RabbitMQ are also available?

4️⃣ Why are you looking for a job change?

5️⃣ What challenges have you faced in your project and how did you handle them?

6️⃣ How did you implement pagination in your project? How do OFFSET and LIMIT work in SQL, and if you want to go to the last page, what would be your query?

7️⃣ What is serialization, and how are Java objects serialized and deserialized?

8️⃣ What is the difference between Set and HashSet?

9️⃣ What is flatMap and how is it different from map in Java streams?

🔟 What are the different bean scopes in Spring?

1️⃣1️⃣ What is the purpose of equals() and hashCode() methods, and how do they work?

1️⃣2️⃣ What is the internal working of HashSet?

1️⃣3️⃣ What is an API Gateway and why is it used?

1️⃣4️⃣ How do you implement security in a Spring Boot application?

1️⃣5️⃣ Can we inject a singleton bean into a prototype bean class in Spring?

1️⃣6️⃣ Write a program to sort Employee objects using firstName, and if firstName is the same, then sort by lastName.

Differentiate between == and .equals() in Java.

- Describe the internal workings of HashMap. What occurs when two keys share the same hash code?
- Define String, StringBuilder, and StringBuffer. Which is preferable in multithreaded code and why?
- Elaborate on checked vs unchecked exceptions with examples.
- What sets an abstract class apart from an interface in Java 8+?
- How does Java manage memory (Heap, Stack, Garbage Collection)?
- Explain the usage of transient and volatile keywords.
- *Collections & Concurrency:**
- Contrast HashMap, LinkedHashMap, and TreeMap.
- Compare ConcurrentHashMap and Hashtable.
- How does the synchronized keyword function? When is ReentrantLock preferred?
- Describe the thread lifecycle states in Java.
- Differentiate between ExecutorService and manual thread creation.
- *Java 8 Features:**
- Define functional interfaces and their applications.
- Explore the Streams API. How does map() differ from flatMap()?
- Compare Optional.ofNullable() and Optional.of().
- Provide an example utilizing Collectors.groupingBy().
- *Spring & Microservices (Relevant for 3–4 YOE):**
- Distinguish Spring from Spring Boot.
- Explain the workings of dependency injection in Spring.
- Differentiate between @Component, @Service, and @Repository annotations.
- How does Spring Boot manage external configuration (

[**application.properties**](http://application.properties/)

vs YAML vs environment variables)?

- Detail Spring's transaction management with @Transactional.
- Define the role of API Gateway in microservices.
- Implement communication between two microservices (REST vs Kafka/Queue).
- *Database & JPA:**
- Contrast JDBC, Hibernate, and JPA.
- Enumerate the types of joins in SQL.
- Explain how lazy loading operates in Hibernate and its potential drawbacks.
- Differentiate save() from saveAndFlush() in JPA.