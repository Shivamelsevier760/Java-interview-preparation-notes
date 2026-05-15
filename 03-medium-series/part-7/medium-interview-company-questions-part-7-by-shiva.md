# Medium interview company questions part 7 by Shivam Srivastava

# **Wipro Java Developer Interview**

**1. What is the difference between Method overloading and Method overriding?**

![](https://dgxf6kim16yjpd.archive.ph/ovnt3/b8ce0eeb02e6a708360b9f9a4562c1b3357af555.webp)

## **2. What is an Interface?**

An interface in Java is like a blueprint of methods that a class must implement, but it doesn’t provide the implementation itself.

By default, all methods in an interface are public and abstract (at least until Java 8). It’s primarily used to achieve abstraction and multiple inheritance.

For example, if you have an interface called `Animal` with a method `void eat()`, any class implementing `Animal` must provide its own definition of `eat()`.

```
interface Animal {
    void eat(); // Abstract method
}

class Dog implements Animal {
    @Override
    public void eat() {
        System.out.println("Dog eats bones");
    }
}
```

Java 8 added more flexibility by introducing **default methods** and **static methods** in interfaces. Default methods can have a body, so we can now provide a default implementation if needed.

For example:

```
interface Animal {
    default void sleep() {
        System.out.println("Sleeping...");
    }
}
```

One of the key advantages of interfaces is that they allow **multiple inheritance**. A class can implement multiple interfaces, which helps overcome the limitation of single inheritance in Java.

For instance:

```
interface Pet {
    void play();
}

class Dog implements Animal, Pet {
    @Override
    public void eat() {
        System.out.println("Dog eats food");
    }
    @Override
    public void play() {
        System.out.println("Dog plays fetch");
    }
}
```

## **3. What is an Abstract Class?**

An abstract class in Java is a class that cannot be instantiated on its own. It’s meant to be extended by other classes, providing a blueprint for those subclasses.

It can contain both abstract methods (methods without a body) and concrete methods (methods with a body).

For example:

```
abstract class Animal {
    abstract void sound(); // Abstract method
    void sleep() { // Concrete method
        System.out.println("Sleeping...");
    }
}
```

Here’s how it works:

1. **Abstract Methods:** These are methods that don’t have a body. Subclasses are required to implement them.
2. **Concrete Methods:** Abstract classes can also have fully implemented methods to share common functionality across subclasses.
3. **Variables:** Unlike interfaces, abstract classes can have instance variables as well as static constants.
4. **Constructors:** Abstract classes can have constructors, which can be used to initialize fields when a subclass is instantiated.

## **Features:**

1. **Purpose:** Abstract classes are useful when you want to provide a base class with default behavior and require certain methods to be implemented by subclasses.
2. **Inheritance:** A class can only extend one abstract class (single inheritance).
3. **Flexibility:** Unlike interfaces, abstract classes allow you to define shared states (fields) and methods that subclasses can use directly.

Here’s an example of inheritance using an abstract class:

```
abstract class Animal {
    abstract void sound(); // Abstract method
    void sleep() { // Concrete method
        System.out.println("Animal sleeps");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
```

Now, if you try to instantiate `Animal` directly, it will result in a compilation error because it’s abstract:

```
Animal animal = new Animal(); // ERROR
```

## **Usecase of Abstract Class?**

- Use an abstract class when classes share common behavior and fields, but you also want to enforce certain methods to be implemented by subclasses.
- If you need multiple inheritance, interfaces are a better choice since Java doesn’t support multiple inheritance with classes.

## **4. When to use Interface vs Abstract class?**

## **Use an Interface When:**

1. **You Need Multiple Inheritance:**
- Since Java allows a class to implement multiple interfaces but only extend one class, interfaces are ideal when a class needs to inherit behavior from multiple sources.
- For example, if a class needs to represent both a `Vehicle` and a `Trackable` entity, interfaces are the way to go:

```
interface Vehicle {
    void drive();
}

interface Trackable {
    void trackLocation();
}

class Car implements Vehicle, Trackable {
    @Override
    public void drive() {
        System.out.println("Driving...");
    }

    @Override
    public void trackLocation() {
        System.out.println("Tracking location...");
    }
}
```

**2. Defining a Contract:**

- Use interfaces when you want to define a contract that multiple classes must adhere to, without specifying how they implement it.

**3. No Shared State or Code:**

- Interfaces are best when there’s no common state or functionality across implementing classes, as they cannot have instance variables or non-static code.

**4. Backward Compatibility (Post-Java 8):**

- Interfaces in Java 8+ allow **default methods**, which can provide shared functionality. However, if heavy shared code is needed, abstract classes might be better.

## **Use an Abstract Class When:**

1. **Shared State or Behavior:**
- If multiple classes need to share fields or default implementations, an abstract class is a better fit.
- For example, if all animals have a `name` and a `sleep()` method:

```
abstract class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    abstract void makeSound();

    void sleep() {
        System.out.println(name + " is sleeping...");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    @Override
    void makeSound() {
        System.out.println(name + " barks!");
    }
}
```

**2. Providing a Base Class with Default Behavior:**

- Abstract classes allow you to define concrete methods that can be reused by subclasses while still requiring them to implement specific abstract methods.

**3. Extensibility:**

- If your base class might evolve to include more shared functionality or state, an abstract class provides more flexibility.

**4. Constructors Needed:**

- Abstract classes can have constructors, allowing you to initialize shared fields, which interfaces can’t do.

## **5. Explain Exception Handling in Java.**

**Exception Handling** is a mechanism in Java that allows the programmer to handle runtime errors gracefully, ensuring the normal flow of the application isn’t disrupted.

It involves detecting and responding to exceptional situations (errors) that arise during program execution.

**Exception**:

- An event that disrupts the normal flow of a program.
- Exceptions can occur due to issues like invalid input, resource unavailability, or logical errors.

**Types of Exceptions**:

1. **Checked Exceptions**:
- Exceptions checked at compile time.
- Must be declared in the `throws` clause or handled using `try-catch`.
- Examples: `IOException`, `SQLException`.

**2. Unchecked Exceptions**:

- Exceptions not checked at compile time but at runtime.
- Caused by logical errors in the program.
- Examples: `ArithmeticException`, `NullPointerException`.

**3. Errors**:

- Severe problems beyond the application’s control.
- Examples: `OutOfMemoryError`, `StackOverflowError`.

## **Exception Handling Keywords**

Java uses five keywords for exception handling:

1. **`try`**:Encloses the code that might throw an exception.

```
try
{
// Code that may cause an exception
}
```

2. **`catch`**:Handles the exception. It follows the `try` block and matches the exception type.

```
catch (ExceptionType e)
{
// Code to handle the exception
}
```

3.**`finally`**:A block that executes irrespective of whether an exception is thrown or not. Typically used for resource cleanup.

```
finally {
     // Cleanup code
}
```

4.**`throw`**:Used to explicitly throw an exception.

```
throw new ExceptionType("Error Message");
```

5.**`throws`**:Declares exceptions that a method might throw.

```
public void methodName() throws ExceptionType
{
     // Method code
}
```

**Example**

```
public class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // This will cause ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero: " + e.getMessage());
        } finally {
            System.out.println("This block always executes.");
        }
    }
}
```

**Output**:

```
Cannot divide by zero: / by zero
This block always executes.
```

## **6. What is a Finally Block?**

The **`finally` block** is a special block of code in Java associated with exception handling. The finally block always executes when the try block exits.

It is used to execute crucial cleanup code, such as releasing resources, closing files, or clearing buffers, irrespective of whether an exception is thrown or not.

## **Characteristics**

1. **Always Executes**:
- The code inside a `finally` block executes regardless of whether:
- An exception is thrown.
- An exception is caught.
- The `try` block completes normally.
- The only exceptions to this rule are if the program exits using `System.exit()` or if the JVM crashes.

**2. Used for Cleanup**:

- Commonly used for resource cleanup like closing database connections, file streams, or sockets.

**3. Optional**:

- A `finally` block is not mandatory. You can write a `try` block with or without it.

## **Syntax**

```
try {
    // Code that may throw an exception
} catch (ExceptionType e) {
    // Code to handle the exception
} finally {
    // Code that will always execute
}
```

## **7. What Happens if the `finally` Block Contains `return`?**

If a `finally` block contains a `return` statement, it overrides any `return` or exception in the `try` or `catch` blocks. This is generally discouraged as it makes the code less readable and harder to debug.

**Example**:

```
public class FinallyReturnExample {
    public static int testMethod() {
        try {
            return 10; // This return is overridden by the finally block
        } finally {
            return 20;
        }
    }

public static void main(String[] args) {
        System.out.println("Returned Value: " + testMethod());
    }
}
```

**Output**:

```
Returned Value: 20
```

## **8. What are Collections in Java?**

In Java, **Collections** refer to a framework that provides a unified architecture for storing and manipulating a group of objects.

It includes a set of interfaces, classes, and algorithms to manage data efficiently.

Collections are an essential part of Java, allowing developers to manage data like lists, sets, maps, and queues with built-in methods for operations like adding, removing, sorting, and searching.

## **Components of the Java Collections Framework**

1. **Interfaces**: These define the core structure and behavior of collections.
- **`Collection<E>`**: The root interface for most collection types.
- **`List<E>`**: Represents an ordered collection, allows duplicates, and elements can be accessed by index.
- **`Set<E>`**: Represents an unordered collection with no duplicates.
- **`Queue<E>`**: A collection designed for holding elements before processing, based on FIFO (First-In-First-Out).
- **`Map<K, V>`**: Represents key-value pairs where keys are unique, and values can be duplicated.

**2. Implementations**: These are concrete classes that provide actual data structures implementing the collection interfaces.

**`List` Implementations**:

- **`ArrayList<E>`**: A resizable array implementation, ideal for fast random access.
- **`LinkedList<E>`**: A doubly linked list that allows for efficient insertion and removal of elements.
- **`Vector<E>`**: A synchronized version of `ArrayList`, though it’s not recommended for new code.
- **`Stack<E>`**: A subclass of `Vector`, representing a stack (LIFO structure).

**`Set` Implementations**:

- **`HashSet<E>`**: A hash-based implementation that doesn’t maintain any order.
- **`LinkedHashSet<E>`**: A hash set that maintains insertion order.
- **`TreeSet<E>`**: A set that sorts elements in natural order or using a comparator.

**`Queue` Implementations**:

- **`PriorityQueue<E>`**: A queue where elements are ordered based on their natural ordering or a custom comparator.
- **`ArrayDeque<E>`**: A dynamic array-based deque (double-ended queue), ideal for adding/removing elements from both ends.

**`Map` Implementations**:

- **`HashMap<K, V>`**: A hash table-based map, doesn’t guarantee the order of keys.
- **`LinkedHashMap<K, V>`**: A map that maintains insertion order.
- **`TreeMap<K, V>`**: A map that sorts keys in natural or custom order.
- **`Hashtable<K, V>`**: A legacy, synchronized map (typically replaced by `HashMap`).
- **`ConcurrentHashMap<K, V>`**: A thread-safe map for high concurrency situations.

## **Specialized Collections**

1. **`EnumSet<E>`**: A `Set` implementation specifically for use with enum types, more efficient than regular sets when dealing with enums.
2. **`EnumMap<K, V>`**: A `Map` implementation designed for use with enum keys, offering better performance.
3. **`CopyOnWriteArrayList<E>`**: A thread-safe version of `ArrayList`, where every modification creates a copy of the underlying array.
4. **`CopyOnWriteArraySet<E>`**: A thread-safe version of `Set`, using a `CopyOnWriteArrayList`.
5. **`ConcurrentLinkedQueue<E>`**: A thread-safe, non-blocking queue implementation for high concurrency environments.

## **Legacy Collections (Pre-Java 1.2)**

- **`Vector`**: An older, synchronized collection, now generally replaced by `ArrayList`.
- **`Stack`**: A subclass of `Vector`, for stack-like behavior (LIFO).
- **`Properties`**: A `Hashtable` subclass used for key-value pairs with string keys and values, often used for configuration files.

**9. What are the differences between Hashmap vs Hashtable?**

![](https://dgxf6kim16yjpd.archive.ph/ovnt3/17345174abdc7afc3dcad9aca15f61fa558896f9.webp)

**10. What are the differences between LinkedList vs ArrayList?**

![](https://dgxf6kim16yjpd.archive.ph/ovnt3/a15a048c40828d4f896785f21b86eeb2633d4a73.webp)

**11. What are the differences between == and .equals()?**

![](https://dgxf6kim16yjpd.archive.ph/ovnt3/18e39e824e12b4ef89f40d9815c2e041608a9e54.webp)

## **12. How to create an immutable class in Java?**

I’ve already written a very detailed article on this, you should go through this and you’ll understand everything you need to know about Immutable classes and their creation:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/ovnt3/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

**13. What are the differences between Spring Boot vs Spring MVC?**

![](https://dgxf6kim16yjpd.archive.ph/ovnt3/85229f9cb2ece757f8778758c851df84619bcf73.webp)

## **14. What is the default server port in Spring Boot?**

In Spring Boot, the default server port is **8080**.

When you run a Spring Boot application, by default, it starts an embedded web server (like Tomcat) and listens on port **8080**.

You can change this default port by modifying the `application.properties` or `application.yml` configuration file in your project.

## **To change the default port:**

**application.properties:**

```
server.port=9090
```

**application.yml:**

```
server:
  port: 9090
```

This would change the port from the default **8080** to **9090**.

## **15. What is Spring Boot Actuator?**

**Spring Boot Actuator** is a powerful set of tools and features that helps you monitor and manage your Spring Boot application in production.

It provides a range of built-in endpoints that expose various metrics, health checks, and configuration details, making it easier to understand and manage the application’s state.

## **Features of Spring Boot Actuator:**

1. **Health Checks**:
- Provides a `/actuator/health` endpoint that checks the health of your application. It can be used to monitor the system’s overall health by integrating with various subsystems like databases, messaging services, or custom health checks.
- Example: You can check the health of your application via a simple HTTP request:

```
GET /actuator/health
```

**2. Metrics**:

- Exposes application-level metrics such as memory usage, thread counts, system load, HTTP request/response counts, and more via the `/actuator/metrics` endpoint.
- Example: Get detailed metrics on how your application is performing, like:

```
GET /actuator/metrics
```

**3. Application Info**:

- The `/actuator/info` endpoint gives information about the application like version, build time, custom metadata, etc.
- This can be helpful for tracking release versions or displaying build information.

**4. Environment Information**:

- Exposes information about the environment your application is running in, such as system properties, environment variables, and application properties. You can access this via the `/actuator/env` endpoint.

**5. Auditing**:

- Provides support for auditing specific actions within the application (such as login attempts or specific changes). You can audit application events, making it easier to track certain actions.

**6. Logging**:

- The `/actuator/loggers` endpoint allows you to view and manage the application's loggers dynamically. You can change log levels (e.g., DEBUG, INFO) for specific components of your application at runtime.

**7. Custom Endpoints**:

- You can define your own custom actuator endpoints to expose additional application-specific information.

## **Enable Spring Boot Actuator:**

To enable Spring Boot Actuator, simply add the `spring-boot-starter-actuator` dependency to your `pom.xml` (for Maven) or `build.gradle` (for Gradle).

- **Maven:**

```
<dependency>
<groupId>org.springframework.boot</groupId>
     <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

- **Gradle:**

```
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

Once added, you can access several built-in actuator endpoints and customize them in your `application.properties` or `application.yml`.

# **Accenture Java Developer Interview**

## **1. Suppose you’ve a list of employees. Sort them based on their names using Java 8.**

```
import java.util.*;
import java.util.stream.*;

public class Main {
    // Employee class with name and age
    static class Employee {
        private String name;
        private int age;
        // Constructor
        public Employee(String name, int age) {
            this.name = name;
            this.age = age;
        }
        // Getter for name
        public String getName() {
            return name;
        }
        // Getter for age
        public int getAge() {
            return age;
        }
        // toString method to print the Employee details
        @Override
        public String toString() {
            return "Employee{name='" + name + "', age=" + age + "}";
        }
    }

    public static void main(String[] args) {
        // Step 1: Create a list of employees
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 30),
            new Employee("Bob", 25),
            new Employee("Charlie", 28),
            new Employee("David", 35)
        );

        // Step 2: Sort the list of employees by name using Java 8 Stream API
        List<Employee> sortedEmployees = employees.stream()
            .sorted(Comparator.comparing(Employee::getName)) // Sorting by name
            .collect(Collectors.toList()); // Collect the sorted stream back into a list

        // Step 3: Print the sorted list of employees
        sortedEmployees.forEach(System.out::println);
    }
}
```

## **Explanation:**

- **`employees.stream()`**: Converts the `List<Employee>` into a stream. A stream is a sequence of elements that can be processed in parallel or sequentially.
- **`.sorted(Comparator.comparing(Employee::getName))`**:This sorts the stream of employees by their names.
- `Comparator.comparing(Employee::getName)` creates a comparator that compares employees based on the `name` field. `Employee::getName` is a method reference that points to the `getName()` method of the `Employee` class.
- **`.collect(Collectors.toList())`**: After sorting, we collect the sorted stream back into a `List<Employee>`. This is necessary because streams do not modify the original list but return a new one.
- **`forEach(System.out::println)`**: This iterates over the `sortedEmployees` list and prints each `Employee` object to the console. The `System.out::println` is a method reference that calls the `println()` method on `System.out` for each employee in the list.

**Output**:

```
Employee{name='Alice', age=30}
Employee{name='Bob', age=25}
Employee{name='Charlie', age=28}
Employee{name='David', age=35}
```

- The employees are now sorted alphabetically by their `name` field: `Alice`, `Bob`, `Charlie`, and `David`.

## **2. What is a comparable interface? Explain the difference between comparable vs comparator.**

The `Comparable` interface in Java is used to define a natural ordering for objects of a class. It allows objects of that class to be compared with each other, which is especially useful for sorting collections like arrays or lists.

The `Comparable` interface has a **single method**:

```
int compareTo(T o);
```

Where:

- `T` is the type of object being compared.
- The method returns:
- **A negative integer** if the current object is less than the object `o`.
- **Zero** if the current object is equal to the object `o`.
- **A positive integer** if the current object is greater than the object `o`.

## **Example:**

Here’s an example of how you might use the `Comparable` interface to compare and sort objects of a class.

```
class Employee implements Comparable<Employee> {
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
    public int compareTo(Employee other) {
        return this.name.compareTo(other.name);  // Compare by name alphabetically
    }
    @Override
    public String toString() {
        return "Employee{name='" + name + "', age=" + age + "}";
    }
}
```

## **Explanation:**

- The `Employee` class implements the `Comparable<Employee>` interface.
- In the `compareTo()` method, employees are compared by their name alphabetically using `String`'s `compareTo()` method.
- By implementing this method, objects of `Employee` can be naturally sorted based on their name using methods like `Collections.sort()`.

## **Difference Between `Comparable` and `Comparator`:**

![](https://db4ci98k88vxrf.archive.ph/taCf2/47c1399bd01133c8794e34ed59f031cfbe80bfb8.webp)

**3. Difference between callable and runnable interface in Java.**

![](https://db4ci98k88vxrf.archive.ph/taCf2/6e332cbd8564f24265d53c5e7d5fc22fc5025543.webp)

## **4. How are you managing exceptions in your Spring Boot project (Explanation of Global Exception Handling)?**

In Spring Boot, global exception handling is typically implemented using the `@ControllerAdvice` annotation. This approach allows you to manage exceptions centrally across all controllers, providing a consistent and clean way of handling errors.

Here’s how you can implement it:

**1. Create a Custom Exception Class**: First, you define custom exceptions that represent different error scenarios in your application. For example, if a resource is not found, you can create a `ResourceNotFoundException` class.

```
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

**2. Create a Global Exception Handler**: Next, you define a class annotated with `@ControllerAdvice`. This class contains methods annotated with `@ExceptionHandler`, which specify how to handle different types of exceptions.

```
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleResourceNotFoundException(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleAllExceptions(Exception ex) {
        return new ResponseEntity<>("An unexpected error occurred: " + ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```

**Explanation**:

- The `@ControllerAdvice` annotation marks this class as a global exception handler. It applies to all controllers in the application.
- The `@ExceptionHandler` annotation is used on methods to handle specific exceptions. In this case, we handle `ResourceNotFoundException` and a generic `Exception`.
- For each exception, we return a `ResponseEntity` with an appropriate HTTP status and message.

**3. Throwing Exceptions in Controllers**: In the controller, you can now throw these exceptions when a certain error condition occurs.

```
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {
    @GetMapping("/resource/{id}")
    public String getResource(@PathVariable("id") String id) {
        if ("notfound".equals(id)) {
            throw new ResourceNotFoundException("Resource with ID " + id + " not found");
        }
        return "Resource found with ID: " + id;
    }
}
```

When the `getResource` method is called with an ID that is "notfound", it throws the `ResourceNotFoundException`, and the global exception handler handles it by returning a `404 Not Found` response with the appropriate message.

## **Benefits of Global Exception Handling:**

1. **Centralized Error Handling**: All exceptions are handled in one place, making the code cleaner and more maintainable.
2. **Consistent Error Responses**: You can standardize error messages and HTTP status codes across the entire application, improving user experience.
3. **Separation of Concerns**: Your controllers remain focused on business logic, and exception handling is delegated to the `@ControllerAdvice` class.

## **Advanced Handling:**

- You can also define a custom error response format by creating an `ErrorResponse` class, allowing you to return structured JSON error messages.
- Another option is using the `@ResponseStatus` annotation on custom exceptions. This can map exceptions to specific HTTP status codes without needing an explicit handler.

```
@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

This automatically maps the `ResourceNotFoundException` to a `404 Not Found` response.

## **5. What is Deep Cloning? Difference between Shallow Cloning and Deep Cloning.**

Deep cloning is when an object and all the objects it refers to are cloned. This means that not only the object itself is copied, but also all the nested objects (or objects referenced by the original object).

In deep cloning, the new object has its own copies of the nested objects, and changes to the cloned object or any of its nested objects won’t affect the original object.

## **Example of Deep Cloning:**

```
class Person implements Cloneable {
    String name;
    int age;
    Address address;

Person(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        // Create a deep clone by manually cloning the nested objects
        Person cloned = (Person) super.clone();
        cloned.address = (Address) address.clone(); // Deep cloning the Address object
        return cloned;
    }
}
class Address implements Cloneable {
    String city;
    String street;
    Address(String city, String street) {
        this.city = city;
        this.street = street;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone(); // Clone the Address object
    }
}
public class DeepCloneExample {
    public static void main(String[] args) throws CloneNotSupportedException {
        Address address = new Address("New York", "5th Avenue");
        Person person1 = new Person("John", 30, address);
        Person person2 = (Person) person1.clone();
        // Modify address in person2
        person2.address.city = "Los Angeles";
        System.out.println(person1.address.city);  // "New York"
        System.out.println(person2.address.city);  // "Los Angeles"
    }
}
```

## **Explanation:**

- In this example, both the `Person` object and its `Address` object are cloned. When we modify the address in `person2`, it does **not** affect the address in `person1`, because `person2` has its own copy of the `Address` object. This is a result of deep cloning.

## **Difference between Shallow Cloning and Deep Cloning:**

![](https://db4ci98k88vxrf.archive.ph/taCf2/79501bb585c1eec6fc79c938cac07f21bb1a95ae.webp)

## **6. Mention some of the Java 8 features. Don’t explain.**

Below are some of the important Java 8 features:

1. **Lambda Expressions**: Introduced functional programming with concise syntax.
2. **Functional Interfaces**: Interfaces with a single abstract method, like `Predicate`, `Function`, and `Consumer`.
3. **Streams API**: Enables functional-style operations on collections with methods like `filter()`, `map()`, and `collect()`.
4. **Default and Static Methods**: Allows interfaces to have method implementations.
5. **Optional Class**: Helps handle null values and avoid `NullPointerException`.
6. **Date and Time API**: Introduces modern date-time handling with `LocalDate`, `LocalTime`, and more.
7. **Method References**: Simplifies lambdas by directly referencing methods (e.g., `ClassName::methodName`).
8. **Collectors Utility**: Provides utilities to transform and group data in streams.

## **7. What is a Consumer?**

A **Consumer** is a functional interface introduced in Java 8 as part of the `java.util.function` package. It represents an operation that accepts a single input argument and performs an action on it but does not return any result.

## **Characteristics:**

- It is a functional interface with a single abstract method:

```
void accept(T t);
```

- It is commonly used in functional programming and stream operations for performing actions like printing, logging, or modifying elements.

## **Example:**

```
import java.util.function.Consumer;

public class ConsumerExample {
    public static void main(String[] args) {
        Consumer<String> printConsumer = message -> System.out.println("Message: " + message);
        printConsumer.accept("Hello, World!");
    }
}
```

**Output:**

```
Message: Hello, World!
```

## **Using Consumer with Streams**

```
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class ConsumerStreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        Consumer<Integer> print = num -> System.out.println("Number: " + num);
        numbers.forEach(print);
    }
}
```

**Output:**

```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

## **Method Chaining with `andThen()`**

The `Consumer` interface provides a default method `andThen()` to chain multiple `Consumer` actions.

## **Example:**

```
import java.util.function.Consumer;

public class ConsumerChainingExample {
    public static void main(String[] args) {
        Consumer<String> toUpperCase = str -> System.out.println(str.toUpperCase());
        Consumer<String> appendExclamation = str -> System.out.println(str + "!");

        Consumer<String> combinedConsumer = toUpperCase.andThen(appendExclamation);
        combinedConsumer.accept("hello");
    }
}
```

**Output:**

```
HELLO
hello!
```

## **Use Cases**

- Logging each element in a collection.
- Modifying or performing side-effects on objects.
- Writing concise, reusable code in stream pipelines.

`Consumer` is especially useful when you need an operation that consumes data but doesn’t produce a result.

## **8. How to create a Thread in Java. Explain the thread life cycle.**

There are two primary ways to create a thread in Java:

## **1. Extending the `Thread` Class**

- Create a class that extends `Thread`.
- Override the `run()` method to define the task the thread should perform.

Example:

```
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread is running.");
    }
}

public class ThreadExample {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // Starts the thread
    }
}
```

## **2. Implementing the `Runnable` Interface**

- Create a class that implements the `Runnable` interface.
- Define the task in the `run()` method.
- Pass an instance of this class to a `Thread` object.

**Example:**

```
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Thread is running.");
    }
}

public class RunnableExample {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start(); // Starts the thread
    }
}
```

## **3. Using Lambda Expressions**

- Simplifies thread creation by using a lambda expression with the `Runnable` interface and is not a separate way in itself.
- It’s a syntactic enhancement introduced in Java 8 to make working with `Runnable` more concise and readable.

**Example:**

```
public class LambdaThreadExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> System.out.println("Thread is running."));
        thread.start(); // Starts the thread
    }
}
```

## **Thread Life Cycle**

The life cycle of a thread in Java involves the following states:

![](https://db4ci98k88vxrf.archive.ph/taCf2/50efe7a734464056894e78c9b65244104599217d.webp)

## **1. New**

- When a thread object is created but not yet started.
- Code: `Thread t = new Thread();`

## **2. Runnable**

- When the `start()` method is called, the thread enters the **Runnable** state.
- The thread is ready to run but waiting for the CPU to schedule it.

## **3. Running**

- The thread enters the **Running** state when the CPU assigns it time for execution.
- The `run()` method executes during this state.

## **4. Blocked/Waiting**

- A thread enters this state when it is waiting for a resource or another thread to signal it.
- Example:
- `sleep()` method.
- Waiting for I/O operations.
- Explicit locks or synchronization.

## **5. Terminated (Dead)**

- Once the `run()` method finishes or the thread is stopped, it moves to the **Terminated** state.
- The thread cannot be restarted.

## **Example:**

```
public class ThreadLifeCycleExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            System.out.println("Thread is running...");
            try {
                Thread.sleep(1000); // Thread goes to Waiting/Blocked state
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted.");
            }
            System.out.println("Thread is terminating...");
        });

        System.out.println("Thread state: " + thread.getState()); // NEW

        thread.start();

        System.out.println("Thread state: " + thread.getState()); // RUNNABLE

        try {
            Thread.sleep(500); // Allow thread to execute
            System.out.println("Thread state: " + thread.getState()); // TIMED_WAITING
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        try {
            thread.join(); // Wait for thread to finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Thread state: " + thread.getState()); // TERMINATED
    }
}
```

## **9. What is a deadlock and how to avoid it?**

A **deadlock** occurs in a multi-threaded environment when two or more threads are blocked forever, waiting for each other to release resources. It usually happens when multiple threads hold some resources and attempt to acquire resources held by others, creating a circular dependency.

## **Example:**

```
public class DeadlockExample {
    private static final Object lock1 = new Object();
    private static final Object lock2 = new Object();

    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock 1...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock2) {
                    System.out.println("Thread 1: Acquired lock 2.");
                }
            }
        });
        Thread thread2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock 2...");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock1) {
                    System.out.println("Thread 2: Acquired lock 1.");
                }
            }
        });
        thread1.start();
        thread2.start();
    }
}
```

## **Output:**

Both threads are stuck indefinitely:

```
Thread 1: Holding lock 1...
Thread 2: Holding lock 2...
```

## **How to Avoid Deadlock**

Here are some strategies to avoid deadlock:

## **1. Avoid Nested Locks**

- Minimize synchronized blocks or avoid acquiring multiple locks at once.
- **Example**:

```
synchronized (lock1) {
     // Critical section
}
synchronized (lock2) {
 // Another critical section
}
```

## **2. Lock Ordering**

- Always acquire locks in a consistent, predefined order to prevent circular waiting.
- Example:

```
synchronized (lock1)
{
     synchronized (lock2) {
         // Critical section
                           }
}
```

## **3. Use Try-Lock**

- Use `ReentrantLock` with a `tryLock()` method to acquire locks without blocking indefinitely.
- **Example**:

```
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class AvoidDeadlock {
    private static final Lock lock1 = new ReentrantLock();
    private static final Lock lock2 = new ReentrantLock();

    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            if (lock1.tryLock()) {
                try {
                    System.out.println("Thread 1: Acquired lock 1");
                    if (lock2.tryLock()) {
                        try {
                            System.out.println("Thread 1: Acquired lock 2");
                        } finally {
                            lock2.unlock();
                        }
                    }
                } finally {
                    lock1.unlock();
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            if (lock2.tryLock()) {
                try {
                    System.out.println("Thread 2: Acquired lock 2");
                    if (lock1.tryLock()) {
                        try {
                            System.out.println("Thread 2: Acquired lock 1");
                        } finally {
                            lock1.unlock();
                        }
                    }
                } finally {
                    lock2.unlock();
                }
            }
        });

        thread1.start();
        thread2.start();
    }
}
```

## **4. Timeout for Threads**

- Set time limits for acquiring locks or resources to avoid indefinite waiting.

## **5. Avoid Unnecessary Locks**

- Use synchronized blocks or locks only when absolutely necessary.

## **6. Deadlock Detection**

- Use tools like thread dump analyzers to detect deadlocks during runtime.

## **10. What are S.O.L.I.D principles in Java?**

The S.O.L.I.D principles are a set of five design principles that promote good software design, improve maintainability, and make the code more robust and flexible.

These principles form the foundation of **object-oriented programming** and are widely used in Java.

## **1. Single Responsibility Principle (SRP)**

A class should have only **one reason to change**, meaning it should only have one responsibility or functionality.

- **Explanation:** A class should focus on a single task and encapsulate it fully. This makes the code easier to understand, modify, and test.
- **Example:**

```
class Invoice {
    public void calculateTotal() {
        // Logic to calculate the total amount
    }
}

class InvoicePrinter {
    public void printInvoice(Invoice invoice) {
        // Logic to print the invoice
    }
}
```

- **Why:** The `Invoice` class focuses only on calculations, while the `InvoicePrinter` handles printing.

## **2. Open/Closed Principle (OCP)**

Software entities (classes, modules, functions) should be **open for extension** but **closed for modification**.

- **Explanation:** You should be able to add new functionality to a class without altering its existing code.
- **Example:**

```
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing Circle");
    }
}

class Rectangle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing Rectangle");
    }
}

public class OCPDemo {
    public static void main(String[] args) {
        Shape shape1 = new Circle();
        Shape shape2 = new Rectangle();
        shape1.draw();
        shape2.draw();
    }
}
```

- **Why:** Adding a new shape (e.g., `Triangle`) doesn’t require modifying existing code, just extending `Shape`.

## **3. Liskov Substitution Principle (LSP)**

Subtypes must be substitutable for their base types without affecting the correctness of the program.

- **Explanation:** A derived class should extend the functionality of the base class without changing its behavior.
- **Example:**

```
class Bird {
    public void fly() {
        System.out.println("Flying");
    }
}

class Sparrow extends Bird {}

class Ostrich extends Bird {
    @Override
    public void fly() {
        throw new UnsupportedOperationException("Ostriches can't fly!");
    }
}
```

- **Violation:** The `Ostrich` class violates LSP because it breaks the expectation that all birds can fly. Instead, redesign the hierarchy.

## **4. Interface Segregation Principle (ISP)**

A class should not be forced to implement methods it does not use.

- **Explanation:** Split large interfaces into smaller, more specific ones so that implementing classes only need to concern themselves with relevant methods.
- **Example:**

```
interface Printer {
    void print();
}

interface Scanner {
    void scan();
}

class AllInOnePrinter implements Printer, Scanner {
    public void print() {
        System.out.println("Printing...");
    }

    public void scan() {
        System.out.println("Scanning...");
    }
}

class SimplePrinter implements Printer {
    public void print() {
        System.out.println("Printing...");
    }
}
```

- **Why:** A simple printer doesn’t need to implement unnecessary `scan()` functionality.

## **5. Dependency Inversion Principle (DIP)**

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

- **Explanation:** This promotes loose coupling and makes the system more flexible and maintainable.
- **Example:**

```
interface NotificationService {
    void sendNotification(String message);
}

class EmailService implements NotificationService {
    public void sendNotification(String message) {
        System.out.println("Sending Email: " + message);
    }
}

class SMSService implements NotificationService {
    public void sendNotification(String message) {
        System.out.println("Sending SMS: " + message);
    }
}

class NotificationManager {
    private NotificationService service;

    public NotificationManager(NotificationService service) {
        this.service = service;
    }

    public void notifyUser(String message) {
        service.sendNotification(message);
    }
}

public class DIPDemo {
    public static void main(String[] args) {
        NotificationService emailService = new EmailService();
        NotificationManager manager = new NotificationManager(emailService);
        manager.notifyUser("Welcome to S.O.L.I.D principles!");
    }
}
```

- **Why:** The `NotificationManager` depends on the abstraction `NotificationService`, not concrete implementations.

## **Benefits of S.O.L.I.D Principles**

- Promotes modularity and reusability.
- Improves maintainability and scalability.
- Makes the code easier to test and debug.
- Encourages following best practices in object-oriented design.

## **11. How do you decide if you have to choose a Set or List?**

**Choose Set when:**

- You need to ensure uniqueness.
- Performance for lookups is critical.

**Choose List when:**

- You need to maintain order.
- You require duplicates.
- You need to access elements by index.

## **12. How do you monitor health of your Spring Boot application?**

To monitor the health of a Spring Boot application, I would use **Spring Boot Actuator**, which provides production-ready features like health checks, metrics, and other useful endpoints.

## **1. Enable Spring Boot Actuator**

First, I would add the `spring-boot-starter-actuator` dependency to the `pom.xml`:

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

## **2. Expose Health Endpoint**

Spring Boot Actuator automatically exposes a `/actuator/health` endpoint that provides the current health status of the application. By default, this will return a simple status:

```
{
    "status": "UP"
}
```

For more detailed health data, I can configure additional checks for databases, caches, etc., and expose all actuator endpoints by adding the following in `application.properties`:

```
management.endpoints.web.exposure.include=health,metrics,info
```

## **3. Custom Health Checks**

Spring Boot provides default health indicators for common services like databases, caches, and file systems. However, I can implement **custom health checks** by implementing the `HealthIndicator` interface. For example:

```
@Component
public class CustomHealthIndicator implements HealthIndicator {

@Override
    public Health health() {
        if (/* some condition */) {
            return Health.up().withDetail("Custom Service", "Running").build();
        }
        return Health.down().withDetail("Custom Service", "Down").build();
    }
}
```

This custom check will be included in the `/actuator/health` response.

## **4. Securing the Health Endpoint**

For production environments, it’s important to secure health data. Spring Security can be used to secure endpoints. Here’s an example of securing the `/actuator/health` endpoint:

```
spring.security.user.name=admin
spring.security.user.password=admin
```

This ensures that only authorized users can access sensitive health information.

## **5. Integration with External Monitoring Tools**

Spring Boot Actuator can be integrated with monitoring tools like **Prometheus**, **Grafana**, or **Datadog** to get more detailed metrics and visualizations. For instance, to integrate Prometheus:

1. Add the Prometheus registry dependency:

```
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

2. Expose Prometheus metrics via the `/actuator/prometheus` endpoint.

This way, metrics like JVM performance, request counts, and response times can be scraped and visualized in Grafana.

## **6. Alerts**

Finally, I would configure **alerts** to be notified of any health changes. Tools like **Prometheus Alertmanager** or **Grafana Alerts** can trigger notifications if the application health goes down or if certain thresholds are breached.

## **13. When to use application.properties file vs application.yaml file?**

Both `application.properties` and `application.yaml` are configuration files used in Spring Boot to configure the application’s properties. They serve the same purpose, but the format and the way they’re structured differ.

- **`application.properties`**: A traditional, simple key-value pair format.
- **`application.yaml` (or `application.yml`)**: A hierarchical data format, typically used for more complex configurations, where readability and structured data are important.

## **When to Use `application.properties`**

- **Simplicity**: If the application has simple configurations with a flat structure (e.g., one-level properties), using `application.properties` can be easier to manage.
- **Familiarity**: If the team is more familiar with the `.properties` format or working on legacy systems, it's often more convenient to stick to `application.properties`.
- **Java-based Configuration**: If the project relies heavily on Java-based configurations or other properties that require simple key-value pairs (e.g., logging levels, database configurations), `.properties` is a natural choice.
- **Legacy Systems**: For older projects or frameworks that are commonly used with `.properties` files (e.g., Spring 2.x or Java EE), sticking with `.properties` may help maintain consistency with the existing codebase.

## **When to Use `application.yaml`**

- **Complex, Structured Data**: When your configuration requires nested or hierarchical structures (e.g., lists, maps, or nested objects), `application.yaml` provides a more natural, readable structure.

Example of nested structure in `application.yaml`:

```
server:
  port: 8080
  ssl:
    enabled: true
    key-store: classpath:keystore.jks
```

- **Readability**: YAML is more human-readable, especially for more complex configurations. It supports indentation-based hierarchy, which makes it easier to understand and manage.
- **Multi-Environment Configurations**: When managing different environments (e.g., dev, prod), YAML files are often preferred because they make the structure clearer. With properties files, multiple files or profile-based property inclusion are often necessary.

Example of multiple profiles in `application.yaml`:

```
spring:
  profiles:
    active: dev
---
spring:
  profiles: dev
  datasource:
    url: jdbc:mysql://localhost:3306/dev_db
---
spring:
  profiles: prod
  datasource:
    url: jdbc:mysql://localhost:3306/prod_db
```

- **Advanced Features**: YAML can also be used to define more advanced Spring Boot features like multi-level configuration properties, property resolution (e.g., `@Value` injection), and more, in a way that's more flexible than `.properties`.

## **14. What is an API gateway?**

An **API Gateway** is a server that acts as an entry point for client requests to access various services in a microservices architecture.

It functions as a reverse proxy, routing client requests to the appropriate microservices, aggregating the results, and providing a unified response. API Gateways help centralize common functionality like authentication, load balancing, rate limiting, and logging, reducing the complexity of managing multiple services directly.

## **Functions:**

1. **Request Routing**: The API Gateway routes incoming client requests to the appropriate backend services based on the URL and request type.
2. **Aggregation**: It can aggregate responses from multiple microservices into a single response for the client, improving the efficiency and reducing the number of client-server interactions.
3. **Authentication and Authorization**: The API Gateway can handle authentication and authorization for incoming requests, acting as a security layer before passing the request to backend services.
4. **Rate Limiting and Throttling**: The gateway can manage the rate of requests and throttle requests to prevent service overloads, ensuring that the system operates within capacity limits.
5. **Load Balancing**: It can distribute incoming requests across multiple instances of a microservice, providing better scalability and fault tolerance.
6. **Caching**: To reduce the load on backend services, the API Gateway can cache responses for frequent or static requests, improving response times.
7. **Logging and Monitoring**: It centralizes logging and monitoring, tracking client requests, responses, and errors across services, which is useful for debugging and performance optimization.
8. **Fault Tolerance**: It can implement patterns like circuit breakers, retries, or timeouts to gracefully handle failures in downstream services.

## **When to Use an API Gateway:**

- **Microservices Architecture**: When your application is built using microservices, an API Gateway simplifies the interaction between clients and multiple backend services.
- **Complex Client Needs**: If clients need to make multiple service calls that need to be aggregated, an API Gateway helps by reducing the complexity on the client side.
- **Security Concerns**: It centralizes security features like authentication, authorization, and encryption, allowing backend services to remain isolated from direct access.

## **Advantages:**

- Simplifies client interactions by providing a single entry point.
- Centralizes cross-cutting concerns like security, logging, and monitoring.
- Reduces the need for clients to know about internal microservice architecture.
- Improves scalability and fault tolerance.

## **15. How do microservices communicate with each other?**

Microservices communicate with each other using different communication mechanisms, depending on the use case, the nature of the services, and performance requirements.

Here are the most common ways in which microservices communicate:

## **1. Synchronous Communication (HTTP/REST)**

**HTTP/REST APIs**: Microservices often communicate over HTTP using RESTful APIs. One service exposes an endpoint, and another service makes an HTTP request to that endpoint to retrieve data or perform an action. REST APIs are lightweight and easy to implement.

- **Advantages**:
- Simple and widely used.
- Language-agnostic, as any language with HTTP support can consume REST APIs.
- Flexible (supports different data formats like JSON, XML, etc.).

**gRPC**: An open-source, high-performance framework for building APIs using HTTP/2, gRPC is an alternative to REST. It allows for more efficient communication with better performance, support for bi-directional streaming, and built-in features like authentication and load balancing.

- **Advantages**:
- Faster and more efficient than REST (binary protocol, HTTP/2).
- Supports features like bidirectional streaming and multiplexing.

## **2. Asynchronous Communication (Messaging Systems)**

Asynchronous communication helps decouple services, making them more resilient and scalable. Messages are sent to a message broker, which handles the delivery of the messages to the appropriate service. This type of communication is suitable for event-driven architectures.

**Message Brokers (e.g., Kafka, RabbitMQ, ActiveMQ)**: Microservices can communicate asynchronously through a messaging system. One service sends messages to a message queue (e.g., RabbitMQ, ActiveMQ) or a distributed event stream (e.g., Kafka), and the other services listen to those messages or events and act accordingly.

- **Advantages**:
- Decouples services, enabling them to work independently and scale better.
- Services can process messages when they are ready, improving fault tolerance and responsiveness.
- Provides a natural way to implement event-driven architectures.

**Event-Driven Communication**: Microservices can communicate using events, where one service emits an event (e.g., “OrderCreated”), and other services listen and react to these events. This is a popular method in systems that require loose coupling and scalability.

- **Advantages**:
- Helps build more loosely coupled, scalable, and fault-tolerant systems.
- Suitable for systems that need to handle large volumes of events (e.g., IoT or e-commerce systems).

## **3. Service Discovery**

In a microservices architecture, services may be dynamic, where instances come and go frequently. Service discovery helps microservices find each other dynamically at runtime.

- **Eureka**: A service registry from Netflix, which helps microservices discover each other. Services register themselves with Eureka, and other services can query the registry to find available instances.
- **Consul**: Another service discovery tool that allows microservices to register and discover each other. It also supports health checks to ensure services are available.

## **4. Remote Procedure Call (RPC)**

RPC is a communication method where one service calls a function or method of another service, which can be on a different machine.

- **JSON-RPC / XML-RPC**: These protocols are a simpler form of RPC where the client sends data in JSON or XML format to invoke methods on a remote service.
- **gRPC** (mentioned earlier): A modern, efficient, and language-agnostic RPC framework that uses Protocol Buffers for message serialization, allowing services to communicate with high performance.

## **5. API Gateway for Aggregation**

An **API Gateway** acts as an entry point for clients to interact with multiple microservices. It can aggregate responses from multiple services and return a unified response to the client.

- This helps centralize communication for complex systems, especially when multiple microservices are needed to fulfill a single client request.

## **6. Circuit Breakers**

To handle failures in microservices communication, patterns like **Circuit Breakers** are used. A Circuit Breaker (e.g., **Hystrix**) helps in preventing a failure in one service from cascading to other services by detecting failures and temporarily stopping communication to avoid overloading the failing service.

***The choice of communication method depends on the system’s requirements, such as real-time needs, fault tolerance, and scalability.***

## **16. What is a stored procedure?**

A **stored procedure** is a precompiled collection of one or more SQL statements that are stored in a database.

Stored procedures can be executed by the database engine to perform specific tasks such as querying, inserting, updating, or deleting data.

These procedures are written in SQL (or a procedural extension of SQL like PL/SQL in Oracle or T-SQL in SQL Server), and they are stored directly in the database for repeated use.

## **Benefits:**

- **Performance**: Since they are precompiled, stored procedures can be faster than executing individual SQL queries directly, especially for complex queries.
- **Code Reusability**: Complex logic or frequently used queries can be encapsulated in a stored procedure and reused throughout the application.
- **Maintainability**: Changes to the business logic need to be made only in the stored procedure, making it easier to maintain and update.
- **Security**: Users can be given permission to execute a stored procedure without needing access to the underlying tables, reducing the risk of unauthorized data manipulation.

## **Example:**

```
CREATE PROCEDURE GetEmployeeInfo
    @EmployeeID INT
AS
BEGIN
    SELECT FirstName, LastName, Department
    FROM Employees
    WHERE EmployeeID = @EmployeeID;
END;
```

This stored procedure accepts an `EmployeeID` as an input parameter and retrieves the corresponding employee's first name, last name, and department from the `Employees` table.

## **How to Call a Stored Procedure:**

```
EXEC GetEmployeeInfo @EmployeeID = 1;
```

This command executes the `GetEmployeeInfo` procedure, passing `1` as the `EmployeeID` to get the corresponding employee details.

## **Types of Stored Procedures:**

1. **Stored Procedures with Input Parameters**: Accept parameters that are passed when the procedure is called.
2. **Stored Procedures with Output Parameters**: Return values back to the calling application.
3. **Stored Procedures without Parameters**: Perform a set of actions but don’t accept or return any parameters.

## **17. What is a trigger?**

A **trigger** is a special type of stored procedure in a database that automatically executes in response to certain events, such as an `INSERT`, `UPDATE`, or `DELETE` operation on a table or view.

Below are some of it’s key points:

## **Event-Driven:**

- Triggers fire automatically when a specific event occurs on the database.

## **Types:**

- **BEFORE Trigger**: Runs before the event is performed (e.g., validating data before insertion).
- **AFTER Trigger**: Runs after the event is performed (e.g., logging data after insertion).
- **INSTEAD OF Trigger**: Replaces the action (used for custom behavior).

## **Use Cases:**

- **Enforcing Data Integrity**: Automatically checks or modifies data before or after changes.
- **Auditing/Logging**: Automatically logs changes to data for tracking or auditing purposes.
- **Cascading Changes**: Automatically updates related data when a change occurs.

## **Advantages:**

- Automates tasks like logging and maintaining integrity.
- Ensures consistent application of rules at the database level.

## **Disadvantages:**

- Can add complexity and performance overhead.
- Triggers’ behavior may be hidden from applications, making debugging harder.

Triggers provide a way to automate and enforce business rules directly in the database.

## **18. Can we have more than one primary key in a table?**

No, a table can have **only one primary key**.

The primary key in a table is a unique identifier for each record. While a table can have multiple **unique keys** or **unique constraints**, there can only be **one primary key**. The primary key enforces both **uniqueness** and **not null** constraints on the column(s) it is defined on.

However, a primary key can consist of **multiple columns** — this is called a **composite primary key**. But even in this case, there is still only one primary key for the table, which involves multiple columns.

## **Example:**

If you have a table `Orders`, you can define a composite primary key on two columns, like `order_id` and `product_id`, which together uniquely identify a record.

```
CREATE TABLE Orders (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
```

In this case, `order_id` and `product_id` together form the primary key, but it's still a single primary key for the table.

## **19. What is the purpose of JOIN and UNION?**

JOIN and UNION are both used to combine data from multiple tables in SQL, but they serve different purposes and work in distinct ways.

## **JOIN:**

A **JOIN** is used to combine columns from two or more tables based on a related column between them. It allows you to retrieve related data from multiple tables in a single query.

- **Purpose**: To retrieve data from multiple tables by matching rows based on common columns.

**Types of JOINs:**

- **INNER JOIN**: Returns rows when there is a match in both tables.
- **LEFT JOIN (or LEFT OUTER JOIN)**: Returns all rows from the left table and matching rows from the right table (if any). If no match is found, NULLs are returned for columns from the right table.
- **RIGHT JOIN (or RIGHT OUTER JOIN)**: Similar to LEFT JOIN, but returns all rows from the right table and matching rows from the left table.
- **FULL JOIN (or FULL OUTER JOIN)**: Returns all rows when there is a match in one of the tables. Non-matching rows will have NULLs in columns from the table that doesn’t have a match.
- **CROSS JOIN**: Returns the Cartesian product of the two tables (i.e., every row from the first table is combined with every row from the second table).
- **Example** (INNER JOIN):

```
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN
customers ON orders.customer_id = customers.customer_id;
```

- This retrieves the `order_id` and `customer_name` by joining the `orders` and `customers` tables where the `customer_id` matches.

## **UNION:**

A **UNION** is used to combine the results of two or more **SELECT** queries into a single result set. It appends the results of one query to the results of another, but only includes distinct rows (duplicates are removed).

- **Purpose**: To combine results from two or more SELECT queries into a single result.
- **Key Points**:
- The number of columns and their data types in each SELECT statement must be the same.
- **UNION** removes duplicate rows by default.
- If you want to include duplicates, use **UNION ALL**.
- **Example** (UNION):

```
SELECT employee_name
FROM employees

UNION

SELECT customer_name
FROM customers;
```

- This combines the `employee_name` from the `employees` table and `customer_name` from the `customers` table into a single result set, removing duplicates.

## **Differences:**

- **JOIN** combines **columns** from multiple tables based on a related column.
- **UNION** combines **rows** from multiple result sets of separate queries.
- **JOIN** is used to merge data based on relationships, while **UNION** is used to combine the results of multiple SELECT queries into a single list of distinct rows.