# Medium interview questions part 2

## **Basics :**

1. What are JDK, JRE, and JVM?
2. Explain Abstraction and Encapsulation?
3. What is Inheritance, Aggregation, and Association?
4. What is a try-with resource in java?
5. Explain different J[ava 8 features](https://ds73306.medium.com/important-java-8-features-e52c8d8e8662)?
6. Why is String immutable in Java?
7. Explain the JVM memory model?
8. Explain Garbage Collection?
9. What are exceptions and what is exception handling?
10. Explain Autoboxing and Unboxing?
11. What is Typecasting? Explain with Parent-Child inheritance example.
12. Why is the Java platform independent?
13. How many ways can we create objects in java?
14. What is the Collections framework?
15. Explain static, this, and super keyword?
16. Explain finally, finalize and final keyword?

## **Advanced :**

1. What is Serialization?
2. Explain the Internal working of a HashMap? ([answer](https://www.java67.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html))
3. What is Concurrent HashMap? ([answer](https://javarevisited.blogspot.com/2020/09/10-examples-of-concurrenthashmap-in-java.html))
4. Difference between ArrayList and LinkedList. ([answer](https://www.java67.com/2012/12/difference-between-arraylist-vs-LinkedList-java.html))
5. Difference between Comparator and Comparable.
6. What is the default size of ArrayList and HashMap?
7. What are Marker Interfaces and Functional Interfaces?
8. Explain Classloading in java and types of classloaders?
9. What are Generics in Java?
10. How can we create a custom Exception?
11. What is the Covariant return type? ([answer](https://javarevisited.blogspot.com/2014/03/covariant-method-overriding-of-java-5.html))
12. What is Threading?
13. What are Daemon threads?
14. Difference between start() and run() ? ([answer](https://www.java67.com/2015/12/difference-between-thread-start-and-run-method-java.html))
15. What is the Volatile keyword?
16. Difference between Synchronized method and block?
17. Difference between sleep(), wait () , yeild() ?
18. What do you mean by Deadlock?
19. Explain Join()?
20. What are ThreadLocal and Threadpool?
21. Explain hashcode() and equals() .Explain with example of HashSet.
22. What is the immutable class? How can you make a class immutable?
23. What is Singleton?
24. Difference between classNotFound and NoClassDefinitionFound? ([answer](https://javarevisited.blogspot.com/2011/07/classnotfoundexception-vs.html#axzz6H3LuQtU5))
25. What is Consumer, Predicate, Supplier?
26. Difference between map() and flatMap() ? ([answer](https://javarevisited.blogspot.com/2016/03/difference-between-map-and-flatmap-in-java8.html))
27. Example to sort a map to get highest occurring character using stream API.

## **Q1 — What is the output of the given Java code?**

```
public class Test { public static void main(String[] args) {
  method(null);
 }
 public static void method(Object o) {
  System.out.println("Object method");
 }
 public static void method(String s) {
  System.out.println("String method");
 }}
```

## **Answer**

It will print “String method”. First of all, null is not an object in Java. But we know that we can assign null to any object reference type in Java. Java String is also an object of the class `java.lang.String`. Here, the Java compiler chooses to call the overloaded method with the most specific parameters. Which would be String because the String class is more specific than the Object class.

## **Q2 — What will be the output of the given Java code?**

```
public class Test{public static void main(String[] args){
  Integer num1 = 100;
  Integer num2 = 100;  if(num1==num2){
   System.out.println("num1 == num2");
  }
  else{
   System.out.println("num1 != num2");
  }
 }
}
```

## **Answer**

It will print “num1 == num2”. Whenever two different object references are compared using “==,” the value is always “false.” But here, because of the Integer caching, num1 and num2 are autoboxed. Thus `num1==num2` returns “true”. Integer caching happens only for values between -128 and 127.

## **Q3 — How does Garbage Collection prevent a Java application from going out of memory?**

## **Answer**

Java Garbage Collector does not prevent a Java application from going out of memory. It simply cleans the unused memory when an object is out of scope and no longer needed. As a result, garbage collection is not guaranteed to prevent a Java app from going out of memory.

## **Q4 — Is Java “pass-by-reference” or “pass-by-value”?**

## **Answer**

Java is always “pass-by-value”. However, when we pass the value of an object, we pass the reference to it because the variables store the object reference, not the object itself. But this isn’t “pass-by-reference.” This could be confusing for beginners.

## **Q5 — How many String objects are created by the below code?**

```
public class Test{
 public static void main(String[] args){
   String s = new String("Hello World");
 }
}
```

## **Answer**

Two String objects are created. When the new operator is used to create a String object, if the object does not exist in the Java String Pool, it will first be created in it, and then in the heap memory as well. You can simply learn all about Java Strings in my article below.

[**String, StringBuilder, and StringBuffer Do You Know the Difference?A complete guide for Strings in Java**medium.com](https://archive.ph/o/HcypA/https://medium.com/javarevisited/string-stringbuilder-and-stringbuffer-do-you-know-the-difference-6a53429dcf)

## **Q6 — What is the output of the below Java code?**

```
public class Test{
 public static void main(String[] arr){
    System.out.println(0.1*3 == 0.3);
    System.out.println(0.1*2 == 0.2);
 }
}
```

## **Answer**

The first print statement prints “false” and the second prints “true”. This happens simply because of the rounding error in floating-point numbers. Only numbers that are powers of 2 can be represented precisely by a simple binary representation. Numbers that do not correspond to a power of 2 must be rounded to fit into a limited number of bits. Here, because Java uses double to represent decimal values, only 64 bits are available to represent the number. Therefore, `0.1*3` would not be equal to `0.3`.

## **Q7 — Is it possible to override or overload a static method in Java?**

## **Answer**

It’s possible to overload static Java methods, but it’s not possible to override them. You can write another static method with the same signature in the subclass, but it’s not going to override the superclass method. It’s called method hiding in Java.

## **Q8 — What’s the most reliable way to test whether two double values are equal?**

## **Answer**

The most reliable and accurate way to determine whether two double values are equal to each other is to use `Double.compare()` and test it against 0.

`Double.compare(d1, d2) == 0`

## **Q9 — Will the finally block be executed if the try or catch block executes a return statement?**

## **Answer**

Yes, the finally block will still be executed even if a return statement was executed in a try or catch block. This is a very popular and tricky Java question. The only way we can stop finally block from being executed is to use the `System.exit()` method.

## **Q10 — What happens when we run the below Java code?**

```
public class Test{
 public static void main(String[] args){
  System.out.println("main method");
 }
 public static void main(String args){
  System.out.println("Overloaded main method");
 }
}
```

## **Answer**

It prints “main method”. There will be no error or exception because the main method can be overloaded in Java. It has to be called from within the main method to be executed just like any other method.

# **OOP Questions**

These questions apply not only to Java, but object oriented languages in general.

*1. Compare interfaces and abstract classes*

Both are used to achieve **abstraction**. Neither can be instantiated. An abstract class can have concrete implementations, an interface cannot. An interface is like a contract — a structure that classes implementing it must adhere to. Abstract classes are used to hide internals and expose relevant functionality — one doesn’t have to know how an abstract class does something in order to use it.

*2. Explain inheritance*

Making one object the child of another gives the child all properties and methods (with respect to access modifiers) of its parent and ancestors. That is inheritance — it is used to achieve code **reusability** and **polymorphism**. In Java, as in most modern languages, an object can only have one parent — Java does not support multiple inheritance. Inheritance creates tight coupling between the parent and its children, which is why dependency injection is often a preferred alternative, as it allows related pieces of code to be decoupled.

*3. Explain polymorphism*

Polymorphism means an object can belong to **two or more types**. It can be achieved through **inheritance** and **interfaces**. For example, a `Cat` object extending `Mammal` and implementing `LandAnimal` is an instance of all three of those types. Method overloading and overriding is used to achieve flexible behavior when implementing a polymorphic class hierarchy.

*4. Compare association, aggregation, and composition*

These terms are used to describe **relational structures** in a class hierarchy. Association describes how objects relate to/are associated with each other (1–1, 1-N, N-1, N-M). It can be achieved through aggregation and composition. Aggregation describes **“is-a”** relationships — Each object can exist independently. Composition describes **“has-a”** relationships — Objects cannot exist independently.

*5. How would you model an ER Diagram for a social media website?*

There are many ways to answer this one. A first approach could look something like this:

```
User
* Id: Long
* Name: String

Post
* Id: Long
* Likes: Integer

Thread
* Id: Long
* Post: ForeignKey<Post>
```

# **Java Questions**

*6. What can you tell me about memory management and garbage collection in Java?*

Both are **automatically handled by the JVM**. The garbage collector periodically collects variables without any references. Programmers can tell the garbage collector to schedule garbage collection with `System.gc()`, but it’s not guaranteed when that will happen. The two most important memory areas in the JVM are the stack and the heap. They are used for different purposes. The stack is used to hold method frames and local variables, and is **not shared** between threads. Objects are always allocated memory from the heap, which is **shared** between all threads in the JVM. The stack is usually much smaller than heap memory.

*7. What can you tell me about Generics in Java?*

Generics can be used in conjunction with classes and methods. They’re used to specify a **single declaration** for a set of related methods, or a single class declaration for a set of related types. Generics are checked at compile-time for type safety. Two examples are `ArrayList<T>` and three classes representing daily, monthly, and yearly charts that extend an abstract `Chart` and can be specified with `<? extends Chart>`.

*8. What can you tell me about Java Optionals?*

They encapsulate optional values, and are used to make code more readable, stable, and avoid having to deal with **null** values, thus avoiding `NullPointerExceptions`.

*9. Explain the difference between `stream()`and `parallelStream()`.*

A regular stream is always **synchronized**, whereas a parallel stream can execute operations **asynchronously** across CPU cores. Unless running a heavy operation on a lot of objects, one should use regular streams, as parallel streams have a high overhead for setting up multithreading.

*10. What is `ClassLoader` in Java?*

The part of the JVM that loads **bytecodes** for classes at runtime.

*11. When is it appropriate to use a transient variable in Java?*

Use transient variables, when you want to make a variable **non-serializable** in a class that implements the `Serializable` interface.

*12. Can private methods be overwritten in Java?*

No, because private methods are **not visible** in the subclass.

*13. What is the difference between lists and sets in Java?*

They differ in how their items’ **ordering** and **uniqueness**. Lists are ordered and allow duplicate values. Sets are unordered and do not allow duplicate elements.

*14. Which two methods do you have to override for an object to be usable as a key in a hash map?*

To be usable as a key in a hash map, an object needs to be **comparable** and define a **hash function**. You have to overwrite `equals()` and `hashCode()`.

*15. What’s the difference between method overloading and overriding in Java?*

**Overriding** happens in a subclass. **Overloading** happens in the same class.

*16. How do you prevent a class from being sub-classed in Java?*

You can either make the constructor of the class private, or mark the class as `final`.

*17. What’s the difference between `this` and `super` in Java?*

`this` refers to the **current** instance of an object. `super` refers to an instance of the **parent**/superclass.

*18. Will `3*0.1 == 0.3` return true or false?*

This will return **false**, because some floating point numbers cannot be represented exactly.

*19. What is the right data type to represent a price in Java?*

`BigDecimal` if **memory** is not a concern and **performance** is not critical, otherwise `double` with a predefined precision.

*20. Why is String immutable in Java?*

Because Java was designed on the assumption that strings will be heavily used. Making it immutable allows for some **optimization** around easily sharing the same string between multiple clients.

*21. What are some ways that you could sort a collection?*

You could use an inherently **sorted collection** like `TreeMap`, or `Collections.sort()`, or the **Stream** API.

*22. Write a Java program for the Fizz Buzz problem.*

```jsx
for (int i = 0; i < 100; i++) { 
    if (i % 15 == 0) System.out.println("FizzBuzz"); 
    else if (i % 3 == 0) System.out.println("Fizz"); 
    else if (i % 5 == 0) System.out.println("Buzz"); 
    else print(i); 
}
```

*23. Write an algorithm to check, if a string is a palindrome in Java.*

```jsx
public Boolean isPalindrome(String s) { 
    return s.equals(new StringBuilder(s).reverse().toString()); 
}
```

*24. Write a Java program to check, if a number is even or odd.*

```jsx
public Boolean isEven(int num) { 
  return (num & 1) == 0; 
}
```

*25. Write a Java program with a memory overflow.*

```jsx
public int fib(int n) {
    if (i <= 1) return i;
    return fib(n-1) + fib(n-2);
}

...
  
fib(10000000);
```

or

```jsx
Map map = new HashMap<int, int>();
int i = 0;
while(true) { 
  map.put(i++, i); 
}
```

*26. Write a Java program to check, if a number is prime.*

```jsx
bool isPrime(int n) {
    if (n % 2 == 0) return false;
    for (int i = 3; i*i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}
```

*27. Implement a stack in Java.*

```jsx
public class MyStack<T> {
  private List<T> stackList;
  private int top;

  public MyStack() {
    stackList = new ArrayList<T>();
    top = -1;
  }

  public void push(final T value) {
    stackList.add(value);
    top++;
  }
  
  public T pop() { return stackList.remove(top--); }
  public T peek() { return stackList.get(top); };
  public Boolean isEmpty() { return top == -1; };
}
```

*28. In a stack, `peek()` is O(1). How would you achieve O(1) lookup for `peek()` in a linked list?*

Linked lists typically keep a reference to the **head** node. In `peek()`just return `head.value`.

*29. Implement a queue in Java using a linked list.*

```jsx
public class QueueLinkedList<T> implements Queue<T> {
  private int total;
  private Node first, last;
  
  private class Node {
    private T data;
    private Node next;
  }

  public QueueLinkedList<T> enqueue(T data) {
    Node current = last;
    last = new Node();
    last.data = data;
    if (total++ == 0) first = last;
    else current.next = last;
    return this;
  }

  public T dequeue() {
    if (total == 0) throw new java.util.IllegalArgumentException('Queue is empty');
    T data = first.data;
    first = first.next;
    total--;
    if (total == 0) last = null;
    return data;
  }
}
```

*30. Implement a queue in Java using arrays.*

```jsx
public class QueueArray<T> implements Queue<T> {
  private T[] arr;
  private int total; 
  private int first;
  private int next;

  public QueueArray() {
    arr = new T[2];
  }

  private void resize(int capacity) {
    T[] tmp = new T[capacity];
    for (int i = 0; i < total; i++) tmp[i] = arr[(first + i) % arr.length];
    arr = tmp;
    first = 0;
    next = total;
  }

  public QueueArray<T> enqueue(T data) {
    if (arr.length == total) resize(arr.length * 2);
    arr[next++] = data;
    if (next == arr.length) next = 0;
    total++;
    return this;
  }

  public T dequeue() {
    if (total == 0) throw new java.util.IllegalArgumentException('Queue is empty');
    T data = arr[first];
    arr[first] = null;
    first++;
    total--;
    if (first == arr.length) first = 0;
    if (total > 0 && total == arr.length / 4) resize(arr.length / 2);
    return data;
  }
}
```

*31. Implement a singly-linked list in Java.*

```jsx
public class MyLinkedList<T> {

  private Integer size;
  private MyNode head;

  public MyLinkedList() {
    size = 0;
    head = new MyNode(null);
  }

  public void add(final T value) {
    final MyNode node = new MyNode(value);
    if (head.value == null) head = node;
    else {
      MyNode current = head;
      while (current.next != null) current = current.next;
      current.next = node;
    }
    size++;
  }

  public void addAtIndex(final T value, final Integer index) {
    if (index > size) throw new IndexOutOfBoundsException("Some meaningful error message");
    final MyNode node = new MyNode(value);
    if (size == 0) add(value);
    else {
      MyNode current = head;
      for (int i = 0; i < index-1; i++) current = current.next;
      MyNode after = current.next;
      current.next = node;
      node.next = after;
    }
    size++;
  }

  public T get(final Integer index) {
    if (index >= size) throw new IndexOutOfBoundsException("Some other meaningful error message");
    MyNode node = head;
    for (int i = 0; i < index; i++)
      node = node.next;
    return node.value;
  }

  public void remove(final Integer index) {
    if (index > size) throw new IndexOutOfBoundsException("Yet another meaningful error message");
    if (index == 0) head = head.next;
    else {
      MyNode previous = head;
      for (int i = 0; i < index - 1; i++) previous = previous.next;
      previous.next = previous.next.next;
    }
    size--;
  }

  public Boolean isEmpty() { return size == 0; }
  public Integer getSize() { return size; }

  class MyNode {
    public T value;
    public MyNode next;
    public MyNode(final T value) { this.value = value; }
  }
}
```

*32. in Java, how fast is direct lookup in a hash map theoretically, and why is it often slower in reality?*

Lookup in hash maps is supposed to be **constant time**, O(1), as each element is mapped to a key, which is computed using the key object’s hash code. However, if the hash function returns the same result for two or more inputs, **collisions** occur. In this case, each key is essentially mapped to a linked list of N objects belonging to it, reducing lookup speed to O(N).

*33. Implement binary search in Java.*

```
Arrays.binarySearch(sortedArray, key);
```

if you’re being sassy, or from scratch:

```jsx
public int binarySearch(int[] sortedArray, int key) {
    int low = 0;
    int high = sortedArray.size;
    int index = -1;
     
    while (low <= high) {
        int mid = (low + high) / 2;

        // key must be higher
        if (sortedArray[mid] < key) low = mid + 1;

        // key must be lower
        else if (sortedArray[mid] > key) high = mid - 1;
        
        // found key
        else if (sortedArray[mid] == key) {
            index = mid;
            break;
        }
    }

    // if index = -1, array does not contain key
    return index;
}
```

*34. Implement bubble sort in Java.*

```jsx
// O(n^2) --> there are many better sorting alg's
public int[] bubbleSort(int array[]) {
    
    // iterate over array backwards
    for (int i = array.length; i >= 0; i--) {

        // iterate over array forwards
        for (int j = 0; j < array.length - 1; j++) {

            // compare jth and next number
            int k = j + 1;

            // swap if necessary
            if (array[j] > array[k]) {
                int temp;
                temp = array[j];
                array[j] = array[k];
                array[k] = temp;
            }
        }
    }
    return array;
}
```

*35. Given a string like `a**hf*kl9*`, write a function that returns a string with all asterisks appearing first.*

```jsx
public String sortAsterisksInString(final String input) {
  final StringBuilder sb1 = new StringBuilder();
  final StringBuilder sb2 = new StringBuilder();
  for (char c : input.toCharArray()) {
    if (c == '*') sb1.append(c);
    else sb2.append(c);
  }
  return sb1.toString() + sb2.toString();
}
```

Below you’ll find more general technical and nontechnical questions. How you respond to these depends entirely on you, your experience, and the position you’re applying for.

# **General Technical Questions**

*36. How long have you been programming professionally?*

*37. Tell us the details of an interesting problem you worked on. What made it interesting?*

*38. What is something you’re proud to have contributed to?*

*39. What is something that didn’t go so well at work / while programming and how did you handle it / how would you handle it in the future?*

*40. How do you feel about <insert language/framework/library/tool from job posting>? What made you apply?*

*41. Tell us about a time when you had to make a trade-off between user experience and optimization / technical design?*

*42. What’s an example of a time, when you had make a decision quickly? What were the reasons behind that decision? Would you have done anything differently?*

*43. What is your favorite thing you’ve worked on recently?*

*44. What is the biggest technical challenge you have faced?*

*45. Describe a bug you fixed / a feature you implemented.*

*46. What are your favorite and least favorite (Java) frameworks/libraries/tools, and why?*

# **Nontechnical Questions**

*47. Tell us about yourself. What are your career goals and past projects? Where do you see yourself in 2 / 5 / 10 years?*

*48. Where did you hear about this role?*

*49. Which parts of our Creed / Mission / Vision resonate the most with you? Why us? What do you like about our company?*

*50. Which of our products / projects would you be excited to work on and why? Are there technologies you don’t want to work with and why not?*

*51. How do you use our and / or our competitors’ products? How would you improve on them?*

*52. What is your dream job? What’s your perfect work day like?*

*53. How do you work with different teams/departments?*

*54. Do you have references?*

***55. Do you have any questions for us?***

The last one is important. Here are some suggestions for questions you may want to ask your interviewer:

- How are you financed? (especially important for startups)
- What do you like about working here?
- How can I best prepare for this role before starting?
- Could you describe a typical work week?
- How big are teams?
- What would my immediate responsibilities be?
- Will there be opportunities to choose, what projects I work on?
- What does the career path look like for this role?
- How does your company promote personal growth?
- Do you feel there are any skills currently lacking on the team?
- What is the biggest change the company has gone through in the last year?
- What’s the style of leadership?
- What is the rhythm of work here? Is there a particular time of year, when it’s all hands on deck and we’re pulling long hours, or is it fairly consistent throughout the year?
- What type of background and experience are you looking for in this position? What would your ideal candidate be like?
- Is there anything that stands out to you that makes you think I might not be the right fit for this position?
- What is the timeline for making a decision on this position? When should I get back in touch with you?

# **Q1: What is meant by Java being platform independent?**

Java works on the principle of write once and run anywhere. Once a Java program is written, it is compiled into what is known as byte code, which can then be run on any Java Virtual Machine or JVM for short.

[](https://miro.medium.com/v2/resize:fit:875/0*7_U0qVJxjbse_1rk)

Compilation to bytecode is the magic behind Java’s interoperability. Different operating systems and hardware architectures have JVMs custom designed for themselves and all JVMs can run the same bytecode. Therefore, if you write a Java program on Linux, it will run seamlessly on a JVM designed for Windows operating system, making code agnostic to the underlying hardware and OS.

# **Q2: Explain the concepts of JRE, JDK, and JVM**

- **JRE (Java Runtime Environment)** includes the Java Virtual Machine and the standard Java APIs (core classes and supporting files.). The JRE contains just enough to execute a Java application, but not enough to compile it.
- **JDK (Java Development Kit)** is the JRE plus the Java compiler, and a set of other tools to compile and debug code. JRE consists of Java platform libraries, Java Virtual Machine (JVM), Java Plugin and Java Web Start to run Java applications. JRE as a stand-alone does not contain compilers and debugging tools. If you need to develop Java programs you need the full Java SDK. The JRE is not enough for program development. Only the full Java SDK contains the Java compiler which turns your .java source files into bytecode .class files.
- **JVM (Java Virtual Machine)** is an implementation of a specification, detailing the behavior expected of a JVM. Any implementation that conforms to the JVM specification should be able to run code compiled into Java bytecode irrespective of the language in which the code was originally written. In the Java programming language, all source code is first written in plain text files ending with the .java extension. Those source files are then compiled into .class files by the javac compiler. A .class file does not contain code that is native to your processor; it instead contains bytecodes — the machine language of the Java Virtual Machine. The java launcher tool then runs your application with an instance of the Java Virtual Machine.

# **Q3: How would you mark an entity package private in Java?**

There’s no explicit modifier for package private. In the absence of any modifier the class or member variables are package private. A member marked package private is only visible within its own package. Consider the class below.

[](https://miro.medium.com/v2/resize:fit:875/0*m8sa9DI5toNvXF8m)

Package private is a slightly wider form of private. One nice thing about package-private is that you can use it to give access to methods you would otherwise consider private to unit test classes. So, if you use helper classes which have no other use but to help your public classes do something clients need, it makes sense to make them package private as you want to keep things as simple as possible for users of the library.

# **Q4: Why should you avoid the finalize() method in the Object class? What are some alternatives?**

The Object class provides a callback method, finalize(), that may be invoked on an object when it becomes garbage. Object’s implementation of finalize() does nothing — you can override finalize() to do cleanup, such as freeing up resources.

The finalize() method may be called automatically by the system, but when it is called, or even if it is called, is uncertain. Therefore, you should not rely on this method to do your cleanup for you. For example, if you don’t close file descriptors in your code after performing I/O and you expect finalize() to close them for you, you may run out of file descriptors.

Here are some alternatives:

- The try-with-resources idiom can be used to clean up objects. This requires implementing the AutoCloseable interface.
- Using a PhantomReference to perform cleanup when an object is garbage collected
- Using Cleaner class to perform cleanup actions.
- Implement a close() method, which does the cleanup and document that the method be called.

# **Q5: Can you change the contents of a final array as shown in the code snippet below?**

![](https://miro.medium.com/v2/resize:fit:875/1*IeyO3v9rQWR_kjrNUkX-Mg.png)

It may appear counterintuitive, but we can actually change the contents of the array even though it is marked as final. The array variable points to a particular start location in the memory where the contents of the array are placed. The location or the memory address can’t be changed. For instance, the following code will not compile:

![](https://miro.medium.com/v2/resize:fit:875/1*KQB2HmWfxowiB33P_jjhhg.png)

**However, the following code will work.**

![](https://miro.medium.com/v2/resize:fit:875/1*e4-ij1hGel2Lms_Zc_09tQ.png)

# **Q6: Explain the difference between an interface and an abstract class? When should you use one or the other?**

An abstract class can’t be instantiated, but it can be subclassed. An abstract class usually contains abstract and non-abstract methods that subclasses are forced to provide an implementation for.

An interface is a completely “abstract class” that is used to group related methods with empty bodies.

Following are four main differences between abstract classes and interfaces:

- An abstract class can have final variables, static variables, or class member variables whereas an interface can only have variables that are final and static by default.
- An abstract class can have static, abstract, or non-abstract methods. An interface can have static, abstract, or default methods.
- Members of an abstract class can have varying visibility of private, protected, or public. Whereas, in an interface all methods and constants are public.
- A class can only extend another class, but it can implement multiple interfaces. Similarly, an interface can extend multiple interfaces. An interface never implements a class or an interface.

Use an abstract class when subclasses share state or use common functionality. Or you require to declare non-static, non-final fields or need access modifiers other than public.

Use an interface if you expect unrelated classes would implement your interface. For example, the interfaces Comparable and Cloneable are implemented by many unrelated classes. Interfaces are also used in instances where multiple inheritance of type is desired.

# **Q7: What is polymorphism? Can you give an example?**

Polymorphism is the ability in programming to present the same interface for differing underlying forms or data types. Polymorphism is when you can treat an object as a generic version of something, but when you access it, the code determines which exact type it is and calls the associated code. What this means is that polymorphism allows your code to work with different classes without needing to know which class it’s using.

Polymorphism is used to make applications more modular and extensible. Instead of messy conditional statements describing different courses of action, you create interchangeable objects that you select based on your needs. That is the basic goal of polymorphism.

The classic example of polymorphism is a `Shape` class. We derive `Circle`, `Triangle`, and `Rectangle` classes from the parent class `Shape`, which exposes an abstract method draw(). The derived classes provide their custom implementations for the `draw()` method. Now it is very easy to render the different types of shapes all contained within the same array by calling the `draw()` method on each object. This saves us from creating separate draw methods for each shape e.g. `drawTriangle()`, `drawCircle()`etc.

[](https://miro.medium.com/v2/resize:fit:875/0*OUxL4qsOYKtL5Lg-)

# **Q8: Can the main method be overloaded?**

Yes, the main method, which is a static method, can be overloaded. But only `public static void main(String[] args)` will be used when your class is launched by the JVM even if you specify one or two command-line arguments. However, programmatically one can invoke the overloaded versions of the main method.

# **Q9: How can you pass multiple arguments to a method on each invocation call?**

We can pass variable number of arguments to a method using varargs feature. Below is an example of passing multiple arguments of the same type to a method.

![](https://miro.medium.com/v2/resize:fit:875/1*XSSirORKujKnoMhcwQHFsA.png)

- The type name is followed by three dots, a space, and then the variable name.
- The varargs variable is treated like an array.
- The varargs variable must appear at the last in the method signature.
- As a consequence of the above, there can only be a single varargs in a method signature.

The above method can be invoked as follows: **Invoking Varargs Method**

![](https://miro.medium.com/v2/resize:fit:875/1*09WvtFG5Kh5-FHnhwVuOQQ.png)

# **Q10: Can a semaphore act as a mutex?**

A semaphore can potentially act as a mutex if the number of permits it can give out is set to 1. However, the most important difference between the two is that in the case of a mutex, the same thread must call acquire and subsequent release on the mutex whereas in the case of a binary semaphore, different threads can call acquire and release on the semaphore.

This leads us to the concept of “ownership”. A mutex is owned by the thread acquiring it, till the point, it releases it, whereas for a semaphore there’s no notion of ownership.

Need a refresher on multithreading? Check out this article [“Java Multithreading and Concurrency: Cracking Senior Interviews”.](https://blog.educative.io/java-multithreading-and-concurrency-what-to-know-for/)

# **Q11: Explain the Externalizable interface**

The Serializable interface gets us automatic serialization capability for objects of our class. On the other hand the Externalizable interface provides a way to implement a custom serialization mechanism. A class that implements the Externalizable interface is responsible to save and restore the contents of its own instances.

The Externalizable interface extends the Serializable interface and provides two methods to serialize and deserialize an object, `writeExternal()` and `readExternal()`.

# **Q12: If a code block throws more than one exception, how can it be handled?**

Multiple types of exceptions thrown by a snippet of code can be handled by multiple catch block clauses followed by the try block. An example snippet of exception handling appears below:

![](https://miro.medium.com/v2/resize:fit:875/1*NLoCgHgdM7JBxhXGo0P9Dw.png)

# **Q13: If you were to use a set, how would you determine between a HashSet and a TreeSet?**

Initially, you may want to use HashSet as it will give you a better time complexity, but it makes no guarantees as to the iteration order of the set; in particular, it does not guarantee that the order will remain constant over time.

So if you are wanting to maintain the order it’s best to use a TreeSet as it stores keys in ascending order rather than in their insertion order. It’s not thread safe. However, keep in mind that TreeSet is not thread safe whereas a HashSet is.

# **Q14: What are a few ways you can improve the memory footprint of a Java application?**

Here are three key steps you can take to improve the memory footprint:

- Limiting the scope of local variables. Each time the top scope from the stack is popped up, the references from that scope are lost, and this could make objects eligible for garbage collection.
- Explicitly set variable references to null when not needed. This will make objects eligible for garbage collection.
- Avoid finalizers. They slow down program performance and do not guarantee anything.

# **Q15: What is the best way to implement a singleton class?**

The best way to implement a singleton as per Josh Bloch is to use an enum type for the singleton. Because Java ensures that only a single instance of an enum is ever created, the singleton class implemented via enums is safe from reflection and serialization attacks.

![](https://miro.medium.com/v2/resize:fit:875/1*EWpQxY18kS-ZUL1Zwr7_nA.png)

## **Question 1: What’s wrong using HashMap in the multi-threaded environment? When get() method go to the infinite loop? ([answer](http://java67.blogspot.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html))**

Answer: Well, nothing is wrong; it depends upon how you use. For example, if you [initialize a HashMap](http://www.java67.com/2016/01/how-to-initialize-hashmap-with-values-in-java.html) by just one thread and then all threads are only reading from it, then it’s perfectly fine.

One example of this is a **Map that contains configuration properties**.

The real problem starts when at least one of that thread is updating HashMap, i.e. adding, changing, or removing any key-value pair.

Since put() operation can cause re-sizing and which can further lead to an infinite loop, that’s why either you should use [Hashtable](http://javarevisited.blogspot.com/2012/01/java-hashtable-example-tutorial-code.html) or [ConcurrentHashMap](http://javarevisited.blogspot.com/2013/02/concurrenthashmap-in-java-example-tutorial-working.html), later is even better.

## **Question 2. Does not overriding hashCode() method has any performance implication? ([answer](http://java67.blogspot.com/2013/04/example-of-overriding-equals-hashcode-compareTo-java-method.html))**

This is a good question and opens to all, as per my knowledge, a poor hash code function will result in the [frequent collision in HashMap](http://javarevisited.blogspot.sg/2016/01/how-does-java-hashmap-or-linkedhahsmap-handles.html) which eventually increases the time for adding an object into Hash Map.

From [Java 8](https://javarevisited.blogspot.com/2018/08/top-5-java-8-courses-to-learn-online.html) onwards though collision will not impact performance as much as it does in earlier versions because after a threshold the [linked list](http://javarevisited.blogspot.sg/2017/07/top-10-linked-list-coding-questions-and.html#axzz4xXS86IVo) will be replaced by a [binary tree](http://www.java67.com/2016/08/binary-tree-inorder-traversal-in-java.html), which will give you **O(logN)** performance in the worst case as compared to O(n) of a linked list.

## **Question 3: Does all property of the Immutable Object needs to be final in Java? ([answer](http://javarevisited.blogspot.com/2013/03/how-to-create-immutable-class-object-java-example-tutorial.html))**

Not necessary, as stated in the linked answer article, you can achieve the same functionality by *making a member as non-final but private and not modifying them except in the constructor.*

Don’t provide a setter method for them, and if it is a mutable object, then don’t ever leak any reference for that member.

Remember [making a reference variable final](https://javarevisited.blogspot.com/2016/09/21-java-final-modifier-keyword-interview-questions-answers.html), only ensures that it will not be reassigned a different value. However, you can still change the individual properties of an object, pointed by that reference variable.

This is one of the critical points; the Interviewer likes to hear from candidates. If you want to know more about final variables in Java, I recommend joining [**The Complete Java MasterClass](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F)** on Udemy, one of the best, hands-on courses.

[**Complete Java Masterclass (Updated for Java 17)You've just stumbled upon the most complete, in-depth Java programming course online. With over 560,000 students…**
udemy.com](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F&source=post_page-----36ba58865681---------------------------------------)

## **Question 4: How does substring () inside String works? ([answer](http://javarevisited.blogspot.sg/2011/10/how-substring-in-java-works.html))**

Another good Java interview question, I think the answer is not sufficient, but here it is: “*Substring creates a new object out of source string by taking a portion of the original string.”*

This question was mainly asked to see if the developer is familiar with the risk of [memory leak](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-understanding-solving-memory-problems), which a sub-string can create.

Until Java 1.7, substring holds the reference of the original character array, which means even a sub-string of 5 characters extended, *can prevent 1GB character array from garbage collection*, by containing a strong reference.

This issue was fixed in Java 1.7, where the original character array is not referenced anymore, but that change also made the creation of substring a bit costly in terms of time. Earlier it was on the range of O(1), which could be O(n) in the worst case of Java 7 onwards.

Btw, if you want to learn more about memory management in Java, I recommend checking out [**Java Application Performance Tuning and Memory Management course**](https://click.linksynergy.com/deeplink?id=JVFxdTr9V80&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fjava-application-performance-and-memory-management%2F%3FcouponCode%3DKEEPLEARNING) by Matt on Udemy.

[**Understanding the Java Virtual Machine: Memory ManagementThis course covers all aspects of garbage collection in Java, including how memory is split into generations and…**
pluralsight.pxf.io](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Funderstanding-java-vm-memory-management&source=post_page-----36ba58865681---------------------------------------)

By the way, you would need a [**Pluralsight membership**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fpricing) to join this course, which costs around $29 per month or $299 per year (14% discount). If you don’t have this plan, I highly recommend joining as it boosts your learning and as a programmer, you always need to learn new things.

Alternatively, you can also use their **1[0-day-free-trial](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Flearn)** to watch this course for FREE.

[**Build Better Tech Skills for Individuals | PluralsightBuild in-demand skills in everything from cybersecurity to software development. And then use those skills to…**
pluralsight.pxf.io](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Flearn&source=post_page-----36ba58865681---------------------------------------)

## **Question 5: Can you write a critical section code for the singleton? ([answer](http://javarevisited.blogspot.sg/2014/05/double-checked-locking-on-singleton-in-java.html))**

This core Java question is another common question and expecting the candidate to write Java singleton using [double-checked locking](http://www.java67.com/2015/09/thread-safe-singleton-in-java-using-double-checked-locking-pattern.html).

Remember to use a [volatile variable](http://javarevisited.blogspot.sg/2011/06/volatile-keyword-java-example-tutorial.html) to make Singleton [thread-safe](http://www.java67.com/2016/04/why-double-checked-locking-was-broken-before-java5.html).

Here is the code for a critical section of a thread-safe Singleton pattern using double-checked locking idiom:

```
public class Singleton {
private static volatile Singleton _instance;
/** * Double checked locking code on Singleton
    * @return Singelton instance
*/public static Singleton getInstance() {
if (_instance == null) {
synchronized (Singleton.class) {
if (_instance == null) {
_instance = new Singleton();
}
}
}return _instance;
}
}
```

On the same note, it’s good to know about classical design patterns likes Singleton, Factory, Decorator, etc. If you are interested in this, then this [**Low Level System Design, Design Patterns & SOLID Principles**](https://click.linksynergy.com/deeplink?id=JVFxdTr9V80&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Flow-level-system-design%2F%3FcouponCode%3DKEEPLEARNING) course on Udemy is an excellent collection of that.

![](https://miro.medium.com/v2/resize:fit:875/0*ohaQNJbbUkB5FBSu.jpeg)

## **Question 6: How do you handle error conditions while writing a stored procedure or accessing the stored procedure from java? ([answer](http://javarevisited.blogspot.com/2013/04/spring-framework-tutorial-call-stored-procedures-from-java.html))**

This is one of the *tough Java interview questions,* and again it’s open for you all; my friend didn’t know the answer, so he didn’t mind telling me.

My take is that a stored procedure should return an error code if some operation fails, but if stored procedure itself fails, then catching [SQLException](http://www.java67.com/2016/06/javasqlsqlexception-no-suitable-driver-found-jdbc-mysql-localhost-3306.html) is the only choice.

The [**Effective Java 3rd Edition**](https://www.amazon.com/Effective-Java-3rd-Joshua-Bloch/dp/0134685997/?tag=javamysqlanta-20) also has some good advice on dealing with errors and exceptions in Java, which is worth reading.

## **Question 7 : What is difference between Executor.submit() and Executer.execute() method ? ([answer](http://java67.blogspot.com/2012/08/5-thread-interview-questions-answers-in.html))**

This Java interview question is from my list of [Top 50 Java multi-threading question answers](http://javarevisited.blogspot.sg/2014/07/top-50-java-multithreading-interview-questions-answers.html#axzz4jaJmaqbE); It’s getting popular day by day because of the huge demand of a Java developer with good concurrency skills.

This Java interview question answers that former returns an object of [Future](http://javarevisited.blogspot.sg/2015/06/how-to-use-callable-and-future-in-java.html#axzz4tUeeQOAU) which can be used to find the result from a worker thread)

There is a difference when looking at exception handling. If your tasks throw an exception and if it was submitted with executing this exception, will go to the uncaught exception handler (when you don’t have provided one explicitly, the default one will just print the stack trace to System.err).

If you submitted the task with `submit()` the method any thrown exception, [checked exception](http://javarevisited.blogspot.sg/2011/12/checked-vs-unchecked-exception-in-java.html) or not, is the part of the task’s return status.

For a task that was submitted with submitting and that terminates with an exception, the Future.get() will re-throw this exception, wrapped in an ExecutionException.

If you want to learn more about Future, Callable, and Asynchronous computing and take your Java Concurrency skills to the next level, I suggest you check out [**Java Concurrency Practice in Bundle**](https://learning.javaspecialists.eu/courses/concurrency-in-practice-bundle?affcode=92815_johrd7r8) course by Java Champion Heinz Kabutz.

It’s an advanced course, which is based upon the classic [**Java Concurrency Practice**](http://www.amazon.com/dp/0321349601/?tag=javamysqlanta-20) book by none other than [Brian Goetz](https://medium.com/u/9e6fd5717133), which is considered as a bible for Java Developers. The course is definitely worth your time and money. Since Concurrency is a robust and tricky topic, a combination of this book and class is the best way to learn it.

## **Question 8: What is the difference between factory and abstract factory pattern? ([answer](http://javarevisited.blogspot.sg/2013/01/difference-between-factory-and-abstract-factory-design-pattern-java.html))**

Answer: Abstract Factory provides one more level of abstraction. Consider different factories each extended from an Abstract Factory and responsible for the creation of different hierarchies of objects based on the type of factory. E.g., `AbstractFactory` extended by `AutomobileFactory`, `UserFactory`, `RoleFactory`, etc. Each factory would be responsible for the creation of objects in that genre.

If you want to learn more about the Abstract Factory design pattern, then I suggest you check out the [Design Pattern in Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdesign-patterns-java%2F) course, which provides excellent, real-world examples to understand patterns better.

Here is the UML diagram of the factory and abstract factory pattern:

![](https://miro.medium.com/v2/resize:fit:875/0*dJ5G1uE7oRE5_J7f.jpeg)

If you need more choices, then you can also check out my list of [Top 5 Java Design Pattern](https://javarevisited.blogspot.com/2018/02/top-5-java-design-pattern-courses-for-developers.html) courses.

**Question 9: What is Singleton? is it better to make the whole method synchronized or only critical section synchronized?** ([answer](http://javarevisited.blogspot.com/2012/12/how-to-create-thread-safe-singleton-in-java-example.html))

Singleton in Java is a class with just one instance in the entire Java application, for example, `java.lang.Runtime` is a Singleton class.

Creating Singleton was tricky before Java 4, but once Java 5 introduced [Enum](https://javarevisited.blogspot.com/2011/08/enum-in-java-example-tutorial.html), it’s straightforward.

You can see my article [How to create thread-safe Singleton in Java](http://javarevisited.blogspot.sg/2012/12/how-to-create-thread-safe-singleton-in-java-example.html) for more details on writing Singleton using the enum and double-checked locking, which is the purpose of this Java interview question.

**Question 10: Can you write code for iterating over HashMap in Java 4 and Java 5?** ([answer](http://java67.blogspot.com/2014/05/3-examples-to-loop-map-in-java-foreach.html))

Tricky one, but he managed to write using a while and a for a loop. There are four ways to iterate over any Map in Java; one involves using essential [Set()](http://www.java67.com/2016/05/keyset-vs-entryset-vs-values-in-java-map-example.html) and iterating over a key and then using [get()](http://www.java67.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html) method to retrieve values, which is a bit expensive.

The second method involves using [entrySet()](http://www.java67.com/2013/08/best-way-to-iterate-over-each-entry-in.html) and iterating over them either by applying [for each loop](https://javarevisited.blogspot.com/2015/09/java-8-foreach-loop-example.html#axzz5HKqzQNyN) or while with Iterator.hasNext() method.

This one is a better approach because both key and value object is available to you during Iteration, and you don’t need to call [get()](http://javarevisited.blogspot.sg/2011/02/how-hashmap-works-in-java.html) method for retrieving the value, which could give the O(n) performance in case of a huge [linked list](http://www.java67.com/2017/06/5-difference-between-array-and-linked.html) at one bucket.

You can further, see my post four [ways to iterate over Map in Java](http://javarevisited.blogspot.com/2011/12/how-to-traverse-or-loop-hashmap-in-java.html) for detailed explanation and code examples.

## **Question 11 : When do you override hashCode() and equals()? ([answer](http://javarevisited.blogspot.com/2013/08/10-equals-and-hashcode-interview.html))**

Whenever necessary, especially if you want to do an equality check based upon business logic rather than object equality, e.g. two employee objects are equal if they have the same, even though they are two different objects created by a different part of the code.

Also, [overriding](http://www.java67.com/2013/04/example-of-overriding-equals-hashcode-compareTo-java-method.html) both these methods is a must if you want to use them as key in [HashMap](http://www.java67.com/2017/08/top-10-java-hashmap-interview-questions.html).

Now, as part of the equals-hashcode contract in Java, when you override equals, you must override hashcode as well; otherwise, your object will not break invariant of classes, e.g. Set, Map which relies on [equals()](http://javarevisited.blogspot.sg/2013/08/10-equals-and-hashcode-interview.html) method for functioning correctly.

You can also check my post five [tips on equals in Java](http://javarevisited.blogspot.com/2011/02/how-to-write-equals-method-in-java.html) to understand the subtle issue which can arise while dealing with these two methods.

**Question 12: What will be the problem if you don’t override hashCode() method?** ([answer](http://java67.blogspot.sg/2013/04/example-of-overriding-equals-hashcode-compareTo-java-method.html))

If you don’t replace the equals method, then the contract between equals and hashcode will not work, according to which two objects which are equal by equals() must have the **same hashcode**.

In this case, another object may return different hashCode and will be stored on that location, which breaks invariant of [HashMap class](http://www.java67.com/2013/02/10-examples-of-hashmap-in-java-programming-tutorial.html) because they are not supposed to allow duplicate keys.

When you add the object using the put() method, it iterates through all Map.Entry objects present in that bucket location, and update the value of the previous mapping if Map already contains that key. This will not work if the hashcode is not overridden.

If you want to learn more about the role of equals() and hashCode() in Java Collections like Map and Set, I suggest you go through [**60 Days of Java : The Complete Java Masterclass**](https://click.linksynergy.com/deeplink?id=JVFxdTr9V80&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fjavamasterclass%2F%3FcouponCode%3DKEEPLEARNING) course on Udmey

**Question 13 : Is it better to synchronize critical section of getInstance() method or whole getInstance() method?** ([answer](http://javarevisited.blogspot.com/2014/05/double-checked-locking-on-singleton-in-java.html))

The answer is an only critical section because if we lock the whole method that every time someone calls this method, it will have to wait even though we are not creating an object.

In other words, [synchronization](http://javarevisited.blogspot.sg/2011/04/synchronization-in-java-synchronized.html#axzz4sZOoYUxv) is only needed when you create an object, which happens only once.

Once an object has created, there is no need for any synchronization. That’s very poor coding in terms of performance, as synchronized methods reduce production up to 10 to 20 times.

Here is the UML diagram of the [Singleton design pattern](https://javarevisited.blogspot.com/2011/03/10-interview-questions-on-singleton.html):

![](https://miro.medium.com/v2/resize:fit:506/0*mulviFlnCd3p2R_T.png)

By the way, there are several ways to create a thread-safe singleton in Java, including [Enum](http://javarevisited.blogspot.sg/2012/07/why-enum-singleton-are-better-in-java.html#axzz4tzMEHSJw), which you can also mention as part of this question or any follow-up.

If you want to learn more, you can also check to [**Learn Creational Design Patterns in Java**](http://bit.ly/2xZnIDC) — A #FREE Course from Udemy.

[**Free Design Pattern Tutorial — Learn Creational Design Patterns in JavaThe only course you need to learn creational design patterns! — Free Course**
bit.ly](http://bit.ly/2xZnIDC?source=post_page-----36ba58865681---------------------------------------)

## **Question 14: Where does equals() and hashCode() method comes in the picture during the get() operation on HashMap? ([answer](https://javarevisited.blogspot.com/2017/08/top-10-java-concurrenthashmap-interview.html#axzz5ITbIGRsU))**

This core Java interview question is a follow-up of previous Java question, and the candidate should know that once you mention hashCode, people are most likely ask, how they are used in HashMap.

When you provide a crucial object, first it’s hashcode method is called to calculate bucket location. Since a bucket may contain more than one entry as a linked list, each of those `Map.Entry` an object is evaluated by using equals() method to see if they contain the crucial actual object or not.

I strongly suggest you read my post, [**How HashMap works in Java**](http://javarevisited.blogspot.sg/2011/02/how-hashmap-works-in-java.html), another tale of an interview to learn more about this topic.

![](https://miro.medium.com/v2/resize:fit:806/0*s1uIRc3GjoDFlBI0.jpeg)

## **Questions 15: How do you avoid deadlock in Java? ([answer](http://javarevisited.blogspot.sg/2015/10/133-java-interview-questions-answers-from-last-5-years.html))**

If you know, a deadlock occurs when two threads try to access two resources which are held by each other, but to that happen the following four conditions need to match:

1. Mutual exclusionAt least one process must be held in a non-sharable mode.
2. Hold and WaitThere must be a process holding one resource and waiting for another.
3. No preemptionresources cannot be preempted.
4. Circular WaitThere must exist a set of processes

You can avoid deadlock by breaking the *circular wait condition*. To do that, you can make arrangements in the code to impose the **ordering** on the acquisition and release of locks.

If lock were acquired in a logical order and released in just opposite order, there would not be a situation where one thread is holding a lock that is received by others and vice-versa.

You can further see my post, [**how to avoid deadlock in Java**](https://javarevisited.blogspot.com/2018/08/how-to-avoid-deadlock-in-java-threads.html) for the code example, and a more detailed explanation.

I also recommend, [Java Multithreading, Concurrency & Performance Optimization course](https://click.linksynergy.com/deeplink?id=JVFxdTr9V80&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fjava-multithreading-concurrency-performance-optimization%2F%3FcouponCode%3DKEEPLEARNING) by Michael Pogrebinsky for a better understanding of concurrency patterns for Java developers.

![](https://miro.medium.com/v2/resize:fit:660/0*Oax0vcfY6E0enqWU.gif)

## **Question 16: What is the difference between creating String as new() and literal? ([answer](http://javarevisited.blogspot.com/2012/10/10-java-string-interview-question-answers-top.html))**

When we create a String object in Java with a new() Operator, it’s built-in a heap and not added into the string pool while String created using [literal](http://www.java67.com/2014/08/difference-between-string-literal-and-new-String-object-Java.html) are created in the String pool itself, which exists in the PermGen area of heap.

`String str = new String(“Test”)`

Does not put the object str in the String pool, we need to call [String. Intern ()](https://javarevisited.blogspot.com/2015/12/when-to-use-intern-method-of-string-in-java.html) method, which is used to put them into the String pool explicitly.

It’s only when you create a String object as String literal e.g. `String s = “Test”` Java automatically puts that into the String pool.

By the way, there is a catch here Since we are passing arguments as “Test,” which is a string literal, it will also create another object as “Test” on the [string pool](http://javarevisited.blogspot.sg/2016/07/difference-in-string-pool-between-java6-java7.html).

This is the one point, which has gone unnoticed until knowledgeable readers of the [Javarevisited](http://javarevisited.blogspot.com/) blog suggested it. To learn more about the difference between a String literal and String object, see [this](http://java67.blogspot.sg/2014/08/difference-between-string-literal-and-new-String-object-Java.html) article.

Here is a beautiful image which shows this difference quite well:

![](https://miro.medium.com/v2/resize:fit:875/0*SXXBpPu9L9Pwa3ck.png)

## **Question 17: What is Immutable Object? Can you write Immutable Class? ([answer](http://javarevisited.blogspot.in/2013/03/how-to-create-immutable-class-object-java-example-tutorial.html))**

Immutable classes are Java classes whose objects cannot be modified once created. Any modification in an Immutable object results in a new purpose; for example, [String is immutable in Java](http://javarevisited.blogspot.sg/2010/10/why-string-is-immutable-in-java.html).

Mostly Immutable classes are also [final](https://javarevisited.blogspot.com/2011/12/final-variable-method-class-java.html) in Java to prevent subclasses from overriding methods, which can compromise Immutability.

You can achieve the same functionality by making member as non-final but [private](http://javarevisited.blogspot.sg/2012/10/difference-between-private-protected-public-package-access-java.html) and not modifying them except in constructor.

Apart from obvious, you also need to make sure that you should not expose the internals of an Immutable object, mainly if it contains a mutable member.

Similarly, when you accept the value for the mutable member from client e.g. `java.util.Date`, use the [clone() method](http://javarevisited.blogspot.sg/2013/09/how-clone-method-works-in-java.html) to keep a separate copy for yourself to prevent the risk of malicious client modifying mutable reference after setting it.

The Same precaution needs to be taken while returning value for a mutable member, return another separate copy to the client, never return original reference held by Immutable class. You can also see my post [How to create an Immutable class in Java](http://javarevisited.blogspot.sg/2013/03/how-to-create-immutable-class-object-java-example-tutorial.html) for step by step guide and code examples.

## **Question 18: Give the simplest way to find out the time a method takes for execution without using any profiling tool? ([answer](http://javarevisited.blogspot.com/2012/10/10-java-string-interview-question-answers-top.html))**

Read the system time just before the method is invoked and immediately after method returns. Take the time difference, which will give you the time taken by a plan for execution.

Remember that if the time taken for execution is too small, it might show that it is taking zero milliseconds for performance. Try it on a method which is big enough, in a sense the one which is doing a considerable amount of processing

## **Question 19: Which two ways you need to implement to use any Object as key in HashMap? ([answer](http://javarevisited.blogspot.com/2013/01/difference-between-identityhashmap-and-hashmap-java.html))**

To use any object as Key in HashMap or Hashtable, it must implement [equals](http://www.java67.com/2012/11/difference-between-operator-and-equals-method-in.html) and [hashcode](http://javarevisited.blogspot.sg/2015/01/why-override-equals-hashcode-or-tostring-java.html#axzz55oDxm8vv) method in Java.

You can also read [How HashMap works in Java](http://javarevisited.blogspot.sg/2011/02/how-hashmap-works-in-java.html) for a detailed explanation of how the equals and hashcode method is used to put and get an object from HashMap.

**Question 20: How would you prevent a client from directly instantiating your concrete classes? For example, you have a Cache interface and two implementation classes MemoryCache and DiskCache. How do you ensure there is no object of these two classes created by the client using new() keyword.**

I leave this question for you to practice and think about before I answer. I am sure you can figure out the right way to do this, as this is one of the critical decisions to keep control of classes in your hand, great from a maintenance perspective.

A lot of you asked me to answer this question, so I am answering it now.

In Java, one way to prevent clients from directly instantiating your concrete classes is by using the **factory method pattern**. The factory method pattern involves defining an interface or an abstract class for creating objects, and allowing subclasses or implementing classes to alter the type of objects that will be created.

Here’s how you could structure your classes to achieve this:

```
// Cache interface
public interface Cache {
    void storeData(String key, String data);
    String retrieveData(String key);
}

// MemoryCache implementation
public class MemoryCache implements Cache {
    // Private constructor to prevent direct instantiation
    private MemoryCache() {}

    // Factory method to create an instance of MemoryCache
    public static MemoryCache createMemoryCache() {
        return new MemoryCache();
    }

    // Implement the Cache interface methods
    @Override
    public void storeData(String key, String data) {
        // Implementation for storing data in memory
    }

    @Override
    public String retrieveData(String key) {
        // Implementation for retrieving data from memory
        return null;
    }
}

// DiskCache implementation
public class DiskCache implements Cache {
    // Private constructor to prevent direct instantiation
    private DiskCache() {}

    // Factory method to create an instance of DiskCache
    public static DiskCache createDiskCache() {
        return new DiskCache();
    }

    // Implement the Cache interface methods
    @Override
    public void storeData(String key, String data) {
        // Implementation for storing data on disk
    }

    @Override
    public String retrieveData(String key) {
        // Implementation for retrieving data from disk
        return null;
    }
}
```

In this example, the constructors of `MemoryCache` and `DiskCache` are made private, making it impossible for clients to directly instantiate them using the `new` keyword. Instead, clients should use the provided factory methods (`createMemoryCache` and `createDiskCache`) to obtain instances of these classes.

By following this approach, you provide a controlled way for clients to obtain instances of your classes while maintaining encapsulation and preventing direct instantiation.

## **21. Designing a Connection Pool**

Imagine you are tasked with designing a connection pool for a database access library. The library will be used by multiple clients in a high-performance system. Each client might need to perform various read and write operations on the database.

How would you design a connection pool that meets the following requirements:

1. Efficiently manages a pool of database connections.
2. Supports concurrent usage by multiple clients without causing contention or bottlenecks.
3. Provides a mechanism for handling connection timeouts and failures gracefully.
4. Ensures that connections are reused effectively to reduce overhead.

Discuss the key components, design patterns, and considerations you would take into account to implement such a connection pool. How would you handle connection acquisition, release, and monitoring?

**Answer:** Designing a connection pool is a complex task that involves considerations for efficiency, concurrency, fault tolerance, and resource management. Here’s an overview of how you might approach designing a connection pool:

**Key Components:**

1. Connection Pool Class:
- Create a central class responsible for managing the connection pool.
- Implement a singleton pattern to ensure a single instance throughout the application.
1. Connection Object:
- Define a connection object representing a connection to the database.
- Include properties like connection status, creation time, last usage time, etc.
1. Connection Pool Configuration:
- Allow configuration of parameters such as maximum pool size, minimum pool size, timeout settings, etc.
- Use a configuration mechanism (properties, XML, etc.) to make the pool adaptable to different environments.

**Design Patterns and Strategies:**

1. Object Pool Pattern:
- Implement the Object Pool pattern to manage a pool of connection objects efficiently.
- Pre-create a pool of connections during initialization to minimize runtime overhead.
1. Concurrency Control:
- Use thread-safe data structures and synchronization mechanisms to handle concurrent access.
- Implement techniques like connection leasing and reference counting to control access.
1. Timeout Handling:
- Implement a mechanism to handle connection timeouts.
- Regularly check and evict idle connections beyond a specified timeout period.
1. Connection Reuse:
- Implement connection reuse to minimize the overhead of opening and closing connections.
- Use an algorithm to allocate and release connections efficiently.

**Connection Acquisition and Release:**

1. Connection Acquisition:
- When a client requests a connection, check if there are available connections in the pool.
- If the pool is not full, create a new connection; otherwise, wait or return an error based on the configured behavior.
1. Connection Release:
- When a client is done using a connection, return it to the pool for reuse.
- Reset the connection state and update relevant metadata (last usage time).

Monitoring and Fault Tolerance:

1. Monitoring:
- Implement monitoring features to log and track the usage of connections.
- Log information about connection acquisition, release, timeouts, and failures.
1. Fault Tolerance:
- Implement mechanisms to handle database connection failures.
- Consider implementing connection validation to ensure that a connection is still valid before it is provided to a client.

**Additional Considerations:**

1. Idle Connection Cleanup:
- Periodically check for idle connections and remove them from the pool to free up resources.
1. Graceful Shutdown:
- Implement a graceful shutdown mechanism to release all connections when the application exits.
1. Dynamic Pool Sizing:
- Consider dynamically adjusting the pool size based on demand to optimize resource utilization.
1. Connection Pool Statistics:
- Provide APIs for clients to retrieve statistics about the connection pool, such as the number of active connections, total connections, etc.

By carefully considering these components, design patterns, and strategies, you can create a robust and efficient connection pool that meets the requirements of a high-performance system. Keep in mind that the specific implementation details may vary based on the programming language and database technology being used.

1) **How does Java achieve platform independence?** ([answer](http://www.java67.com/2012/08/how-java-achieves-platform-independence.html))

hint: bytecode and Java Virtual Machine

2) **What is `ClassLoader` in Java?** ([answer](http://javarevisited.blogspot.sg/2012/12/how-classloader-works-in-java.html#axzz59AWpr6cb))

hint: part of JVM that loads bytecodes for classes. You can write your own.

3) **Write a Java program to check if a number is Even or Odd?** ([answer](http://javarevisited.blogspot.sg/2013/04/how-to-check-if-number-is-even-or-odd.html#axzz59AWpr6cb))

hint: you can use bitwise operator, like bitwise AND, remember, even the number has zero at the end in binary format and an odd number has 1 in the end.

4) **Difference between `ArrayList` and `HashSet` in Java?** ([answer](http://www.java67.com/2012/07/difference-between-arraylist-hashset-in-java.html))

hint: all differences between `List` and `Set` are applicable here, e.g. ordering, duplicates, random search, etc. See [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) by Richard Warburton to learn more about ArrayList, HashSet and other important Collections in Java.

![](https://miro.medium.com/v2/resize:fit:875/1*hd861fcwDe86tY-1Y0VNRQ.png)

5) **What is double-checked locking in Singleton?** ([answer](http://www.java67.com/2016/04/why-double-checked-locking-was-broken-before-java5.html))

hint: two-time check whether instances are initialized or not, first without locking and second with locking.

**6) How do you create thread-safe Singleton in Java? ([answer](http://javarevisited.blogspot.sg/2012/12/how-to-create-thread-safe-singleton-in-java-example.html))**

hint: many ways, like using Enum or by using double-checked locking pattern or using a nested static class.

**7) When to use the volatile variable in Java? ([answer](http://www.java67.com/2012/08/what-is-volatile-variable-in-java-when.html))**

hint: when you need to instruct the JVM that a variable can be modified by multiple threads and give hint to JVM that does not cache its value.

**8) When to use a transient variable in Java? ([answer](http://www.java67.com/2012/08/what-is-transient-variable-in-java.html))**

hint: when you want to make a variable non-serializable in a class, which implements the Serializable interface. In other words, you can use it for a variable whose value you don’t want to save. See [**The Complete Java MasterClass**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F) to learn about transient variables in Java.

**9) Difference between the transient and volatile variable in Java? ([answer](http://www.java67.com/2012/11/difference-between-transient-vs-volatile-modifier-variable-java.html))**

hint: totally different, one used in the context of serialization while the other is used in concurrency.

**10) Difference between Serializable and Externalizable in Java? ([answer](http://www.java67.com/2012/10/difference-between-serializable-vs-externalizable-interface.html))**

hint: Externalizable gives you more control over the Serialization process.

**11) Can we override the private method in Java? ([answer](http://www.java67.com/2013/08/can-we-override-private-method-in-java-inner-class.html))**

hint: No, because it’s not visible in the subclass, a primary requirement for overriding a method in Java.

**12) Difference between `Hashtable` and `HashMap` in Java? ([answer](http://javarevisited.blogspot.sg/2010/10/difference-between-hashmap-and.html#axzz53B6SD769))**hint: several but most important is `Hashtable`, which is synchronized, while `HashMap` is not. It's also legacy and slow as compared to `HashMap`.

**13) Difference between `List`and `Set` in Java? ([answer](http://javarevisited.blogspot.sg/2012/04/difference-between-list-and-set-in-java.html#axzz53n9YK0Mb))**

hint: `List` is ordered and allows duplicate. `Set` is unordered and doesn't allow duplicate elements.

![](https://miro.medium.com/v2/resize:fit:755/1*qYHkxvWr5Hw-gGF0sm4UIg.jpeg)

**14) Difference between `ArrayList` and `Vector` in Java ([answer](http://www.java67.com/2012/09/arraylist-vs-vector-in-java-interview.html))**

hint: Many, but most important is that `ArrayList` is non-synchronized and fast while `Vector` is synchronized and slow. It's also legacy class like `Hashtable`.

**15) Difference between `Hashtable` and `ConcurrentHashMap` in Java? ([answer](http://javarevisited.blogspot.sg/2011/04/difference-between-concurrenthashmap.html#axzz4qw7RoNvw))**

hint: more scalable. See [**Java Fundamentals: Collections**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections) by Richard Warburton to learn more.

**16) How does `ConcurrentHashMap` achieve scalability? ([answer](http://javarevisited.blogspot.sg/2017/08/top-10-java-concurrenthashmap-interview.html#axzz50U9xyqbo))**

hint: by dividing the map into segments and only locking during the write operation.

**17) Which two methods you will override for an `Object` to be used as `Key` in `HashMap`? ([answer](http://www.java67.com/2013/06/how-get-method-of-hashmap-or-hashtable-works-internally.html))**

hint: equals and hashcode

**18) Difference between wait and sleep in Java? ([answer](http://www.java67.com/2012/08/what-are-difference-between-wait-and.html))**

hint: The `wait()` method releases the lock or monitor, while sleep doesn't.

**19) Difference between `notify` and `notifyAll` in Java? ([answer](http://www.java67.com/2013/03/difference-between-wait-vs-notify-vs-notifyAll-java-thread.html))**

hint: `notify` notifies one random thread is waiting for that lock while `notifyAll` inform to all threads waiting for a monitor. If you are certain that only one thread is waiting then use `notify`, or else `notifyAll` is better. See [**Threading Essentials Mini-Course](https://javaspecialists.teachable.com/p/threading-essentials/?product_id=539197&coupon_code=SLACK100%3Faffcode%3D92815_johrd7r8)** by Java Champion Heinz Kabutz to learn more about threading basics.

**20) Why do you override hashcode, along with `equals()` in Java? ([answer](http://javarevisited.blogspot.sg/2015/01/why-override-equals-hashcode-or-tostring-java.html#axzz55oDxm8vv))**

hint: to be compliant with equals and hashcode contract, which is required if you are planning to store your object into collection classes, e.g. `HashMap` or `ArrayList`.

**21) What is the load factor of `HashMap` means? ([answer](http://www.java67.com/2017/08/top-10-java-hashmap-interview-questions.html))**

hint: The threshold that triggers the re-sizing of `HashMap` is generally 0.75, which means `HashMap` resize itself if it's 75 percent full.

**22) Difference between `ArrayList` and `LinkedList` in Java? ([answer](http://www.java67.com/2012/12/difference-between-arraylist-vs-LinkedList-java.html))**

hint: same as an array and linked list, one allows random search while the other doesn't. Insertion and deletion are easy on the linked list but a search is easy on an array. See [**Java Fundamentals: Collections](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-collections),** Richard Warburton’s course on Pluralsight, to learn more about essential Collection data structure in Java.

**23) Difference between `CountDownLatch` and `CyclicBarrier` in Java? ([answer](http://www.java67.com/2012/08/difference-between-countdownlatch-and-cyclicbarrier-java.html))**

hint: You can reuse `CyclicBarrier` after the barrier is broken but you cannot reuse `CountDownLatch` after the count reaches to zero.

**24) When do you use `Runnable` vs `Thread` in Java? ([answer](http://www.java67.com/2016/01/7-differences-between-extends-thread-vs-implements-Runnable-java.html))**

hint: always

**25) What is the meaning of Enum being type-safe in Java? ([answer](http://www.java67.com/2014/04/what-java-developer-should-know-about-Enumeration-type-in-Java.html))**

hint: It means you cannot assign an instance of different Enum type to an Enum variable. e.g. if you have a variable like `DayOfWeek` day then you cannot assign it value from `DayOfMonth` enum.

**26) How does Autoboxing of Integer work in Java? ([answer](http://javarevisited.blogspot.sg/2012/07/auto-boxing-and-unboxing-in-java-be.html#axzz59AWpr6cb))**

hint: By using the `valueOf()` method in Java.

**27) Difference between `PATH` and `Classpath` in Java? ([answer](http://www.java67.com/2012/08/what-is-path-and-classpath-in-java-difference.html))**

hint: `PATH` is used by the operating system while `Classpath` is used by JVM to locate Java binary, e.g. JAR files or Class files. See **[Java Fundamentals: The Core Platform](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-core-platform)** to learn more about `PATH`, `Classpath`, and other Java environment variable.

![](https://miro.medium.com/v2/resize:fit:478/1*PBuMgGmVXwBguv-SPw7YJw.jpeg)

**28) Difference between method overloading and overriding in Java? ([answer](http://www.java67.com/2015/08/top-10-method-overloading-overriding-interview-questions-answers-java.html))**

hint: Overriding happens at subclass while overloading happens in the same class. Also, overriding is a runtime activity while overloading is resolved at compile time.

**29) How do you prevent a class from being sub-classed in Java? ([answer](http://www.java67.com/2017/06/10-points-about-final-modifier-in-java.html))**

hint: just make its constructor private

**30) How do you restrict your class from being used by your client? ([answer](http://javarevisited.blogspot.sg/2016/01/why-jpa-entity-or-hibernate-persistence-should-not-be-final-in-java.html))**

hint: make the constructor private or throw an exception from the constructor

**31) Difference between `StringBuilder` and `StringBuffer` in Java? ([answer](http://www.java67.com/2016/10/5-difference-between-stringbuffer.html))**

hint: `StringBuilder` is not synchronized while `StringBuffer` is synchronized.

**32) Difference between Polymorphism and Inheritance in Java? ([answer](http://www.java67.com/2014/04/difference-between-polymorphism-and-Inheritance-java-oops.html))**

hint: Inheritance allows code reuse and builds the relationship between classes, which is required by Polymorphism, which provides dynamic behavior. See [**Grokking the Object-Oriented Design Interview course**](https://www.educative.io/collection/5668639101419520/5692201761767424?affiliate_id=5073518643380224)s on Educative to learn more about OOP features and designing classes using OOP techniques.

![](https://miro.medium.com/v2/resize:fit:875/1*HOHL45cizmKdgWWiWidnvA.png)

**33) Can we override the static method in Java? ([answer](http://www.java67.com/2012/08/can-we-override-static-method-in-java.html))**

hint: No, because overriding resolves at runtime while static method call is resolved at compile time.

**34) Can we access the private method in Java? ([answer](http://www.java67.com/2012/08/can-we-override-private-method-in-java.html))**

hint: yes, in the same class but not outside the class

**35) Difference between interface and abstract class in Java? ([answer](http://www.java67.com/2017/08/difference-between-abstract-class-and-interface-in-java8.html))**

hint: from [Java 8](https://dzone.com/articles/5-courses-to-crack-java-certification-ocajp-1z0-80), the difference is blurred. However, a Java class can still implement multiple interfaces but can only extend one class.

**36) Difference between DOM and SAX parser in Java? ([answer](http://www.java67.com/2012/09/dom-vs-sax-parser-in-java-xml-parsing.html))**

hint: DOM loads the whole XML File in memory while SAX doesn’t. It is an event-based parser and can be used to parse a large file, but DOM is fast and should be preferred for small files.

**37) Difference between the throw and throws keyword in Java? ([answer](http://www.java67.com/2012/10/difference-between-throw-vs-throws-in.html))**

hint: throws declare what exception a method can throw in case of error but throw keyword actually throws an exception. See [**Java Fundamentals: Exception Handling**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fjava-fundamentals-exception-handling) to learn more about Exception handling in Java.

![](https://miro.medium.com/v2/resize:fit:875/1*O5DEoN9mOy3D0HxFKWwfKQ.png)

**38) Difference between fail-safe and fail-fast iterators in Java? ([answer](http://www.java67.com/2015/06/what-is-fail-safe-and-fail-fast-iterator-in-java.html))**

hint: fail-safe doesn’t throw `ConcurrentModificationException` while `fail-fast` does whenever they detect an outside change on the underlying collection while iterating over it.

**39) Difference between Iterator and Enumeration in Java? ([answer](http://javarevisited.blogspot.sg/2010/10/what-is-difference-between-enumeration.html#axzz59AWpr6cb))**

hint: Iterator also gives you the ability to remove an element while iterating while Enumeration doesn’t allow that.

**40) What is `IdentityHashMap` in Java? ([answer](http://www.java67.com/2016/09/difference-between-identityhashmap-weakhashmap-enummap-in-java.html))**

hint: A `Map`, which uses the `==` equality operator to check equality instead of the `equals()` method.

**41) What is the `String` pool in Java? ([answer](http://javarevisited.blogspot.sg/2016/07/difference-in-string-pool-between-java6-java7.html#axzz4pGGwsyna))**

hint: A pool of `String` literals. Remember it's moved to heap from perm gen space in JDK 7.

![](https://miro.medium.com/v2/resize:fit:630/1*kbVqv7Hhrcf0nltAHRDVqw.jpeg)

**42) Can a `Serializable` class contains a non-serializable field in Java? ([answer](http://javarevisited.blogspot.sg/2016/09/how-to-serialize-object-in-java-serialization-example.html))**hint: Yes, but you need to make it either static or transient.

**43) Difference between this and super in Java? ([answer](http://www.java67.com/2013/06/difference-between-this-and-super-keyword-java.html))**

hint: this refers to the current instance while super refers to an instance of the superclass.

**44) Difference between `Comparator` and `Comparable` in Java? ([answer](http://www.java67.com/2013/08/difference-between-comparator-and-comparable-in-java-interface-sorting.html))**

hint: `Comparator` defines custom ordering while `Comparable` defines the natural order of objects, e.g. the alphabetic order for `String`. See **[The Complete Java MasterClass](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F)** to learn more about sorting in Java.

![](https://miro.medium.com/v2/resize:fit:875/1*MTR8OytpiIMidLndBnsJ5g.png)

**45) Difference between `java.util.Date` and `java.sql.Date` in Java? ([answer](http://javarevisited.blogspot.sg/2012/04/difference-between-javautildate-and.html))**

hint: former contains both date and time while later contains only date part.

**46) Why wait and notify methods are declared in `Object` class in Java? ([answer](http://javarevisited.blogspot.sg/2012/02/why-wait-notify-and-notifyall-is.html))**

hint: because they require a lock that is only available to an object.

![](https://miro.medium.com/v2/resize:fit:500/1*ZFtmAEtT5RVLD_-X0974qg.png)

**47) Why Java doesn’t support multiple inheritances? ([answer](http://javarevisited.blogspot.sg/2011/07/why-multiple-inheritances-are-not.html))**

hint: It doesn’t support because of a bad experience with C++, but with Java 8, it does in some sense — only multiple inheritances of `Type` are not supported in Java now.

**48) Difference between Checked and Unchecked Exception in Java? ([answer](http://javarevisited.blogspot.sg/2011/12/checked-vs-unchecked-exception-in-java.html))**

hint: In case of checked, you must handle exception using catch block, while in case of unchecked, it’s up to you; compile will not bother you.

![](https://miro.medium.com/v2/resize:fit:875/1*tOIvNBF0x3eSR6Yezdf3Vg.jpeg)

**49) Difference between Error and Exception in Java? ([answer](http://www.java67.com/2012/12/difference-between-error-vs-exception.html))**

hint: I am tired of typing please check the answer

**50) Difference between Race condition and Deadlock in Java? ([answer](http://javarevisited.blogspot.sg/2012/02/what-is-race-condition-in.html#axzz59AbkWuk9))**

hint: both are errors that occur in a concurrent application, one occurs because of thread scheduling while others occur because of poor coding. See [Multithreading and Parallel Computing in Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fmultithreading-and-parallel-computing-in-java%2F) to learn more about deadlock, Race Conditions, and other multithreading issues.

1. Difference between static and non-static methods, variables And explain their memory architecture as well?
2. What do you understand by using of final keyword with classes and variables as well, give the case where you will prefer to use the final keyword?
3. What is typecasting? Suppose there is a data which is of type double then how can you show that double in int data type?
4. What are the main advantages of polymorphism? And what is the alternate of polymorphism?
5. What is constructor chaining in java?
6. Explain constructor with the help of inheritance?
7. ‘Super’ keyword is used to access superclass properties, but what when you are not allowed to use super then how can you access the property of superclass, if yes then how?
8. Suppose you have 11th, 12th class books in your beg, now how will you use inheritance to show the relationship between them?
9. Why java compiler needs main method static only?
10. What do you understand by anonymous word? And what is the impact of anonymous array and object in java? Explain memory structure with or without anonymous?
11. Why java requires inner class? What do you understand by static inner classes in java? And where will you use a static and non-static class?
12. An abstraction is hiding information in java, how java showing abstraction and write a program where you have to show abstraction and do the same program without abstraction?
13. What are different ways to create an object in java? And what do you understand by object creation in java? Where the memory will be allocated when the object is created in java?
14. JVM is compiler in java to run your program, explain steps from writing your code to execute on the machine?
15. What is heap memory allocation in java? Explain the difference between stack and heap memory allocation in java?
16. How JVM knows about your program and what is the cycle of code execution in java?
17. Difference between public, private and protected modifiers and explain why do you need all these modifiers in your code?
18. What will be the result If java set the main method to private?
19. What is command line argument and how can you give order to java program to execute a file reading operation by command line argument?
20. Where do you need super constructor and suppose you don’t have super constructor then is there any way to execute superclass constructor, if yes then explain?
21. The interface is about 100% abstraction, what do you understand by 100% abstraction and how can you achieve 100% abstraction in java? Write the same program from both interface and abstract class, now as you can write the same code with abstract class then why do you need an interface in java?
22. What is multilevel inheritance in java? And does java support multiple inheritances, explain your thoughts?
23. Java is object-oriented language, explain both object and oriented word?
24. What do you understand by design patterns in oops, if you have to design your own patterns then what are the parameters you will consider most?
25. Write some basic programs like: <1>. Palindrome,< 2>. String reverse, <3>. Patterns of stars in all possible ways, <4>.Find out minimum and maximum numbers in a given array, <5>. You are given city name and person name blank array of fixed-sized, write a program to get the city name of a person. You have to take city name and person name at run time, <6>. Write matrix multiplication program in java, <7>. How will you break an array in an equal part? Consider all possible cases, <8>. Write a program using switch case where you have to ask day name from the user and then you will print the first three letters of that day in the capital letter as a response to the user,<9>. Ask the user to give a string as input then show repeated letters with count as a response, <10>. Convert any given number into binary format, <11>. Read context from a file and replace every small letter into capital and every capital letter into the small letter and then print the modified file as the response of program,<12>. Write a program where the program will ask the user about name, age, address and college name, then you will print the detail in order but if user repeats the same name again then show available data of the user.
26. What do you understand by the break and continue keyword in an iteration?
27. Write all possible syntax of for loop?
28. What is the difference between while and for loop? And explain the cases where which one suits better?
29. What do you understand by variable scope? Is it required to initialize the local variable explain why so?
30. What is an interpreter in java? And the difference between compilation and interpretation in java?
31. What do you get by mean of return type in java? And suppose you have to return int data but return type of method is double, explain will it work or not?
32. Whether you can override superclass methods or variables? Explain it?
33. What is object chaining in java?
34. Difference between parameters and arguments in java?
35. Write a singleton class in java? And where, why you will prefer singleton in any case?
36. As java have multi-threaded programming nature, first explain what is it? Then : <1>.Why do you need it? <2>.Explain and write every possible case to create a thread in java? ❤>What is thread sleeping mean in java?<4>.Suppose you have two different files at any location then write a program with two threads where every single thread will read and print single file but both will do the operation at the same time. So file 1 will be read by thread 1 and file 2 will be read by thread 2. <5>. Explain thread architecture in java? <6>. What is thread pooling in java? <7>. Read some basic function related to multithreading in java.
37. Whether java is procedural language or functional language explain it?
38. What are the parameters that make java different from other language give some practical examples where java suits better than any other language?
39. Why exception handling is introduced in java? List down all the causes behind this?
40. Let's consider java is not having error handling mechanism then write a function where you need to handle ArrayIndexOutOfBoundException yourself.
41. Difference between try, catch and finally?
42. Consider your body as a task and then design every body part as per oops concept. (think as per your convenience).
43. Try to relate every oop concept from your surrounding.

1. **What is the volatile keyword in Java?**
2. **What is synchronization in Java and when do we use it?**
3. **Explain enum in Java with a use case.**
4. **What is serialization and why is it used?**
5. **If a Student object has normal, static, and transient fields — which ones get serialized?**
6. **What is serialVersionUID and why is it important in serialization?**

🔹 **HashMap & Collections**

1. **What kind of keys and values does a HashMap accept?**
2. **Why use Map.Entry when we can directly iterate over the Map?**
3. **Can we use both primitive and object types as keys or values in a Map?**
4. **What is a Set in Java and how is it different from a List?**

🔹 **Stream API & Java 8 Features**

1. **What are the two types of stream operations in Java 8?** (Hint: Intermediate & Terminal)
2. **What is flatMap in Java Streams and how is it different from map?**
3. **Have you used map() and flatMap() in your real project? Share an example.**

🔹 **Java 7 Logic-Based Coding/ JAVA 8**

1. **Write a Java 7 program to find the frequency of each character in a string (ignoring spaces).( asked to write the same code in java 8 also).**
2. **Can you explain how your frequency map logic works under the hood?**

🔹 **Spring & Spring Boot (Stereotypes & Behavior)**

1. **What are stereotype annotations in Spring Boot? (@Component, @Service, @Controller, etc.)**
2. **What happens if we put @Service on a controller class and @Controller on a service? Will the server start?**
3. **If annotations are swapped incorrectly, will Postman requests still work?**

🔹 **Spring Boot Config & Properties**

1. **How can we access a property defined in application.properties inside a class?**
2. **What happens if we use @Value but forget to define the key in the properties file?**
3. **What if both key and value are missing from application.properties?**
4. **Can we provide a default value using @Value?**
5. **What happens if the property is missing? Will the app crash or use default?**

🔹 **Spring Core Concepts**

1. **What is the @Primary annotation in Spring?**
2. **What is tight coupling in Java?** (e.g., “I always want a Car object, no matter what.”)
3. **What does @Autowired do, and how does it work behind the scenes?**
4. **What happens if we create an object using new even though we’ve used @Autowired?**
5. **If we manually instantiate the same object in 10 classes using new, what are we losing?**

**Core Java / OOPs**

1. What are the concepts related to Object Oriented Programming?
2. How many ways can an object be created in Java?
3. How many objects will be created using a string literal?
4. Why does Java have two ways of creating strings (literal vs new keyword)?
5. What makes a class mutable or immutable?
6. Have you heard about Marker Interfaces?
7. What’s the difference between throw and throws?
8. Can we use only a try block without catch or finally?
9. Can we have multiple catch blocks?
10. What is the purpose of the finally block?
11. What’s the difference between abstract class and interface?
12. When should we use an interface and when should we use an abstract class?
13. What are the main interfaces/classes in the Collection framework?
14. What is the contract of equals() and hashCode()?
15. Internal working of HashMap?
16. On what basis does HashMap decide where to store an element?
17. Is hashing based on key, value, or both?
18. If we insert the same key in HashMap, what happens to the previous value?
19. What’s the difference between Comparable and Comparator? When to use each?
20. What are Fail-Fast and Fail-Safe iterators?
21. Why does Fail-Safe not throw exceptions?
22. How to make an ArrayList read-only?

🔹 **Java 8 / Stream API**

1. What’s the difference between Collection and Stream?
2. If Stream modifies the data using filter/map, isn’t that a modification?
3. What are the new features in Java 8?
4. What are intermediate and terminal operations in streams?
5. Have you used filter() and map()?
6. How to declare a list of integers in Java?
7. How to reverse a list using Java 8 Stream API?
8. How to sort a list using Java 8?
9. Do we have an intermediate method in Java 8 to sort a list?
10. How to find even numbers from a list?
11. How to square elements in a list and filter those greater than 25?
12. What is a functional interface?

🔹 **Design Principles / Patterns**

1. What are the SOLID principles?
2. What is the Factory Design Pattern?
3. What is Singleton? How to break Singleton?

🔹 **Multithreading**

1. How to create a thread using Thread and Runnable?
2. Which method is overridden in Runnable?
3. What happens when a thread is started?

🔹 **Architecture / Messaging**

1. What is event-driven architecture?
2. What is the Producer-Consumer problem?
3. Have you worked with Kafka or RabbitMQ?
4. What is the use of API Gateway?
5. What is message-driven architecture?

🔹 **Database / SQL**

1. What do you mean by normalization?
2. Difference between TRUNCATE, DROP, and DELETE?
3. What does @EnableJpaRepositories do in Spring Boot?
4. Write a query to find students whose names start with the letter ‘A’.

🔹 **Tools & DevOps**

1. Have you worked with any profilers?
2. Is a profiler a tool or a code snippet?
3. Have you used any performance/load testing tools like JMeter?
4. What happens in Jenkins when image creation is triggered?
5. How do you check logs in UAT/Release environment using tools like Dynatrace?

🔹 **Spring Boot / Microservices**

1. How does a Spring Boot application start?
2. What annotations are used in the Spring Boot main class?
3. Have you used GraphQL or Spring Security?
4. Have you implemented JWT or OAuth2?

# **Core Java (Beginner to Intermediate)**

1. **What are the features of Java?**Object-oriented, platform-independent, secure, robust, multithreaded, and architecture-neutral.
2. **What is the difference between JDK, JRE, and JVM?**JDK = development tools + JRE, JRE = JVM + libraries, JVM = executes bytecode.
3. **Why is Java platform-independent?**Bytecode runs on any platform with JVM.
4. **Explain the concept of OOP in Java.**Encapsulation, Inheritance, Polymorphism, and Abstraction.
5. **What is the difference between `==` and `.equals()`?**`==` checks reference, `.equals()` checks content.
6. **What is autoboxing and unboxing?**Automatic conversion between primitives and wrapper classes.
7. **How is memory managed in Java?**Through stack, heap, and garbage collection.
8. **What is the role of the `main` method in Java?**Entry point of any standalone Java application.
9. **What is a constructor? How is it different from a method?**Initializes objects; no return type and same name as class.
10. **Can we overload constructors?**Yes, by using different parameters.
11. **What is the difference between `break`, `continue`, and `return`?**`break` exits loop, `continue` skips iteration, `return` exits method.
12. **What are enhanced for-loops?**A simpler syntax for iterating over collections or arrays.
13. **What is the difference between primitive and wrapper classes?**Primitive is basic type; wrapper wraps it into an object.
14. **What are static variables and methods?**Belong to the class, not to instances.
15. **Difference between `String`, `StringBuilder`, and `StringBuffer`?**`String` is immutable, `StringBuilder` is mutable and fast, `StringBuffer` is thread-safe.
16. **Why are Strings immutable in Java?**For security, thread-safety, and caching.
17. **How does String interning work?**Stores unique string literals in a pool for reuse.
18. **What is the difference between Array and ArrayList?**Array has fixed size; ArrayList is resizable.
19. **What are generics in Java?**Enable type safety and reusability.
20. **Difference between `List`, `Set`, and `Map`.**`List` allows duplicates, `Set` doesn’t, `Map` stores key-value pairs.
21. **When to use `HashMap` vs `TreeMap` vs `LinkedHashMap`?**`HashMap` for fast access, `TreeMap` for sorted keys, `LinkedHashMap` for insertion order.
22. **What is the difference between fail-fast and fail-safe iterators?**Fail-fast throws `ConcurrentModificationException`, fail-safe doesn’t.

# **Object-Oriented Programming (Intermediate)**

1. **What is method overloading and overriding?**Overloading = same method name, different params; overriding = subclass version of superclass method.
2. **What is runtime polymorphism?**Method overriding resolved at runtime.
3. **What is the `super` keyword?**Refers to parent class methods/constructors.
4. **What is the difference between `this` and `super`?**`this` refers to current class, `super` to parent class.
5. **What is an abstract class vs interface?**Abstract class can have state; interfaces are contracts.
6. **Can we have default methods in interfaces? Why?**Yes, to provide backward-compatible enhancements.
7. **What is the diamond problem and how does Java solve it?**Ambiguity in multiple inheritance; solved via interfaces and default methods.

# **Exception Handling**

1. **What is the difference between checked and unchecked exceptions?**Checked = compile-time, Unchecked = runtime.
2. **What is `finally` block? When is it not executed?**Executes always, except when JVM exits or `System.exit()` is called.
3. **Can a `try` block exist without a `catch`?**Yes, if `finally` block is present.
4. **How does `throw` and `throws` work?**`throw` is for actual exception, `throws` declares potential exceptions.

# **Multithreading and Concurrency**

1. **What is a thread in Java?**A lightweight process for multitasking.
2. **Difference between `Runnable` and `Thread`?**`Runnable` decouples task from thread; `Thread` is more heavyweight.
3. **What are thread states?**New, Runnable, Running, Blocked, Waiting, Timed Waiting, Terminated.
4. **What is a thread-safe class? Is `HashMap` thread-safe?**Safe for use by multiple threads; `HashMap` is not.
5. **How does `synchronized` work?**Locks an object/method to ensure mutual exclusion.
6. **What is `volatile` keyword?**Ensures visibility of changes across threads.
7. **Difference between `wait()` and `sleep()`?**`wait()` releases lock; `sleep()` doesn't.
8. **What is thread starvation and deadlock?**Starvation: thread waits indefinitely; Deadlock: two threads wait on each other.
9. **What are `Callable` and `Future`?**Callable returns a value; Future holds result.
10. **What is the use of `ExecutorService`?**Manages thread pools and asynchronous task execution.
11. **Explain `CompletableFuture` with example.**Allows chaining async tasks with callback-style logic.
12. **What is ForkJoinPool and when to use it?**For parallel processing using divide-and-conquer.
13. **What is `ReentrantLock` and how is it better than `synchronized`?**More flexible locking with try-lock and fairness options.
14. **What are atomic variables?**Variables like `AtomicInteger` support lock-free thread-safe operations.

# **Java 8+ Features**

1. **What is a functional interface?**Interface with a single abstract method.
2. **What is the `@FunctionalInterface` annotation?**Marks interface as functional for compiler validation.
3. **Explain Lambda expressions.**Short syntax for implementing functional interfaces.
4. **What are method references?**Shorthand for calling existing methods.
5. **What are Java Streams?**API for processing data in a functional style.
6. **Difference between `map()` and `flatMap()`?**`map()` transforms, `flatMap()` flattens nested streams.
7. **What is lazy evaluation in Streams?**Execution deferred until terminal operation is called.
8. **What is a terminal operation?**Operation that triggers Stream processing (e.g., `collect`, `forEach`).
9. **What is `Optional` in Java?**A container to avoid null checks.
10. **How to avoid `NullPointerException` using Optional?**Use `ifPresent`, `orElse`, `map`.
11. **What is the difference between old Date API and `java.time` API?**New API is immutable and thread-safe.

# **Memory Management & Performance**

1. **What are the different memory areas allocated by JVM?**Heap, stack, method area, code cache, metaspace.
2. **How does garbage collection work in Java?**Automatically removes unreachable objects.
3. **What are strong, weak, soft, and phantom references?**Reference types that affect GC behavior differently.
4. **What is a memory leak in Java?**When unused objects are unintentionally retained.
5. **How do you analyze and fix OutOfMemoryError?**Heap dump analysis and optimizing memory usage.
6. **What are Java profilers?**Tools like JVisualVM, YourKit to monitor performance.

# **Java Design Patterns**

1. **What is a Singleton Pattern? How to implement it?**One instance per JVM; use private constructor + static instance >>> private constructor and a thread-safe, lazy-loaded static accessor >>> Use ENUM for more robustness
2. **Explain Factory Pattern.**Creates objects without exposing instantiation logic.
3. **What is the Builder Pattern?**Constructs complex objects step-by-step.
4. **What is the Observer Pattern?**One-to-many dependency for event notification.
5. **Difference between Strategy and State pattern?**Strategy = interchangeable behaviors; State = internal state changes.

# **Java and APIs**

1. **What is Java Reflection API?**Inspect or modify classes/methods/fields at runtime.
2. **What is `Annotation`? How are custom annotations created?**Metadata for code; use `@interface`.
3. **How does Serialization work in Java?**Converts object to byte stream.
4. **What is the `transient` keyword?**Prevents serialization of fields.

# **Java Security and Best Practices**

1. **What are best practices for exception handling?**Use specific exceptions, never swallow, log properly.
2. **How to prevent memory leaks in Java applications?**Avoid static references, use WeakReference, close resources.
3. **How do you secure a Java application?**
    
    Input validation, encryption, avoiding reflection misuse.
    
4. **How to write immutable classes?**
    
    Make class final, fields private final, no setters.
    

# **Advanced Java + Industry Usage**

1. **What is Just-In-Time (JIT) Compiler?**Improves performance by compiling bytecode to native code.
2. **What are JVM tuning parameters?**Flags to optimize memory and GC (`Xmx`, `XX:+UseG1GC`, etc.).
3. **How to analyze GC logs?**Use tools like GCViewer to detect frequency, pause time.
4. **What is the Java Platform Module System (JPMS)?**Modularizes JDK and large apps since Java 9.
5. **Difference between modular and non-modular applications?**Modular uses `module-info.java`, non-modular doesn’t.
6. **What are Records in Java?**Immutable data carriers with concise syntax.
7. **Can Records implement interfaces?**
    
    Yes, but cannot extend classes.
    
8. **What are Sealed Classes?**Restrict which classes can extend them.
9. **How do they help in type safety?**Enforce control over class hierarchy.
10. **What are virtual threads in Java?**Lightweight threads introduced in Java 21.
11. **Difference between platform and virtual threads?**Virtual threads use less memory and context-switch overhead.
12. **What problems do virtual threads solve?**Scalability in high-concurrency apps.

# **Java in System Design and Microservices**

1. **How do you handle concurrency in microservices using Java?**
    
    With
    
    `ExecutorService`
    
    ,
    
    `CompletableFuture`
    
    , and proper DB locking.
    
2. **How do you implement caching in Java?**Use libraries like Caffeine, Ehcache, or Redis.
3. **What is circuit breaker pattern and how is it used in Java?**Prevents cascading failures; use Resilience4j or Hystrix.
4. **How do you use Java with Kafka or RabbitMQ?**Through official client libraries for pub/sub and messaging.
5. **How do you implement idempotency in Java APIs?**Use unique request IDs or tokens and database checks.

# **Testing in Java**

1. **What is the difference between Unit and Integration testing?**Unit tests individual components; Integration tests system parts together.
2. **What is Mockito? How to mock dependencies?**A mocking framework to simulate dependencies.
3. **How to write parameterized tests in JUnit?**Use `@ParameterizedTest` with `@ValueSource` or `@CsvSource`.
4. **What is test coverage and how do you measure it?**% of code exercised by tests; use Jacoco or Cobertura(legacy, not updated from long time), Codecov.

# **Miscellaneous / Situational**

1. **What happens when `System.gc()` is called?**
    
    Suggests JVM to perform GC; not guaranteed.
    
2. **Can you write a thread-safe singleton?**Yes, using `enum` or `synchronized` block.
3. **How do you design a rate limiter in Java?**Use token bucket or leaky bucket algorithms.
4. **How do you handle 10M+ records in Java efficiently?**Use batching, streaming, and paging.

# **1. What are the new features in Java 17 and 21?**

**Java 17 (LTS)** introduced:

- Sealed Classes
- Pattern Matching for `switch`
- Enhanced `instanceof`

**Java 21** adds:

- Virtual Threads (Project Loom)
- Record Patterns
- Structured Concurrency
- Scoped Values

👉 *Follow-up: How do virtual threads improve scalability in web applications?*

# **2. What is the difference between `var`, `record`, and `sealed` classes?**

- `var`: Local variable type inference (Java 10)
- `record`: Immutable data classes (Java 14+)
- `sealed`: Restricted inheritance (Java 17+)

# **3. Explain the internal working of `HashMap`.**

- Buckets and hashing
- Handling collisions using Linked List / Tree (since Java 8)
- Resizing logic
- Load factor and threshold

# **🔹 Java 8+ Features (Still Frequently Asked)**

# **4. What are functional interfaces and how are they used with lambdas?**

Example:

```
@FunctionalInterface
interface Calculator {
    int operate(int a, int b);
}
```

Usage:

```
Calculator add = (a, b) -> a + b;
```

# **5. Explain Stream API and how it differs from loops.**

- Lazy evaluation
- Functional-style coding
- Parallel streams for multi-core optimization

# **🔹 Spring Boot and Modern Java Frameworks**

# **6. What are the major features of Spring Boot 3.x?**

- Native Compilation support with GraalVM
- Jakarta EE 10 alignment
- Observability via Micrometer
- Java 17+ baseline

# **7. What is dependency injection and how is it implemented in Spring?**

Spring uses:

- Constructor injection (preferred)
- Field injection
- Setter injection

```
@Component
public class Service {
    private final Repo repo;
    public Service(Repo repo) {
        this.repo = repo;
    }
}
```

# **8. What is the difference between `@Component`, `@Service`, `@Repository`, and `@Controller`?**

All are component stereotypes but serve different layers:

- `@Service` for business logic
- `@Repository` for persistence
- `@Controller` for MVC web layer
- `@Component` is generic

# **🔹 Reactive Programming and WebFlux**

# **9. What is Reactive Programming in Spring?**

- Non-blocking, event-driven model
- Built using Project Reactor (Mono, Flux)
- Used in Spring WebFlux

```
public Mono<User> getUser(String id) {
    return userRepository.findById(id);
}
```

# **10. What is the difference between Spring MVC and Spring WebFlux?**

![](https://d675ssp99jaw39.archive.ph/wzoum/229d035e88b10f06995cb47e268d5bb2974be2a2.webp)

# **🔹 Database & JPA**

# **11. Explain JPQL vs Native Query.**

- JPQL: Object-oriented queries (on entities)
- Native: SQL-based queries directly on tables

# **12. How do you handle N+1 problems in JPA?**

- Use `@EntityGraph`
- `JOIN FETCH` in JPQL
- Hibernate batch fetching

# **🔹 Security, DevOps, and Observability**

# **13. How does Spring Security integrate with JWT?**

- Stateless auth
- Custom filters for token parsing
- OAuth2 / Keycloak integration for SSO

# **14. What are some tools you use for observability in Spring Boot?**

- **Micrometer**
- **Prometheus + Grafana**
- **Spring Boot Actuator**

# **15. How is a Spring Boot app deployed in Kubernetes?**

- Dockerize the app using `Dockerfile`
- Create `Deployment` and `Service` YAMLs
- Use ConfigMaps and Secrets
- Monitor with Prometheus

# **🔹 Microservices & Cloud-Native Java**

# **16. How do microservices communicate?**

- REST APIs (synchronous)
- Kafka/RabbitMQ (asynchronous)
- gRPC (binary protocol)

# **17. How to handle distributed configuration in Spring Boot?**

- Spring Cloud Config
- Vault for secrets
- Consul or Zookeeper

# **18. How do you implement resilience in microservices?**

- Retry, Fallback: Resilience4j
- Circuit Breakers: Resilience4j / Hystrix (legacy)
- Bulkheads, Rate Limiting

# **🔹 Testing & Best Practices**

# **19. What’s the difference between `@Mock`, `@Spy`, and `@InjectMocks` in Mockito?**

- `@Mock`: Creates dummy
- `@Spy`: Partial mock (real object + stubs)
- `@InjectMocks`: Injects mocks into actual object

# **20. How do you test a REST API in Spring Boot?**

- Use `@WebMvcTest` for controller layer
- Mock dependencies using Mockito
- Use `MockMvc` or `TestRestTemplate`

```
mockMvc.perform(get("/api/users"))
       .andExpect(status().isOk());
```

# **🔹 Bonus: Behavioral & Real-world Questions**

# **21. How do you handle memory leaks in Java applications?**

- Profiling with VisualVM / JMC
- Check GC logs
- Analyze heap dumps

# **22. Describe a recent challenge in a Java project and how you solved it.**

📌 *Pro Tip:* Focus on debugging, scaling, performance optimization, or refactoring legacy code.

# **Core Java Interview Questions and Answers — Get Java Interview-Ready**

# **1. What is Java?**

Java is a high-level, object-oriented programming language that is designed to be platform-independent, meaning you can write code once and run it anywhere with the Java Virtual Machine (JVM).

It’s easy to learn for beginners and widely used for building web, mobile, and enterprise applications. Java is known for its robustness, security features, and versatility. It supports modular and reusable code through its object-oriented principles, and it comes with a rich set of libraries and frameworks to streamline development.

[**What is Java?This post provides everything you'll need to know about getting started with the Java programming language.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/11/java-programming-language-getting-started.html)

You may also get a question like What are the key features of Java?

Refer to this article: [Main Features of Java ( Explained with Examples )](https://archive.ph/o/L24n2/https://www.javaguides.net/2025/04/main-features-of-java-explained.html)

# **2. What is the Java Virtual Machine (JVM)?**

**Answer:**The JVM is a **virtual machine that executes Java bytecode**. It converts bytecode into machine-specific code and handles tasks like **memory management, garbage collection, and security**. The JVM is what makes Java platform-independent.

## **Why is the JVM Important?**

The JVM makes Java a platform-independent language. It allows developers to write code once and run it anywhere. The JVM also handles memory management, security, and performance optimization, making Java applications reliable and efficient.

[**What is JVM?Blog about guides/tutorials on Java, Java EE, Spring, Spring Boot, Microservices, Hibernate, JPA, Interview, Quiz…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2024/09/what-is-jvm.html)

# **3. What is the difference between JDK, JRE, and JVM?**

## **JDK (Java Development Kit)**

🧑‍💻 **JDK is the full toolbox for Java developers.**

**What it includes:**

- JRE (which includes JVM)
- Java compiler (`javac`)
- Debugger (`jdb`)
- Other dev tools (like `jar`, `javadoc`, etc.)

> ✅ Use JDK when you want to WRITE, COMPILE, and RUN Java programs.
> 

## **JRE (Java Runtime Environment)**

⚙️ **JRE is a software package that contains everything needed to run a Java program.**

**What it includes:**

- JVM (Java Virtual Machine)
- Libraries and class files needed at runtime (like `rt.jar`)
- Other supporting files

**What it doesn’t include:**

- Compiler (`javac`)
- Development tools

## **JVM (Java Virtual Machine)**

🧠 **JVM is the brain behind Java.**

**What it does:**

- It **runs Java bytecode** (compiled `.class` files).
- Converts bytecode into **machine-specific instructions**.
- Provides features like: Garbage collection, Memory management, Security and runtime optimization.

![](https://dd3bvkffiijvsa.archive.ph/L24n2/d4ad242ad75c5437c432bc03afc9eafac78c9c33.webp)

[**What is JDK, JRE and JVM in Java - Explained with DiagramsIn this post, we will discuss an important definition of JVM, JRE, and JDK in the Java programming language. We also…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2019/02/java-jvm-jre-jdk-explained-with-diagrams.html)

# **4. What is a class and an object in Java?**

**Answer:**

- A **class** is a blueprint or template for creating objects. It defines properties and behaviors.
- An **object** is an instance of a class. It holds real values for the properties defined in the class.

**Example:**

```
class Car {
    String color;
    void drive() {
        System.out.println("Driving...");
    }
}

Car myCar = new Car(); // object
myCar.color = "Red";
myCar.drive();
```

[**Object Oriented Programming in Java with ExamplesThis page contains a list of tutorials, and examples on important OOPS concepts and OOPS principles.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/object-oriented-design.html)

# **5. What is the main() method in Java?**

**Answer:**The `main()` method is the **entry point** of any Java application. It has a specific signature that the JVM looks for when starting a program.

```
public static void main(String[] args) {
    // code to run
}
```

- `public` – accessible from anywhere
- `static` – no need to create an object to call it
- `void` – does not return any value
- `String[] args` – receives command-line arguments

[**Java main() Method Interview Questions with AnswersLooking for a simple and complete guide to Java’s main() method interview questions? You’re in the right place!**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/java-main-method-interview-questions-with-answers-7cb7456dd855)

# **6. What is the difference between primitive and non-primitive data types?**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/627a28136d23c1cc846b66abe9af3ec0a02fa569.webp)

# **7. What is a constructor in Java?**

**Answer:**A constructor is a **special method** used to **initialize objects**. It has the same name as the class and **no return type**. It is called automatically when an object is created.

```
public class Student {
    String name;
    Student(String n) {
        name = n;
    }
}
```

Java also provides a **default constructor** if none is defined.

# **8. What is method overloading?**

**Answer:**Method overloading means **defining multiple methods with the same name** but different parameters (number, type, or order).

```
void print(int a) { }
void print(String s) { }
void print(int a, String s) { }
```

It increases the **readability** and **flexibility** of the program.

[**Method Overloading in Java with ExamplesIn Java, it is possible to define two or more methods within the same class that share the same name, as long as their…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/09/method-overloading-in-java-with-examples.html)

# **9. What is the use of the `this` keyword in Java?**

The `this` keyword refers to the **current object**. It is used when **instance variables are shadowed** by method or constructor parameters.

```
class Employee {
    String name;
    Employee(String name) {
        this.name = name; // refers to instance variable
    }
}
```

# **10. What is garbage collection in Java?**

Garbage collection is a process in which the **JVM automatically removes unused or unreachable objects** from memory to free up space. It helps manage memory efficiently and prevents memory leaks.

You can suggest garbage collection using:

```
System.gc();
```

But the JVM decides when to actually run it.

# **11. What are the four main principles of Object-Oriented Programming (OOP) in Java?**

The four key principles of OOP are:

- **Encapsulation**: Hiding internal details and exposing only essential features using classes and access modifiers.
- **Abstraction**: Hiding complex implementation and showing only necessary details using abstract classes or interfaces.
- **Inheritance**: Reusing code by deriving a new class from an existing one.
- **Polymorphism**: Ability to take many forms — method overloading (compile-time) and method overriding (runtime).

[**OOPs Concepts in Java with ExamplesObject-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", contains data and…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/08/oops-concepts-in-java.html)

# **12. What is the difference between `==` and `.equals()` in Java?**

**Answer:**

- `==` checks **reference equality** — whether two references point to the same object.
- `.equals()` checks **value equality** — whether two objects have the same content (when overridden properly).

**Example:**

```
String a = new String("Java");
String b = new String("Java");

System.out.println(a == b);      // false
System.out.println(a.equals(b)); // true
```

# **13. What are access modifiers in Java?**

**Answer:**Access modifiers control the **visibility** of classes, methods, and variables. Java provides four main access levels:

![](https://dd3bvkffiijvsa.archive.ph/L24n2/34d7c64738b8f05f4df1eb2a4c7ffe37accb363d.webp)

[**Java Access ModifiersIn this article, we will discuss Java access modifiers - public, private, protected & default, which are used to…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/10/java-access-modifiers-public-private-protected-default.html)

# **14. What is the difference between `static` variables and `instance` variables?**

**Answer:**

- **Static variables** belong to the **class**, not to any object. Only one copy exists.
- **Instance variables** belong to **each object**. Every object has its own copy.

**Example:**

```
class Counter {
    static int count = 0;
    int id;

    Counter() {
        count++;
        id = count;
    }
}
```

[**static variable vs instance variable in JavaA static variable is associated with the class itself. In contrast, an instance variable is associated with a specific…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2023/11/static-variable-vs-instance-variable-in-java.html)

# **15. What is method overriding?**

**Answer:**Method overriding is when a **subclass provides a new implementation** for a method that is already defined in its superclass.

- The method must have the **same name, return type, and parameters**.
- The method in the subclass should not have **less access** than the superclass method.
- Use the `@Override` annotation for clarity.

[**Method Overloading vs Method Overriding in JavaIn this article, we will explore the differences between Method Overloading and Method Overriding in Java, understand…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2025/04/method-overloading-vs-method-overriding-in-java.html)

# **16. Can we override a `static` method in Java?**

**Answer:**No, we cannot truly override a static method. Static methods belong to the class, not objects, so **method hiding** occurs instead of overriding.

**Example:**

```
class A {
    static void show() {
        System.out.println("Class A");
    }
}

class B extends A {
    static void show() {
        System.out.println("Class B");
    }
}
```

Calling `B.show()` calls B’s version, but it’s **not true polymorphism**.

[**Can You Override Private or Static Methods in Java?Understand whether private or static methods can be overridden in Java. Learn the difference between method hiding and…**medium.com](https://archive.ph/o/L24n2/https://medium.com/javarevisited/can-you-override-private-or-static-methods-in-java-924ace8db355)

# **17. What is the purpose of the `final` keyword in Java?**

**Answer:**`final` is used to declare:

- **Final variable**: Value cannot be changed after assignment.
- **Final method**: Cannot be overridden.
- **Final class**: Cannot be extended (e.g., `String` class).

[**final Java Keyword with ExamplesThe final keyword in Java is used to restrict the user. The final keyword can be used with variable, method, and class.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/12/final-java-keyword-with-examples.html)

# **18. What is a constructor overloading?**

**Answer:**Constructor overloading means defining **multiple constructors** in a class with different parameter lists. It allows objects to be initialized in different ways.

**Example:**

```
class Book {
    Book() { }
    Book(String title) { }
    Book(String title, String author) { }
}
```

# **19. What is `super` keyword in Java?**

**Answer:**The `super` keyword is used to refer to the **immediate parent class**. It can be used to:

- Call the parent class constructor: `super()`
- Access parent class methods or variables: `super.methodName()`

# **20. What is the difference between compile-time and run-time polymorphism?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/6d30fda4ba64fe2652ba2d37485c12e99bea80cf.webp)

# **21. What is the difference between an abstract class and an interface in Java?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/618ae6945cf79143161e31e18b78fca124d63e65.webp)

# **22. What is the purpose of the `interface` keyword in Java?**

**Answer:**An `interface` defines a **contract** that a class must follow. It contains **method declarations** without implementations (except for default/static methods). A class implements an interface using the `implements` keyword.

**Example:**

```
interface Vehicle {
    void start();
}

class Car implements Vehicle {
    public void start() {
        System.out.println("Car started");
    }
}
```

# **23. What is exception handling in Java?**

**Answer:**Exception handling is a mechanism to **handle runtime errors** and prevent the program from crashing. Java provides:

- `try` block to write risky code
- `catch` block to handle exceptions
- `finally` block to execute code regardless of exceptions
- `throw` to manually throw an exception
- `throws` to declare exceptions

**Example:**

```
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
}
```

[**Java Exception Handling TutorialThis is a complete tutorial to exception handling in Java. The source code examples of this guide are well tested with…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-exception-handling-tutorial.html)

# **24. What is the difference between `throw` and `throws`?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/22f05fb63fa1486a48990724fe1a43375fd92f15.webp)

# **25. What is the difference between checked and unchecked exceptions?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/1c2f74f9db92ca9f7b9bdba70826e3f005a98a33.webp)

# **26. What is the use of `finally` block?**

**Answer:**The `finally` block is used to write **clean-up code** (like closing a file, releasing a database connection). It **always executes** whether an exception is thrown or not.

```
try {
    // code
} catch (Exception e) {
    // handle
} finally {
    System.out.println("Always runs");
}
```

# **27. What are wrapper classes in Java?**

In Java, wrapper classes are used to convert primitive types into objects.

Java is an object-oriented language, but primitive types like `int`, `double`, `char` are not objects.

So Java provides wrapper classes for each primitive data type to help you use them like objects.

![](https://dd3bvkffiijvsa.archive.ph/L24n2/f8281ef71724c6b54f1c1569afc10b4c5847fac5.webp)

**Example:**

```
int x = 10;
Integer obj = Integer.valueOf(x); // Boxing
int y = obj.intValue();           // Unboxing
```

[**Wrapper Classes in Java: A Simple GuideLearn what wrapper classes are in Java, why they’re important, and how to use them effectively. Includes code examples…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/wrapper-classes-in-java-a-simple-guide-3a10dbc4e5bb)

# **28. What is autoboxing and unboxing in Java?**

**Answer:**

- **Autoboxing**: Automatic conversion of a primitive to a wrapper class object.
- **Unboxing**: Automatic conversion of a wrapper class object back to a primitive.

**Example:**

```
Integer a = 10; // Autoboxing
int b = a;      // Unboxing
```

Introduced in **Java 5** to simplify code when using collections and generics.

[**Autoboxing and Unboxing in Java: A Simple Guide for BeginnersLearn what autoboxing and unboxing are in Java, why they matter, and how they simplify working with primitive types and…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/autoboxing-and-unboxing-in-java-a-simple-guide-for-beginners-311d8333d972)

# **29. What is the difference between `String`, `StringBuilder`, and `StringBuffer`?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/afec2f27a528b2dd81eefaf803eecdb69212c7eb.webp)

[**String vs StringBuilder vs StringBuffer in JavaString: Use when the text won't change, and thread safety is required. StringBuilder: Use in a single-threaded…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2023/08/string-vs-stringbuilder-vs-stringbuffer.html)

# **30. What is the difference between `==` and `.equals()` in the case of `String`?**

**Answer:**

- `==` compares **references** (memory locations).
- `.equals()` compares **values** (actual characters in the string).

**Example:**

```
String a = new String("Java");
String b = new String("Java");

System.out.println(a == b);      // false
System.out.println(a.equals(b)); // true
```

Always use `.equals()` for value comparison in strings.

# **31. What is the Java Collections Framework?**

**Answer:**The Java Collections Framework is a set of classes and interfaces that provide **data structures** and **algorithms** to store, retrieve, and manipulate data efficiently. It includes:

- **Interfaces** like `List`, `Set`, `Queue`, `Map`
- **Implementations** like `ArrayList`, `HashSet`, `LinkedList`, `HashMap`, etc.

It supports both **generic** and **non-generic** types and provides operations like sorting, searching, and iteration.

[**Java Collections TutorialThis tutorial is a one-stop shop for all the Java collections interfaces, implementation classes, interface questions…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-collections-tutorial.html)

# **32. What is the difference between ArrayList and LinkedList?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/8ff74cb9691cacbe89f48ecf45c7535af3943aa4.webp)

[**Difference between ArrayList and LinkedList in JavaIn this post, we will discuss the difference between ArrayList and LinkedList in Java.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2020/08/difference-between-arraylist-and-linkedlist-in-java.html)

# **33. What is the difference between HashSet and TreeSet?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/fa16dacb85ef94223289d1614af913d27eb52352.webp)

[**HashSet vs TreeSet: Difference Between HashSet and TreeSet in JavaIn this article, we will discuss the difference between HashSet and TreeSet in Java with examples.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2023/08/hashset-vs-treeset-in-java.html)

# **34. What is the difference between Iterator and ListIterator?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/1d3a849bffb9c439c7837ac046b5fdc3fe7fcf5c.webp)

# **35. What are Generics in Java?**

**Answer:**Generics allow you to **define classes, interfaces, and methods with type parameters**. They enable **compile-time type checking** and eliminate the need for type casting.

**Example:**

```
List<String> names = new ArrayList<>();
names.add("Ravi");
String first = names.get(0); // No casting needed
```

Generics improve code **safety and readability**.

[**Java Generics TutorialGenerics were added in Java 5 to provide compile-time type checking and removing the risk of ClassCastException that…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-generics-tutorial.html)

# **36. What is the difference between Comparable and Comparator?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/eb8bac8f9adacfa1a6441d5ae24927d3faec99a8.webp)

# **37. What is a thread in Java?**

**Answer:**A thread is a **lightweight unit of execution** in a program. Java supports **multithreading**, which allows multiple threads to run concurrently, improving performance in CPU-bound or I/O-bound tasks.

You can create threads in two ways:

1. Extending `Thread` class
2. Implementing `Runnable` interface

[**Java Multithreading TutorialMultithreading in Java is a very important topic. In this tutorial, we will learn low-level APIs that have been part of…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-multithreading-utorial.html)

# **38. What is the difference between `start()` and `run()` methods in threads?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/04f4f6e2bc57d4aee45f140e787c00259572f333.webp)

[**Difference Between start() and run() in Java🔒 This is a Medium member-only article. If you’re not a Medium member, you can read the full article for free on my…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/difference-between-start-and-run-in-java-96affe586a85)

# **39. What is synchronization in Java?**

**Answer:**Synchronization is used to **control access to shared resources** in a multithreaded environment. It prevents **race conditions** by allowing only one thread to access a block of code or object at a time.

You can use:

- `synchronized` keyword on methods or code blocks
- `synchronized` blocks with object references

**Example:**

```
synchronized void increment() {
    count++;
}
```

# **40. What is a deadlock in Java?**

**Answer:**A deadlock is a situation where **two or more threads are blocked forever**, waiting for each other to release locks.

**Example Scenario:**

- Thread A holds Lock 1 and waits for Lock 2
- Thread B holds Lock 2 and waits for Lock 1

To avoid deadlocks:

- Always acquire locks in the same order
- Use timeout with `tryLock()` from `java.util.concurrent.locks`

# **41. What is an immutable class in Java?**

**Answer:**An immutable class is one whose **objects cannot be modified** once they are created. All the fields of an immutable object are final and set only once through the constructor.

**Example:**

```
public final class Student {
    private final String name;

    public Student(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

The `String` class in Java is a common example of an immutable class.

[**🔒 How to Make an Immutable Class in Java (Step-by-Step Guide)Learn how to create an immutable class in Java with real-world examples. Understand why immutability matters, and…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/how-to-make-an-immutable-class-in-java-step-by-step-guide-a6a91b3decc8)

# **42. What is the Java Memory Model?**

**Answer:**The Java memory model divides memory into different regions:

- **Heap**: Stores objects and class instances
- **Stack**: Stores method call frames and local variables
- **Method Area (MetaSpace)**: Stores class metadata
- **Program Counter Register**: Holds the address of the current executing instruction
- **Native Method Stack**: Used for native method calls

Understanding this model helps in optimizing memory usage and identifying memory leaks or performance bottlenecks.

# **43. Why is String immutable in Java?**

Strings in Java are immutable by design. This design decision is about more than just simplicity.

## **Key reasons:**

- **Security**: Strings are often used in sensitive areas like file paths and network connections. If a string could be changed, it could lead to vulnerabilities.
- **Performance**: Since immutable strings can be cached and reused, the JVM can optimize performance using a **string pool**.
- **Thread safety**: Immutable objects are naturally thread-safe, which avoids the need for synchronization.

## **Example:**

```
String s = "Hello";
s.concat(" World");
System.out.println(s); // prints "Hello"

s = s.concat(" World");
System.out.println(s); // prints "Hello World"
```

# **44. What is class loading in Java?**

**Answer:**Java uses **Class Loaders** to load `.class` files into memory when needed.

The three main class loaders are:

- **Bootstrap ClassLoader** — loads core Java classes from the JDK
- **Extension ClassLoader** — loads JDK extension libraries
- **Application ClassLoader** — loads classes from the classpath

Java uses **lazy loading**, meaning classes are only loaded when they are first accessed.

# **45. What is the difference between compile-time and runtime errors?**

**Answer:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/eb745e2a2923ae52ec3955dbb9c14d47e4d09f2e.webp)

# **46. What are Lambda Expressions in Java?**

**Answer:**A lambda expression is simply a function without a name. It can even be used as a parameter in a function. Lambda Expressions facilitate functional programming and simplify development greatly.

The main use of Lambda expression is to provide an implementation for functional interfaces.

**Syntax:**

```
(parameter) -> expression
```

**Example:**

![](https://dd3bvkffiijvsa.archive.ph/L24n2/6123354985f0672f08ef9d61ac83576595642b54.webp)

[**Java 8 Lambda ExpressionsIn this post, we will discuss the most important feature of Java 8 that is Lambda Expressions. We will learn Lambda…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/07/java-8-lambda-expressions.html)

# **47. What is a Functional Interface?**

**Answer:**A functional interface is an interface that has **exactly one abstract method**. It can have default or static methods.

Java 8 introduced the `@FunctionalInterface` annotation to ensure this rule.

**Example:**

```
@FunctionalInterface
interface MyFunc {
    void execute();
}
```

Common built-in functional interfaces: `Runnable`, `Callable`, `Predicate`, `Function`, `Supplier`, and `Consumer`.

[**Java 8 Functional InterfacesIn this post, we will learn the Java 8 the functional interface with examples. Key points about the functional…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/07/java-8-functional-interfaces.html)

# **48. What is the Stream API in Java?**

**Answer:**Stream API is used to **process collections** (like List or Set) in a **functional style**. It supports operations like `filter`, `map`, `reduce`, `collect`, and more.

**Example:**

```
List<String> names = List.of("Ram", "Shyam", "Ravi");
names.stream()
     .filter(name -> name.startsWith("R"))
     .forEach(System.out::println);
```

Streams help write clean, readable, and concise code for data processing.

[**Java 8 Stream API TutorialThis complete an in-depth tutorial, we will go through the practical usage of Java 8 Streams. Source code examples and…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-8-stream-api-tutorial.html)

# **49. What is Optional in Java?**

**Answer:**`Optional` is a container object used to **avoid null checks** and prevent `NullPointerException`.

**Example:**

```
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(System.out::println);
```

It encourages writing **null-safe** code in a more readable way.

[**Java 8 Optional Class with ExamplesJava introduced a new class Optional in JDK 8. It is a public final class and used to deal with NullPointerException in…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/07/java-8-optional-class.html)

# **50. What are the design principles in OOP?**

Some key OOP design principles include:

1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)
6. Encapsulate What Varies
7. DRY (Don’t Repeat Yourself)
8. YAGNI (You Aren’t Gonna Need It)
9. KISS (Keep It Simple, Stupid)
10. Composition over Inheritance
11. Dependency Injection