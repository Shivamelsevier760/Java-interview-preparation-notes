# Medium interview company questions part 5 by Shivam Srivastava

# **Morgan Stanley Java Developer Interview**

## **1. How can you make your code more flexible (scalable)?**

To ensure our code remains flexible and scalable, we follow key principles such as SOLID, design patterns, dependency injection, and modular architecture.

## **1. Follow SOLID Principles**

- **Single Responsibility:** Each class should focus on one responsibility.
- **Open/Closed:** The system should be open for extension but closed for modification.
- **Liskov Substitution:** Subtypes should be interchangeable with base types.
- **Interface Segregation:** Large interfaces should be split into smaller, more specific ones.
- **Dependency Inversion:** We should depend on abstractions, not concrete implementations.

For instance, in a payment processing system, we should avoid tightly coupling payment methods with the main service. Instead, we use interfaces to ensure flexibility.

## **2. Use Abstraction & Dependency Inversion**

Instead of hardcoding payment logic inside the service, we define an interface that multiple payment methods can implement.

This follows the Dependency Inversion Principle, ensuring that higher-level modules do not depend on low-level details.

```
// Abstraction to ensure flexibility and dependency inversion
interface PaymentProcessor {
    void processPayment(double amount);
}
```

## **3. Implement Open/Closed Principle**

By using polymorphism, we can extend the system without modifying existing code. New payment methods can be added without altering the core logic.

```
// Concrete implementations following Open/Closed Principle
class CreditCardPayment implements PaymentProcessor {
    public void processPayment(double amount) {
        System.out.println("Processing Credit Card payment of $" + amount);
    }
}

class PayPalPayment implements PaymentProcessor {
    public void processPayment(double amount) {
        System.out.println("Processing PayPal payment of $" + amount);
    }
}
```

## **4. Use Factory Pattern for Scalability**

To avoid directly instantiating objects, we use the Factory Pattern. This centralizes object creation and makes it easier to introduce new payment types in the future.

```
// Factory Pattern for flexible object creation
class PaymentFactory {
    public static PaymentProcessor getPaymentProcessor(String type) {
        return switch (type.toLowerCase()) {
            case "creditcard" -> new CreditCardPayment();
            case "paypal" -> new PayPalPayment();
            default -> throw new IllegalArgumentException("Invalid payment type");
        };
    }
}
```

## **5. Use Dependency Injection for Loose Coupling**

Instead of hardcoding dependencies, we inject them into the service class. This makes unit testing easier and improves maintainability.

```
// Dependency Injection ensures flexibility and testability
class PaymentService {
    private final PaymentProcessor paymentProcessor;

    public PaymentService(PaymentProcessor paymentProcessor) {
        this.paymentProcessor = paymentProcessor;
    }
    public void makePayment(double amount) {
        paymentProcessor.processPayment(amount);
    }
}
```

## **6. Demonstrate Scalability in Action**

Now, we can dynamically switch between payment methods without modifying any existing logic.

```
public class ScalableCodeDemo {
    public static void main(String[] args) {
        // Dynamically selecting payment processor
        PaymentProcessor processor = PaymentFactory.getPaymentProcessor("creditcard");
        PaymentService service = new PaymentService(processor);
        service.makePayment(100.0);

        // Easily switch to another payment method
        PaymentProcessor anotherProcessor = PaymentFactory.getPaymentProcessor("paypal");
        PaymentService anotherService = new PaymentService(anotherProcessor);
        anotherService.makePayment(200.0);
    }
}
```

## **7. Implement Asynchronous Processing for Scalability**

For real-world applications, we often need asynchronous processing. Using message queues (Kafka, RabbitMQ) or multithreading ensures that our system can scale efficiently.

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

// Asynchronous execution using ExecutorService
class AsyncPaymentService {
    private final ExecutorService executor = Executors.newFixedThreadPool(5);
    public void processPaymentAsync(PaymentProcessor processor, double amount) {
        executor.submit(() -> processor.processPayment(amount));
    }
}
```

## **8. Caching and Performance Optimization**

To improve performance, we use caching mechanisms like Redis or in-memory caching. This helps avoid redundant computations and speeds up frequently accessed data.

## **2. How can you identify that the written code is most optimal code?**

We can identify if the written code is optimal by evaluating the following factors:

## **1. Time and Space Complexity**

- Use Big-O notation to analyze efficiency.
- Aim for the lowest possible time complexity without sacrificing readability.
- **Example:** Finding the maximum element in an array:

```
// O(N) - Linear Time Complexity
public int findMax(int[] arr) {
    int max = Integer.MIN_VALUE;
    for (int num : arr) {
        if (num > max) {
            max = num;
        }
    }
    return max;
}
```

- If the array is sorted, the optimal approach is `arr[arr.length - 1]` in O(1) time.

## **2. Avoiding Unnecessary Computations**

- Reduce redundant calculations using caching or memoization.
- **Example**: Fibonacci series computation:

```
// O(2^N) - Naive Recursive Approach (Inefficient)
public int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

```
// O(N) - Optimized with Memoization
public int fibonacciOptimized(int n, Map<Integer, Integer> memo) {
    if (n <= 1) return n;
    if (memo.containsKey(n)) return memo.get(n);
    int result = fibonacciOptimized(n - 1, memo) + fibonacciOptimized(n - 2, memo);
    memo.put(n, result);
    return result;
}
```

## **3. Choosing the Right Data Structures**

- Selecting the appropriate data structure impacts performance.
- **Example**: Searching for an element in a collection:

```
// O(N) - Searching in a List
boolean findInList(List<Integer> list, int target) {
    return list.contains(target);
}

// O(1) - Using HashSet for Faster Lookup
boolean findInSet(Set<Integer> set, int target) {
    return set.contains(target);
}
```

- Use HashSet for frequent lookups instead of a List to achieve O(1) time complexity.

## **4. Benchmarking and Profiling**

- Measure execution time to detect bottlenecks.
- Use `System.nanoTime()` or JMH (Java Microbenchmark Harness).

```
long startTime = System.nanoTime();
findMax(arr);

long endTime = System.nanoTime();
System.out.println("Execution Time: " + (endTime - startTime) + " ns");
```

## **5. Parallelization and Concurrency**

- Optimize CPU-bound operations using parallel processing.
- **Example**: Using parallel streams for large datasets:

```
list.parallelStream().forEach(System.out::println);
```

- Use multithreading to improve performance when dealing with large-scale data.

## **3. What is ConcurrentHashMap and what are it’s use cases?**

`ConcurrentHashMap` is a thread-safe, high-performance implementation of `Map` from the `java.util.concurrent` package.

It allows multiple threads to read and write simultaneously without locking the entire map, making it more efficient than `Collections.synchronizedMap()`.

## **Features**

1. **Thread-Safety with High Performance**
- Uses fine-grained locking (bucket-level locks) instead of synchronizing the whole map.
- From Java 8 onwards, it relies on Compare-And-Swap (CAS) operations for updates.

**2. No `null` Keys or Values**

- Unlike `HashMap`, `ConcurrentHashMap` does not allow `null` keys or values to avoid ambiguity in concurrent operations.

**3. Atomic Operations**

- Methods like `putIfAbsent()`, `remove(key, value)`, and `computeIfPresent()` ensure atomic modifications.

**4. Better Scalability than `Collections.synchronizedMap()`**

- `synchronizedMap()` locks the entire map for every operation, causing contention in multi-threaded applications.
- `ConcurrentHashMap` locks only specific buckets, allowing more parallel operations.

## **Use Cases**

1. **Multi-Threaded Caching**
- Frequently used for in-memory caching, where multiple threads read and update data.

**2. Real-Time Analytics**

- Used in applications tracking live user activity, like counting website visits or event occurrences.

**3. Counters and Frequency Maps**

- Ideal for word frequency counters, logging request counts, or storing metrics in concurrent systems.

```
map.merge("event", 1, Integer::sum);
```

**4. Thread-Safe Configuration Storage**

- Helps store dynamic configuration settings that multiple threads update.

**5. Concurrent Queues and Task Processing**

- Used in multi-threaded messaging systems where tasks are picked and processed by worker threads.

## **Example**

```
import java.util.concurrent.*;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
        // Adding values
        map.put("A", 1);
        map.put("B", 2);
        // Atomic put-if-absent
        map.putIfAbsent("C", 3);
        // Atomic update
        map.computeIfPresent("A", (key, val) -> val + 10);
        // Removing conditionally
        map.remove("B", 2);
        System.out.println(map);  // Output: {A=11, C=3}
    }
}
```

**Use `ConcurrentHashMap` When:**

- Multiple threads need to modify a shared map.
- You need a high-performance thread-safe alternative to `HashMap`.
- You require atomic operations like `putIfAbsent()`.

**Avoid `ConcurrentHashMap` When:**

- You need `null` keys or values.
- Your application is single-threaded (use `HashMap` instead).
- You need sorted data (use `ConcurrentSkipListMap`).

## **4. What is Java Vert.x? What are it’s advantages and disadvantages?**

Vert.x is a reactive, event-driven, and non-blocking framework for building high-performance applications on the JVM (Java Virtual Machine).

It is similar to Node.js but supports multiple languages like Java, Kotlin, Groovy, Scala, and JavaScript.

It follows the reactive programming paradigm and uses a verticle-based concurrency model instead of traditional threads.

## **Features**

1. **Event-Driven & Non-Blocking**
- Uses an event loop model (similar to Node.js) for handling concurrency without blocking threads.

**2. Polyglot (Multi-Language Support)**

- Supports multiple JVM languages: Java, Kotlin, Groovy, Scala, JavaScript.

**3. Verticle-Based Concurrency Model**

- Instead of using Java threads, Vert.x runs “verticles” (lightweight reactive components) on an event loop.

**4. Clustered and Distributed**

- Supports clustering and distributed event buses, making it easy to scale.

**5. Microservices & WebSockets**

- Ideal for microservices architectures and supports WebSockets, HTTP, and event-driven messaging.

## **Advantages**

**1. High Performance (Non-Blocking I/O)**

- Uses Netty for non-blocking I/O, making it highly efficient for handling concurrent requests.
- Performs better than traditional thread-per-request models.

**2. Lightweight & Scalable**

- Unlike Java EE, it does not require a heavyweight application server.
- Runs as a simple JAR file with minimal dependencies.

**3. Reactive & Asynchronous Programming**

- Built-in support for reactive programming with RxJava, Kotlin Coroutines, and CompletableFuture.

**4. Polyglot & Modular Architecture**

- Developers can write Vert.x applications in multiple languages and use various modules.

**5. Easy to Deploy and Scale**

- Supports Docker, Kubernetes, and cloud-native deployments.

## **Disadvantages**

**1. Learning Curve**

- Developers used to traditional Java EE or Spring Boot might struggle with the reactive programming model.

**2. Debugging Complexity**

- Asynchronous & non-blocking calls make debugging and stack traces harder to follow.

**3. Not Ideal for CPU-Intensive Tasks**

- Designed for I/O-bound tasks (like API handling, messaging).
- CPU-heavy tasks can block the event loop unless handled properly.

**4. Less Mature Ecosystem Compared to Spring Boot**

- Spring Boot has richer libraries and stronger enterprise adoption.
- Vert.x is still evolving in comparison.

## **Example:**

```
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Vertx;

public class VertxHttpServer extends AbstractVerticle {
    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();
        vertx.deployVerticle(new VertxHttpServer());
    }
    @Override
    public void start() {
        vertx.createHttpServer()
            .requestHandler(req -> req.response()
                .putHeader("content-type", "text/plain")
                .end("Hello from Vert.x!"))
            .listen(8080);
    }
}
```

- Runs a non-blocking HTTP server on port 8080
- Handles thousands of concurrent requests efficiently

## **5. Is it possible to use batch jobs using Java Vert.x?**

Yes, it is possible to use batch jobs in Java Vert.x.

Vert.x is primarily an event-driven, non-blocking framework, but we can still implement batch jobs using different approaches.

## **Approaches for Running Batch Jobs in Vert.x**

## **1. Using `Vertx.setPeriodic()` for Scheduled Batch Jobs**

- **Use case:** Running a job at fixed intervals (e.g., cleaning old database records).
- **Working:** Runs asynchronously on a worker thread.

**Example**:

```
import io.vertx.core.Vertx;

public class BatchJobExample {
    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();
        // Schedule a batch job to run every 10 seconds
        vertx.setPeriodic(10000, id -> {
            System.out.println("Executing batch job at: " + System.currentTimeMillis());
            performBatchProcessing();
        });
    }
    private static void performBatchProcessing() {
        System.out.println("Processing batch records...");
        // Simulate batch task (e.g., DB updates, API calls)
    }
}
```

## **2. Using `Worker Verticles` for Long-Running Batch Jobs**

- **Use case:** Processing large data sets without blocking the event loop.
- **Working:** Runs the batch job in a worker thread pool.

**Example**:

```
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Vertx;

public class BatchWorkerVerticle extends AbstractVerticle {
    @Override
    public void start() {
        vertx.executeBlocking(promise -> {
            System.out.println("Running batch job in worker thread...");
            processLargeBatch();
            promise.complete();
        }, res -> System.out.println("Batch job completed."));
    }
    private void processLargeBatch() {
        // Simulating batch processing (e.g., processing millions of records)
        try {
            Thread.sleep(5000); // Simulate time-consuming work
            System.out.println("Batch processing finished.");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();
        vertx.deployVerticle(new BatchWorkerVerticle());
    }
}
```

## **3. Using `Vertx Scheduler` with Quartz for Cron-Based Jobs**

- **Use case:** Running cron-based batch jobs (e.g., daily report generation).
- **How it works:** Integrates Quartz Scheduler with Vert.x.

**Example**:

```
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Vertx;
import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

public class QuartzBatchJob extends AbstractVerticle {
    @Override
    public void start() {
        try {
            Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
            scheduler.start();
            JobDetail job = JobBuilder.newJob(BatchJob.class)
                    .withIdentity("batchJob", "group1").build();
            Trigger trigger = TriggerBuilder.newTrigger()
                    .withIdentity("cronTrigger", "group1")
                    .withSchedule(CronScheduleBuilder.cronSchedule("0 0/2 * * * ?")) // Every 2 minutes
                    .build();
            scheduler.scheduleJob(job, trigger);
        } catch (SchedulerException e) {
            e.printStackTrace();
        }
    }
    public static class BatchJob implements Job {
        public void execute(JobExecutionContext context) {
            System.out.println("Executing scheduled batch job at: " + System.currentTimeMillis());
        }
    }
    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();
        vertx.deployVerticle(new QuartzBatchJob());
    }
}
```

## **6. If your batch jobs consumes an endpoint and during the batch run, there is a timeout error. So, how will you retry/reprocess the remaining records?**

When a batch job consumes an external API/endpoint and encounters a timeout error, it’s important to retry or reprocess the failed records efficiently.

Below are different approaches to handle this situation:

## **1. Implement Retry Mechanism (Exponential Backoff)**

Before marking a record as failed, retry the request a few times with increasing delay (**exponential backoff**) to avoid overwhelming the endpoint.

## **Using Spring Retry (if using Spring Boot)**

```
import org.springframework.retry.annotation.Backoff;
import org.springframework.retry.annotation.Retryable;
import org.springframework.stereotype.Service;
import java.net.SocketTimeoutException;

@Service
public class ApiService {
    @Retryable(
        value = { SocketTimeoutException.class },
        maxAttempts = 3,
        backoff = @Backoff(delay = 2000, multiplier = 2)
    )
    public String callExternalApi() throws SocketTimeoutException {
        // Simulating API call
        if (Math.random() > 0.7) {
            throw new SocketTimeoutException("Timeout occurred");
        }
        return "Success";
    }
}
```

- Automatically retries if a timeout occurs.
- Backoff prevents flooding the server with retries.

## **2. Store Failed Records for Reprocessing**

If retries fail, store the failed records in a database or queue (e.g., Kafka, RabbitMQ) for later reprocessing.

## **Using a “Retry Table”**

```
CREATE TABLE failed_records (
    id SERIAL PRIMARY KEY,
    record_data TEXT,
    error_message TEXT,
    retry_count INT DEFAULT 0,
    status VARCHAR(10) DEFAULT 'FAILED'
);
```

- Re-run failed jobs manually or on schedule.
- Prevents data loss by tracking failures.

## **3. Reprocess Using a Message Queue (Kafka/RabbitMQ)**

Instead of storing in a DB, push failed records into a queue and retry later.

## **Producer (Storing Failed Requests in Kafka)**

```
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class KafkaProducerService {
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    public void sendToRetryQueue(String failedRecord) {
        kafkaTemplate.send("retry_topic", failedRecord);
    }
}
```

## **Consumer (Retrying Failed Requests)**

```
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService {
    @KafkaListener(topics = "retry_topic", groupId = "batch_jobs")
    public void processFailedRecord(String record) {
        // Reprocess the failed record
        System.out.println("Retrying record: " + record);
    }
}
```

- Asynchronous retry mechanism.
- Highly scalable for large batch jobs.

## **4. Partial Batch Processing with Checkpoints**

- Instead of failing the entire batch, mark each record as “processed” or “failed” in the DB.
- Maintain a checkpoint (last successful record ID) and resume from there.

## **Example: Processing Records in Chunks**

```
int batchSize = 100;
int retryCount = 3;

for (Record record : batchList) {
    boolean success = false;
    int attempt = 0;

    while (attempt < retryCount && !success) {
        try {
            callExternalApi(record);
            updateStatus(record.getId(), "SUCCESS");
            success = true;
        } catch (TimeoutException e) {
            attempt++;
        }
    }
    if (!success) {
        updateStatus(record.getId(), "FAILED");
    }
}
```

- Ensures that processed records are not retried unnecessarily.
- Allows reprocessing of only failed records later.

## **5. Scheduled Job for Reprocessing Failed Records**

If records fail even after retries, schedule a nightly/periodic job to retry them.

## **Spring Boot Scheduler for Retrying Failed Jobs**

```
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class RetryBatchJob {
    @Scheduled(fixedDelay = 60000) // Runs every minute
    public void retryFailedJobs() {
        List<Record> failedRecords = fetchFailedRecords();
        for (Record record : failedRecords) {
            try {
                callExternalApi(record);
                updateStatus(record.getId(), "SUCCESS");
            } catch (Exception e) {
                System.out.println("Retry failed for record: " + record.getId());
            }
        }
    }
}
```

- Runs automatically to retry failed requests.
- No manual intervention required.

## **7. How to create a new REST API?**

Steps to create a basic REST API for managing users:

## **1. Setting Up the Spring Boot Project**

We can create a Maven/Gradle project with:

- **Spring Web** (for building REST APIs)
- **Lombok** (for reducing boilerplate code)
- **Spring Boot DevTools** (for auto-reloading)

We can add the following Spring Boot Starter dependency in `pom.xml`:

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

## **2. Creating the REST API Components**

I’ll follow the **MVC (Model-View-Controller)** pattern to structure the API.

## **Step 1: Create a Model (User)**

This represents the data entity.

```
import lombok.*;

@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class User {
    private int id;
    private String name;
    private String email;
}
```

## **Step 2: Create a Service Layer**

The service layer contains business logic.

```
import org.springframework.stereotype.Service;
import java.util.*;

@Service
public class UserService {
    private final List<User> users = new ArrayList<>(List.of(
        new User(1, "Alice", "alice@example.com"),
        new User(2, "Bob", "bob@example.com")
    ));
    public List<User> getAllUsers() {
        return users;
    }
    public User getUserById(int id) {
        return users.stream()
                    .filter(user -> user.getId() == id)
                    .findFirst()
                    .orElse(null);
    }
    public void addUser(User user) {
        users.add(user);
    }
    public void deleteUser(int id) {
        users.removeIf(user -> user.getId() == id);
    }
}
```

## **Step 3: Create a REST Controller**

This handles incoming HTTP requests.

```
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserService userService;
    public UserController(UserService userService) {
        this.userService = userService;
    }
    // GET all users
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }
    // GET user by ID
    @GetMapping("/{id}")
    public User getUserById(@PathVariable int id) {
        return userService.getUserById(id);
    }
    // POST - Add a new user
    @PostMapping
    public String addUser(@RequestBody User user) {
        userService.addUser(user);
        return "User added successfully!";
    }
    // DELETE - Remove a user
    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable int id) {
        userService.deleteUser(id);
        return "User deleted successfully!";
    }
}
```

## **3. Running the API**

To start the Spring Boot application, we run:

```
mvn spring-boot:run
```

The API will be available at:[`http://localhost:8080/users`](https://archive.ph/o/ck82s/localhost:8080/users)

## **4. Testing the API**

Using Postman or curl:

**GET All Users**

```
curl -X GET http://localhost:8080/users
```

**GET User by ID**

```
curl -X GET http://localhost:8080/users/1
```

**POST Add a New User**

```
curl -X POST http://localhost:8080/users -H "Content-Type: application/json" -d '{"id": 3, "name": "Charlie", "email": "charlie@example.com"}'
```

**DELETE User by ID**

```
curl -X DELETE http://localhost:8080/users/2
```

## **5. Extending the API (Optional Enhancements)**

1. **Database Integration:** Use Spring Data JPA to persist data in MySQL/PostgreSQL.
2. **Exception Handling:** Implement `@ExceptionHandler` for better error messages.
3. **Security:** Use Spring Security + JWT authentication.
4. **API Documentation:** Use Swagger (`springdoc-openapi`) for better API visibility.

## **8. Write a query to find duplicate records in a table.**

## **Basic Query to Find Duplicates**

If we want to find duplicates based on a single column (e.g., `email` in a `users` table):

```
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

This query groups records by `email` and checks if any count is greater than 1.

## **Finding Duplicates Based on Multiple Columns**

If a record should be unique based on multiple columns (e.g., `name` and `email`):

```
SELECT name, email, COUNT(*)
FROM users
GROUP BY name, email
HAVING COUNT(*) > 1;
```

This helps detect duplicates where both `name` and `email` match.

**9. What are the differences between monolithic vs microservice architecture?**

![](https://d1s4l2jz3l15y6.archive.ph/ck82s/f746fa13f829a5119351926b0338670d8af98d86.webp)

## **10. How do you deploy your microservices to the containers?**

To deploy microservices into containers, we typically follow these steps:

## **1. Create a Dockerfile for Each Microservice**

Each microservice should have a Dockerfile to package it as a container.

**Example: Dockerfile for a Spring Boot Microservice**

```
# Use an official JDK as base image
FROM openjdk:17-jdk-slim

# Set working directory inside the container
WORKDIR /app
# Copy the JAR file into the container
COPY target/my-microservice.jar app.jar
# Expose the application port
EXPOSE 8080
# Command to run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
```

This creates a lightweight container image for your microservice.

## **2. Build & Run the Docker Image**

Use the following commands:

```
# Build Docker image
docker build -t my-microservice:latest .

# Run the container
docker run -d -p 8080:8080 my-microservice
```

Now, your microservice runs inside a Docker container.

## **3. Use Docker Compose for Multiple Microservices**

If you have multiple microservices, use Docker Compose to define and run them together.

**Example: `docker-compose.yml`**

```
version: '3.8'
services:
  user-service:
    build: ./user-service
    ports:
      - "8081:8081"
    environment:
      - SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/users
    depends_on:
      - db

db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: users
```

This sets up User Service and a MySQL database in containers.

## **4. Deploying with Kubernetes (K8s) for Scaling**

For production, use Kubernetes to manage and scale microservices.

**Example: Kubernetes Deployment (`deployment.yaml`)**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
        - name: user-service
          image: my-microservice:latest
          ports:
            - containerPort: 8081
```

```
# Deploy to Kubernetes
kubectl apply -f deployment.yaml
```

This deploys three replicas of the microservice.

## **11. How do you ensure that your endpoints work with different data formats like json, xml etc?**

To make your REST API endpoints support different data formats like JSON and XML, we need to configure content negotiation properly.

## **1. Enable Content Negotiation**

Spring Boot automatically supports JSON (via Jackson) and XML (via JAXB), but we must configure it correctly.

**Example: Spring Boot Configuration for JSON & XML**

```
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.add(new MappingJackson2HttpMessageConverter()); // JSON
        converters.add(new MarshallingHttpMessageConverter(new Jaxb2Marshaller())); // XML
    }
}
```

This ensures your API can return both **JSON and XML** responses.

## **2. Use `@RestController` with Content Negotiation**

Spring Boot automatically determines the response format based on the `Accept` header in the request.

**Example: A Simple REST API with JSON & XML Support**

```
@RestController
@RequestMapping("/users")
public class UserController {

    @GetMapping(value = "/{id}", produces = { MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE })
    public User getUser(@PathVariable int id) {
        return new User(id, "John Doe", "john@example.com");
    }
}
```

Here, the endpoint supports both JSON (`application/json`) and XML (`application/xml`) responses.

## **3. Add `@XmlRootElement` for XML Support**

By default, Java objects don’t serialize to XML unless they are annotated with `@XmlRootElement`.

**Modify the `User` Model to Support XML**

```
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class User {
    private int id;
    private String name;
    private String email;
    // Constructors, Getters, and Setters
}
```

Now, the same `User` object works for both JSON and XML.

## **4. Explicitly Define Supported Formats in Spring Boot (`application.properties`)**

```
spring.mvc.contentnegotiation.favor-path-extension=true
spring.mvc.contentnegotiation.favor-parameter=true
spring.mvc.contentnegotiation.media-types.json=application/json
spring.mvc.contentnegotiation.media-types.xml=application/xml
```

This allows clients to specify formats via URL extensions (`/users/1.xml` or `/users/1.json`) or query parameters (`?format=xml`).

## **12. How do you convert your JSON to XML format and vice versa?**

There are multiple ways to convert JSON to XML and vice versa in Java. The most common approach is using Jackson (for JSON processing) and org.json (for direct conversion).

## **1. Using org.json (Simple Approach)**

The `org.json` library provides an easy way to convert between JSON and XML.

**Maven Dependency:**

```
<dependency>
    <groupId>org.json</groupId>
    <artifactId>json</artifactId>
    <version>20210307</version>
</dependency>
```

**Example Code: JSON to XML & XML to JSON Conversion**

```
import org.json.JSONObject;
import org.json.XML;

public class JsonXmlConverter {
    public static void main(String[] args) {

        // JSON to XML Conversion
        String jsonString = "{ \"name\": \"Shivam Srivastava\", \"age\": 29, \"city\": \"New York\" }";
        JSONObject json = new JSONObject(jsonString);
        String xml = XML.toString(json);
        System.out.println("Converted XML:\n" + xml);

        // XML to JSON Conversion
        String xmlString = "<name>Shivam Srivastava</name><age>29</age><city>New York</city>";
        JSONObject jsonObject = XML.toJSONObject(xmlString);
        System.out.println("Converted JSON:\n" + jsonObject.toString(4)); // Pretty print
    }
}
```

**Output:**

```
Converted XML:
<name>Shivam Srivastava</name><age>29</age><city>New York</city>
Converted JSON:
{
    "name": "Shivam Srivastava",
    "age": 29,
    "city": "New York"
}
```

## **2. Using Jackson (More Control, JAXB for XML)**

Another way is using **Jackson** to handle JSON and **JAXB** for XML.

**Maven Dependencies:**

```
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.15.0</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-xml</artifactId>
    <version>2.15.0</version>
</dependency>
```

**Example Code: JSON to XML & XML to JSON using Jackson**

```
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

public class JacksonJsonXmlConverter {
    public static void main(String[] args) throws Exception {
        ObjectMapper jsonMapper = new ObjectMapper();
        XmlMapper xmlMapper = new XmlMapper();
        // Sample JSON String
        String jsonString = "{ \"name\": \"Shivam Srivastava\", \"age\": 29, \"city\": \"New York\" }";
        // Convert JSON to Object
        Person person = jsonMapper.readValue(jsonString, Person.class);
        // Convert Object to XML
        String xml = xmlMapper.writeValueAsString(person);
        System.out.println("Converted XML:\n" + xml);
        // Convert XML back to Object
        Person xmlToPerson = xmlMapper.readValue(xml, Person.class);
        // Convert Object back to JSON
        String jsonOutput = jsonMapper.writeValueAsString(xmlToPerson);
        System.out.println("Converted JSON:\n" + jsonOutput);
    }
}
// Model class
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;
@JacksonXmlRootElement(localName = "Person")
class Person {
    @JsonProperty
    private String name;
    @JsonProperty
    private int age;
    @JsonProperty
    private String city;
    public Person() {} // Default constructor needed
    public Person(String name, int age, String city) {
        this.name = name;
        this.age = age;
        this.city = city;
    }
}
```

## **13. Suppose you have 2 threads running simultaneously. One is printing 1,2,3,4..26 and the other one is printing A,B,C…Z. How to print 1,A,2,B,..etc.**

> This question was also asked in JP Morgan Interview. So, this is an important question.
> 

To achieve this sequence of alternating outputs (`1, A, 2, B, ...`) from two threads, we can use **synchronization mechanisms** like a shared lock (`ReentrantLock` or `synchronized`) and a condition variable (`wait/notify`) to coordinate the execution of the threads.

Here’s how we can implement this in Java:

```
class AlternatingPrinter {

private final Object lock = new Object();
  private boolean numberTurn = true; // Indicates whether it's the number thread's turn
  public static void main(String[] args) {
        AlternatingPrinter printer = new AlternatingPrinter();
        Thread numberThread = new Thread(() -> printer.printNumbers());
        Thread letterThread = new Thread(() -> printer.printLetters());
        numberThread.start();
        letterThread.start();
    }
   public void printNumbers() {
        for (int i = 1; i <= 26; i++) { // Adjust the range as needed
            synchronized (lock) {
                while (!numberTurn) {
                    try {
                        lock.wait(); // Wait until it's this thread's turn
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
                System.out.print(i + " ");
                numberTurn = false; // Pass the turn to the letter thread
                lock.notifyAll(); // Notify the waiting thread
            }
        }
    }
   public void printLetters() {
        for (char c = 'A'; c <= 'Z'; c++) { // Adjust the range as needed
            synchronized (lock) {
                while (numberTurn) {
                    try {
                        lock.wait(); // Wait until it's this thread's turn
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
                System.out.print(c + " ");
                numberTurn = true; // Pass the turn to the number thread
                lock.notifyAll(); // Notify the waiting thread
            }
        }
    }
}
```

**Output**:

```
1 A 2 B 3 C ....
```

## **14. What DB tools you can use to measure performance?**

To measure database performance, you can use both built-in database tools and third-party monitoring tools.

## **1. Built-in Database Tools**

Most databases provide their own performance monitoring tools:

1. **MySQL**
- `EXPLAIN ANALYZE`: Analyzes how a query executes.
- `SHOW STATUS`: Displays database performance metrics.
- `Performance Schema`: Monitors query execution and resource usage.

**2. PostgreSQL**

- `EXPLAIN ANALYZE`: Shows the query execution plan and timing.
- `pg_stat_statements`: Tracks slow and frequently executed queries.
- `pgBadger`: Generates detailed reports from PostgreSQL logs.

**3. Oracle**

- `AWR (Automatic Workload Repository)`: Collects database performance statistics.
- `SQL Trace` / `TKPROF`: Helps in SQL profiling and query optimization.

**4. SQL Server**

- `SQL Profiler`: Captures query execution details.
- `Dynamic Management Views (DMVs)`: Provides insights into system and query performance.

## **2. Third-Party Performance Monitoring Tools**

For large-scale applications, third-party tools provide better real-time insights:

- **New Relic** — Monitors database query performance and transaction times.
- **Datadog** — Provides real-time database analytics and alerts.
- **Prometheus + Grafana** — Open-source tools for tracking database performance.
- **SolarWinds DPA** — Helps identify slow queries and bottlenecks.
- **Percona Monitoring and Management (PMM)** — Open-source monitoring for MySQL and PostgreSQL.

## **Example: Checking Query Performance in MySQL**

```
-- Analyze query execution plan
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'SHIPPED';

-- Show database performance statistics
SHOW STATUS LIKE 'Queries';
```

# **Oracle Java Developer Interview — 2**

## **1. How would you handle logging in a REST API application?**

When it comes to logging in a REST API application, it’s essential for debugging, monitoring, and scaling applications.

## **1. Choosing a Logging Framework**

For Java-based REST APIs, we would use SLF4J with Logback as the logging framework, particularly in Spring-based applications.

SLF4J serves as the API, and Logback takes care of the actual logging.

**Maven Dependency**:

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-logging</artifactId>
</dependency>
```

## **2. Log Levels**

We should configure different log levels to capture the right amount of detail:

- **INFO**: For high-level information about request handling.
- **DEBUG**: For detailed information like request payloads or query parameters (excluding sensitive data).
- **ERROR**: For logging exception details.
- **WARN**: For non-critical issues.
- **TRACE**: For very fine-grained logs when necessary.

**Code Example**:

```
logger.info("Received request: {} {}", request.getMethod(), request.getRequestURI());
logger.debug("Request body: {}", requestBody);  // Sensitive data masked
logger.error("Error occurred while processing request", exception);
```

## **3. Logging Request and Response**

We should log key details about incoming requests and outgoing responses. This includes method type, request URI, response status, and timing to monitor performance.

**Code Example**:

```
@RequestMapping("/api/resource")
public ResponseEntity<String> getResource(HttpServletRequest request) {
    long startTime = System.currentTimeMillis();
    logger.info("Received request: {} {}", request.getMethod(), request.getRequestURI());

    // Simulating processing
    String response = "Resource data";
    long endTime = System.currentTimeMillis();
    logger.info("Response sent: {} Status: {} Time taken: {} ms", request.getRequestURI(), 200, (endTime - startTime));
    return ResponseEntity.ok(response);
}
```

## **4. Handling Exceptions**

Whenever we encounter an exception, it’s essential to log it with a detailed error message and the exception stack trace to ensure we can diagnose issues efficiently.

**Code Example**:

```
@RequestMapping("/api/resource")
public ResponseEntity<String> getResource() {
    try {
        // API processing logic that may throw exceptions
        throw new RuntimeException("Simulated error");

        } catch (Exception e) {
        logger.error("Error while processing request: {}", e.getMessage(), e);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Internal Server Error");
    }
}
```

## **5. Contextual Logging**

To make our logs more traceable, we can use MDC (Mapped Diagnostic Context) to attach contextual information, such as a correlation ID.

This helps us trace the flow of requests across multiple services in a microservices architecture.

**Code Example**:

```
@Component
public class RequestLoggingFilter implements Filter {
    private static final Logger logger = LoggerFactory.getLogger(RequestLoggingFilter.class);

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        String correlationId = UUID.randomUUID().toString();
        MDC.put("correlationId", correlationId);
        logger.info("Request received with Correlation ID: {}", correlationId);
        chain.doFilter(request, response);
        logger.info("Response sent with Correlation ID: {}", correlationId);
        MDC.clear(); // Clear the MDC to avoid memory leaks
    }
}
```

In this filter, we generate a unique correlation ID for each request and attach it to the MDC.

It allows us to correlate logs from different parts of the application.

## **6. Handling Sensitive Data**

When logging request bodies or responses, we must mask sensitive data such as passwords or credit card numbers to prevent exposing this information in the logs.

**Code Example**:

```
logger.debug("Request body: {}", maskSensitiveData(requestBody));

private String maskSensitiveData(String data) {
    // Mask sensitive data like credit card numbers or passwords
    return data.replaceAll("(?<=\\d{4})\\d{4}(?=\\d{4})", "****");
}
```

## **7. Log Rotation and Retention**

To manage log files effectively, we need to configure log rotation. This ensures that logs don’t consume excessive disk space and that older logs are archived or deleted after a certain period.

**Logback Configuration**:

```
<appender name="RollingFile" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logs/api.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
        <fileNamePattern>logs/api-%d{yyyy-MM-dd}.log</fileNamePattern>
        <maxHistory>30</maxHistory>  <!-- Keep logs for 30 days -->
    </rollingPolicy>
    <encoder>
        <pattern>%d{ISO8601} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## **8. External Monitoring**

For production environments, we should integrate with monitoring tools like ELK Stack (Elasticsearch, Logstash, Kibana) or Datadog.

These tools help aggregate logs, visualize trends, and set up alerts for anomalies or critical errors.

## **2. What are the different endpoints of actuators.**

Spring Boot Actuator provides several built-in endpoints that help monitor and manage your application.

Below are the key Actuator endpoints:

## **1. Common Actuator Endpoints**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/362bcc4e04cb8167dc5ff498134f411b1dc82f88.webp)

## **2. Metrics and Monitoring Endpoints**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/691c18d38cad7ba6c4a93d490a544f6ed78c6c21.webp)

## **3. Tracing and Auditing Endpoints**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/a430ff50598844b9def8cc4f9a0504a8fe2a3a2a.webp)

## **4. Application Management Endpoints**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/4bbad8940bc41a8205ccdeba94d7d7dd882fbddf.webp)

## **5. Shutdown and Customization Endpoints**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/6756b627972672c1f4722b8930e6a2bc3b29f3c2.webp)

## **Enabling Actuator Endpoints**

By default, only the `/actuator/health` and `/actuator/info` endpoints are enabled. To enable all endpoints, add the following in `application.properties`:

```
management.endpoints.web.exposure.include=*
```

Or selectively enable specific endpoints:

```
management.endpoints.web.exposure.include=health,metrics,loggers
```

## **3. Explain @CrossOrigin annotation.**

The `@CrossOrigin` annotation in Spring Boot is used to enable Cross-Origin Resource Sharing (CORS) for REST APIs.

CORS is a security feature in web browsers that prevents unauthorized requests from different origins.

By default, browsers block cross-origin requests for security reasons, and `@CrossOrigin` helps bypass this restriction in Spring applications.

## **1. Basic Usage**

You can apply `@CrossOrigin` at the class level (for all endpoints) or at the method level (for specific endpoints).

## **Example: Enabling CORS for All Endpoints in a Controller**

```
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "https://example.com")  // Allows requests only from example.com
public class MyController {

@GetMapping("/data")
    public String getData() {
        return "Hello from Spring Boot!";
    }
}
```

- Here, only requests from `https://example.com` are allowed.
- If a request comes from a different origin, it will be blocked.

## **2. Enabling CORS for a Specific Method**

You can allow CORS for a specific method rather than the entire class.

```
@RestController
@RequestMapping("/api")
public class MyController {

@GetMapping("/public")
    @CrossOrigin(origins = "*")  // Allows all origins
    public String publicEndpoint() {
        return "Public Data";
    }
    @GetMapping("/secure")
    @CrossOrigin(origins = "https://trusted.com")  // Only allows https://trusted.com
    public String secureEndpoint() {
        return "Secure Data";
    }
}
```

- `publicEndpoint()` is accessible from any origin ().
- `secureEndpoint()` is restricted to [`https://trusted.com`.](https://archive.ph/o/M5Swy/https://trusted.com/)

## **3. Configuring CORS for Multiple Origins**

```
@CrossOrigin(origins = {"https://site1.com", "https://site2.com"})
```

This allows requests only from `site1.com` and `site2.com`.

## **4. Allowing Specific HTTP Methods**

By default, `@CrossOrigin` allows all HTTP methods unless specified using the `methods` parameter.

You can allow specific methods like `POST`, `PUT`, `DELETE`, etc.

```
@CrossOrigin(origins = "https://example.com", methods = {RequestMethod.GET, RequestMethod.POST})
```

- This allows only `GET` and `POST` requests from [`https://example.com`.](https://archive.ph/o/M5Swy/https://example.com/)

## **5. Allowing Headers & Credentials**

You can allow custom headers and enable credentials (cookies, authentication tokens, etc.).

```
@CrossOrigin(
    origins = "https://example.com",
    allowedHeaders = {"Authorization", "Content-Type"},
    allowCredentials = "true"
)
```

- `allowCredentials = "true"`: Allows cookies and authentication headers.
- `allowedHeaders`: Specifies which headers are allowed.

## **6. Global CORS Configuration (Without `@CrossOrigin`)**

If you want to enable CORS globally for all controllers, define it in a configuration class.

```
@Configuration
public class CorsConfig {
    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/**") // Applies CORS to all API endpoints
                        .allowedOrigins("https://example.com") // Allow this origin
                        .allowedMethods("GET", "POST", "PUT", "DELETE") // Allowed methods
                        .allowedHeaders("*") // Allow all headers
                        .allowCredentials(true); // Allow authentication
            }
        };
    }
}
```

- This configuration applies CORS globally without needing `@CrossOrigin` on each controller.

**4. What are the challenges faced in microservices vs monolithic application?**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/207374231fe15d6f97f2ebccb17c06bf2f2a00c8.webp)

## **5. What is Decomposition design pattern in microservices?**

In microservices architecture, decomposition is the process of breaking down a monolithic application into smaller, independent services.

The Decomposition Design Pattern ensures that each service is:

- **Loosely coupled** → Independent, reducing dependencies on other services.
- **Scalable** → Can handle increased load efficiently.
- **Manageable** → Easier to develop, deploy, and maintain.

There are two primary approaches to decomposition:

1. Decomposition by Business Capability.
2. Decomposition by Subdomain (Domain-Driven Design — DDD).

## **1. Decomposition by Business Capability**

- Each microservice is designed around a specific business function (not a technical layer).

**Example:** An e-commerce app can be decomposed into:

- **Order Service** → Handles order creation & tracking.
- **Payment Service** → Processes payments securely.
- **Inventory Service** → Manages stock availability.

## **Use Case:**

- Best for applications with well-defined business functions.
- Services evolve independently, making scaling easier.

## **Example:**

```
@RestController
@RequestMapping("/orders")
public class OrderService {

@PostMapping
    public ResponseEntity<String> createOrder() {
        return ResponseEntity.status(HttpStatus.CREATED).body("Order Created");
    }
}
```

- `OrderService` is an independent microservice responsible for order management.
- Returns a proper HTTP response (`201 Created`).

## **2. Decomposition by Subdomain (DDD — Domain-Driven Design)**

- Based on Bounded Contexts from Domain-Driven Design (DDD).
- The system is divided into subdomains, ensuring each service operates within a clear boundary.

## **Use Case:**

- Works well for complex applications with multiple interdependent modules.
- Helps maintain data integrity by defining clear context boundaries.

## **Example (Java — Shipping Service in Logistics Subdomain)**

```
@RestController
@RequestMapping("/shipping")
public class ShippingService {

@GetMapping("/{orderId}")
    public ResponseEntity<TrackingResponse> trackOrder(@PathVariable String orderId) {
        TrackingResponse response = new TrackingResponse(orderId, "In Transit");
        return ResponseEntity.ok(response);
    }
}
class TrackingResponse {
    private String orderId;
    private String status;

    public TrackingResponse(String orderId, String status) {
        this.orderId = orderId;
        this.status = status;
    }

    // Getters and Setters
}
```

- `ShippingService` exists in the Logistics subdomain, separate from the Order subdomain.
- Uses DTO (Data Transfer Object) instead of returning raw strings.

## **3. Other Decomposition Strategies**

## **a) Decomposition by Transactions (Aggregates Pattern)**

- Services are split based on data consistency needs.
- **Example:** Order Service & Payment Service handle separate transactions and sync via event-driven mechanisms (e.g., Saga Pattern).

## **b) Decomposition by Scalability**

- Some services are separated to handle high loads independently.
- **Example:** A Search Service in an e-commerce app is split from the Product Service for better performance.

## **6. How microservices health is checked?**

In microservices, health checks ensure that services are running properly and can handle requests.

This is done using health check endpoints, Kubernetes probes, service discovery tools, and monitoring dashboards.

## **1. Health Check Endpoints**

A microservice exposes a special **HTTP endpoint** (e.g., `/health` or `/actuator/health`) that returns the service status.

## **Spring Boot Actuator (For Java-based Microservices)**

**Step 1: Add Actuator Dependency**

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

**Step 2: Enable Health Check in `application.properties`**

```
management.endpoints.web.exposure.include=health
management.endpoint.health.show-details=always
```

- `show-details=always` ensures that the health check provides details about dependencies like DB, disk space, etc.

**Step 3: Access Health Check Endpoint**

```
curl -X GET http://localhost:8080/actuator/health
```

- **Response (Service is UP)**

```
{
    "status": "UP"
}
```

- **Response (Service is DOWN)**

```
{
    "status": "DOWN",
    "details": {
        "diskSpace": {
            "status": "DOWN",
            "details": {
                "total": 50000000000,
                "free": 1000000000,
                "threshold": 10485760
            }
        }
    }
}
```

## **2. Kubernetes Health Probes**

If the microservice is deployed on Kubernetes, it uses Liveness and Readiness Probes to check the health.

- **Liveness Probe**: Checks if the service is running. If it fails, Kubernetes restarts the pod.
- **Readiness Probe**: Checks if the service is ready to handle traffic. If it fails, Kubernetes removes it from load balancing until it’s ready.

## **Example: Kubernetes Health Probes**

```
livenessProbe:
  httpGet:
    path: /actuator/health
    port: 8080
  initialDelaySeconds: 3
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /actuator/health
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

## **3. External Health Monitoring Tools**

## **Service Discovery Tools (Eureka, Consul, etc.)**

Microservices use Eureka or Consul to register themselves, and these tools check their health.

**Eureka Example**

```
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8761/eureka/
  instance:
    leaseRenewalIntervalInSeconds: 10
    leaseExpirationDurationInSeconds: 30
```

- If a service is DOWN, Eureka stops routing traffic to it.

## **4. Observability & Monitoring**

## **Monitoring Tools**

- **Prometheus & Grafana** → Collects and visualizes health metrics.
- **ELK Stack (Elasticsearch, Logstash, Kibana)** → Logs health failures.
- **Zipkin / Jaeger** → Traces requests between microservices.

## **Enabling Prometheus in Spring Boot**

```
management.metrics.export.prometheus.enabled=true
```

**Prometheus Configuration (Scrape Health Metrics)**

```
scrape_configs:
  - job_name: 'microservice-health'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: ['localhost:8080']
```

- Grafana Dashboard visualizes service uptime and failures.

**7. What are the differences between @ResponseBody vs @Inject vs @RequestParameter annotation?**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/a1805ec7c0985d7da8d82f15857414e9f68b95ad.webp)

**8. What are the differences between PUT vs PATCH?**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/e122ede7eaf10110633a8d0e1c1caf61e589e8a5.webp)

**9. What are the differences between Spring JDBC vs Spring Data JPA?**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/5c28db96cec92568de3d0d88adbf521d2e2d5858.webp)

## **10. What are different cascading types in JPA?**

In JPA, cascade types define how operations (persist, merge, remove, etc.) on a parent entity should affect related child entities.

## **1. `CascadeType.PERSIST`**

- Saves the child entity automatically when the parent is saved.
- **Example:**

```
@OneToMany(mappedBy = "parent", cascade = CascadeType.PERSIST)
private List<Child> children;
```

- **Effect:** If you save `Parent`, all associated `Child` entities are also saved.

## **2. `CascadeType.MERGE`**

- Updates child entities when the parent is updated.
- **Example:**

```
@OneToOne(cascade = CascadeType.MERGE)
private Profile profile;
```

- **Effect:** If `Parent` is updated, `Profile` is also updated.

## **3. `CascadeType.REMOVE`**

- Deletes child entities when the parent is deleted.
- **Example:**

```
@OneToMany(mappedBy = "order", cascade = CascadeType.REMOVE)
private List<OrderItem> items;
```

- **Effect:** If `Order` is deleted, all `OrderItem` entries are also deleted.

## **4. `CascadeType.DETACH`**

- Removes child entities from the persistence context when the parent is detached.
- **Example:**

```
@OneToMany(mappedBy = "company", cascade = CascadeType.DETACH)
private List<Employee> employees;
```

- **Effect:** If `Company` is detached, `Employee` entities are also detached.

## **5. `CascadeType.REFRESH`**

- Reloads child entities when the parent is refreshed.
- **Example:**

```
@OneToOne(cascade = CascadeType.REFRESH)
private Address address;
```

- **Effect:** If `Person` is refreshed, `Address` is also refreshed from the database.

## **6. `CascadeType.ALL` (Combination of All)**

- Applies all the above cascade operations (`PERSIST`, `MERGE`, `REMOVE`, `DETACH`, `REFRESH`).
- **Example:**

```
@OneToMany(mappedBy = "department", cascade = CascadeType.ALL)
private List<Employee> employees;
```

- **Effect:** Any operation on `Department` will apply to all `Employee` entities.

## **11. Why search with primary keys are faster?**

Searching with primary keys is significantly faster compared to other types of queries because of the following reasons:

## **1. Indexed Search**

- Primary keys are automatically indexed by the database.
- Indexing allows O(1) or O(log n) lookup time, making searches very efficient.
- Instead of scanning all rows, the database directly finds the record using the index.

**Example:**

```
SELECT * FROM users WHERE id = 101;  -- Fast lookup using primary key index
```

## **2. Unique Constraint Ensures One Result**

- Since primary keys are unique, the database stops searching after finding the first match.
- This avoids unnecessary full table scans (which happen in non-indexed searches).

**Slow Example (Non-Indexed Search)**:

```
SELECT * FROM users WHERE email = 'test@example.com'; -- Might scan many rows
```

**Fast Example (Indexed Primary Key Search)**:

```
SELECT * FROM users WHERE id = 101; -- Fetches instantly
```

## **3. Optimized Storage & B-Trees**

- Most relational databases use B-Trees (or B+ Trees) for indexing.
- B-Trees reduce search time to O(log n) instead of O(n).
- This means the database doesn’t need to scan all rows — it navigates the tree efficiently to find the key.

## **4. Clustered Index in InnoDB (MySQL)**

- In MySQL InnoDB, the primary key is stored as a clustered index.
- This means the actual data rows are physically stored in order of the primary key.
- Searching via the primary key directly retrieves the record without an extra lookup.

In contrast, non-primary key searches require a separate lookup in a secondary index.

## **5. Avoids Extra Sorting and Filtering**

- Since primary keys are already sorted in B-Trees, queries don’t require additional sorting or filtering operations.
- This improves performance, especially in large datasets.

## **12. Explain EXISTS and how it is used.**

`EXISTS` is a logical operator in SQL used in `WHERE` clauses to check if a subquery returns any rows. It returns TRUE if the subquery produces at least one row and FALSE if it returns zero rows.

## **Syntax**

```
SELECT column_name(s)
FROM table_name
WHERE EXISTS (subquery);
```

- The `EXISTS` clause runs the subquery.
- If the subquery returns at least one row, the outer query proceeds.
- If the subquery returns no rows, the outer query does not execute.

## **EXISTS Working**

**Example: Check if a user has orders**

```
SELECT user_id, name
FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.user_id
);
```

**Explanation:**

- The query retrieves users only if they have at least one order.
- The subquery `SELECT 1 FROM orders WHERE o.user_id = u.user_id` checks for orders linked to users.
- If at least one order exists, `EXISTS` returns `TRUE` for that user.

## **EXISTS vs. IN**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/55a06f75e4c39f8ef59f9a903fc8164ec77695de.webp)

**Example: Fetch users with orders using `IN`**

```
SELECT user_id, name
FROM users
WHERE user_id IN (SELECT user_id FROM orders);
```

EXISTS is often faster than `IN` because it stops at the first match, while `IN` evaluates all results.

## **EXISTS with NOT EXISTS**

**Find users who have NOT placed any orders**

```
SELECT user_id, name
FROM users u
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.user_id
);
```

**Explanation:**

- `NOT EXISTS` filters only users who don’t have any orders.
- The subquery returns no rows for such users, making `EXISTS` evaluate to `FALSE`, and `NOT EXISTS` returns `TRUE`.

## **13. What is the max limit of varchar and what are the differences between Byte and Char in Database?**

The maximum size of `VARCHAR` depends on the database system:

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/1502241e8226b1f375eb6ca5f1151cd03b7a084a.webp)

**MySQL Limitation**:

- The total row size cannot exceed 65,535 bytes, including all columns.
- UTF-8 encoding can use up to 4 bytes per character, so `VARCHAR(10)` may take up to 40 bytes.

## **Difference Between BYTE and CHAR in DB**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/7d07befa84ae4dcd64cf619c9501b3181d999489.webp)

**14. What are the differences between 2NF vs 3NF?**

![](https://d5m5k4y1rvhvk5.archive.ph/M5Swy/40c8852d796fc93628d33c29cd5cf2e2431a2223.webp)

## **15. Write a query to find top 5 employees details having salary greater than average salary of all employees in the company.**

## **Approach 1: Using TOP or LIMIT**

This query retrieves the top 5 highest-paid employees who earn above the average salary in the company.

## **SQL Query (MySQL & PostgreSQL)**

```
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC
LIMIT 5;
```

## **SQL Query (SQL Server)**

```
SELECT TOP 5 *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;
```

## **Approach 2: Handling Salary Ties with `RANK()`**

If multiple employees have the same salary, `LIMIT 5` may skip employees with equal salaries.

To ensure all employees with the same salary are included, use `RANK()`:

```
WITH SalaryRank AS (
    SELECT *, RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT *
FROM SalaryRank
WHERE rnk <= 5 AND salary > (SELECT AVG(salary) FROM employees);
```

## **Why the Rank approach is better:**

- **Handles salary ties properly** — If multiple employees have the same salary, they are included.
- **Ensures correct ranking** — The ranking is applied first, and the filtering happens afterward.

**16. Write a program using Stream API to sort list of string using length.
Ascending Order (Shortest to Longest)**

```jsx
import java.util.Arrays;
import java.util.List;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "kiwi", "grapes", "cherry");
        List<String> sortedWords = words.stream()
                .sorted(Comparator.comparingInt(String::length))
                .collect(Collectors.toList());
        System.out.println(sortedWords);
    }
}
```

**Output:**

`[kiwi, apple, grapes, cherry, banana]`

**Descending Order (Longest to Shortest)**

```jsx
import java.util.Arrays;
import java.util.List;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "kiwi", "grapes", "cherry");
        List<String> sortedWordsDesc = words.stream()
                .sorted(Comparator.comparingInt(String::length).reversed())
                .collect(Collectors.toList());
        System.out.println(sortedWordsDesc);
    }
}
```

**Output:**

`[banana, grapes, cherry, apple, kiwi]`

# **Oracle Java Developer Interview**

## **1. How static works in Inheritance?**

In Java, `static` members (methods and variables) have special behavior in inheritance.

Here’s how they work:

## **1. Static Variables in Inheritance**

- Static variables belong to the **class**, not to an instance.
- They are inherited by subclasses but **not overridden**. Instead, they are **hidden** if redeclared.
- Changing a static variable affects all instances of the class.

```
class Parent {
    static String message = "Hello from Parent";
}
class Child extends Parent {
    static String message = "Hello from Child"; // Hides Parent's message
}
public class Main {
    public static void main(String[] args) {
        System.out.println(Parent.message); // Output: Hello from Parent
        System.out.println(Child.message);  // Output: Hello from Child
    }
}
```

- **No method overriding for static variables.** Even though `Child` defines `message`, it's **hiding**, not overriding.

## **2. Static Methods in Inheritance**

- Static methods **are inherited** but **not overridden** (instead, they are hidden).
- Method calls are resolved **at compile-time** using the reference type, not at runtime.

```
class Parent {
    static void show() {
        System.out.println("Parent's static method");
    }
}
class Child extends Parent {
    static void show() {
        System.out.println("Child's static method");
    }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        p.show(); // Output: Parent's static method (Not Child's)
    }
}
```

- Even though `p` refers to a `Child` instance, the method call is resolved **statically** at compile-time using `Parent` type.

## **3. Static Methods and `super`**

- You **cannot** use `super` to call a static method because it belongs to the class, not an instance.
- However, you can explicitly call the parent’s static method using the class name.

```
class Parent {
    static void display() {
        System.out.println("Parent's static method");
    }
}
class Child extends Parent {
    static void display() {
        System.out.println("Child's static method");
    }
    void test() {
        Parent.display(); // Calls Parent's static method
    }
}
```

## **4. Static Blocks in Inheritance**

- Static blocks in parent and child classes execute in **order of inheritance** (parent first, then child).
- Static blocks execute **only once** when the class is loaded.

```
class Parent {
    static { System.out.println("Parent's static block"); }
}
class Child extends Parent {
    static { System.out.println("Child's static block"); }
}
public class Main {
    public static void main(String[] args) {
        Child obj1 = new Child();
        Child obj2 = new Child();
    }
}
```

**Output:**

```
Parent's static block
Child's static block
```

- Static blocks execute **once per class** regardless of how many objects are created.

**2. What are the differences between Call by Value vs Call by Reference?**

![](https://d2m1rbbhrnz727.archive.ph/Ft8sy/332a32a03deaec0638007a68e77fc2b447831495.webp)

## **3. Can we change the scope of an overridden method?**

Yes, we can change the scope (access modifier) of an overridden method, but only to a wider (more permissive) scope. We cannot reduce the visibility.

## **Rules for Changing Access Modifiers in Overridden Methods:**

1. **Private Methods**
- Private methods are not inherited by subclasses, so they **cannot be overridden**.
- If a subclass declares a method with the same name, it’s not an override, but a new method in the subclass.

```
class Parent {
    private void display() {
        System.out.println("Parent's private method");
    }
}

class Child extends Parent {
    private void display() { // Not an override, just a new method
        System.out.println("Child's private method");
    }
}
```

**2. Default (Package-Private) Methods**

- If the parent class method is `default` (no access modifier), it can be overridden with `protected` or `public` in the subclass.
- It **cannot** be overridden with a `private` method.

```
class Parent {
    void show() { // Default method
        System.out.println("Parent method");
    }
}

class Child extends Parent {
    public void show() { // Allowed: default → public
        System.out.println("Child method");
    }
}
```

**3. Protected Methods**

- If the parent class method is `protected`, it can be overridden with `public`, but **not** with `private` or `default` (package-private).
- The access level can only be widened (e.g., `protected` → `public`).

```
class Parent {
    protected void show() { // Protected method
        System.out.println("Parent method");
    }
}

class Child extends Parent {
    public void show() { // Allowed: protected → public
        System.out.println("Child method");
    }
}
```

**4. Public Methods**

- If the parent class method is `public`, it must remain `public` in the subclass.
- You **cannot** override a `public` method with a `protected` or `private` method.

```
class Parent {
     public void display() { // Public method
        System.out.println("Parent method");
    }
}
class Child extends Parent {
     private void display() { // ❌ Error: Cannot reduce visibility
         System.out.println("Child method");
     }
 }
```

## **4. Explain Thread lifecycle.**

The Thread Lifecycle in Java represents the different states a thread goes through during its execution.

There are six main states in a thread’s lifecycle, and each state transitions based on various events that occur during the thread’s execution.

## **Thread States in the Java Thread Lifecycle:**

![](https://d2m1rbbhrnz727.archive.ph/Ft8sy/50efe7a734464056894e78c9b65244104599217d.webp)

1. **New (Born)**
- A thread is in the **New** state when it is created but not yet started. At this point, the thread is just an object, and the `start()` method has not been called yet.

**Example:**

```
Thread t = new Thread();  // New state
```

**2. Runnable (Ready)**

- The thread is in the **Runnable** state once the `start()` method is invoked. In this state, the thread is ready to run, but it may not be running immediately because it's waiting for the CPU to allocate time.
- The thread is considered to be in a **“ready to run”** state.

**Example:**

```
t.start();  // Moves to Runnable state
```

**3. Blocked (Waiting for Resource)**

- A thread enters the **Blocked** state when it is waiting to acquire a lock (mutex) that another thread holds.
- This occurs when a thread tries to access a synchronized block or method and the resource is locked by another thread.

**Example:**

```
synchronized (object) {
    // Thread is blocked if another thread holds the lock
}
```

**4. Waiting (Not Runnable)**

- The **Waiting** state is when a thread is waiting indefinitely for another thread to perform a particular action. This happens when methods like `wait()`, `join()`, or other blocking calls are invoked.
- The thread remains in the **Waiting** state until the specified condition is met or the thread is interrupted.

**Example:**

```
thread1.join();  // thread1 will wait until thread1 completes
```

**5. Timed Waiting (Temporary Waiting)**

- A thread enters the **Timed Waiting** state when it’s waiting for a specific period of time. Methods like `sleep(long millis)` or `join(long millis)` cause a thread to enter this state.

**Example:**

```
thread.sleep(1000);  // Timed Waiting state for 1 second
```

**6. Terminated (Dead)**

- A thread enters the **Terminated** state when it has completed its execution or if it terminates due to an exception or interruption. The thread cannot be restarted after it enters the **Terminated** state.

**Example:**

```
// The thread reaches the end of its run() method and terminates
```

## **5. Can we write default and static methods in a functional interface? If yes, will lambda expressions be allowed to use with it?**

Yes, we can write both default and static methods in a functional interface.

However, a functional interface is defined as an interface that has exactly one abstract method. The presence of default or static methods does not break this rule because they are not considered abstract methods.

Lambda expressions are still allowed because they target only the single abstract method (SAM) in the interface.

## **Example Code:**

```
@FunctionalInterface
interface MyFunctionalInterface {
    void abstractMethod();  // Single Abstract Method (SAM)

    // Default method in a functional interface
    default void defaultMethod() {
        System.out.println("This is a default method in the functional interface.");
    }

    // Static method in a functional interface
    static void staticMethod() {
        System.out.println("This is a static method in the functional interface.");
    }
}
public class Main {
    public static void main(String[] args) {

        // Using Lambda Expression (Only for the single abstract method)
        MyFunctionalInterface obj = () -> System.out.println("Abstract method implemented using lambda.");

        obj.abstractMethod(); // Lambda expression calls the single abstract method
        obj.defaultMethod();  // Calling default method
        MyFunctionalInterface.staticMethod(); // Calling static method via interface name
    }
}
```

## **6. Can we use an `int` variable declared outside inside the `filter()` method in Stream API to check a condition?**

Yes, we can use an external `int` variable inside the `filter()` method of the Stream API, but there are certain restrictions.

## **Restrictions:**

1. **Effectively Final:**
- If the variable is assigned once and not modified afterward, it is effectively final, and you can use it inside `filter()`.
- A local variable can be used inside a lambda only if it is effectively final (i.e., assigned only once and never modified). If you attempt to modify it anywhere in the method, the compiler will throw an error.

**2. Lambda Expressions and Local Variables:**

- A lambda expression can only capture effectively final local variables because Java captures them by value, not by reference.
- This restriction ensures predictable behavior and prevents accidental modifications.

## **Example 1: Using an Effectively Final Variable (Allowed)**

```
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        int threshold = 10; // Effectively final
        List<Integer> numbers = List.of(5, 10, 15, 20, 25);
        List<Integer> filteredNumbers = numbers.stream()
                .filter(n -> n > threshold) // Using external variable
                .collect(Collectors.toList());
        System.out.println(filteredNumbers); // Output: [15, 20, 25]
    }
}
```

- Works fine because `threshold` is not modified and is considered effectively final**.**

## **Example 2: Trying to Modify the Variable (Compilation Error)**

```
public class Main {
    public static void main(String[] args) {
        int threshold = 10; // Not final
        List<Integer> numbers = List.of(5, 10, 15, 20, 25);
        List<Integer> filteredNumbers = numbers.stream()
                .filter(n -> {
                    threshold++; // Compilation error
                    return n > threshold;
                })
                .collect(Collectors.toList());
        System.out.println(filteredNumbers);
    }
}
```

- Fails to compile because `threshold` is modified inside the lambda expression, making it non-final.

## **Work Around for Mutable Variable:**

If you need a mutable variable, you can use:

- AtomicInteger for primitive `int` values.
- Wrapper classes like `Integer[]`.
- Final arrays (`final int[] threshold = {10}`) to store mutable primitives.

**Example: Using an AtomicInteger (Allowed)**

```
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        AtomicInteger threshold = new AtomicInteger(10); // Mutable
        List<Integer> numbers = List.of(5, 10, 15, 20, 25);
        List<Integer> filteredNumbers = numbers.stream()
                .filter(n -> n > threshold.get())
                .collect(Collectors.toList());
        System.out.println(filteredNumbers); // Output: [15, 20, 25]
        threshold.set(20); // Modifiable later
    }
}
```

- Works because `AtomicInteger` is mutable and supports safe modification.

## **7. Explain Object Cloning in Java.**

Object cloning is the process of creating an exact copy of an existing object in Java.

It allows you to duplicate an object without manually copying each field. Java provides the `clone()` method for this purpose, defined in the `Object` class.

## **Features:**

1. Must implement `Cloneable` or else `CloneNotSupportedException` is thrown.
2. `clone()` method in `Object` performs a shallow copy by default.
3. Deep cloning requires manually copying mutable fields.
4. Alternatives to `clone()`:
- Serialization/Deserialization (`ObjectInputStream` / `ObjectOutputStream`).
- Copy constructors.
- Using third-party libraries like Apache Commons `SerializationUtils.clone()`.

## **Cloning Working:**

## **1. Using the `clone()` Method:**

- The `clone()` method is available in the `Object` class.
- It creates a field-by-field copy of an object.
- The class must implement the `Cloneable` interface to allow cloning.

## **2. Types of Cloning:**

- **Shallow Cloning:** Copies only the references of non-primitive fields.
- **Deep Cloning:** Creates independent copies of all fields, including objects inside the cloned object.

## **Example of Shallow Cloning**

```
class Person implements Cloneable {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone(); // Performs shallow cloning
    }
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person("Alice", 25);
        Person p2 = (Person) p1.clone();
        System.out.println(p1.name + " - " + p1.age); // Alice - 25
        System.out.println(p2.name + " - " + p2.age); // Alice - 25
    }
}
```

- Works fine because it only contains primitive and immutable fields.

## **Example of Deep Cloning**

```
class Address {
    String city;

    Address(String city) {
        this.city = city;
    }
}

class Person implements Cloneable {
    String name;
    int age;
    Address address; // Reference type field
    Person(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        Person cloned = (Person) super.clone(); // Shallow copy
        cloned.address = new Address(this.address.city); // Deep copy of address
        return cloned;
    }
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person("Alice", 25, new Address("New York"));
        Person p2 = (Person) p1.clone();
        p2.address.city = "Los Angeles"; // Change city in cloned object
        System.out.println(p1.address.city); // New York (Original remains unchanged)
        System.out.println(p2.address.city); // Los Angeles (Clone modified)
    }
}
```

- Works correctly as `Address` is cloned separately, preventing unwanted modifications.

## **8. *What are the rules for method overriding in Java?***

Method overriding in Java is a fundamental concept, and there are specific rules that govern it. Let me break them down for you.

1. **Same Method Signature**:
- The method in the subclass must have the same method signature (i.e., method name, return type, and parameters) as the method in the superclass.
- This ensures the subclass method is correctly overriding the superclass method.

```
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    // Overriding the method
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}
```

**2. Inheritance**:

- The method in the subclass must inherit the method from the superclass.
- For example, if a method is defined in the superclass, the subclass needs to inherit it to override it.

**3. Access Modifier**:

- The access level of the overriding method in the subclass **cannot be more restrictive** than the superclass method.
- If the superclass method is `public`, the subclass method must be `public`. If it’s `protected`, it can be `protected` or `public`, but not `private`.

```
class Animal {
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {  // Same or less restrictive access
        System.out.println("Dog barks");
    }
}
```

**4. Return Type**:

- The return type of the overridden method must be the same or a subtype (covariant return type) of the return type of the superclass method.
- For example, if the superclass method returns `Object`, the subclass method can return `String` (which is a subclass of `Object`).

```
class Animal {
    Object getType() {
        return new Object();
    }
}

class Dog extends Animal {
    @Override
    String getType() {  // Covariant return type
        return "Dog";
    }
}
```

**5. Exceptions**:

- The overridden method can throw the **same or fewer** exceptions as the superclass method.
- If the superclass method throws a checked exception, the subclass method can throw that exception or a subclass of it, but not a new exception that the superclass method doesn’t declare.

```
class Animal {
    void makeSound() throws IOException {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() throws IOException {  // Same exception
        System.out.println("Dog barks");
    }
}
```

**6. `@Override` Annotation**:

- The `@Override` annotation is not mandatory, but it’s good practice to use it.
- It helps the compiler verify that you're actually overriding a method from the superclass.
- If you mistakenly don’t match the signature, it will throw a compile-time error.

```
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override  // Helps avoid mistakes
    void makeSound() {
        System.out.println("Dog barks");
    }
}
```

**7. Static, Final, and Private Methods**:

- **Static methods** cannot be overridden; they can only be redeclared.
- **Final methods** cannot be overridden, as they’re meant to remain unchanged.
- **Private methods** cannot be overridden because they are not inherited.

```
class Animal {
    static void sleep() {
        System.out.println("Animal sleeps");
    }

    final void eat() {
        System.out.println("Animal eats");
    }

    private void drink() {
        System.out.println("Animal drinks");
    }
}

class Dog extends Animal {
    @Override
    static void sleep() {  // This is NOT method overriding
        System.out.println("Dog sleeps");
    }

    // Cannot override final method eat()
    // Cannot override private method drink()
}
```

**9. *What are the differences between `map()` vs `reduce()`?***

![](https://d2m1rbbhrnz727.archive.ph/Ft8sy/3fb3f13ab58ef8e806ca0fdea2ed9d40429ee977.webp)

## **10. Explain working of Optional.of() method?**

The `Optional.of()` method in Java, introduced in Java 8, is used to create an `Optional` instance that contains a non-null value.

It helps prevent `NullPointerException` by ensuring that the value is present.

## **Working:**

1. **Creates an Optional Object**:
- `Optional.of(value)` wraps a non-null value inside an `Optional`.
- If `value` is `null`, it throws a `java.lang.NullPointerException`.

**2. Ensures Non-Null Values**:

- It is useful when you are 100% sure that the value is never null.
- If there’s a chance of `null`, use `Optional.ofNullable()` instead.

## **Example: Valid Case — Storing a Non-Null Value**

```
Optional<String> name = Optional.of("Shivam");
System.out.println(name.get());  // Output: Shivam
```

Since `"Shivam"` is non-null, `Optional.of()` correctly wraps the value.

## **Example: Invalid Case — Passing a Null Value**

```
Optional<String> empty = Optional.of(null);  // Throws java.lang.NullPointerException
```

Since `null` is passed, it throws a `java.lang.NullPointerException` at runtime.

## **Comparison with `Optional.ofNullable()`**

![](https://d2m1rbbhrnz727.archive.ph/Ft8sy/c584a03200b23232252bb2662f7685c7a01ba7f5.webp)

```
Optional<String> safeValue = Optional.ofNullable(null);
System.out.println(safeValue.orElse("Default Value"));  // Output: Default Value
```

- `Optional.ofNullable(null)` returns an empty `Optional`, preventing exceptions.
- Instead of calling `get()`, which throws an exception if empty, use `orElse()` or `orElseGet()` to provide a fallback value.

## **11. Explain Lazy loading in Stream.**

Lazy loading in Java Streams means that elements are not processed immediately when a Stream is created. Instead, operations on the Stream are executed only when a terminal operation is invoked.

Java Streams use a pipeline execution model where intermediate operations build a sequence of transformations without performing them until a terminal operation is encountered.

This lazy nature allows Java to optimize performance by deferring computation until absolutely necessary.

## **Working**

In Java Streams, operations are categorized into **intermediate operations** and **terminal operations**:

1. **Intermediate Operations (Lazy):**
- These operations do not execute immediately. Instead, they return a new Stream that holds the transformation logic.
- Examples: `map()`, `filter()`, `sorted()`, `limit()`, `distinct()`.

**2. Terminal Operations (Triggers Execution):**

- These operations trigger the execution of all preceding intermediate operations.
- Examples: `collect()`, `forEach()`, `count()`, `reduce()`, `toArray()`.

> Some intermediate operations like limit() and findFirst() can short-circuit and stop execution before traversing the entire stream.
> 

## **Example:**

```
import java.util.List;
import java.util.stream.Stream;

public class LazyLoadingExample {
    public static void main(String[] args) {
        List<String> names = List.of("Aman", "Bobby", "Chandan", "Dinesh");
        Stream<String> stream = names.stream()
            .filter(name -> {
                System.out.println("Filtering: " + name);
                return name.startsWith("A") || name.startsWith("C");
            })
            .map(name -> {
                System.out.println("Mapping: " + name);
                return name.toUpperCase();
            });
        System.out.println("Stream defined, but no execution yet!");
        // Execution starts only when terminal operation is called
        stream.forEach(System.out::println);
    }
}
```

## **Output:**

```
Stream defined, but no execution yet!
Filtering: Aman
Mapping: Aman
AMAN
Filtering: Bobby
Filtering: Chandan
Mapping: Chandan
CHANDAN
Filtering: Dinesh
```

## **Breakdown:**

1. **No Execution Until a Terminal Operation is Called**
- The Stream is defined, but `"Filtering: ..."` and `"Mapping: ..."` messages do not appear immediately.
- Execution starts only when `forEach()` is called.

**2. Short-Circuiting in Action**

- `filter()` only processes elements as needed.
- `"Bobby"` is filtered out and not passed to `map()`, reducing unnecessary computation.

## **Advantages**

- **Performance Optimization:** Operations are only applied when necessary.
- **Memory Efficiency:** Streams process elements **on demand** rather than storing all transformed elements in memory.
- **Short-Circuiting:** Stream stops processing early when a condition is met (e.g., `findFirst()`, `limit()`).

## **Disadvantages**

- **Debugging Complexity:** Since execution is deferred, debugging intermediate operations is harder compared to traditional loops.
- **Potential Performance Overhead:** Excessive intermediate operations can slow down execution if not optimized properly.
- **Less Readability for Complex Pipelines:** Stream pipelines can be harder to understand than traditional loops, especially for developers unfamiliar with functional programming.

## **12. Explain Terminal Operations in Streams.**

In Java Streams, **terminal operations** are operations that trigger the actual processing of the stream and produce a result or a side-effect. These operations are what cause the **stream pipeline to execute**. Until a terminal operation is invoked, no processing happens, even if intermediate operations are defined.

## **Characteristics**

- **Triggers Execution:** They initiate the processing of the stream, which includes executing all intermediate operations.
- **Consumes the Stream:** A terminal operation consumes the stream, making it no longer usable after the operation is performed.
- **Produces a Result:** The result can be anything, such as a value, a collection, or a side effect.

## **Types**

Here are some common types of terminal operations in Java Streams:

1. **Collecting Results (`collect()`)**
- Collects the elements of the stream into a collection or other form.
- Example: Converting a stream to a list or a set.

```
List<String> names = Stream.of("Alice", "Bob", "Charlie")
    .filter(name -> name.startsWith("A"))
    .collect(Collectors.toList());  // Returns List with "Alice"
```

**2. Reducing Elements (`reduce()`)**

- Combines elements of the stream into a single result.
- Example: Summing the elements of a stream of integers.

```
int sum = Stream.of(1, 2, 3, 4, 5)
          .reduce(0, Integer::sum);  // Returns 15
```

**3. For Each (`forEach()`)**

- Iterates over the elements of the stream and performs an action for each element.
- Example: Printing each element.

```
Stream.of("Aman", "Bobby", "Chandan")
    .forEach(System.out::println);  // Prints each name
```

**4. Checking Conditions (`anyMatch()`, `allMatch()`, `noneMatch()`)**

- Checks whether any, all, or no elements of the stream satisfy a given condition.
- Example: Checking if any element is greater than 10.

```
boolean anyGreaterThan10 = Stream.of(5, 10, 15)
    .anyMatch(num -> num > 10);  // Returns true
```

**5. Counting Elements (`count()`)**

- Returns the number of elements in the stream.
- Example: Counting the number of elements.

```
long count = Stream.of(1, 2, 3, 4, 5)
              .count();  // Returns 5
```

**6. Finding Elements (`findFirst()`, `findAny()`)**

- Finds and returns the first or any element in the stream.
- Example: Finding the first element.

```
Optional<String> first = Stream.of("Aman", "Bobby", "Chandan")
    .findFirst();  //Returns "Aman"
```

**7. Summing (`sum()`)**

- Calculates the sum of the elements in the stream (for numeric streams).
- Example: Summing integers.

```
int sum = Stream.of(1, 2, 3, 4)
          .mapToInt(Integer::intValue)
          .sum();  // Returns 10
```

## **Behavior**

- **Eager Execution:** Once a terminal operation is invoked, the entire stream pipeline is executed, which includes all intermediate operations.
- **Single Execution:** A stream can only be consumed once. After invoking a terminal operation, the stream is considered closed and can no longer be used.

## **Example**

```
import java.util.Arrays;
import java.util.List;

public class TerminalOperationsExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Aman", "Bobby", "Chandan", "Dinesh");
        // Example 1: collect()
        List<String> filteredNames = names.stream()
            .filter(name -> name.startsWith("A"))
            .collect(Collectors.toList());  // Collects into a list
        System.out.println(filteredNames);  // Output: [Aman]
        // Example 2: forEach()
        names.stream().forEach(System.out::println);  // Output: Aman, Bobby, Chandan, Dinesh
        // Example 3: reduce()
        String combined = names.stream()
            .reduce("", (acc, name) -> acc + name + " ");  // Concatenates all names
        System.out.println(combined);  // Output: Aman Bobby Chandan Dinesh
    }
}
```

## **13. What are the use cases of FlatMap()?**

The `flatMap()` function in Java Streams is used to transform and flatten data structures.

It comes in handy when working with elements in a stream that are collections or even other streams themselves.

It allows you to take each element, apply a function that returns a new stream, and then flatten all those streams into a single stream.

Below are some of the key use cases of `flatMap():`

## **1. Flattening Nested Collections**

When working with a stream of collections (such as lists or sets), `flatMap()` can be used to **flatten** those collections into a single stream of elements.

**Example:**

```
List<List<String>> names = List.of(
    List.of("Alice", "Bob"),
    List.of("Charlie", "David"),
    List.of("Eve", "Frank")
);

names.stream()
    .flatMap(Collection::stream)
    .forEach(System.out::println);
```

**Output:**

```
Alice
Bob
Charlie
David
Eve
Frank
```

Here, `flatMap()` is flattening the `List<List<String>>` structure into a single stream of individual names.

## **2. Transforming Elements into Multiple Values**

You can use `flatMap()` to transform each element into multiple values. For example, splitting a word into its characters.

**Example:**

```
Stream<String> words = Stream.of("hello", "world");
words.flatMap(word -> Stream.of(word.split("")))
    .forEach(System.out::println);
```

**Output:**

```
h
e
l
l
o
w
o
r
l
d
```

Here, each word is split into its constituent characters, and `flatMap()` flattens them into a single stream of characters.

## **3. Converting a Stream of Optional Values**

When working with a stream of `Optional` values, `flatMap()` can help **extract values** from the `Optional` and flatten them into a single stream.

**Example:**

```
Stream<Optional<String>> options = Stream.of(Optional.of("A"), Optional.empty(), Optional.of("B"));
options.flatMap(Optional::stream)
    .forEach(System.out::println);
```

**Output:**

```
A
B
```

In this case, `flatMap()` unwraps each `Optional`, removing any empty `Optional` values and creating a stream of non-empty values.

## **4. Handling Streams of Streams**

If you have a stream of streams (e.g., `Stream<Stream<T>>`), you can use `flatMap()` to merge them into a single stream.

**Example:**

```
Stream<Stream<String>> streamOfStreams = Stream.of(
    Stream.of("a", "b"),
    Stream.of("c", "d"),
    Stream.of("e", "f")
);

streamOfStreams.flatMap(s -> s).forEach(System.out::println);
```

**Output:**

```
a
b
c
d
e
f
```

Here, `flatMap()` flattens the `Stream<Stream<String>>` into a single `Stream<String>`.

## **5. Combining Multiple Lists or Arrays into One**

`flatMap()` can also be used to merge multiple lists or arrays into a single stream.

**Example:**

```
List<String> list1 = List.of("apple", "banana");
List<String> list2 = List.of("cherry", "date");

Stream<List<String>> lists = Stream.of(list1, list2);
lists.flatMap(List::stream)
    .forEach(System.out::println);
```

**Output:**

```
apple
banana
cherry
date
```

In this case, `flatMap()` is used to merge multiple lists into one flat stream of values.

## **6. Dealing with Multiple Values from a Single Source**

Sometimes, a single source element produces multiple values. For instance, when working with text, you may want to break it down into words.

**Example:**

```
Stream<String> lines = Stream.of("Hello world", "Java programming");
lines.flatMap(line -> Stream.of(line.split(" ")))
    .forEach(System.out::println);
```

**Output:**

```
Hello
world
Java
programming
```

Each line is split into individual words, and `flatMap()` flattens the resulting arrays into a single stream of words.

## **7. Working with Nested Data Structures**

When you have nested data structures, like trees or graphs, where each node has a collection of child nodes, `flatMap()` can help process all nodes in a flattened manner.

**Example:**

```
class Person {
    String name;
    List<Person> children;

Person(String name, List<Person> children) {
        this.name = name;
        this.children = children;
    }
}

Person child1 = new Person("Child1", List.of());
Person child2 = new Person("Child2", List.of());
Person parent = new Person("Parent", List.of(child1, child2));

Stream<Person> familyTree = Stream.of(parent);
familyTree.flatMap(person -> Stream.concat(Stream.of(person), person.children.stream()))
    .forEach(person -> System.out.println(person.name));
```

**Output:**

```
Parent
Child1
Child2
```

Here, `flatMap()` is used to flatten the family tree structure, ensuring that all family members (parent and children) are processed in a single stream.

## **14. Explain Singleton design pattern.**

I’ve written below article on Singleton design pattern. I would recommend you to read this for clarity and understanding of Singleton Design pattern:

[**Is Your Code Lacking Leadership?See how Singleton brings clarity and control to your code.**medium.com](https://archive.ph/o/Ft8sy/https://medium.com/java-and-beyond/is-your-code-lacking-leadership-14215d3fc215)

## **15. Explain Factory design pattern.**

The Factory Design Pattern is a creational design pattern that provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.

It helps in the process of object creation by delegating the responsibility of creating objects to a specific factory class, rather than directly creating them in client code.

This pattern promotes loose coupling and enhances flexibility, as it abstracts the instantiation process.

## **Concepts:**

1. **Product Interface**: The interface or abstract class that defines the objects being created.
2. **Concrete Product**: The actual implementation or subclass of the product.
3. **Factory Interface**: The abstract factory that defines a method for creating products.
4. **Concrete Factory**: The class that implements the factory interface and creates concrete products.

## **Benefits:**

- **Loose Coupling**: The client code doesn’t need to know about the concrete classes it uses. It relies on the factory to provide objects.
- **Flexibility and Extensibility**: New products can be introduced without changing the client code, as long as the factory method is updated.
- **Centralized Object Creation**: Object creation is centralized in the factory, making it easier to maintain and modify.

## **Use Case:**

- When the object creation process is complex or involves multiple steps.
- When the system needs to be independent of how the objects are created, composed, and represented.
- When the system needs to allow for the addition of new types of products without altering existing code.

## **Example:**

Let’s say we have an application where we need to create different types of vehicles. Instead of creating instances directly in the client, we use a **Factory** to create different vehicle objects.

## **Step 1: Create a common interface for the product**

```
public interface Vehicle {
    void drive();
}
```

## **Step 2: Implement concrete products (concrete classes)**

```
public class Car implements Vehicle {
    @Override
    public void drive() {
        System.out.println("Driving a car");
    }
}
public class Bike implements Vehicle {
    @Override
    public void drive() {
        System.out.println("Riding a bike");
    }
}
```

## **Step 3: Create the Factory class that generates different types of vehicles**

```
public class VehicleFactory {
    public Vehicle getVehicle(String type) {
        if (type == null) {
            return null;
        }
        if (type.equalsIgnoreCase("Car")) {
            return new Car();
        } else if (type.equalsIgnoreCase("Bike")) {
            return new Bike();
        }
        return null;
    }
}
```

## **Step 4: Client code using the factory**

```
public class FactoryPatternDemo {
    public static void main(String[] args) {
        VehicleFactory vehicleFactory = new VehicleFactory();

        Vehicle vehicle1 = vehicleFactory.getVehicle("Car");
        vehicle1.drive();
        Vehicle vehicle2 = vehicleFactory.getVehicle("Bike");
        vehicle2.drive();
    }
}
```

## **Output:**

```
Driving a car
Riding a bike
```

## **Code Breakdown:**

1. **Product (Vehicle interface)**: Defines the `drive()` method that is implemented by the concrete products (`Car` and `Bike`).
2. **Concrete Products (Car and Bike)**: These classes implement the `Vehicle` interface and provide specific implementations for the `drive()` method.
3. **Factory (VehicleFactory)**: The factory class contains the logic to create instances of `Car` and `Bike`. The client uses the factory to obtain objects without worrying about their instantiation.
4. **Client Code**: The client code interacts with the factory and doesn’t need to know about the concrete classes.

## **Types:**

1. **Simple Factory**: A single method is used to create objects. It is not a formal design pattern but is commonly used. In the example above, the `VehicleFactory` acts as a simple factory.
2. **Factory Method Pattern**: Defines an interface for creating objects, but lets subclasses alter the type of objects that will be created. This allows for more flexibility in subclassing the factory.
3. **Abstract Factory Pattern**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**16. What are the differences between @Bean vs @Component in Spring Boot?**

![](https://d2m1rbbhrnz727.archive.ph/Ft8sy/f003a51969b138c695cddc0de22125b007e56af6.webp)

# **IBM Java Developer Interview — 2**

## **1. Describe the collision resolution mechanism in HashMap and How Java 8 improved it?**

A **collision** in a `HashMap` occurs when two different keys produce the same **bucket index** in the underlying array after applying hashing and modulo-based bucket assignment.

Java’s `HashMap` uses **chaining** as the primary collision resolution technique, meaning that multiple key-value pairs that map to the same bucket are stored within a **linked list**.

## **Collision Resolution Process (Pre-Java 8):**

1. The **`hashCode()`** of the key is computed, then **Java applies a bit-mixing function (`hash()`)** to improve hash distribution and reduce collisions.
2. The final bucket index is calculated using:**`(hash & (n - 1))`**, where `n` is the capacity of the internal array (always a power of 2).
3. If a **collision** occurs (i.e., multiple keys hash to the same index), Java stores these key-value pairs in a **linked list** at that bucket.
4. When retrieving a value, Java traverses the linked list to find the matching key.

This approach is **efficient for low collision rates**, but when multiple keys map to the same bucket, it degrades to **O(n) lookup time** in the worst-case scenario, especially if all entries end up in a single bucket.

## **Improvements in Java 8**

To mitigate performance issues caused by long linked lists in high-collision scenarios, Java 8 introduced **red-black trees** for better efficiency.

**1. Tree-based Collision Handling:**

- If the number of elements in a bucket exceeds a threshold (`TREEIFY_THRESHOLD = 8`), the linked list is **converted into a balanced red-black tree**.
- Searching in a red-black tree takes **O(log n)** time instead of **O(n)** in a linked list.

**However, treeification does NOT happen immediately when the threshold is exceeded.**

- If the total capacity of the `HashMap` is **less than 64**, Java **resizes the table instead of converting to a tree**.
- Treeification happens **only if the capacity is at least 64** (defined by `MIN_TREEIFY_CAPACITY`).

**2. Performance Optimization:**

- During insertion, Java **checks the type of bucket** (linked list or tree).
- If the bucket has **fewer than 8 elements**, it remains a linked list.
- If the number of elements exceeds **8 and the capacity is ≥ 64**, it converts into a **red-black tree** for faster lookups.

**3. Thresholds for Tree Conversion and Untreeing:**

- **`TREEIFY_THRESHOLD = 8`** → Converts a linked list to a red-black tree (if capacity ≥ 64).
- **`UNTREEIFY_THRESHOLD = 6`** → Converts back to a linked list when elements reduce.

**4. Ordering Optimization (Specific to Red-Black Trees):**

- Java 8 improved how **hash codes are used for tree balancing**, reducing unnecessary restructuring.
- These optimizations **do not change the core hashing algorithm** but ensure more balanced tree structures.

If you want to learn more about HashMaps, please go through the below article:

[**HashMap: Deep Dive and Interview QuestionsDive Into HashMaps with Interview Prep**medium.com](https://archive.ph/o/8Axv3/https://medium.com/coding-odyssey/hashmap-deep-dive-and-interview-questions-6cf251baf61a)

**2. What are the differences between == and .equals() ?**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/516de2b309c3a32d1643922496a31a5ae219897c.webp)

## **3. What is String interning and how does it affect comparisons?**

String interning is a process where Java stores a single instance of each unique string literal in a special memory area called the String Pool, which resides within the heap.

This allows **efficient memory usage** and **faster string comparisons** using `==`.

When a `String` is interned, Java ensures that all identical string values share the same memory reference in the String Pool.

## **String Interning for comparisons (`==` vs. `.equals()`)**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/634cc663e3f5145ee8d0ca5a85369df4874d7559.webp)

## **Example 1: String Literals (Automatically Interned)**

```
String s1 = "Hello";
String s2 = "Hello";

System.out.println(s1 == s2);      // true  (Same reference from String Pool)
System.out.println(s1.equals(s2)); // true  (Same content)
```

Both `"Hello"` literals are automatically stored in the String Pool, so `s1` and `s2` share the same memory reference.

## **Example 2: Using `new` Keyword (Not Interned by Default)**

```
String s1 = new String("Hello");
String s2 = new String("Hello");

System.out.println(s1 == s2);      // false (Different memory locations)
System.out.println(s1.equals(s2)); // true  (Same content)
```

Each `new String("Hello")` creates a separate object in the heap. Therefore, `s1` and `s2` have different references, but their content is the same.

## **Example 3: Manually Interning Strings**

```
String s1 = new String("Java");
String s2 = s1.intern(); // Moves to String Pool
String s3 = "Java";

System.out.println(s1 == s2); // false (s1 is still in heap)
System.out.println(s2 == s3); // true  (Both are in the String Pool)
```

- `s1` is a heap object.
- `s2 = s1.intern();` ensures that `s2` refers to the interned version in the String Pool.
- Since `s3` is also a string literal, it reuses the same reference as `s2`.

**4. What are the differences between String and StringBuffer?**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/321975e84008e1c2614fe9580029640673c6c0fa.webp)

## **5. Describe thread-safety in StringBuffer and how it’s thread safety compares to String and StringBuilder?**

`StringBuffer` is thread-safe because all its methods such as `append()`, `insert()`, and `delete()`are synchronized.

This means that multiple threads cannot modify a `StringBuffer` object simultaneously, preventing race conditions.

However, this synchronization comes with a performance cost, making `StringBuffer` slower than `StringBuilder` in single-threaded applications.

**Example:**

```
StringBuffer sb = new StringBuffer("Hello");

Thread t1 = new Thread(() -> sb.append(" World"));
Thread t2 = new Thread(() -> sb.append(" Java"));
t1.start();
t2.start();
```

Since the methods are synchronized, the modifications happen sequentially, preventing inconsistencies.

## **Thread-Safety in String:**

- `String` objects are immutable, meaning once created, they cannot be changed.
- Since multiple threads cannot modify the same `String` object, it is inherently thread-safe.

**Example**:

```
String s = "Hello";
s = s + " World";  // Creates a new object, old one remains unchanged
```

Even if multiple threads access `s`, there is **no risk of corruption** because a new object is created instead of modifying the existing one.

## **Thread-Safety in StringBuilder:**

- Unlike `StringBuffer`, `StringBuilder` does not synchronize its methods, making it faster but unsafe in multi-threaded environments.
- If multiple threads modify the same `StringBuilder` object, race conditions can occur.

**Example:**

```
StringBuilder sb = new StringBuilder("Hello");

Thread t1 = new Thread(() -> sb.append(" World"));
Thread t2 = new Thread(() -> sb.append(" Java"));
t1.start();
t2.start();
```

Here, since `StringBuilder` is not synchronized, both threads can modify the object simultaneously, leading to data corruption.

## **6. How String and StringBuffer handle memory differently?**

## **Memory Handling in `String` (Immutable):**

- `String` objects are immutable, meaning every modification creates a new object in memory.
- When a `String` is modified, a new copy is created in the heap, while the old one remains until garbage collection removes it.
- If a string is interned (`String.intern()`), it is stored in the String Pool, which was in PermGen before Java 7 and moved to the heap in Java 7 and later.

**Example:**

```
String s = "Hello";
s = s + " World";  // Creates a new "Hello World" object; "Hello" remains in memory until GC
```

Each modification creates a new object, increasing memory usage.

## **Memory Handling in `StringBuffer` (Mutable):**

- `StringBuffer` is mutable, meaning modifications happen in the same memory location without creating new objects.
- The underlying implementation uses a char array (`char[] value`) to store characters.
- If the buffer’s capacity is exceeded, a new, larger array is created, and characters are copied over.

**Example:**

```
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");  // Modifies existing object, no new object created
```

Unlike `String`, no unnecessary objects are created, making `StringBuffer` memory-efficient for frequent modifications.

## **7. What is Dependency Injection and what are it’s advantages?**

> This exact question was asked in JP Morgan interview as well. So, it’s an important question.
> 

Dependency Injection (DI) is a **technique** used in object-oriented programming to achieve **Inversion of Control (IoC)**.

It involves providing an object (called the *dependent object*) with its dependencies (other objects it depends on) from the outside, instead of the dependent object instantiating them itself.

This approach decouples the creation of objects from their behavior, making the code more modular, testable, and maintainable.

## **Dependency Injection Working**

At its core, DI involves:

- **Dependencies**: The objects or resources a class needs to function.
- **Injection**: The process of passing these dependencies to the dependent object.

DI can be implemented in three main ways:

1. **Constructor Injection**: Dependencies are passed to the object via its constructor.
2. **Setter Injection**: Dependencies are set through public setter methods.
3. **Interface Injection**: The dependency provides an injector method that the dependent class uses to receive its dependencies (less common).

## **Example:**

**Without DI:**

```
public class Service {
    private Repository repository = new Repository(); // Tight coupling
    public void performService() {
        repository.save();
    }
}
```

**With DI:**

```
public class Service {
    private Repository repository;

    public Service(Repository repository) { // Constructor Injection
        this.repository = repository;
    }
    public void performService() {
        repository.save();
    }
}
```

Here, the `Repository` object is passed from outside, making `Service` independent of its creation logic.

## **Advantages**

1. **Loose Coupling**:
- Classes are no longer responsible for creating their own dependencies, which makes the code more modular and easier to manage.

**2. Improved Testability**:

- Dependencies can be easily mocked or stubbed for unit testing, as they are passed from outside rather than being hardcoded inside the class.

**3. Easier Maintenance**:

- If a dependency changes (e.g., swapping a database implementation), you only need to update the dependency injection configuration, not the dependent class.

**4. Reusability**:

- Dependencies can be reused across different classes, promoting a more DRY (Don’t Repeat Yourself) codebase.

**5. Scalability**:

- Adding new functionality or dependencies becomes easier, as the code is modular and not tightly coupled.

**6. Adherence to SOLID Principles**:

- Promotes the **Single Responsibility Principle** by separating the creation of dependencies from the use of dependencies.
- Encourages the **Dependency Inversion Principle**, as classes depend on abstractions (interfaces) rather than concrete implementations.

**7. Configuration Flexibility**:

- DI allows dynamic injection of dependencies based on runtime configurations, making the code adaptable to different environments (e.g., development, production).

**8. Better Code Readability**:

- By delegating dependency management to a DI container or framework, the main code becomes cleaner and more focused on business logic.

**8. What are the differences between Constructor Injection vs Setter Injection?**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/8ae3eb408e529d584827e286bd396ed76284bc53.webp)

**9. What are the differences between @Autowired vs @Resource vs @Inject.**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/8c6f7986a356d9fd43c20b9ce3666cdf72fc15ea.webp)

## **10. Explain Qualifier annotation.**

> This question was also asked in Barclays Interview and Capgemini Interview. So, this is an important question.
> 

The `@Qualifier` annotation in Spring is used to resolve ambiguity when multiple beans of the same type are present in the application context.

It helps Spring to choose which bean to inject when there are multiple candidates for autowiring.

## **Purpose:**

It’s used along with `@Autowired` to specify which bean should be injected into a field or method when multiple beans of the same type exist.

## **Usage:**

You define the `@Qualifier` annotation with the name of the bean you want to inject. This ensures that the correct bean is injected instead of the default behavior, where Spring would throw an exception due to ambiguity.

**Example**:

```
@Component
public class Employee {
    private Address address;

    @Autowired
    public Employee(@Qualifier("homeAddress") Address address) {
        this.address = address;
    }
}
@Component("homeAddress")
public class HomeAddress implements Address {
    // Implementation
}
@Component("officeAddress")
public class OfficeAddress implements Address {
    // Implementation
}
```

## **When to Use:**

You would use `@Qualifier` when you have multiple beans of the same type (e.g., multiple `Address` beans) and need to specify which one to inject.

## **11. How to handle exception in Spring Boot application?**

Exception handling in a Spring Boot application can be managed in an organized way using several key approaches:

## **1. Using `@ControllerAdvice` and `@ExceptionHandler`**

`@ControllerAdvice` is used to define a global exception handler for the entire application, combined with `@ExceptionHandler` to specify how to handle particular exceptions.

**Example**:

```
@RestControllerAdvice
public class GlobalExceptionHandler {

@ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleResourceNotFound(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleGenericException(Exception ex) {
        return new ResponseEntity<>("An unexpected error occurred: " + ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```

Ensures exceptions are handled consistently and provides proper HTTP responses.

## **2. Using `@ResponseStatus` Annotation**

The `@ResponseStatus` annotation maps exceptions to specific HTTP status codes.

**Example:**

```
@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

When this exception is thrown, Spring automatically returns a `404 Not Found` status with the custom message.

## **3. Custom Error Response Structure**

For detailed error responses, create a custom error object containing fields like a timestamp, error code, and message.

**Example**:

```
public class ErrorResponse {
    private String timestamp;
    private String message;
    private String details;

    public ErrorResponse(String timestamp, String message, String details) {
        this.timestamp = timestamp;
        this.message = message;
        this.details = details;
    }
    // Getters and setters
}
```

This custom object can be returned from the global exception handler:

```
@ExceptionHandler(Exception.class)
public ResponseEntity<ErrorResponse> handleAllExceptions(Exception ex, WebRequest request) {
    ErrorResponse error = new ErrorResponse(
        LocalDateTime.now().toString(),
        ex.getMessage(),
        request.getDescription(false)
    );

return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
}
```

Helps provide structured and informative error responses.

## **4. Handling Validation Exceptions**

When using `@Valid` or `@Validated`, Spring automatically throws `MethodArgumentNotValidException` for validation failures. This can be handled as follows:

**Example**:

```
@ExceptionHandler(MethodArgumentNotValidException.class)
public ResponseEntity<String> handleValidationException(MethodArgumentNotValidException ex) {
    String errors = ex.getBindingResult().getAllErrors().stream()
                      .map(ObjectError::getDefaultMessage)
                      .collect(Collectors.joining(", "));
    return new ResponseEntity<>("Validation failed: " + errors, HttpStatus.BAD_REQUEST);
}
```

Extracts all validation error messages and returns them in a readable format.

## **5. Logging Exceptions**

All exceptions can be logged using SLF4J or a similar framework to ensure proper monitoring and debugging.

**Example**:

```
private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
@ExceptionHandler(Exception.class)
public ResponseEntity<String> handleGenericException(Exception ex) {
    logger.error("An error occurred: ", ex);
    return new ResponseEntity<>("Something went wrong", HttpStatus.INTERNAL_SERVER_ERROR);
}
```

Ensures errors are logged for troubleshooting and debugging.

## **6. Fallback for Unhandled Exceptions**

A fallback mechanism ensures unhandled exceptions are caught and returned with a generic error response.

**Example**:

```
@ExceptionHandler(Throwable.class)
public ResponseEntity<String> handleUnexpectedException(Throwable ex) {
    return new ResponseEntity<>("An unexpected error occurred", HttpStatus.INTERNAL_SERVER_ERROR);
}
```

Catches any unexpected exceptions, preventing server crashes and ensuring users receive meaningful responses.

## **12. How to implement logging mechanism in Spring Boot application?**

Spring Boot provides built-in support for logging using **SLF4J** with **Logback** as the default logging framework. Below are some other ways as well:

## **1. Using SLF4J with Logback (Default Logging Setup)**

Spring Boot automatically includes SLF4J (Simple Logging Facade for Java) with Logback as the default logging implementation. You can use it directly in your classes:

**Example**:

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class LoggingService {
    private static final Logger logger = LoggerFactory.getLogger(LoggingService.class);
    public void performTask() {
        logger.info("Task is being performed.");
        logger.debug("This is a debug message.");
        logger.error("An error occurred while performing the task.");
    }
}
```

**Ensures structured and consistent logging throughout the application.**

## **2. Configuring Log Levels in `application.properties` or `application.yml`**

Spring Boot allows configuring log levels for different packages/classes via properties or YAML files.

**Example (`application.properties`)**

```
logging.level.root=INFO
logging.level.com.example=DEBUG
logging.level.org.springframework.web=ERROR
```

**Example (`application.yml`)**

```
logging:
  level:
    root: INFO
    com.example: DEBUG
    org.springframework.web: ERROR
```

**Helps control the verbosity of logs and reduces unnecessary noise.**

## **3. Custom Log Format with Logback Configuration**

To define a custom log format, create a `logback-spring.xml` file in `src/main/resources/`.

**Example (`logback-spring.xml`)**

```
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/application.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/application-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>7</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} - %logger{36} - [%thread] - %-5level - %msg%n</pattern>
        </encoder>
    </appender>

<logger name="com.example" level="DEBUG" />
    <root level="INFO">
        <appender-ref ref="FILE"/>
    </root>
</configuration>
```

**Enables logging to a file with automatic log rotation.**

## **4. Writing Logs to a File**

Spring Boot can write logs to a file by configuring `application.properties`:

```
logging.file.name=logs/app.log
logging.file.path=logs
```

**Ensures logs are saved persistently for future debugging and audits.**

## **5. Using `@Slf4j` from Lombok (Simpler Logging)**

Lombok provides the `@Slf4j` annotation to avoid manually declaring the logger instance.

## **Example:**

```
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class LoggingService {
    public void performTask() {
        log.info("Task is being performed.");
        log.debug("Debug message.");
        log.error("Error occurred.");
    }
}
```

**Reduces boilerplate code and simplifies logging setup.**

## **6. Logging HTTP Requests and Responses with Spring Boot’s `CommonsRequestLoggingFilter`**

To log incoming HTTP requests and outgoing responses, use `CommonsRequestLoggingFilter`.

**Example (`@Configuration`)**

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.filter.CommonsRequestLoggingFilter;

@Configuration
public class RequestLoggingConfig {
    @Bean
    public CommonsRequestLoggingFilter logFilter() {
        CommonsRequestLoggingFilter filter = new CommonsRequestLoggingFilter();
        filter.setIncludeQueryString(true);
        filter.setIncludePayload(true);
        filter.setMaxPayloadLength(10000);
        filter.setIncludeHeaders(true);
        filter.setAfterMessagePrefix("REQUEST DATA: ");
        return filter;
    }
}
```

**Provides detailed request logging, useful for debugging API calls.**

## **7. Using Log Aggregation and Monitoring Tools**

For large-scale applications, logs can be collected and monitored using:

- ELK Stack (Elasticsearch, Logstash, Kibana)
- Graylog
- Splunk
- AWS CloudWatch Logs

**Enables centralized log management and real-time monitoring.**

## **13. What are the differences between REST vs SOAP? When to choose one over another?**

![](https://d7k25cvbjmwslv.archive.ph/8Axv3/107f2aca7063b2a73309f5e8a1ebccfcb3f98fab.webp)

## **When to Choose REST?**

- Microservices, mobile applications, IoT, and web applications.
- Public APIs (e.g., Google Maps, GitHub).
- When you need lightweight communication with minimal overhead.
- Scenarios requiring high performance and scalability.

## **When to Choose SOAP?**

- Enterprise applications that require high security and transactional support (e.g., banking, healthcare, insurance).
- When ACID-compliant transactions are needed (e.g., financial operations).
- When using legacy systems that already rely on SOAP-based services.
- Environments requiring protocol flexibility (not limited to HTTP).

## **14. What are the roles of HTTP methods in RESTful APIs?**

Below are the HTTP methods used in RESTful APIs:

## **1. GET — Retrieve a Resource**

Fetches data without modifying it.**Example:** Fetch all users.

```
@RestController
@RequestMapping("/users")
public class UserController {

@GetMapping
    public List<String> getUsers() {
        return List.of("Alice", "Bob", "Charlie");
    }
}
```

**Request:** `GET /users`**Response:** `["Alice", "Bob", "Charlie"]`

## **2. POST — Create a New Resource**

Adds a new resource to the system.**Example:** Add a new user.

```
@RestController
@RequestMapping("/users")
public class UserController {

@PostMapping
    public String addUser(@RequestBody String user) {
        return "User " + user + " added successfully!";
    }
}
```

**Request:** `POST /users` with body `"David"`**Response:** `"User David added successfully!"`

## **3. PUT — Update/Replace an Existing Resource**

Completely replaces a resource.**Example:** Update a user’s name.

```
@RestController
@RequestMapping("/users")
public class UserController {

@PutMapping("/{id}")
    public String updateUser(@PathVariable int id, @RequestBody String user) {
        return "User ID " + id + " updated to " + user;
    }
}
```

**Request:** `PUT /users/1` with body `"Daniel"`**Response:** `"User ID 1 updated to Daniel"`

## **4. PATCH — Partially Update a Resource**

Updates only specific fields of a resource.**Example:** Update a user’s email.

```
@RestController
@RequestMapping("/users")
public class UserController {

@PatchMapping("/{id}")
    public String updateEmail(@PathVariable int id, @RequestBody String email) {
        return "User ID " + id + " email updated to " + email;
    }
}
```

**Request:** `PATCH /users/1` with body `"daniel@email.com"`**Response:** `"User ID 1 email updated to daniel@email.com"`

## **5. DELETE — Remove a Resource**

Deletes a resource.**Example:** Delete a user by ID.

```
@RestController
@RequestMapping("/users")
public class UserController {

@DeleteMapping("/{id}")
    public String deleteUser(@PathVariable int id) {
        return "User ID " + id + " deleted successfully!";
    }
}
```

**Request:** `DELETE /users/1`**Response:** `"User ID 1 deleted successfully!"`

## **6. HEAD — Retrieve Headers Only**

Gets metadata without the actual data.**Example:** Check if a user exists.

```
@RestController
@RequestMapping("/users")
public class UserController {

@HeadMapping("/{id}")
    public ResponseEntity<Void> checkUser(@PathVariable int id) {
        return ResponseEntity.ok().build();
    }
}
```

**Request:** `HEAD /users/1`**Response:** Status `200 OK` with no body

## **7. OPTIONS — Get Allowed HTTP Methods**

Determines what HTTP methods are supported.**Example:** Get allowed methods for `/users`.

```
@RestController
@RequestMapping("/users")
public class UserController {

@RequestMapping(value = "/{id}", method = RequestMethod.OPTIONS)
    public ResponseEntity<Void> options() {
        return ResponseEntity.ok()
                .allow(HttpMethod.GET, HttpMethod.POST, HttpMethod.PUT, HttpMethod.PATCH, HttpMethod.DELETE)
                .build();
    }
}
```

**Request:** `OPTIONS /users/1`**Response:** Headers with allowed methods:

```
Allow: GET, POST, PUT, PATCH, DELETE
```

## **15. Explain statelessness in RESTful APIs.**

In RESTful APIs, statelessness means that each client request must be self-contained, carrying all the necessary information for processing.

The server does not store client-specific session data between requests, making each request independent.

This adheres to the REST architectural constraints as defined by **Roy Fielding**.

## **Characteristics:**

1. **No Session State on Server** — Each request is independent, and the server does not remember past interactions. There is no reliance on in-memory session storage or server-side session persistence (e.g., HTTP sessions in Java Servlets).
2. **Scalability** — Stateless APIs enable horizontal scaling, allowing load balancers to distribute requests across multiple servers without worrying about session consistency.
3. **Reliability & Fault Tolerance** — Since no session data is stored, failures on one server do not affect other instances. Requests can be routed to healthy servers seamlessly.
4. **Cacheability** — Stateless APIs can be cached efficiently using cache-control mechanisms like `ETag`, `Last-Modified`, and `Cache-Control` headers, improving performance.

## **Stateful vs. Stateless API Calls**

## **Stateful API (Bad Example — Server stores session data)**

**Problem:** The server **stores user session data**, violating REST principles. If multiple servers are used, session data won’t be shared, leading to inconsistent user experiences.

```
// Server-side session storage (violates REST statelessness)
Map<String, String> userSessions = new ConcurrentHashMap<>();

@PostMapping("/login")
public String login(@RequestBody User user) {
    String sessionId = UUID.randomUUID().toString();
    userSessions.put(sessionId, user.getUsername()); // Stores session (not RESTful)
    return sessionId; // Returns session ID to client
}
@GetMapping("/profile")
public String getProfile(@RequestHeader("Session-Id") String sessionId) {
    if (userSessions.containsKey(sessionId)) {
        return "Profile of " + userSessions.get(sessionId);
    }
    return "Unauthorized"; // Request fails if session does not exist
}
```

## **Stateless API (Good Example — Client sends credentials every request)**

**Fix:** The client must send authentication credentials with **every request**. No session is stored on the server.

```
@RestController
@RequestMapping("/users")
public class UserController {

@GetMapping("/profile")
    public ResponseEntity<String> getProfile(@RequestHeader("Authorization") String token) {
        if (validateToken(token)) { // Stateless authentication
            String username = extractUsernameFromToken(token);
            return ResponseEntity.ok("Profile of " + username);
        }
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Unauthorized");
    }
}
```

## **Benefits:**

- **Better Scalability** — No session data allows easy **horizontal scaling**.
- **Simpler Architecture** — No need for session management, making implementation straightforward.
- **More Reliable & Fault Tolerant** — Requests can be handled by any available server without session loss.
- **Faster Performance** — Stateless APIs can be **cached efficiently**, reducing server load.

## **16. How to secure REST APIs?**

Below are some of the best practices to secure your API:

## **1. Use HTTPS (SSL/TLS)**

- **Always use HTTPS** instead of HTTP to encrypt data in transit.
- Prevents **Man-in-the-Middle (MITM) attacks** and **eavesdropping**.
- Enforce **HSTS (HTTP Strict Transport Security)** to ensure all requests use HTTPS.

**Implementation in Spring Boot** (Redirect HTTP to HTTPS)

```
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.requiresChannel(channel -> channel.anyRequest().requiresSecure());
    return http.build();
}
```

- Ensures **all traffic** is forced over HTTPS.

## **2. Implement Authentication & Authorization**

- **Use JWT (JSON Web Token)** for stateless authentication.
- **OAuth 2.0 or OpenID Connect** for secure third-party authentication.
- **API Keys** for simple authentication but avoid using them for sensitive data.

**Bad Example (Basic Authentication — Insecure)**

```
@RequestMapping("/profile")
public ResponseEntity<String> getProfile(@RequestHeader("Authorization") String credentials) {
    if (!isValid(credentials)) {
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Unauthorized");
    }
    return ResponseEntity.ok("User Profile");
}
```

Basic Authentication sends credentials in every request, which can be intercepted.

**Good Example (JWT Authentication — Secure)**

```
@RequestMapping("/profile")
public ResponseEntity<String> getProfile(@RequestHeader("Authorization") String token) {
    if (validateToken(token)) {
        String username = extractUsernameFromToken(token);
        return ResponseEntity.ok("Profile of " + username);
    }
    return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Unauthorized");
}
```

- Uses JWT, which is **stateless and secure**.
- No need to store session data on the server.

## **3. Validate & Sanitize Input**

- **Prevent SQL Injection** — Use prepared statements instead of string concatenation.
- **Validate all inputs** — Use frameworks like Hibernate Validator in Java.
- **Escape special characters** — Avoid XSS (Cross-Site Scripting) attacks.

**Bad Example (Vulnerable to SQL Injection)**

```
String query = "SELECT * FROM users WHERE username = '" + userInput + "'";
```

**Good Example (Prepared Statement)**

```
String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, userInput);
```

- Prevents SQL Injection attacks**.**

**Spring Boot Input Validation**

```
public class UserDTO {
    @NotBlank
    @Size(min = 3, max = 20)
    private String username;

    @Email
    private String email;
}
```

- Prevents malicious input before processing.

## **4. Use Rate Limiting & Throttling**

- **Prevent DDoS attacks** — Limit the number of API requests per user/IP.
- **Use API Gateway (like AWS API Gateway, Nginx, or Kong)** for throttling.
- Implement exponential backoff for failed requests.

**Spring Boot Rate Limiting using Bucket4j**

```
@RateLimiter(name = "default")
@GetMapping("/data")
public String getData() {
    return "Limited API response";
}
```

- Protects against brute force attacks and abuse.

## **5. Secure API Endpoints with Roles & Scopes**

- Implement **RBAC (Role-Based Access Control)**.
- Use **OAuth 2.0 scopes** to define permissions.

**Example (Restricting Access Based on Role)**

```
@PreAuthorize("hasRole('ADMIN')")
@GetMapping("/admin/dashboard")
public String getAdminDashboard() {
    return "Admin Dashboard";
}
```

- Only ADMIN users can access this endpoint.

**Fine-grained Authorization with Scopes**

```
@PreAuthorize("hasAuthority('SCOPE_read:user')")
@GetMapping("/user/details")
public String getUserDetails() {
    return "User Details";
}
```

- Ensures specific API actions are restricted based on user roles.

## **6. Hide Sensitive Data & Avoid Leaks**

- Never expose API keys, tokens, or credentials in URLs.
- Use environment variables instead of hardcoding secrets.

**Bad Example (API Key in URL — Insecure)**

```
GET /users?api_key=12345
```

**Good Example (API Key in Header)**

```
GET /users
Authorization: Bearer <JWT_TOKEN>
```

- Hides sensitive data from logs & browser history.

**Spring Boot Secure Config Handling**

```
@Value("${api.secret.key}")
private String apiKey;
```

- Uses environment variables, avoiding hardcoded secrets.

## **7. Enable Logging & Monitoring**

- Use centralized logging (ELK Stack, Splunk, or AWS CloudWatch).
- Detect unusual activity (e.g., failed login attempts).
- Implement Intrusion Detection Systems (IDS).

**Example (Spring Boot Logging)**

```
private static final Logger logger = LoggerFactory.getLogger(MyController.class);

@GetMapping("/secure-data")
public ResponseEntity<String> getSecureData() {
    logger.info("Accessing secure data...");
    return ResponseEntity.ok("Secure Data");
}
```

- Helps with debugging and security audits.

**Enable Audit Logging**

```
@Bean
public AuditorAware<String> auditorProvider() {
    return () -> Optional.ofNullable(SecurityContextHolder.getContext().getAuthentication().getName());
}
```

- Tracks who accessed what and when.

## **17. Explain HATEOAS and its role in REST API?**

HATEOAS (Hypermedia as the Engine of Application State) is a key constraint of RESTful APIs, where API responses include hyperlinks (hypermedia) that dynamically guide clients on available actions.

This means that instead of hardcoding API endpoints in the client, the client discovers actions through the API response. This makes the system more flexible, loosely coupled, and self-descriptive.

HATEOAS was introduced as part of REST constraints by **Roy Fielding** in his dissertation.

## **Role of HATEOAS in REST API**

1. **Improves API Discoverability** — Clients dynamically navigate through resources based on hypermedia.
2. **Reduces Hardcoding of URLs** — Changes in endpoints don’t break clients, as links are provided in responses.
3. **Enhances Scalability & Flexibility** — The API can evolve without requiring constant client-side updates.
4. **Follows REST Principles** — Maintains a stateless architecture and ensures self-descriptive messages, reducing API documentation dependency.

## **Example: HATEOAS in REST API**

Let’s say we have a REST API that fetches user details.

## **Without HATEOAS (Basic API Response)**

```
{
    "id": 101,
    "name": "Shivam Srivastava",
    "email": "shivam.srivastava@example.com"
}
```

The client does not know what actions are available next.

## **With HATEOAS (Hypermedia-Enabled Response)**

```
{
    "id": 101,
    "name": "Shivam Srivastava",
    "email": "shivam.srivastava@example.com",
    "_links": {
        "self": {
            "href": "http://api.example.com/users/101"
        },
        "update": {
            "href": "http://api.example.com/users/101",
            "method": "PUT"
        },
        "delete": {
            "href": "http://api.example.com/users/101",
            "method": "DELETE"
        }
    }
}
```

Now, the client knows what actions (update, delete) are possible without hardcoding URLs.

## **Spring Boot Implementation of HATEOAS**

Spring Boot provides **Spring HATEOAS**, which allows adding hypermedia links dynamically to responses.

## **Controller Implementation:**

```
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;
    @GetMapping("/{id}")
    public EntityModel<User> getUser(@PathVariable Long id) {
        User user = userService.getUserById(id);
        EntityModel<User> resource = EntityModel.of(user);
        resource.add(WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(UserController.class).getUser(id)).withSelfRel());
        resource.add(WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(UserController.class).updateUser(id, user)).withRel("update"));
        resource.add(WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(UserController.class).deleteUser(id)).withRel("delete"));
        return resource;
    }
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        return userService.updateUser(id, user);
    }
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

## **18. Explain Joins in SQL?**

I would recommend you to go through the below article to learn about Joins in SQL:

[**SQL Joins : Deep Dive with Interview QuestionsA Deep Dive into Joins with Queries and Questions**medium.com](https://archive.ph/o/8Axv3/https://medium.com/coding-odyssey/sql-joins-deep-dive-with-interview-questions-b0d64a5670a8)

**19. Write a program to sort Employees based on Name and Age using Stream API.**

```jsx
import java.util.*;
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
public class EmployeeSorter {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Amit", 30),
            new Employee("Priya", 25),
            new Employee("Amit", 22),
            new Employee("Rahul", 35),
            new Employee("Suresh", 28),
            new Employee("Priya", 26),
            new Employee("Anjali", 24)
        );
        // Sorting employees by name (A-Z), then by age (ascending)
        List<Employee> sortedEmployees = employees.stream()
            .sorted(Comparator.comparing(Employee::getName).thenComparing(Employee::getAge))
            .collect(Collectors.toList());
        // Print sorted employees
        sortedEmployees.forEach(System.out::println);
    }
}
```

**Output:**

```jsx
Employee{name='Amit', age=22}
Employee{name='Amit', age=30}
Employee{name='Anjali', age=24}
Employee{name='Priya', age=25}
Employee{name='Priya', age=26}
Employee{name='Rahul', age=35}
Employee{name='Suresh', age=28}
```

# **IBM Java Developer Interview — 1**

## **1. What is aggregation?**

**Aggregation** is a relationship between two classes where one class contains a reference to another class, but both can exist independently.

It represents a **“Has-A” relationship** with weak ownership.

- It is a form of **association**.
- The contained object **can exist independently** of the container.
- It is implemented using **instance variables** in Java.

## **Example:**

```
class Address {
    String city, state, country;

    Address(String city, String state, String country) {
        this.city = city;
        this.state = state;
        this.country = country;
    }
}
class Employee {
    String name;
    int id;
    Address address; // Aggregation
    Employee(String name, int id, Address address) {
        this.name = name;
        this.id = id;
        this.address = address;
    }
    void display() {
        System.out.println(name + " " + id);
        System.out.println(address.city + ", " + address.state + ", " + address.country);
    }
}
public class AggregationExample {
    public static void main(String[] args) {
        Address addr = new Address("Varanasi", "UP", "India");
        Employee emp = new Employee("Shivam", 101, addr);
        emp.display();
    }
}
```

## **Output:**

```
Shivam 101
Varanasi, UP, India
```

## **Why Use Aggregation?**

- **Code Reusability**: The `Address` class can be used in other classes (e.g., `Company` or `Customer`).
- **Maintainability**: Changes to `Address` don’t require modifications in `Employee`.

## **Difference Between Aggregation and Composition:**

![](https://dfhqskic79jp5c.archive.ph/cwO7L/4f754b26a8c349d3effcdf7da92fd3707792c773.webp)

Aggregation is useful when one object logically **belongs to another** but is **not strictly dependent** on its existence.

## **2. How heap memory is divided in Java?**

In Java, **heap memory** is where objects are stored at runtime. It is divided into different regions to optimize **garbage collection (GC) and memory management**.

## **Main Divisions of Heap Memory:**

1. **Young Generation (Young Gen):**

a) Stores newly created objects.

b) Further divided into:

- **Eden Space** → Most new objects are allocated here.
- **Survivor Spaces (S0 and S1)** → Objects that survive a minor GC are moved between these two spaces.

**c) Garbage Collection:**

- Uses **Minor GC**, which is fast and frequent.
- Short-lived objects are quickly removed.

**2. Old Generation (Old Gen) / Tenured Generation:**

a) Stores long-lived objects that have survived multiple Minor GCs.

b) When an object gets old (crosses a threshold), it is moved here.

**c) Garbage Collection:**

- Uses **Major GC (Full GC)**, which is slower and can cause application pauses.

**3. Metaspace (Introduced in Java 8, replaced PermGen)**

a) Stores **class metadata, method information, and runtime constant pool**.

b) Unlike **PermGen (pre-Java 8),** Metaspace is allocated in **native memory** and grows dynamically.

## **Diagram of Java Heap Memory**

```
|---------------- Heap Memory ----------------|
|          Young Generation (Eden + S0 + S1) |
|   |---- Eden ----|---- S0 ----|---- S1 ----| |
|--------------------------------------------|
|           Old Generation (Tenured)         |
|--------------------------------------------|
|                 Metaspace                  |
|--------------------------------------------|
```

## **Garbage Collection in Heap**

- **Minor GC** → Cleans **Young Gen** (Fast & frequent).
- **Major GC (Full GC)** → Cleans **Old Gen** (Slower, can cause pauses).
- **Metaspace GC** → Cleans **class metadata**.

## **Heap Memory JVM Parameters for Tuning**

- **`Xms<size>`** → Initial heap size (e.g., `Xms512m`).
- **`Xmx<size>`** → Maximum heap size (e.g., `Xmx1024m`).
- **`XX:NewRatio=<ratio>`** → Ratio of Young to Old Gen (`XX:NewRatio=2` → 1/3rd Young, 2/3rd Old).
- **`XX:SurvivorRatio=<ratio>`** → Ratio of Eden to Survivor (`XX:SurvivorRatio=8` → Eden = 8 parts, S0/S1 = 1 part each).
- **`XX:MaxMetaspaceSize=<size>`** → Limits Metaspace growth (`XX:MaxMetaspaceSize=256m`).

Understanding heap memory structure helps in JVM tuning for **performance optimization** and **better memory management**.

## **3. Explain System.gc()? Can we use this in production environment?**

The `System.gc()` method is a **request** to the JVM to run the garbage collector, but it **does not guarantee** that GC will actually run. It simply **suggests** that the JVM perform garbage collection.

## **`System.gc()` Working:**

- When you call `System.gc()`, the JVM may or may not run the garbage collector immediately.
- The actual behavior **depends on the JVM implementation** and the GC algorithm in use.
- The method internally calls **`Runtime.getRuntime().gc()`**.

## **Example:**

```
public class GarbageCollectionExample {
    public static void main(String[] args) {
        GarbageCollectionExample obj = new GarbageCollectionExample();
        obj = null;  // Making object eligible for GC

        System.gc(); // Requesting GC
        System.out.println("Garbage Collection requested");
    }
    @Override
    @Deprecated // finalize() is deprecated in Java 9+
    protected void finalize() {
        System.out.println("Finalize method called, object garbage collected.");
    }
}
```

## **Possible Output**

```
Garbage Collection requested
Finalize method called, object garbage collected.
```

*(Note: The finalize method may not always execute, as `System.gc()` is just a request.)*

## **Can We Use `System.gc()` in Production?**

No, using `System.gc()` in production is not recommended.

**Reasons:**

1. **Unnecessary Overhead**
- `System.gc()` can trigger a **Full GC**, which **pauses the entire application**, leading to performance degradation.

**2. JVM Already Optimizes GC**

- Modern JVMs have **adaptive garbage collection** that works efficiently without manual intervention.

**3. Unpredictable Behavior**

- Calling `System.gc()` **does not guarantee** that GC will run immediately or free up significant memory.

**4. Performance Issues in High-Load Systems**

- In a high-traffic application, forcing GC can cause **latency spikes and slow response times**.

## **Use case:**

- **Testing and debugging** memory leaks in a development environment.
- **Before running memory-intensive operations** (but even this is not ideal for production).
- **Explicit GC control in applications** that require controlled memory management (rare cases).

## **Alternatives to `System.gc()` in Production:**

- **Tuning JVM GC settings** (`XX:+UseG1GC`, `Xms`, `Xmx`) for better automatic garbage collection.
- **Using memory profiling tools** like JVisualVM, JConsole, or GC logs.
- **Optimizing memory usage** by reducing object creation and properly managing resources.

## **4. What types of memories are present in Java Memory Model along with their use cases?**

The **Java Memory Model (JMM)** defines how Java threads interact with memory and ensures consistency across different hardware and JVM implementations.

Java memory is divided into several types, each serving a specific purpose.

## **Types of Memories in Java Memory Model:**

## **1. Heap Memory (Dynamic Memory)**

**a) Stores:** Objects and class instances.

**b) Use Cases:**

- Memory allocation for objects at runtime.
- Shared memory accessible by multiple threads.

**c) Divisions:**

- **Young Generation** → Short-lived objects.
- **Old Generation (Tenured Gen)** → Long-lived objects.
- **Metaspace** → Class metadata (Java 8+).

## **2. Stack Memory (Thread Stack)**

**a) Stores:** Method call frames, local variables, and references to heap objects.

**b) Use Cases:**

- Stores method execution details for individual threads.
- Each thread gets its own stack.

**c) Memory Allocation:**

- Follows **LIFO (Last In, First Out)** principle.

**Example:**

```
public class StackExample {
    public static void main(String[] args) {
        int num = 10; // Stored in stack
        String text = "Java"; // Reference in stack, object in heap
        method();
    }

    static void method() {
        double value = 5.5; // New stack frame created for this method
    }
}
```

## **3. Metaspace (Replaced PermGen in Java 8)**

**a) Stores:** Class metadata, method data, and runtime constant pool.

**b) Use Cases:**

- Stores information about loaded classes.
- Uses **native memory** (unlike PermGen, which had a fixed size).

**Example JVM Parameter:**

```
-XX:MaxMetaspaceSize=256m
```

## **4. PC Register (Program Counter Register)**

**a) Stores:** Address of the currently executing Java instruction.

**b) Use Cases:**

- Helps the JVM keep track of execution flow.
- Each thread has its own PC register.
- JVM **does not expose the PC Register directly to developers**, and its role is mostly internal.

**c) Special Case:**

- If a thread executes a **native method**, the PC register value is undefined.

## **5. Native Method Stack**

**a) Stores:** Native (non-Java) method calls.

**b) Use Cases:**

- Required when Java calls **C/C++ (JNI — Java Native Interface)** methods.
- Stores native function call details.

**Example:**

```
class NativeExample {
     native void nativeMethod(); // Native method declaration
  }
```

## **5. In which section of memory are primitive data types are stored?**

Primitive data types (`int`, `char`, `float`, `double`, etc.) are stored differently depending on how they are declared:

## **1. If Declared Inside a Method (Local Variables) → Stored in Stack Memory**

- **Stack memory** stores method-specific local variables, including primitive types.
- **Faster access** because each thread has its own stack.

**Example:**

```
public class PrimitiveExample {
    public static void main(String[] args) {
        int a = 10;  // Value stored directly in stack
        char c = 'J'; // Value stored directly in stack
        String str = "Hello"; // Reference stored in stack, object in heap
    }
}
```

**Why in Stack?**

- These are method-local variables.
- Stack memory is lightweight and automatically cleared when the method finishes execution.

## **2. If Declared as Instance Variables (Class-Level) → Stored in Heap Memory**

- **Instance variables of a class are part of the object** → Stored in **Heap Memory**.
- Their actual **values are stored inside the object**, while references stay in stack memory.

**Example:**

```
class Test {
    int x = 20; // Stored in heap (inside object)
}

public class Main {
    public static void main(String[] args) {
        Test obj1 = new Test(); // Reference in stack, object in heap
        Test obj2 = new Test(); // Separate object in heap
    }
}
```

**Why in Heap?**

- The object `obj` is stored in heap memory.
- Since `x` is an **instance variable**, it is stored inside the object in heap.

## **3. If Declared as Static Variables → Stored in Method Area (Part of Metaspace in Java 8+)**

- **Static variables belong to the class, not instances.**
- They are stored in **Method Area** (which is part of Metaspace in Java 8+).

**Example:**

```
class Test {
    static int y = 50; // Stored in Method Area (Metaspace)
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Test.y); // Accessed via class name
    }
}
```

**Why in Method Area?**

- Static variables **belong to the class itself, not objects**.
- They persist throughout the program execution.

## **6. What do you mean by memory reference?**

A **memory reference** in Java refers to the address in memory where an object is stored.

Instead of storing actual objects in variables, Java stores references (pointers) to the memory location where the object resides in **heap memory**.

- **References are stored in stack memory**, while objects reside in **heap memory**.
- Java passes a copy of the reference (pass-by-value), meaning modifications affect the object but not the reference itself.
- If no variable holds a reference to an object, it becomes eligible for **garbage collection**.
- **Primitives do not have memory references**; they are stored directly in stack or heap.

## **Memory References Working:**

1. When you create an object in Java using `new`, the object is stored in **heap memory**, and a **reference to that memory location** is assigned to the variable.
2. This reference is stored in **stack memory** if it’s a local variable.
3. Multiple variables can hold references to the same object.

## **Example:**

```
class Test {
    int x;
}

public class Main {
    public static void main(String[] args) {
        Test obj1 = new Test(); // obj1 stores a reference to the object in heap memory
        Test obj2 = obj1; // obj2 now holds the same reference as obj1
        obj1.x = 10;
        System.out.println(obj2.x); // Output: 10 (because obj1 and obj2 reference the same object)
    }
}
```

## **Breakdown:**

- `new Test();` creates an object in **heap memory**.
- `obj1` holds a **memory reference** to that object.
- `obj2 = obj1;` assigns the **same reference** to `obj2`, meaning both `obj1` and `obj2` point to the **same object**.
- Any modification through `obj1` reflects when accessed via `obj2`, since both reference the same memory location.

## **Example: Losing a Memory Reference (Garbage Collection)**

```
public class Main {
    public static void main(String[] args) {
        Test obj = new Test(); // obj holds reference to heap memory
        obj = null; // The object is now eligible for garbage collection
    }
}
```

Here, setting `obj = null;` **removes the reference**, making the object unreachable and eligible for garbage collection.

## **7. Why do we store cookies?**

Cookies are small pieces of data stored on a user’s browser by websites. They help websites remember information about users to improve **functionality, performance, personalization, and tracking**.

## **1. Maintaining User Sessions**

Cookies store session IDs, enabling websites to keep users logged in even when they navigate between pages.

**Example:**

- When you log into Gmail, a session cookie keeps you logged in until you close the browser or log out.

## **2. Personalizing User Experience**

Websites use cookies to remember user preferences like themes, language settings, or layout choices.

**Example:**

- YouTube remembers your preferred video resolution.
- An e-commerce site remembers items in your cart.

## **3. Tracking User Behavior (Analytics & Ads)**

Cookies help websites track user activities to improve services and show targeted ads.

**Example:**

- Google Analytics uses cookies to analyze website traffic.
- Advertisers track which products you viewed and show relevant ads later.

## **4. Storing Temporary Data**

Cookies store temporary data like search history or recently viewed items.

**Example:**

- Amazon suggests products based on your recent searches.
- A form autofills based on previous inputs.

## **5. Enhancing Website Performance**

Some cookies store cached data to make websites load faster.

**Example:**

- A news website caches article thumbnails for quick loading.

## **8. What do you understand by recursive program?**

A **recursive program** is a program that calls itself within its own execution. In simple terms, **recursion** is a technique where a function **calls itself** to solve a smaller version of the same problem until a base condition is met.

## **Components:**

1. **Base Case:** The condition that stops the recursion to prevent infinite loops.
2. **Recursive Case:** The function calls itself with a smaller problem.

## **Example: Factorial Using Recursion**

Factorial of `n` (`n!`) is calculated as: n!=n×(n−1)!

**Recursive Approach:**

```
public class Factorial {
    public static int factorial(int n) {
        if (n == 0) {  // Base case
            return 1;
        }
        return n * factorial(n - 1);  // Recursive case
    }

public static void main(String[] args) {
        System.out.println(factorial(5)); // Output: 120
    }
}
```

## **Working: Recursive Call Stack**

```
factorial(5) → 5 * factorial(4)
factorial(4) → 4 * factorial(3)
factorial(3) → 3 * factorial(2)
factorial(2) → 2 * factorial(1)
factorial(1) → 1 * factorial(0)
factorial(0) → 1 (Base case reached)
```

Final result: `5 * 4 * 3 * 2 * 1 = 120`

## **Types of Recursion**

1. **Direct Recursion** → A function calls itself.

```
void function() {
function(); // Direct call
}
```

**2. Indirect Recursion** → Two or more functions call each other.

```
void functionA(int n) {
    if (n == 0) return;
    functionB(n - 1);
}
void functionB(int n) {
    if (n == 0) return;
    functionA(n - 1);
}
```

**3. Tail Recursion** → The recursive call is the last operation before returning the result.

```
public int tailRecursion(int n, int result) {
    if (n == 0) return result;
    return tailRecursion(n - 1, n * result);
}
```

## **Use Cases:**

1. **Mathematical Problems** → Factorial, Fibonacci, Power Calculation.
2. **Data Structures** → Trees, Graphs, Linked Lists.
3. **Backtracking Algorithms** → Sudoku Solver, Maze Solving.
4. **Sorting Algorithms** → QuickSort, MergeSort

## **Pros:**

1. **Simplifies complex problems** (like tree traversal)
2. **Less code, more readability**

## **Cons:**

1. **Uses more memory (Stack Overflows if deep recursion occurs)**
2. **Can be slower compared to loops** (due to function call overhead).

## **9. Explain ConcurrentHashMaps. Is it possible for two threads to read or modify a ConcurrentHashMap at the same time?**

A **ConcurrentHashMap** in Java is a thread-safe, high-performance alternative to `HashMap`, designed for concurrent operations.

It belongs to the **java.util.concurrent** package and allows multiple threads to access and modify the map without explicit synchronization.

## **Features:**

1. **Thread Safety Without Locks on the Whole Map**
- Unlike `HashMap`, which is **not thread-safe**, and `Hashtable`, which uses **synchronized methods (slower)**, `ConcurrentHashMap` **divides** the map into segments and synchronizes them individually.

**2. Allows Concurrent Reads & Controlled Writes**

- Multiple threads **can read simultaneously** without blocking.
- Writes (updates, inserts, deletes) use a **fine-grained locking mechanism** for better performance.

**3. No Null Keys or Values**

- Unlike `HashMap`, `ConcurrentHashMap` **does not allow** `null` keys or `null` values to prevent ambiguity in concurrent environments.

**4. Uses Segmentation (Before Java 8) & CAS (After Java 8)**

- **Before Java 8:** Used **segment-based locking**, where different parts of the map were locked separately.
- **Java 8 & Later:** Uses **Compare-And-Swap (CAS)** and bucket-level locks for better performance.

## **Can Two Threads Read or Modify a ConcurrentHashMap Simultaneously?**

1. **Two or more threads can read a `ConcurrentHashMap` simultaneously** because read operations do **not** require locking.
2. **Multiple threads can modify different segments of the map at the same time.** Writes are synchronized at the bucket level, meaning:
- If two threads modify **different keys**, they can do so **concurrently**.
- If two threads modify **the same key**, one thread will block until the operation is completed due to internal locks or CAS.

3. **Iteration using `keySet()`, `values()`, or `entrySet()` is weakly consistent** and does **not throw `ConcurrentModificationException`**, unlike `HashMap`.

## **Example:**

```
import java.util.concurrent.*;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<Integer, String> map = new ConcurrentHashMap<>();
        // Adding elements concurrently
        map.put(1, "A");
        map.put(2, "B");
        // Thread 1: Reading from the map
        new Thread(() -> {
            System.out.println("Thread 1: " + map.get(1));
        }).start();
        // Thread 2: Writing to the map
        new Thread(() -> {
            map.put(3, "C");
            System.out.println("Thread 2: Inserted key 3");
        }).start();
    }
}
```

**Thread 1 can read while Thread 2 writes, without blocking each other.**

## **10. What do you understand by prototype design pattern? Explain with example and code.**

The **Prototype Design Pattern** is a **creational design pattern** that allows you to **clone existing objects** instead of creating new ones from scratch. This improves performance, especially when object creation is costly.

## **Use case:**

1. When object creation is **expensive** (e.g., large configurations, database connections).
2. When we need to **avoid creating new objects repeatedly** (e.g., game characters, UI elements).
3. When an object’s **initialization is complex** and copying an existing one is easier.

## **Concepts:**

1. **Prototype Interface** → Declares a `clone()` method. The `cloneObject()` method should follow Java's `Cloneable` interface and use `Object.clone()`.
2. **Concrete Class** → Implements the `clone()` method to duplicate objects.
3. **Client Code** → Uses the `clone()` method instead of creating new objects manually.

## **Example:**

Imagine we have a `Shape` class with multiple properties. Instead of creating new objects, we can **clone** an existing one.

## **Step 1: Create a Prototype Interface**

```
public interface Prototype {
    Prototype cloneObject();
}
```

## **Step 2: Implement Concrete Class**

```
class Shape implements Prototype {
    private String type;
    private String color;

    public Shape(String type, String color) {
        this.type = type;
        this.color = color;
    }

    // Implement clone method
    @Override
    public Shape cloneObject() {
        return new Shape(this.type, this.color);
    }

    public void display() {
        System.out.println("Shape Type: " + type + ", Color: " + color);
    }
}
```

## **Step 3: Client Code Using Prototype**

```
public class PrototypePatternDemo {
    public static void main(String[] args) {
        Shape originalShape = new Shape("Circle", "Red");
        originalShape.display();

        // Clone the object
        Shape clonedShape = originalShape.cloneObject();
        clonedShape.display();
    }
}
```

## **Output:**

```
Shape Type: Circle, Color: Red
Shape Type: Circle, Color: Red
```

The cloned object has the same properties as the original.

## **Real-World Examples:**

1. **Game Development** → Cloning character objects to avoid expensive creation.
2. **UI Frameworks** → Reusing similar UI components by cloning templates.
3. **Document Editors** → Duplicating existing files instead of reloading data.

## **11. Explain some annotations in Rest API?**

In **Spring Boot REST APIs**, annotations are used to define **endpoints, request handling, and response processing**.

Here are some of the most commonly used annotations:

## **1. `@RestController`**

- A combination of `@Controller` and `@ResponseBody`.
- Used to define a **REST API controller** that handles HTTP requests.

**Example:**

```
@RestController
public class MyController {
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }
}
```

No need to use `@ResponseBody` explicitly since `@RestController` does it by default.

## **2. `@RequestMapping`**

- Used to map **HTTP requests** to handler methods.
- Can specify **path, HTTP method, headers, etc.**

**Example:**

```
@RestController
@RequestMapping("/api")
public class UserController {
    @RequestMapping(value = "/users", method = RequestMethod.GET)
    public String getUsers() {
        return "List of users";
    }
}
```

Here, `/api/users` is mapped to a **GET request**.

## **3. `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`**

- Shortcuts for `@RequestMapping` for specific HTTP methods.

**Example:**

```
@RestController
@RequestMapping("/products")
public class ProductController {

@GetMapping("/{id}")
    public String getProduct(@PathVariable int id) {
        return "Product ID: " + id;
    }
    @PostMapping
    public String createProduct(@RequestBody String product) {
        return "Product Created: " + product;
    }
    @PutMapping("/{id}")
    public String updateProduct(@PathVariable int id, @RequestBody String product) {
        return "Product Updated: " + product;
    }
    @DeleteMapping("/{id}")
    public String deleteProduct(@PathVariable int id) {
        return "Product Deleted with ID: " + id;
    }
}
```

Simplifies REST endpoint definitions for different HTTP operations.

## **4. `@PathVariable`**

- Used to extract **path parameters** from the URL.

**Example:**

```
@GetMapping("/users/{userId}")
public String getUser(@PathVariable int userId) {
    return "User ID: " + userId;
}
```

`/users/10` → `User ID: 10`

## **5. `@RequestParam`**

- Used to extract **query parameters** from the URL.

**Example:**

```
@GetMapping("/search")
public String search(@RequestParam String query) {
    return "Searching for: " + query;
}
```

`/search?query=Java` → `Searching for: Java`

## **6. `@RequestBody`**

- Used to bind **JSON request bodies** to Java objects.

**Example:**

```
@PostMapping("/users")
public String createUser(@RequestBody User user) {
    return "User Created: " + user.getName();
}
```

Converts incoming **JSON data** into a Java object (`User`).

## **7. `@ResponseBody`**

- Converts Java object → **JSON response**.
- Used **internally in `@RestController`**.

**Example:**

```
@GetMapping("/info")
@ResponseBody
public String getInfo() {
    return "API Information";
}
```

Usually **not needed** inside `@RestController`, as it’s implicit.

## **8. `@ResponseStatus`**

- Used to set **custom HTTP status codes** in responses.

**Example:**

```
@PostMapping("/users")
@ResponseStatus(HttpStatus.CREATED)  // 201 Created
public String createUser() {
    return "User Created Successfully";
}
```

Returns **201 Created** instead of default **200 OK**.

## **9. `@ExceptionHandler`**

- Handles exceptions in **REST APIs** globally.

**Example:**

```
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleException(Exception e) {
        ErrorResponse error = new ErrorResponse("Error occurred", e.getMessage());
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}

// DTO class for better error response
class ErrorResponse {
    private String message;
    private String details;

    public ErrorResponse(String message, String details) {
        this.message = message;
        this.details = details;
    }

    public String getMessage() {
        return message;
    }

    public String getDetails() {
        return details;
    }
}
```

Captures exceptions **globally** and returns **custom error responses**.

## **10. `@CrossOrigin`**

- Enables **CORS (Cross-Origin Resource Sharing)**.

**Example:**

```
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("http://example.com")
                .allowedMethods("GET", "POST", "PUT", "DELETE");
    }
}
```

Allows API access from [`http://example.com`.](https://archive.ph/o/cwO7L/example.com/)

## **12. Briefly explain some of the new features of Java 8?**

Java 8 brought **major enhancements** to the language, making it more functional and efficient. Below are some of the most important features:

## **1. Lambda Expressions (Functional Programming)**

- Allows writing **shorter, cleaner** code for implementing functional interfaces.
- Enables passing behavior as a parameter.

**Example:**

```
// Without Lambda (Before Java 8)
Comparator<Integer> comparator = new Comparator<Integer>() {
    @Override
    public int compare(Integer a, Integer b) {
        return a.compareTo(b);
    }
};

// With Lambda (Java 8)
Comparator<Integer> comparatorLambda = (a, b) -> a.compareTo(b);
```

**Reduces boilerplate code** and improves readability.

## **2. Functional Interfaces & `@FunctionalInterface` Annotation**

- Introduced to support **Lambda Expressions**.
- A **functional interface** has **exactly one abstract method**.

**Example:**

```
@FunctionalInterface
interface Greeting {
    void sayHello(String message);
}

// Using Lambda
Greeting greeting = msg -> System.out.println("Hello, " + msg);
greeting.sayHello("Java 8!"); // Output: Hello, Java 8!
```

Functional interfaces like `Runnable`, `Callable`, `Comparator`, and new ones (`Predicate`, `Consumer`, `Supplier`) support functional programming.

## **3. Stream API (Efficient Data Processing)**

- Introduces a **functional approach** for processing collections.
- Supports operations like **filter, map, reduce, collect, etc.**.

**Example:**

```
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// Using Streams to filter names starting with "A"
List<String> filteredNames = names.stream()
                                  .filter(name -> name.startsWith("A"))
                                  .collect(Collectors.toList());
System.out.println(filteredNames); // Output: [Alice]
```

Makes collection processing **declarative, concise, and parallelizable**.

## **4. Default & Static Methods in Interfaces**

- Allows **interface methods** to have **default implementations**.
- Enables backward compatibility **without breaking existing code**.

**Example:**

```
interface Vehicle {
    default void print() {
        System.out.println("This is a vehicle.");
    }
}

class Car implements Vehicle {}
Car car = new Car();
car.print(); // Output: This is a vehicle.
```

**Avoids duplicate code** across multiple implementing classes.

## **5. `Optional` Class (Avoids `NullPointerException`)**

- Helps handle **null values safely** and reduces `NullPointerException` risks.

**Example:**

```
Optional<String> optional = Optional.ofNullable(null);
System.out.println(optional.orElse("Default Value")); // Output: Default Value
```

Encourages **safe handling of missing values**.

## **6. New Date and Time API (`java.time` Package)**

- Replaces **legacy `Date` and `Calendar`** classes.
- Provides **immutable, thread-safe** classes like `LocalDate`, `LocalTime`, and `LocalDateTime`.

**Example:**

```
LocalDate today = LocalDate.now();
System.out.println(today); // Output: 2025-02-07 (Current Date)
```

**More readable, reliable, and time-zone aware**.

## **7. Method References (More Readable Lambdas)**

- A shorthand for calling methods using `::` instead of lambda expressions.

**Example:**

```
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// Using Method Reference
names.forEach(System.out::println);
```

Improves **code clarity**.

## **8. `Collectors` (For Stream API)**

- Helps in **collecting stream data** into different forms like lists, sets, and maps.

**Example:**

```
List<String> list = Arrays.asList("Apple", "Banana", "Mango");

// Collecting elements into a List
List<String> upperCaseList = list.stream()
                                 .map(String::toUpperCase)
                                 .collect(Collectors.toList());
System.out.println(upperCaseList); // Output: [APPLE, BANANA, MANGO]
```

**Efficient data transformation and aggregation**.

## **9. Improved Concurrency with `ConcurrentHashMap` Enhancements**

- New methods like `compute()`, `merge()`, and `forEach()` improve performance and flexibility.

**Example:**

```
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.put("A", 1);
map.put("B", 2);

map.compute("A", (key, value) -> value + 10);
System.out.println(map.get("A")); // Output: 11
```

**Improved thread-safe operations**.

## **13. Suppose if we don’t override hash code in a hashing collection, then what will be the impact?**

If we **don’t override the `hashCode()` method** in a class used as a key in a **hashing-based collection** (like `HashMap`, `HashSet`, or `HashTable`), it can lead to **unexpected behavior and performance issues**.

## **1. Different Objects Might Have the Same Hash Code (Default Implementation)**

- The default `hashCode()` method in Object is typically based on the object's memory reference, meaning two logically equal objects may have different hash codes unless overridden.
- If not overridden, two logically equal objects **might not have the same hash code**, causing issues in hashing collections.

**Example:**

```
class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }
}
public class Main {
    public static void main(String[] args) {
        HashSet<Employee> employees = new HashSet<>();
        Employee e1 = new Employee("Alice");
        Employee e2 = new Employee("Alice");
        employees.add(e1);
        employees.add(e2);
        System.out.println(employees.size()); // Output: 2 (Expected: 1)
    }
}
```

**Issue:** Since `hashCode()` is not overridden, `e1` and `e2` get different hash codes, leading to **duplicate entries** in the `HashSet`.

## **2. Hash-Based Collections May Not Work Properly**

- Collections like `HashMap` or `HashSet` **rely on `hashCode()` for efficient storage and retrieval**.
- If `hashCode()` is not overridden, elements may be stored in **different hash buckets**, causing incorrect behavior.

**Example (Incorrect Key Lookup in `HashMap`)**

```
class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }
}
public class Main {
    public static void main(String[] args) {
        HashMap<Employee, Integer> map = new HashMap<>();
        Employee e1 = new Employee("Bob");
        map.put(e1, 100);
        Employee e2 = new Employee("Bob");
        System.out.println(map.get(e2)); // Output: null (Expected: 100)
    }
}
```

**Issue:** Since `hashCode()` is not overridden, `e1` and `e2` have different hash codes, making `map.get(e2)` **fail to retrieve** the expected value.

## **3. Performance Degradation**

- Hash-based collections **use `hashCode()` to locate elements quickly**.
- Without a proper `hashCode()`, all elements may end up in **one bucket**, degrading performance **from O(1) to O(n)**.

## **14. Suppose if we don’t override equals method in a hashing collection, then what will be the impact?**

If two objects are considered equal by `equals()`, they must return the same hash code from `hashCode()`.

If we **don’t override the `equals()` method** in a class used as a key in a **hashing-based collection** (like `HashMap`, `HashSet`, or `HashTable`), it can lead to **incorrect behavior, data duplication, and failed lookups**.

## **1. Objects with Same Data Will Be Treated as Different**

- By default, the `equals()` method in `Object` **compares memory addresses**.
- If we don’t override it, two objects with the same data will be treated as **different**, even if they logically represent the same entity.

**Example (Duplicate Entries in `HashSet`)**

```
import java.util.HashSet;

class Employee {
    String name;
    Employee(String name) {
        this.name = name;
    }
}
public class Main {
    public static void main(String[] args) {
        HashSet<Employee> employees = new HashSet<>();
        Employee e1 = new Employee("Alice");
        Employee e2 = new Employee("Alice");
        employees.add(e1);
        employees.add(e2);
        System.out.println(employees.size()); // Output: 2 (Expected: 1)
    }
}
```

**Issue**: Even though `e1` and `e2` **have the same name**, they are stored as **separate entries** because `equals()` is not overridden.

## **2. HashMap Fails to Retrieve Values Correctly**

- `HashMap` stores keys using **hash codes** but uses `equals()` for **key comparisons**.
- If `equals()` is not overridden, two objects with the **same data but different memory addresses** will be considered **different keys**.

**Example (Failed Key Lookup in `HashMap`)**

```
import java.util.HashMap;

class Employee {
    String name;
    Employee(String name) {
        this.name = name;
    }
}
public class Main {
    public static void main(String[] args) {
        HashMap<Employee, Integer> map = new HashMap<>();
        Employee e1 = new Employee("Bob");
        map.put(e1, 100);
        Employee e2 = new Employee("Bob");
        System.out.println(map.get(e2)); // Output: null (Expected: 100)
    }
}
```

**Issue**:

- Since `equals()` is not overridden, `e1` and `e2` **are considered different** objects.
- Even though they have the same name, `map.get(e2)` **returns `null` instead of 100**.

## **3. Performance Issues in Hash-Based Collections**

- Hash-based collections like `HashSet` and `HashMap` use **hash codes to determine bucket placement** and `equals()` to check for duplicate keys.
- If `equals()` is not overridden, it leads to **unnecessary duplicate entries**, increasing **memory usage and lookup time**.

## **15. How would you detect a deadlock in a running program?**

Deadlocks occur when two or more threads **block each other indefinitely** while waiting for resources held by the other.

## **1. Using `jstack` (Java Stack Trace)**

- **Best for Production Systems**
- The `jstack` tool (part of the JDK) captures thread dumps of a running JVM.
- If a deadlock exists, the output will explicitly mention it.

**Steps to Detect Deadlocks:**

1. Find the **PID (Process ID)** of the Java application:

```
jps
```

2. Run `jstack` on the Java process:

```
jstack <PID>
```

3. Look for `"Found one Java-level deadlock"` in the output.

**Example Output (Deadlock Detected)**

```
Found one Java-level deadlock:
=============================
Thread-1: waiting to lock Monitor A, which is held by Thread-2
Thread-2: waiting to lock Monitor B, which is held by Thread-1
```

Confirms that a **circular wait** is causing a deadlock.

## **2. Using `jconsole` (Java Monitoring & Management Console)**

- **Best for GUI-Based Monitoring**
- `jconsole` (Java Console) is a GUI tool that detects deadlocks automatically.
- Open `jconsole`, connect to the running JVM, and go to the **Threads tab** to check for deadlocks.

**Command to Launch:**

```
jconsole
```

- Select the Java process and navigate to **Threads > Detect Deadlock**.

## **3. Using `VisualVM` (Advanced JVM Monitoring)**

- **Best for Large Applications**
- `VisualVM` provides a **graphical thread dump and monitoring**.
- It automatically flags deadlocks under the **Threads** tab.

**How to Use:**

1. Start `VisualVM`:

```
jvisualvm
```

2. Attach to the running Java process.

3. Navigate to **Threads** and look for blocked threads.

## **4. Programmatic Detection Using `ThreadMXBean`**

- The **`ThreadMXBean`** class from `java.lang.management` allows **real-time deadlock detection**.
- **Best for Debugging Inside Code.**

**Example: Automatically Detect and Log Deadlocks**

```
import java.lang.management.ManagementFactory;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
import java.util.Arrays;

public class DeadlockDetector {
    public static void main(String[] args) {
        ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
        long[] deadlockedThreads = threadMXBean.findDeadlockedThreads();
        if (deadlockedThreads != null) {
            System.out.println("Deadlock detected!");
            ThreadInfo[] threadInfos = threadMXBean.getThreadInfo(deadlockedThreads);
            Arrays.stream(threadInfos).forEach(System.out::println);
        } else {
            System.out.println("No deadlocks detected.");
        }
    }
}
```

This can be scheduled to **run periodically in production systems**.

## **5. Manual Code Review (Identifying Common Deadlock Patterns)**

Deadlocks typically occur due to:

- **Nested locks:** One thread locks `A` → waits for `B`, while another locks `B` → waits for `A`.
- **Improper lock ordering:** Locks acquired in different sequences.
- **Synchronized blocks on shared resources.**

**Example Code That Can Cause Deadlock**

```
class A {
    synchronized void methodA(B b) {
        System.out.println("Thread 1: Locked A, waiting for B...");
        synchronized (b) {
            System.out.println("Acquired B");
        }
    }
}

class B {
    synchronized void methodB(A a) {
        System.out.println("Thread 2: Locked B, waiting for A...");
        synchronized (a) {
            System.out.println("Acquired A");
        }
    }
}
public class DeadlockExample {
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        new Thread(() -> a.methodA(b)).start();
        new Thread(() -> b.methodB(a)).start();
    }
}
```

If you **run this program**, it will get stuck because **each thread is waiting for the other**.

**16. What are the differences between Vector and ArrayList?**

![](https://dfhqskic79jp5c.archive.ph/cwO7L/ccf789a0a39e5faff0646d91b4408df0a7904b49.webp)

## **17. Explain Immutable class in Java.**

> This is a very important question and has been asked multiple times in my interview experiences.
> 

This is the best article you’ll find on Immutable classes., specifically written for this question. I highly recommend it:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/cwO7L/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

## **18. Suppose an arraylist reaches it’s threshold, how will it expand itself? What is it’s default size?**

When an `ArrayList` reaches its **current capacity**, it automatically **expands** by increasing its size by **50%**. The process follows these steps:

1. **Check if more elements can be added** → If not, **expansion is triggered**.
2. **New array is created** with about **50% more capacity** than the current one.
3. **Existing elements are copied** to the new array.
4. **Reference is updated** to point to the new, larger array.

This ensures that `ArrayList` dynamically grows as needed, but frequent resizing can be costly in terms of performance.

## **Default Initial Size:**

- If created using **`new ArrayList<>()`**, the **default capacity is `10`**.
- If created using **`new ArrayList<>(initialCapacity)`**, it starts with the specified `initialCapacity`.

**Example:** Default capacity expansion

```
import java.util.ArrayList;

public class ArrayListExpansion {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 1; i <= 15; i++) { // Adding more than 10 elements
            list.add(i);
            System.out.println("Size: " + list.size() + ", Capacity: Not Directly Accessible");
        }
    }
}
```

**Note:** The capacity is not directly accessible in `ArrayList`, but you can check it using reflection.

## **Capacity Growth Formula:**

The new capacity is calculated as:

New Capacity= ((Old Capacity * 3) / 2) + 1

**Example:** How `ArrayList` expands:

![](https://dfhqskic79jp5c.archive.ph/cwO7L/8bed888bd45649420f6011b58eb4470bd4e0f9ef.webp)

## **Performance Considerations:**

- Frequent resizing can be expensive **(O(n) complexity per resize)**.
- **Best Practice**: If you know the expected size, initialize with `new ArrayList<>(expectedSize)` to **avoid unnecessary resizing**.

**Example:**

```
ArrayList<Integer> list = new ArrayList<>(100); // Avoids multiple expansions
```