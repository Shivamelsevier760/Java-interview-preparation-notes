# Medium interview company questions part 2

# **Barclays Java Spring-Boot Micro-service Interview Question with answer 2024**

## **How HashMap Works internally?**

HashMap is Hash table based implementation of the `Map` interface. This implementation provides all of the optional map operations, and permits `null` values and the `null` key. (The `HashMap` class is roughly equivalent to `Hashtable`, except that it is unsynchronized and permits nulls.) This class makes no guarantees as to the order of the map; in particular, it does not guarantee that the order will remain constant over time.

![](https://ddfx29dm3fys07.archive.ph/H1nNz/1ed6180edbaa64b2a1a6244a068f7c1ee5e0f8fe.webp)

***Here is the working:***

- Java HashMap allows null key and null values.
- HashMap is not an ordered collection. You can iterate over HashMap entries through keys set but they are not guaranteed to be in the order of their addition to the HashMap.
- HashMap is almost similar to Hashtable except that it’s unsynchronized and allows null key and values.
- HashMap uses it’s inner class Node<K,V> for storing map entries.
- HashMap stores entries into multiple singly linked lists, called buckets or bins. Default number of bins is 16 and it’s always power of 2.
- HashMap uses hashCode() and equals() methods on keys for get and put operations. So HashMap key object should provide good implementation of these methods. This is the reason immutable classes are better suitable for keys, for example String and Interger.
- Java HashMap is not thread safe, for multithreaded environment you should use ConcurrentHashMap class or get synchronized map using Collections.synchronizedMap() method.

## **Difference between Put and Post?**

.The PUT method is typically used to create resources if they don’t exist and update them if they do, while the POST method is primarily used only for creating new resources.

![](https://ddfx29dm3fys07.archive.ph/H1nNz/82cd614f4b1d9d3fc28b5df4c5c259402baa9989.webp)

*Note — In Java Interview always expect one question from HTTP methods like put vs post and so on.*

## **Write a program to reverse the array of string without using predefined method?**

Basically, Interviewer wants to know if you can write code manually apart from using existing Java API to do this.

```
public class ReverseArrayWithoutPredefinedMethod {

    public static void main(String[] args) {
        // Sample array of strings
        String[] array = {"apple", "banana", "orange", "grape"};

        // Printing original array
        System.out.println("Original array:");
        printArray(array);

        // Reversing the array
        reverseArray(array);

        // Printing reversed array
        System.out.println("\nReversed array:");
        printArray(array);
    }

    // Method to reverse the array of strings
    public static void reverseArray(String[] arr) {
        int start = 0;
        int end = arr.length - 1;

        // Swap elements from start to end until mid is reached
        while (start < end) {
            // Swapping elements
            String temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            // Moving pointers towards the center
            start++;
            end--;
        }
    }

    // Method to print the array of strings
    public static void printArray(String[] arr) {
        for (String s : arr) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
}
```

Similarly there might be one more question on this, Reverse a string without using Java API or any Reverse methods.

## **Difference between comparable and comparator?**

The most fundamental difference between Comparable and Comparator in Java is the number of sorting sequences they support:

- **Comparable:** Supports a **single sorting sequence** based on the object’s natural ordering (often defined by a single field).
- **Comparator:** Offers the ability to define **multiple sorting sequences** based on your custom logic, potentially using multiple fields for comparison.

**Comparable:**

- Defines a natural ordering for a class’s objects.
- Implemented by the class itself using the `compareTo(Object o)` method.
- This method returns a negative integer if the current object is less than the argument (`o`), zero if they are equal, and a positive integer if the current object is greater.
- Only allows sorting based on a single aspect (natural ordering) of the class.

**Comparator:**

- Provides a separate way to define sorting logic for objects.
- Implemented in a separate class or as an anonymous inner class.
- Uses the `compare(Object o1, Object o2)` method to compare two objects and return a negative integer if the first is less than the second, zero if they are equal, and a positive integer if the first is greater.
- Offers flexibility for defining custom sorting criteria on various object attributes.

## **What is jdbctemplate ,statement,preparedstatement ,callable statement?**

JDBC (Java Database Connectivity) provides interfaces for interacting with relational databases in Java. Here’s a breakdown of the key concepts you mentioned:

**JdbcTemplate (from frameworks like Spring):**

- JdbcTemplate is a helper class that simplifies working with JDBC APIs.
- It abstracts away boilerplate code related to creating connections, statements, and handling exceptions.
- You can use it to execute SQL queries and updates with features like prepared statements and parameter binding.

**Statement:**

- The `Statement` interface is the most basic way to execute SQL statements.
- You can create a `Statement` object from a `Connection` object.
- It allows you to execute various SQL statements like SELECT, INSERT, UPDATE, and DELETE.
- However, `Statement` has limitations:
- It cannot accept parameters directly in the SQL string, making it vulnerable to SQL injection attacks.
- It’s less efficient for repeated executions of the same query with different data.

**PreparedStatement:**

- `PreparedStatement` is an extension of `Statement` that addresses the limitations mentioned above.
- You create a `PreparedStatement` object by providing a pre-compiled SQL template with placeholders for parameters (represented by '?').
- You then set the values for these parameters using setter methods before executing the statement.
- This separation of query and data improves security (prevents SQL injection) and performance (avoids recompiling the same query repeatedly).

**CallableStatement:**

- `CallableStatement` is another extension of `Statement` specifically designed for calling stored procedures in a database.
- Stored procedures are pre-written SQL code blocks stored in the database that can be executed and potentially return results or modify data.
- `CallableStatement` allows you to define parameters for the stored procedure (both input and output parameters) and execute the call.

## **What are these annotations @Component and @Autowired annotation?**

These annotations are fundamental concepts in Spring Framework for dependency injection and managing beans. Here’s a breakdown of their roles:

**@Component**

- A stereotype annotation that marks a class as a Spring bean.
- Spring scans your project for classes annotated with `@Component` (or its specialized variants like `@Controller`, `@Service`, or `@Repository`) during application startup.
- These classes are then managed by the Spring container, meaning Spring will:
- Instantiate them.
- Inject any required dependencies into them (using `@Autowired`).
- Make them available for autowiring in other beans.

**@Autowired**

- Used to inject dependencies into a bean managed by Spring.
- You can mark fields, setter methods, or constructor arguments with `@Autowired`.
- Spring will automatically find a compatible bean in the Spring application context and inject it into the field/method/constructor.
- This simplifies dependency injection by removing the need for manual bean creation and wiring.

**Relationship between @Component and @Autowired:**

- `@Component` marks a class as a bean that Spring manages.
- `@Autowired` injects dependencies (other Spring-managed beans) into these beans.

**In essence:**

- `@Component` is like saying "This class is a bean I want Spring to manage."
- `@Autowired` is like saying "Spring, please inject the required bean dependency here."

**Additional Points:**

- By default, Spring scans the base package where your main application class is located for components. You can customize this behavior using `@ComponentScan` annotation.
- There are different ways to configure autowiring behavior using qualifiers if you have multiple beans of the same type.

## **What is SQL Injection?**

SQL injection (SQLi) is a dangerous web security vulnerability. Attackers can exploit it to steal, modify, or even delete data from your database.

Imagine a web form where users enter data. If the application doesn’t properly handle that data (sanitize it), attackers can inject malicious SQL code disguised as normal input. This code then gets executed by the database, potentially causing havoc.

To prevent SQLi, follow these security measures:

- Validate user input to make sure it’s what you expect.
- Use special techniques (prepared statements) to separate user input from the actual SQL query.
- Consider using stored procedures for complex queries.
- Keep your software updated with the latest security patches.

By taking these steps, you can make your web application much more secure against SQL injection attacks.

## **What is session and sessionfactory in Hibernate?**

In Hibernate, which is an object-relational mapper (ORM) framework for Java, `Session` and `SessionFactory` play crucial roles in interacting with your database:

**SessionFactory:**

- **Factory for Sessions:** Think of it as a factory that creates `Session` objects. There's typically one `SessionFactory` per application.
- **Configuration:** It encapsulates the Hibernate configuration details like database connection information, dialect, and mappings between your Java classes and database tables.
- **Long-lived:** A `SessionFactory` is created during application startup and remains available throughout the application's lifecycle. It's thread-safe for concurrent access.
- **Benefits:**
- Manages connection pooling for efficient database access.
- Caches information about database schema and mappings, improving performance.

**Session:**

- **Database Interaction:** Represents a single unit of work (transaction) with the database. You use a `Session` to perform CRUD (Create, Read, Update, Delete) operations on your persistent objects.
- **Short-lived:** A `Session` is typically created, used for a specific task (transaction), and then closed to release resources. It's not thread-safe and should not be shared between threads.
- **Functionality:** Provides methods for:
- Saving, updating, and deleting persistent objects.
- Retrieving data from the database using queries.
- Managing transactions (commit or rollback changes).
- **First-Level Cache:** Maintains a temporary cache of recently accessed objects within the `Session` itself, improving performance for repetitive operations.

## **What is HQL?**

HQL stands for Hibernate Query Language. In a nutshell, it’s a special query language designed for Hibernate, a popular object-relational mapper (ORM) framework in Java. Here’s the gist:

- **Focuses on objects:** HQL lets you write queries using the names of your Java classes and their properties instead of raw database tables and columns. This makes it more readable and less prone to errors compared to writing pure SQL.
- **Behind the scenes translation:** When you execute an HQL query, Hibernate translates it into the corresponding SQL statement for your underlying database. This frees you from worrying about the specifics of different database dialects.

So, HQL provides a convenient and object-oriented way to interact with your database through Hibernate.

## **What are Joins?**

joins are a fundamental concept for combining data from multiple tables. They allow you to retrieve related information from different tables based on a shared field. Imagine you have a database for an online store:

- One table (`customers`) stores customer information like names and IDs.
- Another table (`orders`) stores details about orders, including the customer ID (linking it to the `customers` table).

To get a complete picture, you might want to combine customer details with their corresponding orders. This is where joins come in.

Here are the different types of joins you can use to achieve various results:

- **Inner Join:** This is the most common type. It returns only rows where there’s a match in both tables based on the join condition. For example, you could retrieve customer names and their corresponding order details.
- **Left Join:** This includes all rows from the left table (the one you specify first), and matching rows from the right table. Rows from the right table with no match on the join condition will have null values for the joined columns.
- **Right Join:** Similar to a left join, but it includes all rows from the right table and matching rows from the left table. Unmatched rows in the left table will have null values.
- **Full Join:** This combines all rows from both tables, regardless of whether there’s a match in the join condition. Unmatched rows will have null values in the corresponding columns.

## **What is the difference between Primary and Foreign key?**

Both primary keys and foreign keys are crucial for maintaining data integrity and relationships within relational databases, but they serve distinct purposes:

![](https://ddfx29dm3fys07.archive.ph/H1nNz/c04160b458a1f30b971396c9a8c32639f7c1868e.gif)

**Primary Key:**

- **Uniqueness:** Ensures each row in a table has a unique identifier. This prevents duplicate records and allows for efficient data retrieval.
- **Single Key:** A table can only have one primary key. It’s typically composed of one or more columns that uniquely identify a row.
- **Not Null:** Primary key columns generally don’t allow null values. This guarantees that every row has a distinct identifier.
- **Example:** In a `customers` table, the primary key could be a `customer_id` column, ensuring no two customers have the same ID.

**Foreign Key:**

- **Relationship Builder:** Establishes a link between two tables. It references the primary key of another table (parent table).
- **Multiple Keys:** A table can have multiple foreign keys, each referencing a different primary key in other tables.
- **Can be Null:** Foreign key columns can allow null values, indicating a record that doesn’t have a corresponding entry in the referenced table (parent table).
- **Example:** In an `orders` table, a `customer_id` foreign key might reference the primary key (`customer_id`) of the `customers` table, linking each order to a specific customer.

## **What is REST-API?**

REST API (or RESTful API) stands for Representational State Transfer API. It’s a popular architectural style for designing web APIs. In short, it defines a set of rules for how APIs communicate using HTTP requests and responses. This allows applications to easily interact with each other in a standardized way, regardless of the programming language used. Imagine it as a universal language for applications to exchange information over the web.

## **When to use Encapsulation and Abstraction in your project?**

Encapsulation and abstraction are fundamental concepts in object-oriented programming (OOP) that promote code reusability, maintainability, and security. Here’s a breakdown of when to use them in your project:

**Encapsulation:**

- **Data Hiding and Protection:** Use encapsulation when you want to control access to an object’s internal data (attributes). By making attributes private and providing public methods (getters and setters) to access and modify them, you can ensure data integrity and prevent unintended modifications.
- **Example:** In a `Bank` class, you might want to encapsulate the `accountBalance` attribute to ensure it's only accessed and modified through appropriate methods like `deposit` and `withdraw`.

**Abstraction:**

- **Focus on Functionality:** Use abstraction to hide the implementation details of a class and expose only the essential functionality through interfaces or abstract classes. This allows users to interact with the object without worrying about the underlying complexities.
- **Example:** Consider a `Shape` interface with methods like `calculateArea` and `draw`. Different concrete shapes (like `Circle` or `Square`) can implement this interface, providing their specific implementations for these methods. Users can then interact with all shapes using the same interface methods, without needing to know the specifics of each shape's implementation.

**In essence:**

- Use encapsulation to protect an object’s internal state and control access to its data.
- Use abstraction to focus on the “what” (functionality) rather than the “how” (implementation details) of an object.

## **Explain Lazy Loading and Eager Loading?**

Lazy loading and eager loading are two strategies for fetching data in object-relational mapping (ORM) frameworks like Hibernate. They determine when and how related entities (objects) are loaded from the database.

**Lazy Loading:**

- **Delays Loading:** Data is retrieved only when it’s explicitly needed. Imagine a product listing page that displays basic product details (name, price) initially. Lazy loading ensures related information like product descriptions or reviews are loaded only when the user clicks on a specific product.
- **Performance Benefits:** By avoiding unnecessary database queries for data that might not be used, lazy loading can improve initial page load times.
- **Potential for Extra Queries:** If you do end up needing the related data, lazy loading will trigger additional database queries, which might add some overhead.

**Eager Loading:**

- **Loads Everything Upfront:** All related data is fetched along with the primary object in a single database query. This means all product details (description, reviews) might be loaded on the initial product listing page, even if the user doesn’t view them all.
- **Faster Access to Related Data:** Since the data is already available, accessing related information doesn’t require additional database queries, potentially improving performance for scenarios where you need to use most or all of the related data.
- **Potentially Slower Initial Load:** Eager loading can lead to slower initial page load times if you’re fetching a lot of data that might not be immediately needed.

## **When to use these annotation in your project — @GetMapping and @PostMapping?**

Here’s a breakdown of when to use `@GetMapping` and `@PostMapping` annotations in your Spring MVC projects:

**@GetMapping**

- Use this annotation for methods that handle HTTP GET requests. These requests are typically used to retrieve data from the server.
- **Common Use Cases:**
- Fetching a list of resources (e.g., `/products`)
- Getting details of a specific resource (e.g., `/products/{id}`)
- Handling searches or filtering requests (e.g., `/products?category=electronics`)

```
@Controller
public class ProductController {

    @GetMapping("/products")
    public List<Product> getAllProducts() {
        // Logic to retrieve all products from the database
    }
}
```

**@PostMapping**

- Use this annotation for methods that handle HTTP POST requests. These requests are typically used to submit data to the server for creation or update purposes.
- **Common Use Cases:**
- Creating a new resource (e.g., submitting a new product through a form)
- Updating an existing resource (e.g., editing product details)
- Deleting a resource (although DELETE is a more specific method for deletion)

```
@Controller
public class ProductController {

    @PostMapping("/products")
    public Product createProduct(@RequestBody Product product) {
        // Logic to save the new product to the database
    }
}
```

**Choosing Between GET and POST:**

- In general, use GET for retrieving data and POST for modifying data (creating, updating, or deleting).
- However, the specific choice might depend on your API design and the semantics of the operation.

## **What is Exception Handling rule for Method Overriding?**

Here are the key rules for exception handling when overriding methods in Java:

**Subclasses and Exceptions:**

- **Same or Subclass Exception:** When a superclass method declares a checked exception, the overriding method in the subclass can declare the same exception or a subclass of that exception. This allows for more specific exception handling in the subclass.

```
class SuperClass {
    public void doSomething() throws IOException {
        // ...
    }
}

class SubClass extends SuperClass {
    @Override
    public void doSomething() throws FileNotFoundException { // Subclass of IOException
        // ...
    }
}
```

**No Checked Exception:** If the superclass method doesn’t declare any exceptions (doesn’t throw any checked exceptions), the overriding method in the subclass cannot declare a checked exception. However, it can still declare unchecked exceptions (runtime exceptions).

```
class SuperClass {
    public void doSomething() {
        // ...
    }
}

class SubClass extends SuperClass {
    @Override
    public void doSomething() throws IOException { // Not allowed (superclass doesn't throw IOException)
        // ...
    }
}
```

## **Explain Spring MVC flow in detail?**

![](https://ddfx29dm3fys07.archive.ph/H1nNz/9a70c727735c4c49e3cf9ea882cc00d3c6cde974.webp)

Spring MVC follows the Model-View-Controller (MVC) architectural pattern, which separates application logic, data presentation, and user interaction for better maintainability and testability. Here’s a detailed breakdown of the flow in a Spring MVC application:

**1. Client Request:**

- The user interacts with the web application through their browser, initiating an HTTP request (GET, POST, etc.) to a specific URL on the server.

**2. DispatcherServlet Intercept:**

- The `DispatcherServlet` acts as the front controller in Spring MVC. It receives all incoming HTTP requests from the web container (like Tomcat or Jetty).

**3. Handler Mapping:**

- The `DispatcherServlet` consults the `HandlerMapping` (usually implemented by `RequestMappingHandlerMapping`) to determine which controller method should handle the incoming request.
- This mapping is typically defined using annotations like `@RequestMapping` or `@GetMapping` on controller methods, specifying the URL patterns they handle.

**4. Handler Selection:**

- Based on the request URL and HTTP method, the `HandlerMapping` identifies the appropriate controller class and method to handle the request.

**5. Controller Invocation:**

- The `DispatcherServlet` creates an instance of the identified controller class (if not already created) using Spring Dependency Injection.
- It then invokes the corresponding handler method on the controller, passing the request object as an argument.

**6. Model Population:**

- Inside the controller method, the business logic is executed. This might involve:
- Interacting with the model (domain objects) to retrieve or update data (e.g., accessing a database through a service layer).
- Performing calculations or validations.
- Populating a model object with the processed data to be used for view rendering.

**7. View Resolution:**

- Once the model is populated, the controller needs to choose a view to render the response. It typically uses a `ViewResolver` (usually implemented by `InternalResourceViewResolver` or other resolvers) to identify the appropriate view template.
- The view name is often specified by the controller method using `ModelAndView` or returning a String representing the view name.

**8. View Rendering:**

- The `ViewResolver` locates the view template based on the chosen view name (usually a JSP or FreeMarker template).
- The model object is passed to the view engine (like JSP engine or FreeMarker engine) for rendering the final HTML response.
- The rendered HTML response is then sent back to the client’s browser.

## **What happens when there is a exception occurs in Finally block?**

In Java, when an exception occurs within the `finally` block of a try-catch block, the behavior is slightly different from exceptions in the try or catch blocks. Here's how it works:

1. **Exception in Try or Catch Block:**
- If an exception occurs in the `try` block or a `catch` block, the following happens:
- The normal flow of execution stops.
- If a matching `catch` block is found for the exception type, the code within that `catch` block is executed. This allows you to handle the exception gracefully.
- After the `catch` block finishes, or if no matching `catch` block is found, any code in the `finally` block is still executed.
1. **Exception in Finally Block:**
- If an exception occurs within the `finally` block:
- The original exception (from the `try` or `catch` block, if any) is **suppressed**. This means the original exception is not propagated to the caller of the method.
- The exception thrown from the `finally` block becomes the new exception that is propagated to the caller.

**Key Points:**

- The `finally` block is always executed, regardless of whether an exception occurs in the `try` or `catch` block.
- An exception in the `finally` block suppresses the original exception.
- The exception thrown from the `finally` block becomes the new exception that the caller needs to handle.

**Common Use Cases for Finally Block:**

- Releasing resources (closing files, database connections, etc.) to prevent leaks, even if exceptions occur elsewhere.
- Performing cleanup actions (like closing streams) that should always happen, regardless of exceptions.

## **What is the Diamond problem in java?**

The “diamond problem” in Java refers to a specific issue that arises in multiple inheritance scenarios, particularly in languages that support both single and multiple inheritance. It’s named after the diamond shape that results when class inheritance diagrams are drawn.

1. Java’s Approach: Java doesn’t support multiple inheritance of classes (where a class can inherit from more than one class). However, Java allows multiple inheritance of interfaces. If a class implements multiple interfaces, and those interfaces have the same method signature, it doesn’t cause ambiguity because interfaces only declare method signatures, leaving it up to the implementing class to define the method bodies.
2. Diamond Problem in Java Interfaces: While Java doesn’t have the diamond problem with classes, it can occur with interfaces. If a class implements two interfaces, and both interfaces declare a method with the same signature but different default implementations, the implementing class must provide its own implementation of the method to resolve the ambiguity.

Here is how diamond problem will look like,

```
interface InterfaceA {
    default void display() {
        System.out.println("Inside InterfaceA");
    }
}

interface InterfaceB {
    default void display() {
        System.out.println("Inside InterfaceB");
    }
}

class MyClass implements InterfaceA, InterfaceB {
    // Here, we must provide our own implementation of display to resolve the ambiguity.
    @Override
    public void display() {
        InterfaceA.super.display(); // calling InterfaceA's default implementation
        InterfaceB.super.display(); // calling InterfaceB's default implementation
    }
}
```

How To resolve it?

To resolve the diamond problem in Java interfaces, where a class implements multiple interfaces with conflicting default method implementations, you can follow several approaches:

1. Override the Method: Provide your own implementation of the method in the implementing class, thus resolving the ambiguity. This approach is suitable when you want to choose one of the default implementations or provide a completely new implementation.

```
class MyClass implements InterfaceA, InterfaceB {
    @Override
    public void display() {
        InterfaceA.super.display(); // or InterfaceB.super.display()
    }
}
```

Call Specific Interface’s Method: Call the specific interface’s method directly in your implementation. This approach is useful when you want to utilize both default implementations or choose a specific one dynamically.

```
class MyClass implements InterfaceA, InterfaceB {
    @Override
    public void display() {
        InterfaceA.super.display(); // or InterfaceB.super.display()
        // Additional logic if needed
    }
}
```

## **What is Multilevel Inheritance?**

In multilevel inheritance, a class inherits properties and methods from another class, which itself inherits from yet another class. This creates a hierarchy of classes where each class inherits from the one above it in the chain.

![](https://ddfx29dm3fys07.archive.ph/H1nNz/5a31c72fcf8e0fbb4c427b1a1d842f1fd952eeac.webp)

Here’s a breakdown of multilevel inheritance in Java:

**Structure:**

Imagine a family tree:

- **Grandparent Class:** Represents the most base class in the hierarchy.
- **Parent Class:** Inherits properties and methods from the grandparent class.
- **Child Class:** Inherits properties and methods from the parent class.

**Inheritance Chain:**

The `Child` class inherits indirectly from the `Grandparent` class through the `Parent` class. The `Child` class has access to all public and protected members (methods and properties) of both the `Parent` and `Grandparent` classes.

## **Difference between String ,Stringbuffer and Stringbuilder?**

![](https://ddfx29dm3fys07.archive.ph/H1nNz/f11f761ade478c1a5e322a5acf3b5aac0b16d30b.webp)

Note: String is important topic in Beginners level interview

## **How to create immutable class in java?**

Most common question Java dev interview, If you are following me since long i have written its answer multiple time.

## **What is the Method Overloading and Overriding?**

Method overloading and overriding are both concepts in object-oriented programming (OOP) related to methods in classes. They deal with how methods with the same name are handled, but they differ in their context and purpose.

**Method Overloading**

- **Definition:** Method overloading occurs within a single class. It refers to multiple methods in the same class having the same name but different parameter lists (number, order, or type of parameters).
- **Purpose:** Method overloading allows you to create methods that perform similar operations but with different inputs or variations.

```
class Calculator {
  public int add(int a, int b) {
    return a + b;
  }

  public double add(double a, double b) {
    return a + b;
  }
}
```

In this example, the `add` method is overloaded. It has two versions: one for adding integers and another for adding doubles. The compiler can identify which `add` method to call based on the arguments provided.

**Method Overriding**

- **Definition:** Method overriding occurs between classes in an inheritance hierarchy. It refers to a subclass re-defining a method inherited from its parent class. The method has the same name, return type, and parameter list (same signature) as the parent class method.
- **Purpose:** Method overriding allows subclasses to provide their own implementation of a method inherited from a parent class, potentially specializing the behavior for the subclass.
- **Example:**

```
class Animal {
  public void makeSound() {
    System.out.println("Generic animal sound");
  }
}

class Dog extends Animal {
  @Override
  public void makeSound() {
    System.out.println("Woof!");
  }
}
```

Here, the `makeSound` method is overridden in the `Dog` class. It inherits the method from `Animal` but provides a specific implementation for dogs (printing "Woof!").

## **What is the Hierarchy of exception?**

![](https://ddfx29dm3fys07.archive.ph/H1nNz/879f1abb5529c8e139722118c6840a8c2506170b.webp)

## **Difference between Arraylist and Linkedlist?**

![](https://ddfx29dm3fys07.archive.ph/H1nNz/189b64b8f9a662357b79296dcdda151be8625cca.webp)

**Difference between Set and Arraylist?
How to Create Custom exception in spring boot?
What is Java-8 features — Explain stream api and functional interface?
What is Microservice in details?**

![](https://ddfx29dm3fys07.archive.ph/H1nNz/fd3ecd15af9a0df2f75e456859d57fc44cae64fa.webp)

# **Top 15 Java Tech Round Interview Questions 2025 (Experience 2–5years)**

![](https://d7bvq6dphr91ja.archive.ph/c910J/ce5964c33f0c835c13d9c0055bc188186fde493c.webp)

[ByteByteGo](https://archive.ph/o/c910J/https://bytebytego.com/?fpr=ajay-rathod90)

For study purposes, I have segregated questions based on topics.Weekly, I post an article regarding interview questions. So far, I have focused only on Java, which is my background. In the future, I plan to cover Python, JavaScript, System Design, and coding-related articles. Stay tuned!If this is your first time visiting my Medium page, here is a list of my stories worth reading if you are serious about preparing for Java Developer interviews.

> REST API Basics
> 

For Every software engineer working with API is must one, that why you need to know how they work and what are the different styles of API development like REST, SOAP, GRAPH-QL and All.

If you are interested in reading more here is one article i have written previously, [Most popular API architecture styles in our Digital World](https://archive.ph/o/c910J/https://medium.com/javarevisited/most-popular-api-architecture-styles-in-our-digital-world-be5f409e814b)

Lets Dive into Actual Questions,

## **What is a REST API, and how does it differ from SOAP?(SOAP vs REST)?**

![](https://d7bvq6dphr91ja.archive.ph/c910J/1fa6b53eedfd2dfeef42621fdbf16b4dfa02a64b.webp)

## **Explain the key principles of RESTful architecture.**

Key Principles of RESTful Architecture

RESTful architecture is guided by six fundamental principles or constraints that ensure simplicity, scalability, and modularity in web service design:

Uniform Interface

- Ensures consistent interaction between clients and servers.
- Resources are uniquely identified via URIs, manipulated using standard HTTP methods (GET, POST, PUT, DELETE), and represented uniformly.
- Messages are self-descriptive and include enough information for the client to understand how to process them.
- Hypermedia as the engine of application state (HATEOAS) allows clients to dynamically navigate resources via hyperlinks

Client-Server Separation

- Separates concerns between the client (user interface) and server (data storage and processing).
- This independence allows both components to evolve independently without breaking their communication contract.

Statelessness

Each client request must contain all the information necessary for the server to process it.

- The server does not store any session state, making REST APIs easier to scale and more fault-tolerant.

Cacheable Responses

- Responses from the server must explicitly define whether they are cacheable or non-cacheable.
- Caching improves performance by reducing server load and latency for repeated requests

Layered System

- REST APIs can be designed with multiple hierarchical layers (e.g., security, business logic) that work together but remain invisible to the client.
- This enhances scalability, security, and system performance through load balancing and shared caches

## **What are resources in the context of REST APIs, and how are they identified?**

In the context of REST APIs, a resource is any piece of information that can be named, accessed, or manipulated via the API. Resources are the key abstraction in RESTful architecture and represent entities such as documents, images, users, products, or even collections of other resources. For example:

- A user profile (`/users/123`)
- A collection of blog posts (`/posts`)
- A specific product (`/products/456`)

Each resource has a state at a given time, called its *representation*, which includes:

1. Data: The actual content or information (e.g., user details like name and email).
2. Metadata: Descriptive information about the resource (e.g., timestamps or versioning).
3. Hypermedia Links: Links to related resources that allow navigation (e.g., `/users/123/orders`)

*How Are Resources Identified?*

Resources in REST APIs are uniquely identified using Uniform Resource Identifiers (URIs). A URI specifies the path to a resource on the server. For example:

- `/users/123` identifies a specific user with ID 123.
- `/products/456/reviews` identifies reviews for a specific product.

The URI acts as a unique address for the resource, enabling clients to interact with it using standard HTTP methods like:

- GET: Retrieve the resource.
- POST: Create a new resource.
- PUT/PATCH: Update an existing resource.
- DELETE: Remove the resource.

This design ensures that resources are easily accessible and manipulated in a consistent manner across different systems

## **What is the role of HTTP methods (GET, POST, PUT, PATCH, DELETE) in REST APIs?**

*I think everyone knows this, thats why keeping it blank.*

> Advanced REST API Concepts
> 

## **How would you troubleshoot issues with REST API resource requests?**

To troubleshoot REST API issues effectively:

Check HTTP Status Codes

- Identify errors using status codes like 4xx (client-side) or 5xx (server-side).

Verify Endpoint URLs

- Ensure the URL structure is correct and matches the API documentation.

Inspect Request Headers

- Confirm proper headers, including authentication tokens and content types.

Validate Query Parameters and Request Body

- Check for missing or incorrect parameters and ensure the request body matches the expected format (e.g., JSON).

Analyze Logs and Monitor Tools

- Use server logs and monitoring tools to pinpoint issues.

Test Authentication

- Verify credentials and authorization protocols (e.g., OAuth).

Debug Using Tools

- Utilize tools like Postman or curl to manually test requests and responses.

Check Rate Limits

- Ensure requests comply with API rate limits to avoid throttling errors.

## **What are cache-control headers, and how do they impact API performance?**

Cache-Control headers are HTTP headers used to define caching policies for server responses. They specify how, by whom, and for how long a response can be cached, enabling efficient reuse of resources without repeatedly fetching them from the origin server.

How Cache-Control Headers Impact API Performance:

Reduced Bandwidth Usage

- Cached responses eliminate the need for repeated data transfers, lowering bandwidth consumption.

Improved Latency

- Serving cached resources reduces response times, enhancing user experience.

Decreased Server Load

- By offloading requests to caches (e.g., browser or CDN), servers handle fewer requests, improving scalability.

Enhanced Fault Tolerance

- Cached copies can serve users during network failures or server downtimes

Common Cache-Control Directives:

- `max-age`: Specifies the maximum time (in seconds) a resource is considered fresh (e.g., `Cache-Control: max-age=3600`).
- `no-cache`: Forces validation with the origin server before using cached data.
- `no-store`: Prevents caching entirely[5](https://archive.ph/o/c910J/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control).
- `private`: Restricts caching to the client's browser only.
- `public`: Allows caching by any intermediary (e.g., CDN).

By leveraging Cache-Control headers effectively, REST APIs can achieve better performance and reliability while reducing infrastructure costs.

## **How can you protect a REST API from spamware or bots?**

Implement CAPTCHA

- Add CAPTCHA checks for endpoints that handle sensitive or spammable actions, such as account creation or form submissions. This ensures that only human users can proceed.

Use API Keys

- Require clients to use unique API keys for authentication. This allows you to track and limit requests from specific users.

Rate Limiting

- Limit the number of requests per client or IP address within a specific time frame to prevent abuse.

IP Filtering

- Block or throttle requests from suspicious IPs or regions known for spam activity.

Session Validation

- Use session-based identifiers to track client activity and prevent excessive requests during a single session.

HMAC Authentication

- Implement HMAC (Hash-based Message Authentication Code) to ensure that requests are signed securely, preventing unauthorized access even if API keys are exposed.

Bot Detection Mechanisms

- Use tools or algorithms to detect patterns of automated behavior, such as unusual request rates or identical user-agent strings.

Secure Endpoints with SSL/TLS

- Encrypt all communications using HTTPS to protect API keys and sensitive data from interception.

## **What are payloads in RESTful web services?**

There are json payload in rest and mostly we have request payload and response payload. Example look like this,

```
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

> Testing and Tools
> 

## **Which tools would you use to test a REST API, and what steps would you follow during testing?**

Personally I use POSTMAN or SWAGGER UI if it is implemented in my spring boot project, there are other tools available like Rest-Assured, insomnia.

*Steps to Follow During REST API Testing*

Understand API Documentation

- Review the API’s endpoints, parameters, authentication methods, and expected responses.

Set Up Test Environment

- Configure tools like Postman or SoapUI with the correct base URL, headers, and authentication tokens.

Craft Test Requests

- Create requests using various HTTP methods (GET, POST, PUT, DELETE) with valid payloads and parameters.

Validate Responses

- Check status codes (e.g., 200 for success, 400 for client errors), response formats (JSON/XML), and data accuracy.

Test Edge Cases

- Include invalid inputs, missing parameters, or unauthorized access scenarios to ensure robust error handling.

Perform Load Testing

- Use tools like JMeter or SoapUI to simulate high traffic and analyze API performance under stress.

Automate Tests

- Automate repetitive test cases using tools like Rest-Assured or Postman collections integrated with CI/CD pipelines.

## **How do you validate the response format and status codes of an API?**

These Rest API testing questions usually asked to tester who is doing the api testing and need to setup env related to that. developer can skip this.

> Microservices and System Design
> 

In Microservice, Design related Questions is must one below i have documented. [Top 5 Design Patterns Asked in Java Developer Interview](https://archive.ph/o/c910J/https://medium.com/javarevisited/top-5-design-patterns-asked-in-java-developer-interview-67df7b3c1599).

## **What are the challenges of implementing microservices compared to monolithic applications?**

This questions easy but we don’t give answer properly thats why we tend to fail.

Increased Complexity

- Microservices require managing multiple independent services, making development, deployment, and monitoring more complicated.

Debugging Difficulties

- Issues can span multiple services, complicating error tracing compared to monolithic systems where everything runs in a single process.

Higher Operational Overhead

- Each service needs separate hosting, monitoring, and management, increasing infrastructure costs.

Service Interdependencies

- Communication between microservices via APIs introduces potential cascading failures and latency issues.

Deployment Complexity

- Independent deployments require robust CI/CD pipelines and coordination across services.

Organizational Coordination

- Teams must collaborate effectively to manage updates and interfaces between services.

## **Explain decomposition design patterns in microservices?**

Decomposition Design Patterns in Microservices

Decomposition design patterns help break down monolithic applications into smaller, manageable microservices. The two primary patterns are:

1. Decompose by Business Capability

- Concept: Align microservices with business capabilities — functions or processes that deliver value (e.g., sales, billing, claims processing).
- Example: In an insurance company, services might include underwriting, claims processing, and compliance.
- Benefits: Ensures services are business-oriented and loosely coupled[1](https://archive.ph/o/c910J/https://dzone.com/articles/design-patterns-for-microservices)[2](https://archive.ph/o/c910J/https://hackernoon.com/microservice-architecture-patterns-part-1-decomposition-patterns).

2. Decompose by Subdomain

- Concept: Use Domain-Driven Design (DDD) to identify subdomains and bounded contexts within the business domain. Each subdomain becomes a microservice.
- Example: An e-commerce platform might have subdomains like order management, payment processing, and shipping.
- Benefits: Helps manage complex systems by focusing on specific areas of business logic.

These patterns ensure scalability, maintainability, and alignment with business needs while reducing complexity in microservices architecture.

## **How do you monitor the health of microservices in a distributed system?**

I will give you answer from my experience,

1. We have inbuilt end-points available as actuators in the spring boot app that we can use in kubernetes to check the pod health
2. We have implemented Zipkin, Open Telemetry for distributed tracing that helps in service to service communication.
3. also we should have centralised logging like splunk
4. to monitor key metrics we can use prometheus
5. for alerts we can use aws cloud-watch or any other tool.

> Spring Framework & Annotations
> 

You should know each and every concepts of spring framework, it s essential to succeed in the interview. I have documented all the possible spring framework related interview questions here and its worth reading for [**Top 60 Spring-Framework Interview Questions for Java Developers 2024(Contain All the Questions from…**](https://archive.ph/o/c910J/https://medium.com/@rathod-ajay/top-60-spring-framework-interview-questions-for-java-developers-2024-contain-all-the-questions-from-f15621f77d2a)

## **What is the `@CrossOrigin` annotation in Spring, and when would you use it?**

The `@CrossOrigin` annotation in Spring is used to enable Cross-Origin Resource Sharing (CORS) for specific methods, controllers, or globally across the application. CORS is a security feature implemented by browsers to prevent unauthorized cross-origin requests, but it can block legitimate requests in scenarios where the frontend and backend are hosted on different domains.

When Would You Use @CrossOrigin?

Frontend-Backend Communication

- If your frontend (e.g., React or Angular) and backend (Spring Boot REST API) are hosted on different domains or ports, you need `@CrossOrigin` to allow cross-origin HTTP requests.

Granular Control

- Use `@CrossOrigin` at the method or controller level to specify which origins, headers, and HTTP methods are allowed.

Global Configuration

- Apply CORS settings globally when you want all endpoints to accept cross-origin requests.

## **Compare `@ResponseBody`, `@RequestParam`, and `@PathVariable` annotations.**

![](https://d7bvq6dphr91ja.archive.ph/c910J/4c73f9b23c211725b4aa48514a44abaf95afb71d.webp)

> Database Concepts
> 

**In any Java Interview, DB knowledge is must and it requires good amount of study and practic**e, If you are not confident in SQL part and looking for more SQL Query Interview Questions then you can read this article [**“Mastering the Art of SQL Interviews: Unlocking the Solutions to Common and Complex Queries 📊💼](https://archive.ph/o/c910J/https://medium.com/javarevisited/mastering-the-art-of-sql-interviews-unlocking-the-solutions-to-common-and-complex-queries-302c2aba9620) This will help.**

## **Why are searches using primary keys faster than other queries?**

Unique Identification

- Primary keys uniquely identify each record in a table, eliminating the need for scanning the entire dataset to locate specific entries.

Indexing

- Primary keys are automatically indexed, creating a structured roadmap for the database engine to quickly locate records. Indexing reduces the time required for data retrieval, optimizing query performance.

Optimized Search Path

- The database uses the index associated with the primary key to directly access the desired row, bypassing irrelevant data and avoiding full table scans.

Data Integrity

- Primary keys enforce constraints like uniqueness and non-null values, ensuring reliable and consistent query results.

Efficiency in Large Datasets

- In large datasets, primary keys significantly improve query speed by narrowing down search operations to specific indexed rows rather than scanning all records

## **What is the difference between 2NF and 3NF in database normalization?**

![](https://d7bvq6dphr91ja.archive.ph/c910J/6d382baaad58efcce9f5db0d7dbaf040e95f17c5.webp)

## **Write a SQL query to find the top 5 employees earning more than the average salary.**

```
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC
LIMIT 5;
```

> Programming Tasks
> 

## **Write a program using Java Stream API to sort a list of strings by their length.**

```
import java.util.*;
import java.util.stream.Collectors;

public class SortStringsByLength {
    public static void main(String[] args) {
        // Create a list of strings
        List<String> strings = Arrays.asList("apple", "banana", "kiwi", "pear", "orange");

        // Sort the list by string length using Stream API
        List<String> sortedStrings = strings.stream()
                                            .sorted(Comparator.comparingInt(String::length))
                                            .collect(Collectors.toList());

        // Print the sorted list
        System.out.println("Sorted Strings by Length: " + sortedStrings);
    }
}
```

## **How would you implement rate-limiting for an API endpoint?**

So basically this is a system design Interview question, I would recommend Alex xu’s system design interview book which i have myself referred it for such a question and its a must have book for every software engineer.

# **JP Morgan Java Developer Interview**

## **1. What is content negotiation in microservices?**

Content negotiation in microservices refers to the process where a client and a server agree on the format of data to be exchanged during an HTTP request/response.

It enables a microservice to deliver responses in multiple formats, such as JSON, XML, or plain text, based on the client’s preference or capability.

## **Content Negotiation Working**

**1. Client Preference:** The client specifies its preferred data format(s) using HTTP headers:

- **Accept header**: Specifies the media types the client can handle, eg) `Accept: application/json, application/xml`.
- **Content-Type header**: Specifies the format of the data sent in the request body, eg) `Content-Type: application/json`.

**2. Server Response:** The server analyzes the `Accept` header and determines the best format it can provide. If multiple formats are supported, the server chooses the most appropriate one based on priority.

**3. Response:** The server sends the response in the agreed-upon format, along with the `Content-Type` header indicating the media type, eg) `Content-Type: application/json`.

## **Types of Content Negotiation**

1. **Server-Driven Negotiation:** The server decides the response format based on the `Accept` header from the client.
2. **Client-Driven Negotiation:** The client requests specific formats through query parameters, such as `?format=json`.
3. **Agent-Driven Negotiation:** Intermediary software or a proxy negotiates the content format.

## **Benefits in Microservices**

1. **Flexibility:** Supports diverse client applications by delivering data in formats they understand.
2. **Interoperability:** Enhances integration with systems using different data formats.
3. **Scalability:** Allows services to evolve without breaking client compatibility by adding or deprecating formats.

## **Example**

Suppose a client sends the following request to a microservice:

```
GET /users HTTP/1.1
Accept: application/json
```

- If the server supports JSON, it responds:

```
HTTP/1.1 200 OK Content-Type: application/json
```

```
{
"id": 1,
"name": "Shivam Srivastava"
}
```

- If the server cannot provide JSON, it might return:

```
HTTP/1.1406NotAcceptable
```

Content negotiation ensures microservices can adapt to the needs of various clients, making them more versatile and interoperable.

## **2. Why do we use Java 8? Why was it introduced over Java 7?**

We use Java 8 because it was introduced as a major upgrade over Java 7 to bring revolutionary features to the language, making it more modern, expressive, and efficient. Some of the features are:

1. **Functional Programming**:Java 8 introduced functional programming paradigms, which simplify and improve how developers write code. This helps in writing cleaner, more readable, and concise code.
2. **Stream API**:A powerful abstraction for processing collections of data in a functional style. Operations like filtering, mapping, and reducing large data sets are now easier and faster.
3. **Better Concurrency**:Java 8 introduced parallel streams, which enable developers to process data in parallel with minimal effort, improving performance in multi-core systems.
4. **Enhanced Productivity**:Features like **lambda expressions**, **method references**, and **default methods** reduce boilerplate code and increase developer productivity.
5. **Date and Time API**:The new `java.time` package provides a modern, immutable, and thread-safe way to handle date and time, replacing the old, clunky `java.util.Date` and `java.util.Calendar`.
6. **Backward Compatibility**:All features in Java 8 are fully backward-compatible, ensuring older codebases work seamlessly while benefiting from new features.
7. **Improved Performance**:With advancements in the JVM and libraries, Java 8 provides better performance for both functional programming and overall application execution.

## **Why Was Java 8 Introduced Over Java 7:**

> The real reason Java 8 was introduced because Java started to lose market share to Python as Python was very efficient and reduced boiler plate code to minimum.
> 

Below are some of the reason given by Oracle on the same:

1. **Functional Programming Revolution:**

Java 7 lacked functional programming capabilities, while languages like Scala, Python, and JavaScript were already popularizing this paradigm. To stay relevant and competitive, Java 8 added:

- **Lambda Expressions**: Anonymous functions that simplify handling of single-method interfaces.
- **Stream API**: To process data collections in a functional way.

**2. Modernization of the API:**

Java 7’s APIs were verbose and lacked flexibility. Java 8 improved this by:

- Introducing **default methods** in interfaces, enabling backward compatibility and allowing interfaces to evolve without breaking existing implementations.
- Updating APIs like `Collections` and `Map` to support streams and lambda expressions.

**3. Improved Handling of Date and Time:**

The existing `Date` and `Calendar` classes were mutable, cumbersome, and error-prone. Java 8 introduced the `java.time` package, inspired by Joda-Time, to provide:

- Immutability for safety.
- Intuitive APIs for date/time manipulations.

**4. Parallelism:**

Java 7 introduced the **Fork/Join Framework**, but it was complex for average developers. Java 8 simplified parallel processing with:

- **Parallel Streams**: High-level abstraction for parallel data processing.

**5. Global Trends in Software Development:**

With the rise of big data, cloud computing, and modern software practices, Java 8 brought tools to address:

- The need for efficient data processing (via Streams).
- Improved scalability and concurrency (via parallel streams and performance improvements).

**6. Cleaner Codebase:**

Java 7 required verbose constructs for tasks like iterating over collections or implementing single-method interfaces. Java 8 introduced:

- Lambdas for brevity.
- Method references for better readability.

**7. Demand for Backward Compatibility with Innovation:**

Developers needed new features without breaking existing codebases. Java 8 allowed:

- Introduction of **default methods** to extend interfaces without affecting existing implementations.
- Full backward compatibility, making it easy for organizations to adopt it.

## **3. What is Dependency Injection and what are it’s advantages?**

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
3. **Interface Injection**
    
    : The dependency provides an injector method that the dependent class uses to receive its dependencies (less common).
    

## **Example**

Without DI:

```
public class Service {
    private Repository repository = new Repository(); // Tight coupling

    public void performService() {
        repository.save();
    }
}
```

With DI:

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

## **4. What are advantages of MongoDB over MySQL?**

Below are some of the advantages of MongoDB over MySQL in:

## **Core Features:**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/b94409d9d4784f587c1e3dc4cfdd16db89b1efd9.webp)

## **Advanced Capabilities:**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/3e1ff28752b3e2c7958555f005c237df5adea448.webp)

## **Use cases:**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/c17ef0003cc48daa87ec501bd3b0e0476fc8e068.webp)

## **5. Suppose you have 2 threads. One of them prints (1,2,3…) and the other one prints (A,B,C,..). How will you ensure that they run in a sequence, so that it prints (1,A,2,B…)?**

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

## **6. What is a Bean? What are the differences between normal Bean vs Spring Bean?**

A **bean** is an object that is instantiated, assembled, and managed by a container.

In the context of **Java**, a bean is a reusable software component that adheres to specific conventions (e.g., having a no-argument constructor, being serializable, and providing getters and setters).

In **Spring**, a bean is any object that is managed by the Spring IoC (Inversion of Control) container.

## **Example of a Normal Bean:**

```
public class NormalBean {
    private String name;

public NormalBean() {}
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

## **Example of a Spring Bean:**

Using `@Component`:

```
@Component
public class SpringBean {
    private String name;

public SpringBean() {}
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

Defined in a configuration class:

```
@Configuration
public class AppConfig {
    @Bean
    public SpringBean springBean() {
        return new SpringBean();
    }
}
```

## **Differences:**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/ec12c9f3c9f3847246d9eb7fe9d1aa954b50b439.webp)

## **7. How do you secure your microservices?**

Below are some of the ways to secure your microservices:

## **1. Authentication and Authorization:**

**Why:**

- To ensure only legitimate users or systems access the services.

**How:**

- Implement **OAuth2.0** with tokens for users and system authentication.
- Centralize user identity management with solutions like **Keycloak** or **Okta**.

## **2. API Gateway:**

1. Acts as the central entry point for requests and enforces security.
2. Use gateways like **Kong**, **AWS API Gateway**, or **Spring Cloud Gateway** for:
- Authenticating requests.
- Enforcing rate limits.
- Applying access control policies.

## **3. Secure Communication:**

- Use **TLS/SSL** to encrypt all traffic between:
- Clients and microservices.
- Inter-microservice communication (using mutual TLS if possible).

## **4. Service Mesh:**

- A service mesh (e.g., **Istio**, **Linkerd**) provides:
- Built-in **mTLS** for service-to-service communication.
- Fine-grained traffic control policies.
- Observability and logging features.

## **5. Centralized Logging and Monitoring:**

- Enable early detection of breaches or anomalies by:
- Logging security events (e.g., failed logins).
- Using monitoring tools (e.g., **Prometheus**, **ELK Stack**, or **Splunk**).

## **6. Secure Secrets Management:**

- **Do not hard-code secrets** like passwords or API keys in code.
- Use secret management tools:
- **AWS Secrets Manager**, **Azure Key Vault**, or **HashiCorp Vault**.

**8. What are the differences between @Component vs @Service vs @Repository?**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/951f7a0ab5f613a81708f935e1a663b884e79574.webp)

## **9. Suppose you’ve a controller annotation and then you perform DB operation in it. What will happen in that case?**

If you perform database operations directly inside a controller in a Spring application, it **can technically work**, but it’s considered a **bad practice.**

## **What Happens:**

- The controller will still handle the HTTP request and call the repository for the database operation. For example, you might inject a repository directly into the controller like this:

```
@RestController
public class UserController {
    @Autowired
    private UserRepository userRepository;

    @GetMapping("/getUser/{id}")
    public User getUserById(@PathVariable Long id) {
        return userRepository.findById(id).orElse(null);
    }
}
```

- This would work, but the controller is now doing more than just handling HTTP requests — it’s also managing business logic and directly interacting with the database.

## **Why It’s a Bad Practice:**

1. **Violation of Separation of Concerns (SoC)**: A controller’s primary responsibility is to handle HTTP requests and responses. By including database operations, you’re blurring the lines between the different layers of your application.
2. **Harder to Maintain and Test**: Controllers become bloated with business logic, making them harder to maintain and test. For example, you can’t easily test the business logic separately without involving the HTTP layer.
3. **Poor Scalability**: As your application grows, this approach makes it difficult to scale, since controllers will need to handle more responsibilities. This leads to tightly coupled code, which is harder to refactor.
4. **Lack of Transaction Management**: If you don’t manage transactions properly (for example, using `@Transactional`), you risk running into issues with partial updates, especially if the database operations involve multiple steps.

## **Correct Approach:**

The best practice is to **delegate database operations to the service layer**. Here’s the right way to structure it:

- **Controller**: Handles incoming requests and delegates to the service layer.

```
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/getUser/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }
}
```

- **Service Layer**: Contains business logic and interacts with the repository layer.

```
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }
}
```

- **Repository Layer**: Manages database interactions.

```
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
```

## **Why This Is Better:**

- **Separation of Concerns**: Each layer has its distinct responsibility — controllers handle requests, services contain business logic, and repositories manage data access.
- **Testability**: Business logic in services can be tested independently of the web layer.
- **Scalability**: As the application grows, this structure helps with maintainability and avoids bloated controllers.
- **Transaction Management**: You can easily use `@Transactional` at the service layer to manage transactions effectively.

## **10. What are the benefits of using DAO layer?**

The **DAO (Data Access Object)** layer provides a structured way of interacting with a data source, like a database, while abstracting the underlying data persistence mechanism.

Using a DAO layer offers several benefits, especially in terms of maintainability, flexibility, and decoupling of concerns in your application. Below are some of them:

## **1. Separation of Concerns**

- The DAO layer separates the data access logic from the business logic, allowing each layer to focus on its specific responsibility.
- **Benefit**: This leads to **cleaner code**, as your business logic does not need to worry about how the data is retrieved, stored, or updated.

## **2. Maintainability**

- Since the data access logic is centralized in one layer, changes to the underlying data store (such as switching from one database to another) can be made in just the DAO layer without impacting the rest of the application.
- **Benefit**: **Easier to maintain** and **refactor** the application as the data access logic is isolated and doesn’t spread across the application.

## **3. Code Reusability**

- The DAO layer allows you to encapsulate common data access operations (like save, update, delete, and find) in reusable methods.
- **Benefit**: This leads to **less duplication** of code, as any part of your application that needs to interact with the database can reuse the DAO layer.

## **4. Data Source Independence**

- The DAO layer abstracts the underlying data source. If you need to switch from one database (e.g., MySQL) to another (e.g., MongoDB), you can modify the DAO layer with minimal changes to the business logic.
- **Benefit**: **Decoupling** the data source from the rest of the application allows for **greater flexibility** in choosing or changing data stores.

## **5. Simplified Unit Testing**

- The DAO layer can be easily mocked or stubbed in unit tests, allowing you to test the business logic in isolation without needing an actual database connection.
- **Benefit**: It improves **testability** by enabling you to simulate different data access scenarios without the overhead of setting up a database.

## **6. Transaction Management**

- The DAO layer allows for better handling of transactions, especially when dealing with multiple database operations in a single transaction.
- **Benefit**: It simplifies **transaction management** by centralizing it in the DAO, and you can easily use `@Transactional` in a service layer to ensure consistency.

## **7. Encapsulation and Security**

- The DAO layer acts as a **gatekeeper** between the database and the rest of the application, controlling access to the data and hiding the complexities of direct database access (such as SQL queries, connections, etc.).
- **Benefit**: This improves **security** and reduces the risk of exposing sensitive database logic or vulnerabilities (e.g., SQL injection).

## **8. Improved Readability**

- By abstracting the complexity of database queries and data handling into the DAO layer, your codebase becomes more **readable** and focused on higher-level operations.
- **Benefit**: **Better organization** of code, as the business logic is not cluttered with low-level database interactions.

## **9. Flexibility with Data Handling**

- The DAO layer can offer more flexible methods for complex querying, including custom SQL or specific data transformations.
- **Benefit**: You can handle data operations in a **customizable** way, without cluttering the service layer or business logic.

## **Example of DAO Layer Usage**

```
public class UserDAO {
    private EntityManager entityManager;

    public UserDAO(EntityManager entityManager) {
        this.entityManager = entityManager;
    }
    // Save operation
    public void saveUser(User user) {
        entityManager.persist(user);
    }
    // Find operation
    public User findUserById(Long id) {
        return entityManager.find(User.class, id);
    }
    // Delete operation
    public void deleteUser(Long id) {
        User user = findUserById(id);
        if (user != null) {
            entityManager.remove(user);
        }
    }
}
```

## **11. How do you measure DB performance?**

Below are some of the ways to measure **database performance**:

## **1. Query Performance**

- Measure execution time and use **EXPLAIN** plans to optimize queries.

## **2. Response Time**

- Track round-trip time for queries, aiming for low latency.

## **3. Throughput**

- Monitor how many queries the database handles per second/minute.

## **4. Database Connections**

- Monitor the number of active connections and optimize connection pooling.

## **5. Disk I/O**

- Measure read/write speeds, queue length, and disk throughput.

## **6. CPU Usage**

- Track CPU utilization to ensure the database is not overburdened.

## **7. Memory Usage**

- Monitor memory consumption to avoid excessive usage leading to slowdowns.

## **8. Lock Contention**

- Track lock conflicts and deadlocks to avoid delays.

## **9. Cache Hit Ratio**

- Monitor cache hit ratios to ensure frequently accessed data is cached.

## **10. Network Latency**

- Measure round-trip time for data transfer between the application and database.

## **11. Slow Query Logs**

- Capture and analyze slow queries for optimization.

## **12. Index Optimization**

- Ensure efficient indexing and monitor index fragmentation.

## **13. Query Execution Plan:**

- Mentioned briefly but should include advice on using query profiling tools like `EXPLAIN` in SQL databases.

## **14. Database Schema Design:**

- Optimizing schema design impacts performance and should be addressed.

By tracking these metrics using **monitoring tools** (e.g., **Prometheus**, **New Relic**, **MySQL’s EXPLAIN**, **Query profiling**), you can spot and address performance bottlenecks.

## **12. *How would you design a scalable database? What challenges do you foresee, and how would you mitigate them?***

To design a scalable database, we need to focus on both horizontal and vertical scalability, ensuring the system can handle growing data volumes and traffic efficiently.

Here’s how to approach it:

1. **Database Schema Design**
- Start with a normalized schema to eliminate redundancy and ensure consistency.
- For performance-critical applications, we can selectively denormalize certain tables to optimize read-heavy operations.

**2. Horizontal Scaling**

- Implement **sharding** to distribute data across multiple nodes. For example, we can shard based on user ID or geographic regions to evenly distribute the load.
- Partition large tables logically, such as by time ranges (e.g., monthly partitions for a logging system).

**3. Replication**

- Use **master-slave replication** where the master handles writes, and the replicas handle reads, improving both performance and reliability.
- In more complex systems, **multi-master replication** can be used to handle writes from multiple locations.

**4. Caching**

- Integrate caching solutions like **Redis** or **Memcached** to store frequently accessed data in memory, reducing the load on the database.
- Use query-level caching for expensive operations to further enhance performance.

**5. Load Balancing**

- Add a load balancer to distribute queries across multiple database instances, ensuring no single node becomes a bottleneck.

**6. Asynchronous Processing**

- For write-intensive operations, we can leverage message queues like **Kafka** or **RabbitMQ** to handle tasks asynchronously, reducing the immediate load on the database.

**7. Cloud or Distributed Databases**

- For large-scale applications, we can consider databases like **Cassandra**, **CockroachDB**, or **MongoDB** that are inherently distributed and designed for horizontal scaling.
- Alternatively, use managed cloud services like **AWS RDS** or **Google Cloud SQL** that offer built-in scaling and fault tolerance.

**8. Monitoring and Optimization**

- Regularly monitor database metrics like query performance, CPU usage, memory utilization, and disk I/O using tools like **Prometheus** or **Grafana**.
- Continuously optimize slow queries and ensure indexes are up to date.

**9. Archiving and Data Management**

- Archive older, less-used data to a separate storage system to keep the active dataset manageable. This helps maintain fast query performance on current data.

By combining these strategies, the database can handle increased traffic, maintain low latency, and remain resilient as the system grows.

## **Challenges:**

- **Data Consistency**: In distributed databases, maintaining strong consistency can be challenging. We can use appropriate consistency models, like eventual consistency where acceptable.
- **Shard Management**: Resharding as data grows can be complex. To mitigate this, we can plan sharding keys carefully from the beginning.
- **Query Optimization**: Complex joins across shards or replicas can slow down performance. We can design queries and schema to minimize such operations.

Proactively monitoring and iterating on the design would help address these challenges effectively.

## **13. How do you handle exceptions in Spring Boot application?**

Exception handling in a Spring Boot application can be managed in an organized way using several key approaches:

## **1. Using `@ControllerAdvice` and `@ExceptionHandler`**

- `@ControllerAdvice` is used to define a global exception handler for the entire application, combined with `@ExceptionHandler` to specify how to handle particular exceptions.
- Example:

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

This ensures that exceptions are handled consistently and provides proper HTTP responses.

## **2. Using `@ResponseStatus` Annotation**

- The `@ResponseStatus` annotation maps exceptions to specific HTTP status codes.
- Example:

```
@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

When this exception is thrown, Spring automatically returns a 404 status with the custom message.

## **3. Custom Error Response Structure**

- For detailed error responses, create a custom error object containing fields like `timestamp`, `error code`, and `message`.
- Example:

```
public class ErrorResponse {
    private String timestamp;
    private String message;
    private String details;

    // Getters and setters
}
```

This custom object can be returned from the global exception handler:

```
@ExceptionHandler(Exception.class)
public ResponseEntity<ErrorResponse> handleAllExceptions(Exception ex, WebRequest request) {
    ErrorResponse error = new ErrorResponse();
    error.setTimestamp(LocalDateTime.now().toString());
    error.setMessage(ex.getMessage());
    error.setDetails(request.getDescription(false));

    return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
}
```

## **4. Handling Validation Exceptions**

- When using `@Valid` or `@Validated`, Spring automatically throws `MethodArgumentNotValidException` for validation failures. This can be handled as follows:

```
@ExceptionHandler(MethodArgumentNotValidException.class)
public ResponseEntity<String> handleValidationException(MethodArgumentNotValidException ex) {
    String errors = ex.getBindingResult().getAllErrors().stream()
                      .map(ObjectError::getDefaultMessage)
                      .collect(Collectors.joining(", "));
    return new ResponseEntity<>("Validation failed: " + errors, HttpStatus.BAD_REQUEST);
}
```

## **5. Logging Exceptions**

- All exceptions can be logged using SLF4J or a similar framework to ensure proper monitoring and debugging.

```
private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

@ExceptionHandler(Exception.class)
public ResponseEntity<String> handleGenericException(Exception ex) {
    logger.error("An error occurred: ", ex);
    return new ResponseEntity<>("Something went wrong", HttpStatus.INTERNAL_SERVER_ERROR);
}
```

## **6. Fallback for Unhandled Exceptions**

- A fallback mechanism ensures unhandled exceptions are caught and returned with a generic error response.

## **14. How to write a custom method in MongoDB?**

Creating a custom method in MongoDB depends on the context of its usage. If the goal is to implement custom queries or operations, it can be achieved through a combination of the following techniques:

## **1. Using the MongoDB Shell or Compass**

Custom logic can be written directly using the JavaScript-based MongoDB shell. For example:

```
db.collectionName.findCustom = function(criteria) {
    return this.find({ $or: [criteria] }).sort({ createdAt: -1 });
};
```

This adds a custom method (`findCustom`) to a collection that can be reused. However, this is typically used for quick testing or prototyping.

## **2. Using MongoDB Aggregation Framework**

For complex queries, the aggregation framework can be used to implement custom logic. Example:

```
db.orders.aggregate([
    { $match: { status: "Pending" } },
    { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
    { $sort: { total: -1 } }
]);
```

This retrieves all pending orders, groups them by customer, calculates the total amount, and sorts the result.

## **3. In Application Code (Custom Repository Methods)**

Custom methods are often created in application code using a driver like **Mongoose** (Node.js) or **Spring Data MongoDB** (Java).

## **Example: Using Spring Data MongoDB**

**a) Define a Custom Repository Interface**:

```
public interface CustomUserRepository {
    List<User> findUsersByCustomCriteria(String status, int minAge);
}
```

**b) Implement the Custom Repository**:

```
public class CustomUserRepositoryImpl implements CustomUserRepository {

@Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public List<User> findUsersByCustomCriteria(String status, int minAge) {
        Query query = new Query();
        query.addCriteria(Criteria.where("status").is(status).and("age").gte(minAge));
        return mongoTemplate.find(query, User.class);
    }
}
```

**c) Integrate the Repository in a Service**:

```
@Service
public class UserService {
    @Autowired
    private CustomUserRepository customUserRepository;

    public List<User> getFilteredUsers(String status, int minAge) {
        return customUserRepository.findUsersByCustomCriteria(status, minAge);
    }
}
```

This approach allows clean separation of custom query logic and integrates seamlessly into the application.

## **4. Custom JavaScript Functions in MongoDB**

For reusable custom logic, MongoDB allows custom JavaScript functions to be stored on the server.

**a) Define a JavaScript Function**:

```
db.system.js.save({
    _id: "findUsersByAge",
    value: function(age) {
        return db.users.find({ age: { $gte: age } });
    }
});
```

**b) Call the Function**:

```
db.loadServerScripts();
findUsersByAge(30);
```

## **5. Custom Commands**

MongoDB supports defining custom commands at the database level using server-side scripts or through MongoDB plugins.

**15. What are the differences between Maven and Gradle?**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/bd593fef5aad58222c6d0261f1fec2433ebc43f0.webp)

## **16. What is rebasing in GIT?**

Rebasing in Git is a way to reapply commits from one branch onto another branch in a linear sequence.

It essentially transfers the base of the branch you are working on to another branch, giving you a cleaner project history.

## **Working:**

- Git replays the commits from your branch onto the target branch one by one.
- The commits are re-created with new commit hashes since they’re applied in a different context.

## **Command:**

```
git checkout feature-branch   git rebase main
```

This moves the `feature-branch` commits to start after the `main` branch commits.

## **Advantages:**

- **Clean History**: Keeps the commit history linear and easier to read.
- **Avoids Merge Commits**: Unlike merging, rebasing doesn’t create extra merge commits.

## **When to Use:**

- For keeping feature branches up to date with the main branch.
- To clean up commit history before merging.

## **Risks:**

- **Rewriting History**: Rebasing changes commit hashes, which can cause issues in shared branches.
- **Conflict Resolution**: Requires resolving conflicts for each commit being replayed.

**17. What are the advantages of Lambda expression?**

![](https://d6gl9gdsvnqcy0.archive.ph/Zzcwz/da0ae6fe018fd8611f0e15d70efd42a85147e706.webp)

## **18. What is the contract between Hashcode and equals method in Java?**

The contract between `hashCode()` and `equals()` can be described as below:

1. **If two objects are equal (as per `equals()` method), they must have the same `hashCode()`.**
- This ensures consistent behavior in hash-based collections.

**2. If two objects have the same `hashCode()`, they are not guaranteed to be equal.**

- Collisions can occur, where different objects share the same hash code.

**3. Overriding `equals()` requires overriding `hashCode()` as well.**

- Failing to do so can lead to inconsistent behavior in collections.

## **Example**

**Without Proper Implementation**:

```
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }
    @Override
    public boolean equals(Object o) {
        if (o instanceof Person) {
            return ((Person) o).name.equals(this.name);
        }
        return false;
    }
}
```

- If `hashCode()` is not overridden, two `Person` objects with the same `name` may have different hash codes, leading to inconsistent behavior in collections.

**With Proper Implementation**:

```
class Person {
    String name;
    Person(String name) {
        this.name = name;
    }
    @Override
    public boolean equals(Object o) {
        if (o instanceof Person) {
            return ((Person) o).name.equals(this.name);
        }
        return false;
    }
    @Override
    public int hashCode() {
        return name.hashCode();
    }
}
```

Now, objects with the same `name` will have the same hash code, ensuring consistent behavior in hash-based collections.

## **19. What is a weak hashmap?**

A **`WeakHashMap`** is a type of map in Java where the keys are stored as **weak references**. This means that if there are no strong references to a key object, it can be garbage collected, even if it still exists in the map.

This differs from the regular `HashMap`, where the keys are stored as strong references, preventing the key objects from being garbage collected.

1. **Weak References for Keys**:
- The keys are weakly referenced. If a key is no longer reachable by any active thread (i.e., no strong references exist to it), the entry for that key will be removed from the map during the next garbage collection cycle.

**2. Automatic Garbage Collection**:

- This behavior is particularly useful for caching scenarios where we don’t want the keys to persist in memory unnecessarily once they are no longer used elsewhere.

**3. No Impact on Values**:

- The values in the `WeakHashMap` are **strong references**, meaning they won’t be garbage collected unless they are no longer referenced by any object.

## **Use Cases:**

- **Memory-sensitive caching**: When objects used as keys are large or expensive to create, you can let the garbage collector reclaim them if they are no longer in use.
- **Metadata management**: When you need to store temporary mappings that should not prevent the referenced objects from being garbage collected.

## **Example**

```
import java.util.*;
public class WeakHashMapExample {
    public static void main(String[] args) {
        Map<String, String> map = new WeakHashMap<>();

        String key = new String("Key");
        map.put(key, "Value");
        System.out.println("Before GC: " + map);
        key = null;  // Remove strong reference to key

        // Suggesting garbage collection
        System.gc();
        System.out.println("After GC: " + map);  // Entry may be removed
    }
}
```

In this example, once the strong reference to `key` is removed (set to `null`), the garbage collector can reclaim it, and the entry may be removed from the `WeakHashMap`.

## **20. Explain Internal working of concurrent hashmap?**

A **`ConcurrentHashMap`** is a thread-safe map introduced in Java 5, designed for high concurrency, which allows multiple threads to read and write to the map concurrently without blocking each other.

Unlike a regular `HashMap` that is not synchronized and prone to data inconsistency when accessed concurrently, `ConcurrentHashMap` provides an efficient way to handle concurrent operations.

## **Internal Working of `ConcurrentHashMap`:**

1. **Segmented Locking (Bucket-Level Locking)**:
- Internally, `ConcurrentHashMap` divides the map into **segments**, each of which is independently locked.
- The map is divided into a number of segments (usually 16). Each segment behaves like a separate hash table, and each segment can be locked independently, which allows multiple threads to work on different segments simultaneously without contention.
- For example, if one thread is updating a segment, another thread can still access or modify other segments without being blocked.

**2. Buckets**:

- Within each segment, the `ConcurrentHashMap` uses an array of **buckets**, just like a regular hash map. Each bucket holds a linked list of entries (key-value pairs) or uses a more advanced data structure like a balanced tree for high-concurrency scenarios.

**3. Concurrency Level**:

- The **concurrency level** defines how many segments the map should be divided into. This can be adjusted during the map’s creation using the constructor. By default, it’s set to 16 segments, meaning 16 threads can work in parallel, with each thread accessing a different segment.

**4. Lock Striping**:

- The segments implement **lock striping**, which allows each segment to be locked independently.
- When a thread accesses the map and wants to perform an operation (like `put` or `remove`), it first calculates which segment the key belongs to using the hash value. Then it locks that particular segment.

**5. Non-Blocking Reads**:

- One of the key features of `ConcurrentHashMap` is that reads are **non-blocking**. Multiple threads can read from the map simultaneously without locking, as long as they are not modifying the same segment. This significantly improves performance in high-concurrency scenarios.

**6. Write Operations (Locking)**:

- When a thread performs a write operation (like `put` or `remove`), the corresponding segment is locked. However, since only one thread can modify a segment at a time, this minimizes contention.
- For **key-value pairs in buckets**, the modification is done with finer granularity, locking only the specific segment and bucket being updated.

**7. Increased Scalability**:

- The use of segments and lock striping increases the scalability of the `ConcurrentHashMap`. It’s particularly beneficial in multi-core systems where several threads can access different segments in parallel, reducing the overall contention and improving throughput.

**8. Rehashing**:

- Just like `HashMap`, `ConcurrentHashMap` handles **rehashing** when the number of entries exceeds a certain threshold. However, during rehashing, only the segment being expanded is locked, so other segments are still available for concurrent operations.

## **Operations Internal Working:**

1. **`put()`**:
- The key’s hash value is used to determine the segment.
- The corresponding segment is locked (if necessary), and the key-value pair is added to the appropriate bucket in that segment.
- If the bucket’s size exceeds a threshold, a **resize** or rehashing may occur.

2. **`get()`**:

- The hash value is used to find the correct segment and bucket.
- Reads can occur concurrently, and they don’t require locking the entire map or segment, which makes the operation faster.

3. **`computeIfAbsent()`**:

- A thread-safe method that computes a value if it’s absent, typically using a `lambda` expression to create or fetch the value.
- This method ensures that only one thread can compute the value for a particular key at a time.

## **21. You have a list of student names in a college. How can you convert this list into a set? What happens with the duplicate names?**

To convert a list of student names into a set, the list can be passed directly to the constructor of the `Set` interface, such as a `HashSet`.

For example:

```
import java.util.*;

public class ListToSetExample {
    public static void main(String[] args) {
        List<String> studentNames = Arrays.asList("Alice", "Bob", "Alice", "Charlie", "Bob");
        // Convert list to set
        Set<String> uniqueNames = new HashSet<>(studentNames);
        // Print the set
        System.out.println("Unique Names: " + uniqueNames);
    }
}
```

## **What Happens to Duplicate Names?**

When converting the list to a set:

1. **Duplicate names are automatically removed** because a `Set` does not allow duplicate elements.
2. Only one instance of each name will remain in the set, ensuring all elements in the set are unique.

For example, if the list contains:`["Alice", "Bob", "Alice", "Charlie", "Bob"]`,the resulting set will contain:`["Alice", "Bob", "Charlie"]`.

This behavior is particularly useful when the goal is to eliminate duplicates from a collection.

## **22. Explain deep copy with examples.**

A **deep copy** refers to creating an entirely new copy of an object, including its nested or referenced objects.

In a deep copy, changes made to the copied object do not affect the original object and vice versa. This is because the deep copy creates new instances for all referenced objects as well.

## **Example:**

Let’s demonstrate this with a `Student` class containing a nested `Address` object.

```
class Address implements Cloneable {
    String city;
    String state;

public Address(String city, String state) {
        this.city = city;
        this.state = state;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return new Address(this.city, this.state); // Create a new Address instance
    }
}
class Student implements Cloneable {
    String name;
    Address address;
    public Student(String name, Address address) {
        this.name = name;
        this.address = address;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        // Perform deep copy
        Student clonedStudent = (Student) super.clone();
        clonedStudent.address = (Address) address.clone(); // Clone nested Address object
        return clonedStudent;
    }
}
public class DeepCopyExample {
    public static void main(String[] args) throws CloneNotSupportedException {
        // Original object
        Address address = new Address("New York", "NY");
        Student originalStudent = new Student("John", address);
        // Perform deep copy
        Student clonedStudent = (Student) originalStudent.clone();
        // Modify cloned object
        clonedStudent.name = "Alice";
        clonedStudent.address.city = "Los Angeles";
        // Print both objects
        System.out.println("Original Student: " + originalStudent.name + ", Address: "
                + originalStudent.address.city + ", " + originalStudent.address.state);
        System.out.println("Cloned Student: " + clonedStudent.name + ", Address: "
                + clonedStudent.address.city + ", " + clonedStudent.address.state);
    }
}
```

## **Output:**

```
Original Student: John, Address: New York, NY
Cloned Student: Alice, Address: Los Angeles, NY
```

## **Advantages of Deep Copy:**

- Ensures complete independence between the original and the copied object.
- Ideal when the object contains nested objects or mutable fields.

# **ThoughtWorks Java Developer Interview Question July 2024**

## **Find the next greatest element for each element in an array?**

Here’s a Java code example to find the next greatest element for each element in an array. This problem is often referred to as the “Next Greater Element” problem. The solution uses a stack to efficiently find the next greater elements:

```
import java.util.Arrays;
import java.util.Stack;
public class NextGreaterElement {
public static void main(String[] args) {
int[] arr = {4, 5, 2, 25, 7, 8};
int[] result = findNextGreaterElements(arr);

System.out.println("Array: " + Arrays.toString(arr));
System.out.println("Next Greater Elements: " + Arrays.toString(result));
}
 public static int[] findNextGreaterElements(int[] arr) {
 int[] result = new int[arr.length];
Stack<Integer> stack = new Stack<>();

for (int i = arr.length – 1; i >= 0; i – ) {
while (!stack.isEmpty() && stack.peek() <= arr[i]) {
stack.pop();
}
result[i] = stack.isEmpty() ? -1 : stack.peek();
stack.push(arr[i]);
}

return result;
}
}

### Explanation:
**Initialize Result Array and Stack**:
. – `result` array stores the next greater element for each position.
. – `stack` is used to keep track of elements for which we haven't found the next greater element yet.

2. **Traverse the Array from Right to Left**:
. – For each element, we pop elements from the stack that are less than or equal to the current element, because they cannot be the next greater element for any of the remaining elements.

3. **Assign Next Greater Element**:
. – If the stack is not empty, the next greater element for the current element is the top of the stack.
. – If the stack is empty, there is no greater element, so we assign `-1`.

4. **Push Current Element onto the Stack**:
. – This ensures that the current element can be used as the next greater element for the elements on its left.

The time complexity of this solution is \(O(n)\) because each element is pushed and popped from the stack at most once. The space complexity is also \(O(n)\) due to the stack.
```

## **What is the difference between Postgres and MySQL database?**

- **ACID Compliance**: PostgreSQL is fully ACID compliant; MySQL’s compliance depends on the storage engine (InnoDB is ACID compliant).
- **SQL Compliance**: PostgreSQL is highly SQL-compliant; MySQL is less so but supports essential features.
- **Data Types**: PostgreSQL supports a wide range of data types, including JSONB; MySQL supports fewer types but includes JSON.
- **Performance**: PostgreSQL excels with complex queries and large datasets; MySQL is often faster for simple, read-heavy operations.
- **Extensibility**: PostgreSQL is highly extensible with custom functions and types; MySQL is less extensible.
- **Replication**: Both support replication, but PostgreSQL offers advanced features like logical replication.
- **Community**: Both have strong community support, with PostgreSQL known for extensive third-party tools.
- **Licensing**: PostgreSQL uses a permissive license; MySQL uses the GPL with commercial options from Oracle.
- **Indexing**: PostgreSQL supports advanced indexing techniques; MySQL supports basic indexing.
- **Foreign Keys**: Fully supported in PostgreSQL; supported in MySQL’s InnoDB engine but not in MyISAM.

# Note — Since Java is releasing newer versions every years, make sure you know these features. interviewer may ask to check how update you are.

## **What are the Features of Java 8?**

Java 8 introduced several significant features and enhancements:

1. **Lambda Expressions**: Enables functional programming by allowing you to pass functions as arguments.
2. **Stream API**: Facilitates functional-style operations on collections, such as map, filter, and reduce.
3. **Optional Class**: Helps in handling null values more gracefully, reducing the risk of `NullPointerException`.
4. **Default Methods**: Allows methods in interfaces to have a default implementation.
5. **Functional Interfaces**: Interfaces with a single abstract method, used primarily with lambda expressions.
6. **Date and Time API**: A new, comprehensive API for date and time manipulation (java.time package).
7. **Nashorn JavaScript Engine**: A new JavaScript engine for embedding JavaScript code within Java applications.
8. **Method References**: A shorthand notation for calling methods via lambda expressions.
9. **Type Annotations**: Enhanced support for annotations, allowing them to be used in more places.
10. **Repeating Annotations**: Allows the same annotation to be applied multiple times to the same declaration.

## **What are the Features of Java 17?**

Java 17, a Long-Term Support (LTS) release, introduced several new features and enhancements:

1. **Sealed Classes**: Restricts which classes can extend or implement them, providing more control over the class hierarchy.
2. **Pattern Matching for `switch` (Preview)**: Enhances the `switch` statement to support pattern matching, making it more powerful and expressive.
3. **Records**: Provides a compact syntax for declaring classes that are primarily used to store data.
4. **Text Blocks**: Simplifies the creation of multi-line string literals.
5. **Enhanced `switch` Expressions**: Allows `switch` to be used as an expression, returning a value.
6. **Foreign Function & Memory API (Incubator)**: Facilitates interaction with native code and memory outside the Java heap.
7. **Removal of Deprecated APIs**: Removal of older, deprecated APIs and features to clean up the language.
8. **Strong Encapsulation by Default**: Modules now strongly encapsulate all internal elements by default.
9. **New macOS Rendering Pipeline**: A new rendering pipeline for macOS, using the Apple Metal API.
10. **Deprecation of the Applet API**: The Applet API is deprecated for removal in a future release.

# Singleton and Immutability are darling questions for every interviewer make sure you know the concept very well

## **What is the difference between these two Singleton and immutability?**

Singleton and immutability are two distinct design concepts in software engineering. Here are the key differences:

Singleton

1. **Purpose**: Ensures that a class has only one instance and provides a global point of access to it.
2. **Implementation**: Typically involves a private constructor, a static method to get the instance, and a static variable to hold the instance.
3. **State**: The single instance can have mutable state, meaning its fields can be changed after the instance is created.
4. **Usage**: Commonly used for managing shared resources like configuration settings, logging, or connection pools.

Immutability

1. **Purpose**: Ensures that an object’s state cannot be changed after it is created.
2. **Implementation**: Typically involves making all fields `final`, providing no setters, and ensuring that any mutable objects passed to the constructor are deeply copied.
3. **State**: The object’s state is fixed after construction and cannot be altered.
4. **Usage**: Commonly used for value objects, thread-safe data structures, and functional programming.

Summary

- **Singleton**: Focuses on having a single instance of a class with potentially mutable state.
- **Immutability**: Focuses on creating objects whose state cannot change after they are constructed.

## **How to break singleton design pattern?**

Breaking the Singleton design pattern can be done in several ways, often unintentionally. Here are some common methods:

1. Reflection

Reflection can be used to access the private constructor of a Singleton class, creating multiple instances.

```
import java.lang.reflect.Constructor;

public class SingletonBreaker {
    public static void main(String[] args) {
        Singleton instanceOne = Singleton.getInstance();
        Singleton instanceTwo = null;

        try {
            Constructor<Singleton> constructor = Singleton.class.getDeclaredConstructor();
            constructor.setAccessible(true);
            instanceTwo = constructor.newInstance();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println(instanceOne.hashCode());
        System.out.println(instanceTwo.hashCode());
    }
}

class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

2. Serialization and Deserialization

Serialization and deserialization can create a new instance of the Singleton class

```
import java.io.*;

public class SingletonBreaker {
    public static void main(String[] args) {
        Singleton instanceOne = Singleton.getInstance();
        Singleton instanceTwo = null;

        try (ObjectOutput out = new ObjectOutputStream(new FileOutputStream("singleton.ser"))) {
            out.writeObject(instanceOne);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (ObjectInput in = new ObjectInputStream(new FileInputStream("singleton.ser"))) {
            instanceTwo = (Singleton) in.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(instanceOne.hashCode());
        System.out.println(instanceTwo.hashCode());
    }
}

class Singleton implements Serializable {
    private static final long serialVersionUID = 1L;
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    // To prevent creating a new instance during deserialization
    protected Object readResolve() {
        return getInstance();
    }
}
```

3. Cloning

Cloning can create a new instance of the Singleton class.

```
public class SingletonBreaker {
    public static void main(String[] args) {
        Singleton instanceOne = Singleton.getInstance();
        Singleton instanceTwo = null;

        try {
            instanceTwo = (Singleton) instanceOne.clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }

        System.out.println(instanceOne.hashCode());
        System.out.println(instanceTwo.hashCode());
    }
}

class Singleton implements Cloneable {
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
        return super.clone();
    }
}
```

4. Multiple Class Loaders

Different class loaders can load the Singleton class multiple times, creating multiple instances.

**Preventing Singleton Breakage**

To prevent these issues, you can:

- Use an enum to implement Singleton, which is inherently safe from reflection, serialization, and cloning issues.
- Implement `readResolve` method for serialization.
- Override `clone` method to throw `CloneNotSupportedException`.

```
public enum Singleton {
    INSTANCE;
}
```

Using an enum is the most robust way to implement a Singleton in Java.

## **What is data engine?**

A data engine, often referred to as a database engine or storage engine, is the underlying software component that a database management system (DBMS) uses to create, read, update, and delete (CRUD) data from a database. It is responsible for managing how data is stored, retrieved, and manipulated.

## **What will happen if we exchange @Repository and @Service annotations in spring boot project?**

What Happens if Exchanged?

1. **Functionality**: The primary functionality of the application may still work because both annotations make the classes Spring-managed beans. However, the specific roles and behaviors associated with each annotation will be lost.
2. **Exception Translation**: If you annotate a DAO class with `@Service` instead of `@Repository`, you will lose the automatic exception translation feature provided by `@Repository`.
3. **Semantics**: The code will become semantically incorrect, making it harder for other developers to understand the intended design and architecture of the application.
4. **Best Practices**: Violating best practices and conventions can lead to maintenance challenges and potential bugs in the future.

## **What is functional interface?**

A functional interface in Java is an interface that contains exactly one abstract method. It can have multiple default or static methods, but only one abstract method. Functional interfaces are used primarily for lambda expressions and method references.

Key Points:

- **Single Abstract Method**: Must have exactly one abstract method.
- **@FunctionalInterface Annotation**: Optional but recommended to indicate that the interface is intended to be a functional interface.
- **Usage**: Enables the use of lambda expressions and method references, promoting functional programming in Java.

```
@FunctionalInterface
public interface MyFunctionalInterface {
    void execute(); // Single abstract method

    // Default method
    default void defaultMethod() {
        System.out.println("Default method");
    }

    // Static method
    static void staticMethod() {
        System.out.println("Static method");
    }
}

// Using a lambda expression with the functional interface
MyFunctionalInterface func = () -> System.out.println("Executing...");
func.execute();
```

# Everyone loves Java’s HashMap, make sure you have prepared it well.

## **What is default size of HashMap?**

The default initial capacity of a `HashMap` in Java is 16. This means that when a `HashMap` is created without specifying an initial capacity, it will have an initial capacity of 16 buckets.

Key Points:

- **Initial Capacity**: The number of buckets in the hash table, initially set to 16.
- **Load Factor**: The default load factor is 0.75, which means the `HashMap` will be resized when 75% of the capacity is filled.
- **Threshold**: The point at which the `HashMap` will resize, calculated as `initial capacity * load factor` (e.g., 16 * 0.75 = 12).

```
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        // Creating a HashMap with default initial capacity (16) and load factor (0.75)
        HashMap<String, String> map = new HashMap<>();

        // Adding elements to the HashMap
        map.put("key1", "value1");
        map.put("key2", "value2");

        // Printing the HashMap
        System.out.println(map);
    }
}
```

## **What is load factor?**

The default initial capacity of a `HashMap` in Java is 16, with a default load factor of 0.75. This configuration helps balance memory usage and performance, providing a good trade-off between space and time complexity for most use cases.

## **What happens if size increases beyond load factor?**

When the size of a `HashMap` exceeds its load factor threshold, the `HashMap` automatically resizes itself to maintain efficient performance. This process is known as rehashing.

Steps Involved in Resizing:

1. **Calculate New Capacity**: The new capacity is typically double the current capacity.
2. **Rehash Entries**: All existing entries are rehashed and redistributed into the new, larger array of buckets.

Key Points:

- **Load Factor**: The default load factor is 0.75. When the number of entries exceeds `capacity * load factor`, resizing occurs.
- **Threshold**: The threshold is the point at which resizing happens, calculated as `initial capacity * load factor`.
- **Performance Impact**: Resizing is an expensive operation because it involves rehashing all existing entries, but it ensures that the `HashMap` maintains efficient performance for future operations.

```
import java.util.HashMap;

public class HashMapResizeExample {
    public static void main(String[] args) {
        // Creating a HashMap with default initial capacity (16) and load factor (0.75)
        HashMap<Integer, String> map = new HashMap<>();

        // Adding elements to the HashMap
        for (int i = 0; i < 20; i++) {
            map.put(i, "Value" + i);
        }

        // Printing the HashMap
        System.out.println(map);
    }
}
```

In this example, when the number of entries exceeds 12 (16 * 0.75), the `HashMap` will resize itself to a new capacity of 32.

# **Summary:**

When the size of a `HashMap` exceeds its load factor threshold, the `HashMap` resizes itself by doubling its capacity and rehashing all existing entries. This ensures that the `HashMap` maintains efficient performance, though the resizing operation itself is computationally expensive.

# **Top 15 DS Algo Interview Questions for Java Developers(Commonly Asked)**

1. **Print all substrings of a string (List every possible substring)**

```
ublic class SubstringPrinter {

    public static void main(String[] args) {
        String str = "example";
        printAllSubstrings(str);
    }

    public static void printAllSubstrings(String str) {
        int n = str.length();
        // Loop through all possible starting points of substrings
        for (int i = 0; i < n; i++) {
            // Loop through all possible ending points of substrings
            for (int j = i + 1; j <= n; j++) {
                // Print the substring from index i to j
                System.out.println(str.substring(i, j));
            }
        }
    }
}
```

Explanation:

1. **Outer Loop (`i`)**: Iterates through each character in the string as the starting point of the substring.
2. **Inner Loop (`j`)**: Iterates from the current starting point (`i`) to the end of the string, defining the ending point of the substring.
3. **`str.substring(i, j)`**: Extracts and prints the substring from index `i` to `j`.

**2. Return all subsequences of a string(Generate all possible subsequences, not necessarily contiguous).**

```
import java.util.ArrayList;
import java.util.List;

public class SubsequenceGenerator {

    public static void main(String[] args) {
        String str = "abc";
        List<String> subsequences = generateAllSubsequences(str);
        System.out.println(subsequences);
    }

    public static List<String> generateAllSubsequences(String str) {
        List<String> subsequences = new ArrayList<>();
        generateSubsequencesHelper(str, "", 0, subsequences);
        return subsequences;
    }

    private static void generateSubsequencesHelper(String str, String current, int index, List<String> subsequences) {
        if (index == str.length()) {
            subsequences.add(current);
            return;
        }

        // Include the current character
        generateSubsequencesHelper(str, current + str.charAt(index), index + 1, subsequences);

        // Exclude the current character
        generateSubsequencesHelper(str, current, index + 1, subsequences);
    }
}
```

Explanation:

1. **`generateAllSubsequences` Method**: Initializes the list to store subsequences and calls the helper method.
2. **`generateSubsequencesHelper` Method**: Recursively generates subsequences.
- **Base Case**: When the index reaches the length of the string, add the current subsequence to the list.
- **Recursive Case**:
- Include the current character and move to the next index.
- Exclude the current character and move to the next index.

This method ensures that all possible subsequences (including the empty subsequence) are generated and returned.

## **3. Rotate an array to the right by k steps— Shift elements right by k positions.**

```
import java.util.Arrays;

public class ArrayRotator {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        rotateRight(arr, k);
        System.out.println(Arrays.toString(arr));
    }

    public static void rotateRight(int[] arr, int k) {
        int n = arr.length;
        k = k % n; // In case k is greater than the length of the array
        reverse(arr, 0, n - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
    }

    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

Explanation:

1. **`rotateRight` Method**:
- **Step 1**: Calculate the effective rotation steps `k` by taking `k % n` (where `n` is the length of the array) to handle cases where `k` is greater than the array length.
- **Step 2**: Reverse the entire array.
- **Step 3**: Reverse the first `k` elements.
- **Step 4**: Reverse the remaining `n - k` elements.

**`reverse` Method**: Reverses the elements in the array between the specified `start` and `end` indices.

## **4. Rotate an array to the left by d steps— Shift elements left by d positions.**

```
import java.util.Arrays;

public class ArrayRotator {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int d = 3;
        rotateLeft(arr, d);
        System.out.println(Arrays.toString(arr));
    }

    public static void rotateLeft(int[] arr, int d) {
        int n = arr.length;
        d = d % n; // In case d is greater than the length of the array
        reverse(arr, 0, d - 1);
        reverse(arr, d, n - 1);
        reverse(arr, 0, n - 1);
    }

    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

Explanation:

1. **`rotateLeft` Method**:
- **Step 1**: Calculate the effective rotation steps `d` by taking `d % n` (where `n` is the length of the array) to handle cases where `d` is greater than the array length.
- **Step 2**: Reverse the first `d` elements.
- **Step 3**: Reverse the remaining `n - d` elements.
- **Step 4**: Reverse the entire array.

**`reverse` Method**: Reverses the elements in the array between the specified `start` and `end` indices.

This approach ensures that the array is rotated to the left by `d` steps efficiently with a time complexity of O(n).

## **5. String compression— Compress repeated characters into counts.**

```
public class StringCompressor {

    public static void main(String[] args) {
        String str = "aaabbbcccaaa";
        String compressed = compressString(str);
        System.out.println(compressed);
    }

    public static String compressString(String str) {
        if (str == null || str.length() == 0) {
            return str;
        }

        StringBuilder compressed = new StringBuilder();
        int count = 1;

        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == str.charAt(i - 1)) {
                count++;
            } else {
                compressed.append(str.charAt(i - 1)).append(count);
                count = 1;
            }
        }

        // Append the last character and its count
        compressed.append(str.charAt(str.length() - 1)).append(count);

        // Return the original string if compression does not reduce the size
        return compressed.length() < str.length() ? compressed.toString() : str;
    }
}
```

Explanation:

1. **Edge Case Handling**: Check if the input string is null or empty and return it as is.
2. **StringBuilder**: Use `StringBuilder` for efficient string concatenation.
3. **Count Repeated Characters**: Iterate through the string and count consecutive repeated characters.
4. **Append Character and Count**: Append each character and its count to the `StringBuilder`.
5. **Handle Last Character**: After the loop, append the last character and its count.
6. **Return Result**: Return the compressed string if it is shorter than the original string; otherwise, return the original string.

## **6. Find the maximum element in an array that first increases and then decreases— Identify the peak element.**

```
public class PeakElementFinder {

    public static void main(String[] args) {
        int[] arr = {1, 3, 8, 12, 4, 2};
        int peak = findPeakElement(arr);
        System.out.println("The peak element is: " + peak);
    }

    public static int findPeakElement(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] < arr[mid + 1]) {
                // Peak is in the right half
                left = mid + 1;
            } else {
                // Peak is in the left half or at mid
                right = mid;
            }
        }

        // left and right will converge to the peak element
        return arr[left];
    }
}
```

Explanation:

1. **Binary Search Approach**: Use binary search to efficiently find the peak element.
2. **Initialization**: Initialize `left` to 0 and `right` to the last index of the array.
3. **Binary Search Loop**:
- Calculate the middle index `mid`.
- Compare `arr[mid]` with `arr[mid + 1]`:
- If `arr[mid] < arr[mid + 1]`, the peak is in the right half, so move `left` to `mid + 1`.
- Otherwise, the peak is in the left half or at `mid`, so move `right` to `mid`.

**Convergence**: The loop continues until `left` and `right` converge to the peak element.

**Return Peak**: Return the element at the converged index.

This method ensures that the peak element is found efficiently with a time complexity of O(log n).

## **7. Height of a binary tree— Find the maximum depth of the tree.**

```
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class BinaryTreeHeight {

    public static void main(String[] args) {
        // Example tree:
        //      1
        //     / \
        //    2   3
        //   / \
        //  4   5
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        int height = findHeight(root);
        System.out.println("The height of the binary tree is: " + height);
    }

    public static int findHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftHeight = findHeight(root.left);
        int rightHeight = findHeight(root.right);

        return Math.max(leftHeight, rightHeight) + 1;
    }
}
```

Explanation:

1. **TreeNode Class**: Defines the structure of a tree node with a value and left and right children.
2. **findHeight Method**:
- **Base Case**: If the node is `null`, return 0 (indicating no height).
- **Recursive Case**: Recursively find the height of the left and right subtrees.
- **Calculate Height**: The height of the current node is the maximum of the heights of its left and right subtrees plus one.

**Example Tree**: Constructs a sample binary tree and calculates its height.

## **8. Find the largest subarray sum— Calculate the continuous subarray with the highest sum (Kadane’s algorithm).**

```
public class LargestSubarraySum {

    public static void main(String[] args) {
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int maxSum = findLargestSubarraySum(arr);
        System.out.println("The largest subarray sum is: " + maxSum);
    }

    public static int findLargestSubarraySum(int[] arr) {
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];

        for (int i = 1; i < arr.length; i++) {
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }
}
```

Explanation:

**Initialization**:

- `maxSoFar`: Keeps track of the maximum sum found so far.
- `maxEndingHere`: Keeps track of the maximum sum of the subarray ending at the current position.

**Iteration**:

- For each element in the array, update `maxEndingHere` to be the maximum of the current element itself or the current element plus the previous `maxEndingHere`.
- Update `maxSoFar` to be the maximum of `maxSoFar` and `maxEndingHere`.

**Return Result**: After iterating through the array, `maxSoFar` will contain the largest subarray sum.

## **9. Majority element (Boyer–Moore algorithm)— Find the element that appears more than n/2 times.**

```
public class MajorityElementFinder {

    public static void main(String[] args) {
        int[] arr = {2, 2, 1, 1, 1, 2, 2};
        int majorityElement = findMajorityElement(arr);
        System.out.println("The majority element is: " + majorityElement);
    }

    public static int findMajorityElement(int[] arr) {
        int candidate = findCandidate(arr);
        return validateCandidate(arr, candidate) ? candidate : -1;
    }

    private static int findCandidate(int[] arr) {
        int count = 0;
        Integer candidate = null;

        for (int num : arr) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }

    private static boolean validateCandidate(int[] arr, int candidate) {
        int count = 0;
        for (int num : arr) {
            if (num == candidate) {
                count++;
            }
        }
        return count > arr.length / 2;
    }
}
```

Explanation:

**findMajorityElement Method**:

- Calls `findCandidate` to identify a potential majority element.
- Calls `validateCandidate` to confirm if the candidate is indeed the majority element.

**findCandidate Method**:

- Uses the Boyer-Moore Voting Algorithm to find a candidate for the majority element.
- Iterates through the array, adjusting the count based on whether the current element matches the candidate.
- If the count drops to zero, the current element becomes the new candidate.

**validateCandidate Method**:

- Validates the candidate by counting its occurrences in the array.
- Returns true if the candidate appears more than `n/2` times, otherwise false.

## **10. Find triplets in an array with a given sum— Locate all triplets matching the specified sum.**

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TripletFinder {

    public static void main(String[] args) {
        int[] arr = {1, 4, 45, 6, 10, 8};
        int sum = 22;
        List<List<Integer>> triplets = findTriplets(arr, sum);
        for (List<Integer> triplet : triplets) {
            System.out.println(triplet);
        }
    }

    public static List<List<Integer>> findTriplets(int[] arr, int sum) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(arr);

        for (int i = 0; i < arr.length - 2; i++) {
            if (i > 0 && arr[i] == arr[i - 1]) {
                continue; // Skip duplicates
            }
            int left = i + 1;
            int right = arr.length - 1;

            while (left < right) {
                int currentSum = arr[i] + arr[left] + arr[right];
                if (currentSum == sum) {
                    result.add(Arrays.asList(arr[i], arr[left], arr[right]));
                    while (left < right && arr[left] == arr[left + 1]) left++; // Skip duplicates
                    while (left < right && arr[right] == arr[right - 1]) right--; // Skip duplicates
                    left++;
                    right--;
                } else if (currentSum < sum) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}
```

**Sorting**: Sort the array to facilitate the two-pointer approach.

**Iterate through the array**:

- Use a loop to fix the first element of the triplet.
- Use two pointers (`left` and `right`) to find the other two elements.

**Two-pointer approach**:

- Initialize `left` to the element next to the fixed element and `right` to the last element.
- Calculate the current sum of the triplet.
- If the current sum matches the target sum, add the triplet to the result list and move both pointers inward, skipping duplicates.
- If the current sum is less than the target sum, move the `left` pointer to the right to increase the sum.
- If the current sum is greater than the target sum, move the `right` pointer to the left to decrease the sum.

**Skip Duplicates**: Ensure that duplicate elements are skipped to avoid duplicate triplets in the result.

This method ensures that all unique triplets that sum up to the given value are found efficiently with a time complexity of O(n²).

## **11. Merge intervals— Combine overlapping intervals into one.**

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {

    public static void main(String[] args) {
        int[][] intervals = { {1, 3}, {2, 6}, {8, 10}, {15, 18} };
        int[][] merged = merge(intervals);
        for (int[] interval : merged) {
            System.out.println(Arrays.toString(interval));
        }
    }

    public static int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][];
        }

        // Sort intervals by their start times
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> merged = new ArrayList<>();
        int[] currentInterval = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            // If the current interval overlaps with the next, merge them
            if (intervals[i][0] <= currentInterval[1]) {
                currentInterval[1] = Math.max(currentInterval[1], intervals[i][1]);
            } else {
                merged.add(currentInterval);
                currentInterval = intervals[i];
            }
        }

        merged.add(currentInterval);
        return merged.toArray(new int[merged.size()][]);
    }
}
```

**Sorting**: The intervals are sorted based on their starting values.

**Merging Process**:

- Iterate over the sorted intervals.
- If the current interval overlaps with the next one (i.e., the start of the next interval is less than or equal to the end of the current interval), they are merged by updating the end.
- If they do not overlap, add the current interval to the result list and move to the next interval.

**Final Output**: The merged intervals are converted back to a 2D array and returned.

## **12. Non-overlapping intervals— Find maximum or minimum sets of intervals that do not overlap.**

Below is a Java solution using a greedy approach to select the maximum set of non-overlapping intervals. The solution sorts intervals by their end times and then iterates through, selecting intervals that do not conflict with the previously chosen interval.

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NonOverlappingIntervals {

    public static void main(String[] args) {
        int[][] intervals = { {1, 3}, {2, 4}, {3, 5}, {7, 9}, {8, 10} };
        List<int[]> selectedIntervals = maxNonOverlappingIntervals(intervals);

        System.out.println("Maximum set of non-overlapping intervals:");
        for (int[] interval : selectedIntervals) {
            System.out.println(Arrays.toString(interval));
        }
    }

    public static List<int[]> maxNonOverlappingIntervals(int[][] intervals) {
        // Sort intervals based on end times
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        List<int[]> result = new ArrayList<>();
        int lastEnd = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            // If the current interval does not overlap with the previously selected one, select it.
            if (interval[0] >= lastEnd) {
                result.add(interval);
                lastEnd = interval[1];
            }
        }
        return result;
    }
}
```

Explanation:

**Sorting**:

- The intervals are sorted by their end times so that the interval with the earliest end can be chosen first. This minimizes conflicts with future intervals.

**Greedy Selection**:

- Initialize `lastEnd` to a very small value.
- Iterate over sorted intervals. For each interval, if its start time is greater than or equal to `lastEnd` (indicating no overlap with the last selected interval), add it to the result.
- Update `lastEnd` to the end of the selected interval.

**Result**:

- The list `result` contains the maximum number of intervals that do not overlap.

## **13. Diameter of a binary tree— Determine the longest path between any two nodes.**

```
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class BinaryTreeDiameter {

    // This variable will hold the maximum diameter found during recursion.
    private static int diameter = 0;

    public static void main(String[] args) {
        // Example tree:
        //      1
        //     / \
        //    2   3
        //   / \
        //  4   5
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        int treeDiameter = findDiameter(root);
        System.out.println("The diameter of the binary tree is: " + treeDiameter);
    }

    public static int findDiameter(TreeNode root) {
        diameter = 0; // reset diameter before computing
        depth(root);
        return diameter;
    }

    // Helper method to calculate depth of tree and update diameter.
    private static int depth(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftDepth = depth(node.left);
        int rightDepth = depth(node.right);

        // Update the diameter if the path through the current node is larger.
        diameter = Math.max(diameter, leftDepth + rightDepth);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

**TreeNode Class**:

- Represents each node in the binary tree.

**findDiameter Method**:

- Resets `diameter` and calls the helper method `depth` to compute the depth of the tree while updating the diameter.

**depth Method**:

- Recursively computes the depth of each subtree.
- At each node, the potential diameter passing through that node is `leftDepth + rightDepth`.
- Updates the global `diameter` variable if this potential diameter is greater than the current maximum.
- Returns the maximum depth from the current node.

This approach finds the longest path (diameter) in the binary tree efficiently with a time complexity of O(n).

## **14. Reverse a linked list in groups of K— Reverse nodes of the list in batches of K elements.**

```
public class ReverseLinkedListInGroups {

    // Definition for singly-linked list.
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public static ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;

        // Check if there are at least k nodes left in the list.
        while (curr != null && count < k) {
            curr = curr.next;
            count++;
        }

        // If we have k nodes, then reverse them.
        if (count == k) {
            // Recursively reverse the rest of the list.
            curr = reverseKGroup(curr, k);
            // Reverse current k-group.
            while (count-- > 0) {
                ListNode temp = head.next;
                head.next = curr;
                curr = head;
                head = temp;
            }
            head = curr;
        }
        return head;
    }

    public static void main(String[] args) {
        // Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        int k = 3; // Group size to reverse.
        head = reverseKGroup(head, k);

        // Print the modified linked list.
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
    }
}
```

**ListNode Class**: Defines the structure of a linked list node.

**reverseKGroup Method**:

- **Count K Nodes**: Check if there are at least k nodes remaining.
- **Recursive Reversal**: If there are, recursively reverse the rest of the list.
- **Reverse Current Group**: Reverse the links in the current group of k nodes.

**Main Method**: Creates a sample list, applies the reversal in groups of k, and prints the result.

## **15. LRU Cache implementation— Design a cache with least recently used eviction.**

```
import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;

    public LRUCache(int capacity) {
        // true for access-order, false for insertion-order
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }

    // Test the LRUCache
    public static void main(String[] args) {
        LRUCache<Integer, String> cache = new LRUCache<>(3);

        cache.put(1, "One");
        cache.put(2, "Two");
        cache.put(3, "Three");
        System.out.println("Cache content: " + cache);

        // Access some elements
        cache.get(1);
        cache.put(4, "Four"); // This should evict key 2 as it is the least recently used.

        System.out.println("After accessing key 1 and adding key 4: " + cache);
    }
}
```

- **Extending LinkedHashMap**:The constructor configures the map for access-order (setting the third parameter to `true`) so that the least recently accessed element is removed first.
- **removeEldestEntry**:This overridden method checks whether the cache size exceeds the defined capacity and, if so, automatically removes the eldest entry.
- **Usage**:In the `main` method, a cache of capacity 3 is created. After adding elements and accessing one of them, adding a new element will cause the least recently used entry to be evicted.
- This implementation provides an efficient cache with O(1) operations for get and put, leveraging the built-in capabilities of Java’s LinkedHashMap.