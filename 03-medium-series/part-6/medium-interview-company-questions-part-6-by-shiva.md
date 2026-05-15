# Medium interview company questions part 6 by Shivam Srivastava

# **Scenario Based Interview Question — 3**

# **Scenario**

In a microservices architecture, multiple teams often publish messages to a shared Kafka topic. Suppose another team publishes a message to `my-topic`, but its format differs from what the consumer service expects. Since the consumer does not know the structure of this new message, it fails to deserialize it, leading to repeated failures.

# **Problem Statement:**

- **Endless Loop of Failures:** The consumer keeps encountering deserialization errors, preventing it from processing any other messages in the topic queue.
- **Service Downtime:** The consumer becomes stuck, resulting in a potential service outage.
- **No Visibility on Failures:** Without proper logging or redirection, debugging the issue becomes difficult.

Kafka consumers may repeatedly fail while processing messages unless proper error handling mechanisms are in place. This can lead to cascading failures across microservices.

# **Answer:**

## **Handling Kafka Message Deserialization Failures Without Stopping the Consumer:**

In a Kafka-based system, message deserialization failures are common and can cause serious issues if not handled properly. The default behavior of Kafka consumers is to stop processing when they encounter deserialization errors, potentially leading to a complete halt in message consumption.

## **Why Do Deserialization Failures Occur?**

Deserialization failures typically happen due to:

- **Schema Evolution Issues** — Consumer expects a different schema than the producer.
- **Corrupt Messages** — Malformed messages due to upstream issues.
- **Incorrect Deserializer Configuration** — Consumer is not configured with the right deserializer.
- **Message Type Mismatch** — The expected object type does not match the received data.

Kafka deserialization failures can break consumers, causing data loss, increased latencies, and operational overhead. To ensure consumers remain resilient, we can adopt a structured approach that includes:

- **Safe Deserializers** to catch failures gracefully.
- **Dead Letter Queues (DLQ)** to handle unprocessable messages.
- **Schema Registry Validation** to prevent schema mismatches.
- **Retry Mechanisms** before discarding messages.Let’s explore these strategies in depth.

## **Step 1: Implementing a Safe Deserializer**

A custom deserializer ensures that failures are logged and problematic messages are wrapped in an error object instead of crashing the consumer.

```
import org.apache.kafka.common.serialization.Deserializer;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.DeserializationFeature;
import java.util.Base64;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SafeKafkaDeserializer<T> implements Deserializer<T> {
    private static final Logger logger = LoggerFactory.getLogger(SafeKafkaDeserializer.class);
    private final ObjectMapper objectMapper = new ObjectMapper();
    private static final Counter failedDeserializationCounter = Metrics.counter("kafka_failed_deserialization_total");
    private Class<T> targetType;

    public SafeKafkaDeserializer() {
        objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    @Override
    @SuppressWarnings("unchecked")
    public void configure(Map<String, ?> configs, boolean isKey) {
        String className = (String) configs.getOrDefault("value.deserializer.target.type", "");
        if (className.isEmpty()) {
            logger.error("Missing 'value.deserializer.target.type' configuration.");
            throw new RuntimeException("Missing 'value.deserializer.target.type' configuration.");
        }
        try {
            targetType = (Class<T>) Class.forName(className);
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Invalid target class for deserialization: " + className, e);
        }
    }

    @Override
    public T deserialize(String topic, byte[] data) {
        if (data == null || data.length == 0) {
            return null;
        }
        try {
            return objectMapper.readValue(data, targetType);
        }
        catch (Exception e) {
             String encodedData = Base64.getEncoder().encodeToString(data);
             logger.error("Deserialization failed for topic {}. Base64 encoded message: {}", topic, encodedData, e);
             failedDeserializationCounter.increment();
             return (T) new ErrorWrapper("Deserialization failed", encodedData, e.getMessage());
        }
    }

    @Override
    public void close() {}

    public static class ErrorWrapper {
        private final String error;
        private final String encodedMessage;
        private final String details;

        public ErrorWrapper(String error, String encodedMessage, String details) {
            this.error = error;
            this.encodedMessage = encodedMessage;
            this.details = details;
        }

        public String getError() { return error; }
        public String getEncodedMessage() { return encodedMessage; }
        public String getDetails() { return details; }
    }
}
```

*Ensure that the Kafka consumer properties include `value.deserializer.target.type` when configuring the consumer, otherwise, this approach will not work as expected*

## **Step 2: Redirecting Failed Messages to a Dead Letter Queue (DLQ)**

If the deserializer returns `null` or an `ErrorWrapper`, the message should be redirected to a **Dead Letter Queue (DLQ)** instead of discarding it.

```
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.clients.producer.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.*;

public class KafkaConsumerWithDLQ {
    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumerWithDLQ.class);
    private static final String TOPIC = "input-topic";
    private static final String DLQ_TOPIC = "dlq-topic";
    private static final KafkaProducer<String, String> dlqProducer = createDLQProducer();
    private static final KafkaConsumer<String, Object> consumer = createConsumer();

    public static void main(String[] args) {
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            consumer.close();
            dlqProducer.close();
        }));

        consumer.subscribe(Collections.singletonList(TOPIC));

        while (true) {
            ConsumerRecords<String, Object> records = consumer.poll(Duration.ofMillis(100));
            for (ConsumerRecord<String, Object> record : records) {
                try {
                    if (record.value() instanceof SafeKafkaDeserializer.ErrorWrapper) {
                        logger.warn("Received an unprocessable message, redirecting to DLQ: {}", record.value());
                        sendToDLQ(record);
                    } else {
                        processWithRetry(record, 3);
                    }
                  }
                catch (Exception e) {
                    logger.error("Unexpected error while processing record: {}", record, e);
                    sendToDLQ(record);
                }
            }
            consumer.commitSync();
        }
    }

    private static void processWithRetry(ConsumerRecord<String, Object> record, int maxRetries) {
        int attempt = 0;
        while (attempt < maxRetries) {
            try {
                processRecord(record);
                return; // Success, exit retry loop
            } catch (Exception e) {
                attempt++;
                logger.warn("Processing attempt {} failed for record: {}", attempt, record.value(), e);
                try {
                    Thread.sleep((long) Math.pow(2, attempt) * 100); // Exponential backoff
                } catch (InterruptedException ignored) {}
            }
        }
        sendToDLQ(record); // Final fallback
    }

    private static void sendToDLQ(ConsumerRecord<String, Object> record) {
        String metadata = String.format("Offset: %d, Partition: %d, Timestamp: %d",
                record.offset(), record.partition(), record.timestamp());
        String errorData = (record.value() == null) ? "NULL" : record.value().toString();

        try {
            dlqProducer.send(new ProducerRecord<>(DLQ_TOPIC,
                    Optional.ofNullable(record.key()).orElse("UNKNOWN"),
                    metadata + " | " + errorData));
            logger.info("Message sent to DLQ: {}", errorData);
          }
        catch (Exception e) {
            logger.error("Failed to send message to DLQ: {}", e.getMessage(), e);
        }
    }

    private static void processRecord(ConsumerRecord<String, Object> record) {
        System.out.println("Processing record: " + record.value());
    }

    private static KafkaProducer<String, String> createDLQProducer() {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        return new KafkaProducer<>(props);
    }

    private static KafkaConsumer<String, Object> createConsumer() {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "consumer-group");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "your.custom.SafeKafkaDeserializer");
        return new KafkaConsumer<>(props);
    }
}
```

## **Step 3: Using Schema Registry for Schema Evolution**

To handle schema mismatches, we use **Avro with Confluent Schema Registry** to enforce schema evolution.

```
import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
import io.confluent.kafka.schemaregistry.client.SchemaRegistryClient;
import io.confluent.kafka.schemaregistry.client.rest.entities.SchemaMetadata;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.Decoder;
import org.apache.avro.io.DecoderFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SchemaValidation {
    private static final Logger logger = LoggerFactory.getLogger(SchemaValidation.class);
    private static final String SCHEMA_REGISTRY_URL = "http://localhost:8081";
    private static final String TOPIC = "your-topic-name";

    public static void validateSchema(GenericRecord record) {
        try {
            // Initialize Schema Registry Client
            SchemaRegistryClient schemaRegistry = new CachedSchemaRegistryClient(SCHEMA_REGISTRY_URL, 10);

            // Fetch latest schema from Schema Registry
            SchemaMetadata schemaMetadata = schemaRegistry.getLatestSchemaMetadata(TOPIC + "-value");
            Schema latestSchema = new Schema.Parser().parse(schemaMetadata.getSchema());

            // Validate received schema
            DatumReader<GenericRecord> reader = new GenericDatumReader<>(latestSchema);
            Decoder decoder = DecoderFactory.get().binaryDecoder(record.toString().getBytes(), null);
            reader.read(null, decoder);  // Throws an exception if schema is incompatible

            logger.info("Schema validation successful for record: {}", record);
        } catch (Exception e) {
            logger.error("Schema mismatch detected. Expected Schema: {}, Received Record: {}", TOPIC + "-value", record, e);
            sendToDLQ(record);
        }
    }

}
```

## **Consumer Configuration:**

```
key.deserializer=io.confluent.kafka.serializers.KafkaAvroDeserializer
value.deserializer=io.confluent.kafka.serializers.KafkaAvroDeserializer
schema.registry.url=http://localhost:8081
specific.avro.reader=true
use.latest.version=true
value.subject.name.strategy=io.confluent.kafka.serializers.subject.TopicNameStrategy
```

This ensures consumers can handle **evolving schemas** instead of failing due to unexpected fields.

*Ensure that the producer is also using the correct Avro schema evolution strategy (e.g., `BACKWARD`, `FORWARD`, or `FULL`) to prevent breaking changes when new fields are introduced.*

## **Step 4: Kafka Streams Exception Handling**

If using Kafka Streams, we can handle deserialization errors using a **custom DeserializationExceptionHandler**.

```
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.streams.errors.DeserializationExceptionHandler;
import org.apache.kafka.streams.processor.ProcessorContext;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.Map;

public class CustomDeserializationHandler implements DeserializationExceptionHandler {
    private static final Logger logger = LoggerFactory.getLogger(CustomDeserializationHandler.class);
    private String DLQ_TOPIC = "dead-letter-topic";
    private boolean dlqEnabled = true;

    @Override
    public void configure(Map<String, ?> configs) {
        if (configs.containsKey("dlq.topic")) {
            DLQ_TOPIC = configs.get("dlq.topic").toString();
        }
        if (configs.containsKey("dlq.enabled")) {
            dlqEnabled = Boolean.parseBoolean(configs.get("dlq.enabled").toString());
        }
    }

   @Override
    public DeserializationHandlerResponse handle(ProcessorContext context, ConsumerRecord<byte[], byte[]> record, Exception exception) {
    logger.error("Deserialization error for record: {}", record.value() != null ? new String(record.value()) : "null", exception);

    if (dlqEnabled && record.value() != null) {
        try {
            context.forward(new ProducerRecord<>(DLQ_TOPIC, record.key(), record.value()));
        } catch (Exception ex) {
            logger.error("Failed to forward message to DLQ: {}", ex.getMessage(), ex);
        }
    }

    return DeserializationHandlerResponse.CONTINUE;
}
}
```

## **Configuring Kafka Streams:**

```
Properties props = new Properties();
props.put(StreamsConfig.DEFAULT_DESERIALIZATION_EXCEPTION_HANDLER_CLASS_CONFIG, CustomDeserializationHandler.class.getName());
```

# **Final Thoughts**

We have created a **fault-tolerant Kafka consumer** that can:

- **Safely deserialize messages** without crashing
- **Redirect failed messages** to a DLQ for debugging
- **Handle schema evolution** seamlessly using Avro and Schema Registry
- **Recover from exceptions** using Kafka Streams exception handlers

# **Scenario Based Java Interview Question — 2**

# ***Scenario:***

Your team is preparing to upgrade a critical Java application from Java 8 to Java 17. The upgrade involves significant changes in language features, library support, and performance optimizations.

# ***Question:***

Describe your strategy for planning and executing this major version upgrade.

How would you handle the technical challenges of migrating legacy code, ensure compatibility with third-party libraries?

# **Answer:**

## **Strategy for Upgrading from Java 8 to Java 17**

Upgrading from Java 8 to Java 17 is a significant leap. So, let’s start:

# **1. Key Compatibility Issues & Solutions**

**a) Removal of Java EE Modules (JAXB, JAX-WS, CORBA)**

- **Issue**: Java 17 removes Java EE modules like JAXB, JAX-WS, and CORBA.
- **Solution**: Migrate to Jakarta EE, which replaces the old `javax` namespaces with `jakarta`. This requires changing dependencies and package imports in your codebase.

```
<dependencies>
  <dependency>
    <groupId>jakarta.xml.bind</groupId>
    <artifactId>jakarta.xml.bind-api</artifactId>
    <version>2.3.3</version>
  </dependency>
</dependencies>
```

**b) Encapsulation of Internal APIs (JEP 403)**

- **Issue**: Java 17 restricts access to internal APIs like `sun.misc.Unsafe`.
- **Solution**: Identify and upgrade third-party dependencies that rely on these internal APIs. If upgrading isn’t possible, use JVM arguments to open access to internal APIs (though this is a short-term workaround).

```
--add-opens java.base/sun.misc=ALL-UNNAMED
```

**c) Security Manager Deprecation (JEP 411)**

- **Issue**: The Security Manager has been deprecated.
- **Solution**: Replace it with modern security frameworks, like Spring Security, to handle sandboxing and access control.

```
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests().anyRequest().authenticated()
            .and().httpBasic();
    }
}
```

**d) TLS 1.0/1.1 Removal**

- **Issue**: Java 17 no longer supports weak TLS versions.
- **Solution**: Ensure your application supports only strong TLS protocols (TLS 1.2 and 1.3).

```
System.setProperty("https.protocols", "TLSv1.2,TLSv1.3");
```

# **2. Pre-Migration Dependency & Code Analysis**

**a) Use `jdeps` to Identify Internal API Usage**

- Run `jdeps` to scan for deprecated or removed APIs in your codebase:

```
jdeps --jdk-internals your-app.jar
```

This helps you catch potential breakages early.

**b) Update Dependencies & Build Tools**

- Ensure all dependencies are Java 17 compatible:
- **Spring Boot** → 3.x+ (Jakarta EE required).
- **Hibernate** → 6.x+.
- **Maven/Gradle** → Ensure you’re using the latest versions to support Java 17.

Update your `pom.xml`:

```
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
</properties>
```

Use the **Maven Enforcer Plugin** to enforce Java 17:

```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-enforcer-plugin</artifactId>
    <version>3.0.0</version>
    <executions>
        <execution>
            <id>enforce-java</id>
            <goals>
                <goal>enforce</goal>
            </goals>
            <configuration>
                <rules>
                    <requireJavaVersion>
                        <version>17</version>
                    </requireJavaVersion>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

# **3. ️Modernizing Code with Java 17 Features**

**a) `var` for Type Inference**

- Simplify local variable declarations by using `var` for type inference:

```
var list = List.of("A", "B", "C");
```

**b) Enhanced Switch Expressions (JEP 361)**

- Use switch expressions for more concise code that can return values:

```
int result = switch (day) {
    case MONDAY, FRIDAY -> 6;
    case TUESDAY -> 7;
    default -> 0;
};
```

**c) Use `record` for Immutable Data Classes (JEP 395)**

- Simplify DTO creation with `record` for immutable objects:

```
record User(String name, int age) {}
```

**d) Leverage Text Blocks for Multi-line Strings (JEP 378)**

- Handle multi-line strings easily with text blocks:

```
String json = """
    {
      "name": "Shivam",
      "age": 29
    }
    """;
```

**e) Sealed Classes for Controlled Inheritance (JEP 409)**

- Restrict inheritance with sealed classes, useful for creating fixed hierarchies:

```
public sealed class Vehicle permits Car, Truck {}

public final class Car extends Vehicle {}
public final class Truck extends Vehicle {}
```

**f) Pattern Matching for `instanceof` (JEP 394)**

- Simplify casting checks with pattern matching:

```
if (obj instanceof String s) {
    System.out.println(s.length()); // No explicit casting needed
}
```

# **4. Security Enhancements in Java 17**

**a) Enable TLS 1.3**

- Ensure secure connections by supporting the latest TLS protocol versions:

```
System.setProperty("https.protocols", "TLSv1.2,TLSv1.3");
```

**b) Deserialization Filtering (JEP 290)**

- Prevent deserialization attacks with global serialization filters:

```
ObjectInputFilter.Config.setSerialFilter("maxdepth=10;maxrefs=1000;");
```

# **5. Performance Optimizations**

**a) Use Shenandoah or Z Garbage Collector (Low-Latency GC)**

- Enable low-latency garbage collectors for high-performance applications:

```
java -XX:+UseShenandoahGC -Xmx4g -jar your-app.jar
```

**b) Use Java Flight Recorder (JFR) for Profiling**

- Profile your application with minimal overhead using JFR:

```
java -XX:StartFlightRecording=duration=120s,filename=app-recording.jfr -jar app.jar
```

**c) Optimize JVM for Production**

- Fine-tune JVM settings for production environments:

```
-XX:+UseZGC -Xms512m -Xmx4g -XX:+UseStringDeduplication
```

# **6. Advanced Java 17 Enhancements**

**a) Virtual Threads (Project Loom) for Concurrency**

- Use virtual threads for lightweight concurrency and scalability:

```
ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();
executor.submit(() -> System.out.println("Running in a virtual thread!"));
```

# **7. Optimizing for Docker & Kubernetes**

**a) Use a Minimal Java Runtime in Docker**

- Deploy your Java application in Docker using a minimal Java runtime:

```
FROM eclipse-temurin:17-jre
COPY target/app.jar /app.jar
CMD ["java", "-jar", "/app.jar"]
```

**b) Use `jlink` to Create a Custom Java Runtime**

- Create a custom Java runtime for reduced size and optimized performance:

```
jlink --module-path $JAVA_HOME/jmods --add-modules java.base,java.sql --output custom-runtime
```

# **8.️ Deployment & Risk Mitigation**

**a) Canary Release Strategy**

- Roll out Java 17 to a small user base initially to monitor performance and errors:

```
# Deploy to 5% of users
# Monitor performance and errors for 48 hours
```

**b) Rollback Plan**

- Always have a clear rollback strategy to revert to a stable version in case of issues:

```
git checkout release/java8
kubectl rollout undo deployment my-app
```

# **9. Optional: GraalVM for Faster Startup & Lower Memory**

- If startup time is critical, use **GraalVM** for native image compilation:

```
native-image -jar your-app.jar
```

# **10. Handling Edge Cases & Challenges**

While the upgrade from Java 8 to Java 17 can significantly improve performance and security, there are a few edge cases to consider:

**a) Legacy Applications with Heavy Dependency on Outdated Libraries**:

- **Problem**: Many older applications may rely on libraries or frameworks that haven’t been updated to support Java 17, such as libraries that are stuck on older Java EE standards or those using deprecated or removed APIs.
- **Solution**: Identify these libraries early in the process using `jdeps` or similar tools. You may need to either find modern alternatives or contribute to updating the libraries. In extreme cases, refactoring large chunks of code may be required.
- **Tip**: Before upgrading, perform a thorough audit of your third-party libraries and replace or upgrade them as necessary. Use `Maven` or `Gradle` to manage versions and keep track of deprecated libraries. Be mindful of any custom-built libraries that are not actively maintained.

**b) Large Codebase with High Coupling**:

- **Problem**: Some legacy applications have large codebases with tightly coupled components, which could make the transition more challenging. This is especially true for monolithic applications that heavily rely on internal APIs, or for applications that have been built with custom security models or configurations.
- **Solution**: Refactor parts of the code to reduce tight coupling before migrating to Java 17. Focus on modularizing the application, applying design principles like SOLID, and using dependency injection where possible to simplify the migration process.
- **Tip**: Apply the Strangler Fig pattern to slowly refactor parts of the system to be Java 17 compatible while still working within the legacy application. This allows a gradual migration with minimal disruption.

**c) Backward Compatibility in Multi-Version Environments**:

- **Problem**: In environments where multiple Java versions (such as Java 8 and Java 17) are running simultaneously due to specific use cases (e.g., some services still requiring Java 8), maintaining backward compatibility could be tricky.
- **Solution**: Use features like `jlink` to bundle only the necessary parts of the JDK in each version to reduce the compatibility burden. You may also need to implement dual-version compatibility during the migration phase, ensuring that both Java 8 and Java 17 versions of the application work side-by-side.
- **Tip**: For microservices architecture, use versioning for APIs and ensure services running on different Java versions don’t interfere with one another.

**d) Database Compatibility**:

- **Problem**: Some legacy systems may use outdated database drivers that aren’t compatible with Java 17.
- **Solution**: Update your JDBC drivers or any database interaction libraries to newer versions that are Java 17-compatible.
- **Tip**: Test the application with the new database driver in a staging environment to ensure that database connectivity and transaction behavior are functioning correctly.

**e) Build and CI/CD Pipeline Adjustments**:

- **Problem**: Legacy applications may rely on specific Java 8 features in the build tools, such as Maven/Gradle plugins or custom scripts that are not compatible with Java 17.
- **Solution**: Update build tools and pipeline scripts to support Java 17. This may involve upgrading Maven or Gradle plugins, updating CI/CD pipelines, and adjusting configurations for Java 17.
- **Tip**: During the migration process, ensure that the build and deployment pipelines are fully tested to work seamlessly with Java 17. Also, ensure that Docker containers and Kubernetes configurations are updated for Java 17 support.

# **Barclays Java Developer Interview**

## **1. Explain use cases of Kafka.**

Kafka is widely used for real-time data processing, event-driven architectures, and large-scale distributed systems. Below are some key use cases:

1. **Real-Time Data Streaming:**
- Kafka is used for processing continuous data streams, such as fraud detection in banking, IoT sensor data, and stock market analytics.
- **Example**: A bank can use Kafka to analyze credit card transactions in real time and detect fraud instantly.

**2. Log Aggregation & Monitoring:**

- Kafka centralizes logs from multiple microservices and sends them to monitoring tools like Elasticsearch, Logstash, and Kibana (ELK stack).
- **Example**: A company can collect server logs to track performance and troubleshoot failures.

**3. Event-Driven Microservices:**

- Kafka enables event-driven communication between microservices, ensuring they work independently but in sync.
- **Example**: In an e-commerce system, when a customer places an order, Kafka triggers inventory updates, payment processing, and shipping workflows.

**4. Messaging System (Pub-Sub):**

- Kafka replaces traditional message brokers (like RabbitMQ) for high-throughput, fault-tolerant, and scalable messaging.
- **Example**: A ride-sharing app can use Kafka to send real-time location updates to drivers and passengers.

**5. Big Data & Analytics Pipelines:**

- Kafka is often used as a data ingestion layer for big data frameworks like Apache Spark, Flink, or Hadoop.
- **Example**: A retail company can analyze customer purchases in real time and adjust promotions dynamically.

**6. Database Change Data Capture (CDC):**

- Kafka helps track and replicate database changes in real time across multiple systems.
- **Example:** A banking application syncing customer records across multiple databases without downtime.

**7. Data Replication & Synchronization:**

- Kafka is used to replicate data across distributed systems or multi-region deployments.
- **Example:** A global enterprise using Kafka to replicate user profiles and transactions across different data centers to ensure consistency.
- Tools like **Kafka MirrorMaker** help replicate data across clusters for fault tolerance and high availability.

**8. Streaming Video & Content Delivery:**

- Kafka powers video streaming platforms by handling real-time video encoding, buffering, and distribution.
- **Example:** A platform like Netflix uses Kafka to optimize video recommendations and streaming quality based on user interactions.

## **2. How many types of request and response are generated by Rest API? (Media Types)**

In REST APIs, request and response data are exchanged in different **media types**, which define how data is formatted and transmitted. The most commonly used media types are:

## **1. JSON (JavaScript Object Notation) — `application/json`**

- The most widely used media type in REST APIs.
- Lightweight, human-readable, and easy to parse.
- Used for data exchange between frontend and backend services.
- Example:

```
{
  "id": 101,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

- **Use Case:** Modern web applications, microservices, and mobile apps.

## **2. XML (Extensible Markup Language) — `application/xml`**

- Older format but still used in enterprise applications.
- Supports complex data structures and hierarchical relationships.
- Example:

```
<user>
    <id>101</id>
    <name>John Doe</name>
    <email>john.doe@example.com</email>
</user>
```

- **Use Case:** Legacy systems, SOAP-based web services, and data interchange between enterprises.

## **3. Form URL Encoded — `application/x-www-form-urlencoded`**

- Commonly used for submitting form data in web applications.
- Data is sent as key-value pairs in the request body.
- Example:

```
id=101&name=John+Doe&email=john.doe@example.com
```

- **Use Case:** HTML form submissions (like login forms) and simple API requests.

## **4. Multipart Form Data — `multipart/form-data`**

- Used when uploading files along with form data.
- Data is divided into multiple parts, each with its own content type.
- Example (Boundary-based format):

```
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="image.jpg"
Content-Type: image/jpeg

(binary data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

- **Use Case:** File uploads in web and mobile applications.

## **5. Plain Text — `text/plain`**

- Simple text-based data exchange.
- Example:

```
Hello, this is a plain text response.
```

- **Use Case:** Debugging responses, logging, and simple API outputs.

## **6. HTML — `text/html`**

- Used when REST APIs return HTML content (less common).
- Example:

```
<html>
  <body>
         <h1>Welcome to My API</h1>
  </body>
</html>
```

- **Use Case:** Web pages, email templates, or browser-based API responses.

## **7. CSV (Comma-Separated Values) — `text/csv`**

- Used to return tabular data in a lightweight format.
- Example:

```
id,name,email 101,John Doe,john.doe@example.com
```

- **Use Case:** Data export and bulk data processing.

## **8. YAML (Yet Another Markup Language) — `application/x-yaml`**

- Human-readable format, often used for configurations.
- Example:

```
id: 101 name: John Doe email: john.doe@example.com
```

- **Use Case:** Configuration files and API responses in DevOps applications.

## **3. In Hibernate, explain internal workings of lazy loading and eager loading?**

In Hibernate, **lazy loading** and **eager loading** control how associated entities are fetched from the database.

## **1. Lazy Loading (Default in Hibernate)**

- Hibernate **loads only the parent entity initially**, and the associated entities are loaded **on demand** when accessed.
- **Implementation:** Uses **proxy objects** (subclass of the entity) to delay database queries until the associated entity is accessed.
- **Advantage:** Improves performance by reducing unnecessary database queries.
- **Disadvantage:** Can cause `LazyInitializationException` if accessed outside the session.

## **Internal Working of Lazy Loading**

1. When an entity with a lazy-loaded association is fetched, Hibernate **does not** load the associated entities.
2. Instead, it creates a **proxy object** (a subclass of the entity with overridden methods).
3. When an associated entity is accessed for the first time, Hibernate triggers an additional SQL query to fetch it.
4. If the session is closed before accessing the lazy-loaded entity, a `LazyInitializationException` occurs.

**Example**:

**Entity Class with Lazy Loading (Default):**

```
@Entity
class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    @OneToMany(mappedBy = "employee", fetch = FetchType.LAZY) // Default is LAZY
    private List<Address> addresses;
}
```

**SQL Queries in Lazy Loading:**

```
-- When fetching the Employee:
SELECT * FROM Employee WHERE id = 1;

-- When accessing addresses for the first time:
SELECT * FROM Address WHERE employee_id = 1;
```

**LazyInitializationException Scenario**

```
Employee emp = session.get(Employee.class, 1); // Session open
session.close(); // Session closed
emp.getAddresses(); // Throws LazyInitializationException
```

## **2. Eager Loading**

- Hibernate loads the parent entity **along with** all associated entities **immediately** in a single SQL query (using `JOIN FETCH`).
- **Implementation:** Uses **JOIN queries** to fetch associated entities when the parent entity is loaded.
- **Advantage:** Prevents `LazyInitializationException` and reduces extra queries.
- **Disadvantage:** Can cause performance issues if unnecessary data is loaded.

## **Internal Working of Eager Loading**

1. When an entity with eager-loaded associations is fetched, Hibernate **immediately** loads both the entity and its related entities.
2. It executes a **single SQL query with a `JOIN FETCH`** to retrieve all necessary data at once.
3. No proxy objects are created, so all associated entities are fully initialized.

**Example:**

**Entity Class with Eager Loading:**

```
@Entity
class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    @OneToMany(mappedBy = "employee", fetch = FetchType.EAGER)
    private List<Address> addresses;
}
```

**SQL Query in Eager Loading:**

```
-- Hibernate executes a JOIN FETCH query:
SELECT e.*, a.*
FROM Employee e
LEFT JOIN Address a ON e.id = a.employee_id
WHERE e.id = 1;
```

**No `LazyInitializationException` Issue:**

```
Employee emp = session.get(Employee.class, 1); // Session open
session.close(); // Session closed
emp.getAddresses(); // Works fine (already loaded)
```

## **4. Suppose you’ve a Java class (with nothing else), now define some techniques that work based on eager loading vs lazy loading?**

**Techniques for Eager loading vs lazy loading** using pure **Java** concepts without Hibernate.

## **1. Techniques for Eager Loading in Java**

In **eager loading**, objects are fully initialized when created.

## **(i) Using Constructor Initialization**

- The object and its dependencies are **created immediately**.

**Example**:

```
class Employee {
    private Address address; // Dependency

    // Eagerly initializing the dependency in the constructor
    public Employee() {
        this.address = new Address("123 Street, City");
        System.out.println("Employee created with Address eagerly loaded.");
    }
    public Address getAddress() {
        return address;
    }
}
class Address {
    private String location;

    public Address(String location) {
        this.location = location;
        System.out.println("Address created.");
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee(); // Address is loaded immediately
        System.out.println(emp.getAddress().toString());
    }
}
```

**Pros:** No delay in data availability.**Cons:** Wastes memory if the dependency is not always needed.

## **(ii) Using Static Initialization (Singleton Pattern)**

- Object is created **at class loading time**, ensuring it is ready when needed.

**Example**:

```
class Singleton {
    private static final Singleton INSTANCE = new Singleton(); // Eager loading

    private Singleton() {
        System.out.println("Singleton instance created.");
    }
    public static Singleton getInstance() {
        return INSTANCE;
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        Singleton instance = Singleton.getInstance(); // Already loaded
    }
}
```

**Pros:** No synchronization issues, faster access.**Cons:** Wastes memory if never used.

## **(iii) Using Preloaded Cache**

- Data is preloaded **at startup** for quick access.

**Example**:

```
import java.util.*;

class Cache {
    private static final Map<Integer, String> data = new HashMap<>();
    static {
        // Preloading data (Eager loading)
        data.put(1, "John");
        data.put(2, "Jane");
        System.out.println("Cache preloaded.");
    }
    public static String getData(int id) {
        return data.get(id);
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        System.out.println(Cache.getData(1)); // No delay, already loaded
    }
}
```

**Pros:** Faster access.**Cons:** High memory usage if data is large.

## **2. Techniques for Lazy Loading in Java**

Lazy loading means **objects are created only when needed**.

## **(i) Using Lazy Initialization in Getters**

- The object is **not created until it is actually needed**.

**Example**:

```
class Employee {
    private Address address;

    public Address getAddress() {
        if (address == null) { // Load only when accessed
            address = new Address("123 Street, City");
            System.out.println("Address loaded lazily.");
        }
        return address;
    }
}
class Address {
    private String location;
    public Address(String location) {
        this.location = location;
        System.out.println("Address created.");
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee(); // No address loaded yet
        System.out.println("Employee created.");

        Address addr = emp.getAddress(); // Address loads only now
    }
}
```

**Pros:** Saves memory if object is never used.**Cons:** Slight delay when first accessed.

## **(ii) Using Lazy Singleton (Bill Pugh Singleton)**

- Instead of creating an instance at class loading time, we use a **nested static class**.

**Example**:

```
class LazySingleton {
    private LazySingleton() {
        System.out.println("LazySingleton instance created.");
    }

private static class Holder {
        private static final LazySingleton INSTANCE = new LazySingleton();
    }
    public static LazySingleton getInstance() {
        return Holder.INSTANCE; // Loads only when first called
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        LazySingleton instance = LazySingleton.getInstance(); // First access creates it
    }
}
```

**Pros:** Efficient and thread-safe.**Cons:** Delay in first access.

## **(iii) Using Supplier Functional Interface (Java 8)**

- Java 8 introduced `Supplier<T>`, which is a great way to implement **lazy loading**.

**Example**:

```
import java.util.function.Supplier;

class Employee {
    private Supplier<Address> address = () -> loadAddress();
    private Address loadAddress() {
        System.out.println("Address loaded lazily.");
        return new Address("123 Street, City");
    }
    public Address getAddress() {
        return address.get();
    }
}
class Address {
    private String location;

    public Address(String location) {
        this.location = location;
        System.out.println("Address created.");
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee(); // No address loaded yet
        System.out.println("Employee created.");

        Address addr = emp.getAddress(); // Address loads only now
    }
}
```

**Pros:** Clean and modern implementation.**Cons:** Slightly harder to debug for beginners.

## **(iv) Using Proxy Pattern for Lazy Loading**

- Uses a **dummy object** that loads the real object **only when needed**.

**Example**:

```
interface Data {
    void load();
}

class RealData implements Data {
    public RealData() {
        System.out.println("RealData loaded.");
    }
    public void load() {
        System.out.println("Using RealData.");
    }
}
class DataProxy implements Data {
    private RealData realData;
    public void load() {
        if (realData == null) {
            realData = new RealData(); // Load only on first call
        }
        realData.load();
    }
}
// Usage
public class Main {
    public static void main(String[] args) {
        Data data = new DataProxy(); // No real object created yet
        System.out.println("Proxy created.");

        data.load(); // RealData loads now
    }
}
```

**Pros:** Useful for large objects like images, files, or database connections.**Cons:** Adds complexity.

**5. What are the differences between load() and get()?**

![](https://d0a34zyak3rj61.archive.ph/f7JBx/d653a4c6ee190073275d54ab00292b9c34da2b03.webp)

## **6. What are the advantages of JPA?**

JPA is a specification for ORM (Object-Relational Mapping) in Java, making database interactions easier by abstracting SQL complexities. It is commonly used with Hibernate, EclipseLink, or OpenJPA.

## **1. Reduces Boilerplate Code**

- No need for JDBC code like `ResultSet`, `PreparedStatement`, or manually mapping database rows to objects.
- CRUD operations become simpler with `EntityManager` or `Repository`.

**Example Without JPA (JDBC Approach)**

```
Connection con = DriverManager.getConnection(url, user, password);
PreparedStatement ps = con.prepareStatement("SELECT * FROM Employee WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
if (rs.next()) {
    Employee emp = new Employee();
    emp.setId(rs.getInt("id"));
    emp.setName(rs.getString("name"));
}
```

- Manually handling SQL, result sets, and connections.

**With JPA (Hibernate Implementation)**

```
Employee emp = entityManager.find(Employee.class, 101);
```

- **JPA reduces boilerplate code** and handles database interactions internally.

## **2. Database Independence (Portable Code)**

- Works with **MySQL, PostgreSQL, Oracle, SQL Server**, etc., just by changing configuration.
- No need to write **database-specific SQL**.

**Example**

```
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

- Changing the database: Just update the configuration — no need to change code.

## **3. Supports Object-Oriented Features**

- Maps Java objects (POJOs) to database tables.
- Supports relationships (`@OneToMany`, `@ManyToOne`, `@OneToOne`, etc.).
- Supports inheritance (`@MappedSuperclass`, `@Inheritance`).

**Example**

```
@Entity
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
}
```

- **JPA automatically maps the class to the table.**

## **4. Built-in Caching for Performance Optimization**

- Uses **First-Level Cache (Session Cache)** automatically.
- **Second-Level Cache** (via Ehcache, Redis, etc.) can be enabled to avoid redundant database queries.

**Example**

```
Employee emp1 = entityManager.find(Employee.class, 101); // SQL query executes
Employee emp2 = entityManager.find(Employee.class, 101); // No query (cached result)
```

- **JPA avoids unnecessary database hits.**

## **5. Supports Transactions & Concurrency**

- Manages database transactions (`@Transactional` in Spring).
- Provides **optimistic (`@Version`) and pessimistic locking** to handle concurrent updates.

**Example (Optimistic Locking)**

```
@Version
private int version;
```

- **Prevents conflicts when multiple users update the same record.**

## **6. Querying with JPQL (Simplified Queries)**

- Uses **JPQL (Java Persistence Query Language)** instead of SQL.
- Works across different databases without modification.

**Example**

```
Query query = entityManager.createQuery("SELECT e FROM Employee e WHERE e.name = :name");
query.setParameter("name", "John");
List<Employee> employees = query.getResultList();
```

- **No database-specific SQL needed.**

## **7. Supports Pagination and Sorting**

- Built-in support for **pagination and sorting** in Spring Data JPA.

**Example (Spring Data JPA)**

```
Page<Employee> employees = employeeRepository.findAll(PageRequest.of(0, 10, Sort.by("name")));
```

- **Efficiently fetches data in chunks.**

## **8. Works Well with Spring Boot**

- Integrates seamlessly with **Spring Boot** using `spring-boot-starter-data-jpa`.
- Auto-configures the database connection, making setup easy.

**Example (Spring Boot Configuration)**

```
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.jpa.hibernate.ddl-auto=update
```

- **Minimal configuration required.**

## **9. Entity Lifecycle Callbacks**

- Provides lifecycle methods (`@PrePersist`, `@PostPersist`, `@PreUpdate`, etc.).
- Allows automatic actions like logging or validation before persisting data.

**Example**

```
@PrePersist
public void beforeSave() {
    this.createdAt = LocalDateTime.now();
}
```

- **Automatic timestamps before saving records.**

## **10. Works with NoSQL Databases (MongoDB, Cassandra, etc.)**

- **Spring Data JPA** supports NoSQL databases like **MongoDB, Redis, and Cassandra**.

**Example (Spring Data MongoDB Repository)**

```
public interface EmployeeRepository extends MongoRepository<Employee, String> {}
```

- **JPA is not limited to relational databases.**

**7. Why do we use microservices architecture instead of monolithic architecture?**

![](https://d0a34zyak3rj61.archive.ph/f7JBx/7202f703917b71a6f79671d89022c34eb8b3c8da.webp)

## **8. Explain microservices design pattern?**

Below are the microservice design patterns:

## **1. API Gateway Pattern**

- Provides a single entry point for all client requests and handles routing to appropriate services.
- **Benefit**: Simplifies client interactions and handles cross-cutting concerns (authentication, logging).

## **2. Service Discovery Pattern**

- Enables services to discover and communicate with each other dynamically.
- **Benefit**: Supports scaling and service location management in distributed environments.

## **3. Circuit Breaker Pattern**

- Prevents repeated requests to failing services, avoiding cascading failures.
- **Benefit**: Helps in graceful degradation and recovery from failures.

## **4. Saga Pattern**

- Manages distributed transactions across multiple services with compensating actions.
- **Benefit**: Ensures data consistency without relying on a single database.

## **5. Event Sourcing Pattern**

- Stores a sequence of events instead of the current state, allowing state reconstruction.
- **Benefit**: Provides an audit trail and supports event-driven systems.

## **6. CQRS Pattern**

- Separates reading (queries) and writing (commands) operations to optimize both.
- **Benefit**: Allows independent scaling of read and write operations and better performance.

## **7. Strangler Fig Pattern**

- Gradually replaces parts of a monolithic system with microservices.
- **Benefit**: Enables incremental migration without a full system rewrite.

## **8. Database per Service Pattern**

- Each service owns its database, reducing dependencies.
- **Benefit**: Ensures service autonomy and scalability, with the option to use different database types.

## **9. Sidecar Pattern**

- Deploys a helper service alongside a main service to handle cross-cutting concerns.
- **Benefit**: Offloads tasks like logging or monitoring, keeping the main service focused.

## **10. Bulkhead Pattern**

- Isolates failures to prevent them from affecting the entire system.
- **Benefit**: Increases resilience by containing service failures.

These patterns solve specific problems in microservice architectures, making systems more scalable, resilient, and easier to maintain.

**9. What are the differences between SpringBoot vs Spring framework?**

![](https://d0a34zyak3rj61.archive.ph/f7JBx/8fa8ec053e2932d49cf125e5cd398432caa60585.webp)

## **10. How do you create SpringBoot application from command line interface?**

To create a Spring Boot application from the command line, you can use **Spring Initializr** or **Spring CLI**.

## **1. Using Spring Initializr (Command Line):**

1. **Open your terminal** (CLI).
2. **Use the `curl` command** to generate a Spring Boot project. For example:

```
curl https://start.spring.io/starter.zip -d dependencies=web,jpa,h2 -d name=demo -d packageName=com.example.demo -d javaVersion=11 -o demo.zip
```

**Explanation:**

- `dependencies=web,jpa,h2` specifies the dependencies like Spring Web, JPA, and H2 database.
- `name=demo` specifies the name of the project.
- `packageName=com.example.demo` specifies the package name.
- `javaVersion=11` specifies the Java version.
- `o demo.zip` specifies the output file name for the zip file.

**3. Extract the downloaded zip file**:

```
unzip demo.zip -d demo cd demo
```

**4. Build and run the Spring Boot application** using Maven or Gradle:

For Maven:

```
./mvnw spring-boot:run
```

For Gradle:

```
./gradlew bootRun
```

## **2. Using Spring CLI**

If you have **Spring CLI** installed, you can create a Spring Boot application using the following commands:

1. **Install Spring CLI** (if you haven’t already):
- On macOS with Homebrew:

```
brew install springboot
```

- On other systems, you can download the Spring CLI from [Spring.IO.](https://archive.ph/o/f7JBx/https://spring.io/tools)

**2. Create a Spring Boot application using `spring init`**:

For example:

```
spring init --dependencies=web,jpa,h2 demo
```

This will create a new Spring Boot project in the `demo` directory with dependencies for Spring Web, JPA, and H2 database.

**3. Navigate into the project folder**:

```
cd demo
```

**4. Run the application**:

For Maven:

```
./mvnw spring-boot:run
```

For Gradle:

```
./gradlew bootRun
```

## **11. How do spring boot application initializes?**

The initialization of a Spring Boot application follows these steps:

1. **Entry Point**: The application starts with a `main()` method in a class annotated with `@SpringBootApplication`.
2. **SpringApplication.run()**: This method initializes the Spring context, applies auto-configuration, and starts the embedded server (if it’s a web app).
3. **ApplicationContext Initialization**: The Spring IoC container is created, and beans are loaded based on component scanning and configuration classes.
4. **Auto-Configuration**: Spring Boot automatically configures beans and components based on the application’s dependencies and environment settings.
5. **Bean Initialization**: Beans are instantiated and injected into other beans as needed, with lifecycle methods like `@PostConstruct` being invoked.
6. **Embedded Web Server (if Web App)**: For web applications, the embedded server (Tomcat, Jetty, etc.) is started to serve HTTP requests.
7. **CommandLineRunner / ApplicationRunner** (Optional): If defined, these interfaces run custom logic after the application context is initialized.

Once all these steps are completed, the application is fully initialized and ready to serve requests or execute background tasks.

## **12. Explain Qualifier annotation.**

The `@Qualifier` annotation in Spring is used to resolve ambiguity when multiple beans of the same type are present in the application context.

It helps Spring to choose which bean to inject when there are multiple candidates for autowiring.

**Purpose**:

It’s used along with `@Autowired` to specify which bean should be injected into a field or method when multiple beans of the same type exist.

**Usage**:

You define the `@Qualifier` annotation with the name of the bean you want to inject. This ensures that the correct bean is injected instead of the default behavior, where Spring would throw an exception due to ambiguity.

**Example**:

```
@Component
public class Employee {
    private Address address;

    @Autowired
    @Qualifier("homeAddress") // Specifies which bean to inject
    public void setAddress(Address address) {
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

**When to Use**:

You would use `@Qualifier` when you have multiple beans of the same type (e.g., multiple `Address` beans) and need to specify which one to inject.

> This question was also asked to me in my Capgemini Interview. So, this is an important question.
> 

## **13. Write a program to implement comparator interface in Java.**

To implement the `Comparator` interface in Java, you need to define the comparison logic for the objects of a class. The `Comparator` interface has a single method, `compare()`, which compares two objects.

## **Program:**

```
import java.util.*;

// Employee class
class Employee {
    String name;
    int age;
    // Constructor
    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }
    // Getter methods
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
// Comparator implementation to compare by age
class EmployeeAgeComparator implements Comparator<Employee> {
    @Override
    public int compare(Employee e1, Employee e2) {
        // Compare based on age
        return Integer.compare(e1.getAge(), e2.getAge());
    }
}
// Comparator implementation to compare by name
class EmployeeNameComparator implements Comparator<Employee> {
    @Override
    public int compare(Employee e1, Employee e2) {
        // Compare based on name
        return e1.getName().compareTo(e2.getName());
    }
}
public class Main {
    public static void main(String[] args) {
        // Creating a list of Employee objects
        List<Employee> employees = new ArrayList<>();
        employees.add(new Employee("John", 28));
        employees.add(new Employee("Jane", 22));
        employees.add(new Employee("Alex", 32));

        // Sorting employees by age using EmployeeAgeComparator
        System.out.println("Employees sorted by age:");
        Collections.sort(employees, new EmployeeAgeComparator());
        for (Employee emp : employees) {
            System.out.println(emp);
        }

        // Sorting employees by name using EmployeeNameComparator
        System.out.println("\nEmployees sorted by name:");
        Collections.sort(employees, new EmployeeNameComparator());
        for (Employee emp : employees) {
            System.out.println(emp);
        }
    }
}
```

## **Breakdown:**

1. **Employee Class**: This class represents an employee with `name` and `age` fields.

**2. Comparator Implementations**:

- `EmployeeAgeComparator`: Compares employees based on their age.
- `EmployeeNameComparator`: Compares employees based on their name.

**3. Sorting**:

- `Collections.sort()` is used to sort the list of employees based on the comparator.
- The list is first sorted by age, and then by name.

## **Output:**

```
Employees sorted by age:
Employee{name='Jane', age=22}
Employee{name='John', age=28}
Employee{name='Alex', age=32}

Employees sorted by name:
Employee{name='Alex', age=32}
Employee{name='Jane', age=22}
Employee{name='John', age=28}
```

# **Final Thoughts**

Since this was a round 1 of 3, this was a short interview which was easy and difficult at the same time, depending on your understanding of the concepts.

# **KPMG Java Developer Interview**

## **1. Abstraction**

Abstraction is the process of hiding the internal workings of an object and only exposing the necessary functionalities. It simplifies interaction with complex systems by reducing complexity and focusing only on essential details. Abstraction is usually implemented using abstract classes and interfaces.

**Example:**

```
abstract class Vehicle {
    abstract void start();

    void stop() {
        System.out.println("Vehicle is stopping");
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car is starting!");
    }
}
public class Main {
    public static void main(String[] args) {
        Vehicle vehicle = new Car();
        vehicle.start();  // Output: Car is starting!
        vehicle.stop();   // Output: Vehicle is stopping
    }
}
```

In this example, the `Vehicle` class is abstract, and its abstract method `start()` must be implemented by the `Car` class. Abstraction allows for hiding unnecessary implementation details and providing a simple interface for interaction.

## **2. Encapsulation**

Encapsulation refers to bundling the data (fields) and methods that manipulate the data into a single unit (class). It also involves restricting access to some of an object’s internal state to safeguard it from external interference.

**Example:**

```
class BankAccount {
    private double balance;

public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    public double getBalance() {
        return balance;
    }
}
public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.deposit(1000);
        System.out.println("Balance: " + account.getBalance());
    }
}
```

Here, the `balance` field is private, making it inaccessible directly outside the `BankAccount` class. Access to it is controlled via the `deposit()` and `getBalance()` methods.

## **3. Inheritance**

Inheritance allows a new class to inherit the fields and methods from an existing class, establishing an “is-a” relationship. This promotes code reuse and simplifies the creation of hierarchical relationships.

**Example:**

```
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}
public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        animal.makeSound();  // Output: Animal makes a sound
        Dog dog = new Dog();
        dog.makeSound();  // Output: Dog barks
    }
}
```

In this example, `Dog` inherits from `Animal` and overrides its `makeSound()` method. This demonstrates how inheritance helps reduce code duplication and build class hierarchies.

## **4. Polymorphism**

Polymorphism allows objects of different types to be treated as instances of a common superclass. It promotes flexibility and enables you to write more generic code. There are two types of polymorphism: **method overloading** (compile-time polymorphism) and **method overriding** (runtime polymorphism).

**Example:**

```
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting");
    }

    void start(String key) {
        System.out.println("Vehicle is starting with key: " + key);
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car is starting");
    }
    void start(String key, int speed) {
        System.out.println("Car is starting with key: " + key + " at speed: " + speed);
    }
}
public class Main {
    public static void main(String[] args) {
        Vehicle vehicle = new Vehicle();
        vehicle.start();                    // Output: Vehicle is starting
        vehicle.start("Remote");            // Output: Vehicle is starting with key: Remote
        Vehicle myVehicle = new Car();
        myVehicle.start();                  // Output: Car is starting (Runtime Polymorphism)
        Car myCar = new Car();
        myCar.start("Remote", 80);          // Output: Car is starting with key: Remote at speed: 80
    }
}
```

- **Method Overloading** (Compile-Time Polymorphism): Multiple `start()` methods with different parameter lists.
- **Method Overriding** (Runtime Polymorphism): `Car` overrides `Vehicle`'s `start()` method, which is called dynamically at runtime based on the actual object type.

## **5. Composition**

Composition represents a “has-a” relationship, where one object contains another object as part of itself. The contained object cannot exist independently outside of the containing object.

**Example:**

```
class Engine {
    void start() {
        System.out.println("Engine is starting");
    }
}

class Car {
    private Engine engine;

    public Car() {
        engine = new Engine();
    }
    void startCar() {
        engine.start();
        System.out.println("Car is starting");
    }
}
public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.startCar();  // Output: Engine is starting, Car is starting
    }
}
```

Here, `Car` has an `Engine`, and the `Engine` cannot exist independently of the `Car` object, showing a strong **has-a** relationship.

## **6. Aggregation**

Aggregation represents a “whole-part” relationship but allows the “part” to exist independently of the “whole.” The contained objects can exist separately and are not tightly coupled with the container.

**Example:**

```
class Wheel {
    void rotate() {
        System.out.println("Wheel is rotating");
    }
}

class Car {
    private Wheel wheel;
    public Car(Wheel wheel) {
        this.wheel = wheel;
    }
    void move() {
        wheel.rotate();
        System.out.println("Car is moving");
    }
}
public class Main {
    public static void main(String[] args) {
        Wheel wheel = new Wheel();
        Car car = new Car(wheel);
        car.move();  // Output: Wheel is rotating, Car is moving
    }
}
```

The `Wheel` object can exist independently of the `Car` object, demonstrating a looser "whole-part" relationship than composition.

## **7. Association**

Association represents any relationship between two objects where each object can exist independently. It is the most general form of relationship.

**Example:**

```
import java.util.ArrayList;
import java.util.List;

class Student {
    private String name;

    public Student(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
}
class School {
    private List<Student> students;
    public School() {
        students = new ArrayList<>();
    }
    public void addStudent(Student student) {
        students.add(student);
    }
    public void showStudents() {
        for (Student student : students) {
            System.out.println(student.getName());
        }
    }
}
public class Main {
    public static void main(String[] args) {
        School school = new School();
        school.addStudent(new Student("Alice"));
        school.addStudent(new Student("Bob"));
        school.showStudents();  // Output: Alice, Bob
    }
}
```

In this example, **School** has an association with **Student**, but both objects can exist independently. The association here is a **one-to-many** relationship.

## **2. What is exception handling and why do we need it?**

Exception handling is a mechanism in Java that allows us to handle runtime errors gracefully, ensuring that the program doesn’t crash unexpectedly.

It helps in identifying, catching, and managing errors so that we can provide a proper response instead of abrupt termination.

## **Need:**

1. **Prevent Program Crashes** — Without it, an unhandled exception (like division by zero) would cause the program to terminate unexpectedly. Exception handling ensures the program either recovers or exits cleanly.
2. **Improve Code Readability & Debugging** — It separates error-handling logic from the main code, making it cleaner and easier to maintain. Plus, exceptions provide stack traces, which help in debugging.
3. **Handle Unexpected Scenarios** — Issues like invalid user input, file not found, or network failures are unpredictable. Exception handling allows us to respond dynamically instead of letting the program fail.
4. **Ensure Application Stability** — Proper exception handling prevents security vulnerabilities (e.g., leaking system details through raw error messages) and ensures the application continues functioning as expected.

## **Example:**

```
public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // This will cause an ArithmeticException
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed.");
        } finally {
            System.out.println("Execution completed.");
        }
    }
}
```

**Output:**

```
Error: Division by zero is not allowed.
Execution completed.
```

- The `try` block contains risky code.
- The `catch` block handles the exception.
- The `finally` block ensures cleanup, executing whether an exception occurs or not.

## **Types:**

Java has two main types of exceptions:

1. **Checked Exceptions (Compile-time exceptions):**
- These are checked at compile time and must be handled using `try-catch` or declared with `throws`.
- Examples: `IOException`, `SQLException`.
- Example:

```
import java.io.*;

public class CheckedExceptionExample {
    public static void main(String[] args) {
        try {
            FileReader file = new FileReader("nonexistent.txt"); // FileNotFoundException
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }
    }
}
```

**2. Unchecked Exceptions (Runtime exceptions):**

- These occur at runtime and are not checked by the compiler.
- Examples: `NullPointerException`, `ArrayIndexOutOfBoundsException`.
- Example:

```
public class UncheckedExceptionExample {
    public static void main(String[] args) {
        String str = null;
        System.out.println(str.length()); // NullPointerException
    }
}
```

**3. Errors:**

- These indicate serious system failures (like `OutOfMemoryError`) and should not be caught in most cases.

## **3. Explain Internal working of HashMap. Also, explain features and use cases of HashMap.**

I have answered this in detail in my HashMap article. I recommend reading this, as HashMap is a very important topic (especially for Junior roles) and it’s very important to understand it completely.

[**HashMap: Deep Dive and Interview QuestionsDive Into HashMaps with Interview Prep**medium.com](https://archive.ph/o/0hnBY/https://medium.com/coding-odyssey/hashmap-deep-dive-and-interview-questions-6cf251baf61a)

## **4. If we want to create our own HashMap class, can we do it without extending the HashMap class or implementing the Map interface? What do you need to do?**

It is possible to create your own `HashMap` class without extending the `HashMap` class or implementing the `Map` interface.

You would just need to implement the basic functionality of a `HashMap`, like hashing, handling collisions, resizing, and storing key-value pairs manually.

## **Steps:**

1. **Define the Data Structure:**
- You need an underlying array to store the key-value pairs. This array will hold *buckets*, and each bucket can be a linked list (or another structure) to handle collisions.

**2. Handle Hashing:**

- Compute the hash value of the keys by calling the `hashCode()` method of the key and mapping that value to an index in the array. You must handle the possibility of collisions when multiple keys hash to the same index.

**3. Handle Collisions:**

- When two keys hash to the same index, you can store them in the same bucket (using a linked list or a balanced tree structure for performance if needed). This ensures that multiple keys can be stored in the same index.

**4. Resize the Map:**

- Just like `HashMap`, you’ll need to resize your data structure when the number of entries exceeds a threshold. Typically, this involves creating a larger array (doubling the size) and rehashing all the entries into the new array.

**5. Implement Basic Methods:**

- You’ll need to implement basic methods such as `put()`, `get()`, `remove()`, `size()`, and `containsKey()` to interact with the map.

## **Example:**

```
class MyHashMap<K, V> {

    private Entry<K, V>[] table;
    private int size;
    private static final int INITIAL_CAPACITY = 16;
    private static final float LOAD_FACTOR = 0.75f;

    public MyHashMap() {
        table = new Entry[INITIAL_CAPACITY];
        size = 0;
    }

    private static class Entry<K, V> {
        K key;
        V value;
        Entry<K, V> next;

        Entry(K key, V value) {
            this.key = key;
            this.value = value;
            this.next = null;
        }
    }

    private int hash(K key) {
        return key == null ? 0 : key.hashCode() % table.length;
    }

    public void put(K key, V value) {
        int index = hash(key);
        Entry<K, V> newEntry = new Entry<>(key, value);

        if (table[index] == null) {
            table[index] = newEntry;
        } else {
            Entry<K, V> current = table[index];
            while (current != null) {
                if (current.key.equals(key)) {
                    current.value = value;  // Update existing value
                    return;
                }
                current = current.next;
            }
            newEntry.next = table[index];  // Handle collision by chaining
            table[index] = newEntry;
        }

        size++;
        if (size > table.length * LOAD_FACTOR) {
            resize();
        }
    }

    public V get(K key) {
        int index = hash(key);
        Entry<K, V> current = table[index];
        while (current != null) {
            if (current.key.equals(key)) {
                return current.value;
            }
            current = current.next;
        }
        return null;  // Key not found
    }

    private void resize() {
        Entry<K, V>[] oldTable = table;
        table = new Entry[table.length * 2];
        size = 0;

        // Rehash all entries
        for (Entry<K, V> entry : oldTable) {
            while (entry != null) {
                put(entry.key, entry.value);
                entry = entry.next;
            }
        }
    }

    public int size() {
        return size;
    }

    public boolean remove(K key) {
        int index = hash(key);
        Entry<K, V> current = table[index];
        Entry<K, V> prev = null;

        while (current != null) {
            if (current.key.equals(key)) {
                if (prev == null) {
                    table[index] = current.next;
                } else {
                    prev.next = current.next;
                }
                size--;
                return true;
            }
            prev = current;
            current = current.next;
        }
        return false;  // Key not found
    }
}
```

## **Components:**

1. **`Entry` class**: This is the class that holds each key-value pair. If a collision occurs, the `next` pointer of the entry will point to the next entry in the same bucket.
2. **`hash()` method**: This computes the hash code and maps it to an index in the table using the modulus operation.
3. **`put()` method**: This is used to insert key-value pairs. If the key already exists, it updates the value. If there's a collision, the new entry is added to the linked list at the corresponding bucket.
4. **`get()` method**: This retrieves the value for a given key. If the key exists, it returns the value; otherwise, it returns `null`.
5. **`resize()` method**: This is triggered when the size of the map exceeds the load factor multiplied by the current table size. It doubles the array size and rehashes all existing entries.
6. **`remove()` method**: This method removes a key-value pair from the map.

## **5. What is static keyword?**

The `static` keyword in Java is mainly used for memory management. It is used to indicate that a particular variable, method, or inner class belongs to the class itself, rather than to instances of the class. This means you don't need to create an object of the class to access the static member.

The users can apply static keywords with variables, methods, blocks, and nested classes.

## **1. Static Variables:**

- A `static` variable is shared across all instances of a class. Rather than each object having its own copy, all instances share the same variable.
- Static variables are initialized only once when the class is loaded into memory.
- You can access a static variable directly using the class name or an instance of the class (although it’s not recommended to access it through an instance).

**Example:**

```
class Counter {
    static int count = 0; // Static variable

    public void increment() {
        count++; // Increment static variable
    }
}
```

Here, the `count` variable will be shared by all instances of `Counter`. If one object increments it, the change is reflected across all instances.

## **2. Static Methods:**

- A `static` method belongs to the class, not the instance, so it can be called without creating an object.
- Static methods can access static variables and call other static methods, but they cannot access instance variables or methods (non-static members) directly.

**Example:**

```
class MathUtility {
    static int square(int x) {
        return x * x; // Static method
    }
}
```

You can call `MathUtility.square(5)` directly without creating an object of `MathUtility`.

## **3. Static Blocks:**

- A `static` block is a block of code that runs only once when the class is first loaded into memory, making it useful for initializing static variables.
- It is executed before the constructor when the class is loaded.

**Example:**

```
class MyClass {
    static {
        System.out.println("Class loaded!");
    }
}
```

This block will execute when the class is loaded for the first time.

## **4. Static Classes (Nested Classes):**

- A static inner class is an inner class that can be instantiated without an instance of the outer class. It can only access the static members of the outer class.

**Example:**

```
class OuterClass {
    static class InnerClass {
        void display() {
            System.out.println("Inside static inner class");
        }
    }
}

OuterClass.InnerClass obj = new OuterClass.InnerClass();
obj.display();  // No need to create an instance of OuterClass
```

## **Advantages:**

- **Memory Efficiency**: Static members are shared, reducing memory consumption when the same data is used across multiple instances.
- **Class Level**: Static members belong to the class rather than the objects, making them accessible even if no objects are created.
- **Global Access**: Static methods can be used for utility functions, like `Math.sqrt()` or `System.out.println()`.

## **Use Case:**

- When you need a value or method that is common to all objects of the class (e.g., constants, utility methods).
- For creating singleton patterns, static blocks for initialization, or shared data among all instances of the class.

## **6. Explain Singleton class and how to create a Singleton class.**

**A Singleton class** is a design pattern in software development that ensures a class has only one instance and provides a global point of access to that instance.

This pattern is useful when you want to control access to shared resources, like a configuration manager, logging service, or database connection.

## **Characteristics:**

- **Single Instance:** Only one instance of the class is created throughout the application’s lifecycle.
- **Global Access:** The single instance is globally accessible, preventing the creation of other instances.
- **Lazy Initialization:** The instance is created only when it’s first needed, ensuring efficient use of resources.
- **Thread Safety:** In a multi-threaded environment, the singleton should be designed in a thread-safe manner to prevent the creation of multiple instances.

## **Steps to Create a Singleton Class:**

1. **Private Constructor:**
- The constructor should be private so that no other class can instantiate the singleton class using the `new` keyword. This ensures that the class can only be instantiated within itself.

```
private Singleton() {
     // Private constructor to prevent instantiation
}
```

**2. Static Instance:**

- Create a static field to hold the single instance of the class. This instance is the only one that will exist throughout the application’s lifecycle.

```
private static Singleton instance;
```

**3. Global Access Method:**

- Provide a static method to retrieve the instance of the class. This method checks if the instance already exists. If it does, it returns the existing instance; otherwise, it creates a new one.

```
public static Singleton getInstance() {

     if (instance == null) {
         instance = new Singleton();  // Lazy initialization
     }
     return instance;
}
```

## **Complete Example:**

```
class Singleton {
    // Step 1: Private constructor
    private Singleton() {}

    // Step 2: Static instance
    private static Singleton instance;

    // Step 3: Global access method
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();  // Lazy initialization
        }
        return instance;
    }
}
```

## **Types of Singleton Implementation:**

**1. Eager Initialization:**

- The instance of the class is created as soon as the class is loaded into memory.
- **Thread-Safe**: This approach is thread-safe because the class loader ensures that the instance is created only once when the class is loaded.

```
class Singleton {
    // Create an instance of Singleton at the time of class loading
    private static final Singleton instance = new Singleton();

    // Private constructor
    private Singleton() {}

    // Public method to access the instance
    public static Singleton getInstance() {
        return instance;
    }
}
```

**2. Lazy Initialization:**

- The instance is created only when the `getInstance()` method is called for the first time.
- **Not thread-safe**: Multiple threads calling this method simultaneously might create multiple instances, so this approach isn’t safe in multi-threaded environments.

```
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();  // Lazy initialization
        }
        return instance;
    }
}
```

**3. Thread-Safe Lazy Initialization:**

- This version ensures thread-safety by synchronizing the `getInstance()` method. However, it introduces performance overhead because synchronization is performed on every method call.

```
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();  // Lazy initialization
        }
        return instance;
    }
}
```

**4. Double-Checked Locking:**

- A more efficient thread-safe solution where synchronization is only performed when the instance is `null`.
- **The `volatile` keyword** ensures that the instance is correctly initialized in a multi-threaded environment, preventing issues with stale references.

```
class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();  // Lazy initialization
                }
            }
        }
        return instance;
    }
}
```

**5. Bill Pugh Singleton Design:**

- This is the most efficient and thread-safe way to implement the Singleton pattern. The instance is created only when the inner static class is loaded, and it leverages the class loader mechanism to ensure thread safety without synchronization.

```
class Singleton {
    private Singleton() {}

    // Inner static class responsible for holding the Singleton instance
    private static class SingletonHelper {
        // The instance is created when the class is loaded
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}
```

6. **Enum Singleton:**

- This approach uses the `enum` type to create the Singleton. It is the simplest and most robust solution for creating a Singleton class in Java, ensuring thread-safety and preventing issues related to serialization or reflection.

```
public enum Singleton {
     INSTANCE;      // Example method

     public void doSomething() {
         System.out.println("Singleton is doing something.");
     }
 }

// Usage
Singleton singleton = Singleton.INSTANCE;
singleton.doSomething();
```

## **Use case:**

- **Shared resources** like database connections or configuration settings.
- **Logging mechanisms**, where only one instance of a logger is needed throughout the application.
- **Thread pools** where you want to manage and control the number of threads used by the application.

I have already written an article on the same, you can go through it as well.

[**Is Your Code Lacking Leadership?See how Singleton brings clarity and control to your code.**medium.com](https://archive.ph/o/0hnBY/https://medium.com/java-and-beyond/is-your-code-lacking-leadership-14215d3fc215)

## **7. What is an Immutable class and how to create it?**

This is the best article you’ll find on Immutable classes., specifically written for this question. I highly recommend it:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/0hnBY/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

## **8. How is the string immutable?**

In Java, a `String` is immutable, meaning once a `String` object is created, its state (the sequence of characters it holds) cannot be changed.

This immutability is a key characteristic of the `String` class and is achieved through several design decisions in Java.

## **How String is Immutable:**

1. **Final Class:** The `String` class is declared as `final`, meaning it cannot be subclassed. This is crucial because subclassing could potentially override methods that modify the state of the string, undermining its immutability.

```
public final class String {
     // Fields and methods here
}
```

**2. Private and Final Character Array:** The `String` class stores its characters in a private `final` array of `char`. Since the array is marked as `final`, it cannot be reassigned to another array, and because it's private, other classes cannot directly modify it.

```
private final char[] value;
```

**3. No Setter Methods:** The `String` class does not provide any setter methods to modify the contents of a string. Once a `String` object is created, you cannot change the characters inside it directly. If you try to "modify" a string, you’re essentially creating a new `String` object with the modified value.

**4. String Pool:** Strings are stored in a special area of memory known as the **String Pool**. When you create a string literal (e.g., `"Hello"`), Java first checks if that string already exists in the pool. If it does, it returns a reference to the existing string rather than creating a new object. This optimizes memory usage by ensuring that identical string literals are stored only once.

**5. Methods that Appear to Modify Strings:** Even though methods like `concat()`, `substring()`, `replace()`, etc., might appear to modify a string, they don’t change the original object. Instead, they return a new string instance with the desired modification. The original string remains unchanged.

**Example:**

```
String str = "Hello";
str = str.concat(" World");  // A new string object is created
```

In this example, `"Hello"` remains unchanged, and a new string `"Hello World"` is created and assigned to `str`.

**6. Thread Safety:** Since strings cannot be changed after creation, they are inherently thread-safe. Multiple threads can access the same string object without worrying about one thread modifying it while another is reading it.

## **Advantages:**

1. **Security:** Immutability prevents the state of strings from being changed, which can help avoid security risks like modifying passwords or other sensitive data.
2. **Caching and Performance:** Since strings are immutable, they can be safely cached and reused, especially in the string pool, leading to memory and performance optimizations.
3. **Thread Safety:** Immutability makes strings safe to be used in multi-threaded environments, as multiple threads can safely share a string without synchronization.
4. **HashCode Consistency:** The `hashCode()` of a string is computed once when the string is created and remains consistent throughout its lifetime. This makes strings ideal for being used as keys in hash-based collections like `HashMap`.

**9. What are the differences between String vs StringBuffer vs StringBuilder?**

![](https://d8bhb5dvpcvh6y.archive.ph/0hnBY/3469793f106ec5f98cc17bc53fb07273580da51d.webp)

## **10. What is Spring Boot? Explain some annotations.**

Spring Boot is a framework that simplifies the process of setting up, developing, and deploying Spring-based applications.

It is built on top of the Spring Framework and offers a set of conventions, auto-configuration options, and embedded servers that eliminate the need for much of the boilerplate code that comes with traditional Spring development.

Spring Boot makes it easier to develop stand-alone, production-ready applications that you can “just run” with minimal configuration.

Key features of **Spring Boot** include:

- **Auto-configuration**: Spring Boot can automatically configure many of the components in your application based on the libraries present in the classpath.
- **Standalone**: It eliminates the need for a web.xml or complex configuration setup and runs applications as stand-alone Java applications with an embedded server (e.g., Tomcat, Jetty).
- **Production-ready**: Spring Boot provides out-of-the-box support for features like health checks, metrics, and application monitoring.

## **Core Concepts:**

- **Spring Boot Starter**: A set of predefined configurations for various scenarios, such as web, data, and messaging. For example, `spring-boot-starter-web` for web applications.
- **Spring Boot Auto Configuration**: Automatically configures components like database connections, security, etc., based on your project setup.
- **Embedded Servers**: Spring Boot includes embedded servers like Tomcat, Jetty, or Undertow, so you don’t need to deploy your app to a separate server.
- **Actuator**: Provides production-ready features such as metrics, health checks, and application monitoring.

## **Some Important Spring Boot Annotations:**

1. **@SpringBootApplication**
- The most important annotation in Spring Boot. It combines three annotations:
- `@Configuration`: Marks the class as a source of bean definitions.
- `@EnableAutoConfiguration`: Tells Spring Boot to automatically configure your application based on the dependencies you have in the classpath.
- `@ComponentScan`: Enables component scanning to detect beans in the current package and its sub-packages.
- **Example**:

```
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**2. @RestController**

- This annotation is used to create RESTful web services in Spring Boot. It combines `@Controller` and `@ResponseBody` annotations, meaning the methods in the class will return data directly to the HTTP response body.
- **Example**:

```
@RestController
public class MyController {
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }
}
```

**3. @GetMapping, @PostMapping, @PutMapping, @DeleteMapping**

- These are specialized annotations for mapping HTTP requests to methods. They are shorthand for `@RequestMapping` with the HTTP method set to GET, POST, PUT, or DELETE.
- **Example**:

```
@GetMapping("/greet")
public String greet() {
    return "Hello, Spring Boot!";
}
```

**4. @Autowired**

- Used for automatic dependency injection in Spring. Spring Boot uses this annotation to inject the required dependencies into a class.
- **Example**:

```
@Autowired
private MyService myService;
```

**5. @Component**

- Marks a class as a Spring component (bean) that should be managed by the Spring container. It is often used in combination with `@Service`, `@Repository`, or `@Controller` to define the role of the class in the application.
- **Example**:

```
@Component
public class MyComponent {
    // Logic goes here
}
```

**6. @Service**

- A specialization of `@Component` used to define a service class. It marks a class as a service provider in the business logic layer of the application.
- **Example**:

```
@Service
public class MyService {
    // Business logic goes here
}
```

**7. @Repository**

- A specialization of `@Component` used to define a data access object (DAO) or repository. It is typically used in classes that interact with a database.
- **Example**:

```
@Repository
public class MyRepository {
    // Data access logic goes here
}
```

**8. @Value**

- Used to inject values into fields from properties files or environment variables. It can be used to get configuration values into your Spring beans.
- **Example**:

```
@Value("${my.custom.property}")
private String customProperty;
```

**9. @Configuration**

- Indicates that a class contains Spring configuration, i.e., bean definitions and other configuration settings. It’s used in conjunction with Java-based configuration in Spring.
- **Example**:

```
@Configuration
public class AppConfig {
    @Bean
    public MyService myService() {
        return new MyServiceImpl();
    }
}
```

**10. @Bean**

- Used within a `@Configuration` class to declare a bean. It tells Spring that a method produces a bean that should be managed by the Spring container.
- **Example**:

```
@Configuration
public class AppConfig {
    @Bean
    public MyService myService() {
        return new MyServiceImpl();
    }
}
```

**11. @EnableAutoConfiguration**

- This annotation is typically used by `@SpringBootApplication` but can be used independently as well. It tells Spring Boot to automatically configure your application based on the libraries on the classpath.
- **Example**:

```
@EnableAutoConfiguration
public class MyApp {
    // Spring Boot will auto-configure beans based on the classpath and configurations
}
```

**12. @ConfigurationProperties**

- This annotation is used to bind external configuration properties (e.g., from `application.properties` or `application.yml`) to a POJO (Plain Old Java Object).
- **Example**:

```
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private String name;
    private String version;
    // Getters and Setters
}
```

**13. @EnableScheduling**

- This annotation enables Spring’s scheduled task execution capability, which allows you to run tasks at fixed intervals or according to cron expressions.
- **Example**:

```
@EnableScheduling
public class SchedulingConfig {

     @Scheduled(fixedRate = 5000)
     public void task() {

         System.out.println("Task executed every 5 seconds");
     }
 }
```

## **11. What are Microservices?**

Microservices is an architectural style that structures an application as a collection of small, independent services, each focused on a specific business function.

These services can be developed, deployed, and scaled independently, communicating through lightweight protocols like HTTP or messaging systems.

## **Characteristics:**

- **Independently Deployable**: Each service can be developed, deployed, and scaled independently.
- **Single Responsibility**: Each service handles a specific business capability.
- **Loose Coupling**: Services are decoupled, reducing dependencies.
- **Autonomous Data Management**: Each service has its own database.
- **Technology Agnostic**: Different services can use different tech stacks.

## **Benefits:**

- **Scalability**: Services can be scaled independently.
- **Flexibility**: Teams can use different technologies for different services.
- **Fault Tolerance**: Failure of one service doesn’t affect the entire system.
- **Faster Development**: Independent services allow parallel development and frequent releases.

## **Challenges:**

- **Complexity**: Managing multiple services and their communication can be difficult.
- **Data Consistency**: Ensuring data consistency across services is complex.
- **Deployment Overhead**: Requires managing multiple deployments, often with tools like Kubernetes.

## **12. How is authentication done in your microservices project?**

In a microservices architecture, authentication is often handled centrally to ensure that the authentication process is consistent across services. There are several approaches to achieving this, but the most common methods are:

## **1. API Gateway with Authentication**

- An API Gateway acts as the entry point for all requests to microservices. It handles authentication and forwards the authenticated request to the appropriate microservice.

**How it works**:

- The API Gateway receives requests from clients and checks for valid authentication tokens (such as JWT).
- If the token is valid, the request is forwarded to the appropriate microservice.
- The microservices do not perform authentication themselves; they trust the API Gateway.
- **Example**: Using **OAuth2** or **JWT** tokens in the API Gateway to authenticate requests.

## **2. OAuth2 and JWT (JSON Web Tokens)**

- **OAuth2** is commonly used for managing authorization, and **JWT** is a popular choice for managing authentication tokens in microservices.

**How it works**:

- **User Authentication**: The user logs in, and an identity provider (IDP) such as **Auth0**, **Keycloak**, or **Okta** authenticates the user.
- **Token Generation**: Upon successful authentication, the IDP generates a **JWT** token and sends it to the client.
- **Token Validation**: The client sends this token with each subsequent request to the microservices.
- **Microservices**: Each microservice checks the validity of the token using a shared secret or public key (for JWT) before allowing access to resources.

## **3. Single Sign-On (SSO)**

- SSO allows a user to authenticate once and gain access to all microservices without needing to log in multiple times.

**How it works**:

- SSO uses an identity provider that handles the authentication and provides access tokens to the user.
- The user can then access all microservices within the same ecosystem without re-authenticating each time.

## **4. Centralized Identity Provider**

- A single, centralized identity provider (e.g., **Keycloak**, **Okta**, or **Auth0**) is used for authenticating users and generating tokens.

**How it works**:

- The identity provider manages the user’s credentials and generates access tokens (like JWT or OAuth tokens).
- Microservices trust the centralized identity provider for validating tokens and granting access.

**13. What are the differences between Dependency Injection vs IOC?**

![](https://d8bhb5dvpcvh6y.archive.ph/0hnBY/1b414b8d41b8e45924a3ab49c9a822c685818b0b.webp)

## **14. In how many ways autowiring can be done?**

In Spring, **autowiring** is a mechanism that allows Spring to automatically inject dependencies into a bean without needing to explicitly define them in the configuration.

There are **four types of autowiring** that can be done in Spring:

## **1. Autowire by Type (`@Autowired` with `@Qualifier` or by default):**

- **Description**: Spring will attempt to autowire the dependency by matching the data type of the field, constructor, or setter method with the available bean in the container.
- **Example**:

```
@Autowired
private Car car;  // Spring injects the 'Car' bean based on type
```

- Here, Spring will inject the appropriate `Car` bean based on its type. If multiple beans of type `Car` are available, you can use `@Qualifier` to specify the exact bean:

```
@Autowired
@Qualifier("sedanCar")
private Car car;  // Autowires the bean with id 'sedanCar'
```

## **2. Autowire by Name:**

- Spring will autowire the dependency by matching the name of the property (or field) to the name of the bean in the container.
- **Example**:

```
@Autowired
private Car sedan;  // If a bean named 'sedan' exists, it will be injected
```

This requires that a bean with the same name as the property be present in the Spring context (e.g., `sedan`).

## **3. Autowire by Constructor:**

- Spring will attempt to autowire the dependencies by matching the constructor parameters with the available beans.
- **Example**:

```
@Autowired
public CarService(Car car, Engine engine) {
    this.car = car;
    this.engine = engine;
}
```

Here, Spring will inject the `Car` and `Engine` beans into the constructor based on their types.

## **4. Autowire by Setter:**

- Spring will attempt to autowire the dependencies by matching the setter method parameter types with available beans.
- **Example**:

```
@Autowired
public void setCar(Car car) {
    this.car = car;  // Spring injects the 'Car' bean
}
```

This allows Spring to inject dependencies via setter methods.

## **15. In how many ways dependency injection be done?**

In Spring, **Dependency Injection (DI)** is a fundamental concept where an object’s dependencies are provided rather than the object creating them itself.

There are three main ways to perform dependency injection in Spring:

## **1. Constructor Injection:**

- Dependencies are provided through the class constructor. This method is highly recommended because it makes the dependencies immutable and ensures that the object is always in a valid state (i.e., all required dependencies are provided at the time of object creation).
- **Example**:

```
public class CarService {
    private Car car;
    private Engine engine;

    @Autowired
    public CarService(Car car, Engine engine) {
        this.car = car;
        this.engine = engine;
    }
}
```

Here, the `CarService` class requires `Car` and `Engine` objects to be injected when it is created. Spring automatically injects them via the constructor.

## **2. Setter Injection:**

- Dependencies are provided through setter methods after the object is constructed. This is useful for optional dependencies or when you want to allow for changes in the injected dependencies post-creation.
- **Example**:

```
public class CarService {
    private Car car;

    @Autowired
    public void setCar(Car car) {
        this.car = car;
    }
}
```

Here, the `Car` dependency is injected using the `setCar` method. This method can be invoked later to inject or modify the dependency.

## **3. Field Injection:**

- Dependencies are directly injected into the fields of the class using the `@Autowired` annotation. This method is less preferred because it bypasses constructor visibility and does not allow for easy testing or enforcing immutability.
- **Example**:

```
public class CarService {
     @Autowired
     private Car car;
}
```

- Here, Spring directly injects the `Car` bean into the `car` field of the `CarService` class.

# **Scenario Based Java Interview Question**

## ***Question:***

> A new requirement has come in to shift our master data from our current legacy system to a home-built solution in the cloud. Our business model does not support off the shelve vendor options currently available. Working with the enterprise architect as well as your architect, please collaborate on a solution.
> 

## **Answer:**

To migrate master data from a legacy system to a custom-built cloud solution, I recommend a scalable, secure, and maintainable architecture.

This approach ensures seamless data handling, future-proof design, and a strong foundation for further enhancements.

Below is a breakdown of the key components and implementation plan:

## **Solution Components:**

1. **API Development**:
- Use **Spring Boot** to develop a scalable RESTful API for CRUD operations.
- Integrate pagination and filtering for efficient data querying.

**2. Cloud Integration**:

- Leverage **AWS S3** for secure, version-controlled backups and easy recovery.
- Implement encryption for data at rest and in transit using AWS Key Management Service (KMS).

**3. Data Migration**:

- Develop an **ETL (Extract, Transform, Load)** process using Python for smooth data migration.
- Introduce data validation and logging for error handling and auditing.

**4. Database Setup**:

- Use **PostgreSQL** or **Amazon RDS** for enhanced scalability and advanced features like JSONB for semi-structured data.

**5. Monitoring and Logging**:

- Implement **Spring Boot Actuator** for real-time monitoring.
- Use **ELK Stack** (Elasticsearch, Logstash, and Kibana) or **AWS CloudWatch** for centralized logging and visualization.

**6. Security Enhancements**:

- Enforce security best practices with **Spring Security** for authentication and role-based access control.
- Integrate OAuth2/JWT for secure API endpoint access.

**7. CI/CD Integration**:

- Set up automated pipelines using **GitHub Actions**, **GitLab CI**, or **Jenkins** to streamline build, test, and deployment.

# **Implementation Plan:**

## **1. Project Setup**

Update the Maven `pom.xml` with all necessary dependencies:

```
<dependencies>
    <!-- Spring Boot Dependencies -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    <!-- MySQL/PostgreSQL Driver -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
    </dependency>
    <!-- Lombok -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <scope>provided</scope>
    </dependency>
    <!-- AWS SDK -->
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>s3</artifactId>
    </dependency>
</dependencies>
```

## **2. Database Configuration**

Use environment variables for sensitive information like database credentials. Update the `application.yml` file:

```
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/master_data_db
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
  jpa:
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
    hibernate:
      ddl-auto: update
server:
  port: 8080
management:
  endpoints:
    web:
      exposure:
        include: "*"
```

## **3. Spring Boot RESTful API**

**Entity Class**

```
package com.example.entity;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "master_data")
@Data
public class MasterData {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String type;

    @Column(unique = true, nullable = false)
    private String identifier;
}

}
```

**Repository**

```
package com.example.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.entity.MasterData;

public interface MasterDataRepository extends JpaRepository<MasterData, Long> {
}
```

**Service**

```
package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.entity.MasterData;
import com.example.repository.MasterDataRepository;
import java.util.List;
import java.util.Optional;

@Service
public class MasterDataService {

    @Autowired
    private MasterDataRepository repository;

    public MasterData save(MasterData data) {
        return repository.save(data);
    }

    public List<MasterData> saveAll(List<MasterData> dataList) {
        return repository.saveAll(dataList);
    }

    public List<MasterData> findAll() {
        return repository.findAll();
    }

    public Optional<MasterData> findById(Long id) {
        return repository.findById(id);
    }

    public void deleteById(Long id) {
        repository.deleteById(id);
    }

}
```

**Controller**

```
package com.example.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.example.entity.MasterData;
import com.example.service.MasterDataService;
import java.util.List;

@RestController
@RequestMapping("/api/master-data")
public class MasterDataController {

    @Autowired
    private MasterDataService service;

    @PostMapping
    public ResponseEntity<MasterData> create(@RequestBody MasterData data) {
        return ResponseEntity.ok(service.save(data));
    }

    @GetMapping
    public ResponseEntity<List<MasterData>> getAll() {
        return ResponseEntity.ok(service.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<MasterData> getById(@PathVariable Long id) {
        return service.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteById(@PathVariable Long id) {
        service.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    // Bulk operation for creating multiple records
    @PostMapping("/bulk")
    public ResponseEntity<List<MasterData>> createBulk(@RequestBody List<MasterData> dataList) {
        List<MasterData> savedData = service.saveAll(dataList);
        return ResponseEntity.ok(savedData);
    }

    // Global Exception Handling for this Controller
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleExceptions(Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(e.getMessage());
    }
}
```

## **4. Data Migration Script (ETL Process)**

Use the Python script to migrate data:

```
import pandas as pd
import requests
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load legacy data
legacy_data = pd.read_csv("legacy_master_data.csv").dropna().drop_duplicates()

# Check if data exists
def check_data_exists(identifier):
    response = requests.get(f"http://localhost:8080/api/master-data", params={"identifier": identifier})
    return response.status_code == 200

# Retry logic for API calls
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def migrate_data(row):
    if check_data_exists(row["identifier"]):
        logging.info(f"Data already exists: {row['name']}")
        return

    payload = {
        "name": row["name"],
        "type": row["type"],
        "identifier": row["identifier"]
    }
    response = requests.post("http://localhost:8080/api/master-data", json=payload)
    response.raise_for_status()  # Raise exception for HTTP errors
    logging.info(f"Successfully migrated: {row['name']}")

# Transform and Load
for _, row in legacy_data.iterrows():
    try:
        migrate_data(row)
    except Exception as e:
        logging.error(f"Failed to migrate: {row['name']}, Error: {e}")
```

## **5. Cloud Backup Integration with AWS S3**

**S3 Service**

```
package com.example.service;

import org.springframework.stereotype.Service;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import java.nio.file.Paths;

@Service
public class S3Service {
    private final S3Client s3Client = S3Client.create();

    public void uploadFile(String bucketName, String filePath, String key) {

    try {
        PutObjectRequest request = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        s3Client.putObject(request, Paths.get(filePath));
        System.out.println("File uploaded successfully");
        }

      catch (Exception e) {
        System.err.println("File upload failed: " + e.getMessage());
    }
}
}
```

## **6. Monitoring with Actuator**

Expose health and metrics for monitoring:

```
management:
  endpoints:
    web:
      exposure:
        include: health, metrics
```

Access health at:

- [http://localhost:8080/actuator/health](https://archive.ph/o/yz27i/localhost:8080/actuator/health)
- [http://localhost:8080/actuator/metrics](https://archive.ph/o/yz27i/localhost:8080/actuator/metrics)

# **Execution Steps**

1. **Run the Application**:

```
mvn spring-boot:run
```

**2. Migrate Data**:

```
python3 data_migration.py
```

3. **Monitor and Validate**:

- Use `/actuator` endpoints for runtime health checks.

# **Extending the Project**

- **Add Security**: Use Spring Security for user authentication.
- **Enhance Data Migration**: Scale with Apache Spark or a more robust ETL framework.
- **CI/CD Pipeline**: Implement GitHub Actions or Jenkins for automated deployment.
- **Testing:** Add unit tests and integration tests, particularly for APIs and data migration scripts.

This approach ensures a smooth transition of master data to the new cloud-based system while maintaining security, reliability, and scalability.

# **Deloitte Java Developer Interview**

## **1. How to handle multiple beans at the same time in Spring Boot?**

Spring Boot provides several mechanisms to handle multiple beans of the same type:

## **1. Use `@Qualifier`**

If you have multiple beans of the same type, you can use the `@Qualifier` annotation to specify which bean to inject.

**Example:**

```
@Component
public class ServiceA implements MyService {}

@Component
public class ServiceB implements MyService {}
@Service
public class ConsumerService {
    private final MyService myService;
    @Autowired

    public ConsumerService(@Qualifier("serviceA") MyService myService) {
        this.myService = myService;
    }
}
```

- `@Qualifier("serviceA")` tells Spring to inject the `ServiceA` bean.

## **2. Use Bean Names Directly**

Spring allows you to specify bean names when defining beans in the configuration.

**Example**:

```
@Configuration
public class AppConfig {

@Bean(name = "beanA")
    public MyService myServiceA() {
        return new ServiceA();
    }
    @Bean(name = "beanB")
    public MyService myServiceB() {
        return new ServiceB();
    }
}
@Service
public class ConsumerService {
    @Autowired
    @Qualifier("beanA")
    private MyService myService;
}
```

## **3. Inject a List or Map of Beans**

If you need all beans of a specific type, inject them as a list or map.

**Example**:

```
@Service
public class ConsumerService {
    private final List<MyService> services;

    @Autowired
    public ConsumerService(List<MyService> services) {
        this.services = services;
    }
    public void processServices() {
        for (MyService service : services) {
            service.performTask();
        }
    }
}
```

- **List**: All beans of type `MyService` are injected in the order they are declared.
- **Map**: You can also inject beans into a map, where the keys are the bean names.

**Example with Map**:

```
@Autowired
private Map<String, MyService> servicesMap;
```

## **4. Use `@Primary` for a Default Bean**

If one bean is the primary candidate, you can annotate it with `@Primary`.

**Example**:

```
@Component
@Primary
public class DefaultService implements MyService {}

@Component
public class SecondaryService implements MyService {}
@Service
public class ConsumerService {
    @Autowired
    private MyService myService; // DefaultService will be injected
}
```

## **5. Use Profiles**

Use `@Profile` to activate a specific bean based on the environment or configuration.

**Example**:

```
@Component
@Profile("dev")
public class DevService implements MyService {}

@Component
@Profile("prod")
public class ProdService implements MyService {}
```

- The active profile determines which bean to load.

## **6. Use Custom Annotations**

For better clarity and maintainability, create custom annotations that act as qualifiers.

**Example**:

```
@Target({ElementType.FIELD, ElementType.PARAMETER, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface ServiceType {
    String value();
}

// Usage:
@Component
@ServiceType("special")
public class SpecialService implements MyService {}
@Autowired
@ServiceType("special")
private MyService myService;
```

## **7. Factory Methods for Conditional Beans**

Use `@Bean` methods to define beans conditionally based on logic.

**Example**:

```
@Bean
public MyService myService(Environment env) {
    if ("dev".equals(env.getProperty("spring.profiles.active"))) {
        return new DevService();
    } else {
        return new ProdService();
    }
}
```

## **2. How do we create custom annotations in Spring Boot? Explain with an example.**

Here’s how you can create and use custom annotations in Spring Boot:

## **1. Define the Annotation**

Create a custom annotation for logging method execution details.

```
package com.example.annotations;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.METHOD) // Applicable only on methods
@Retention(RetentionPolicy.RUNTIME) // Available at runtime
public @interface LogExecutionTime {
}
```

- `@Target(ElementType.METHOD)`: Restricts the annotation to methods.
- `@Retention(RetentionPolicy.RUNTIME)`: Makes the annotation available at runtime for processing.

## **2. Implement the Annotation’s Behavior Using AOP**

Use **Spring AOP** to define what happens when a method annotated with `@LogExecutionTime` is executed.

```
package com.example.aspects;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;
@Aspect
@Component
public class LoggingAspect {
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();

        Object proceed = joinPoint.proceed(); // Execute the method

        long executionTime = System.currentTimeMillis() - start;
        System.out.println(joinPoint.getSignature() + " executed in " + executionTime + "ms");

        return proceed;
    }
}
```

- `@Aspect`: Marks the class as an AOP aspect.
- `@Around("@annotation(com.example.annotations.LogExecutionTime)")`: Intercepts methods annotated with `@LogExecutionTime`.

## **3. Apply the Annotation**

Use the custom annotation in your service or controller class.

```
package com.example.services;

import com.example.annotations.LogExecutionTime;
import org.springframework.stereotype.Service;
@Service
public class SampleService {
    @LogExecutionTime
    public String performTask() throws InterruptedException {
        Thread.sleep(1000); // Simulate a task
        return "Task Completed";
    }
}
```

## **4. Test the Annotation**

Call the method annotated with `@LogExecutionTime` and observe the logging.

```
package com.example;

import com.example.services.SampleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class CustomAnnotationApplication implements CommandLineRunner {
    @Autowired
    private SampleService sampleService;
    public static void main(String[] args) {
        SpringApplication.run(CustomAnnotationApplication.class, args);
    }
    @Override
    public void run(String... args) throws Exception {
        System.out.println(sampleService.performTask());
    }
}
```

**Output**

When the application runs, the method’s execution time is logged:

```
public String com.example.services.SampleService.performTask() executed in 1002ms
Task Completed
```

## **3. What is caching in Spring Boot?**

Caching in Spring Boot is a way to store frequently accessed data in memory to improve performance and reduce repetitive database calls or computations.

Here’s how it works:

1. **Enable Caching**: Add `@EnableCaching` to the main application class.

```
@SpringBootApplication
@EnableCaching
public class CachingApplication {
    public static void main(String[] args) {
        SpringApplication.run(CachingApplication.class, args);
    }
}
```

**2. Use `@Cacheable`**: Annotate a method whose results need to be cached.

```
@Service
public class ProductService {
    @Cacheable("products")
    public String getProductById(String productId) {
        System.out.println("Fetching product from DB...");
        return "Product Details for ID: " + productId;
    }
}
```

**3. Add Dependencies**: Include the caching starter in your `pom.xml`.

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
```

**4. Test Caching**: When calling the method multiple times with the same input, the result is cached.

```
@Component
public class TestCaching implements CommandLineRunner {

@Autowired
    private ProductService productService;
    @Override
    public void run(String... args) throws Exception {
        System.out.println(productService.getProductById("101")); // Fetches from DB
        System.out.println(productService.getProductById("101")); // Fetches from cache
    }
}
```

**Output:**

```
Fetching product from DB...
Product Details for ID: 101
Product Details for ID: 101
```

This shows that the first call fetches from the database, while subsequent calls use the cached result.

Spring Boot supports caching providers like EhCache, Redis, and Caffeine, making it flexible for different use cases.

## **4. How inter service communication occurs in microservices?**

> This question was asked in Accenture Interview (Question 15) as well. So, this is an important question.
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

## **5. How can we customize specific auto configuration in spring boot?**

We can customize the defaults configurations using the following approaches:

## **1. Customizing with `application.properties` or `application.yml`:**

Spring Boot allows us to override default properties via configuration files.Example: If the default server port is `8080`, we can change it:

```
server.port=9090
```

## **2. Defining Beans to Override Defaults:**

If a default bean doesn’t meet requirements, define your own bean of the same type.For example, to customize `DataSource`:

```
@Configuration
public class DataSourceConfig {
    @Bean
    public DataSource customDataSource() {
        return DataSourceBuilder.create()
                                .url("jdbc:mysql://localhost:3306/mydb")
                                .username("user")
                                .password("password")
                                .build();
    }
}
```

## **3. Exclude Specific Auto-Configuration Classes:**

Use the `@SpringBootApplication` or `@EnableAutoConfiguration` annotations to exclude specific auto-configurations.Example: To exclude `DataSourceAutoConfiguration`:

```
@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## **4. Conditional Beans with `@ConditionalOn...` Annotations:**

If you are writing your own auto-configuration, use conditional annotations like `@ConditionalOnProperty` or `@ConditionalOnMissingBean` to control bean creation.**Example:**

```
@Configuration
public class CustomConfig {
    @Bean
    @ConditionalOnProperty(name = "custom.feature.enabled", havingValue = "true")
    public MyFeature myFeature() {
        return new MyFeature();
    }
}
```

## **5. Using Spring Factories (`spring.factories`):**

For advanced customization, you can replace or modify auto-configuration using `spring.factories` in `META-INF`.**Example**:

```
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.example.config.CustomAutoConfiguration
```

## **6. Customizing with `@ConfigurationProperties`:**

You can define your own configuration properties and bind them to classes using `@ConfigurationProperties`.**Example**:

```
@Component
@ConfigurationProperties(prefix = "app.custom")
public class CustomProperties {
    private String name;
    private int value;
    // getters and setters
}
```

Then, define the properties in `application.properties`:

```
app.custom.name=CustomName
app.custom.value=42
```

## **6. What are the different scopes present in Spring Boot?**

> This question was asked in TCS Interview (Question 7) as well. So, this is an important question.
> 

In Spring, **bean scopes** determine the lifecycle and visibility of beans in the Spring container.

Below are the main **bean scopes** available in Spring:

## **1. Singleton (Default Scope):**

- A single instance of the bean is created for the entire Spring container. All requests for the bean will return the same instance.
- **Usage**: Default scope if no other scope is specified.
- **Example**:

```
@Scope("singleton")
@Component
public class MyBean
{
...
}
```

## **2. Prototype:**

- A new instance of the bean is created each time it is requested from the Spring container. Each bean request results in a fresh instance.
- **Usage**: Useful when you need a new instance of the bean every time.
- **Example**:

```
@Scope("prototype")
@Component
public class MyBean
{
...
}
```

## **3. Request (Web Application Scope):**

- A new instance of the bean is created for each HTTP request. The bean is valid for the duration of a single HTTP request.
- **Usage**: Useful in web applications where you need a bean tied to the lifecycle of a single HTTP request.
- **Example**:

```
@Scope("request")
@Component
public class MyBean
{
...
}
```

## **4. Session (Web Application Scope):**

- A new instance of the bean is created for each HTTP session. The bean is valid for the duration of a single HTTP session.
- **Usage**: Useful in web applications where you need a bean tied to the lifecycle of an HTTP session.
- **Example**:

```
@Scope("session")
@Component
public class MyBean
{
...
}
```

## **5. Application (Web Application Scope):**

- A new instance of the bean is created for the entire lifecycle of the `ServletContext`. The bean is valid for the duration of the application.
- **Usage**: Useful when you want a bean to be shared across all requests and sessions within a web application.
- **Example**:

```
@Scope("application")
@Component
public class MyBean
{
...
}
```

## **6. WebSocket Session (Custom Scope for WebSocket Applications):**

- WebSocket sessions don’t have a predefined Spring scope like others. However, you can manage WebSocket-specific data by using a custom approach. For example, you might use **`@SessionScope`** to manage the scope for WebSocket sessions or manage WebSocket connections programmatically.
- **Usage**: WebSocket connections typically require custom logic or the use of a custom scope.
- **Example**:

```
@Scope("session")
@Component
public class WebSocketSessionHandler {
    // Manage WebSocket session-related data
}
```

## **7. How can we create a custom scope?**

We can create custom scopes for managing beans or dependencies like in the below example:

## **1. Define a Custom Scope Annotation**

Create an annotation to mark beans that belong to the custom scope.

```
import org.springframework.context.annotation.Scope;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Scope("customScope")
public @interface CustomScope {
}
```

## **2. Implement the Custom Scope**

Implement the `org.springframework.beans.factory.config.Scope` interface to manage the lifecycle of beans in the custom scope.

```
import org.springframework.beans.factory.ObjectFactory;
import org.springframework.beans.factory.config.Scope;
import java.util.HashMap;
import java.util.Map;
public class CustomScopeImplementation implements Scope {
    private final Map<String, Object> scopedObjects = new HashMap<>();
    @Override
    public Object get(String name, ObjectFactory<?> objectFactory) {
        // Check if the bean exists in the custom scope
        return scopedObjects.computeIfAbsent(name, key -> objectFactory.getObject());
    }
    @Override
    public Object remove(String name) {
        // Remove the bean from the custom scope
        return scopedObjects.remove(name);
    }
    @Override
    public void registerDestructionCallback(String name, Runnable callback) {
        // Optional: Add cleanup logic for the bean
    }
    @Override
    public Object resolveContextualObject(String key) {
        // Optional: Handle contextual objects
        return null;
    }
    @Override
    public String getConversationId() {
        // Optional: Return an ID for the scope
        return "customScope";
    }
}
```

## **3. Register the Custom Scope**

Register the custom scope with the Spring application context using a `CustomScopeConfigurer`.

```
import org.springframework.beans.factory.config.CustomScopeConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class CustomScopeConfig {
    @Bean
    public CustomScopeConfigurer customScopeConfigurer() {
        CustomScopeConfigurer configurer = new CustomScopeConfigurer();
        configurer.addScope("customScope", new CustomScopeImplementation());
        return configurer;
    }
}
```

## **4. Use the Custom Scope**

Annotate beans or components with your custom scope annotation.

```
import org.springframework.stereotype.Component;

@Component
@CustomScope
public class CustomScopedBean {
    public void sayHello() {
        System.out.println("Hello from custom-scoped bean!");
    }
}
```

## **5. Testing the Custom Scope**

Write a test or application logic to verify the behavior of the custom scope.

```
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MainApp {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(CustomScopeConfig.class);
        CustomScopedBean bean1 = context.getBean(CustomScopedBean.class);
        CustomScopedBean bean2 = context.getBean(CustomScopedBean.class);
        System.out.println(bean1 == bean2); // true or false depending on scope implementation
    }
}
```

**8. What are the differences between @SprintBootAplication vs @EnableAutoConfiguration?**

![](https://dc6zlwpwb10b5x.archive.ph/pN9yq/91d0d75f293acf54f7ea58cda9d1b39ce1ea9ddd.webp)

**9. What are the differences between Service Registry vs Service Discovery?**

![](https://dc6zlwpwb10b5x.archive.ph/pN9yq/2b9532f1baccd7004899f6da9594e560671dbdf5.webp)

## **10. What is the Saga design pattern?**

The Saga Design Pattern is a way to manage distributed transactions in microservices. Since microservices often lack a central database or traditional ACID transactions across services, the Saga pattern ensures **eventual consistency** without relying on distributed locks or two-phase commits, which can hinder scalability.

A Saga breaks a large transaction into smaller, manageable steps. Each step updates one service and, upon success, triggers the next step. If any step fails, compensating transactions are used to roll back the changes from the previous steps.

There are two main types of Sagas:

1. **Choreography:**
- Each service emits events that other services listen to and act upon.
- It’s decentralized, which works well for simpler systems, but debugging and tracing can get tricky as the system grows.

**2. Orchestration:**

- A central coordinator controls the flow of the transaction, issuing commands to each service.
- This approach is more suitable for complex workflows as it centralizes control, making it easier to monitor and debug, but it introduces a single point of failure — the orchestrator.

For example, consider an **online order system**:

1. The Order Service creates the order.
2. The Payment Service processes the payment.
3. The Inventory Service reserves the stock.
4. The Shipping Service schedules delivery.

If payment fails, the Saga might trigger compensations like canceling the order or releasing inventory.

In terms of implementation, tools like Kafka or RabbitMQ are popular for choreography, while Temporal or Netflix Conductor work well for orchestration.

## **11. What is idempotency in microservices?**

Idempotency in microservices refers to the property of an operation where performing it multiple times produces the same result as performing it once.

In other words, if a client sends the same request repeatedly — intentionally or due to retries — the state of the system remains consistent, and there are no unintended side effects.

**For example:**

- **GET** requests are naturally idempotent because retrieving the same resource multiple times doesn’t change its state.
- **PUT** requests can be idempotent if they always overwrite a resource with the same data, ensuring the state doesn’t change further with repeated requests.
- **POST** requests are typically not idempotent because they create new resources with every request unless explicitly designed to be so (e.g., by using unique identifiers).

Idempotency is crucial in distributed systems and microservices to handle failures, retries, and duplicate requests gracefully. It ensures consistency and reliability, even in the presence of network issues or system crashes.

## **12. What is the super class of all Java classes? What are some of the methods in it?**

The superclass of all Java classes is the **`Object`** class from the `java.lang` package. It is the root of the class hierarchy, and all classes in Java either directly or indirectly inherit from it.

Some important methods provided by the `Object` class are:

1. **`toString()`** - Returns a string representation of the object.
2. **`equals(Object obj)`** - Compares the object for equality.
3. **`hashCode()`** - Returns the hash code for the object.
4. **`getClass()`** - Returns the runtime class of the object.
5. **`wait()`** - Causes the current thread to wait until it is notified.
6. **`notify()`** - Wakes up a single thread waiting on the object's monitor.
7. **`notifyAll()`** - Wakes up all threads waiting on the object's monitor.
8. **`finalize()`** - Called before the object is garbage collected (deprecated as of Java 9).

## **13. Suppose you only have a class A. How can you prove that it follows OOPS principles?**

Even with a single class `A`, we can demonstrate that it adheres to **Object-Oriented Programming (OOP) principles** by checking how the class is designed internally. Here's how:

1. **Encapsulation**
- The class encapsulates data and behavior.
- If `A` has private fields and exposes them through public getter and setter methods, it satisfies encapsulation.
- **Example:**

```
public class A {
    private int value; // Private field

    public int getValue() { // Controlled access
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
```

**2. Abstraction**

- Even without a parent or child class, `A` can abstract away internal details.
- By providing methods that perform meaningful actions without exposing internal logic, the class demonstrates abstraction.
- **Example:**

```
public class A {
    private int value;

    public void incrementValue() { // Abstracted operation
        value++;
    }

    public int getValue() {
        return value;
    }
}
```

**3. Polymorphism**

- With just one class, polymorphism can still be demonstrated through method overloading within the same class.
- **Example:**

```
public class A {
    public void calculate(int x) {
        System.out.println("Square: " + (x * x));
    }

    public void calculate(int x, int y) {
        System.out.println("Product: " + (x * y));
    }
}
```

**4. Inheritance**

- Although class `A` does not explicitly inherit from another class, **every class in Java implicitly extends the `Object` class**, which is the root of the class hierarchy.
- This means `A` inherits methods like `toString()`, `hashCode()`, and `equals()`.
- **Proof:**

```
public class A
{
     @Override
     public String toString()
     {
         return "Class A instance";
     }
}
```

## **14. What are the use cases of Array list and Linked list?**

## **ArrayList**

- **Best for:** Fast random access to elements (`get()`), memory efficiency, and when the list size is relatively stable.
- **Use Case:** When you need quick lookups or additions at the end of the list. Ideal for applications where elements are accessed frequently by index, like a list of items.

## **LinkedList**

- **Best for:** Efficient insertions and deletions, especially at the beginning or middle of the list.
- **Use Case:** When you need to frequently add or remove elements at various positions in the list, such as implementing queues, stacks, or other dynamic lists.

**15. What are the differences between HashMap vs Concurrent HashMap?**

![](https://dc6zlwpwb10b5x.archive.ph/pN9yq/e377934db0eb45e2074c8459d7b38e7865a7203f.webp)

## **16. What collection would you use to remove duplicates from list and maintain insertion order?**

To remove duplicates from a list while maintaining the insertion order, I would use **`LinkedHashSet`**because LinkedHashset:

- **Removes Duplicates:** It doesn’t allow duplicate elements, ensuring only unique values are stored.
- **Maintains Insertion Order:** It preserves the order in which elements were inserted, unlike `HashSet`, which does not guarantee order.

**Example**:

```
List<String> list = new ArrayList<>(Arrays.asList("apple", "banana", "apple", "orange"));
Set<String> set = new LinkedHashSet<>(list);
List<String> result = new ArrayList<>(set);

System.out.println(result); // Output: [apple, banana, orange]
```

In this case, `LinkedHashSet` will remove the duplicates while keeping the original insertion order intact.

## **17. What is a volatile keyword in Java?**

The `volatile` keyword in Java ensures that a variable's value is always directly read from and written to the main memory, guaranteeing visibility across threads.

It prevents threads from caching the value, ensuring they see the most recent updates made by other threads.

- **Visibility Guarantee:** Ensures that updates to a `volatile` variable are immediately visible to all threads.
- **No Atomicity Guarantee:** It does not make operations like `count++` atomic. For atomic operations, synchronization is needed.

**Example:**

```
private volatile boolean flag = false;
```

Use `volatile` for variables shared between threads where visibility of changes is critical.

## **18. What is a transient keyword in Java?**

The `transient` keyword in Java is used to indicate that a field should not be serialized. When an object is serialized, any field marked as `transient` will be excluded from the serialization process.

- **Serialization:** When an object is written to a stream (for example, saving an object to a file), all its fields are typically serialized. However, `transient` fields are skipped.
- **Use Case:** It’s used for sensitive data (like passwords) or fields that don’t need to be saved (like file handles or database connections).

**Example**:

```
class Employee implements Serializable {
    private String name;
    private transient int salary;  // This field will not be serialized.

    // getters and setters
}
```

In this example, `salary` will not be serialized, while `name` will be.

**19. What are the differences between String Builder vs String Buffer?**

![](https://dc6zlwpwb10b5x.archive.ph/pN9yq/f72dfbdfce4af2284a008ecd2bf4a32020c8e4d4.webp)

**20. What are the differences between == and .equals() method?***This question was asked in [Wipro Interview (Question 11)](https://archive.ph/o/pN9yq/https://medium.com/coding-odyssey/wipro-java-developer-interview-acdcc666e553) as well. So, this is an important question.*

![](https://dc6zlwpwb10b5x.archive.ph/pN9yq/18e39e824e12b4ef89f40d9815c2e041608a9e54.webp)

## **21. What is an index and how do you create an index in SQL?**

An **index** in SQL is a database object that improves the speed of data retrieval operations on a table at the cost of additional space and maintenance time.

It helps to quickly locate and access data without having to search every row in the table.

## **Types of Indexes:**

- **Primary Index:** Automatically created on primary keys.
- **Unique Index:** Ensures all values in a column are unique.
- **Non-Unique Index:** Can have duplicate values.
- **Composite Index:** Index on multiple columns.

## **How to Create an Index:**

You can create an index using the `CREATE INDEX` statement. The syntax is:

```
CREATE INDEX index_name
ON table_name (column_name);
```

**Example**:

```
CREATE INDEX idx_employee_name
ON employees (name);
```

In this example, `idx_employee_name` is the index name, and it’s created on the `name` column of the `employees` table.

## **Use Case:**

Indexes are useful when you need fast lookups, especially on columns that are frequently queried in `WHERE`, `JOIN`, or `ORDER BY` clauses.

## **22. How indexing works internally?**

Internally, indexes in SQL are typically implemented using **B-trees (Balanced Trees)** or **Hash Tables**, depending on the type of index. Here’s how indexing works in general:

## **1. B-Tree Index (Most Common)**

- **Structure:** The index is organized as a balanced tree. The tree has nodes where each node holds a value (key) and a pointer to the data in the table.
- **Search:** Searching for a value involves traversing the tree from the root to a leaf node, which is a logarithmic operation, making it efficient (`O(log n)`).
- **Insertion/Deletion:** When data is inserted or deleted, the tree is rebalanced to maintain its balance, ensuring efficient searching.
- **Range Queries:** B-trees are ideal for range queries (e.g., `BETWEEN`, `>`, `<`), as they maintain ordered keys.

## **2. Hash Index (For Exact Match Queries)**

- **Structure:** The index is based on a hash table. The hash function maps the column’s values to a specific bucket, where the data pointers are stored.
- **Search:** Searching involves applying the hash function to the search value, which directly leads to the corresponding bucket for fast lookups (`O(1)`).
- **Limitation:** Hash indexes are good for exact matches (e.g., `=`) but are inefficient for range queries.

## **3. Clustered vs Non-Clustered Indexes**

- **Clustered Index:** The table’s rows are stored in the same order as the index, meaning there’s only one clustered index per table.
- **Non-Clustered Index:** A separate structure that holds pointers to the table’s rows, allowing multiple non-clustered indexes on the same table.

# **CGI Java Developer Interview**

## **1. What are variable length arguments in Java?**

Variable-length arguments (**varargs**) allow you to pass a variable number of arguments to a method. Use `...` after the data type in the method signature.

## **Example:**

```
public class VarArgsExample {
    public static void displayNumbers(int... numbers) {
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        displayNumbers(1, 2, 3);  // Output: 1 2 3
        displayNumbers(5);       // Output: 5
        displayNumbers();        // Output: (nothing)
    }
}
```

## **Rules:**

1. Internally, varargs are treated as an array.
2. Only one varargs parameter is allowed, and it must be the last parameter.

## **2. Can we replace arguments in main method with variable length arguments?**

Yes, we can replace the arguments in the `main` method with variable-length arguments in Java.

The `main` method signature:

```
public static void main(String[] args)
```

can be replaced with:

```
public static void main(String... args)
```

## **Example:**

```
public class VarArgsInMain {
    public static void main(String... args) {
        for (String arg : args) {
            System.out.println(arg);
        }
    }
}
```

## **How It Works:**

- Both `String[] args` and `String... args` are treated the same by the JVM.
- You can still run the program and pass command-line arguments like before.

## **Output:**

For `java VarArgsInMain Hello World`:

```
Hello
World
```

## **3. There are two variables: int i = 9 and int i = 09, is there a difference between the two? Is int i = 09 a valid statement?**

In Java, there is a difference between `int i = 9;` and `int i = 09;`.

## **Explanation:**

1. **`int i = 9;`**:
- This is a valid statement. `i` is assigned the value `9` as a decimal (base 10) number.

2. **`int i = 09;`**:

- This **is not a valid statement in Java**.
- In Java, a leading `0` indicates that the number is in **octal (base 8)** format.
- Octal numbers can only contain digits from `0` to `7`. Therefore, `09` is not a valid octal number, and it will cause a **compilation error** like:

```
error: integer number too large
```

## **Correct Example for Octal:**

```
int i = 011;  // Valid octal number (9 in decimal)
```

In this case, `011` is an octal representation, which equals `9` in decimal.

## **4. What is a Base class?**

A **base class** (also known as a **superclass** or **parent class**) in object-oriented programming is a class that provides common functionality or attributes that can be inherited by other classes (called **derived classes** or **subclasses**).

The base class acts as the foundation for creating more specialized classes.

## **Features:**

1. **Inheritance:** A subclass inherits fields and methods from the base class, enabling code reuse and reducing redundancy.
2. **Common Behavior:** The base class usually contains common behavior (methods) and attributes (fields) that are shared among all subclasses.
3. **Not Always Instantiated:** The base class itself is often not instantiated directly; instead, subclasses are instantiated, inheriting the properties and methods from the base class.

## **Example:**

```
class Animal {  // Base class
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {  // Derived class
    void bark() {
        System.out.println("The dog barks.");
    }
}
public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // Inherited from Animal (Base class)
        dog.bark(); // Defined in Dog (Derived class)
    }
}
```

## **Output:**

```
This animal eats food.
The dog barks.
```

- The **Animal** class is the base class, and **Dog** is the derived class.
- The `Dog` class inherits the `eat()` method from the `Animal` class, making use of common functionality defined in the base class.

**5. Difference between Abstract Class and Base Class?**

![](https://d1b203qpf791qi.archive.ph/HnAvZ/a7542e95fdfa730bd795c8b01b633b1a95608bd8.webp)

**6. Difference between Abstract Class and Interface?**

![](https://d1b203qpf791qi.archive.ph/HnAvZ/3a329a84c4cafd8fb27c9c92b931eb314dcc7e2f.webp)

**7. Difference between Abstract Class and Functional Interface?**

![](https://d1b203qpf791qi.archive.ph/HnAvZ/667824a63161c07e10e2e852803f551f7d0463c7.webp)

## **8. You have a Hashmap, which is overridden and the hashcode method is also overridden, so that it always returns a constant value, lets say, 1 . After adding multiple values to the hashmap, what will be the complexity of fetching a value from such hashmap.**

When the `hashCode()` method is overridden to always return a constant value (e.g., `1`), all keys will collide and be stored in the same bucket of the `HashMap`. As a result, the retrieval complexity is affected.

## **Fetching Complexity:**

- In a normal `HashMap`, the average time complexity of fetching a value is **O(1)**, as keys are usually well-distributed across buckets.
- When all keys collide (same hash code), the complexity depends on how the keys are stored in the bucket:

**Pre-Java 8:**

- The bucket uses a linked list. Searching for a key in this linked list takes **O(n)** time in the worst case, where `n` is the number of elements in the bucket.

**Java 8 and later:**

When the bucket size exceeds a threshold (typically 8), the linked list is converted to a balanced binary search tree (BST). In this case:

- Lookup in the BST takes **O(log n)**.
- If the bucket size is below the threshold, it remains a linked list, and complexity remains **O(n)**.

## **9. What is rehashing?**

Rehashing is the process of resizing a `HashMap` and redistributing its entries when the load factor threshold is exceeded.

The default load factor is 0.75, and the initial capacity is 16. This helps maintain efficient retrieval and insertion operations.

- **When:** Rehashing occurs when the number of elements exceeds `capacity × load factor`.
- **What happens:** The capacity is doubled, and all elements are rehashed into the new bucket array.
- **Time Complexity:** The rehashing process takes **O(n)** for resizing, but ensures average **O(1)** complexity for subsequent operations.

## **Example in Code:**

```
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        // Initial capacity = 4, Load factor = 0.75
        HashMap<Integer, String> map = new HashMap<>(4, 0.75f);

        // Adding elements to trigger rehashing
        map.put(1, "One");
        map.put(2, "Two");
        map.put(3, "Three");
        map.put(4, "Four"); // Rehashing happens after this
        System.out.println("HashMap after rehashing: " + map);
    }
}
```

## **10. What are the criteria for Hashmap keys?**

In Java, `HashMap` keys must satisfy below criteria to function correctly. These criteria ensure the keys are handled efficiently during storage and retrieval.

## **1. Keys Must Be Non-Null**

- A `HashMap` allows a single `null` key.
- If you try to insert another `null` key, it will overwrite the existing entry.

**Example:**

```
HashMap<String, Integer> map = new HashMap<>();
map.put(null, 1); // Valid, adds a null key
map.put(null, 2); // Overwrites the previous null key entry
System.out.println(map); // Output: {null=2}
```

## **2. Keys Should Be Immutable**

- The value of a key should not change after it’s inserted into the `HashMap`.
- If the key’s value changes (e.g., a mutable object like `StringBuilder`), it may not be retrievable because its hash code and equality comparison might differ.

**Bad Example:**

```
HashMap<StringBuilder, String> map = new HashMap<>();
StringBuilder key = new StringBuilder("key1");
map.put(key, "Value1");
key.append("Updated"); // Modifying the key

System.out.println(map.get(new StringBuilder("key1"))); // Output: null
```

## **3. Keys Must Implement `equals()` and `hashCode()` Consistently**

- The `hashCode()` method determines the bucket where the key-value pair is stored.
- The `equals()` method is used to compare keys within the same bucket.
- Keys with the same `hashCode()` should also be equal according to the `equals()` method.

**Example:**

```
class Employee {
    int id;
    String name;

    Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }
    @Override
    public int hashCode() {
        return id; // Hash based on id
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee e = (Employee) o;
        return id == e.id;
    }
}

HashMap<Employee, String> map = new HashMap<>();

Employee emp1 = new Employee(1, "John");
Employee emp2 = new Employee(1, "Doe");

map.put(emp1, "Manager");
System.out.println(map.get(emp2)); // Output: Manager
```

## **11. Can String or String builder or primitive integer or wrapper class be a hashmap key?**

## **1. String as a HashMap Key**

- **Allowed**: `String` is one of the most commonly used types for `HashMap` keys.
- **Why:** Strings are **immutable**, meaning their state cannot change after creation. This ensures consistent behavior for `hashCode()` and `equals()`.
- **Example:**

```
HashMap<String, String> map = new HashMap<>();
map.put("Key1", "Value1");
map.put("Key2", "Value2");

System.out.println(map.get("Key1")); // Output: Value1
```

## **2. StringBuilder as a HashMap Key**

- **Not Recommended**: While technically possible, it’s risky.
- **Why:**`StringBuilder` is **mutable**, so its `hashCode()` and `equals()` can change if the object is modified. This can lead to unexpected behavior.
- **Example of Issue:**

```
HashMap<StringBuilder, String> map = new HashMap<>();
StringBuilder key = new StringBuilder("Key1");
map.put(key, "Value1");
key.append("Updated"); // Modifying the key
System.out.println(map.get(new StringBuilder("Key1"))); // Output: null
```

## **3. Primitive `int` as a HashMap Key**

- **Not Allowed**: Primitive types cannot be used directly as keys because `HashMap` only accepts objects as keys.
- **Alternative:** Use the wrapper class `Integer` instead.

## **4. Wrapper Class (e.g., `Integer`) as a HashMap Key**

- **Allowed**: Wrapper classes like `Integer`, `Double`, etc., are immutable and work well as keys.
- **Why:** They implement `hashCode()` and `equals()` correctly, ensuring consistent behavior in the `HashMap`.
- **Example:**

```
HashMap<Integer, String> map = new HashMap<>();
map.put(1, "One"); map.put(2, "Two");
System.out.println(map.get(1)); // Output: One
```

## **Summary:**

![](https://d1b203qpf791qi.archive.ph/HnAvZ/27df8b3786658e017e1ebe23ac2a57eb056842f5.webp)

## **12. What is fail-fast and fail-safe in collections?**

In Java, the behavior of iterators when a collection is structurally modified during iteration is categorized into **fail-fast** and **fail-safe**.

## **1. Fail-Fast Iterators**

**Behavior:**

- These iterators throw a `ConcurrentModificationException` if the collection is structurally modified during iteration, except through the iterator itself.
- Fail-fast iterators directly access the collection’s internal structure. Any structural modification invalidates the iterator, ensuring data consistency.

**Examples:**`ArrayList`, `HashMap`, `HashSet`, etc.

**Code Example:**

```
import java.util.ArrayList;

public class FailFastExample {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);

        for (Integer num : list) {
            System.out.println(num);
            list.add(4); // Structural modification
        }
    }
}
```

**Output:**

```
1 Exception in thread "main" java.util.ConcurrentModificationException
```

## **2. Fail-Safe Iterators**

**Behavior:**

- These iterators do not throw `ConcurrentModificationException` even if the collection is structurally modified during iteration.
- Fail-safe iterators operate on a **copy** of the collection, not the original, so modifications to the original collection do not affect iteration.

**Examples:**`CopyOnWriteArrayList`, `ConcurrentHashMap`.

**Code Example:**

```
import java.util.concurrent.CopyOnWriteArrayList;

public class FailSafeExample {
    public static void main(String[] args) {
        CopyOnWriteArrayList<Integer> list = new CopyOnWriteArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);

        for (Integer num : list) {
            System.out.println(num);
            list.add(4); // Structural modification allowed
        }
        System.out.println("List after iteration: " + list);
    }
}
```

**Output:**

```
1 2 3 List after iteration: [1, 2, 3, 4, 4, 4]
```

## **Differences Between Fail-Fast and Fail-Safe**

![](https://d1b203qpf791qi.archive.ph/HnAvZ/a1700e6608d1ec6d7edf38c131ef72efe087f03f.webp)

## **13. You have a string builder as a hashmap key, now you appended the string builder. What will be value of the string builder with the get object?**

If you use a `StringBuilder` as a `HashMap` key and modify (append) the `StringBuilder` after adding it to the map, you may not be able to retrieve the value associated with that key. This is because the `hashCode` of `StringBuilder` depends on its current state, and modifying it changes the `hashCode`.

## **Explanation:**

1. **StringBuilder as a Key:**
- The `hashCode()` of a `StringBuilder` is calculated based on its current content.
- If you modify the `StringBuilder`, the `hashCode()` changes, and the `HashMap` can no longer locate the key in its internal structure.

**2. Effect on Retrieval:**

- After modification, the key becomes “untraceable” since the `HashMap` uses the `hashCode` to find the bucket where the key-value pair is stored.

## **Code Example:**

```
import java.util.HashMap;
public class HashMapStringBuilderKey {
    public static void main(String[] args) {
        HashMap<StringBuilder, String> map = new HashMap<>();
        StringBuilder key = new StringBuilder("Key1");
        map.put(key, "Value1");
        System.out.println("Before modification: " + map.get(key)); // Output: Value1
        // Modify the StringBuilder
        key.append("Modified");
        System.out.println("After modification: " + map.get(key)); // Output: null
    }
}
```

## **Output:**

```
Before modification: Value1
After modification: null
```

## **Solution:**

1. Use immutable keys like `String` instead of `StringBuilder`.

```
HashMap<String, String> map = new HashMap<>();
String key = "Key1";

map.put(key, "Value1"); key = key + "Modified"; // No impact on map

System.out.println(map.get("Key1")); // Output: Value1
```

2. Avoid modifying objects used as keys in a `HashMap`.

## **14. There are two variables, storing exchange rates of currency. Now, what data type will you use for these variables and which method will you use to equate them?**

When dealing with exchange rates of currencies, it’s essential to ensure precision due to the potential for financial inaccuracies caused by floating-point arithmetic.

## **Data Type for Exchange Rates**

- Use `BigDecimal` in Java for storing exchange rates.
- **Reason:** `BigDecimal` provides high precision and control over rounding behavior, making it ideal for financial calculations.
- **Why not `float` or `double:`** Floating-point numbers (`float` and `double`) can introduce rounding errors due to their binary representation, which is unsuitable for financial computations.

## **Method for Equating Exchange Rates**

- To compare two `BigDecimal` variables, you can use the `compareTo()` method instead of `equals()`.
- **Reason:** The `equals()` method checks for both value and scale (e.g., `1.0` is not equal to `1.00`), whereas `compareTo()` only compares the numerical value.

## **Example:**

```
import java.math.BigDecimal;

public class CurrencyExchange {
    public static void main(String[] args) {
        BigDecimal rate1 = new BigDecimal("74.256");
        BigDecimal rate2 = new BigDecimal("74.2560");

        // Comparing using compareTo()
        if (rate1.compareTo(rate2) == 0) {
            System.out.println("Exchange rates are equal.");
        } else {
            System.out.println("Exchange rates are different.");
        }
    }
}
```

## **15. How long does Heap memory and Stack Memory stay in Java?**

## **Heap Memory Lifecycle:**

- Persists as long as the object is referenced or until garbage collection removes it.
- Exists for the entire lifetime of the JVM instance.

## **Stack Memory Lifecycle:**

- Exists only during the execution of a method.
- Destroyed when the method finishes or the thread terminates.

## **16. What is Marker interface in Java? Can we create a custom Marker interface?**

- A **marker interface** is an interface with no methods or fields (essentially empty).
- It is used to indicate or “mark” a class for a specific capability, behavior, or property.

## **Examples:**

- **`Serializable`:** Marks a class as serializable, enabling object serialization.
- **`Cloneable`:** Marks a class as cloneable, allowing its objects to be cloned.
- **`Remote`:** Marks a class as remote for distributed computing.

## **Purpose:**

- They act as a **tag** to signal to the JVM or frameworks that special behavior should be applied to marked classes.
- The marker is often checked using the `instanceof` operator or reflection.

## **Example:**

```
public class Example implements Serializable {
    // JVM allows serialization because this class is marked as Serializable
}
```

## **Custom Marker Interface?**

Yes, you can create your own marker interface. It can be used to signal a specific behavior or functionality in your application.

## **Example:**

```
// Custom Marker Interface
public interface MyMarker {}

// Class implementing the marker
public class MyClass implements MyMarker {}

// Checking the marker
public class MarkerTest {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        if (obj instanceof MyMarker) {
            System.out.println("Object is marked with MyMarker!");
        } else {
            System.out.println("Object is not marked.");
        }
    }
}
```

## **Usecase:**

- When you need to define a custom tagging mechanism for specific types of classes.
- When frameworks or tools you create need to apply special logic to marked classes.

However, modern alternatives like **annotations** (e.g., `@Override`, `@Deprecated`) are often preferred for such use cases as they are more flexible and provide metadata directly.

## **17. You have an array list of Employees having Emp Id and Manager id. Retrieve data of all employees reporting to Manager with Emp Id = 200.**

```
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    private int empId;
    private int managerId;

    // Constructor
    public Employee(int empId, int managerId) {
        this.empId = empId;
        this.managerId = managerId;
    }

    // Getters
    public int getEmpId() {
        return empId;
    }
    public int getManagerId() {
        return managerId;
    }

    @Override
    public String toString() {
        return "Employee{empId=" + empId + ", managerId=" + managerId + '}';
    }
}

public class ManagerEmployeeFilter {
    public static void main(String[] args) {

        // Sample Employee List
        List<Employee> employees = Arrays.asList(
                new Employee(101, 200),
                new Employee(102, 200),
                new Employee(103, 201),
                new Employee(104, 200),
                new Employee(105, 202)
        );

        // Manager ID to filter by
        int managerId = 200;

        // Filtering employees who report to the manager with EmpId = 200
        List<Employee> reportingEmployees = employees.stream()
                .filter(emp -> emp.getManagerId() == managerId)
                .collect(Collectors.toList());

        // Check if the list is empty or contains employees
        if (reportingEmployees.isEmpty()) {
            System.out.println("No employees found reporting to Manager with EmpId = " + managerId);
        } else {
            System.out.println("Employees reporting to Manager with EmpId = " + managerId + ":");
            reportingEmployees.forEach(System.out::println);
        }
    }
}
```

## **Explanation:**

1. **Data Filtering:**
- `filter(emp -> emp.getManagerId() == managerId)` ensures we only retrieve employees whose `managerId` is `200`.

**2. Check for Empty List:**

- If `reportingEmployees.isEmpty()` evaluates to `true`, it prints a message indicating no employees were found.

## **18. What is a Circuit breaker pattern?**

> This is a very important question that came up in both my first and second rounds at Capgemini.
> 

In a microservices architecture, a **Circuit Breaker** is a design pattern used to detect failures in a system and prevent them from propagating to other parts of the system. It helps in improving the system’s resilience by allowing the system to recover from failures gracefully. The main goal is to prevent a system from repeatedly making calls to a service that is failing and causing additional load or cascading failures.

## **Circuit Breaker Working:**

1. **Closed State**:
- In the closed state, the circuit breaker allows all requests to go through to the service.
- If the service responds successfully, everything continues as normal.
- If the service fails a number of times (typically due to timeouts or exceptions), the circuit breaker moves to the **open state**.

**2. Open State**:

- When the failure threshold is exceeded, the circuit breaker “opens” and all requests are rejected.
- During this time, instead of making the request, the circuit breaker returns a fallback response or performs other recovery mechanisms.
- After a certain “cooldown” period, the circuit breaker will move to the **half-open state**.

**3. Half-Open State**:

- In the half-open state, the circuit breaker allows a limited number of requests to pass through to check if the issue is resolved.
- If the service is working fine, the circuit breaker goes back to the **closed state**.
- If the service is still failing, the circuit breaker goes back to the **open state**.

## **Components of Circuit Breaker:**

- **Failure Threshold**: The number of failures after which the circuit breaker will open.
- **Timeouts**: Time window after which the circuit breaker switches back from the open to the half-open state.
- **Fallback Mechanism**: In case of failure, a fallback response can be provided, such as cached data or default values.

## **Advantages of Circuit Breaker:**

1. **Prevents cascading failures**: By stopping the flow of requests to a failing service, you prevent further damage or system overload.
2. **Improves resilience**: The system can recover more gracefully by falling back to alternative paths.
3. **Better resource management**: The system avoids overloading failing services and uses resources more efficiently.

## **19. How do you do fault isolation?**

Fault isolation is the process of identifying, diagnosing, and containing errors or faults in a system to prevent them from affecting other parts of the system.

It ensures that failures are handled gracefully and do not propagate or impact other services or components.

Here’s how fault isolation can be achieved:

## **1. Exception Handling:**

- Use robust exception handling mechanisms to capture errors and prevent crashes.
- Properly define custom exceptions where needed to better categorize different fault scenarios.

## **2. Try-Catch Blocks (Error Containment):**

- Wrap critical sections of code that are prone to errors in try-catch blocks to catch exceptions and handle them appropriately, such as logging them or notifying the user.

## **3. Circuit Breaker Pattern:**

- Implement a **circuit breaker** to detect and isolate failures in external services or systems.
- If a particular service or external resource is failing repeatedly, the circuit breaker will stop further calls to it, preventing cascading failures.

## **4. Redundancy:**

- Use redundancy in systems to isolate faults. For example, in databases, replication can help isolate faults and ensure availability even if one instance fails.
- Backup systems and load balancers can help ensure that failure in one part of the system does not bring down the entire system.

## **5. Microservices Architecture:**

- In a **microservices** architecture, each service is isolated from others, and failures in one service don’t necessarily impact others.
- Implementing proper service boundaries and API gateways can further isolate faults within specific services.

## **6. Failover Mechanism:**

- A **failover** mechanism allows a backup system or server to take over automatically when a primary system fails, ensuring minimal impact on system performance.

## **7. Log Aggregation and Monitoring:**

- Set up log aggregation tools (e.g., ELK stack, Splunk) to monitor application logs in real-time. This helps in quickly identifying when something goes wrong, even before it fully impacts the system.
- Continuous monitoring tools (e.g., Prometheus, Grafana) help track the system’s health and allow for proactive fault isolation.

## **8. Distributed Tracing:**

- Use distributed tracing (e.g., OpenTracing, Zipkin) to track requests across services and pinpoint where failures occur in a distributed environment.

## **9. Isolation at the Network Level:**

- In distributed systems, ensure services can be isolated at the network level, where faulty services can be isolated by routing or network partitioning, preventing broader system impacts.

## **10. Resource Limits:**

- Set resource limits (e.g., memory, CPU) to prevent a single faulty process from consuming all system resources and affecting other parts of the application.

## **11. Automated Testing:**

- Perform thorough **unit, integration, and regression testing** to catch errors during development, preventing bugs from reaching production environments.

## **12. Containerization and Virtualization:**

- Use **containers** (e.g., Docker) or virtual machines to isolate environments. If a container or VM fails, it can be restarted without affecting the rest of the system.

# **Capgemini Java Developer Interview — 2**

## **1. Wrap Checked Exceptions in a Runtime Exception**

You can catch the checked exception inside the lambda expression and wrap it in a `RuntimeException`.

```
List<String> data = List.of("1", "2", "a", "4");
List<Integer> result = data.stream()
    .map(item -> {
        try {
            return Integer.parseInt(item);
        } catch (NumberFormatException e) {
            throw new RuntimeException("Error parsing: " + item, e);
        }
    })
    .collect(Collectors.toList());
```

## **2. Use a Custom Functional Interface**

Create a functional interface that allows throwing checked exceptions, and use it in the lambda expression.

```
@FunctionalInterface
public interface CheckedFunction<T, R> {
    R apply(T t) throws Exception;
}
// Wrapper for handling exceptions
public static <T, R> Function<T, R> handleCheckedException(CheckedFunction<T, R> function) {
    return item -> {
        try {
            return function.apply(item);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    };
}
// Usage
List<String> data = List.of("1", "2", "a", "4");
List<Integer> result = data.stream()
    .map(handleCheckedException(Integer::parseInt))
    .collect(Collectors.toList());
```

## **3. Use a Default Value for Exception Cases**

You can catch the exception in the lambda expression and return a default value in case of failure.

```
List<String> data = List.of("1", "2", "a", "4");
List<Integer> result = data.stream()
    .map(item -> {
        try {
            return Integer.parseInt(item);
        } catch (NumberFormatException e) {
            return 0; // Default value
        }
    })
    .collect(Collectors.toList());
```

## **4. Filter Out Invalid Entries**

Use a `filter` step to skip invalid elements before applying the lambda expression.

```
List<String> data = List.of("1", "2", "a", "4");
List<Integer> result = data.stream()
    .filter(item -> {
        try {
            Integer.parseInt(item);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    })
    .map(Integer::parseInt)
    .collect(Collectors.toList());
```

## **5. Use `flatMap` for Better Handling**

You can return an empty stream when an exception occurs, effectively skipping invalid elements.

```
List<String> data = List.of("1", "2", "a", "4");

List<Integer> result = data.stream()
    .flatMap(item -> {
        try {
            return Stream.of(Integer.parseInt(item));
        } catch (NumberFormatException e) {
            return Stream.empty(); // Skip invalid elements
        }
    })
    .collect(Collectors.toList());
```

## **6. Log and Handle Errors Gracefully**

If you want to log the error and still proceed:

```
List<String> data = List.of("1", "2", "a", "4");
List<Integer> result = data.stream()
    .map(item -> {
        try {
            return Integer.parseInt(item);
        } catch (NumberFormatException e) {
            System.err.println("Invalid input: " + item);
            return -1; // Placeholder value
        }
    })
    .collect(Collectors.toList());
```

***2. What is the difference between IntStream and Stream of Integer?***

![](https://d2cwpxxfdri09s.archive.ph/64kV9/8cd530fee6887a0d8a3ed2b6c8d7d397eadea3fd.webp)

***3. What are the differences between Interfaces and Abstract class?***

![](https://d2cwpxxfdri09s.archive.ph/64kV9/2d61fefe1b0a52a36a3bf8ae53c38d1d01096399.webp)

***4. What is the output of the below code?***

```
class A {
    public void m(String p) {
        System.out.println("String method called");
    }

    public void m(Object o) {
        System.out.println("Object method called");
    }

    public static void main(String[] args) {
        A a = new A();
        a.m(null);
    }
}
```

## **Output:**

```
String method called
```

## **Explanation:**

When you call `a.m(null);`, Java needs to determine which method to invoke between `m(String p)` and `m(Object o)`. Since `String` is more specific (it's a subclass of `Object`), Java prefers the `m(String p)` method. Java always chooses the most specific method when `null` is passed.

***5. Explain the below scenarios in code?***

```
class A {
    public void display() {
        System.out.println("Class A");
    }
}

class B extends A {
    public void display() {
        System.out.println("Class B");
    }
}
public class Test {
    public static void main(String[] args) {

// Case 1:
        B b = new A();  // Is this possible?

// Case 2:
        A a = new B();  // Is this possible?

        }
}
```

## **Explanation:**

1. **Case 1: `B b = new A();`**
- This **will cause a compile-time error** because you cannot assign an instance of a superclass (`A`) to a reference of a subclass (`B`).
- `A` is not a subclass of `B`, so this assignment is not allowed.

**2. Case 2: `A a = new B();`**

- This is **valid** because `B` is a subclass of `A`, and in Java, you can assign an object of a subclass (`B`) to a reference of its superclass (`A`), which is known as **upcasting**.
- The method `display()` in `B` is called (not `A`), demonstrating **dynamic method dispatch** (runtime polymorphism), where the actual object's type (`B`) determines which method is invoked, even though the reference type is `A`.

***6. Suppose you have a Hashset with 3 attributes: name, id, and deptId for each employee. Write a program to group the employees by deptId and return the count of employees in each department using Java 8.***

```
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    int empId;
    String name;
    int deptId;
    public Employee(int empId, String name, int deptId) {
        this.empId = empId;
        this.name = name;
        this.deptId = deptId;
    }
    public int getDeptId() {
        return deptId;
    }
    @Override
    public String toString() {
        return "Employee{" + "empId=" + empId + ", name='" + name + '\'' + ", deptId=" + deptId + '}';
    }
}
public class DepartmentEmployeeCount {
    public static void main(String[] args) {
        // List of employees
        List<Employee> employees = Arrays.asList(
                new Employee(101, "John", 1),
                new Employee(102, "Jane", 1),
                new Employee(103, "Doe", 2),
                new Employee(104, "Mark", 1),
                new Employee(105, "Alice", 2)
        );
        // Using Stream API to group employees by department and count them
        Map<Integer, Long> departmentCount = employees.stream()
                .collect(Collectors.groupingBy(Employee::getDeptId, Collectors.counting()));

       // Printing department count based on deptId
        departmentCount.forEach((deptId, count) -> {
            System.out.println("Dept ID: " + deptId + " | Employee Count: " + count);
        });
    }
}
```

## **Explanation:**

1. **Stream API**:
- `employees.stream()` creates a stream from the list of employees.
- `Collectors.groupingBy(Employee::getDeptId, Collectors.counting())` groups employees by their `deptId` and counts the number of employees in each department.
- `groupingBy(Employee::getDeptId)` groups the stream elements by the `deptId`.
- `Collectors.counting()` counts the number of elements (employees) in each group (department).

**2. Map Result**:

- The result is a `Map<Integer, Long>` where:
- The key is the `deptId`.
- The value is the count of employees in that department (`Long` type).

## **Output:**

```
Dept ID: 1 | Employee Count: 3
Dept ID: 2 | Employee Count: 2
```

***7. What will be the output of below code:***

```
import java.util.HashMap;
import java.util.Map;

class Employee {
    int id;
    String name;
    // Constructor to initialize Employee object
    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }
    // Override hashCode() to calculate hash based on id and name
    @Override
    public int hashCode() {
        return id + name.hashCode(); // Hash code based on id and name
    }
    // Override equals() to compare Employee objects based on id and name
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true; // Same reference check
        if (obj == null || getClass() != obj.getClass()) return false; // Null check and class type check
        Employee employee = (Employee) obj;
        return id == employee.id && name.equals(employee.name); // Compare id and name
    }
    // Override toString() for better representation
    @Override
    public String toString() {
        return "Employee{id=" + id + ", name='" + name + "'}";
    }
}
public class Main {
    public static void main(String[] args) {
        // Creating a new HashMap with Employee as key and Integer as value (salary)
        Map<Employee, Integer> salaryMap = new HashMap<>();
        // Adding employees to the map with their respective salaries
        salaryMap.put(new Employee(1, "Ram"), 1000); // Adding first employee
        salaryMap.put(new Employee(1, "Ram"), 200);  // Adding second employee (same id and name)
        // Retrieving the salary using the same Employee object (id=1, name="Ram")
        System.out.println("Salary of employee Ram: " + salaryMap.get(new Employee(1, "Ram")));
    }
}
```

## **Output:**

```
Salary of employee Ram: 200
```

## **Explanation of Output:**

1. **First `put()` Call:**
- The first `put()` inserts an employee object with `id=1` and `name="Ram"` into the map with a salary of `1000`.

**2. Second `put()` Call**:

- The second `put()` call inserts another employee with the same `id=1` and `name="Ram"`, but the salary is `200`.
- Since both employee objects are considered equal (as defined by the `equals()` and `hashCode()` methods), the second call **overwrites** the first one.

**3. Get Salary**:

- The `salaryMap.get(new Employee(1, "Ram"))` retrieves the salary of the employee with `id=1` and `name="Ram"`.
- Despite the fact that the `get()` method creates a new `Employee` object, the map treats it as equal to the employee already in the map, so the most recently inserted salary value (`200`) is returned.

Thus, the final output shows “**Salary of employee Ram: 200**” because the salary was updated in the map during the second `put()` call.

***8. Write a program to move all zeros at the end of the array without changing the insertion order.***

```
import java.util.Arrays;

public class MoveZeros {
    // Method to move zeros to the end of the array
    public static void moveZerosToEnd(int[] arr) {
        int n = arr.length;
        int nonZeroIndex = 0; // Index to place the non-zero elements
        // Iterate through the array
        for (int i = 0; i < n; i++) {
            if (arr[i] != 0) {
                // Swap non-zero element with the element at nonZeroIndex
                int temp = arr[i];
                arr[i] = arr[nonZeroIndex];
                arr[nonZeroIndex] = temp;
                nonZeroIndex++;
            }
        }
    }
    // Main method to test the functionality
    public static void main(String[] args) {
        int[] arr = {0, 1, 9, 0, 3, 12, 0, 5};

        System.out.println("Original array: " + Arrays.toString(arr));

        // Move zeros to the end
        moveZerosToEnd(arr);

        System.out.println("Array after moving zeros: " + Arrays.toString(arr));
    }
}
```

## **Explanation:**

1. **Initialization**: The variable `nonZeroIndex` is initialized to `0`. It keeps track of the position where the next non-zero element should be placed.
2. **Iterating through the array**: The array is traversed element by element using a `for` loop. For each non-zero element found, it is swapped with the element at the `nonZeroIndex`.
3. **Swapping**: When a non-zero element is encountered, it is swapped with the element at the `nonZeroIndex`. After the swap, `nonZeroIndex` is incremented to place the next non-zero element in the correct position.
4. **Result**: By the end of the loop, all non-zero elements are moved to the beginning of the array, and the zeros are automatically shifted to the end.

## **Output:**

```
Original array: [0, 1, 9, 0, 3, 12, 0, 5]
Array after moving zeros: [1, 9, 3, 12, 5, 0, 0, 0]
```

***9. What are the differences between Bean and Component?***

![](https://d2cwpxxfdri09s.archive.ph/64kV9/ad045a12d09579e4f715bc1b1130415b54f003ad.webp)

***10. Can we define two main() methods in Spring?***

In a Spring application:

1. **Same Class**: Only **one `main()` method** is allowed per class. You cannot have two `main()` methods in the same class.
2. **Different Classes**: You can define **multiple `main()` methods** in **different classes**. Only one class will be chosen as the entry point when running the application.

In Spring Boot:

- Typically one `main()` method is used to start the application, but you can have multiple Spring Boot applications with different entry points in separate classes.

***11. Explain POST Endpoint validation in brief.***

To perform **POST endpoint validation** in Spring:

1. **Basic Validation**: Use `@Valid` on the request body parameter with JSR-303 annotations (`@NotNull`, `@Size`, etc.).

```
@PostMapping public ResponseEntity<String> addEmployee(@Valid @RequestBody Employee employee)
{
    return ResponseEntity.ok("Employee added successfully!");
}
```

**2. Error Handling**: Use `BindingResult` after `@Valid` to capture and handle validation errors.

```
@PostMapping public ResponseEntity<String> addEmployee
(@Valid @RequestBody Employee employee, BindingResult result)
{
     if (result.hasErrors())
      {
         return ResponseEntity.badRequest().body("Validation failed");
       }
   return ResponseEntity.ok("Employee added successfully!");
}
```

**3. Custom Validation**: Create custom validation logic using `@Constraint` and `ConstraintValidator`.

**4. Global Error Handling**: Use `@ControllerAdvice` to handle validation exceptions globally and return structured error responses.

```
@ExceptionHandler(MethodArgumentNotValidException.class)
public ResponseEntity<Object> handleValidationExceptions (MethodArgumentNotValidException ex)
{
  return new ResponseEntity<>(ex.getBindingResult().getAllErrors(),
  HttpStatus.BAD_REQUEST);
}
```

***12. Explain Circuit Breaker in brief.***

In a microservices architecture, a **Circuit Breaker** is a design pattern used to detect failures in a system and prevent them from propagating to other parts of the system. It helps in improving the system’s resilience by allowing the system to recover from failures gracefully. The main goal is to prevent a system from repeatedly making calls to a service that is failing and causing additional load or cascading failures.

## **How Circuit Breaker Works:**

1. **Closed State**:
- In the closed state, the circuit breaker allows all requests to go through to the service.
- If the service responds successfully, everything continues as normal.
- If the service fails a number of times (typically due to timeouts or exceptions), the circuit breaker moves to the **open state**.

**2. Open State**:

- When the failure threshold is exceeded, the circuit breaker “opens” and all requests are rejected.
- During this time, instead of making the request, the circuit breaker returns a fallback response or performs other recovery mechanisms.
- After a certain “cooldown” period, the circuit breaker will move to the **half-open state**.

**3. Half-Open State**:

- In the half-open state, the circuit breaker allows a limited number of requests to pass through to check if the issue is resolved.
- If the service is working fine, the circuit breaker goes back to the **closed state**.
- If the service is still failing, the circuit breaker goes back to the **open state**.

## **Key Components of Circuit Breaker:**

- **Failure Threshold**: The number of failures after which the circuit breaker will open.
- **Timeouts**: Time window after which the circuit breaker switches back from the open to the half-open state.
- **Fallback Mechanism**: In case of failure, a fallback response can be provided, such as cached data or default values.

## **Advantages of Circuit Breaker:**

1. **Prevents cascading failures**: By stopping the flow of requests to a failing service, you prevent further damage or system overload.
2. **Improves resilience**: The system can recover more gracefully by falling back to alternative paths.
3. **Better resource management**: The system avoids overloading failing services and uses resources more efficiently.

# **Capgemini Java Developer Interview**

1. ***Write a program to find second duplicate number from the given list.***

```
import java.util.*;
import java.util.stream.*;

public class SecondDuplicateFinderWithStream {
    public static void main(String[] args) {
        // Example list of numbers
        List<Integer> numbers = Arrays.asList(5, 3, 8, 3, 2, 1, 8, 7, 2);

        // Find the second duplicate using Stream API
        Optional<Integer> secondDuplicate = findSecondDuplicate(numbers);

        // Print the result
        secondDuplicate.ifPresentOrElse(
            num -> System.out.println("The second duplicate number is: " + num),
            () -> System.out.println("No second duplicate found.")
        );
    }

    public static Optional<Integer> findSecondDuplicate(List<Integer> numbers) {
        Set<Integer> seen = new HashSet<>();

        return numbers.stream()
                .filter(num -> !seen.add(num)) // Filter only duplicate numbers
                .skip(1)                      // Skip the first duplicate
                .findFirst();                 // Find the second duplicate
    }
}
```

**Output:**

```
The second duplicate number is: 8
```

***2. What will be the size of below Hashset?***

```
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        set.add(5); // Input 1
        set.add(5); // Input 2

        System.out.println("HashSet size: " + set.size());
    }
}
```

**Explanation:**

As Hashset does not allow duplicate elements, thus the second set.add(5) [in line Input 2] will be rejected and **the size of Hashset will be 1.**

***3. What is the output of below program?***

```
public class Main {
    public static void main(String[] args) {
        String s = "Java";
        s.concat(" World");
        System.out.println(s);    }
}
```

**Output**:

```
Java
```

**Explanation:**

Strings in Java are **immutable**. The `concat` method creates a new `String` but does not modify the original `String` (`s`). Since the new string is not assigned to `s`, the value of `s` remains `"Java"`.

To update `s` with the concatenated value, assign the result of `concat` back to `s`:

**Fixed Code:**

```
public class Main {
    public static void main(String[] args) {
        String s = "Java";
        s = s.concat(" World"); // Assigns the concatenated string back to s
        System.out.println(s); // Prints the updated value of s
    }
}
```

**Output**:

```
Java World
```

***4. What is the output of below program?***

```
try {
    // Code that may throw exceptions
} catch (Exception e) {
    // Print StackTrace
} catch (NullPointerException npe) {
    // Print StackTrace
}
```

**Explanation:**

In Java, you **cannot catch a larger exception (e.g., `Exception`) before a smaller one (e.g., `NullPointerException`)** because **exception classes follow an inheritance hierarchy**. `NullPointerException` is a subclass of `Exception`, so if you catch `Exception` first, it would already handle all exceptions of its subclasses (like `NullPointerException`), leaving the smaller, more specific exceptions unreachable.

***5. What is the difference between map() and flatmap()?***

![](https://df473cvj66mjlj.archive.ph/WKQtn/ebb7792f5541dfa872fb323b06e36b5c0b815535.webp)

***6. What are some examples of functional Interfaces in Java?***

Common **functional interfaces** in Java:

**1. Runnable:**

- **Method**: `void run()`
- **Example**:

```
Runnable task = () -> System.out.println("Running task...");
task.run();
```

- **Explanation**: Represents a task to be executed. It has a single method `run()` that takes no arguments and returns no result.

**2. Comparator:**

- **Method**: `int compare(T o1, T o2)`
- **Example**:

```
Comparator<String> comparator = (s1, s2) -> s1.length() - s2.length();
```

- **Explanation**: Used for comparing two objects. It allows custom sorting logic (e.g., comparing based on string length).

**3. Predicate:**

- **Method**: `boolean test(T t)`
- **Example**:

```
Predicate<Integer> isEven = x -> x % 2 == 0;
```

- **Explanation**: Represents a condition or test on a single argument, returning a boolean.

**4. Function:**

- **Method**: `R apply(T t)`
- **Example**:

```
Function<Integer, Integer> square = x -> x * x;
```

- **Explanation**: Transforms an input of type `T` to an output of type `R` (e.g., squaring a number).

**5. Consumer:**

- **Method**: `void accept(T t)`
- **Example**:

```
Consumer<String> printUpperCase = str -> System.out.println(str.toUpperCase());
```

- **Explanation**: Performs an operation on a single argument without returning a result (e.g., printing in uppercase).

**6. Supplier:**

- **Method**: `T get()`
- **Example**:

```
Supplier<Double> randomValue = () -> Math.random();
```

- **Explanation**: Provides a result without taking any input (e.g., generating a random value).

Each of these functional interfaces has a single abstract method, which makes them suitable for use with **lambda expressions** in Java.

***7. How to create an Immutable class in Java?***

Immutable class in java means that once an object is created, we cannot change its content. In Java, all the wrapper classes (like Integer, Boolean, Byte, Short) and String class are immutable.

We can create our own immutable class with below steps:

- The class must be declared as final so that child classes can’t be created.
- Data members in the class must be declared private so that direct access is not allowed.
- Data members in the class must be declared as final so that we can’t change the value of it after object creation.
- A parameterized constructor should initialize all the fields performing a deep copy so that data members can’t be modified with an object reference.
- Deep Copy of objects should be performed in the getter methods to return a copy rather than returning the actual object reference)

> Note: There should be no setters or in simpler terms, there should be no option to change the value of the instance variable.
> 

***8. In which scenario do we get NoClassDefFound Error?***

A `NoClassDefFoundError` occurs when the JVM or a class loader cannot find a class at runtime, even though it was available during compile-time. This typically happens due to missing class files in the classpath, incorrect classpath configuration, or if a class was removed, renamed, or failed to load due to a static initialization error. It can also occur if there's a version mismatch between the compiled class and the runtime environment.

***9. What is a transient variable and what are it’s use cases?***

A **transient** variable in Java is marked with the `transient` keyword to prevent it from being serialized. When an object is serialized, transient variables are not included in the serialized data.

**Use Cases of transient Keyword:**

1. **Sensitive Data**:
- Prevents sensitive information (e.g., passwords) from being serialized.
- **Example**: `private transient String password;`

**2. Temporary or Caching Data**:

- Skips serialization of temporary data that can be recomputed (e.g., cached data).
- **Example**: `private transient Map<String, String> cache;`

**3. Non-Serializable Dependencies**:

- Avoids serialization of objects that are not serializable (e.g., database connections or GUI components).
- **Example**: `private transient Connection conn;`

***10. What is Qualifier annotation and what is it’s alternative?***

The `@Qualifier` annotation in Java is used in dependency injection to specify which bean should be injected when there are multiple candidates of the same type. It helps disambiguate between beans that share the same type but are meant for different purposes.

**Example**:

```
@Qualifier("serviceA")
@Autowired
private Service service;
```

In this example, `@Qualifier("serviceA")` ensures that the `serviceA` bean is injected, even if there are other `Service` beans available.

**Alternatives:**

1. **Primary Annotation (`@Primary`)**:
- Used to mark a bean as the default choice when multiple beans of the same type are available.
- **Example**:

```
@Primary
@Bean
public Service serviceA()
{
  return new ServiceA();
}
```

**2. Qualifying by Name**:

- You can specify a bean by its name directly during injection, without using `@Qualifier`.
- **Example**:

```
@Autowired
@Qualifier("serviceA")
private Service service;
```

- You can also inject by name directly if you prefer.

In summary, `@Qualifier` is typically used to resolve ambiguity when multiple beans of the same type exist, and `@Primary` can be used to mark the default bean.

***11. What is the default scope in Spring boot?***

The default scope in Spring Boot (and Spring Framework) is **singleton**. This means that by default, Spring creates only one instance of a bean and uses that single instance across the entire Spring container. Every time the bean is needed, the same instance is injected.

```
@Service
public class MyService {
    // This will be a singleton by default
}
```

In this example, `MyService` will be created only once, and Spring will inject the same instance wherever it is required.

***12. What is HTTP status code 403? When is it implemented as expected to 401?***

**HTTP Status Code 403 — Forbidden:**

The server understands the request, but the client is **not authorized** to access the requested resource, even though authentication may have been provided. This means the server is refusing to process the request, typically due to insufficient permissions or access restrictions.

**403 is used when:**

- The client is **authenticated**, but does not have **permission** to access the resource.
- The server knows who the user is, but is deliberately blocking access due to permissions, roles, or restrictions.

**401 should be used when:**

- The client is **not authenticated** or does not provide valid authentication credentials (e.g., missing or incorrect token, session, or login details).

**Example:**

- **403**: A user is logged in but tries to access an admin page without admin privileges.
- **401**: A user tries to access a page without logging in, so the server requires authentication.

***13. Suppose you’re dealing with data such as Aadhar Number, PAN Number etc. Which HTTP method will you prefer for this call?***

**Use `POST` for Sensitive Data**

- Data is included in the **request body**, not the URL, reducing the risk of sensitive information being logged in browser history or server logs.
- `GET` parameters are visible in the URL, making them less secure.
- **Example:**

```
@PostMapping("/sensitive-endpoint")
public ResponseEntity<String> handleSensitiveData(@RequestBody SensitiveData requestData)
{     // Process sensitive data
return ResponseEntity.ok("Data processed");
}
```

**Avoid Using `GET` for Sensitive Data**

- `GET` should **not** be used for sensitive information like personal data because the query parameters in the URL can be logged or cached.

***14. Explain briefly about circuit breakers.***

A **Circuit Breaker** is a design pattern used to handle failures in distributed systems and prevent cascading failures. It acts like an electrical circuit breaker by monitoring service calls and “tripping” (stopping the calls) when the system detects a failure threshold has been exceeded.

1. **Closed State**: The circuit breaker allows calls to be made. If calls are successful, the breaker remains closed.
2. **Open State**: If the failure rate exceeds a threshold, the circuit breaker “opens” and stops further calls to the failing service, allowing time for recovery.
3. **Half-Open State**: After a timeout, the circuit breaker allows a limited number of test calls to check if the service has recovered. If these calls succeed, it closes again. If they fail, it remains open.

**Use Case:**

- Prevents overloading a failing service by stopping requests and letting it recover, improving overall system stability and resilience.

**Example:**

In a microservices architecture, if one service is down, the**Suppose you have a list of Employees containing name , age, emp id, and role. Sort them with name and age in Java 8.** circuit breaker prevents all other services from repeatedly trying to call it and failing, thus avoiding further strain.

# **TCS Java Developer Interview**

## **1. What is an Immutable class and How to create an Immutable class in Java?**

I’ve written a very detailed article on this, you should go through this and you’ll understand everything you need to know about Immutable classes and their creation:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/zGg58/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

**2. Suppose you have a list of Employees containing name , age, emp id, and role. Sort them with name and age in Java 8.**

```jsx
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    private String name;
    private int age;
    private int empId;
    private String role;
    
    // Constructor
    public Employee(String name, int age, int empId, String role) {
        this.name = name;
        this.age = age;
        this.empId = empId;
        this.role = role;
    }
    
    // Getters
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public int getEmpId() {
        return empId;
    }
    public String getRole() {
        return role;
    }
    
    // toString for printing
    @Override
    public String toString() {
        return "Employee{name='" + name + "', age=" + age + ", empId=" + empId + ", role='" + role + "'}";
    }
}

public class EmployeeSortingExample {
    public static void main(String[] args) {
        
        // List of Employees with Indian names
        List<Employee> employees = Arrays.asList(
            new Employee("Aarav", 30, 101, "Software Engineer"),
            new Employee("Vihaan", 28, 102, "Product Manager"),
            new Employee("Aarav", 25, 103, "Data Analyst"),
            new Employee("Ishita", 29, 104, "UI Designer"),
            new Employee("Ananya", 30, 105, "HR Manager")
        );
        
        // Sorting using streams
        List<Employee> sortedEmployees = employees.stream()
            .sorted(Comparator.comparing(Employee::getName)
                .thenComparing(Employee::getAge))
            .collect(Collectors.toList());
        
        // Printing the sorted list
        sortedEmployees.forEach(System.out::println);
    }
}
```

**Output:**

```jsx
Employee{name='Aarav', age=25, empId=103, role='Data Analyst'}
Employee{name='Aarav', age=30, empId=101, role='Software Engineer'}
Employee{name='Ananya', age=30, empId=105, role='HR Manager'}
Employee{name='Ishita', age=29, empId=104, role='UI/UX Designer'}
Employee{name='Vihaan', age=28, empId=102, role='Product Manager'}
```

**3. What are the differences between Hashset vs Linked Hashset?**

![](https://df58ssq2ibv83z.archive.ph/zGg58/c3d194a4daed2d9c7187aebc79183e82da2aee07.webp)

## **4. Is there any collection in Java that supports key-value pairs and keeps the keys in sorted order?**

Yes, in Java, we have the **TreeMap** that supports key-value pairs and ensures that the keys are always sorted.

It uses a **red-black tree** under the hood, which ensures that the keys are sorted in their **natural order** (if the key class implements `Comparable`) or according to a **custom comparator** that you can provide during the TreeMap's creation.

Key operations like `put()`, `get()`, and `remove()` have a time complexity of **O(log n)** because of the red-black tree structure.

Additionally, TreeMap offers methods like `firstKey()`, `lastKey()`, `higherKey()`, and `lowerKey()` to efficiently navigate through the sorted keys.

## **5. What happens when you try to insert the above discussed employee object in Treemap?**

The `Employee` class does not implement `Comparable`, and no custom comparator is provided.

Attempting to insert `Employee` objects into a `TreeMap` as keys will result in a runtime exception:

```
TreeMap<Employee, String> treeMap = new TreeMap<>();
treeMap.put(new Employee("Aarav", 30, 101, "Software Engineer"), "First");
treeMap.put(new Employee("Vihaan", 28, 102, "Product Manager"), "Second");
```

**Exception:**

```
Exception in thread "main" java.lang.ClassCastException: Employee cannot be cast to Comparable
```

This happens because **TreeMap** requires a way to compare keys to maintain the sorted order.

You can fix the above error using either of the two methods mentioned below:

## **Solution 1: Implement Comparable in the Employee Class**

You can modify the `Employee` class to implement the `Comparable` interface and define the sorting logic inside the `compareTo` method.

**Modified Employee Class:**

```
class Employee implements Comparable<Employee> {
    private String name;
    private int age;
    private int empId;
    private String role;

    // Constructor, Getters, and toString() remain the same...
    @Override
    public int compareTo(Employee other) {
        // Sort by name, then by age
        int nameComparison = this.name.compareTo(other.name);
        if (nameComparison != 0) {
            return nameComparison;
        }
        return Integer.compare(this.age, other.age);
    }
}
```

**Example**

```
TreeMap<Employee, String> treeMap = new TreeMap<>();
treeMap.put(new Employee("Aarav", 30, 101, "Software Engineer"), "First");
treeMap.put(new Employee("Vihaan", 28, 102, "Product Manager"), "Second");
treeMap.put(new Employee("Aarav", 25, 103, "Data Analyst"), "Third");

treeMap.forEach((key, value) -> System.out.println(key + " -> " + value));
```

**Output:**

```
Employee{name='Aarav', age=25, empId=103, role='Data Analyst'} -> Third
Employee{name='Aarav', age=30, empId=101, role='Software Engineer'} -> First
Employee{name='Vihaan', age=28, empId=102, role='Product Manager'} -> Second
```

## **Solution 2: Use a Custom Comparator**

If you don’t want to modify the `Employee` class, you can provide a custom comparator when creating the TreeMap.

**Example**

```
TreeMap<Employee, String> treeMap = new TreeMap<>(
    Comparator.comparing(Employee::getName)
              .thenComparing(Employee::getAge)
);

treeMap.put(new Employee("Aarav", 30, 101, "Software Engineer"), "First");
treeMap.put(new Employee("Vihaan", 28, 102, "Product Manager"), "Second");
treeMap.put(new Employee("Aarav", 25, 103, "Data Analyst"), "Third");

treeMap.forEach((key, value) -> System.out.println(key + " -> " + value));
```

**Output:**

```
Employee{name='Aarav', age=25, empId=103, role='Data Analyst'} -> Third
Employee{name='Aarav', age=30, empId=101, role='Software Engineer'} -> First
Employee{name='Vihaan', age=28, empId=102, role='Product Manager'} -> Second
```

**6. What are the differences between wait() and sleep()?**

![](https://df58ssq2ibv83z.archive.ph/zGg58/071149c92d5b06e9c271e3b670048d8b0ab38999.webp)

## **7. What are the bean scopes available in Spring?**

In Spring, **bean scopes** determine the lifecycle and visibility of beans in the Spring container.

Below are the main **bean scopes** available in Spring:

## **1. Singleton (Default Scope):**

- A single instance of the bean is created for the entire Spring container. All requests for the bean will return the same instance.
- **Usage**: Default scope if no other scope is specified.
- **Example**:

```
@Scope("singleton")
@Component
public class MyBean
{
...
}
```

## **2. Prototype:**

- A new instance of the bean is created each time it is requested from the Spring container. Each bean request results in a fresh instance.
- **Usage**: Useful when you need a new instance of the bean every time.
- **Example**:

```
@Scope("prototype")
@Component
public class MyBean
{
...
}
```

## **3. Request (Web Application Scope):**

- A new instance of the bean is created for each HTTP request. The bean is valid for the duration of a single HTTP request.
- **Usage**: Useful in web applications where you need a bean tied to the lifecycle of a single HTTP request.
- **Example**:

```
@Scope("request")
@Component
public class MyBean
{
...
}
```

## **4. Session (Web Application Scope):**

- A new instance of the bean is created for each HTTP session. The bean is valid for the duration of a single HTTP session.
- **Usage**: Useful in web applications where you need a bean tied to the lifecycle of an HTTP session.
- **Example**:

```
@Scope("session")
@Component
public class MyBean
{
...
}
```

## **5. Application (Web Application Scope):**

- A new instance of the bean is created for the entire lifecycle of the `ServletContext`. The bean is valid for the duration of the application.
- **Usage**: Useful when you want a bean to be shared across all requests and sessions within a web application.
- **Example**:

```
@Scope("application")
@Component
public class MyBean
{
...
}
```

## **6. WebSocket Session (Custom Scope for WebSocket Applications):**

- WebSocket sessions don’t have a predefined Spring scope like others. However, you can manage WebSocket-specific data by using a custom approach. For example, you might use **`@SessionScope`** to manage the scope for WebSocket sessions or manage WebSocket connections programmatically.
- **Usage**: WebSocket connections typically require custom logic or the use of a custom scope.
- **Example**:

```
@Scope("session")
@Component
public class WebSocketSessionHandler {
    // Manage WebSocket session-related data
}
```

## **8. What is lazy loading?**

Lazy loading is a design pattern where an object or resource is not loaded or initialized until it is actually needed.

In Spring, this concept is used to delay the creation of beans until they are first referenced in the application, instead of initializing them at the application startup.

This can help optimize performance and reduce memory usage, especially in large applications with beans that are not always used.

In Spring, lazy loading can be enabled using the `@Lazy` annotation.

When you annotate a bean with`@Lazy`, Spring will not initialize that bean when the application context is created. Instead, it will create the bean only when it's required — for example, when it's injected into another bean or explicitly requested by the application.

**For example:**

```
@Lazy
@Component
public class MyBean {
    // Bean's properties and methods
}
```

Spring will delay its instantiation until it’s actually needed, rather than during application startup. This can help speed up startup time if you have a lot of beans, but only some of them are actively used.

However, it’s important to note that lazy loading can have a downside in some cases. If certain beans are essential to the application, or if the bean’s initialization is resource-intensive, relying too heavily on lazy loading might introduce delays at runtime, which could affect performance negatively.

## **9. What is cascading?**

**Cascading** refers to the automatic propagation of certain operations (like persist, delete, or update) from one entity to its related entities.

This means that when an operation is performed on a parent entity, it can automatically affect the child entities that are associated with it, depending on the cascade configuration.

When dealing with relationships between entities, you may have operations like saving, updating, or deleting an entity. By configuring **cascading**, you can specify that these operations should automatically be performed on related entities as well.

For example, if you have a `Parent` entity and a `Child` entity, and you delete the `Parent`, you might want to automatically delete all the associated `Child` entities as well. Cascading lets you do this without explicitly deleting each child entity.

## **Types of Cascade Operations:**

In JPA/Hibernate, the most common cascade operations are:

1. **CascadeType.PERSIST**: When the parent entity is saved or persisted, its associated child entities are also persisted automatically.
2. **CascadeType.MERGE**: When the parent entity is merged (i.e., updated), its associated child entities are also merged.
3. **CascadeType.REMOVE**: When the parent entity is deleted, its associated child entities are also deleted.
4. **CascadeType.REFRESH**: When the parent entity is refreshed from the database, its associated child entities are also refreshed.
5. **CascadeType.DETACH**: When the parent entity is detached (removed from the persistence context), its associated child entities are also detached.

Example of cascading in Hibernate/JPA:

```
@Entity
public class Parent
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    @OneToMany(cascade = CascadeType.ALL)
    private List<Child> children;
    // Getters and setters
}
@Entity
public class Child {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    // Getters and setters
}
```

In this example:

- The `Parent` entity has a one-to-many relationship with the `Child` entity.
- The `cascade = CascadeType.ALL` means that **all** operations (persist, merge, remove, refresh, and detach) will be cascaded from the `Parent` to its associated `Child` entities.
- If we persist or delete a `Parent` entity, the corresponding `Child` entities will also be persisted or deleted automatically.