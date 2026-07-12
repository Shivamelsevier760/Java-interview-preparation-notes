# Medium Interview Series (company questions) — Interview Q&A

> Auto-extracted from the notes in [`03-medium-series/`](../03-medium-series/) by [`scripts/extract_qa.mjs`](../scripts/extract_qa.mjs).
> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.

**676 answered questions** · **366 question prompts without recorded answers**

---

## 1. When to use 422 Unprocessable Entity instead of 400 Bad Request?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

**When to use:**

Think of `400` as *"The server can’t even parse your request"*, and `422` as *"The server parsed your request, but the content doesn’t make sense in context."*

**Example:**

```
@PostMapping("/register")
public ResponseEntity<?> register(@RequestBody @Valid UserDto userDto, BindingResult result) {
    if (result.hasErrors()) {
        Map<String, Object> errorResponse = new HashMap<>();
        errorResponse.put("status", 422);
        errorResponse.put("error", "Validation Failed");
        errorResponse.put("message", result.getAllErrors());
        errorResponse.put("timestamp", LocalDateTime.now());

        return ResponseEntity.unprocessableEntity().body(errorResponse);
    }

    userService.register(userDto);
    return ResponseEntity.ok().build();
}
```

**Client (curl):**

```
curl -X POST http://localhost:8080/register \
  -H "Content-Type: application/json" \
  -d '{"username":"abc", "email":"not-an-email"}'
```

---

## 2. A client sends a PUT request to update a resource. The server responds with 204 No Content. Why is this better than 200 OK?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Below are some of the reasons why `204 No Content` better than `200 OK` for a successful `PUT` update:

- The update is successful and there’s nothing more the client needs to know.
- It avoids sending a redundant or empty response body.
- Helps optimize performance, especially in high-traffic APIs.

---

## 3. What’s the difference between 301 Moved Permanently and 308 Permanent Redirect in HTTP/1.1 and HTTP/2?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Both `301` and `308` are used to indicate permanent redirects, but they behave differently when it comes to preserving the HTTP method and body.

**Spring Boot redirect:**

```
@GetMapping("/old-endpoint")
public ResponseEntity<Void> redirect() {
    return ResponseEntity.status(HttpStatus.PERMANENT_REDIRECT)
                         .location(URI.create("/new-endpoint"))
                         .build();
}
```

**301 vs 308 in curl:**

```
#With 301, many clients (including older versions of curl) convert POST to GET, which may lead to data loss.
curl -X POST http://example.com/old-endpoint -L

#With 308, the method and body are preserved exactly, making it safer for POST/PUT redirects.
curl -X POST http://example.com/old-endpoint -L
```

- ***Use `308` to preserve POST/PUT methods in redirects.***

---

## 4. If a server receives a PATCH request but lacks support for the method, which status code should it return: 405, 501, or 400?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Firstly, let’s understand what each of the given status codes indicate:

- **405 Method Not Allowed**: Server understands the method but doesn’t allow it for the resource
- **501 Not Implemented**: Server doesn’t support the method at all
- **400 Bad Request**: Incorrect when the syntax is valid

So, if a server receives a `PATCH` request but lacks support for the method, it should **return 501 (Not Implemented)** if method is unknown.

- **Use `405` only if the method is supported but not allowed on that specific endpoint.**

---

## 5. You’re building an API Gateway. How do you differentiate between 502 Bad Gateway, 503 Service Unavailable, and 504 Gateway Timeout?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

When building an API Gateway, understanding the differences between **502 Bad Gateway**, **503 Service Unavailable**, and **504 Gateway Timeout** is crucial for debugging and managing API traffic. Here’s a breakdown:

---

## 6. What are the risks of always returning 200 OK in your API, even for errors?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Below are some of the the risks of always returning `200 OK` in your API, even for errors:

- Misleads client into thinking request was successful
- Violates REST principles
- Breaks automated clients that rely on status codes
- Increases debugging complexity
- Prevents effective caching and monitoring

***Always align HTTP status codes with the actual outcome of the request.***

**Bad practice:**

```
@PostMapping("/login")
public ResponseEntity<?> login(@RequestBody LoginDto dto) {
    if (!authService.authenticate(dto)) {
        // Bad idea: 200 OK with error message
        return ResponseEntity.ok("Invalid credentials");
    }
    return ResponseEntity.ok("Success");
}
```

**Better:**

```
return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                      .body("Invalid credentials"); // 401
```

---

## 7. You’re implementing rate limiting. Why is 429 Too Many Requests more appropriate than 503 Service Unavailable?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Below are the some of the reasons why`429 Too Many Requests`is more appropriate than `503 Service Unavailable:`

- `503` means **server issues** (overload/maintenance)
- `429` specifically signals **client-side overuse**
- `429` allows you to include `Retry-After` header to inform retry time

**`*429` provides a clear signal that the client is being throttled.***

**Spring Rate Limiting with Bucket4j Example:**

```
@RateLimiter(name = "basic")
@GetMapping("/api")
public ResponseEntity<String> callApi() {
    return ResponseEntity.ok("API accessed");
}
```

**On exceeding limit:**

```
{
  "status": 429,
  "message": "Too many requests"
}
```

**Add `Retry-After` header:**

```
return ResponseEntity.status(HttpStatus.TOO_MANY_REQUESTS)
                     .header("Retry-After", "60")
                     .body("Rate limit exceeded. Try again later.");
```

---

## 8. Can a 304 Not Modified response include a body? If not, why?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

No, `304 Not Modified` must not include a body.

- It’s designed to tell the client: “Use your cached version.”
- A body would defeat the purpose of reducing data transfer

***Only headers (e.g., ETag, Cache-Control) are returned with 304 responses.***

**Spring Example:**

```
@GetMapping("/image")
public ResponseEntity<byte[]> getImage(@RequestHeader("If-None-Match") String etag) {
    String currentEtag = "abc123";

if (etag != null && etag.equals(currentEtag)) {
        return ResponseEntity.status(HttpStatus.NOT_MODIFIED).eTag(currentEtag).build();  // 304
    }
    byte[] content = fetchImage();
    return ResponseEntity.ok().eTag(currentEtag).body(content);
}
```

---

## 9. A client sends invalid credentials. What’s the difference between 401 Unauthorized and 403 Forbidden?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

**Example:**

```
@GetMapping("/admin")
public ResponseEntity<?> adminEndpoint(@RequestHeader("Authorization") String token) {
    if (!jwtService.isValid(token)) {
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid token"); // 401
    }
    if (!jwtService.hasRole(token, "ADMIN")) {
        return ResponseEntity.status(HttpStatus.FORBIDDEN).body("Access denied");    // 403
    }
    return ResponseEntity.ok("Welcome Admin");
}
```

---

## 10. Why should you avoid using 302 Found for API redirects involving POST requests?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Below are the reasons why you avoid should using `302 Found` for API redirects involving POST requests:

- `302` might cause the client to change POST to GET, losing the request body
- Non-standard behavior across browsers and clients

Instead, use:

- `307 Temporary Redirect` → Preserves the method
- `308 Permanent Redirect` → Same, but for permanent moves

***APIs should favor 307/308 over 302 to preserve method semantics.***

**Bad:**

```
@PostMapping("/upload")
public String upload() {
    // Redirects after POST using 302 → may lose POST data
    return "redirect:/status";
}
```

**Better:**

```
@PostMapping("/upload")
public ResponseEntity<Void> upload() {
    return ResponseEntity.status(HttpStatus.TEMPORARY_REDIRECT)
                         .location(URI.create("/status"))
                         .build();  // 307
}
```

---

## 11. How can you dynamically route requests to different backend services at runtime in Spring Cloud Gateway?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Dynamic routing allows API Gateway to determine the backend service at runtime, instead of hardcoding routes in `application.yml`.

This can be done using RouteLocator:

```
@Configuration
public class DynamicRouteConfig {

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("dynamic_route", r -> r
                .path("/service/**")
                ..filters(f -> f.rewritePath("^/service/(?<segment>.*)", "/${segment}"))
                .uri("lb://DYNAMIC-SERVICE"))
            .build();
    }
}
```

- The service name is resolved dynamically using a Load Balancer (`lb://`).
- Requests like `/service/user` will be routed to `/user` in the respective service.

---

## 12. How do you handle request aggregation in API Gateway when multiple microservices must be queried?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Request aggregation is essential when an API requires data from multiple microservices.

This can be done using WebClient for parallel calls:

```
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.MediaType;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import java.nio.charset.StandardCharsets;
import java.util.Map;

@Component
public class AggregationFilter implements GlobalFilter, Ordered {

    private final WebClient.Builder webClientBuilder;
    private final ObjectMapper objectMapper;

    public AggregationFilter(WebClient.Builder webClientBuilder, ObjectMapper objectMapper) {
        this.webClientBuilder = webClientBuilder;
        this.objectMapper = objectMapper;
    }

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        WebClient webClient = webClientBuilder.build();

        // Fetch data from multiple microservices in parallel
        Mono<String> userDetails = webClient.get().uri("lb://user-service/user/123")
            .retrieve().bodyToMono(String.class);

        Mono<String> orderDetails = webClient.get().uri("lb://order-service/orders/123")
            .retrieve().bodyToMono(String.class);

        return Mono.zip(userDetails, orderDetails).flatMap(tuple -> {
            try {
                Map<String, Object> aggregatedData = Map.of(
                    "user", objectMapper.readTree(tuple.getT1()),
                    "orders", objectMapper.readTree(tuple.getT2())
                );
                String aggregatedResponse = objectMapper.writeValueAsString(aggregatedData);

                ServerHttpResponse response = exchange.getResponse();
                response.getHeaders().setContentType(MediaType.APPLICATION_JSON);
                return response.writeWith(Mono.fromSupplier(() ->
                    response.bufferFactory().wrap(aggregatedResponse.getBytes(StandardCharsets.UTF_8))
                ));
            } catch (Exception e) {
                return Mono.error(e);
            }
        });
    }

    @Override
    public int getOrder() {
        return -1;
    }
}
```

- This fetches user and order details in parallel and aggregates them before returning a response.

---

## 13. How do you implement dynamic rate limiting per user using API Gateway?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

```
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import java.time.Duration;
import java.util.Collections;

@Component
public class UserRateLimiterFilter implements GlobalFilter, Ordered {

    private final StringRedisTemplate redisTemplate;
    private static final String RATE_LIMIT_SCRIPT =
        "local current = redis.call('INCR', KEYS[1]) " +
        "if tonumber(current) == 1 then " +
        "  redis.call('EXPIRE', KEYS[1], ARGV[1]) " +
        "end " +
        "if tonumber(current) > tonumber(ARGV[2]) then " +
        "  return 0 " +
        "end " +
        "return 1";

    private static final int TIME_WINDOW_SECONDS = 10;
    private static final int REQUEST_LIMIT = 5;

    public UserRateLimiterFilter(StringRedisTemplate redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String userId = exchange.getRequest().getHeaders().getFirst("X-User-ID");

        if (userId == null || userId.isBlank()) {
            return setErrorResponse(exchange.getResponse(), HttpStatus.BAD_REQUEST, "Missing X-User-ID header");
        }

        String key = "rate-limit:" + userId;
        Long allowed = redisTemplate.execute(
                (connection, keySerializer, valueSerializer) ->
                        (Long) connection.scriptingCommands().eval(
                                RATE_LIMIT_SCRIPT.getBytes(),
                                Collections.singletonList(keySerializer.serialize(key)),
                                new byte[][]{
                                        valueSerializer.serialize(String.valueOf(TIME_WINDOW_SECONDS)),
                                        valueSerializer.serialize(String.valueOf(REQUEST_LIMIT))
                                }),
                Collections.singletonList(key)
        );

        if (allowed == null || allowed == 0) {
            return setErrorResponse(exchange.getResponse(), HttpStatus.TOO_MANY_REQUESTS, "Rate limit exceeded");
        }

        return chain.filter(exchange);
    }

    private Mono<Void> setErrorResponse(ServerHttpResponse response, HttpStatus status, String message) {
        response.setStatusCode(status);
        return response.setComplete();
    }

    @Override
    public int getOrder() {
        return Ordered.LOWEST_PRECEDENCE;
    }
}
```

- This filter dynamically enforces rate limits per user.

---

## 14. What is a shadow deployment in API Gateway, and how can you implement it?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Shadow deployment allows testing a new version of an API without impacting live traffic.

Requests are sent both to the current and new version, but only the original response is returned.

**Implementation:**

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import java.net.URI;
import java.util.concurrent.ThreadLocalRandom;

@Component
public class ShadowTrafficFilter implements GlobalFilter, Ordered {

    private static final Logger logger = LoggerFactory.getLogger(ShadowTrafficFilter.class);
    private final WebClient webClient = WebClient.create();

    @Value("${shadow.traffic.sampling:20}") // Default: 20% of requests go to shadow
    private int shadowSamplingRate;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String originalUri = exchange.getRequest().getURI().toString();
        String shadowUri = originalUri.replace("/v1/", "/v2/");

        if (shadowUri.equals(originalUri)) {
            return chain.filter(exchange); // No modification, proceed normally
        }

        // Only send shadow traffic for a percentage of requests (default 20%)
        if (ThreadLocalRandom.current().nextInt(100) < shadowSamplingRate) {
            webClient.method(exchange.getRequest().getMethod())
                     .uri(URI.create(shadowUri))
                     .retrieve()
                     .bodyToMono(Void.class)
                     .doOnError(error -> logger.error("Shadow request failed: {}", error.getMessage()))
                     .subscribe();
        }

        return chain.filter(exchange); // Proceed with the original request
    }

    @Override
    public int getOrder() {
        return -1;
    }
}
```

---

## 15. How would you implement multi-tenancy in API Gateway?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

For multi-tenancy, API Gateway must route requests dynamically based on tenant ID.

**Approach:**

- Store tenant configuration in a database or config server.
- Fetch tenant-specific routing rules dynamically.
- Rewrite URLs and inject tenant context in headers.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;
import org.springframework.core.io.buffer.DataBuffer;

import java.nio.charset.StandardCharsets;

@Component
public class TenantRoutingFilter implements GlobalFilter, Ordered {

    private static final Logger logger = LoggerFactory.getLogger(TenantRoutingFilter.class);
    private final TenantService tenantService;

    @Value("${multi-tenancy.path-format:/tenant/{tenantId}}")
    private String pathFormat;

    public TenantRoutingFilter(TenantService tenantService) {
        this.tenantService = tenantService;
    }

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String tenantId = exchange.getRequest().getHeaders().getFirst("X-Tenant-ID");

        if (tenantId == null || tenantId.isBlank()) {
            tenantId = exchange.getRequest().getQueryParams().getFirst("tenantId"); // Fallback to query param
        }

        if (tenantId == null || tenantId.isBlank()) {
            return setErrorResponse(exchange.getResponse(), HttpStatus.BAD_REQUEST, "Missing X-Tenant-ID header");
        }

        if (!tenantService.isValidTenant(tenantId)) {
            logger.warn("Unauthorized access attempt with invalid tenant ID: {}", tenantId);
            return setErrorResponse(exchange.getResponse(), HttpStatus.FORBIDDEN, "Invalid Tenant ID");
        }

        ServerHttpRequest request = exchange.getRequest().mutate()
            .path(pathFormat.replace("{tenantId}", tenantId) + exchange.getRequest().getPath().toString())
            .header("X-Tenant-Context", tenantId)
            .build();

        return chain.filter(exchange.mutate().request(request).build());
    }

    private Mono<Void> setErrorResponse(ServerHttpResponse response, HttpStatus status, String message) {
        response.setStatusCode(status);
        byte[] bytes = ("{\"error\": \"" + message + "\"}").getBytes(StandardCharsets.UTF_8);
        DataBuffer buffer = response.bufferFactory().wrap(bytes);
        response.getHeaders().setContentType(MediaType.APPLICATION_JSON);
        return response.writeWith(Mono.just(buffer));
    }

    @Override
    public int getOrder() {
        return -1;
    }
}
```

---

## 16. How can API Gateway enforce zero-trust security principles?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

- **Mutual TLS (mTLS):** Enforce authentication **for both client & server**.
- **OAuth2/JWT-based authentication:** No implicit trust, every request must be validated.
- **Dynamic access control:** API Gateway should **verify user permissions** for each request.
- **Runtime anomaly detection:** Detect **unusual request patterns** in real time.

---

## 17. How does API Gateway handle caching, and what problems can arise?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

API Gateway can cache responses using a **distributed cache** (e.g., Redis).

**Problems:**

- **Stale data**: Need cache invalidation strategies.
- **Incorrect granularity**: Caching too much or too little.
- **Security risk**: Caching sensitive data (avoid caching auth tokens).

---

## 18. How can API Gateway track request tracing across microservices?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Use distributed tracing (Zipkin, OpenTelemetry):

- Inject trace ID in request headers:

```
String traceId = UUID.randomUUID().toString();
ServerHttpRequest request = exchange.getRequest().mutate()
    .header("X-Trace-ID", traceId)
    .build();
```

---

## 19. How would you prevent replay attacks in API Gateway?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

- Use a nonce (one-time token) for each request.
- Reject duplicate requests within a time window using Redis.

---

## 20. How do you implement blue-green deployments in API Gateway?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Use **weighted routing**:

```
routes:
  - id: blue-service
    uri: http://blue-version
    weight: 90
  - id: green-service
    uri: http://green-version
    weight: 10
```

---

## 21. Define the Project Structure

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Once the project is created, define a clean and organized structure. A typical Spring Boot project follows this pattern:

**1. Controller Layer (controller):**

- Contains all the REST endpoints.
- Uses `@RestController` to handle HTTP requests and responses.
- **Example:** `UserController.java` manages routes like `/api/users`.

**2. Service Layer (service)**

- Contains business logic.
- Uses `@Service` to define reusable business functions.
- **Example:** `UserService.java` handles data processing and complex logic.

**3. Repository Layer (repository)**

- Handles data access using Spring Data JPA.
- Uses `@Repository` to abstract database operations.
- **Example:** `UserRepository.java` extends `JpaRepository`.

**4. Model Layer (model)**

- Contains entity classes that map to database tables.
- Uses `@Entity` to define JPA entities.
- **Example:** `User.java` maps to the `user` table.

**5. Main Class**

- `@SpringBootApplication` initializes the Spring Boot context.
- **Example:** `SpringBootRestApplication.java` is the entry point of the app.

**6. Resources**

- `application.properties` – Configures the app (database URL, logging, etc.).
- `schema.sql` – (Optional) Initializes database schema if needed.

**7. Test Layer (test)**

- Holds unit and integration tests.
- Follows the same package structure as `main`.

---

## 22. How would you implement error handling in an RSocket service? What happens if the client or server disconnects during a request-response interaction?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

RSocket provides built-in error handling mechanisms and allows developers to implement custom handling to ensure resilience.

---

## 23. What are some common challenges you face when using RSocket in a microservices architecture?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

RSocket is great for low-latency, reactive, and bi-directional communication, but it comes with some challenges when integrating it into a microservices architecture. Let me break them down one by one.

---

## 24. Explain the concept of backpressure in RSocket. How does it handle it differently compared to other protocols like HTTP/2?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Backpressure is a flow-control mechanism that ensures a fast producer does not overwhelm a slow consumer. It helps maintain system stability and prevents memory overflows when handling large amounts of data.

In traditional request-response models like HTTP/1.1, the server sends data as fast as possible, assuming the client can handle it. Since HTTP/1.1 lacks built-in backpressure, this can overwhelm the consumer.

In contrast, reactive systems (like RSocket) use the Reactive Streams specification, where consumers can request data at their own pace, ensuring a controlled and efficient data flow.

---

## 25. How Does RSocket Handle Backpressure?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

RSocket is fully reactive and natively supports backpressure through the Reactive Streams specification.

Unlike protocols like HTTP/2, where flow control is handled at the transport level, RSocket decouples transport flow control from application logic, allowing fine-grained control over data flow.

While RSocket runs over TCP, it does not rely on TCP’s backpressure alone; instead, it implements reactive backpressure at the application level for optimal performance.

---

## 26. If you need to deploy an RSocket service in Kubernetes, how would you scale it efficiently to handle a large number of connections?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

To deploy and scale an RSocket service efficiently in Kubernetes (K8s) while handling a large number of connections, you need to address key concerns like load balancing, connection persistence, scaling strategies, and resource optimization.

Here’s how you can achieve this:

---

## 27. How does RSocket handle retries if a request fails?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

RSocket enables resilient communication by allowing client-side retries, resumable sessions, and circuit breakers to handle failures efficiently.

---

## 28. Can RSocket work in a serverless environment (AWS Lambda, Google Cloud Functions)?

*Source: [`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*

Yes, RSocket can work in a serverless environment (AWS Lambda, Google Cloud Functions), but there are several challenges due to the nature of serverless architectures.

---

## 29. What is the Java Memory Model?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The Java Memory Model (JMM) defines how threads interact through memory and what behaviors are allowed in a multithreaded environment. It specifies the interaction between the main memory and the local memory (CPU cache).

Key Points:

- The JMM ensures visibility of changes to variables across threads.
- It defines the rules for synchronizing access to memory.
- It is important for understanding how to write thread-safe code.

---

## 30. Describe the different parts of the Java heap memory.

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Java heap memory is divided into several parts:

1. Young Generation:

- Eden Space: Where new objects are allocated.
- Survivor Spaces (S0 and S1): Objects that survive garbage collection in Eden are moved here.

2. Old Generation (Tenured):

- Objects that survive multiple garbage collection cycles in the Young Generation are promoted here.

3. Metaspace (formerly PermGen):

- Stores class metadata and other static content.

Example:

```
public class MemoryAllocationExample {
    public static void main(String[] args) {
        // Object allocation in Eden space
        Object obj1 = new Object();
        Object obj2 = new Object();

        // Objects may be moved to Survivor space after GC
        System.gc();

        // Long-lived objects may be moved to Old Generation
        List<Object> longLivedObjects = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            longLivedObjects.add(new Object());
        }
    }
}
```

---

## 31. What is garbage collection in Java?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Garbage collection (GC) is the process by which the JVM automatically reclaims memory by deleting objects that are no longer reachable in the application.

Key Points:

- It helps in managing memory efficiently by removing unused objects.
- The main types of GC algorithms are Serial, Parallel, CMS (Concurrent Mark-Sweep), and G1 (Garbage-First).

---

## 32. How does the garbage collector know which objects to collect?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The garbage collector uses several algorithms to determine which objects are no longer reachable:

1. Reference Counting:

- Counts references to each object, but can lead to issues with cyclic references.

2. Tracing (Mark and Sweep):

- Marks all reachable objects and then sweeps through the heap to collect unmarked objects.

3. Generational GC:

- Based on the generational hypothesis that most objects die young. It divides the heap into different generations (Young and Old).

---

## 33. Explain the concept of “Stop-the-world” in Java garbage collection.

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

“Stop-the-world” refers to the pause in application execution when the garbage collector runs. During this time, all application threads are stopped to allow the GC to perform its work.

Example:

```
public class StopTheWorldExample {
    public static void main(String[] args) {
        Runtime runtime = Runtime.getRuntime();
        System.out.println("Total Memory: " + runtime.totalMemory());
        System.out.println("Free Memory: " + runtime.freeMemory());

        // Trigger a GC
        System.gc();

        // GC may cause a stop-the-world pause
        System.out.println("Free Memory after GC: " + runtime.freeMemory());
    }
}
```

---

## 34. What are the different types of references in Java?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Java provides different types of references to manage memory more flexibly:

1. Strong Reference:

- Standard reference type that prevents the object from being collected.

2. Soft Reference:

- Used for memory-sensitive caches. Objects are collected only when the JVM runs out of memory.

3. Weak Reference:

- Used for implementing canonicalizing mappings. Objects are collected when there are no strong or soft references.

4. Phantom Reference:

- Used to schedule post-mortem cleanup actions. Objects are collected but the reference is enqueued.

Example:

```
import java.lang.ref.*;

public class ReferenceExample {
    public static void main(String[] args) {
        // Strong Reference
        String strongRef = new String("Strong Reference");

        // Soft Reference
        SoftReference<String> softRef = new SoftReference<>(new String("Soft Reference"));

        // Weak Reference
        WeakReference<String> weakRef = new WeakReference<>(new String("Weak Reference"));

        // Phantom Reference
        ReferenceQueue<String> queue = new ReferenceQueue<>();
        PhantomReference<String> phantomRef = new PhantomReference<>(new String("Phantom Reference"), queue);

        System.gc();

        // Soft reference might still be accessible if there's enough memory
        if (softRef.get() != null) {
            System.out.println("Soft Reference: " + softRef.get());
        }

        // Weak reference will likely be collected
        if (weakRef.get() == null) {
            System.out.println("Weak Reference has been collected");
        }

        // Phantom reference is always null
        System.out.println("Phantom Reference: " + phantomRef.get());
    }
}
```

---

## 35. What is the difference between the finalize() method and the Cleaner/PhantomReference?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

`finalize()` Method:

- Called by the garbage collector before an object is collected.
- Deprecated due to unpredictable behavior and performance issues.

Cleaner/PhantomReference:

- Introduced to provide a more reliable way to clean up resources.
- `Cleaner` can be used to register cleanup actions.
- `PhantomReference` allows actions to be scheduled after the object is collected.

Example:

```
import java.lang.ref.Cleaner;

public class CleanerExample {
    private static final Cleaner cleaner = Cleaner.create();

    static class Resource implements Runnable {
        @Override
        public void run() {
            System.out.println("Cleaning up resources...");
        }
    }

    public static void main(String[] args) {
        Cleaner.Cleanable cleanable = cleaner.register(new Object(), new Resource());

        System.gc();
    }
}
```

---

## 36. How does the JVM manage memory in terms of stack and heap?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

- Stack Memory: Used for storing method call frames, including local variables and function call details. Each thread has its own stack.
- Heap Memory: Used for dynamic memory allocation of objects. Shared among all threads.

Example:

```
public class StackHeapExample {
    public static void main(String[] args) {
        int localVariable = 42; // Stored in stack

        MyObject obj = new MyObject(); // Stored in heap
        obj.display();
    }
}

class MyObject {
    void display() {
        System.out.println("Hello, World!");
    }
}
```

---

## 37. What is a memory leak in Java, and how can it be prevented?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

A memory leak in Java occurs when objects that are no longer needed are not properly garbage collected because references to them still exist.

Prevention:

- Ensure references to unused objects are removed.
- Use tools like Eclipse MAT or VisualVM to analyze heap dumps.
- Be cautious with static fields, collections, and event listeners.

Example:

```
public class MemoryLeakExample {
    private static List<Object> leakList = new ArrayList<>();

    public static void main(String[] args) {
        for (int i = 0; i < 10000; i++) {
            leakList.add(new Object());
        }
    }
}
```

---

## 38. Explain the concept of the OutOfMemoryError in Java.

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

`OutOfMemoryError` is thrown when the JVM cannot allocate an object due to insufficient memory.

Causes:

- Excessive memory usage.
- Memory leaks.
- Inadequate heap size configuration.

Example:

```
public class OutOfMemoryErrorExample {
    public static void main(String[] args) {
        try {
            List<int[]> arrays = new ArrayList<>();
            while (true) {
                arrays.add(new int[1000000]);
            }
        } catch (OutOfMemoryError e) {
            System.err.println("Out of memory error caught: " + e.getMessage());
        }
    }
```

---

## 39. What is Docker and why is it useful for Java developers?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Docker is an open-source platform that automates the deployment, scaling, and management of applications within lightweight containers. For Java developers, Docker provides an isolated environment that ensures consistent behavior across different stages of development, testing, and production. It simplifies dependency management, eliminates environment discrepancies, and enhances CI/CD workflows.

---

## 40. What are the key components of Docker architecture?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The key components of Docker architecture include:

- Docker Client: The command-line interface to interact with Docker.
- Docker Daemon (dockerd): The background service running on the host machine that manages Docker objects (images, containers, networks, and volumes).
- Docker Images: Read-only templates used to create containers, often built from a Dockerfile.
- Docker Containers: The runnable instances of Docker images, containing everything needed to run an application.
- Docker Registry: A repository for storing and distributing Docker images, such as Docker Hub

---

## 41. What is a Dockerfile and how is it used?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

A Dockerfile is a script composed of a series of instructions to assemble a Docker image. It defines the base image, application dependencies, environment variables, and commands to run the application.

**Example**:

```
# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Compile and package the application using Maven
RUN ./mvnw package

# Specify the JAR file to run
CMD ["java", "-jar", "target/my-java-app.jar"]
```

---

## 42. How do you create and run a Docker image for a Java application?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To create a Docker image, write a Dockerfile and then use the `docker build` command. To run the image, use the `docker run` command.

**Example**:

```
# Build the Docker image
docker build -t my-java-app .

# Run the Docker container
docker run -d -p 8080:8080 my-java-app
```

This command builds an image named `my-java-app` and runs a container mapping port 8080 of the host to port 8080 of the container.

---

## 43. How do you use COPY and ADD instructions in a Dockerfile?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Both `COPY` and `ADD` instructions are used to copy files and directories into a Docker image, but they have different functionalities:

- `COPY`: Copies files and directories from the host to the container.
- `ADD`: Offers all the features of `COPY`, but also supports extracting TAR files and downloading files from URLs.

Example:

```
COPY myapp.jar /app/
ADD http://example.com/config.yaml /app/config.yaml
```

---

## 44. What is docker-compose and how is it useful for Java developers?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

`docker-compose` is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application’s services, networks, and volumes, making it easier to manage complex applications that require multiple containers.

**Example**: `docker-compose.yml`:

```
version: '3'
services:
  app:
    image: my-java-app
    ports:
      - "8080:8080"
    depends_on:
      - db
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: testdb
```

Running with Docker Compose:

```
docker-compose up
```

---

## 45. How do you persist data in Docker containers?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To persist data in Docker containers, use Docker volumes or bind mounts. Volumes are managed by Docker and are suitable for data persistence across container lifecycles.

**Example**:

```
docker run -d -p 8080:8080 -v mydata:/var/lib/mysql mysql:5.7
```

This command creates a named volume `mydata` and mounts it to `/var/lib/mysql` inside the container, ensuring data persistence.

---

## 46. What is the difference between Docker volumes and bind mounts?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

- Docker Volumes: Managed by Docker, stored in a location controlled by Docker, and preferred for persisting data.
- Bind Mounts: Directly map a directory or file from the host filesystem to the container, providing direct access to the host’s files.

**Example**:

```
# Volume
docker run -v myvolume:/app/data my-java-app

# Bind Mount
docker run -v /path/on/host:/app/data my-java-app
```

---

## 47. How do you share a Docker image with others?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To share a Docker image, push it to a Docker registry, such as Docker Hub.

**Example**:

1. Tag the image:

```
docker tag my-java-app username/my-java-app:latest
```

2. Push the image:

```
docker push username/my-java-app:latest
```

3. Others can pull the image using:

```
docker pull username/my-java-app:latest
```

---

## 48. How can you optimize the size of Docker images for Java applications?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To optimize Docker image size for Java applications:

- Use multi-stage builds to separate the build environment from the runtime environment.
- Use a minimal base image, such as `alpine`.
- Remove unnecessary files and dependencies after building the application.

**Example**:

```
# Stage 1: Build
FROM maven:3.6.3-jdk-11 as builder
WORKDIR /app
COPY . /app
RUN mvn clean package

# Stage 2: Runtime
FROM openjdk:11-jre-slim
WORKDIR /app
COPY --from=builder /app/target/my-java-app.jar /app/
CMD ["java", "-jar", "my-java-app.jar"]
```

---

## 49. What are Docker networks and why are they important?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Docker networks allow containers to communicate with each other, providing isolation and security for applications. Docker supports different types of networks:

- Bridge Network: The default network, suitable for containers running on a single host.
- Host Network: Removes network isolation between the container and the Docker host, using the host’s networking stack.
- Overlay Network: Enables communication between Docker containers across different hosts in a Docker Swarm or Kubernetes cluster.

**Example**:

```
# Create a custom bridge network
docker network create mynetwork

# Run containers on the custom network
docker run -d --network mynetwork --name app my-java-app
docker run -d --network mynetwork --name db mysql:5.7
```

---

## 50. How do you debug a running Docker container?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To debug a running Docker container, you can use several commands:

- `docker logs [container_id]`: View the logs of a container.
- `docker exec -it [container_id] /bin/bash`: Access the container's shell interactively.
- `docker inspect [container_id]`: Retrieve detailed information about a container.

Example:

```
# View container logs
docker logs my-java-app

# Access the container's shell
docker exec -it my-java-app /bin/bash

# Inspect container details
docker inspect my-java-app
```

---

## 51. What is Docker Swarm and how does it differ from Kubernetes?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Docker Swarm is Docker’s native clustering and orchestration tool that enables the deployment and management of a swarm of Docker engines in a distributed environment. It provides features like scaling, load balancing, and service discovery.

Differences from Kubernetes:

- Complexity: Docker Swarm is easier to set up and use, while Kubernetes offers more advanced features and flexibility.
- Scaling: Kubernetes provides more robust and automatic scaling options.
- Ecosystem: Kubernetes has a larger ecosystem and community support with more integrations and tools.

**Example**:

```
# Initialize a Docker Swarm
docker swarm init

# Deploy a stack in the Swarm
docker stack deploy -c docker-compose.yml mystack
```

---

## 52. How can you secure Docker containers?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To secure Docker containers, follow these best practices:

- Use official and trusted images.
- Regularly scan images for vulnerabilities.
- Run containers with the least privileges (use non-root users).
- Limit container capabilities using seccomp and AppArmor profiles.
- Use Docker secrets to manage sensitive information.
- Monitor container activity and apply network security policies.

**Example**:

```
# Use a non-root user in a Dockerfile
FROM openjdk:11-jre-slim
RUN useradd -ms /bin/bash javauser
USER javauser

# Run container with limited capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE my-java-app
```

---

## 53. What are multi-stage builds in Docker, and how do they benefit Java applications?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Multi-stage builds in Docker allow you to use multiple `FROM` statements in a Dockerfile, enabling the use of intermediate images to create the final image. This reduces the size of the final image by excluding unnecessary build tools and dependencies.

Benefits for Java Applications:

- Smaller image size by excluding build-time dependencies.
- Enhanced security by including only the runtime environment.
- Easier to maintain and update Dockerfiles.

**Example**:

```
# Stage 1: Build
FROM maven:3.6.3-jdk-11 as builder
WORKDIR /app
COPY . /app
RUN mvn clean package

# Stage 2: Runtime
FROM openjdk:11-jre-slim
WORKDIR /app
COPY --from=builder /app/target/my-java-app.jar /app/
CMD ["java", "-jar", "my-java-app.jar"]
```

---

## 54. What are differences Between Dockerization and Containerization

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Dockerization and containerization are often used interchangeably, but they have distinct meanings in the context of modern software development and deployment. Understanding these differences can help clarify how they are applied and their respective roles in application management.

**Containerization**

**Definition**: Containerization is a technology that allows you to package an application and its dependencies together in a standardized unit called a container. Containers abstract the application layer away from the operating system and infrastructure, ensuring consistency across multiple environments.

Key Points:

- Technology-Agnostic: Containerization is a general concept and can be implemented using various container technologies such as Docker, LXC (Linux Containers), rkt, and others.
- Isolation: Containers provide process and file system isolation, ensuring that applications run independently without interfering with each other.
- Efficiency: Containers are lightweight and share the host OS kernel, making them more efficient than traditional virtual machines (VMs) which require separate OS instances.

Example Technologies:

- Docker
- LXC
- rkt (CoreOS)

**Dockerization**

**Definition**: Dockerization specifically refers to the process of packaging an application and its dependencies into a Docker container. It involves creating a Dockerfile, building a Docker image, and running containers using Docker.

Key Points:

- Specific to Docker: Dockerization is a subset of containerization that uses Docker as the containerization platform.
- Docker Tools: Involves using Docker-specific tools and commands such as `docker build`, `docker run`, `docker-compose`, and `docker swarm`.
- Standardization: Docker provides a standardized environment and a vast ecosystem, making it the most popular containerization tool.

Example Process:

1. Create a Dockerfile: Define the application environment and dependencies

```
FROM openjdk:11-jre-slim
WORKDIR /app
COPY . /app
RUN ./mvnw package
CMD ["java", "-jar", "target/my-java-app.jar"]
```

2. Build the Docker Image: Use the Dockerfile to build the image.

```
docker build -t my-java-app .
```

3. Run the Docker Container: Run the container from the image.

```
docker run -d -p 8080:8080 my-java-app
```

---

## 55. When to Use RestTemplate?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

**Definition of RestTemplate:**

**RestTemplate** is a synchronous, blocking client provided by Spring Framework for consuming RESTful web services. It executes requests and waits until the response is returned. While simple and widely used, its blocking nature makes it less suitable for high-throughput or low-latency applications.

**Key Features of RestTemplate:**

- Synchronous and blocking.
- Easy to use for basic HTTP requests.
- Well-integrated with traditional Spring applications.

Despite the growing popularity of **WebClient**, **RestTemplate** continues to be a widely used option in many Spring Boot applications, especially in traditional, synchronous architectures. Below are scenarios where using **RestTemplate** is still valid and often preferable.

**1. Synchronous Applications**

If your application is designed as a synchronous, blocking system where each operation waits for the previous one to complete, **RestTemplate** is sufficient and simpler to use. Examples include:

- Legacy systems that do not utilize reactive or asynchronous paradigms.
- Internal tools or systems with low traffic and minimal scalability needs.

**2. Simple Use Cases**

For straightforward use cases like making one-off HTTP requests, downloading small files, or posting data to a service, **RestTemplate** offers ease of use:

- Quick implementation for CRUD operations.
- Integration with existing Spring MVC-based applications.

**3. Legacy Systems**

Many older applications were built before the advent of WebClient and heavily rely on RestTemplate. Refactoring these applications to use WebClient might require significant effort with minimal immediate benefits:

- Applications following a monolithic architecture.
- Systems without performance bottlenecks where non-blocking I/O is unnecessary.

**4. Limited Concurrency Requirements**

In applications with low concurrency requirements, where resource utilization is not a concern, **RestTemplate** is adequate:

- Internal enterprise applications with limited users.
- Batch jobs or ETL systems making periodic HTTP calls.

**5. Testing and Prototyping**

For quick prototyping or testing APIs, RestTemplate is often favored due to its simplicity and low setup overhead.

---

## 56. Why Was RestTemplate Widely Used?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

1. **Historical Significance**:
- **RestTemplate** was introduced early in the Spring ecosystem and became a standard for HTTP communication in Spring applications before the rise of reactive programming.
- It was the default choice for consuming REST APIs in Spring for years, and many developers are familiar with it.

**2. Ease of Use**:

- RestTemplate’s straightforward API allows developers to perform common HTTP operations like `GET`, `POST`, `PUT`, and `DELETE` with minimal configuration.

**3. Strong Ecosystem Support**:

Many Spring Boot tutorials, guides, and examples have used RestTemplate, ensuring that developers have access to abundant resources and community support.

**4. Synchronous Nature**:

- Its blocking behavior aligns naturally with traditional programming paradigms, making it intuitive for developers transitioning from desktop or monolithic applications to web services.

**5. Mature and Stable**:

- RestTemplate is a mature and stable library, making it a reliable choice for many use cases.

---

## 57. When to Use WebClient?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

**Definition of WebClient:**

**WebClient** is a non-blocking, reactive web client introduced as part of the Spring WebFlux framework. It is built to support asynchronous and streaming scenarios, making it ideal for applications requiring high concurrency and scalability.

**Key Features of WebClient:**

- Asynchronous and non-blocking.
- Supports both synchronous and reactive programming.
- Suitable for streaming and real-time scenarios.
- Built-in support for functional-style programming.

**WebClient** is a powerful tool introduced in the **Spring WebFlux** module, designed for handling asynchronous, non-blocking HTTP requests. Its versatility, efficiency, and modern design make it ideal for a wide range of applications. Below is a detailed discussion of scenarios where WebClient shines and is the recommended choice.

**1. Reactive and Non-Blocking Applications**

WebClient is the go-to choice when developing reactive applications. Reactive programming is designed to handle a large number of concurrent requests efficiently by leveraging non-blocking I/O. Use WebClient in the following cases:

- **Reactive APIs**: If your application uses **Reactor**, **RxJava**, or other reactive frameworks, WebClient integrates seamlessly.
- **Event-Driven Architectures**: Systems that rely on events, such as IoT platforms, benefit from the asynchronous capabilities of WebClient.

**Example**:

```
public Mono<User> fetchUser(String userId) {
    return WebClient.create()
        .get()
        .uri("https://api.example.com/users/{id}", userId)
        .retrieve()
        .bodyToMono(User.class);
}
```

**2. Microservices Communication**

In microservices architecture, services often need to communicate with one another. WebClient enables efficient, high-throughput inter-service communication. It allows:

- **Concurrent Requests**: Send multiple requests simultaneously without blocking threads.
- **Low-Latency Responses**: Handle real-time data with reduced response times.

**Example**:

```
public Flux<Order> fetchUserOrders(String userId) {
    return WebClient.create()
        .get()
        .uri("https://orderservice.com/orders?userId=" + userId)
        .retrieve()
        .bodyToFlux(Order.class);
}
```

**3. High-Concurrency Requirements**

For applications that need to handle many simultaneous requests, WebClient is ideal:

- It uses fewer threads compared to blocking clients like RestTemplate, resulting in better scalability.
- Suitable for applications with thousands of users or services running on constrained resources.

**Example Use Case**:

- Social media platforms with millions of users.
- E-commerce platforms handling a high volume of concurrent requests during sales events.

**4. Streaming and Real-Time Data**

WebClient excels in handling streaming data and server-sent events (SSE). Use WebClient for applications requiring:

- **Data Streaming**: For example, consuming real-time stock price updates or sensor data.
- **Long-Lived Connections**: Handling WebSockets or SSE for applications like chats or live dashboards.

**Example**:

```
public Flux<StockPrice> streamStockPrices() {
    return WebClient.create()
        .get()
        .uri("https://api.example.com/stock-prices/stream")
        .retrieve()
        .bodyToFlux(StockPrice.class);
}
```

**5. Handling Large Payloads**

Applications dealing with large file uploads/downloads or streaming large data sets should use WebClient because of its efficient resource utilization:

- Efficient memory handling due to its non-blocking I/O.
- Supports streaming data chunks without loading the entire content into memory.

**Example**:

```
public Flux<DataChunk> downloadLargeFile() {
    return WebClient.create()
        .get()
        .uri("https://api.example.com/largefile")
        .retrieve()
        .bodyToFlux(DataChunk.class);
}
```

**6. Modernizing Legacy Systems**

As systems evolve, legacy synchronous applications are often modernized into asynchronous, reactive systems. WebClient is ideal for such transitions:

- Works seamlessly with legacy synchronous APIs while supporting a reactive design.
- Enables partial modernization by allowing some parts of the system to be reactive.

**7. Fault Tolerance and Resilience**

WebClient integrates with libraries like **Resilience4j** to provide fault-tolerant, resilient communication:

- **Retries**: Retry failed requests automatically.
- **Circuit Breakers**: Prevent cascading failures in interconnected services.
- **Timeouts**: Configure timeouts to handle slow responses gracefully.

**Example**:

```
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import reactor.core.publisher.Mono;

CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("myService");

public Mono<User> fetchUserWithResilience(String userId) {
    return WebClient.create()
        .get()
        .uri("https://api.example.com/users/{id}", userId)
        .retrieve()
        .bodyToMono(User.class)
        .transformDeferred(CircuitBreakerOperator.of(circuitBreaker));
}
```

**8. Security and Token Management**

WebClient provides robust support for secure communication:

- **OAuth2 Integration**: Works with Spring Security for handling OAuth2 token management.
- **Custom Authentication**: Configure custom headers or tokens for secure communication.

**Example**:

```
public Mono<User> fetchUserWithToken(String userId, String token) {
    return WebClient.builder()
        .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + token)
        .build()
        .get()
        .uri("https://api.example.com/users/{id}", userId)
        .retrieve()
        .bodyToMono(User.class);
}
```

**9. Testing and Mocking APIs**

WebClient is suitable for testing purposes as it integrates with mock servers like **WireMock**:

- Simulate API responses for integration testing.
- Test failure scenarios like timeouts or error codes.

**Example**:

```
@Test
public void testFetchUser() {
    WireMockServer wireMockServer = new WireMockServer();
    wireMockServer.start();
    wireMockServer.stubFor(get(urlEqualTo("/users/1"))
        .willReturn(aResponse()
            .withHeader("Content-Type", "application/json")
            .withBody("{\"id\":1,\"name\":\"John Doe\"}")));

    WebClient webClient = WebClient.create(wireMockServer.baseUrl());
    Mono<User> user = webClient.get().uri("/users/1").retrieve().bodyToMono(User.class);

    StepVerifier.create(user)
        .expectNextMatches(u -> u.getName().equals("John Doe"))
        .verifyComplete();

    wireMockServer.stop();
}
```

**10. Cross-Platform Integrations**

WebClient’s flexibility allows it to integrate with diverse platforms and protocols:

- Consuming REST APIs, GraphQL endpoints, or SOAP services.
- Communicating with cloud platforms like AWS, Azure, or Google Cloud.

---

## 58. Why Use WebClient Over RestTemplate in a Spring Boot Application?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

When developing Spring Boot applications, communicating with RESTful web services is a frequent requirement. Historically, developers have used **RestTemplate** for this purpose. However, with the advent of reactive programming and the need for more efficient resource utilization, **WebClient** has become the preferred choice. This article explores the differences between **RestTemplate** and **WebClient**, and highlights why WebClient is more suitable in modern applications with real-world examples.

---

## 59. Why Choose WebClient Over RestTemplate?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

1. **Non-Blocking I/O**: WebClient uses a non-blocking model, which means threads are not held up while waiting for responses. This is particularly useful when multiple API calls are made concurrently.
2. **Support for Reactive Streams**: WebClient integrates seamlessly with reactive libraries like **Reactor** and **RxJava**, making it suitable for modern reactive architectures.
3. **Better Scalability**: Non-blocking behavior allows WebClient to handle more requests simultaneously without exhausting server threads.
4. **Modern and Extensible**: WebClient is more flexible and feature-rich, supporting advanced use cases like streaming large files, handling WebSocket connections, and multipart requests.

---

## 60. What is background processing in the context of Spring Boot?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Background processing refers to executing tasks asynchronously or periodically without blocking the main application flow. It is essential for tasks such as sending emails, processing files, generating reports, etc.

---

## 61. How can you enable asynchronous processing in a Spring Boot application?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

To enable asynchronous processing, you need to use the `@EnableAsync` annotation on a configuration class and the `@Async` annotation on methods that should run asynchronously.

Example:

```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;

@SpringBootApplication
public class AsyncApplication {
    public static void main(String[] args) {
        SpringApplication.run(AsyncApplication.class, args);
    }
}

@Configuration
@EnableAsync
class AsyncConfig {
    @Bean(name = "taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(2);
        executor.setQueueCapacity(500);
        executor.setThreadNamePrefix("AsyncThread-");
        executor.initialize();
        return executor;
    }
}

import org.springframework.stereotype.Service;

@Service
public class AsyncService {
    @Async("taskExecutor")
    public void executeAsyncTask() {
        System.out.println("Executing task in thread: " + Thread.currentThread().getName());
    }
}
```

---

## 62. What is the difference between @Async and @Scheduled in Spring Boot?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

- `@Async` is used for executing methods asynchronously, i.e., in a separate thread without blocking the main thread.
- `@Scheduled` is used for executing methods at specific intervals or schedules, i.e., periodic execution.

---

## 63. How do you schedule a task in Spring Boot?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

You can schedule a task using the `@Scheduled` annotation. You also need to enable scheduling by using the `@EnableScheduling` annotation on a configuration class.

Example:

```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

@SpringBootApplication
public class ScheduledApplication {
    public static void main(String[] args) {
        SpringApplication.run(ScheduledApplication.class, args);
    }
}

@Configuration
@EnableScheduling
class SchedulingConfig {
}

import org.springframework.stereotype.Service;

@Service
public class ScheduledService {
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Scheduled task executed at: " + System.currentTimeMillis());
    }
}
```

---

## 64. How do you configure a thread pool for scheduling tasks in Spring Boot?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

You can configure a thread pool for scheduling tasks by defining a `TaskScheduler` bean.

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
@EnableScheduling
public class SchedulingConfig {
    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10);
        scheduler.setThreadNamePrefix("ScheduledTask-");
        return scheduler;
    }
}
```

---

## 65. How can you handle errors in asynchronous methods?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Errors in asynchronous methods can be handled by using a custom `AsyncUncaughtExceptionHandler`.

Example:

```
import org.springframework.aop.interceptor.AsyncUncaughtExceptionHandler;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.AsyncConfigurer;
import org.springframework.scheduling.annotation.EnableAsync;

import java.lang.reflect.Method;
import java.util.concurrent.Executor;

@Configuration
@EnableAsync
public class AsyncConfig implements AsyncConfigurer {
    @Override
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(2);
        executor.setQueueCapacity(500);
        executor.setThreadNamePrefix("AsyncThread-");
        executor.initialize();
        return executor;
    }

    @Override
    public AsyncUncaughtExceptionHandler getAsyncUncaughtExceptionHandler() {
        return new CustomAsyncExceptionHandler();
    }
}

class CustomAsyncExceptionHandler implements AsyncUncaughtExceptionHandler {
    @Override
    public void handleUncaughtException(Throwable throwable, Method method, Object... obj) {
        System.err.println("Exception message - " + throwable.getMessage());
        System.err.println("Method name - " + method.getName());
        for (Object param : obj) {
            System.err.println("Parameter value - " + param);
        }
    }
}
```

---

## 66. How can you handle errors in scheduled methods?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Errors in scheduled methods can be handled by wrapping the method body with try-catch blocks.

Example:

```
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class ScheduledService {
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        try {
            // Task execution logic
            System.out.println("Scheduled task executed at: " + System.currentTimeMillis());
        } catch (Exception e) {
            // Error handling logic
            System.err.println("Error occurred: " + e.getMessage());
        }
    }
}
```

---

## 67. What are the different types of scheduling options available in @Scheduled?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The `@Scheduled` annotation supports several scheduling options:

- `fixedRate`: Executes the task at a fixed interval, specified in milliseconds.
- `fixedDelay`: Executes the task with a fixed delay between the completion of the last invocation and the start of the next.
- `cron`: Executes the task based on a cron expression.

---

## 68. Can you give an example of a cron expression in @Scheduled?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

A cron expression specifies the schedule using a string format. Here is an example that runs a task every day at 2 AM:

Example:

```
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class ScheduledService {
    @Scheduled(cron = "0 0 2 * * ?")
    public void performTask() {
        System.out.println("Scheduled task executed at: " + System.currentTimeMillis());
    }
}
```

---

## 69. What are the key differences between fixedRate and fixedDelay in @Scheduled?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

- `fixedRate`: The interval between method invocations, measured from the start time of each invocation.
- `fixedDelay`: The interval between method invocations, measured from the completion time of each invocation.

Example:

```
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class ScheduledService {
    @Scheduled(fixedRate = 5000)
    public void performTaskWithFixedRate() {
        System.out.println("Fixed rate task executed at: " + System.currentTimeMillis());
    }

    @Scheduled(fixedDelay = 5000)
    public void performTaskWithFixedDelay() {
        System.out.println("Fixed delay task executed at: " + System.currentTimeMillis());
    }
}
```

These questions and answers cover key concepts and practical implementations of background processing in Spring Boot, providing a comprehensive understanding for interview preparation.

---

## 70. What is Spring Data and how does it simplify database interactions in Spring applications?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Spring Data is a part of the Spring Framework that aims to simplify the data access layer in applications. It provides a consistent and easy-to-use approach to accessing and managing data from various data sources (such as relational databases, NoSQL databases, and others) using a repository abstraction layer. It eliminates boilerplate code, allowing developers to focus on the logic specific to their application.

---

## 71. What are Spring Data Repositories?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Types of Spring Data Repositories:

**1. CrudRepository:** The `CrudRepository` interface provides CRUD functionality for the entity class that is being managed. It includes methods like `save()`, `findById()`, `findAll()`, `count()`, `deleteById()`, etc.

```
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Long> {
    List<User> findByLastName(String lastName);
}
```

**2**. **PagingAndSortingRepository:** The `PagingAndSortingRepository` extends `CrudRepository` and adds methods to handle pagination and sorting. Methods like `findAll(Pageable pageable)` and `findAll(Sort sort)` are included.

```
import org.springframework.data.repository.PagingAndSortingRepository;

public interface UserRepository extends PagingAndSortingRepository<User, Long> {
    Page<User> findByLastName(String lastName, Pageable pageable);
}
```

**3. JpaRepository:** The `JpaRepository` extends `PagingAndSortingRepository` and includes additional methods specific to JPA, such as methods for batch operations. This is the most commonly used repository interface for JPA-based applications.

```
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByEmail(String email);
}
```

**4. Other Specific Repositories:** Spring Data provides specific repository interfaces for various data stores, such as `MongoRepository` for MongoDB, `CassandraRepository` for Cassandra, and `ElasticsearchRepository` for Elasticsearch. These interfaces provide methods tailored to the particular data store.

```
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UserRepository extends MongoRepository<User, String> {
    List<User> findByFirstName(String firstName);
}
```

---

## 72. What is the role of the @Repository annotation?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The `@Repository` annotation is a specialization of the `@Component` annotation, used to indicate that the class is a repository (a mechanism for encapsulating storage, retrieval, and search behavior). It also allows Spring to translate database-related exceptions into Spring's data access exceptions (a feature known as exception translation).

---

## 73. How do you define a simple repository in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Here’s an example of a simple repository for an entity `User`:

```
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByLastName(String lastName);
}
```

---

## 74. What are derived query methods in Spring Data?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Derived query methods in Spring Data JPA are methods in a repository interface that derive their queries from the method name. The method name contains the property names of the entity, and Spring Data parses it to generate the query. For example:

```
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByLastName(String lastName);
    List<User> findByAgeGreaterThanEqual(int age);
    List<User> findByFirstNameAndLastName(String firstName, String lastName);
}
```

---

## 75. What is the @Query annotation and when would you use it?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The `@Query` annotation allows you to define JPQL (Java Persistence Query Language) or SQL queries directly on repository methods. This is useful when the query is complex or cannot be derived from the method name. Here's an example:

```
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface UserRepository extends JpaRepository<User, Long> {

    @Query("SELECT u FROM User u WHERE u.email = :email")
    User findByEmail(@Param("email") String email);
}
```

---

## 76. How does pagination and sorting work in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Pagination and sorting are supported by extending the `PagingAndSortingRepository` or `JpaRepository`. You can use the `Pageable` and `Sort` objects to control these features. Here's an example:

```
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {

    Page<User> findByLastName(String lastName, Pageable pageable);
}
```

And to use this in a service or controller:

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public Page<User> getUsersByLastName(String lastName, int page, int size) {
        Pageable pageable = PageRequest.of(page, size, Sort.by("firstName").ascending());
        return userRepository.findByLastName(lastName, pageable);
    }
}
```

---

## 77. What are custom repository implementations? / How do you implement custom methods in a Spring Data repository?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

If you need custom behavior that cannot be achieved by derived queries or the `@Query` annotation, you can provide a custom implementation for your repository. This involves creating an interface for custom methods and providing an implementation for it.

```
// Custom repository interface
public interface CustomUserRepository {
    List<User> findUsersByCustomCriteria();
}

// Implementation of custom repository
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import java.util.List;

public class CustomUserRepositoryImpl implements CustomUserRepository {

    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<User> findUsersByCustomCriteria() {
        String jpql = "SELECT u FROM User u WHERE ..."; // custom JPQL query
        TypedQuery<User> query = entityManager.createQuery(jpql, User.class);
        return query.getResultList();
    }
}

// Extending repository with custom methods
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long>, CustomUserRepository {
    // Other query methods
}
```

---

## 78. How does Spring Data handle transactions?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Spring Data repositories are transactional by default. The `@Transactional` annotation is used to define transaction boundaries. By default, CRUD methods in repositories are transactional. For custom methods or service methods, you can explicitly use the `@Transactional` annotation.

```
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Transactional
    public void saveUser(User user) {
        userRepository.save(user);
        // Other transactional operations
    }
}
```

---

## 79. What is the role of the @Entity annotation?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The `@Entity` annotation specifies that the class is an entity and is mapped to a database table. It is a JPA annotation and is a prerequisite for Spring Data JPA to manage and persist the entity. Here is an example:

```
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class User {

    @Id
    private Long id;
    private String firstName;
    private String lastName;
    private String email;

    // Getters and setters
}
```

---

## 80. How does Spring Data JPA handle relationships between entities?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Spring Data JPA handles relationships between entities using JPA annotations to define the type of relationship and how the entities are connected. Here are examples of each relationship type:

**@OneToOne:** A one-to-one relationship where each instance of Entity A is related to one instance of Entity B.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @OneToOne
    private Profile profile;

    // Getters and setters
}

@Entity
public class Profile {
    @Id
    private Long id;
    private String bio;

    @OneToOne(mappedBy = "profile")
    private User user;

    // Getters and setters
}
```

**@OneToMany:** A one-to-many relationship where one instance of Entity A is related to multiple instances of Entity B.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @OneToMany(mappedBy = "user")
    private List<Post> posts;

    // Getters and setters
}

@Entity
public class Post {
    @Id
    private Long id;
    private String content;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    // Getters and setters
}
```

**@ManyToOne:** A many-to-one relationship where multiple instances of Entity A are related to one instance of Entity B.

```
@Entity
public class Post {
    @Id
    private Long id;
    private String content;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    // Getters and setters
}

@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @OneToMany(mappedBy = "user")
    private List<Post> posts;

    // Getters and setters
}
```

**@ManyToMany:** A many-to-many relationship where multiple instances of Entity A are related to multiple instances of Entity B.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @ManyToMany
    @JoinTable(
        name = "user_roles",
        joinColumns = @JoinColumn(name = "user_id"),
        inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Set<Role> roles;

    // Getters and setters
}

@Entity
public class Role {
    @Id
    private Long id;
    private String name;

    @ManyToMany(mappedBy = "roles")
    private Set<User> users;

    // Getters and setters
}
```

---

## 81. What are entity lifecycle events in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Entity lifecycle events in Spring Data JPA allow developers to execute logic at specific points in the entity’s lifecycle. These events are managed through JPA annotations:

**@PrePersist:** Invoked before the entity manager persists a new entity.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @PrePersist
    public void prePersist() {
        System.out.println("About to persist: " + this);
    }

    // Getters and setters
}
```

**@PostPersist:** Invoked after the entity manager persists a new entity.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @PostPersist
    public void postPersist() {
        System.out.println("Persisted: " + this);
    }

    // Getters and setters
}
```

**@PreUpdate:** Invoked before the entity manager updates an existing entity.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @PreUpdate
    public void preUpdate() {
        System.out.println("About to update: " + this);
    }

    // Getters and setters
}
```

**@PostUpdate:** Invoked after the entity manager updates an existing entity.

```
@Entity
public class User {
    @Id
    private Long id;
    private String firstName;

    @PostUpdate
    public void postUpdate() {
        System.out.println("Updated: " + this);
    }

    // Getters and setters
}
```

These annotations help manage custom actions or validations during the lifecycle of an entity, such as logging, auditing, or custom business logic.

---

## 82. How do you handle query performance and optimization in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Optimizing query performance in Spring Data JPA involves several best practices:

**1. Use Projections:** Retrieve only the necessary fields using projections to avoid fetching unnecessary data.

```
public interface UserNameOnly {
    String getFirstName();
    String getLastName();
}

public interface UserRepository extends JpaRepository<User, Long> {
    List<UserNameOnly> findByLastName(String lastName);
}
```

**2. Fetch Strategies:** Use appropriate fetch strategies (`@OneToOne`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`) and the `fetch` attribute (FetchType.EAGER or FetchType.LAZY) to manage data loading.

```
@OneToMany(fetch = FetchType.LAZY, mappedBy = "user")
private List<Post> posts;
```

**3. Indexed Columns:** Ensure that frequently queried columns are indexed in the database to speed up query execution.

**4. Batch Fetching:** Use batch fetching to reduce the number of queries for related entities.

```
@BatchSize(size = 10)
@OneToMany(fetch = FetchType.LAZY, mappedBy = "user")
private List<Post> posts;
```

**5. Query Caching:** Enable query caching for frequently executed queries.

```
@QueryHints({ @QueryHint(name = "org.hibernate.cacheable", value = "true") })
@Query("SELECT u FROM User u WHERE u.lastName = :lastName")
List<User> findByLastName(@Param("lastName") String lastName);
```

**6. Native Queries:** For complex queries that are not efficiently handled by JPQL, use native SQL queries.

```
@Query(value = "SELECT * FROM users WHERE email = :email", nativeQuery = true)
User findByEmailNative(@Param("email") String email);
```

**7. Entity Graphs:** Use entity graphs to define a fine-grained fetching strategy at runtime.

---

## 83. What is the @Modifying annotation in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

The `@Modifying` annotation is used in Spring Data JPA to indicate that a query method modifies the database and does not return an entity. It is typically used for `UPDATE` or `DELETE` operations. Here is an example:Copy code

```
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

public interface UserRepository extends JpaRepository<User, Long> {
    @Modifying
    @Transactional
    @Query("UPDATE User u SET u.email = :email WHERE u.id = :id")
    int updateEmail(@Param("id") Long id, @Param("email") String email);
    @Modifying
    @Transactional
    @Query("DELETE FROM User u WHERE u.id = :id")
    void deleteById(@Param("id") Long id);
}
```

In this example:

- The `updateEmail` method updates the email of a user identified by their ID.
- The `deleteById` method deletes a user by their ID.
- The `@Modifying` annotation indicates that these methods modify the database.
- The `@Transactional` annotation ensures that the operations are performed within a transaction.

---

## 84. How do you handle auditing in Spring Data JPA?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Auditing in Spring Data JPA allows tracking and storing metadata about entity changes, such as creation and modification timestamps and users. Here’s how to enable and use auditing:

**1. Enable Auditing:** Add the `@EnableJpaAuditing` annotation to a configuration class.

```
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@Configuration
@EnableJpaAuditing
public class JpaConfig {
}
```

**2. Auditable Entity:** Annotate the entity class with auditing annotations.

```
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.Entity;
import javax.persistence.EntityListeners;
import javax.persistence.Id;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import java.util.Date;

@Entity
@EntityListeners(AuditingEntityListener.class)
public class User {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    @CreatedDate
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdDate;

    @LastModifiedDate
    @Temporal(TemporalType.TIMESTAMP)
    private Date lastModifiedDate;

    // Getters and setters
}
```

**3. AuditorAware Implementation:** Implement the `AuditorAware` interface to provide the current auditor (user).

```
import org.springframework.data.domain.AuditorAware;
import java.util.Optional;

public class AuditorAwareImpl implements AuditorAware<String> {
    @Override
    public Optional<String> getCurrentAuditor() {
        // Return the current user or system as the auditor
        return Optional.of("system");
    }
}
```

**4. Register AuditorAware Bean:** Register the `AuditorAware` implementation as a bean.

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class JpaConfig {

    @Bean
    public AuditorAware<String> auditorProvider() {
        return new AuditorAwareImpl();
    }
}
```

With auditing enabled, Spring Data JPA will automatically populate the `createdDate` and `lastModifiedDate` fields when the entity is persisted or updated.

---

## 85. Question:Explain the difference between findAny and findFirst, and when would you prefer one over the other?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

**`findFirst`** returns the first element of the stream, respecting the encounter order if one exists.

**`findAny`** can return any element from the stream, and it's more performance-friendly in parallel streams because it doesn't enforce processing order.

---

## 86. Question: When would you use Parallel Streams and why?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

We would use Parallel stream if

- We have a lot of data to process in the same (or a very similar) way.
- Ordering doesn’t matter.
- **Items are independent of each other.**
- **if particular processing step is the bottleneck.**

Lets find the Sum of large list of integers.

```
package collectors;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ParallelStreamsDemo {

        public static void main(String[] args) {
            // Create a large list of random integers
            List<Integer> numbers = new ArrayList<>();
            Random random = new Random();
            for (int i = 0; i < 1_000_000; i++) {
                numbers.add(random.nextInt(100));
            }

            // Calculate the sum using parallel stream
            long startTime = System.currentTimeMillis();
            int sum = numbers.parallelStream().reduce(0, Integer::sum);
            long endTime = System.currentTimeMillis();

            System.out.println("Sum: " + sum);
            System.out.println("Time taken with parallel stream: " + (endTime - startTime) + " ms");
        }
}
```

---

## 87. How do you Stream from a File?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

```
Stream<String> lines = Files.lines(Paths.get("file.txt"));
```

---

## 88. What is the purpose of the peek method in a Stream?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

`peek` is an intermediate operation used mainly for debugging purposes, as it allows you to perform an operation on each element of the stream as it's consumed.

**peek is used to**

→**Observing Elements**: is often used to observe the elements of the stream at a certain point in the pipeline.

> This is particularly useful for debugging complex stream operations to understand how elements are transformed as they pass through various stages of the stream.
> 
- **>Logging**: peek can be used to log information about the elements for debugging purposes without altering the stream's processing.

Let’s say we have a list of integers, and we want to filter out numbers less than 10, map them to their squares, and then collect them into a list.

> While we are doing this we want to see the element after filtering and also after mapping. Lets look at the below example.
> 

```
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class PeekExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 5, 10, 15, 20);

        List<Integer> squaredNumbers = numbers.stream()
            .filter(n -> n >= 10)
            .peek(n -> System.out.println("After filter: " + n))
            .map(n -> n * n)
            .peek(n -> System.out.println("After map: " + n))
            .collect(Collectors.toList());
    }
}
```

In the above example we are peeking the elements to log them at each stage that could also be used for debugging purpose.

---

## 89. How do you convert a Stream to an array?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

```
String[] array = stream.toArray(String[]::new);
```

---

## 90. Question 2: How do abstract classes and functional interfaces differ in their usage and design in Java?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Abstract classes are primarily used for class hierarchies and can contain a mix of abstract and concrete methods. Functional interfaces, introduced for functional programming, have a single abstract method and are essential for working with lambdas and method references, promoting concise and readable code.

```
@FunctionalInterface
interface Calculator {
    double calculate(int a, int b);

    // Default method
    default void description() {
        System.out.println("Performs calculations.");
    }

    // Static method
    static void info() {
        System.out.println("A calculator interface.");
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator addition = (a, b) -> a + b;
        Calculator subtraction = (a, b) -> a - b;

        double result1 = addition.calculate(10, 5);
        double result2 = subtraction.calculate(10, 5);

        System.out.println("Addition result: " + result1);
        System.out.println("Subtraction result: " + result2);

        addition.description(); // Calling default method
        Calculator.info(); // Calling static method
    }
}
```

Explanation:

- `Calculator` is a functional interface with a single abstract method `calculate(int a, int b)`.
- It also contains a default method `description()` and a static method `info()`.
- In the `main` method, we create two lambda expressions, `addition` and `subtraction`, to implement the `calculate` method.
- We calculate and print the results of addition and subtraction.
- We also demonstrate calling the default method `description()` and the static method `info()` of the functional interface.

> Abstract classes can have both abstract and concrete methods and support class inheritance, while functional interfaces are designed for lambda expressions and method references, enforcing a single abstract method contract.
>

---

## 91. Question 4: Why can’t we store primitive data types directly in a HashMap as keys, and why are only Wrapper classes allowed for this purpose? What would happen if we attempted to store primitive types as keys in a HashMap?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

Storing primitive data types directly in a HashMap as keys is not allowed in Java because of the way HashMaps work and the need for reference types. Here’s why:

1. **Reference Types Required**: In a HashMap, keys are stored as references to objects, and their uniqueness is determined based on the object’s `equals()` and `hashCode()` methods. Primitive data types, such as `int`, `double`, or `char`, do not have these methods because they are not objects.
2. **Auto-Boxing and Wrapper Classes**: Java provides wrapper classes like `Integer`, `Double`, and `Character` to encapsulate primitive types, effectively converting them into reference types. This allows them to have `equals()` and `hashCode()` methods, making them suitable for use as HashMap keys.
3. **Attempting to Store Primitives:** If you attempt to store primitive types directly as keys in a HashMap, Java will attempt to auto-box them into their corresponding wrapper classes. This process is called auto-boxing. For example, if you try to store an `int` as a key, Java will auto-box it into an `Integer`. While this might work in some cases, it can lead to unexpected behavior and performance overhead.

```
Map<Integer, String> map = new HashMap<>();
int key = 42;
map.put(key, "Value"); // Auto-boxing occurs: key is converted to Integer
```

4. **Performance Overhead:** Using wrapper classes for primitive types introduces performance overhead due to auto-boxing and unboxing (converting between primitive and wrapper types). This can impact memory usage and execution speed, especially in data-intensive applications.

5. **Loss of Identity:** When auto-boxing occurs, each primitive value is converted to a new instance of the wrapper class. This means that two separate auto-boxed instances of the same primitive value may not be considered equal in terms of `equals()` unless they refer to the same object.

```
Integer a = 42;
Integer b = 42;
System.out.println(a.equals(b)); // true (auto-boxed values are cached)
System.out.println(a == b); // true (they refer to the same cached object)
```

> HashMaps require reference types as keys, which is why only Wrapper classes can be used directly. Attempting to store primitive types will result in auto-boxing, potential performance overhead, and issues related to identity comparison. To maintain efficiency and avoid unexpected behavior, it’s generally advisable to use Wrapper classes when working with HashMap keys that represent primitive values.
>

---

## 92. Question 5: When using a StringBuilder as a key in a HashMap, why might you encounter unexpected results when attempting to retrieve a value using a different StringBuilder instance with the same content? How can you address this issue to retrieve values based on the content of a StringBuilder?

*Source: [`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*

When using a `StringBuilder` as a key in a HashMap, the default behavior relies on object identity for `hashCode()` and `equals()` checks. Consequently, attempting to retrieve a value using a different `StringBuilder` instance with the same content may not yield the expected result, as these instances are considered unequal by default.

To address this issue and enable retrieval of values based on the content of a `StringBuilder`, you can create a custom subclass of `StringBuilder` that overrides the `hashCode()` and `equals()` methods. In this subclass, you can implement these methods to consider the content of the `StringBuilder` rather than its identity. This way, you can ensure that two `StringBuilder` instances with the same content are treated as equal, allowing you to retrieve values based on content effectively.

---

## 93. Q1 — What is the output of the given Java code?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 94. Q2 — What will be the output of the given Java code?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 95. Q5 — How many String objects are created by the below code?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

```
public class Test{
 public static void main(String[] args){
   String s = new String("Hello World");
 }
}
```

---

## 96. Q6 — What is the output of the below Java code?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

```
public class Test{
 public static void main(String[] arr){
    System.out.println(0.1*3 == 0.3);
    System.out.println(0.1*2 == 0.2);
 }
}
```

---

## 97. Q10 — What happens when we run the below Java code?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 98. What is meant by Java being platform independent?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Java works on the principle of write once and run anywhere. Once a Java program is written, it is compiled into what is known as byte code, which can then be run on any Java Virtual Machine or JVM for short.

[](https://miro.medium.com/v2/resize:fit:875/0*7_U0qVJxjbse_1rk)

Compilation to bytecode is the magic behind Java’s interoperability. Different operating systems and hardware architectures have JVMs custom designed for themselves and all JVMs can run the same bytecode. Therefore, if you write a Java program on Linux, it will run seamlessly on a JVM designed for Windows operating system, making code agnostic to the underlying hardware and OS.

---

## 99. Explain the concepts of JRE, JDK, and JVM

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- **JRE (Java Runtime Environment)** includes the Java Virtual Machine and the standard Java APIs (core classes and supporting files.). The JRE contains just enough to execute a Java application, but not enough to compile it.
- **JDK (Java Development Kit)** is the JRE plus the Java compiler, and a set of other tools to compile and debug code. JRE consists of Java platform libraries, Java Virtual Machine (JVM), Java Plugin and Java Web Start to run Java applications. JRE as a stand-alone does not contain compilers and debugging tools. If you need to develop Java programs you need the full Java SDK. The JRE is not enough for program development. Only the full Java SDK contains the Java compiler which turns your .java source files into bytecode .class files.
- **JVM (Java Virtual Machine)** is an implementation of a specification, detailing the behavior expected of a JVM. Any implementation that conforms to the JVM specification should be able to run code compiled into Java bytecode irrespective of the language in which the code was originally written. In the Java programming language, all source code is first written in plain text files ending with the .java extension. Those source files are then compiled into .class files by the javac compiler. A .class file does not contain code that is native to your processor; it instead contains bytecodes — the machine language of the Java Virtual Machine. The java launcher tool then runs your application with an instance of the Java Virtual Machine.

---

## 100. How would you mark an entity package private in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

There’s no explicit modifier for package private. In the absence of any modifier the class or member variables are package private. A member marked package private is only visible within its own package. Consider the class below.

[](https://miro.medium.com/v2/resize:fit:875/0*m8sa9DI5toNvXF8m)

Package private is a slightly wider form of private. One nice thing about package-private is that you can use it to give access to methods you would otherwise consider private to unit test classes. So, if you use helper classes which have no other use but to help your public classes do something clients need, it makes sense to make them package private as you want to keep things as simple as possible for users of the library.

---

## 101. Why should you avoid the finalize() method in the Object class? What are some alternatives?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The Object class provides a callback method, finalize(), that may be invoked on an object when it becomes garbage. Object’s implementation of finalize() does nothing — you can override finalize() to do cleanup, such as freeing up resources.

The finalize() method may be called automatically by the system, but when it is called, or even if it is called, is uncertain. Therefore, you should not rely on this method to do your cleanup for you. For example, if you don’t close file descriptors in your code after performing I/O and you expect finalize() to close them for you, you may run out of file descriptors.

Here are some alternatives:

- The try-with-resources idiom can be used to clean up objects. This requires implementing the AutoCloseable interface.
- Using a PhantomReference to perform cleanup when an object is garbage collected
- Using Cleaner class to perform cleanup actions.
- Implement a close() method, which does the cleanup and document that the method be called.

---

## 102. Can you change the contents of a final array as shown in the code snippet below?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

It may appear counterintuitive, but we can actually change the contents of the array even though it is marked as final. The array variable points to a particular start location in the memory where the contents of the array are placed. The location or the memory address can’t be changed. For instance, the following code will not compile:

**However, the following code will work.**

---

## 103. Explain the difference between an interface and an abstract class? When should you use one or the other?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

An abstract class can’t be instantiated, but it can be subclassed. An abstract class usually contains abstract and non-abstract methods that subclasses are forced to provide an implementation for.

An interface is a completely “abstract class” that is used to group related methods with empty bodies.

Following are four main differences between abstract classes and interfaces:

- An abstract class can have final variables, static variables, or class member variables whereas an interface can only have variables that are final and static by default.
- An abstract class can have static, abstract, or non-abstract methods. An interface can have static, abstract, or default methods.
- Members of an abstract class can have varying visibility of private, protected, or public. Whereas, in an interface all methods and constants are public.
- A class can only extend another class, but it can implement multiple interfaces. Similarly, an interface can extend multiple interfaces. An interface never implements a class or an interface.

Use an abstract class when subclasses share state or use common functionality. Or you require to declare non-static, non-final fields or need access modifiers other than public.

Use an interface if you expect unrelated classes would implement your interface. For example, the interfaces Comparable and Cloneable are implemented by many unrelated classes. Interfaces are also used in instances where multiple inheritance of type is desired.

---

## 104. What is polymorphism? Can you give an example?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Polymorphism is the ability in programming to present the same interface for differing underlying forms or data types. Polymorphism is when you can treat an object as a generic version of something, but when you access it, the code determines which exact type it is and calls the associated code. What this means is that polymorphism allows your code to work with different classes without needing to know which class it’s using.

Polymorphism is used to make applications more modular and extensible. Instead of messy conditional statements describing different courses of action, you create interchangeable objects that you select based on your needs. That is the basic goal of polymorphism.

The classic example of polymorphism is a `Shape` class. We derive `Circle`, `Triangle`, and `Rectangle` classes from the parent class `Shape`, which exposes an abstract method draw(). The derived classes provide their custom implementations for the `draw()` method. Now it is very easy to render the different types of shapes all contained within the same array by calling the `draw()` method on each object. This saves us from creating separate draw methods for each shape e.g. `drawTriangle()`, `drawCircle()`etc.

[](https://miro.medium.com/v2/resize:fit:875/0*OUxL4qsOYKtL5Lg-)

---

## 105. Can the main method be overloaded?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Yes, the main method, which is a static method, can be overloaded. But only `public static void main(String[] args)` will be used when your class is launched by the JVM even if you specify one or two command-line arguments. However, programmatically one can invoke the overloaded versions of the main method.

---

## 106. How can you pass multiple arguments to a method on each invocation call?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

We can pass variable number of arguments to a method using varargs feature. Below is an example of passing multiple arguments of the same type to a method.

- The type name is followed by three dots, a space, and then the variable name.
- The varargs variable is treated like an array.
- The varargs variable must appear at the last in the method signature.
- As a consequence of the above, there can only be a single varargs in a method signature.

The above method can be invoked as follows: **Invoking Varargs Method**

---

## 107. Can a semaphore act as a mutex?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A semaphore can potentially act as a mutex if the number of permits it can give out is set to 1. However, the most important difference between the two is that in the case of a mutex, the same thread must call acquire and subsequent release on the mutex whereas in the case of a binary semaphore, different threads can call acquire and release on the semaphore.

This leads us to the concept of “ownership”. A mutex is owned by the thread acquiring it, till the point, it releases it, whereas for a semaphore there’s no notion of ownership.

Need a refresher on multithreading? Check out this article [“Java Multithreading and Concurrency: Cracking Senior Interviews”.](https://blog.educative.io/java-multithreading-and-concurrency-what-to-know-for/)

---

## 108. Explain the Externalizable interface

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The Serializable interface gets us automatic serialization capability for objects of our class. On the other hand the Externalizable interface provides a way to implement a custom serialization mechanism. A class that implements the Externalizable interface is responsible to save and restore the contents of its own instances.

The Externalizable interface extends the Serializable interface and provides two methods to serialize and deserialize an object, `writeExternal()` and `readExternal()`.

---

## 109. If a code block throws more than one exception, how can it be handled?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Multiple types of exceptions thrown by a snippet of code can be handled by multiple catch block clauses followed by the try block. An example snippet of exception handling appears below:

---

## 110. If you were to use a set, how would you determine between a HashSet and a TreeSet?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Initially, you may want to use HashSet as it will give you a better time complexity, but it makes no guarantees as to the iteration order of the set; in particular, it does not guarantee that the order will remain constant over time.

So if you are wanting to maintain the order it’s best to use a TreeSet as it stores keys in ascending order rather than in their insertion order. It’s not thread safe. However, keep in mind that TreeSet is not thread safe whereas a HashSet is.

---

## 111. What are a few ways you can improve the memory footprint of a Java application?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Here are three key steps you can take to improve the memory footprint:

- Limiting the scope of local variables. Each time the top scope from the stack is popped up, the references from that scope are lost, and this could make objects eligible for garbage collection.
- Explicitly set variable references to null when not needed. This will make objects eligible for garbage collection.
- Avoid finalizers. They slow down program performance and do not guarantee anything.

---

## 112. What is the best way to implement a singleton class?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The best way to implement a singleton as per Josh Bloch is to use an enum type for the singleton. Because Java ensures that only a single instance of an enum is ever created, the singleton class implemented via enums is safe from reflection and serialization attacks.

**Question 1: What’s wrong using HashMap in the multi-threaded environment? When get() method go to the infinite loop? (answer)**

Well, nothing is wrong; it depends upon how you use. For example, if you [initialize a HashMap](http://www.java67.com/2016/01/how-to-initialize-hashmap-with-values-in-java.html) by just one thread and then all threads are only reading from it, then it’s perfectly fine.

One example of this is a **Map that contains configuration properties**.

The real problem starts when at least one of that thread is updating HashMap, i.e. adding, changing, or removing any key-value pair.

Since put() operation can cause re-sizing and which can further lead to an infinite loop, that’s why either you should use [Hashtable](http://javarevisited.blogspot.com/2012/01/java-hashtable-example-tutorial-code.html) or [ConcurrentHashMap](http://javarevisited.blogspot.com/2013/02/concurrenthashmap-in-java-example-tutorial-working.html), later is even better.

**Question 2. Does not overriding hashCode() method has any performance implication? (answer)**

This is a good question and opens to all, as per my knowledge, a poor hash code function will result in the [frequent collision in HashMap](http://javarevisited.blogspot.sg/2016/01/how-does-java-hashmap-or-linkedhahsmap-handles.html) which eventually increases the time for adding an object into Hash Map.

From [Java 8](https://javarevisited.blogspot.com/2018/08/top-5-java-8-courses-to-learn-online.html) onwards though collision will not impact performance as much as it does in earlier versions because after a threshold the [linked list](http://javarevisited.blogspot.sg/2017/07/top-10-linked-list-coding-questions-and.html#axzz4xXS86IVo) will be replaced by a [binary tree](http://www.java67.com/2016/08/binary-tree-inorder-traversal-in-java.html), which will give you **O(logN)** performance in the worst case as compared to O(n) of a linked list.

**Question 3: Does all property of the Immutable Object needs to be final in Java? (answer)**

Not necessary, as stated in the linked answer article, you can achieve the same functionality by *making a member as non-final but private and not modifying them except in the constructor.*

Don’t provide a setter method for them, and if it is a mutable object, then don’t ever leak any reference for that member.

Remember [making a reference variable final](https://javarevisited.blogspot.com/2016/09/21-java-final-modifier-keyword-interview-questions-answers.html), only ensures that it will not be reassigned a different value. However, you can still change the individual properties of an object, pointed by that reference variable.

This is one of the critical points; the Interviewer likes to hear from candidates. If you want to know more about final variables in Java, I recommend joining [**The Complete Java MasterClass](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F)** on Udemy, one of the best, hands-on courses.

[**Complete Java Masterclass (Updated for Java 17)You've just stumbled upon the most complete, in-depth Java programming course online. With over 560,000 students…**
udemy.com](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F&source=post_page-----36ba58865681---------------------------------------)

**Question 4: How does substring () inside String works? (answer)**

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

**Question 5: Can you write a critical section code for the singleton? (answer)**

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

*…(truncated — see the source note for the full answer)*

---

## 113. What are the new features in Java 17 and 21?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 114. What is the difference between var, record, and sealed classes?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- `var`: Local variable type inference (Java 10)
- `record`: Immutable data classes (Java 14+)
- `sealed`: Restricted inheritance (Java 17+)

---

## 115. Explain the internal working of HashMap.

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Buckets and hashing
- Handling collisions using Linked List / Tree (since Java 8)
- Resizing logic
- Load factor and threshold

---

## 116. What are functional interfaces and how are they used with lambdas?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 117. Explain Stream API and how it differs from loops.

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Lazy evaluation
- Functional-style coding
- Parallel streams for multi-core optimization

---

## 118. What are the major features of Spring Boot 3.x?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Native Compilation support with GraalVM
- Jakarta EE 10 alignment
- Observability via Micrometer
- Java 17+ baseline

---

## 119. What is dependency injection and how is it implemented in Spring?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 120. What is the difference between @Component, @Service, @Repository, and @Controller?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

All are component stereotypes but serve different layers:

- `@Service` for business logic
- `@Repository` for persistence
- `@Controller` for MVC web layer
- `@Component` is generic

---

## 121. What is Reactive Programming in Spring?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Non-blocking, event-driven model
- Built using Project Reactor (Mono, Flux)
- Used in Spring WebFlux

```
public Mono<User> getUser(String id) {
    return userRepository.findById(id);
}
```

---

## 122. Explain JPQL vs Native Query.

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- JPQL: Object-oriented queries (on entities)
- Native: SQL-based queries directly on tables

---

## 123. How do you handle N+1 problems in JPA?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Use `@EntityGraph`
- `JOIN FETCH` in JPQL
- Hibernate batch fetching

---

## 124. How does Spring Security integrate with JWT?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Stateless auth
- Custom filters for token parsing
- OAuth2 / Keycloak integration for SSO

---

## 125. What are some tools you use for observability in Spring Boot?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- **Micrometer**
- **Prometheus + Grafana**
- **Spring Boot Actuator**

---

## 126. How is a Spring Boot app deployed in Kubernetes?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Dockerize the app using `Dockerfile`
- Create `Deployment` and `Service` YAMLs
- Use ConfigMaps and Secrets
- Monitor with Prometheus

---

## 127. How do microservices communicate?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- REST APIs (synchronous)
- Kafka/RabbitMQ (asynchronous)
- gRPC (binary protocol)

---

## 128. How to handle distributed configuration in Spring Boot?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Spring Cloud Config
- Vault for secrets
- Consul or Zookeeper

---

## 129. How do you implement resilience in microservices?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Retry, Fallback: Resilience4j
- Circuit Breakers: Resilience4j / Hystrix (legacy)
- Bulkheads, Rate Limiting

---

## 130. What’s the difference between @Mock, @Spy, and @InjectMocks in Mockito?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- `@Mock`: Creates dummy
- `@Spy`: Partial mock (real object + stubs)
- `@InjectMocks`: Injects mocks into actual object

---

## 131. How do you test a REST API in Spring Boot?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Use `@WebMvcTest` for controller layer
- Mock dependencies using Mockito
- Use `MockMvc` or `TestRestTemplate`

```
mockMvc.perform(get("/api/users"))
       .andExpect(status().isOk());
```

---

## 132. How do you handle memory leaks in Java applications?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- Profiling with VisualVM / JMC
- Check GC logs
- Analyze heap dumps

---

## 133. Describe a recent challenge in a Java project and how you solved it.

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

📌 *Pro Tip:* Focus on debugging, scaling, performance optimization, or refactoring legacy code.

---

## 134. What is Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Java is a high-level, object-oriented programming language that is designed to be platform-independent, meaning you can write code once and run it anywhere with the Java Virtual Machine (JVM).

It’s easy to learn for beginners and widely used for building web, mobile, and enterprise applications. Java is known for its robustness, security features, and versatility. It supports modular and reusable code through its object-oriented principles, and it comes with a rich set of libraries and frameworks to streamline development.

[**What is Java?This post provides everything you'll need to know about getting started with the Java programming language.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/11/java-programming-language-getting-started.html)

You may also get a question like What are the key features of Java?

Refer to this article: [Main Features of Java ( Explained with Examples )](https://archive.ph/o/L24n2/https://www.javaguides.net/2025/04/main-features-of-java-explained.html)

---

## 135. What is the Java Virtual Machine (JVM)?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The JVM is a **virtual machine that executes Java bytecode**. It converts bytecode into machine-specific code and handles tasks like **memory management, garbage collection, and security**. The JVM is what makes Java platform-independent.

---

## 136. Why is the JVM Important?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The JVM makes Java a platform-independent language. It allows developers to write code once and run it anywhere. The JVM also handles memory management, security, and performance optimization, making Java applications reliable and efficient.

[**What is JVM?Blog about guides/tutorials on Java, Java EE, Spring, Spring Boot, Microservices, Hibernate, JPA, Interview, Quiz…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2024/09/what-is-jvm.html)

---

## 137. What is the difference between JDK, JRE, and JVM?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

**JDK (Java Development Kit)**

🧑‍💻 **JDK is the full toolbox for Java developers.**

**What it includes:**

- JRE (which includes JVM)
- Java compiler (`javac`)
- Debugger (`jdb`)
- Other dev tools (like `jar`, `javadoc`, etc.)

> ✅ Use JDK when you want to WRITE, COMPILE, and RUN Java programs.
> 

**JRE (Java Runtime Environment)**

⚙️ **JRE is a software package that contains everything needed to run a Java program.**

**What it includes:**

- JVM (Java Virtual Machine)
- Libraries and class files needed at runtime (like `rt.jar`)
- Other supporting files

**What it doesn’t include:**

- Compiler (`javac`)
- Development tools

**JVM (Java Virtual Machine)**

🧠 **JVM is the brain behind Java.**

**What it does:**

- It **runs Java bytecode** (compiled `.class` files).
- Converts bytecode into **machine-specific instructions**.
- Provides features like: Garbage collection, Memory management, Security and runtime optimization.

[**What is JDK, JRE and JVM in Java - Explained with DiagramsIn this post, we will discuss an important definition of JVM, JRE, and JDK in the Java programming language. We also…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2019/02/java-jvm-jre-jdk-explained-with-diagrams.html)

---

## 138. What is a class and an object in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 139. What is the main() method in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The `main()` method is the **entry point** of any Java application. It has a specific signature that the JVM looks for when starting a program.

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

---

## 140. What is a constructor in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A constructor is a **special method** used to **initialize objects**. It has the same name as the class and **no return type**. It is called automatically when an object is created.

```
public class Student {
    String name;
    Student(String n) {
        name = n;
    }
}
```

Java also provides a **default constructor** if none is defined.

---

## 141. What is method overloading?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Method overloading means **defining multiple methods with the same name** but different parameters (number, type, or order).

```
void print(int a) { }
void print(String s) { }
void print(int a, String s) { }
```

It increases the **readability** and **flexibility** of the program.

[**Method Overloading in Java with ExamplesIn Java, it is possible to define two or more methods within the same class that share the same name, as long as their…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/09/method-overloading-in-java-with-examples.html)

---

## 142. What is the use of the this keyword in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The `this` keyword refers to the **current object**. It is used when **instance variables are shadowed** by method or constructor parameters.

```
class Employee {
    String name;
    Employee(String name) {
        this.name = name; // refers to instance variable
    }
}
```

---

## 143. What are the four main principles of Object-Oriented Programming (OOP) in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The four key principles of OOP are:

- **Encapsulation**: Hiding internal details and exposing only essential features using classes and access modifiers.
- **Abstraction**: Hiding complex implementation and showing only necessary details using abstract classes or interfaces.
- **Inheritance**: Reusing code by deriving a new class from an existing one.
- **Polymorphism**: Ability to take many forms — method overloading (compile-time) and method overriding (runtime).

[**OOPs Concepts in Java with ExamplesObject-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", contains data and…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/08/oops-concepts-in-java.html)

---

## 144. What is the difference between == and .equals() in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- `==` checks **reference equality** — whether two references point to the same object.
- `.equals()` checks **value equality** — whether two objects have the same content (when overridden properly).

**Example:**

```
String a = new String("Java");
String b = new String("Java");

System.out.println(a == b);      // false
System.out.println(a.equals(b)); // true
```

---

## 145. What are access modifiers in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Access modifiers control the **visibility** of classes, methods, and variables. Java provides four main access levels:

[**Java Access ModifiersIn this article, we will discuss Java access modifiers - public, private, protected & default, which are used to…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/10/java-access-modifiers-public-private-protected-default.html)

---

## 146. What is the difference between static variables and instance variables?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 147. What is method overriding?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Method overriding is when a **subclass provides a new implementation** for a method that is already defined in its superclass.

- The method must have the **same name, return type, and parameters**.
- The method in the subclass should not have **less access** than the superclass method.
- Use the `@Override` annotation for clarity.

[**Method Overloading vs Method Overriding in JavaIn this article, we will explore the differences between Method Overloading and Method Overriding in Java, understand…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2025/04/method-overloading-vs-method-overriding-in-java.html)

---

## 148. Can we override a static method in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

No, we cannot truly override a static method. Static methods belong to the class, not objects, so **method hiding** occurs instead of overriding.

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

---

## 149. What is the purpose of the final keyword in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

`final` is used to declare:

- **Final variable**: Value cannot be changed after assignment.
- **Final method**: Cannot be overridden.
- **Final class**: Cannot be extended (e.g., `String` class).

[**final Java Keyword with ExamplesThe final keyword in Java is used to restrict the user. The final keyword can be used with variable, method, and class.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/12/final-java-keyword-with-examples.html)

---

## 150. What is a constructor overloading?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Constructor overloading means defining **multiple constructors** in a class with different parameter lists. It allows objects to be initialized in different ways.

**Example:**

```
class Book {
    Book() { }
    Book(String title) { }
    Book(String title, String author) { }
}
```

---

## 151. What is super keyword in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The `super` keyword is used to refer to the **immediate parent class**. It can be used to:

- Call the parent class constructor: `super()`
- Access parent class methods or variables: `super.methodName()`

---

## 152. What is the purpose of the interface keyword in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

An `interface` defines a **contract** that a class must follow. It contains **method declarations** without implementations (except for default/static methods). A class implements an interface using the `implements` keyword.

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

---

## 153. What is exception handling in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Exception handling is a mechanism to **handle runtime errors** and prevent the program from crashing. Java provides:

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

---

## 154. What is the use of finally block?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The `finally` block is used to write **clean-up code** (like closing a file, releasing a database connection). It **always executes** whether an exception is thrown or not.

```
try {
    // code
} catch (Exception e) {
    // handle
} finally {
    System.out.println("Always runs");
}
```

---

## 155. What are wrapper classes in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

In Java, wrapper classes are used to convert primitive types into objects.

Java is an object-oriented language, but primitive types like `int`, `double`, `char` are not objects.

So Java provides wrapper classes for each primitive data type to help you use them like objects.

**Example:**

```
int x = 10;
Integer obj = Integer.valueOf(x); // Boxing
int y = obj.intValue();           // Unboxing
```

[**Wrapper Classes in Java: A Simple GuideLearn what wrapper classes are in Java, why they’re important, and how to use them effectively. Includes code examples…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/wrapper-classes-in-java-a-simple-guide-3a10dbc4e5bb)

---

## 156. What is autoboxing and unboxing in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

- **Autoboxing**: Automatic conversion of a primitive to a wrapper class object.
- **Unboxing**: Automatic conversion of a wrapper class object back to a primitive.

**Example:**

```
Integer a = 10; // Autoboxing
int b = a;      // Unboxing
```

Introduced in **Java 5** to simplify code when using collections and generics.

[**Autoboxing and Unboxing in Java: A Simple Guide for BeginnersLearn what autoboxing and unboxing are in Java, why they matter, and how they simplify working with primitive types and…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/autoboxing-and-unboxing-in-java-a-simple-guide-for-beginners-311d8333d972)

---

## 157. What is the difference between String, StringBuilder, and StringBuffer?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

[**String vs StringBuilder vs StringBuffer in JavaString: Use when the text won't change, and thread safety is required. StringBuilder: Use in a single-threaded…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2023/08/string-vs-stringbuilder-vs-stringbuffer.html)

---

## 158. What is the difference between == and .equals() in the case of String?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 159. What is the Java Collections Framework?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

The Java Collections Framework is a set of classes and interfaces that provide **data structures** and **algorithms** to store, retrieve, and manipulate data efficiently. It includes:

- **Interfaces** like `List`, `Set`, `Queue`, `Map`
- **Implementations** like `ArrayList`, `HashSet`, `LinkedList`, `HashMap`, etc.

It supports both **generic** and **non-generic** types and provides operations like sorting, searching, and iteration.

[**Java Collections TutorialThis tutorial is a one-stop shop for all the Java collections interfaces, implementation classes, interface questions…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-collections-tutorial.html)

---

## 160. What is the difference between ArrayList and LinkedList?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

[**Difference between ArrayList and LinkedList in JavaIn this post, we will discuss the difference between ArrayList and LinkedList in Java.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2020/08/difference-between-arraylist-and-linkedlist-in-java.html)

---

## 161. What is the difference between HashSet and TreeSet?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

[**HashSet vs TreeSet: Difference Between HashSet and TreeSet in JavaIn this article, we will discuss the difference between HashSet and TreeSet in Java with examples.**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2023/08/hashset-vs-treeset-in-java.html)

---

## 162. What are Generics in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Generics allow you to **define classes, interfaces, and methods with type parameters**. They enable **compile-time type checking** and eliminate the need for type casting.

**Example:**

```
List<String> names = new ArrayList<>();
names.add("Ravi");
String first = names.get(0); // No casting needed
```

Generics improve code **safety and readability**.

[**Java Generics TutorialGenerics were added in Java 5 to provide compile-time type checking and removing the risk of ClassCastException that…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-generics-tutorial.html)

---

## 163. What is a thread in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A thread is a **lightweight unit of execution** in a program. Java supports **multithreading**, which allows multiple threads to run concurrently, improving performance in CPU-bound or I/O-bound tasks.

You can create threads in two ways:

1. Extending `Thread` class
2. Implementing `Runnable` interface

[**Java Multithreading TutorialMultithreading in Java is a very important topic. In this tutorial, we will learn low-level APIs that have been part of…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-multithreading-utorial.html)

---

## 164. What is the difference between start() and run() methods in threads?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

[**Difference Between start() and run() in Java🔒 This is a Medium member-only article. If you’re not a Medium member, you can read the full article for free on my…**rameshfadatare.medium.com](https://archive.ph/o/L24n2/https://rameshfadatare.medium.com/difference-between-start-and-run-in-java-96affe586a85)

---

## 165. What is synchronization in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Synchronization is used to **control access to shared resources** in a multithreaded environment. It prevents **race conditions** by allowing only one thread to access a block of code or object at a time.

You can use:

- `synchronized` keyword on methods or code blocks
- `synchronized` blocks with object references

**Example:**

```
synchronized void increment() {
    count++;
}
```

---

## 166. What is a deadlock in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A deadlock is a situation where **two or more threads are blocked forever**, waiting for each other to release locks.

**Example Scenario:**

- Thread A holds Lock 1 and waits for Lock 2
- Thread B holds Lock 2 and waits for Lock 1

To avoid deadlocks:

- Always acquire locks in the same order
- Use timeout with `tryLock()` from `java.util.concurrent.locks`

---

## 167. What is an immutable class in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

An immutable class is one whose **objects cannot be modified** once they are created. All the fields of an immutable object are final and set only once through the constructor.

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

---

## 168. Why is String immutable in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Strings in Java are immutable by design. This design decision is about more than just simplicity.

**Key reasons:**

- **Security**: Strings are often used in sensitive areas like file paths and network connections. If a string could be changed, it could lead to vulnerabilities.
- **Performance**: Since immutable strings can be cached and reused, the JVM can optimize performance using a **string pool**.
- **Thread safety**: Immutable objects are naturally thread-safe, which avoids the need for synchronization.

**Example:**

```
String s = "Hello";
s.concat(" World");
System.out.println(s); // prints "Hello"

s = s.concat(" World");
System.out.println(s); // prints "Hello World"
```

---

## 169. What is class loading in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Java uses **Class Loaders** to load `.class` files into memory when needed.

The three main class loaders are:

- **Bootstrap ClassLoader** — loads core Java classes from the JDK
- **Extension ClassLoader** — loads JDK extension libraries
- **Application ClassLoader** — loads classes from the classpath

Java uses **lazy loading**, meaning classes are only loaded when they are first accessed.

---

## 170. What are Lambda Expressions in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A lambda expression is simply a function without a name. It can even be used as a parameter in a function. Lambda Expressions facilitate functional programming and simplify development greatly.

The main use of Lambda expression is to provide an implementation for functional interfaces.

**Syntax:**

```
(parameter) -> expression
```

**Example:**

[**Java 8 Lambda ExpressionsIn this post, we will discuss the most important feature of Java 8 that is Lambda Expressions. We will learn Lambda…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/07/java-8-lambda-expressions.html)

---

## 171. What is a Functional Interface?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

A functional interface is an interface that has **exactly one abstract method**. It can have default or static methods.

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

---

## 172. What is the Stream API in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

Stream API is used to **process collections** (like List or Set) in a **functional style**. It supports operations like `filter`, `map`, `reduce`, `collect`, and more.

**Example:**

```
List<String> names = List.of("Ram", "Shyam", "Ravi");
names.stream()
     .filter(name -> name.startsWith("R"))
     .forEach(System.out::println);
```

Streams help write clean, readable, and concise code for data processing.

[**Java 8 Stream API TutorialThis complete an in-depth tutorial, we will go through the practical usage of Java 8 Streams. Source code examples and…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/p/java-8-stream-api-tutorial.html)

---

## 173. What is Optional in Java?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

`Optional` is a container object used to **avoid null checks** and prevent `NullPointerException`.

**Example:**

```
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(System.out::println);
```

It encourages writing **null-safe** code in a more readable way.

[**Java 8 Optional Class with ExamplesJava introduced a new class Optional in JDK 8. It is a public final class and used to deal with NullPointerException in…**www.javaguides.net](https://archive.ph/o/L24n2/https://www.javaguides.net/2018/07/java-8-optional-class.html)

---

## 174. What are the design principles in OOP?

*Source: [`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*

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

---

## 175. What Worked in My Favor?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

✅ **Deep technical expertise in Java and system design**✅ **Strong problem-solving skills with real-world examples**✅ **Clear communication and leadership mindset**✅ **Ability to balance technical and business perspectives**

---

## 176. Can you explain the principles of object-oriented design and how they apply to Java development?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Object-oriented design (OOD) is a programming paradigm that revolves around the concept of “objects,” which are instances of classes containing both data and methods. These objects interact with each other to accomplish tasks, with an emphasis on encapsulation, inheritance, and polymorphism. In Java development, adherence to these principles is fundamental to writing robust, modular, and maintainable code.

Encapsulation is the practice of bundling data and methods that operate on the data within a single unit, typically a class. By encapsulating data, we hide its internal implementation details, exposing only a well-defined interface for interacting with it. This enhances code readability, facilitates code reuse, and helps prevent unintended modifications to the data.

Inheritance allows new classes to inherit attributes and methods from existing classes, enabling code reuse and promoting a hierarchical structure. In Java, classes can extend other classes to inherit their behavior, fostering a relationship between the parent (superclass) and child (subclass) classes. Through inheritance, common functionality can be centralized in base classes, promoting code organization and reducing redundancy.

Polymorphism, a cornerstone of OOD, refers to the ability of objects to take on multiple forms or behave differently based on their context. In Java, polymorphism is achieved through method overriding and method overloading. Method overriding enables subclasses to provide their own implementation of methods defined in the superclass, facilitating dynamic method dispatch and runtime flexibility. Method overloading allows multiple methods with the same name but different parameters to coexist within a class, improving code readability and conciseness.

Additionally, OOD emphasizes principles such as abstraction, which involves modeling real-world entities as simplified representations in code, and composition, which promotes building complex objects by combining simpler ones. These principles collectively contribute to the creation of modular, extensible, and adaptable software systems in Java development.

In summary, the principles of object-oriented design form the foundation of Java development, guiding developers in creating well-structured, maintainable, and scalable software solutions. By adhering to these principles, developers can write code that is not only functional but also robust, reusable, and easier to understand and maintain over time.

---

## 177. Describe a complex system or application you’ve designed using Java. What were the key design decisions you made, and why?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

One complex system I designed using Java was a comprehensive inventory management application for a retail company. The key design decisions focused on scalability, modularity, and maintainability to accommodate the company’s expanding inventory and evolving business needs.

One significant decision was to implement a layered architecture, separating the application into distinct layers such as presentation, business logic, and data access. This allowed for clear separation of concerns and facilitated easier maintenance and updates.

Additionally, I chose to utilize the Spring Framework to manage dependencies, handle inversion of control, and promote loose coupling between components. Spring’s dependency injection facilitated unit testing and simplified integration with third-party libraries.

Another crucial aspect was the use of a relational database management system (RDBMS) for data storage, with Hibernate as the ORM framework for object-relational mapping. This choice enabled efficient data retrieval and manipulation while abstracting away database-specific details.

Furthermore, I employed design patterns such as the Singleton pattern for managing global resources and the Factory pattern for creating instances of complex objects. These patterns enhanced code readability, promoted reusability, and contributed to overall system robustness.

Overall, these design decisions were made to ensure the scalability, flexibility, and maintainability of the inventory management system, enabling it to adapt to the company’s changing requirements and support future growth.

---

## 178. How do you ensure the scalability and maintainability of Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Scalability and maintainability in Java applications are ensured through several practices. Firstly, adhering to modular design principles and employing design patterns promotes code reusability and flexibility. Secondly, utilizing frameworks like Spring and Hibernate streamlines development and enhances scalability by handling complex functionalities. Additionally, continuous refactoring, automated testing, and documentation upkeep contribute to maintainability. Employing load balancing and caching techniques ensures Java applications can handle increased traffic. Lastly, monitoring performance metrics and employing cloud-based solutions facilitate scalability by dynamically allocating resources based on demand.

---

## 179. What are the differences between checked and unchecked exceptions in Java? When would you use each?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Checked exceptions are those that are checked at compile time and must be handled using try-catch blocks or declared in the method signature. They typically represent exceptional conditions that a well-behaved application should anticipate and recover from, such as IOException or SQLException. Unchecked exceptions, on the other hand, are not checked at compile time and include runtime exceptions and errors. They often result from programming errors or unexpected conditions and can be handled optionally. Unchecked exceptions, like NullPointerException or IllegalArgumentException, are typically used for situations where recovery may not be feasible or practical.

---

## 180. How do you handle memory management and garbage collection in Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In Java applications, memory management is primarily handled by the Java Virtual Machine (JVM) through automatic garbage collection. The JVM dynamically allocates memory for objects and deallocates memory for objects that are no longer in use. Developers can optimize memory usage by minimizing object creation, avoiding memory leaks by ensuring proper object disposal, and using efficient data structures. Additionally, tuning JVM settings such as heap size and garbage collection algorithms can optimize performance. Through these practices, Java applications achieve efficient memory management, reducing the risk of memory leaks and improving overall performance and scalability.

---

## 181. What are the different ways to achieve concurrency in Java, and when would you use each?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Java offers several mechanisms to achieve concurrency, each suited for different use cases:

**1. Threads:** Java’s `**Thread**` class and the `**Runnable**` interface provide the basic building blocks for concurrent programming. Threads are lightweight processes that execute independently, making them suitable for simple concurrent tasks or when fine-grained control over execution is required.

**2. Executor Framework:** The `**Executor**` framework provides a higher-level abstraction for managing thread execution. It includes interfaces like `**ExecutorService**`, `**ThreadPoolExecutor**`, and `**ScheduledExecutorService**`, which handle thread creation, pooling, scheduling, and lifecycle management. This approach is suitable for managing thread lifecycles, resource management, and workload distribution in concurrent applications.

**3. Fork/Join Framework:** Introduced in Java 7, the Fork/Join framework enables parallel execution of recursive tasks by dividing them into smaller subtasks and combining their results. It is particularly useful for embarrassingly parallel problems and recursive algorithms, such as divide-and-conquer algorithms.

**4. Java Concurrency Utilities:** Java provides a rich set of concurrency utilities in the `**java.util.concurrent**` package, including concurrent collections (e.g., `**ConcurrentHashMap**`, `**ConcurrentLinkedQueue**`), synchronization utilities (e.g., `**CountDownLatch**`, `**Semaphore**`), and atomic variables (e.g., `**AtomicInteger**`, `**AtomicReference**`). These utilities simplify concurrent programming tasks and address common concurrency challenges.

**5. Locks and Synchronization:** Java supports synchronization mechanisms such as synchronized blocks, `**Lock**` interfaces (`**ReentrantLock**`, `**ReadWriteLock**`), and `**Condition**` objects for managing access to shared resources and coordinating execution among threads. These mechanisms are suitable for fine-grained control over synchronization and when more sophisticated synchronization techniques are needed.

**6. Parallel Streams:** Introduced in Java 8, parallel streams leverage the Fork/Join framework under the hood to execute stream operations concurrently across multiple threads. They are suitable for processing large data sets in parallel and exploiting multi-core processors to improve performance.

The choice of concurrency mechanism depends on factors such as the nature of the problem, the level of control required over thread execution, scalability requirements, and the complexity of synchronization. Understanding the strengths and weaknesses of each mechanism is essential for selecting the most appropriate approach for a given scenario.

---

## 182. How do you identify and resolve performance bottlenecks in Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Identifying and resolving performance bottlenecks in Java applications involves a systematic approach and the use of various profiling and monitoring tools. Here’s a general process:

**1. Performance Profiling:** Use profiling tools like Java VisualVM, JProfiler, or YourKit to identify performance bottlenecks. Profiling helps pinpoint areas of code that consume significant resources, such as CPU time, memory, or I/O operations.

**2. Benchmarking:** Develop benchmarks and performance tests to measure the performance of different components or modules of the application. This helps establish baseline performance metrics and identify areas for improvement.

**3. Code Review and Analysis:** Conduct a thorough code review to identify inefficient algorithms, resource-intensive operations, or potential concurrency issues. Look for common performance anti-patterns such as excessive object creation, unnecessary synchronization, or inefficient database queries.

**4. Optimization Techniques:** Once performance bottlenecks are identified, apply optimization techniques such as:

👉Algorithm optimization: Use more efficient algorithms or data structures to improve performance.

👉Caching: Cache frequently accessed data or computation results to reduce redundant calculations or database queries.

👉Multithreading and concurrency: Utilize concurrent programming techniques to parallelize tasks and improve throughput.

👉Database optimization: Optimize database queries, indexing, and caching strategies to reduce latency and improve response times.

👉Memory management: Minimize memory usage by avoiding memory. leaks, optimizing object creation and destruction, and tuning garbage collection settings.

**5. Performance Testing:** Perform thorough performance testing after applying optimizations to validate improvements and ensure that the changes have not introduced regressions or new bottlenecks.

**6. Continuous Monitoring:** Implement monitoring solutions to continuously monitor the performance of the application in production. Use tools like Prometheus, Grafana, or New Relic to track key performance metrics and identify any performance degradation or anomalies in real-time.

By following these steps and leveraging appropriate tools and techniques, developers can effectively identify and resolve performance bottlenecks in Java applications, ultimately improving the overall performance, scalability, and reliability of the software system.

---

## 183. What tools and methodologies do you use for profiling and performance testing Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Profiling and performance testing Java applications involve using various tools and methodologies to identify performance bottlenecks, analyze resource utilization, and optimize code. Here are some commonly used tools and methodologies:

**1. Profiling Tools:**

**Java VisualVM:** A graphical tool bundled with the JDK that provides real-time monitoring, profiling, and diagnostic capabilities for Java applications. It offers features such as CPU, memory, and thread profiling, heap dump analysis, and garbage collection monitoring.

**JProfiler:** A commercial Java profiler that offers advanced profiling capabilities, including CPU and memory profiling, thread analysis, JDBC and JPA monitoring, and integration with various IDEs.

**YourKit Java Profiler:** Another commercial Java profiler known for its low overhead and rich feature set, including CPU and memory profiling, thread and deadlock detection, and profiling of Java EE applications.

**2. Performance Testing Tools:**

**Apache JMeter:** An open-source tool for load testing and performance measurement of web applications. It simulates concurrent user activity and measures the application’s response time, throughput, and scalability under various load conditions.

**Gatling:** A high-performance open-source load testing tool written in Scala. It allows for scripting performance tests using a DSL (Domain Specific Language) and provides detailed performance metrics and reports.

**Apache Bench (ab):** A command-line tool for benchmarking web servers by sending multiple concurrent requests and measuring the server’s response time and throughput.

**3. Methodologies:**

**Continuous Performance Testing:** Integrate performance testing into the continuous integration/continuous delivery (CI/CD) pipeline to ensure that performance regressions are detected early in the development cycle.

**Real User Monitoring (RUM):** Monitor and analyze the performance of production applications by capturing and analyzing real user data, such as page load times, transaction durations, and error rates.

**A/B Testing:** Conduct experiments by comparing the performance of different versions or configurations of the application under real-world conditions to determine the impact of changes on performance metrics.

**4. Monitoring and Observability:**

**Application Performance Monitoring (APM) Tools:** Use APM solutions such as New Relic, AppDynamics, or Dynatrace to monitor the performance of Java applications in production environments. These tools provide insights into application performance, transaction traces, and infrastructure metrics in real-time.

By leveraging these tools and methodologies, developers and performance engineers can effectively profile, test, and optimize the performance of Java applications, ensuring they meet performance requirements and deliver a superior user experience.

---

## 184. Have you worked with any Java frameworks such as Spring, Hibernate, or Apache Camel? Can you discuss your experience with them?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

As an AI developed by OpenAI, I don’t have personal experiences, but I can provide insights into these frameworks based on common use cases and industry standards.

1. **Spring Framework:**
- Spring is a comprehensive framework for building enterprise Java applications. It offers a wide range of features, including dependency injection, aspect-oriented programming, data access, transaction management, and MVC web application development.
- Myriad modules within Spring, such as Spring Core, Spring MVC, Spring Data, and Spring Security, cater to different aspects of application development.
- Spring Boot, a part of the Spring ecosystem, simplifies the setup and configuration of Spring-based applications, allowing developers to quickly bootstrap and deploy production-ready applications.
1. **Hibernate:**
- Hibernate is an object-relational mapping (ORM) framework that simplifies database interaction in Java applications. It provides a mapping between Java objects and database tables, allowing developers to work with objects rather than SQL queries.
- Hibernate handles database operations, such as CRUD (Create, Read, Update, Delete) operations and complex queries, abstracting away low-level JDBC code.
- Features like caching, lazy loading, and automatic schema generation contribute to improved performance and developer productivity.
1. **Apache Camel:**
- Apache Camel is an open-source integration framework that facilitates the integration of disparate systems and applications using enterprise integration patterns (EIPs).
- It provides a lightweight, declarative, and highly configurable way to define and route messages between different endpoints, such as HTTP, JMS, FTP, and databases.
- Camel supports various communication protocols, data formats, and message processing capabilities, making it suitable for building scalable and resilient integration solutions.

Overall, these frameworks play vital roles in Java development, offering robust solutions for building enterprise-grade applications, simplifying database interaction, and facilitating integration between heterogeneous systems. Each framework has its strengths and use cases, and their adoption often depends on project requirements, team preferences, and industry standards.

---

## 185. Explain the role of dependency injection in Spring Framework. How does it improve code maintainability and testability?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Dependency injection (DI) is a fundamental concept in the Spring Framework that facilitates loose coupling between components by externalizing the dependencies of a class. In DI, dependencies are “injected” into a class rather than being created or managed by the class itself. This inversion of control (IoC) allows for more modular, flexible, and maintainable code.

The role of dependency injection in the Spring Framework can be summarized as follows:

1. **Decoupling Components:** Dependency injection decouples the classes or components from their dependencies, allowing them to be easily replaced or modified without affecting the overall system. This promotes modularity and enables easier maintenance and evolution of the codebase.
2. **Configuration Flexibility:** Dependency injection allows dependencies to be configured externally, typically through XML configuration files, Java annotations, or Java-based configuration classes. This makes it easy to configure and change dependencies without modifying the code, promoting flexibility and enabling different configurations for different environments (e.g., development, testing, production).
3. **Simplifying Dependency Management:** By externalizing the management of dependencies, DI reduces the complexity of managing object creation, lifecycle management, and dependency resolution within the application code. This simplification leads to cleaner, more concise code that focuses on business logic rather than infrastructure concerns.
4. **Promoting Testability:** Dependency injection enhances the testability of code by facilitating easier isolation and mocking of dependencies during unit testing. By injecting mock or stub implementations of dependencies, developers can write focused unit tests that verify the behavior of individual components in isolation, without requiring the presence of external resources or dependencies.
5. **Encouraging Best Practices:** Dependency injection encourages adherence to best practices such as the single responsibility principle (SRP) and the dependency inversion principle (DIP). By separating concerns and promoting modular, reusable components, DI helps maintain a clear separation of responsibilities and promotes better code organization and maintainability.

In summary, dependency injection plays a crucial role in the Spring Framework by promoting loose coupling, configuration flexibility, simplified dependency management, and improved testability. By adhering to the principles of DI, developers can write cleaner, more maintainable, and more testable code, leading to higher-quality software solutions.

---

## 186. Describe your experience leading a team of Java developers. How do you foster collaboration and communication within the team?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

While I don’t have personal experiences to draw from, I can provide insights into leading a team of Java developers based on common best practices and industry standards.

Leading a team of Java developers involves not only overseeing technical aspects but also fostering collaboration, communication, and a positive team culture. Here’s how one might go about it:

1. **Setting Clear Goals and Expectations:** Clearly communicate project goals, objectives, and expectations to the team. Ensure everyone understands their roles, responsibilities, and deadlines to foster a sense of ownership and accountability.
2. **Encouraging Open Communication:** Create an environment where team members feel comfortable expressing their ideas, concerns, and feedback. Hold regular team meetings, one-on-one discussions, and open forums to facilitate communication and collaboration.
3. **Promoting Knowledge Sharing:** Encourage knowledge sharing and collaboration among team members by organizing regular knowledge-sharing sessions, code reviews, pair programming sessions, and tech talks. This helps spread expertise across the team and fosters a culture of continuous learning.
4. **Providing Support and Guidance:** Be available to support team members, provide guidance, and remove obstacles that hinder their progress. Offer mentorship, coaching, and constructive feedback to help them grow and develop their skills.
5. **Empowering the Team:** Empower team members to make decisions, take ownership of their work, and contribute to the project’s success. Delegate tasks and responsibilities based on each team member’s strengths and expertise, allowing them to take on leadership roles and grow professionally.
6. **Celebrating Successes and Learning from Failures:** Recognize and celebrate team achievements, milestones, and successes to boost morale and motivation. Likewise, use failures and setbacks as opportunities for learning and improvement, fostering a culture of resilience and continuous improvement.
7. **Promoting Diversity and Inclusivity:** Foster a diverse and inclusive team environment where everyone feels valued, respected, and included. Embrace different perspectives, backgrounds, and ideas, as they enrich team dynamics and contribute to innovation and creativity.
8. **Leading by Example:** Lead by example by demonstrating professionalism, integrity, and a strong work ethic. Show enthusiasm, passion, and dedication for the project and the team’s success, inspiring others to do the same.

By implementing these strategies and practices, a leader can effectively foster collaboration, communication, and teamwork within a team of Java developers, ultimately leading to improved productivity, morale, and project success.

---

## 187. How do you handle conflicts or disagreements among team members during the development process?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Handling conflicts or disagreements among team members during the development process requires a combination of communication, empathy, and conflict resolution skills. Here’s a step-by-step approach:

1. **Address the Issue Promptly:** Address conflicts or disagreements as soon as they arise, rather than allowing them to escalate. Encourage open communication and create a safe space for team members to express their concerns.
2. **Listen Actively:** Actively listen to both sides of the conflict without judgment. Allow each team member to share their perspective, concerns, and feelings. Ensure that everyone feels heard and understood.
3. **Identify the Root Cause:** Work with the team to identify the underlying causes of the conflict or disagreement. Encourage team members to focus on the issue at hand rather than personal differences.
4. **Find Common Ground:** Look for areas of agreement or common goals that can serve as a starting point for resolution. Encourage collaboration and brainstorming to find mutually acceptable solutions.
5. **Encourage Empathy:** Foster empathy and understanding among team members by encouraging them to consider each other’s perspectives and feelings. Help team members see the situation from the other person’s point of view.
6. **Facilitate Communication:** Facilitate constructive communication and dialogue between conflicting parties. Encourage respectful and assertive communication, while discouraging blame, criticism, or personal attacks.
7. **Seek Mediation if Necessary:** If the conflict persists or escalates, consider involving a neutral third party, such as a team leader or HR representative, to mediate the discussion and facilitate resolution.
8. **Focus on Solutions:** Encourage the team to focus on finding solutions rather than dwelling on the conflict itself. Brainstorm alternative approaches, compromise when necessary, and work together to implement agreed-upon solutions.
9. **Follow Up:** Follow up with team members after the conflict has been resolved to ensure that the issue has been fully addressed and that everyone is satisfied with the outcome. Encourage ongoing communication and collaboration to prevent future conflicts.

By following these steps and promoting a culture of open communication, empathy, and collaboration, conflicts or disagreements among team members can be effectively managed and resolved, leading to a more positive and productive work environment.

---

## 188. Can you provide an example of a successful project you led, highlighting your leadership approach and its impact on the project outcome?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

While I can’t provide a personal example, I can offer a hypothetical scenario based on common leadership principles and best practices:

As a project leader, I led a software development project aimed at building a new e-commerce platform for a retail client. The project involved a cross-functional team of developers, designers, and QA engineers, and had aggressive timelines and complex requirements.

**Leadership Approach:**

1. **Clear Vision and Goal Setting:** I started by defining a clear vision and project goals, ensuring that every team member understood the project’s objectives and their role in achieving them. I emphasized the importance of delivering a high-quality, user-friendly e-commerce platform that met the client’s needs and expectations.
2. **Empowering the Team:** I empowered team members by providing them with autonomy, ownership, and trust to make decisions and solve problems. I encouraged collaboration, creativity, and innovation, allowing team members to explore different approaches and ideas.
3. **Effective Communication:** I fostered open, transparent communication within the team, ensuring that everyone had the information they needed to perform their roles effectively. I held regular team meetings, one-on-one discussions, and status updates to keep everyone informed and aligned.
4. **Conflict Resolution:** Whenever conflicts or disagreements arose within the team, I addressed them promptly and constructively. I encouraged open dialogue, active listening, and empathy, helping team members understand each other’s perspectives and find mutually acceptable solutions.
5. **Continuous Improvement:** Throughout the project lifecycle, I promoted a culture of continuous improvement and learning. I encouraged feedback, solicited input from team members, and identified opportunities for process optimization and skill development.

**Impact on Project Outcome:**

Despite the project’s challenges and tight deadlines, my leadership approach had a significant impact on the project outcome:

1. **Successful Delivery:** The project was delivered on time and within budget, meeting all key milestones and deliverables. The e-commerce platform was launched successfully, providing a seamless shopping experience for the client’s customers.
2. **High Quality:** The final product was of high quality, with robust functionality, intuitive user interface, and minimal defects. This was achieved through rigorous testing, code reviews, and adherence to best practices throughout the development process.
3. **Client Satisfaction:** The client was highly satisfied with the outcome of the project, praising the team’s professionalism, expertise, and commitment to delivering a top-notch solution. The e-commerce platform exceeded their expectations and contributed to their business growth and success.
4. **Team Morale and Engagement:** My leadership approach fostered a positive team culture, where team members felt valued, motivated, and engaged. Morale was high, and turnover was low, resulting in a cohesive, productive team environment.

In summary, by leveraging effective leadership principles and practices, I was able to lead a successful software development project that met the client’s objectives, exceeded expectations, and contributed to the overall success of the organization.

---

## 189. What coding standards and best practices do you follow when writing Java code?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

When writing Java code, adhering to coding standards and best practices is crucial for ensuring readability, maintainability, and consistency across the codebase. Here are some commonly followed coding standards and best practices:

1. **Naming Conventions:**
- Use meaningful and descriptive names for classes, variables, methods, and packages.
- Follow camelCase for variable and method names (e.g., `firstName`, `calculateTotal`).
- Use PascalCase for class names (e.g., `CustomerService`, `OrderProcessor`).
- Use uppercase for constant variables (e.g., `MAX_LENGTH`, `DEFAULT_TIMEOUT`).

**2. Formatting:**

- Use consistent indentation (usually four spaces) for code blocks.
- Limit line length to improve readability (typically 80–120 characters per line).
- Use whitespace sparingly and consistently to enhance readability.
- Follow a consistent code style for braces, line breaks, and spacing.

**3. Comments:**

- Write clear and concise comments to explain the purpose, behavior, and usage of classes, methods, and variables.
- Avoid unnecessary comments that merely duplicate the code.
- Update comments regularly to keep them in sync with the code.

**4. Error Handling:**

- Handle exceptions appropriately using try-catch blocks or propagate them to the calling code.
- Avoid catching generic exceptions (`Exception`) unless necessary; instead, catch specific exceptions.
- Log exceptions with appropriate context and level of detail for debugging and troubleshooting.

**5. Coding Practices:**

- Follow the single responsibility principle (SRP) and keep classes and methods focused on a single task.
- Minimize method and class complexity by breaking down complex logic into smaller, more manageable units.
- Use meaningful and descriptive method names to convey their purpose and behavior.
- Avoid hardcoded values and magic numbers; use constants or configuration properties instead.
- Favor immutability where possible to reduce side effects and improve thread safety.

**6. Testing:**

- Write comprehensive unit tests to validate the behavior of individual classes and methods.
- Follow test-driven development (TDD) principles to write tests before implementing the code.
- Use mocking frameworks (e.g., Mockito) to isolate dependencies and simulate behavior in unit tests.

**7. Version Control:**

- Use version control systems (e.g., Git) to manage code changes and collaborate with team members.
- Follow best practices for branching, committing, and merging code changes to maintain a clean and stable codebase.

**8. Documentation:**

- Write clear and concise documentation for classes, methods, and APIs using Javadoc comments.
- Document method parameters, return values, and exceptions to guide developers in using the code effectively.

By following these coding standards and best practices, developers can produce high-quality, maintainable Java code that is easy to understand, test, and maintain.

---

## 190. How do you ensure code quality and maintainability in your Java projects?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Ensuring code quality and maintainability in Java projects involves a combination of practices, tools, and methodologies aimed at producing clean, well-structured, and easily maintainable code. Here’s how to achieve this:

1. **Adherence to Coding Standards:**
- Enforce coding standards and best practices, such as naming conventions, code formatting, and documentation guidelines, to maintain consistency and readability across the codebase.

**2. Code Reviews:**

- Conduct regular code reviews to identify and address issues such as code smells, anti-patterns, and potential bugs. Peer review helps catch errors early, promotes knowledge sharing, and ensures code quality.

**3. Unit Testing:**

- Write comprehensive unit tests to validate the behavior of individual components and ensure they meet the specified requirements. Use tools like JUnit and Mockito for writing and executing unit tests.

**4. Test Automation:**

- Automate repetitive testing tasks, such as unit testing, integration testing, and regression testing, to ensure consistent and reliable test coverage. Utilize continuous integration (CI) tools like Jenkins or Travis CI to automate the execution of tests on every code commit.

**5. Static Code Analysis:**

- Use static code analysis tools like SonarQube, PMD, and Checkstyle to analyze code for potential bugs, security vulnerabilities, and code smells. These tools provide automated checks and generate reports to identify areas for improvement.

**6. Refactoring:**

- Regularly refactor code to improve its design, readability, and maintainability. Eliminate duplicate code, extract reusable components, and apply design patterns to simplify complex code and reduce technical debt.

**7. Documentation:**

- Maintain up-to-date documentation for code, APIs, and architectural decisions to facilitate understanding and future maintenance. Use tools like Javadoc and Swagger for generating API documentation.

**8. Continuous Integration/Continuous Deployment (CI/CD):**

- Implement CI/CD pipelines to automate the build, test, and deployment process. Ensure that every code change is automatically built, tested, and deployed to production, reducing the risk of introducing bugs and improving the overall quality of the software.

**9. Monitoring and Feedback:**

- Monitor application performance, error rates, and user feedback to identify areas for improvement and prioritize enhancements. Use tools like Prometheus, Grafana, and New Relic for monitoring application metrics in real-time.

**10. Training and Knowledge Sharing:**

- Invest in training and skill development for team members to stay updated with the latest technologies, best practices, and industry trends. Foster a culture of knowledge sharing through workshops, brown bag sessions, and internal tech talks.

By implementing these practices and leveraging appropriate tools and technologies, developers can ensure high code quality and maintainability in Java projects, leading to better software reliability, scalability, and customer satisfaction.

---

## 191. What security considerations do you take into account when developing Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

When developing Java applications, it’s crucial to consider security at every stage of the development lifecycle to protect against potential vulnerabilities and threats. Here are some key security considerations to take into account:

1. **Input Validation:**
- Validate all input received from users, including data from forms, APIs, and external sources, to prevent injection attacks such as SQL injection, XSS (Cross-Site Scripting), and CSRF (Cross-Site Request Forgery).

**2. Authentication and Authorization:**

- Implement strong authentication mechanisms, such as multi-factor authentication (MFA), OAuth, or OpenID Connect, to verify the identity of users and prevent unauthorized access to sensitive resources.
- Use role-based access control (RBAC) or attribute-based access control (ABAC) to enforce fine-grained authorization policies and limit access to privileged operations and data.

**3. Session Management:**

- Secure session management by using secure cookies, session tokens, or JWT (JSON Web Tokens) with proper expiration, encryption, and validation mechanisms to prevent session hijacking and replay attacks.

**4. Secure Communication:**

- Encrypt sensitive data transmitted over the network using protocols like HTTPS/TLS to ensure confidentiality and integrity. Use secure cipher suites, certificate pinning, and secure headers to mitigate common network-based attacks.

**5. Data Encryption:**

- Encrypt sensitive data at rest using strong encryption algorithms and key management practices to protect against unauthorized access in case of data breaches or unauthorized access to storage devices.

**6. Secure Coding Practices:**

- Follow secure coding practices and principles, such as the principle of least privilege, to minimize the attack surface and reduce the risk of common vulnerabilities like buffer overflows, injection attacks, and insecure deserialization.
- Utilize secure coding libraries and frameworks, such as OWASP ESAPI (Enterprise Security API) or Apache Shiro, to handle security-sensitive tasks like input validation, authentication, and encryption.

**7. Error Handling and Logging:**

- Implement proper error handling and logging mechanisms to provide meaningful error messages to users while preventing information disclosure. Avoid exposing sensitive information in error messages or logs that could aid attackers in exploiting vulnerabilities.

**8. Regular Security Audits and Testing:**

- Conduct regular security audits, code reviews, and penetration testing to identify security vulnerabilities and weaknesses in the application. Utilize automated security testing tools like OWASP ZAP, Burp Suite, or SonarQube to scan for common security flaws and misconfigurations.

**9. Patch Management:**

- Stay up-to-date with security patches and updates for the Java runtime environment, libraries, and dependencies used in the application. Regularly monitor security advisories and apply patches promptly to mitigate known vulnerabilities.

**10. Security Training and Awareness:**

- Provide security training and awareness programs for developers, testers, and other stakeholders to educate them about common security threats, best practices, and mitigation strategies. Foster a security-conscious culture within the development team.

By incorporating these security considerations into the development process, developers can build Java applications that are resilient to attacks, protect sensitive data, and maintain the trust of users and stakeholders.

---

## 192. How do you ensure compliance with industry standards and regulations in your Java projects?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Ensuring compliance with industry standards and regulations in Java projects is essential for meeting legal requirements, protecting sensitive data, and maintaining trust with customers and stakeholders. Here’s how I ensure compliance with industry standards and regulations:

1. **Understand Regulatory Requirements:**
- Begin by understanding the relevant industry standards, regulations, and compliance requirements that apply to the project. This may include standards like ISO/IEC 27001 for information security management or regulations like GDPR, HIPAA, or PCI DSS.

**3. Incorporate Security by Design:**

- Implement security by design principles from the outset of the project to build security into the architecture, design, and development process. Consider security requirements alongside functional requirements and prioritize security controls accordingly.

**4. Risk Assessment and Mitigation:**

- Conduct risk assessments to identify potential security risks, vulnerabilities, and threats to the application. Assess the impact and likelihood of each risk and implement appropriate controls and mitigation measures to reduce risk to an acceptable level.

**5. Adopt Secure Coding Practices:**

- Follow secure coding practices and guidelines, such as those outlined by OWASP (Open Web Application Security Project), to mitigate common security vulnerabilities and weaknesses in the codebase. This includes practices like input validation, output encoding, and proper error handling.

**6. Data Protection and Privacy:**

- Implement measures to protect sensitive data and ensure compliance with data protection regulations like GDPR (General Data Protection Regulation). This may include encryption of sensitive data, pseudonymization, data minimization, and ensuring user consent for data processing.

**7. Access Control and Authentication:**

- Implement strong access controls and authentication mechanisms to restrict access to sensitive resources and prevent unauthorized access. Utilize principles like least privilege, role-based access control (RBAC), and multi-factor authentication (MFA) where appropriate.

**8. Auditing and Logging:**

- Implement robust logging and auditing mechanisms to track and monitor user activities, system events, and security-relevant actions. Ensure that logs are generated, retained, and protected according to regulatory requirements and best practices.

**9. Regular Security Assessments:**

- Conduct regular security assessments, audits, and penetration tests to evaluate the effectiveness of security controls, identify vulnerabilities, and ensure ongoing compliance with industry standards and regulations.

**10. Documentation and Compliance Reporting:**

- Maintain accurate and up-to-date documentation of security controls, policies, procedures, and compliance efforts. Prepare compliance reports, documentation, and evidence as required by regulatory authorities or auditors.

**11. Continuous Improvement:**

- Continuously monitor and improve security posture by staying informed about emerging threats, vulnerabilities, and best practices. Adapt security controls and practices as necessary to address evolving risks and regulatory requirements.

By integrating these practices into the development process, I ensure that Java projects adhere to industry standards and regulations, mitigating risks, protecting data, and maintaining compliance with legal and regulatory requirements.

---

## 193. Can you discuss your experience implementing authentication and authorization mechanisms in Java applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

While I can’t provide personal experience, I can offer insights into implementing authentication and authorization mechanisms in Java applications based on best practices and common approaches.

1. **Authentication:**
- Implement authentication to verify the identity of users accessing the application.
- Common authentication mechanisms in Java applications include:
- **Username and Password:** Authenticate users with a combination of a username and password. Use strong password hashing algorithms like bcrypt or PBKDF2 to securely store passwords.
- **OAuth/OpenID Connect:** Integrate with OAuth or OpenID Connect providers for federated authentication, allowing users to sign in using third-party identity providers like Google, Facebook, or GitHub.
- **LDAP/Active Directory:** Authenticate users against LDAP (Lightweight Directory Access Protocol) or Active Directory servers for centralized authentication and user management.
- **Multi-Factor Authentication (MFA):** Enhance security by implementing MFA, requiring users to provide multiple factors of authentication (e.g., password + OTP, password + biometric).
- Ensure secure transmission of authentication credentials over the network using HTTPS/TLS to prevent eavesdropping and man-in-the-middle attacks.

**2. Authorization:**

- Implement authorization to control access to resources and functionalities within the application.
- Common authorization mechanisms in Java applications include:
- **Role-Based Access Control (RBAC):** Assign roles (e.g., admin, user, guest) to users and define access permissions based on roles. Use annotations like `@PreAuthorize` or programmatic checks to enforce authorization rules.
- **Attribute-Based Access Control (ABAC):** Define access policies based on user attributes (e.g., department, location, job title) and resource attributes. Use frameworks like Spring Security’s Expression-Based Access Control or external policy engines like XACML (eXtensible Access Control Markup Language).
- **JSON Web Tokens (JWT):** Use JWT for stateless authentication and authorization. Encode user claims (e.g., roles, permissions) into JWTs and validate them on subsequent requests.
- Enforce authorization checks at both the application level (e.g., controllers, services) and the data level (e.g., database queries, API calls) to ensure comprehensive access control.

**3. Session Management:**

- Manage user sessions securely to maintain authentication state and prevent session-related attacks.
- Use techniques like session tokens, secure cookies, or JWTs with short expiration times to manage user sessions.
- Implement session fixation prevention, session hijacking detection, and session invalidation mechanisms to mitigate session-related threats.

**4. Secure Configuration:**

- Securely configure authentication and authorization settings, such as password policies, session timeout periods, and access control rules.
- Store sensitive configuration settings (e.g., API keys, encryption keys) securely, using environment variables or secure storage mechanisms, and avoid hardcoding them in source code or configuration files.

**5. Logging and Monitoring:**

- Log authentication and authorization events for auditing and monitoring purposes. Include relevant details such as user identity, timestamp, and outcome (success or failure).
- Monitor authentication and authorization metrics, such as failed login attempts, successful logins, and access control violations, to detect and respond to security incidents in real-time.

By implementing robust authentication and authorization mechanisms in Java applications, developers can ensure that only authorized users can access sensitive resources and functionalities, protecting against unauthorized access and maintaining the security and integrity of the application.

---

## 194. What is Spring Boot and how is it different from Spring?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Spring Boot is a framework built on top of the Spring Framework that helps in **rapid application development** by providing **default configurations**, **auto-setup**, and **opinionated starter templates**.

*Difference:*

- Spring requires a lot of configuration.
- Spring Boot reduces boilerplate code and provides embedded servers, auto-configuration, and starters.

Spring vs Spring Boot

---

## 195. What is auto-configuration in Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Auto-configuration in Spring Boot** is one of the core features that makes development faster and easier. It allows Spring Boot to automatically configure your application based on the **dependencies present in your classpath** and the **beans you define**.

**🔍 What Does Auto-Configuration Mean?**

In traditional Spring applications, you have to explicitly define configuration for things like:

- DataSource
- JPA setup
- DispatcherServlet
- Message converters
- Web MVC config
- Caching setup

> With Spring Boot’s auto-configuration, most of this setup is done automatically based on conventions and project setup.
> 

**⚙️ How It Works:**

- Spring Boot uses the `@EnableAutoConfiguration` annotation (usually included via `@SpringBootApplication`) to **enable automatic bean configuration**.
- It scans your **classpath**, checks for the **presence of specific classes or libraries**, and then configures related beans accordingly.

Example:If `spring-boot-starter-data-jpa` is present:

- Spring Boot automatically sets up:
- DataSource
- EntityManager
- TransactionManager
- JPA repositories

**📦 Common Auto-Configured Components:**

**Common Auto-Configured Components**

**🛠️ Can I Customize It?**

Yes! Auto-configuration is smart but flexible:

- You can **override** auto-configured beans by defining your own.
- Use `@ConditionalOnMissingBean`, `@ConditionalOnClass`, and other annotations to control when a config should apply.
- You can also **disable specific auto-configurations** using:

```
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })
```

**Benefits:**

- **Faster development**
- **Less boilerplate**
- **Simplifies project setup**
- **Easy integration with third-party tools**

---

## 196. What are Spring Boot Starters?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Starters are a set of convenient dependency descriptors you can include in your project. For example:

- `spring-boot-starter-web`: Includes Tomcat, Spring MVC, Jackson.
- `spring-boot-starter-data-jpa`: Includes Hibernate and Spring Data JPA.

---

## 197. What are functional interfaces in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Functional interfaces are interfaces with **a single abstract method**, making them ideal for **lambda expressions** and **method references**.

**Example**:

```
@FunctionalInterface
interface MyFunction {
    void execute();
}
```

---

## 198. Explain the use of Optional in Java 8

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

`Optional` is used to represent a **value that may or may not be present**, helping avoid `NullPointerException`.

```
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(System.out::println);
```

---

## 199. How do you create a REST API using Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

```
@RestController
@RequestMapping("/api")
public class UserController {

    @GetMapping("/users")
    public List<User> getAllUsers() {
        return userService.findAll();
    }
}
```

Spring Boot automatically handles JSON conversion via Jackson and handles dependency injection via `@Autowired`.

---

## 200. How do you handle exceptions in REST APIs?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Using `@ControllerAdvice` and `@ExceptionHandler`.

```
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<String> handleUserNotFound() {
        return new ResponseEntity<>("User not found", HttpStatus.NOT_FOUND);
    }
}
```

---

## 201. What is the difference between @Component, @Service, and @Repository?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In Spring Framework, `@Component`, `@Service`, and `@Repository` are all **stereotype annotations** used for defining Spring beans. While they function similarly in terms of bean registration, they are used for different **semantic purposes** and provide **specific behaviors** in certain layers of the application.

**📊 Comparison Table: `@Component` vs `@Service` vs `@Repository`**

**`@Component` vs `@Service` vs `@Repository`**

---

## 202. What is Spring Boot Actuator?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Spring Boot Actuator provides **production-ready features** such as health checks, metrics, and environment details via endpoints.

```
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Endpoints like `/actuator/health`, `/actuator/metrics` are available.

---

## 203. How do you manage database migrations in Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Using **Flyway** or **Liquibase**. Spring Boot provides out-of-the-box support for Flyway.

```
<dependency>
  <groupId>org.flywaydb</groupId>
  <artifactId>flyway-core</artifactId>
</dependency>
```

---

## 204. How to secure REST APIs in Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Use **Spring Security** with JWT tokens or OAuth2.

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests()
            .anyRequest().authenticated();
    }
}
```

---

## 205. How do you optimize Spring Boot applications?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Use lazy initialization
- Reduce unnecessary autowiring
- Use caching (`@Cacheable`)
- Use asynchronous methods (`@Async`)
- Optimize database queries with pagination

---

## 206. Suppose your Spring Boot app is taking a long time to start. How would you troubleshoot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Enable **debug logs** using `-debug` flag.
- Use **Actuator** to inspect startup stages.
- Analyze **Spring beans loading** time.
- Profile memory usage during startup.

---

## 207. Your REST API returns too much data. What’s the solution?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Use **pagination** (`Pageable`)
- Use **DTOs** to return only required fields
- Implement **response compression**

---

## 208. Write Clean, Readable Code

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Follow standard naming conventions (`camelCase`, `PascalCase`).
- Keep methods short and focused on a single task.
- Avoid magic numbers and hardcoded strings — use constants.

---

## 209. Write Unit & Integration Tests

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Follow TDD (Test-Driven Development) when possible.
- Use JUnit, Mockito, Testcontainers, and other tools.
- Aim for high test coverage **with meaningful assertions**.

---

## 210. What Does a Java Architect Do?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

At a high level, a Java Architect is responsible for designing the **overall architecture** of enterprise-grade applications using Java-based technologies. But the reality is deeper:

What Does a Java Architect Do

---

## 211. Tell me about a time you had to choose between two competing technologies.

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

🧩 **What they’re looking for:**

- Technical evaluation
- Business alignment
- Risk analysis

✅ **How to answer:** Use the **STAR method (Situation, Task, Action, Result)**.

> “In a past project, we debated between Kafka and RabbitMQ for an event-driven system. I evaluated message durability, throughput needs, and developer familiarity. Kafka aligned better with our long-term scaling plans. We ran a PoC, confirmed results, and presented findings to leadership — saving us future migration headaches.”
>

---

## 212. How do you handle disagreements with developers or product managers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

🧩 **What they’re looking for:**

- Empathy and listening
- Conflict resolution
- Balancing business vs. technical needs

✅ **How to answer:**

> “I try to understand each perspective first. In one situation, the product team pushed for a quick release that risked tech debt. I proposed a phased delivery — meeting the deadline while preserving system health. Clear documentation and roadmap alignment helped everyone win.”
>

---

## 213. Describe a time you led a cross-functional technical initiative.

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

🧩 **What they’re looking for:**

- Ownership
- Communication across teams
- End-to-end system vision

✅ **How to answer:**

> “I led the redesign of our monolith into microservices. I broke the app into domains, assigned pods, set up CI/CD pipelines, and aligned with DevOps. The result? Faster releases and 40% improved system resilience.”
>

---

## 214. How do you mentor junior engineers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

🧩 **What they’re looking for:**

- Your leadership style
- Patience and teaching ability
- Culture contribution

✅ **How to answer:**

> “I assign shadowing tasks, review PRs with detailed feedback, and help juniors design small features independently. I also host weekly ‘architecture chats’ where they can ask questions openly. One mentee went from hesitant coder to confident lead in a year.”
>

---

## 215. Describe a mistake you made and what you learned.

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

🧩 **What they’re looking for:**

- Accountability
- Reflection and learning
- No finger-pointing

✅ **How to answer:**

> “In one project, I underestimated the caching layer’s complexity. A small misconfiguration led to stale data issues. I took responsibility, fixed it, and documented new caching guidelines. Now I always include caching in early design reviews.”
>

---

## 216. There were few questions on ConcurrentHashmap and other type of concurrent collection?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

> How to optimise performance of application and what will you do how will you take thread dump what are the tools?
> 

Optimizing the performance of an application involves several steps:

1. **Profiling**: Identify the bottlenecks in your application. This could be CPU usage, memory leaks, slow database queries, etc. Tools like VisualVM, JProfiler, or YourKit can be used for profiling Java applications.
2. **Optimize Code**: Look for inefficient code and try to optimize it. This could involve using more efficient data structures, reducing the time complexity of algorithms, reducing database calls, etc.
3. **Concurrency**: Use multithreading where appropriate to make use of multiple cores and perform tasks in parallel.
4. **Caching**: Implement caching to store the result of expensive operations, to avoid repeating them when the same inputs occur again.
5. **Database Optimization**: Optimize your database queries, use indexing, and normalize or denormalize your database as needed.
6. **Use of Latest Libraries/Frameworks**: Always try to use the latest libraries or frameworks as they usually come with performance improvements.

To take a thread dump:

1. **jstack**: This is a command-line utility that comes with the JDK. You can use it to take a thread dump of a running Java application. The command is `jstack <pid>`, where pid is the process id of the Java application.
2. **VisualVM**: This is a graphical tool that can be used to monitor a running Java application. It can also be used to take a thread dump.
3. **JConsole**: This is another graphical tool that comes with the JDK. It can be used to monitor a running Java application and take a thread dump.

> Stream based questions what are the type of streams in java-8?
> 

In Java 8, the term “streams” usually refers to a new abstraction introduced in the java.util.stream package, which allows you to perform functional-style operations on streams of elements. The Stream API is used to process collections of objects. A stream is a sequence of objects that supports various methods which can be pipelined to produce the desired result.

There are three types of Streams available in Java 8:

1. **Sequential Stream**: A sequential stream has a single pipeline and can process the elements only in sequence. It’s created by default when you call the `stream()` method.

List<String> list = Arrays.asList(“A”, “B”, “C”);

Stream<String> stream = list.stream();

**Parallel Stream**: A parallel stream has multiple pipelines and can process the elements in parallel, which can be faster than a sequential stream for large datasets on a multi-core machine. It’s created when you call the `parallelStream()` method.

List<String> list = Arrays.asList(“A”, “B”, “C”);

Stream<String> parallelStream = list.parallelStream();

**Infinite Stream**: These are streams that don’t have a fixed size, as in they can keep on growing. The `Stream.iterate` and `Stream.generate` methods can be used to create infinite streams.

Stream<Integer> infiniteStream = Stream.iterate(0, i -> i + 2);

Each type of stream is designed for a different kind of operation. Sequential and parallel streams are typically used with a finite number of elements, while infinite streams are used for generating a sequence of values on the fly.

> What is Join method in multithreading?
> 

its execution. If `t` is a `Thread` object whose thread is currently executing, then `t.join()` causes the current thread to pause its execution until `t`'s thread terminates.

Here’s a simple example:

```
Thread t1 = new Thread(new MyRunnable());
t1.start();
try {
t1.join(); // The current thread will wait until t1 finishes its execution
} catch (InterruptedException e) {
Thread.currentThread().interrupt();
}
// Continue with the logic after t1 has finished
```

In this example, the current thread will wait for `t1` to finish its execution before it continues. This can be useful in cases where you want to start another thread to perform some task, but you need the results of that task before you can proceed.

There are also overloaded versions of `join()` that allow you to specify a maximum amount of time that you're willing to wait for the other thread to finish:

- `join(long millis)` Waits at most `millis` milliseconds for this thread to die.
- `join(long millis, int nanos)` Waits at most `millis` milliseconds plus `nanos` nanoseconds for this thread to die.

If the thread doesn’t finish in that time, the `join()` call will return anyway, and the current thread will continue its execution.

> What is Objects class?
> 

The `Objects` class, introduced in Java 7, is a utility class that provides static methods to operate on objects. These utilities include null-safe or null-tolerant methods for computing the hash code of an object, returning a string for an object, comparing two objects, etc.

Here are some of the commonly used methods from the `Objects` class:

**`equals(Object a, Object b)`:** Checks if two objects are equal according to their `equals()` method. This method is null-safe, meaning if both objects are null, it returns true, and if one is null, it returns false.

Objects.equals(“test”, new String(“test”)); // returns true

Objects.equals(null, “test”); // returns false

Objects.equals(null, null); // returns true

**`hashCode(Object o)`:** Returns the hash code of a non-null argument and 0 for a null argument. Useful for null-safe hash code calculation.

Objects.hashCode(null); // returns 0

Objects.hashCode(“test”); // returns hash code of the string “test”

**`toString(Object o)`:** Returns the result of calling `toString` for a non-null argument and "null" for a null argument.

Objects.toString(null); // returns “null”

Objects.toString(“test”); // returns “test”

**`requireNonNull(T obj)`:** Checks that the specified object reference is not null. This method is designed primarily for doing parameter validation in methods and constructors.

Objects.requireNonNull(null); // throws NullPointerException

Objects.requireNonNull(“test”); // returns “test”

**`compare(T a, T b, Comparator<? super T> c)`:** Compares two objects with a given `Comparator`, and is null-safe.

The `Objects` class helps in writing cleaner and more robust code by providing null-safe methods.

> Difference between Flat vs Flat-map?
> 

`flat` and `flatMap` are operations that are used on collections or streams of data. The difference between them lies in how they handle nested structures.

1. **Flat**: The `flat` operation (not available in Java, but exists in some other languages) typically takes a structure that has multiple layers of nesting, and reduces one layer of nesting. It "flattens" the structure by one level. For example, if you have a list of lists, a `flat` operation would give you a single list that contains all the elements of the inner lists.
2. **FlatMap**: The `flatMap` operation is a combination of a `map` and a `flat` operation. It first applies a function to each element in the structure (like `map` does), but then it flattens the result. This is useful when the function you want to apply to each element produces a collection or a stream itself.

Here’s an example in Java:

```
List<String> list = Arrays.asList("Hello World", "Java Stream");
// map operation
List<String[]> mapResult = list.stream()
.map(s -> s.split(" "))
.collect(Collectors.toList());
// flatMap operation
List<String> flatMapResult = list.stream()
.flatMap(s -> Arrays.stream(s.split(" ")))
.collect(Collectors.toList());
```

In this example, the `map` operation splits each string into an array of words, so it produces a `List<String[]>`. The `flatMap` operation also splits each string into words, but it flattens the result into a `List<String>` where each word is an individual element.

So, the key difference is that `flatMap` can handle situations where you want to transform each element in your stream into multiple elements (or none at all), and you want to end up with a flat stream of

*…(truncated — see the source note for the full answer)*

---

## 217. What are the types of operations you can perform on a stream?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

There are two types of operations on streams:

- **Intermediate Operations**: These return a stream and can be chained, like filter(), map(), sorted().
- **Terminal Operations**: These produce a result or a side-effect, ending the stream processing, like collect(), forEach(), reduce().

---

## 218. Can you explain the difference between map and flatMap in Stream API?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

map transforms each element into another object, maintaining the one-to-one relationship. flatMap is used when one element can result in multiple elements or when dealing with collections within streams, effectively flattening the structure into one stream.

- map: Stream.of(“a”, “bb”, “ccc”).map(s -> s.length()) results in [1, 2, 3].
- flatMap: Stream.of(“a”, “bb”, “ccc”).flatMap(s -> s.chars().boxed()) results in a stream of individual character codes.

---

## 219. What does the collect method do in Stream API?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

collect is a terminal operation that aggregates the elements of a stream into a result container, like a List, Set, or Map, using collectors. For example:

`List<String> result = stream.collect(Collectors.toList());`

---

## 220. What is the purpose of Optional in Java 8, and how is it used with Streams?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Optional is used to represent a value that might not be present, reducing the need for null checks. With Streams, it’s often returned by methods like findFirst(), reduce(), or min() to indicate that a result might not exist:

- `Optional<Integer> max = Stream.of(1, 2, 3).max(Integer::compareTo);`

---

## 221. What is a functional interface in Java 8?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

A functional interface is an interface that has exactly one abstract method. This allows them to be implemented by lambda expressions or method references.

---

## 222. Can you name and explain the use of some core functional interfaces in Java 8?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Predicate<T>: Used for filtering operations, returns a boolean.
- Consumer<T>: Accepts one argument and performs an action without returning anything, used in forEach.
- Function<T, R>: Transforms an input type T to an output type R, used in map.
- Supplier<T>: Provides a result of type T without needing an input, used for lazy evaluation.
- UnaryOperator<T> and BinaryOperator<T>: Specializations of Function for operations where input and output types are the same.

---

## 223. How would you use a Predicate to filter a stream?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- `List<String> nonEmptyStrings = Arrays.asList("", "a", "b", "").stream() .filter(Predicate.not(String::isEmpty)) .collect(Collectors.toList());`

---

## 224. What’s the difference between Function and BiFunction?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Function takes one argument and produces a result, while BiFunction takes two arguments to produce a result. Example:

- Function<Integer, String> might convert an Integer to its String representation.
- BiFunction<Integer, Integer, String> could concatenate two integers into a string.

---

## 225. How can you use a Supplier in a Stream operation?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- `Stream.generate(() -> new Random().nextInt(100)).limit(10).forEach(System.out::println);`

This generates a stream of 10 random integers.

---

## 226. Question 1: What is the purpose of the @Qualifier annotation in Spring, and how is it used with @Autowired?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The @Qualifier annotation is used in Spring to resolve ambiguity when there are multiple beans of the same type in the application context. When you use @Autowired for dependency injection and there are multiple beans of the same type, Spring cannot determine which bean to inject. This is where @Qualifier comes in:

- **Usage**: @Qualifier is used alongside @Autowired to specify which bean should be injected when there are multiple candidates. You annotate the injection point with @Qualifier and provide the name or a qualifier of the bean you want to inject.

```
// In configuration or component class
@Bean("specialDataSource")
public DataSource dataSource() {
    return new DataSource();
}

// In the class where you want to inject
@Autowired
@Qualifier("specialDataSource")
private DataSource dataSource;
```

By specifying “specialDataSource” with @Qualifier, you tell Spring to inject the bean named “specialDataSource” rather than any other DataSource bean that might exist.

---

## 227. Explain how the @Transactional annotation works in Spring. What are the key attributes one should be aware of?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The @Transactional annotation in Spring enables declarative transaction management, which means you can handle transactions without explicitly coding them into your business logic. It is applied to classes or methods to define the scope of a transaction:

- **How it Works**: When you annotate a method or class with @Transactional, Spring wraps the method call in a transaction. If an exception is thrown within the method, the transaction will roll back; otherwise, it will commit at the end of the method execution.

**Key Attributes:**

- propagation: Defines how the transaction should behave when one transaction context calls another. Common values include REQUIRED (default), REQUIRES_NEW (new transaction), NESTED (nested transaction within existing one).
- isolation: Specifies the transaction isolation level to prevent problems like dirty reads, non-repeatable reads, and phantom reads. Options include READ_COMMITTED, READ_UNCOMMITTED, REPEATABLE_READ, SERIALIZABLE.
- rollbackFor: Specifies the exception types that should trigger a transaction rollback. By default, only runtime exceptions cause a rollback; checked exceptions do not.
- readOnly: If set to true, it hints that the transaction is read-only, which can optimize performance for some transactional resources.

```
@Transactional(propagation = Propagation.REQUIRED, isolation = Isolation.READ_COMMITTED,
                rollbackFor = Exception.class, readOnly = false)
public void saveData(MyData data) {
    // Business logic here
}
```

In this example, we’re ensuring a transaction with specific rules about how it should propagate, its isolation level, and that it will rollback for any exception, not just runtime ones.

---

## 228. What happens if you have multiple @Transactional annotations in a method call chain?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

When multiple @Transactional annotations are present in a method call chain:

- **Propagation**: The behavior depends on the propagation attribute of each @Transactional annotation. If a method annotated with @Transactional(propagation = Propagation.REQUIRES_NEW) is called from within another transactional method, a new physical transaction will be created for that method, independent of the outer transaction.
- **Nesting**: If methods are annotated with @Transactional but without REQUIRES_NEW, they typically join the existing transaction unless specified otherwise. However, with NESTED, Spring uses savepoints within the same physical transaction to allow partial rollbacks.
- **Outcome**: If an exception occurs, the transaction behavior (commit or rollback) depends on the outermost transaction’s configuration unless inner transactions are configured with REQUIRES_NEW or NESTED with savepoints.

This setup can lead to complex transactional boundaries, and understanding how transactions propagate and interact is crucial for managing data consistency in applications.

> Frontend Questions (React):
>

---

## 229. Question 3 : How Does Service Discovery Work in Microservices with Spring Cloud?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Question:** Describe how service discovery works in a microservices setup using Spring Cloud, and what benefits does it provide?

**Service Discovery** in Spring Cloud involves:

- **Registration**: When a service instance starts, it registers itself with a service registry (like Eureka or Consul). This includes details like its network location, health status, etc.
- **Lookup**: Clients (or other services) can then query this registry to find available instances of services they need to communicate with.
- **Dynamic Updates**: The registry continuously updates as services are added or removed, ensuring that clients can always find active services.

**Benefits:**

- **Decoupling**: Services don’t need to know each other’s locations; they interact via logical service names, reducing coupling.
- **Scalability**: Facilitates horizontal scaling by allowing new instances to be added or removed without configuration changes in clients.
- **Resilience**: If a service instance goes down, clients can automatically discover a healthy instance, improving fault tolerance.
- **Load Balancing**: Often integrated with client-side load balancing, allowing requests to be spread across multiple instances of a service.

Spring Cloud simplifies this with:

- **Eureka or Consul Integration**: Out-of-the-box support for service registries.
- **DiscoveryClient**: An abstraction that services use to interact with the registry, abstracting the underlying discovery mechanism.
- **Ribbon (for older versions) or LoadBalancerClient**: For client-side load balancing, ensuring requests are distributed among instances.

---

## 230. What are the Spring bean scopes and their use cases?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Spring Framework supports several bean scopes, which define the lifecycle and visibility of a bean within the application contexts. Here are the main scopes:

1. **Singleton**: This is the default scope. A single instance of the bean is created and shared across the entire application context. It is stateless in nature. Use case: Service classes, DAOs, Repositories, etc.
2. **Prototype**: A new instance of the bean is created each time it is requested from the container. It is stateful in nature. Use case: Beans that are stateful or not thread-safe.
3. **Request**: A new instance of the bean is created for each HTTP request. This scope is specific to web applications. Use case: Beans that contain user-specific state and are not thread-safe.
4. **Session**: A new instance of the bean is created for each HTTP session. This scope is also specific to web applications. Use case: Beans that need to maintain user session data.
5. **Application**: A single instance of the bean is shared across all servlet contexts in the application. Use case: Beans that need to be shared at the application level, like global configuration data.
6. **WebSocket**: A new instance of the bean is created for each WebSocket connection. This is specific to applications using WebSocket. Use case: Beans that are specific to a WebSocket user session.

Each scope serves different use cases depending on the bean’s required lifecycle and visibility across the application. Singleton and Prototype are the most commonly used scopes, while the others are more specific to web applications.

---

## 231. In how many ways we can create a thread?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In Java, there are two primary ways to create a thread:

1. **Extending the `Thread` class**:
- Create a new class that extends the `Thread` class.
- Override the `run()` method to define the code that should execute in the new thread.
- Create an instance of the class and call the `start()` method to run the new thread.

**2. Implementing the `Runnable` interface**:

- Create a new class that implements the `Runnable` interface.
- Implement the `run()` method to define the code that should execute in the new thread.
- Create an instance of the class and pass it to a `Thread` object, then call the `start()` method on the `Thread` object to run the new thread.
- Here’s a brief example of each method:

**Extending the `Thread` class**:

```
class MyThread extends Thread {
    public void run() {
        // Code to execute in new thread
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start(); // Starts the new thread
    }
}
```

**Implementing the `Runnable` interface**:

```
class MyRunnable implements Runnable {
    public void run() {
        // Code to execute in new thread
    }
}

public class Main {
    public static void main(String[] args) {
        MyRunnable myRunnable = new MyRunnable();
        Thread t = new Thread(myRunnable);
        t.start(); // Starts the new thread
    }
}
```

Both methods are valid, but implementing the `Runnable` interface is more flexible, allowing the class to extend another class if needed.

---

## 232. What is the output of below code ?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

```
thread.run();
thread.run();
thread.start();
```

---

## 233. Create a HashSet of type String and add duplicate strings? what be the output of the program given below?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

```
hs.add("Abcd");
hs.add("efg");
hs.add("abcd");
String s = new String("Abcd");
hs.add(s);
hs.add("Abcdefg");
```

```
System.out.println(hs);
```

---

## 234. What is the benefit of using Micro-service architecture?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Microservice architecture offers several benefits, particularly for complex, large-scale, and evolving applications. Here are some of the key advantages:

1. **Modularity**: It breaks down complex applications into smaller, manageable pieces that are easier to develop, maintain, and understand.
2. **Scalability**: Individual components can be scaled independently, allowing for more efficient use of resources and improving the application’s overall performance.
3. **Flexibility in Technology**: Different microservices can be written in different programming languages, use different data storage technologies, and adopt new technologies without affecting the entire system.
4. **Faster Deployment**: Smaller, independent services can be deployed faster, which accelerates the release cycle and enables continuous delivery and deployment.
5. **Resilience**: Failure in one service does not necessarily bring down the whole system. The modular nature of microservices allows for better fault isolation and recovery.
6. **Improved Fault Isolation**: Since each microservice is independent, issues can be isolated quickly to the specific service, making troubleshooting and recovery faster.
7. **Easier to Scale Development Teams**: Microservices allow for distributed development teams to work on separate services simultaneously without much coordination overhead.
8. **Optimized for the Cloud**: Microservices are well-suited for cloud environments, which offer elasticity, automation in deployment, and scaling.
9. **Enhanced Business Agility**: By enabling quicker updates and improving the speed of introducing new features, microservices architecture supports business agility, allowing companies to adapt to market changes more rapidly.

---

## 235. In micro-services communication, which protocol is lightweight and commonly used?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

HTTP protocol based microservices are commonly used, let me know if you find any useful one.

---

## 236. Which micro-service pattern is used for to prevent failures from cascading to others service?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The microservice pattern used to prevent failures from cascading to other services is the **Circuit Breaker** pattern.

The Circuit Breaker pattern aims to detect failures and encapsulate the logic of preventing a failure from constantly recurring, thereby protecting the system from further damage.

When a microservice component becomes unhealthy, the circuit breaker trips, and further calls to the component are blocked or redirected, usually returning a fallback response. After a certain period, the circuit breaker allows a limited number of test requests to pass through.

If these requests succeed, the circuit breaker resumes normal operation; otherwise, it continues to block requests. This pattern helps maintain system stability and resilience in distributed systems.

---

## 237. In how many ways we can make a REST API call in Micro services?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In microservices architecture, REST API calls can be made in several ways, depending on the technology stack and requirements. Here are some common methods:

**HTTP Client Libraries**:

- **Java**: Use `HttpClient` (Java 11 and above), `RestTemplate` or `WebClient` (Spring Framework).
- **Python**: Use `requests` or `http.client`.
- **JavaScript (Node.js)**: Use `axios`, `fetch`, or the `http` and `https` modules.

**Feign Client** (Spring Cloud): A declarative REST client for microservices communication in Spring applications. It simplifies writing HTTP clients and integrates with Ribbon and Eureka for load balancing.

**Retrofit** (Java): A type-safe HTTP client for Android and Java applications. It allows for synchronous and asynchronous HTTP requests directly to REST endpoints.

**gRPC**: A high-performance, open-source universal RPC framework that can run in any environment. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more.

**GraphQL**: An alternative to REST, GraphQL is a query language for APIs and a runtime for executing those queries by using a type system you define for your data. It allows clients to request exactly the data they need, making it efficient for complex systems and microservices.

**Message Brokers** (e.g., RabbitMQ, Apache Kafka): Though not RESTful, message brokers can be used for asynchronous communication between microservices, supporting event-driven architectures.

Each method has its use cases, advantages, and disadvantages, depending on the requirements for communication, data format, performance, and the complexity of the services involved.

---

## 238. What is the @Restcontroller annotation in Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The `@RestController` annotation in Spring Boot is a convenience annotation that combines `@Controller` and `@ResponseBody`. It is used at the class level and indicates that the class is a controller where every method returns a domain object instead of a view. It simplifies the creation of RESTful web services.

- `@Controller`: Marks the class as a web controller, capable of handling HTTP requests.
- `@ResponseBody`: Indicates that the return value of a method should be used as the response body of the request.

When you annotate a class with `@RestController`, Spring treats it as a controller, and the return value of each method in the class is automatically serialized into JSON or XML and written into the HttpResponse object. This makes it ideal for building RESTful web services with Spring Boot.

```
@RestController
public class ExampleController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }
}
```

In this example, a GET request to `/hello` will return a plain text response with the content "Hello, World!". The `@RestController` annotation ensures that this string is directly written to the response body.

---

## 239. Which of annotations is used to specify a bean as a candidate for dependency injection in Spring Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The annotation used to specify a bean as a candidate for dependency injection in Spring Boot is `@Component`. This annotation marks a Java class as a bean, making it eligible for auto-detection and auto-configuration when using annotation-based configuration and classpath scanning.

Additionally, there are several specialized forms of `@Component` for specific purposes:

- `@Service`: Indicates that an annotated class is a "Service" (e.g., a business service facade).
- `@Repository`: Indicates that an annotated class is a "Repository" (e.g., a Data Access Object).
- `@Controller`: Indicates that an annotated class is a "Controller" (e.g., a web controller).

All these annotations make the annotated class eligible for auto-detection and dependency injection.

---

## 240. Why to use Spring Boot actuator?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Spring Boot Actuator is used for monitoring and managing your application when it’s pushed to production. It provides a series of built-in endpoints allowing you to monitor and interact with your application. Key reasons to use Spring Boot Actuator include:

1. **Health Check**: It provides detailed health information about your application, which can be used to check the status of your application in production.
2. **Metrics Collection**: Actuator gathers application metrics, such as HTTP requests and response statistics, database metrics, cache statistics, and more, which can be crucial for diagnosing issues and understanding application behavior.
3. **Application Info**: It can expose application information, including Git version information, build information, and custom application info.
4. **Dynamic Logging Levels**: Actuator allows changing log levels of your application at runtime without restarting the application.
5. **Thread Dump**: It can generate a thread dump, which can be very useful for diagnosing deadlock situations in your application.
6. **Environment Information**: It provides details about the environment properties, configuration properties, system properties, and environment variables.
7. **Audit Events**: If your application is configured to record audit events, Actuator can expose information about security-related events like user login/logout, access denied, etc.
8. **Custom Endpoints**: Beyond the built-in endpoints, Actuator allows you to define custom endpoints to expose specific functionality or data relevant to your application.

Spring Boot Actuator is a powerful tool for application insights and management, making it easier to maintain and troubleshoot applications in a production environment.

---

## 241. Which annotations is used to declare a Spring Boot application’s main method?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The annotation used to declare a Spring Boot application’s main method is `@SpringBootApplication`. This annotation is typically placed on the main class and serves several purposes:

- It enables auto-configuration, allowing Spring Boot to automatically configure your application based on the dependencies present on the classpath.
- It enables component scanning, allowing Spring to automatically discover and register beans within the application context.
- It enables configuration properties, allowing for externalized configuration.

Here’s an example of how it’s used:

```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

---

## 242. Which design pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The design pattern used to define a family of algorithms, encapsulate each one, and make them interchangeable is the **Strategy Pattern**. This pattern allows the algorithm to vary independently from clients that use it by defining a family of algorithms, encapsulating each one into its own class, and making them interchangeable through the use of a common interface.

---

## 243. Which design pattern is used to add new functionality to an object dynamically?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The design pattern used to add new functionality to an object dynamically is the **Decorator Pattern**. This pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is often used for extending (decorating) the functionality of a class in a flexible and reusable way.

---

## 244. How cloud side load balancing is done in spring boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Cloud-side load balancing in Spring Boot, often referred to as server-side load balancing, is typically managed by the cloud infrastructure or a dedicated load balancer appliance rather than by the application itself. This approach leverages the capabilities of cloud providers (like AWS, Azure, Google Cloud) or dedicated load balancers (like NGINX, HAProxy) to distribute incoming application traffic across multiple instances of the application, thereby improving the responsiveness and availability of applications.

---

## 245. Which keyword is used to handle exceptions in java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The keyword used to handle exceptions in Java is `try-catch`. Additionally, `finally` can be used alongside `try-catch` for code that must execute regardless of whether an exception is thrown or not.

---

## 246. Can we throw exception from static block?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Yes, you can throw an exception from a static block in Java. However, since a static block is executed when the class is loaded, you can only throw a checked exception if you declare it with the `throws` keyword on the class declaration, which is not allowed in Java. Therefore, you can only throw unchecked exceptions (runtime exceptions) from a static block without needing to declare them. Here's an example:

```
public class MyClass {
    static {
        // Throwing an unchecked (runtime) exception
        throw new RuntimeException("Exception from static block");
    }
}
```

Attempting to throw a checked exception directly from a static block without handling it inside the block will result in a compilation error.

---

## 247. Can we have 2 finally block for 1 try catch?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

No, in Java, you cannot have two `finally` blocks for one `try-catch` block. Each `try` block can be followed by zero or more `catch` blocks and only one `finally` block. The `finally` block is optional but, if present, must come after the `try` and any `catch` blocks.

---

## 248. Difference between read time out and connection timed out?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In the context of network operations, including HTTP requests, the terms “read timeout” and “connection timeout” refer to two different timeout behaviors:

- **Connection Timeout**: This is the time limit for establishing a connection between two systems. It specifies the maximum amount of time a client will wait for a connection to be established with a server. If the connection cannot be established within this time frame (due to network issues, the server being down, etc.), the attempt is aborted, and a connection timeout error is thrown.
- **Read Timeout**: Once a connection has been established, the read timeout specifies the maximum amount of time the client will wait for a response from the server after sending a request. This includes waiting for data to start being received, not the total time to download the response. If the server takes longer than this time to respond, a read timeout error occurs, indicating that the server is taking too long to send the data.

Both timeouts are crucial for robust network programming, allowing applications to handle network delays and unavailability gracefully.

---

## 249. Which HTTP method is typically used for safe and idempotent retrieval of information without modifying resources?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The HTTP method typically used for safe and idempotent retrieval of information without modifying resources is `GET`.

---

## 250. Tell me about OOPS concept in java/What are the four basic OOPs principle?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The four principles of Object-Oriented Programming (OOP) are:

**Encapsulation**: This refers to the practice of hiding the internal workings of an object and exposing only the necessary functionality. The data and behaviour of an object are encapsulated within the object, and can only be accessed through well-defined interfaces.

**Inheritance**: Inheritance allows objects to inherit properties and behaviours from other objects. Inheritance allows for the creation of hierarchical relationships between classes, with parent classes passing down their characteristics to their child classes.

**Polymorphism**: Polymorphism refers to the ability of objects to take on many forms, and is achieved through the use of inheritance, overloading and overriding methods, and interfaces. Polymorphism allows for greater flexibility and reuse of code.

**Abstraction**: Abstraction refers to the process of identifying common patterns and extracting essential features of objects, creating classes from these patterns. Abstraction allows for the creation of higher-level concepts that can be used in multiple contexts, and can simplify complex systems.

---

## 251. How do you achieve encapsulation?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Encapsulation is achieved in Java through the use of access modifiers and getter and setter methods.

**Access modifiers control the visibility of variables and methods in a class. There are three access modifiers in Java: public, private, and protected.**

**Public**: Public variables and methods can be accessed from anywhere in the program.

**Private**: Private variables and methods can only be accessed within the same class.

**Protected**: Protected variables and methods can be accessed within the same class, and by subclasses and classes in the same package.

By default, if you don’t specify an access modifier, the variable or method is considered to have “package” or “default” access, which means it can be accessed within the same package.

Here’s an example of how to use access modifiers to achieve encapsulation:

```
public class Person {
private String name;
private int age;
public String getName() {
return name;
}
public void setName(String name) {
this.name = name;
}
public int getAge() {
return age;
}
public void setAge(int age) {
if (age < 0) {
throw new IllegalArgumentException("Age cannot be negative");
}
this.age = age;
}
}
```

In this example, the Person class has two private variables, name and age. These variables are not directly accessible from outside the class, which means that other classes cannot modify or access them directly.

To allow other classes to access these variables, we provide public getter and setter methods for name and age. The getter methods allow other classes to retrieve the values of these variables, while the setter methods allow other classes to modify their values.

Note that we can also add validation logic to the setter methods to ensure that the values being set are valid. In this example, the setAge method throws an exception if the age is negative.

By using access modifiers and getter and setter methods, we can achieve encapsulation in Java. This allows us to protect the data and behavior of our objects and prevent other objects from accessing or modifying them directly, which makes our code more robust and maintainable.

---

## 252. What is abstraction now how it is different from encapsulation?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Abstraction:

· Focus: What the object does, hiding implementation details.

· Goal: Simplifying complex systems by exposing only essential features.

· Mechanisms: Abstract classes, interfaces, functions.

Encapsulation:

· Focus: How the object’s data and behavior are bundled together.

· Goal: Protecting data integrity and controlling access.

· Mechanisms: Access modifiers (public, private, protected), getters and setters.

Key Differences:

· Scope: Abstraction operates at a higher level, focusing on the overall design and interface. Encapsulation works at the object level, managing internal data and implementation.

· Purpose: Abstraction aims to simplify complexity and promote reusability. Encapsulation aims to protect data and manage dependencies.

· Implementation: Abstraction is often achieved through abstract classes or interfaces. Encapsulation is typically implemented using access modifiers and methods to control access to data.

---

## 253. Difference between Abstraction and polymorphism?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Scenario- If you ask someone what is **Abstraction**, he will tell that **it’s an OOP concept which focuses on relevant information by hiding unnecessary detail**, and **when you ask about Encapsulation, many will tell that it’s another OOP concept which hides data from outside world**. The definitions are not wrong as both Abstraction and Encapsulation does hide something, **but the key difference is on intent**.

*Key Points:*

**Abstraction** hides details at the **design** level, while **Encapsulation** hides details at the **implementation** level.

Eg. For example, when you first describe an object, you talk in more abstract term e.g. a Vehicle which can move, you don’t tell how Vehicle will move, whether it will move by using tires or it will fly or it will sell. It just moves. This is called Abstraction. We are talking about a most essential thing, which is moving, rather than focusing on details like moving in plane, sky, or water.

There are also the different levels of Abstraction and it’s good practice that classes should interact with other classes with the same level of abstraction or higher level of abstraction. As you increase the level of Abstraction, things start getting simpler and simpler because you leave out details.

On the other hand, Encapsulation is all about implementation. Its sole purpose is to hide internal working of objects from outside world so that you can change it later without impacting outside clients.

For example, we have a HashMap which allows you to store the object using put() method and retrieve the object using the get() method. How HashMap implements this method (see here) is an internal detail of HashMap, the client only cares that put stores the object and get return it back, they are not concerned whether HashMap is using an array, how it is resolving the collision, whether it is using linked list or binary tree to store object landing on same bucket etc.

1) The most important difference between Abstraction and Encapsulation is that Abstraction solves the problem at design level while Encapsulation solves it implementation level.

2) Abstraction is about hiding unwanted details while giving out most essential details, while Encapsulation means hiding the code and data into a single unit e.g. class or method to protect inner working of an object from outside world. In other words, Abstraction means extracting common details or generalizing things.

3) Abstraction lets you focus on what the object does instead of how it does, while Encapsulation means hiding the internal details of how an object works. When you keep internal working details private, you can change it later with a better method. The Head First Object Oriented Analysis and Design has some excellent examples of these OOP concepts, I suggest you read that book at least once to revisit OOP fundamentals.

4) Abstraction focus on outer lookout e.g. moving of vehicle while Encapsulation focuses on internal working or inner lookout e.g. how exactly the vehicle moves.

5) In Java, **Abstraction is supported using interface and abstract class** while **Encapsulation is supported using access modifiers e.g. public, private and protected.**

---

## 254. What is polymorphism?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Polymorphism in Java is a concept by which we can perform a single action in different ways.

Polymorphism defined as “same code” giving “different behaviour”

---

## 255. What is interface in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- It is the blueprint of the class
- Interface in Java can only contains declaration. You can not declare any concrete methods inside interface
- Java interface can extend multiple interface also Java class can implement multiple interfaces, Which means interface can provide more Polymorphism support than abstract class
- but by using interface it can be part of multiple type hierarchies.a class can be Runnable and Displayable at same time
- In order to implement interface in Java, until your class is abstract, you need to provide implementation of all methods, which is very painful

---

## 256. What is abstract class?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- A class which is declared with the abstract keyword is known as an abstract class in Java.
- abstract class may contain both abstract and concrete methods, which makes abstract class an ideal place to provide common or default functionality

By extending abstract class, a class can only participate in one Type hierarchy

---

## 257. Abstract class vs Interface in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

1) First and the major difference between abstract class and an interface is that an abstract class is a class while the interface is an interface, means by extending the abstract class you can not extend another class because Java does not support multiple inheritances but you can implement multiple inheritance in Java.

2) The second difference between interface and abstract class in Java is that you can not create a non-abstract method in an interface, every method in an interface is by default abstract, but you can create a non-abstract method in abstract class. Even a class which doesn’t contain any abstract method can be made abstract by using the abstract keyword.3) interface is better suited for Type declaration and abstract class is more suited for code reuse and evolution perspective.4)abstract class are slightly faster than interface because interface involves a search before calling any overridden method in Java.5) when you add a new method in existing interface it breaks all its implementation and you need to provide an implementation in all clients which is not good. By using an abstract class you can provide a default implementation for a new method in the superclass without breaking existing clients.

---

## 258. When to use interface and abstract class in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

[**Difference between Abstract Class vs Interface in JavaWhen to use abstract class and interface in Java or object oriented design is a critical question. In order to make…**javarevisited.blogspot.com](https://archive.ph/o/D2VYr/https://javarevisited.blogspot.com/2013/05/difference-between-abstract-class-vs-interface-java-when-prefer-over-design-oops.html)

> Access modifiers in java
>

---

## 259. Different types of access modifiers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

There are four types of access modifiers in Java:

**public**: The public access modifier is the most permissive access level, and it allows access to a class, method, or variable from any other class, regardless of whether they are in the same package or not.

**protected**: The protected access modifier allows access to a class, method, or variable from within the same package, as well as from any subclass, even if they are in a different package.

**default** (no modifier): If no access modifier is specified, then the class, method, or variable has package-level access. This means that it can be accessed from within the same package, but not from outside the package.

**private**: The private access modifier is the most restrictive access level, and it allows access to a class, method, or variable only from within the same class. It cannot be accessed from any other class, even if they are in the same package.

Here is an example of how access modifiers can be used:

```
public class MyClass {
public int publicVar;
protected int protectedVar;
int defaultVar;
private int privateVar;
public void publicMethod() {
}
protected void protectedMethod() {
}
void defaultMethod() {
}
private void privateMethod() {
}
}
```

---

## 260. What is the difference between private and protected access modifiers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The main difference between private and protected access modifiers in Java is that private members are only accessible within the same class, while protected members are accessible within the same class and its subclasses, as well as within the same package.

Here are some more differences between private and protected:

Visibility: Private members are only visible within the same class, while protected members are visible within the same class and its subclasses, as well as within the same package.

Access: Private members cannot be accessed outside the class, while protected members can be accessed by subclasses and other classes in the same package.

Inheritance: Private members are not inherited by subclasses, while protected members are inherited by subclasses.

Overriding: Private members cannot be overridden in subclasses, while protected members can be overridden in subclasses.

Here is an example to illustrate the difference between private and protected access modifiers:

```
public class MyClass {
private int privateVar;
protected int protectedVar;
public void myMethod() {
privateVar = 1; // OK, can be accessed within the same class
protectedVar = 2; // OK, can be accessed within the same class
}
}
public class MySubclass extends MyClass {
public void mySubMethod() {
// privateVar = 3; // Error, cannot be accessed in subclass
protectedVar = 4; // OK, can be accessed in subclass
}
}
public class MyOtherClass {
public void myOtherMethod() {
MyClass obj = new MyClass();
// obj.privateVar = 5; // Error, cannot be accessed outside //the class
// obj.protectedVar = 6; // Error, cannot be accessed //outside the package or subclass
}
}
```

In this example, we have a class MyClass with a private variable privateVar and a protected variable protectedVar. The myMethod() method of MyClass can access both variables. We also have a subclass MySubclass of MyClass, which can access the protectedVar variable, but not the privateVar variable. Finally, we have another class MyOtherClass, which cannot access either variable, because they are not visible outside the class or its package.

> String
>

---

## 261. If string is not immutable then what challenge a developer can face?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

If strings were mutable in Python, developers could face several challenges:

- **Unexpected behavior:** Mutating a string after it has been assigned to a variable could lead to unexpected behavior in different parts of the codebase. Imagine a situation where a function receives a string as input, modifies it, and then returns it. If the original string is also modified elsewhere in the code, it would be difficult to track the source of the changes and reason about the overall state of the string.
- **Memory management issues:** Mutable strings could introduce memory management complexities. If multiple variables point to the same mutable string object, changes made through one variable would be reflected in all the others. This could lead to confusion and memory leaks if not handled carefully.
- **Concurrency problems:** In concurrent programming scenarios, where multiple threads or processes access and potentially modify the same string, concurrency issues could arise. It would be difficult to ensure data consistency and avoid race conditions without proper synchronization mechanisms.
- **Debugging difficulties:** Debugging issues related to mutable strings would likely be more challenging. Tracing the origin of string modifications and the potential side effects across different parts of the codebase would require careful analysis.

---

## 262. Difference between String a = “ajay” and string a2= new String(“Ajay”)?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The key difference between the two string assignments lies in how they are stored in memory:

**String a = "ajay":**

- This creates a string literal "ajay". String literals are stored in the String pool, a special memory area in Java.
- The String pool ensures that only one copy of the same string literal exists in memory, even if it's assigned to multiple variables.
- This approach is memory-efficient and improves performance.

**String a2 = new String("Ajay"):**

- This creates a new String object using the `new` keyword and the String constructor.
- A new object is allocated in the heap memory, containing the characters "Ajay".
- This creates a separate copy of the string even if it has the same characters as a string literal in the pool.
- While it allows modifying the string content later, it consumes more memory compared to string literals.

> Serialization
>

---

## 263. What is transient Keyword and why serialization requires,on which parameter we do serialization?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Transient Keyword:**

- The `transient` keyword is a variable modifier used in Java specifically during serialization.
- When applied to a field, it instructs the JVM to exclude that field’s value from being saved when the object is serialized.
- This means the field’s value is not persisted in the serialized form of the object.

**Why Serialization Requires It:**

Serialization is the process of converting an object’s state into a byte stream for storage or transmission. While useful, it’s not always desirable to serialize every single piece of data within an object. Here’s why the `transient` keyword is important:

- **Excluding Sensitive Information:** Certain fields might contain sensitive information like passwords or temporary data that shouldn’t be stored permanently. Using `transient` prevents these values from being serialized, safeguarding sensitive data.
- **Avoiding Redundant Data:** Some fields might be calculable from other serialized fields. For example, a person’s age can be derived from their date of birth. Serializing the age when it can be calculated later is redundant and wastes storage space.
- **Non-Serializable References:** If a field holds a reference to a non-serializable object, serializing it would lead to errors. Marking the field as `transient` avoids such issues.

**Serialization and Parameter:**

Serialization itself doesn’t directly involve parameters. It’s an object-level process where the entire state of a serializable object is converted into a byte stream. However, the `transient` keyword is applied to individual fields within the object, acting as a parameter on the field level.

By marking specific fields as `transient`, you control which parts of the object's state are serialized, ensuring sensitive data remains secure, redundant data is avoided, and compatibility issues with non-serializable references are prevented.

---

## 264. If i implement class A implements serializable will i get any error for it?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

No, you will not get an error solely for implementing the `Serializable` interface in your class A. However, there are a few things to keep in mind:

**Successful Serialization:**

- Implementing `Serializable` only signifies that your class can be serialized. It doesn't guarantee successful serialization.
- For successful serialization, the following conditions need to be met:
- All fields of the class A must be either serializable themselves or have a custom serialization mechanism defined.
- The class should have a no-argument constructor to allow deserialization.

**Potential Errors:**

- If any field in class A is not serializable (e.g., custom objects without their own serialization implementation), you’ll encounter a `NotSerializableException` during serialization.
- If the class A doesn’t have a no-argument constructor, you might face issues during deserialization, potentially leading to an `InvalidClassException`.

---

## 265. What is the use of serialversionUID in and if my class doesn’t implement it?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The `serialVersionUID` is a long constant used in Java serialization to ensure compatibility between the serialized data and the class used for deserialization. Here's a breakdown of its usage and what happens if your class doesn't implement it:

**Purpose of `serialVersionUID`:**

- It acts as a unique identifier for the serialized form of a class.
- During deserialization, the JVM compares the `serialVersionUID` stored in the serialized data with the `serialVersionUID` of the class being used for deserialization.
- If they match, it indicates compatibility between the serialized data and the class, allowing successful deserialization.

**What happens if your class doesn’t implement it:**

- If you don’t explicitly define `serialVersionUID` in your `Serializable` class, the JVM calculates a default value based on various aspects of the class, like field names, types, and access modifiers.
- This default calculation can be sensitive to changes in the class structure, even seemingly minor ones.
- If the class structure changes in a later version, the default `serialVersionUID` might also change, leading to incompatibility during deserialization and potentially throwing an `InvalidClassException`.

**Consequences:**

- Deserialization failure can cause unexpected errors and program crashes.
- Maintaining compatibility across different versions of a class becomes difficult.

**Best Practice:**

- It’s strongly recommended to explicitly define `serialVersionUID` as a private static final long variable in your `Serializable` class.
- This ensures consistent compatibility and avoids potential issues during deserialization, especially in scenarios where serialized data might be shared across different versions of the class.

Here are some additional points to consider:

- You can use the `serialver` tool included in the JDK to generate a `serialVersionUID` for your class.
- If you make changes to the class structure that might affect compatibility, you should update the `serialVersionUID` accordingly.
- By explicitly defining `serialVersionUID`, you gain control over compatibility and prevent unexpected deserialization errors.

> Collection:HashSet
>

---

## 266. How hashset works internally and what is the main functionality of hashset,why we use hashset,how hashsets add method works?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**B**efore going into internal implementation of HashSet in Java it is important to know two points about HashSet.

- HashSet in Java only stores unique values i.e. no duplicates are allowed.
- HashSet works on the concept of hashing just like HashMap in Java but its working differs from the HashMap in the following way-In HashMap a (Key, Value) pair is added and the hash function is calculated using key.
- Where as in the HashSet hash function is calculated using the value itself. Note that in HashSet we have add(E e) method which takes just the element to be added as parameter.
- Also you may have guessed by now, since hash function is calculated using value that is why only unique values are stored in the HashSet. If you try to store the same element again, the calculated hash function would be same, thus the element will be overwritten.
- Now coming back to internal implementation of HashSet in Java the most important point is HashSet class implementation uses HashMap to store it’s objects.

Within the HashSet there are many constructors one without any parameter and several more with initial capacity or load factor but each one of these constructor creates a HashMap. Since HashSet internally uses HashMap so knowing how HashMap works internally in Java will help you to understand how HashSet works internally in Java.

*HashSet Constructor snippets*

In the HashSet class in Java you can see that constructors of the class do create a HashMap.

```
/**
* Constructs a new, empty set; the backing <tt>HashMap</tt> instance has
* default initial capacity (16) and load factor (0.75).
*/
public HashSet() {
 map = new HashMap<>();
}
public HashSet(int initialCapacity, float loadFactor) {
 map = new HashMap<>(initialCapacity, loadFactor);
}
And the map, which is used for storing values, is defined as
```

private transient HashMap<E,Object> map;In the constructor, if you have noticed, there are parameters named initial capacity and load factor. For HashSet, default initial capacity is 16, that is an array (or bucket) of length 16 would be created and default load factor is 0.75. Where load factor is a measure of how full the hash table is allowed to get before its capacity is automatically increased.

---

## 267. How elements are added in HashSet?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

I stated in the point 2 above that HashSet calculates the hash function using value itself and there is no (Key, Value) pair in HashSet and then came the statement that HashSet internally uses HashMap to store objects. These two statements may sound contradictory as HashMap stores (key, value) pair so let’s see how these these two contradictory statements hold true.

Actually from add method of HashSet class put() method of HashMap is called where the value, which has to be added in the Set, becomes Key and a constant object “PRESENT” is used as value.

That’s how PRESENT is defined in HashSet implementation -

```
// Dummy value to associate with an Object in the backing Map
private static final Object PRESENT = new Object();
And that's how add method is implemented in HashSet class -
public boolean add(E e) {
 return map.put(e, PRESENT)==null;
}
So you can see with in the internal implementation of the HashSet it’s a (key, value) pair which is actually getting added. It’s just that the actual value (which is added to the HashSet) becomes the key and a dummy value “PRESENT” is added as value when storing it in the backing HashMap.
```

One thing to note here is, in HashMap value may be duplicate but Key should be unique. That’s how HashSet makes sure that only unique values are stored in it, since the value which is to be stored in the HashSet becomes the key while storing it in HashMap.

---

## 268. How element is removed from a HashSet in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

When we need to remove an element from the HashSet, internally again remove method of HashSet calls remove(Object key) method of the HashMap.

That is how it is implemented in HashSet class.

```
public boolean remove(Object o) {
 return map.remove(o)==PRESENT;
}
Here note that remove(Object key) method of the HashMap returns the Value associated with the key. Whereas the remove(Object o) method of the HashSet returns Boolean value. Also we know that for every value added in HashSet, internally when it is added to the associated HashMap, value becomes Key and the value is always an object called PRESENT. Therefore the value that is returned from the remove(Object key) method of the HashMap is always PRESENT thus the condition map.remove(o)==PRESENT.
```

---

## 269. How elements are retrieved from HashSet in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In HashSet there is no get method as provided in Map or List. In HashSet iterator is there which will iterate through the values of the Set. Internally it will call the keyset of the HashMap, as values are stored as keys in the HashMap so what we’ll get is the values stored in the HashSet.

That’s how iterator is internally implemented in the HashSet in Java.

```
/**
* Returns an iterator over the elements in this set. The elements
* are returned in no particular order.
*
*@return an Iterator over the elements in this set
*@see ConcurrentModificationException
*/
public Iterator<E> iterator() {
 return map.keySet().iterator();
}
Points to note:
```

Unlike HashMap where hash function is calculated using key HashSet uses the value itself to calculate the hash function.Since hash function is calculated using value that is why only unique values are stored in the HashSet.HashSet internally uses HashMap to store its elements.When element is added to HashSet using add(E e) method internally HashSet calls put() method of the HashMap where the value passed in the add method becomes key in the put() method. A dummy value “PRESENT” is passed as value in the put() method.anation-

> Collection: HashMap
>

---

## 270. How hashmap works internally ?what are the changes has been done in Java 8 in hashmap?How HashMap Internally Works in Java?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

There are four things you should know about HashMap before going into internal working of HashMap in Java-HashMap works on the principal of hashing.

- ***Map.Entry interface*** — This interface gives a map entry (key-value pair). HashMap in Java stores both key and value object, in bucket, as an object of Node class which implements this nested interface Map.Entry.
- ***hashCode()*** — HashMap provides put(key, value) for storing and get(key) method for retrieving values from HashMap. When put() method is used to store (Key, Value) pair, HashMap implementation calls hashcode on Key object to calculate a hash that is used to find a bucket where Entry object will be stored.When get() method is used to retrieve value, again key object (passed with the get() method) is used to calculate a hash which is then used to find a bucket where that particular key is stored.
- ***equals() — equals()*** method is used to compare objects for equality. In case of HashMap key object is used for comparison, also using equals() method Map knows how to handle hashing collision (hashing collision means more than one key having the same hash value, thus assigned to the same bucket). In that case objects are stored in a linked list, refer figure for more clarity.
- Where hashCode() method helps in finding the bucket where that key is stored, equals() method helps in finding the right key as there may be more than one key-value pair stored in a single bucket.Bucket term used here is actually an index of array, that array is called table in HashMap implementation. Thus table[0] is referred as bucket0, table[1] as bucket1 and so on.

---

## 271. How elements are stored internally in Java HashMap?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

HashMap class in Java uses an array called table of type Node to store the elements which is defined in the HahsMap class as-transient Node[] table;Node is defined as a static class with in a Hashmap.static class Node implements

```
Map.Entry {
 final int hash;
 final K key;
 V value;
 Node next;
 ..
 ..
}
```

As you can see for each element four things are stored in the following fields--hash- For storing Hashcode calculated using the key.-key- For holding key of the element.-value- For storing value of the element.-next- To store reference to the next node when a bucket has more than one element and a linkedlist is formed with in a bucket to store elements.Following code shows how Node(key-value pair) objects are stored internally in table array of the HashMap class.How important it is to have a proper hash code and equals method can be seen through the help of the following program:

```
public class HashMapTest {
 public static void main(String[] args) {
 Map <Key, String> cityMap = new HashMap<Key, String>();
 cityMap.put(new Key(1, "NY"),"New York City" );
 cityMap.put(new Key(2, "ND"), "New Delhi");
 cityMap.put(new Key(3, "NW"), "Newark");
 cityMap.put(new Key(4, "NP"), "Newport");
 System.out.println("size before iteration " + cityMap.size());
 Iterator <Key> itr = cityMap.keySet().iterator();
 while (itr.hasNext()){
 System.out.println(cityMap.get(itr.next()));
 }
 System.out.println("size after iteration " + cityMap.size());
 }

}
// This class' object is used as key
// in the HashMap
class Key{
 int index;
 String Name;
 Key(int index, String Name){
 this.index = index;
 this.Name = Name;
 }

 @Override
 // A very bad implementation of hashcode
 // done here for illustrative purpose only
 public int hashCode(){
 return 5;
 }

 @Override
 // A very bad implementation of equals
 // done here for illustrative purpose only
 public boolean equals(Object obj){
 return true;
 }

}
```

*Output*:size before iteration 1Newportsize after iteration 1Refer Overriding hashCode() and equals() method in Java to know more about hashCode() and equals() method

***Understanding the Code***Lets get through the code to see what is happening, this will also help in understanding how put() method of HashMap works internally.Notice that I am inserting 4 values in the HashMap, still in the output it says size is 1 and iterating the map gives me the last inserted entry. Why is that?Answer lies in, how hashCode() and equals() method are implemented for the key Class. Have a look at the hashCode() method of the class Key which always returns “5” and the equals() method which is always returning “true”.When a value is put into HashMap it calculates a hash using key object and for that it uses the hashCode() method of the key object class (or its parent class).

Based on the calculated hash value HashMap implementation decides which bucket should store the particular Entry object.In my code the hashCode() method of the key class always returns “5”. This effectively means, calculated hash value, is same for all the entries inserted in the HashMap.

Thus all the entries are stored in the same bucket.Second thing, a HashMap implementation does use equals() method to see if the key is equal to any of the already inserted keys (Recall that there may be more than one entry in the same bucket).

Note that, with in a bucket key-value pair entries (Entry objects) are stored in a linked-list (Refer figure for more clarity). In case hash is same, but equals() returns false (which essentially means more than one key having the same hash or hash collision) Entry objects are stored, with in the same bucket, in a linked-list.

In my code, I am always returning true for equals() method so the HashMap implementation “thinks” that the keys are equal and overwrites the value. So, in a way using hashCode() and equals() I have “tricked” HashMap implementation to think that all the keys (even though different) are same, thus overwriting the values.

In a nutshell there are three steps in the internal implementation of HashMap put() method-Using hashCode() method, hash value will be calculated. In which bucket particular entry will be stored is ascertained using that hash.

equals() method is used to find if such a key already exists in that bucket, if not found then a new node is created with the map entry and stored within the same bucket. A linked-list is used to store those nodes.If equals() method returns true, it means that the key already exists in the bucket. In that case, the new value will overwrite the old value for the matched key.

---

## 272. How HashMap get() method works internally?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- As we already know how Entry objects are stored in a bucket and what happens in the case of Hash Collision it is easy to understand what happens when key object is passed in the get() method of the HashMap to retrieve a value.
- Using the key (passed in the get() method) again hash value will be calculated to determine the bucket where that Entry object is stored, in case there are more than one Entry object with in the same bucket (stored as a linked-list) equals() method will be used to find out the correct key. As soon as the matching key is found get() method will return the value object stored in the Entry object.In case of null KeyHashMap in Java also allows null as key, though there can only be one null key in HashMap. While storing the Entry object HashMap implementation checks if the key is null, in case key is null, it always map to bucket 0, as hash is not calculated for null keys.

***HashMap changes in Java 8***

- Though HashMap implementation in Java provides constant time performance O(1) for get() and put() methods but that is in the ideal case when the Hash function distributes the objects evenly among the buckets.
- But the performance may worsen in the case hashCode() used is not proper and there are lots of hash collisions. As we know now that in case of hash collision entry objects are stored as a node in a linked-list and equals() method is used to compare keys. That comparison to find the correct key with in a linked-list is a linear operation so in a worst case scenario the complexity becomes O(n).
- To address this issue in Java 8 hash elements use balanced trees instead of linked lists after a certain threshold is reached. Which means HashMap starts with storing Entry objects in linked list but after the number of items in a hash becomes larger than a certain threshold, the hash will change from using a linked list to a balanced tree, this will improve the worst case performance from O(n) to O(log n).

> Try catch finally related question
>

---

## 273. What is finalize method?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Finalize method:**

- A method inherited from the Object class, called just before an object is garbage collected.
- Used for cleanup activities like releasing resources (files, network connections).

---

## 274. Where to write finalize in your application?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Where to write finalize:**

- Override the finalize() method in your class if you need specific cleanup tasks.

---

## 275. What is the flow of webservices?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Web service flow:**

1. Client sends a request (e.g., HTTP) to the web service.
2. Web service processes the request and generates a response.
3. Response is sent back to the client.

---

## 276. What is the entry point of webservices?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Web service entry point:**

- Depends on the web service technology (e.g., Java: servlet, JAX-WS endpoint).
- Generally defined in configuration files or annotations.

> Topic:Hibernate
> 

**What is Hibernate**

Its an ORM that is able to map java objects to a variety of diffrent relational database ,allows us to configuration and to use and connect to database and to specify which is our java object should be mapped to relational tablesIt does job of creating SQL that is able to save update delete and query data from the databseIt presents us the data to us as java objects that we can use and manipulate and then save back to database

---

## 277. What is the use of Hibernate why should we use it and why we should not use sql?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

- Hibernate is persisting technology that is based on the idea of object relational mapping or ORM.
- ORM is a framework that enable you to map the world of objects found in object oriented language like java to row in relational tables found in relational database like MYSQL.
- Why we need Hibernate because, without an ORM we have to translate this object into a few different SQL statements that will insert/update the data into the tables,but to do that we have to write java code to create sql its not that hard but its tedious and pretty easy to get wrong ,thats when the ORM comes in.
- using orm we can declare certain java class should be mapped to relational table and let the ORM deal with it, map objects to tables

> Spring
>

---

## 278. Write a program to check the minimum number of occurence of a character in a given string?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

```
public class MinimumNumberOccrenceofString {
public static void main(String[] args) {
// TODO Auto-generated method stub
String str = "ajay";
char c ='a';
System.out.println(count(str,c));
}
private static int count(String str, char c) {
int result =0 ;
for(int i=0;i<str.length(); i++) {
//checking charector in string
if(str.charAt(i)==c) {
result++;
}
}
return result;
}
}
```

---

## 279. What is Response Entity in Spring-Boot?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In Spring Boot, a ResponseEntity is a class used to represent the entire HTTP response sent back to a client. It goes beyond just the data itself and encapsulates three key aspects:

- **Status Code:** This indicates the outcome of the request, like success (200 OK), not found (404), or internal server error (500).
- **Headers:** These are optional key-value pairs that provide additional information about the response, such as content type, cache control, or authentication details.
- **Body:** This is the actual data being sent back to the client. It can be anything from JSON or XML to plain text, depending on your API design.

By using ResponseEntity, you gain fine-grained control over how Spring Boot constructs the response. You can set the appropriate status code, add custom headers, and include the response data in the body. This allows you to build more informative and flexible APIs.

```
@RestController
public class ProductController {

    @GetMapping("/products/{id}")
    public ResponseEntity<Product> getProduct(@PathVariable Long id) {

        // Simulate product retrieval logic
        Product product = getProductFromDatabase(id);

        // Check if product exists
        if (product == null) {
            return ResponseEntity.notFound().build(); // 404 Not Found
        }

        // Return product with OK status (200)
        return ResponseEntity.ok(product);
    }

    // Simulate product retrieval from database (replace with your actual logic)
    private Product getProductFromDatabase(Long id) {
        // ... (implementation details)
        return new Product(id, "Sample Product", 10.0);
    }
}
```

---

## 280. How to configure multiple databases in spring-boot application?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

This is very interesting question and gets repeated all the time in an interview.

Spring Boot offers a convenient way to configure multiple databases in your application. Here’s a breakdown of the steps involved:

**1. Define Data Source Properties:**

- Spring Boot uses properties to configure data sources. You can define them in your `application.yml` or `application.properties` file.
- Each data source needs its own set of properties, prefixed with a unique identifier. Common properties include:
- `url`: Database connection URL.
- `username`: Database username.
- `password`: Database password.
- `driverClassName`: JDBC driver class name for the database.

Here’s an example configuration for two databases named `users` and `orders`:

```
spring:
  datasource:
    users:
      url: jdbc:mysql://localhost:3306/users
      username: user
      password: password
      driverClassName: com.mysql.cj.jdbc.Driver
    orders:
      url: jdbc:postgresql://localhost:5432/orders
      username: orders_user
      password: orders_password
      driverClassName: org.postgresql.Driver
```

**2. Create DataSource Beans:**

- Spring Boot provides annotations and utilities to create DataSource beans.
- You can use `@ConfigurationProperties` to map the data source properties defined earlier to a bean.
- Here’s an example configuration class with `DataSourceBuilder` to create beans for each data source:

```
@Configuration
public class DataSourceConfig {

  @Bean
  @ConfigurationProperties(prefix = "spring.datasource.users")
  public DataSource usersDataSource() {
    return DataSourceBuilder.create().build();
  }

  @Bean
  @ConfigurationProperties(prefix = "spring.datasource.orders")
  public DataSource ordersDataSource() {
    return DataSourceBuilder.create().build();
  }
}
```

**Configure Entity Manager and Transaction Manager (Optional):**

- If you’re using Spring Data JPA, you’ll need to configure separate Entity Managers and Transaction Managers for each data source.
- These can be created similarly to DataSource beans, specifying the entities associated with each data source.

**4. Injecting the Correct DataSource:**

- By default, Spring Boot auto-configures a single DataSource. To use specific data sources:
- You can inject `@Qualifier("usersDataSource")` or `@Qualifier("ordersDataSource")` for specific repositories or services.
- JPA repositories can also use `@Entity` annotation with a `entityManagerFactoryRef` attribute to specify the EntityManager.

Remember to adapt the configuration details (database type, connection details) to your specific databases.

---

## 281. What is IOC Containers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

An IoC Container is a software framework component that manages the objects (beans) in your application. It takes over the responsibility of creating, configuring, and assembling these objects and their dependencies.

**How Does it Work?**

- **Object Creation:** Traditionally, you’d manually create objects in your code. With an IoC container, you define the objects (beans) you need in your application using configuration files (XML or annotations) or Java classes. The container then takes care of instantiating these objects.
- **Dependency Injection:** Objects often rely on other objects to function properly (dependencies). Instead of manually creating and passing these dependencies around, you declare them in your object definitions. The IoC container injects (provides) the required dependencies to the objects it creates. This creates a loose coupling between objects, making your code more modular and easier to test.
- **Object Lifecycle Management:** The IoC container also manages the lifecycle of objects, including initialization and destruction. This frees you from writing boilerplate code for these tasks.

---

## 282. What is Dependency Injections?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In software development, dependency injection (DI) is a technique for providing an object with the objects (dependencies) it needs to function. Here’s a breakdown of the key concepts:

**What are Dependencies?**

- Dependencies are other objects that a class or function relies on to perform its work effectively.
- Examples:
- A car depends on an engine, wheels, and other parts to function.
- A database access class depends on a database connection object to interact with the database.

---

## 283. What is Application Context & its's use?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In Spring Boot applications, the ApplicationContext is a central interface that plays a critical role in managing the objects (beans) used throughout your application. It’s essentially a container that provides the following functionalities:

**1. Bean Management:**

- The core responsibility of the ApplicationContext is to manage the objects (beans) that make up your application.
- These beans are typically defined using annotations or XML configuration files.
- The ApplicationContext takes care of creating, configuring, and assembling these beans according to the specified configuration.

**2. Dependency Injection:**

- Beans often rely on other beans to function properly. These are called dependencies.
- The ApplicationContext facilitates dependency injection by automatically providing the required dependencies to the beans it creates. This eliminates the need for manual dependency creation and management, leading to loosely coupled and more maintainable code.

**3. Resource Access:**

- The ApplicationContext provides access to various resources your application might need, such as property files, configuration files, and message bundles.
- This simplifies resource retrieval and ensures consistent access throughout your code.

---

## 284. How to Enable multiple Eureka Servers?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

This article deals with this question

[**How to work with multiple instances of Eureka Naming Server to avoid a single point of failureIf you work with Java and microservices, you probably know how to use Eureka Naming Server to get your services…**medium.com](https://archive.ph/o/jDKAO/https://medium.com/become-developer/how-to-work-with-multiple-instances-of-eureka-naming-server-to-avoid-a-single-point-of-failure-d953544281d0)

---

## 285. What’s the main difference between HashTable and ConcurrentHashmap?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

key difference between Hashtable and ConcurrentHashMap in Java:

**Synchronization:**

- **Hashtable:** Uses a single lock for the entire table. This means only one thread can access the table at a time, even for reads, creating a bottleneck in high-concurrency scenarios.
- **ConcurrentHashMap:** Uses fine-grained locking at the bucket level (segments). This allows concurrent reads and limited concurrent writes, significantly improving performance in multi-threaded environments.

---

## 286. If there is Memory Leak in your application how will you find it?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

***Symptoms of a Memory Leak***

1. Severe performance degradation when the application is continuously running for a long time.
2. OutOfMemoryError heap error in the application.
3. Spontaneous and strange application crashes.
4. The application is occasionally running out of connection objects.

---

## 287. What is the use of Stringtokenizer?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

The string tokenizer class allows an application to break a string into tokens. The tokenization method is much simpler than the one used by the `StreamTokenizer` class. The `StringTokenizer` methods do not distinguish among identifiers, numbers, and quoted strings, nor do they recognize and skip comments.

The set of delimiters (the characters that separate tokens) may be specified either at creation time or on a per-token basis.

An instance of `StringTokenizer` behaves in one of two ways, depending on whether it was created with the `returnDelims` flag having the value `true` or `false`:

- If the flag is `false`, delimiter characters serve to separate tokens. A token is a maximal sequence of consecutive characters that are not delimiters.
- If the flag is `true`, delimiter characters are themselves considered to be tokens. A token is thus either one delimiter character, or a maximal sequence of consecutive characters that are not delimiters.

A StringTokenizer object internally maintains a current position within the string to be tokenized. Some operations advance this current position past the characters processed.

A token is returned by taking a substring of the string that was used to create the StringTokenizer object.

The following is one example of the use of the tokenizer. The code:

```
StringTokenizer st = new StringTokenizer("this is a test");
while (st.hasMoreTokens()) {
 System.out.println(st.nextToken());
}
```

---

## 288. What is Spring Security Context?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

SecurityContext — is obtained from the SecurityContextHolder and contains the Authentication of the currently authenticated user. Authentication — Can be the input to AuthenticationManager to provide the credentials a user has provided to authenticate or the current user from the SecurityContext .

---

## 289. What is the Difference between these two — Object Level Locking and Class Level Locking?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In concurrent programming, synchronization is essential to maintain data consistency when multiple threads access shared resources. Locking mechanisms achieve synchronization by restricting access to these resources, ensuring only one thread operates on them at a time. There are two primary locking approaches in object-oriented programming languages like Java: Object Level Locking and Class Level Locking.

**Object Level Locking**

- Applies to individual objects: Every object in Java has a unique lock associated with it.
- Achieved using the `synchronized` keyword with non-static methods or code blocks.
- Ensures only one thread can execute a synchronized method on a specific object at a time.
- Other threads attempting to access the same synchronized method on the same object will be blocked until the lock is released.
- Suitable for synchronizing access to instance variables and methods of an object.
- Maintains granularity, allowing concurrent access to different objects of the same class.

**Class Level Locking**

- Applies to the entire class: Achieved using the `synchronized` keyword with static methods.
- Only one thread can execute a synchronized static method of a class, regardless of the object instance.
- All other threads attempting to access synchronized static methods will be blocked.
- Useful for synchronizing access to static variables and methods of a class.
- Offers a broader level of control but can lead to more significant performance overhead compared to object level locking.

---

## 290. Between these two who will consume more memory(int or Integer)?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

In most programming languages, `int` will consume less memory than `Integer`. Here's why:

- `int` **is a primitive data type:** It represents the basic integer value itself and directly stores the number in memory. The size is typically fixed, often 4 bytes (32 bits) on most modern systems.
- `Integer` **is a class (or object):** In languages like Java, `Integer` is a class that wraps around an `int` value. It provides additional functionalities beyond storing the number, like methods for conversion or advanced math operations. This extra functionality comes at a memory cost.

---

## 291. What is Weak HashMap?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

WeakHashMap is a special implementation of the Map interface in Java. It differs from a regular HashMap in how it handles keys:

- **Key Storage:** In a WeakHashMap, keys are stored using **WeakReferences**. This means the keys themselves are not considered strong references that prevent garbage collection (GC).
- **Automatic Removal:** When the only reference to a key in the WeakHashMap is the weak reference within the map itself, and there are no other strong references to the key elsewhere in the program, GC can reclaim the key’s memory. As a result, the corresponding key-value pair is automatically removed from the WeakHashMap.

**Use Cases for WeakHashMap:**

- **Cache Implementation:** WeakHashMap is useful for creating caches where entries can be automatically removed if they are no longer being actively used. This helps with memory management as unused entries are discarded by GC.
- **Weak References:** When you need to associate data with an object but don’t want to prevent its garbage collection, a WeakHashMap can be a good choice.

---

## 292. What is the difference between these interfaces- Predicates,Supplier,Consumer and Function?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Very Good link on functional interfaces down below,

[https://www.baeldung.com/java-8-functional-interface](https://archive.ph/o/jDKAO/https://www.baeldung.com/java-8-functional-interfaces)

> Repeated Questions in every Java Dev Interview
> 

I am writing down repeated question from database and hibernate, Not putting the answer as they are very easy to know. If you don't know please comment i will provide the answers. You can also provide the answers.

Consider this as a homework lol :)

---

## 293. What is the use of Triggers in Database?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Triggers in databases are like mini-programs that run automatically in response to events (inserts, updates, deletes) on a table. They are used for:

- **Data validation and integrity:** ensure data meets specific rules.
- **Automating tasks:** trigger actions like notifications or calculations based on data changes.
- **Data auditing:** track who, what, and when data was modified.

---

## 294. Difference SQL and NoSQL Database?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Here’s the core difference between SQL and NoSQL databases:

**SQL databases:**

- Relational: Data is stored in tables with relationships between them.
- Structured query language (SQL) for access and manipulation.
- Predefined schema (data structure) for strong data integrity.
- Vertically scalable (adding more powerful hardware).
- Good for complex queries and related data.

**NoSQL databases:**

- Non-relational: Data can be stored in various formats (documents, key-value pairs, graphs).
- Less rigid schema, allowing for flexible data structures.
- Horizontally scalable (adding more servers).
- Faster for handling large, unstructured data sets.

---

## 295. What is DataBase Indexing?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Database indexing is like an organized filing system for your database tables. It’s a special data structure that significantly speeds up data retrieval by allowing quick access to specific information.

Imagine a large library without an index. Finding a specific book would involve searching every shelf, one by one. An index in a database works like the library’s card catalog — it points you directly to the location of the data you need without scanning the entire table.

---

## 296. What is Sharding in database?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Sharding in a database is a technique for splitting a large database into smaller, more manageable pieces called shards. These shards are then distributed across multiple servers or nodes. Here’s a breakdown of how it works:

- **Imagine a huge bookshelf:** This bookshelf represents your entire database, overflowing with books (data).
- **Sharding is like dividing the bookshelf:** You split the data into smaller sections based on a chosen criteria (like genre, author, publication date). Each section becomes a shard.
- **Distributing the shards:** Each shard is then placed on a separate server, like placing the categorized books on different shelves in different rooms.

---

## 297. Difference Hibernate First Level and Second Level Caching?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

Hibernate offers two levels of caching to improve application performance by reducing database calls: First-Level Cache and Second-Level Cache. Here’s a breakdown of their key differences:

**Scope**

- **First-Level Cache (L1 Cache):** Session-specific. Exists for the duration of a single Hibernate session. Data loaded by one query within a session is available to subsequent queries within the same session without hitting the database again.
- **Second-Level Cache (L2 Cache):** Optional, application-wide cache. Shared across all Hibernate sessions associated with the same session factory. Data loaded by one session can be reused by other sessions, significantly reducing database interactions.

---

## 298. Difference Get and Load in hibernate?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**Data Fetching Strategy:**

- **get:** Performs an immediate database query to fetch the object identified by the ID.
- If the object exists in the database, it’s returned as a fully populated object.
- If the object doesn’t exist, `get` returns `null`.
- **load:** Returns a proxy object representing the identified entity.
- The actual data from the database is retrieved only when you access a property or method of the object. This technique is called Lazy Loading.
- If the object doesn’t exist in the database, `load` throws an `ObjectNotFoundException` when you try to access its properties.

**Database Interaction:**

- **get:** Always triggers a database query, even if the object is already in the Hibernate cache (first-level cache).
- **load:** Might not trigger a database query immediately if the object is in the cache. The query happens only when you access the object’s data.

---

## 299. Difference Save and Persist in hibernate?

*Source: [`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*

**save:**

- Tries to insert a new record into the database.
- If the object already has an identifier (primary key) assigned, it assumes an update operation and performs an update query.
- Returns the generated identifier (if applicable).

**persist:**

- Marks the object as managed by Hibernate for persistence.
- The actual insert operation happens when the transaction is committed, not necessarily immediately.
- Does not return anything (void).

**Transaction Context:**

- **save:** Can be called within or outside of a transaction. If outside a transaction, the insert might happen right away depending on the Hibernate configuration.
- **persist:** Requires being called within a transaction. This ensures data consistency and avoids potential issues.

---

## 300. How HashMap Works internally?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

HashMap is Hash table based implementation of the `Map` interface. This implementation provides all of the optional map operations, and permits `null` values and the `null` key. (The `HashMap` class is roughly equivalent to `Hashtable`, except that it is unsynchronized and permits nulls.) This class makes no guarantees as to the order of the map; in particular, it does not guarantee that the order will remain constant over time.

***Here is the working:***

- Java HashMap allows null key and null values.
- HashMap is not an ordered collection. You can iterate over HashMap entries through keys set but they are not guaranteed to be in the order of their addition to the HashMap.
- HashMap is almost similar to Hashtable except that it’s unsynchronized and allows null key and values.
- HashMap uses it’s inner class Node<K,V> for storing map entries.
- HashMap stores entries into multiple singly linked lists, called buckets or bins. Default number of bins is 16 and it’s always power of 2.
- HashMap uses hashCode() and equals() methods on keys for get and put operations. So HashMap key object should provide good implementation of these methods. This is the reason immutable classes are better suitable for keys, for example String and Interger.
- Java HashMap is not thread safe, for multithreaded environment you should use ConcurrentHashMap class or get synchronized map using Collections.synchronizedMap() method.

---

## 301. Difference between Put and Post?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

.The PUT method is typically used to create resources if they don’t exist and update them if they do, while the POST method is primarily used only for creating new resources.

*Note — In Java Interview always expect one question from HTTP methods like put vs post and so on.*

---

## 302. Write a program to reverse the array of string without using predefined method?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 303. Difference between comparable and comparator?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 304. What is jdbctemplate ,statement,preparedstatement ,callable statement?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 305. What are these annotations @Component and @Autowired annotation?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 306. What is SQL Injection?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

SQL injection (SQLi) is a dangerous web security vulnerability. Attackers can exploit it to steal, modify, or even delete data from your database.

Imagine a web form where users enter data. If the application doesn’t properly handle that data (sanitize it), attackers can inject malicious SQL code disguised as normal input. This code then gets executed by the database, potentially causing havoc.

To prevent SQLi, follow these security measures:

- Validate user input to make sure it’s what you expect.
- Use special techniques (prepared statements) to separate user input from the actual SQL query.
- Consider using stored procedures for complex queries.
- Keep your software updated with the latest security patches.

By taking these steps, you can make your web application much more secure against SQL injection attacks.

---

## 307. What is session and sessionfactory in Hibernate?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 308. What is HQL?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

HQL stands for Hibernate Query Language. In a nutshell, it’s a special query language designed for Hibernate, a popular object-relational mapper (ORM) framework in Java. Here’s the gist:

- **Focuses on objects:** HQL lets you write queries using the names of your Java classes and their properties instead of raw database tables and columns. This makes it more readable and less prone to errors compared to writing pure SQL.
- **Behind the scenes translation:** When you execute an HQL query, Hibernate translates it into the corresponding SQL statement for your underlying database. This frees you from worrying about the specifics of different database dialects.

So, HQL provides a convenient and object-oriented way to interact with your database through Hibernate.

---

## 309. What are Joins?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

joins are a fundamental concept for combining data from multiple tables. They allow you to retrieve related information from different tables based on a shared field. Imagine you have a database for an online store:

- One table (`customers`) stores customer information like names and IDs.
- Another table (`orders`) stores details about orders, including the customer ID (linking it to the `customers` table).

To get a complete picture, you might want to combine customer details with their corresponding orders. This is where joins come in.

Here are the different types of joins you can use to achieve various results:

- **Inner Join:** This is the most common type. It returns only rows where there’s a match in both tables based on the join condition. For example, you could retrieve customer names and their corresponding order details.
- **Left Join:** This includes all rows from the left table (the one you specify first), and matching rows from the right table. Rows from the right table with no match on the join condition will have null values for the joined columns.
- **Right Join:** Similar to a left join, but it includes all rows from the right table and matching rows from the left table. Unmatched rows in the left table will have null values.
- **Full Join:** This combines all rows from both tables, regardless of whether there’s a match in the join condition. Unmatched rows will have null values in the corresponding columns.

---

## 310. What is the difference between Primary and Foreign key?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Both primary keys and foreign keys are crucial for maintaining data integrity and relationships within relational databases, but they serve distinct purposes:

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

---

## 311. What is REST-API?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

REST API (or RESTful API) stands for Representational State Transfer API. It’s a popular architectural style for designing web APIs. In short, it defines a set of rules for how APIs communicate using HTTP requests and responses. This allows applications to easily interact with each other in a standardized way, regardless of the programming language used. Imagine it as a universal language for applications to exchange information over the web.

---

## 312. When to use Encapsulation and Abstraction in your project?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 313. Explain Lazy Loading and Eager Loading?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Lazy loading and eager loading are two strategies for fetching data in object-relational mapping (ORM) frameworks like Hibernate. They determine when and how related entities (objects) are loaded from the database.

**Lazy Loading:**

- **Delays Loading:** Data is retrieved only when it’s explicitly needed. Imagine a product listing page that displays basic product details (name, price) initially. Lazy loading ensures related information like product descriptions or reviews are loaded only when the user clicks on a specific product.
- **Performance Benefits:** By avoiding unnecessary database queries for data that might not be used, lazy loading can improve initial page load times.
- **Potential for Extra Queries:** If you do end up needing the related data, lazy loading will trigger additional database queries, which might add some overhead.

**Eager Loading:**

- **Loads Everything Upfront:** All related data is fetched along with the primary object in a single database query. This means all product details (description, reviews) might be loaded on the initial product listing page, even if the user doesn’t view them all.
- **Faster Access to Related Data:** Since the data is already available, accessing related information doesn’t require additional database queries, potentially improving performance for scenarios where you need to use most or all of the related data.
- **Potentially Slower Initial Load:** Eager loading can lead to slower initial page load times if you’re fetching a lot of data that might not be immediately needed.

---

## 314. When to use these annotation in your project — @GetMapping and @PostMapping?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 315. What is Exception Handling rule for Method Overriding?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 316. Explain Spring MVC flow in detail?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 317. What happens when there is a exception occurs in Finally block?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 318. What is the Diamond problem in java?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 319. What is Multilevel Inheritance?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

In multilevel inheritance, a class inherits properties and methods from another class, which itself inherits from yet another class. This creates a hierarchy of classes where each class inherits from the one above it in the chain.

Here’s a breakdown of multilevel inheritance in Java:

**Structure:**

Imagine a family tree:

- **Grandparent Class:** Represents the most base class in the hierarchy.
- **Parent Class:** Inherits properties and methods from the grandparent class.
- **Child Class:** Inherits properties and methods from the parent class.

**Inheritance Chain:**

The `Child` class inherits indirectly from the `Grandparent` class through the `Parent` class. The `Child` class has access to all public and protected members (methods and properties) of both the `Parent` and `Grandparent` classes.

---

## 320. Difference between String ,Stringbuffer and Stringbuilder?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Note: String is important topic in Beginners level interview

---

## 321. How to create immutable class in java?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Most common question Java dev interview, If you are following me since long i have written its answer multiple time.

---

## 322. What is the Method Overloading and Overriding?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 323. Difference between Arraylist and Linkedlist?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

**Difference between Set and Arraylist?
How to Create Custom exception in spring boot?
What is Java-8 features — Explain stream api and functional interface?
What is Microservice in details?**

---

## 324. What are resources in the context of REST APIs, and how are they identified?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 325. What is the role of HTTP methods (GET, POST, PUT, PATCH, DELETE) in REST APIs?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

*I think everyone knows this, thats why keeping it blank.*

> Advanced REST API Concepts
>

---

## 326. How would you troubleshoot issues with REST API resource requests?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 327. What are cache-control headers, and how do they impact API performance?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 328. How can you protect a REST API from spamware or bots?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 329. What are payloads in RESTful web services?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

There are json payload in rest and mostly we have request payload and response payload. Example look like this,

```
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

> Testing and Tools
>

---

## 330. Which tools would you use to test a REST API, and what steps would you follow during testing?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 331. How do you validate the response format and status codes of an API?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

These Rest API testing questions usually asked to tester who is doing the api testing and need to setup env related to that. developer can skip this.

> Microservices and System Design
> 

In Microservice, Design related Questions is must one below i have documented. [Top 5 Design Patterns Asked in Java Developer Interview](https://archive.ph/o/c910J/https://medium.com/javarevisited/top-5-design-patterns-asked-in-java-developer-interview-67df7b3c1599).

---

## 332. What are the challenges of implementing microservices compared to monolithic applications?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 333. Explain decomposition design patterns in microservices?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 334. How do you monitor the health of microservices in a distributed system?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

I will give you answer from my experience,

1. We have inbuilt end-points available as actuators in the spring boot app that we can use in kubernetes to check the pod health
2. We have implemented Zipkin, Open Telemetry for distributed tracing that helps in service to service communication.
3. also we should have centralised logging like splunk
4. to monitor key metrics we can use prometheus
5. for alerts we can use aws cloud-watch or any other tool.

> Spring Framework & Annotations
> 

You should know each and every concepts of spring framework, it s essential to succeed in the interview. I have documented all the possible spring framework related interview questions here and its worth reading for [**Top 60 Spring-Framework Interview Questions for Java Developers 2024(Contain All the Questions from…**](https://archive.ph/o/c910J/https://medium.com/@rathod-ajay/top-60-spring-framework-interview-questions-for-java-developers-2024-contain-all-the-questions-from-f15621f77d2a)

---

## 335. What is the @CrossOrigin annotation in Spring, and when would you use it?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

The `@CrossOrigin` annotation in Spring is used to enable Cross-Origin Resource Sharing (CORS) for specific methods, controllers, or globally across the application. CORS is a security feature implemented by browsers to prevent unauthorized cross-origin requests, but it can block legitimate requests in scenarios where the frontend and backend are hosted on different domains.

When Would You Use @CrossOrigin?

Frontend-Backend Communication

- If your frontend (e.g., React or Angular) and backend (Spring Boot REST API) are hosted on different domains or ports, you need `@CrossOrigin` to allow cross-origin HTTP requests.

Granular Control

- Use `@CrossOrigin` at the method or controller level to specify which origins, headers, and HTTP methods are allowed.

Global Configuration

- Apply CORS settings globally when you want all endpoints to accept cross-origin requests.

---

## 336. Why are searches using primary keys faster than other queries?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 337. How would you implement rate-limiting for an API endpoint?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

So basically this is a system design Interview question, I would recommend Alex xu’s system design interview book which i have myself referred it for such a question and its a must have book for every software engineer.

---

## 338. What is content negotiation in microservices?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Content negotiation in microservices refers to the process where a client and a server agree on the format of data to be exchanged during an HTTP request/response.

It enables a microservice to deliver responses in multiple formats, such as JSON, XML, or plain text, based on the client’s preference or capability.

---

## 339. Why do we use Java 8? Why was it introduced over Java 7?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

We use Java 8 because it was introduced as a major upgrade over Java 7 to bring revolutionary features to the language, making it more modern, expressive, and efficient. Some of the features are:

1. **Functional Programming**:Java 8 introduced functional programming paradigms, which simplify and improve how developers write code. This helps in writing cleaner, more readable, and concise code.
2. **Stream API**:A powerful abstraction for processing collections of data in a functional style. Operations like filtering, mapping, and reducing large data sets are now easier and faster.
3. **Better Concurrency**:Java 8 introduced parallel streams, which enable developers to process data in parallel with minimal effort, improving performance in multi-core systems.
4. **Enhanced Productivity**:Features like **lambda expressions**, **method references**, and **default methods** reduce boilerplate code and increase developer productivity.
5. **Date and Time API**:The new `java.time` package provides a modern, immutable, and thread-safe way to handle date and time, replacing the old, clunky `java.util.Date` and `java.util.Calendar`.
6. **Backward Compatibility**:All features in Java 8 are fully backward-compatible, ensuring older codebases work seamlessly while benefiting from new features.
7. **Improved Performance**:With advancements in the JVM and libraries, Java 8 provides better performance for both functional programming and overall application execution.

---

## 340. What is Dependency Injection and what are it’s advantages?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Dependency Injection (DI) is a **technique** used in object-oriented programming to achieve **Inversion of Control (IoC)**.

It involves providing an object (called the *dependent object*) with its dependencies (other objects it depends on) from the outside, instead of the dependent object instantiating them itself.

This approach decouples the creation of objects from their behavior, making the code more modular, testable, and maintainable.

---

## 341. What are advantages of MongoDB over MySQL?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Below are some of the advantages of MongoDB over MySQL in:

---

## 342. Suppose you have 2 threads. One of them prints (1,2,3…) and the other one prints (A,B,C,..). How will you ensure that they run in a sequence, so that it prints (1,A,2,B…)?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 343. What is a Bean? What are the differences between normal Bean vs Spring Bean?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

A **bean** is an object that is instantiated, assembled, and managed by a container.

In the context of **Java**, a bean is a reusable software component that adheres to specific conventions (e.g., having a no-argument constructor, being serializable, and providing getters and setters).

In **Spring**, a bean is any object that is managed by the Spring IoC (Inversion of Control) container.

---

## 344. How do you secure your microservices?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Below are some of the ways to secure your microservices:

---

## 345. Suppose you’ve a controller annotation and then you perform DB operation in it. What will happen in that case?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

If you perform database operations directly inside a controller in a Spring application, it **can technically work**, but it’s considered a **bad practice.**

---

## 346. What are the benefits of using DAO layer?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

The **DAO (Data Access Object)** layer provides a structured way of interacting with a data source, like a database, while abstracting the underlying data persistence mechanism.

Using a DAO layer offers several benefits, especially in terms of maintainability, flexibility, and decoupling of concerns in your application. Below are some of them:

---

## 347. How do you measure DB performance?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Below are some of the ways to measure **database performance**:

---

## 348. How would you design a scalable database? What challenges do you foresee, and how would you mitigate them?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 349. How do you handle exceptions in Spring Boot application?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Exception handling in a Spring Boot application can be managed in an organized way using several key approaches:

---

## 350. How to write a custom method in MongoDB?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Creating a custom method in MongoDB depends on the context of its usage. If the goal is to implement custom queries or operations, it can be achieved through a combination of the following techniques:

---

## 351. What is rebasing in GIT?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

Rebasing in Git is a way to reapply commits from one branch onto another branch in a linear sequence.

It essentially transfers the base of the branch you are working on to another branch, giving you a cleaner project history.

---

## 352. What is the contract between Hashcode and equals method in Java?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

The contract between `hashCode()` and `equals()` can be described as below:

1. **If two objects are equal (as per `equals()` method), they must have the same `hashCode()`.**
- This ensures consistent behavior in hash-based collections.

**2. If two objects have the same `hashCode()`, they are not guaranteed to be equal.**

- Collisions can occur, where different objects share the same hash code.

**3. Overriding `equals()` requires overriding `hashCode()` as well.**

- Failing to do so can lead to inconsistent behavior in collections.

---

## 353. What is a weak hashmap?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

A **`WeakHashMap`** is a type of map in Java where the keys are stored as **weak references**. This means that if there are no strong references to a key object, it can be garbage collected, even if it still exists in the map.

This differs from the regular `HashMap`, where the keys are stored as strong references, preventing the key objects from being garbage collected.

1. **Weak References for Keys**:
- The keys are weakly referenced. If a key is no longer reachable by any active thread (i.e., no strong references exist to it), the entry for that key will be removed from the map during the next garbage collection cycle.

**2. Automatic Garbage Collection**:

- This behavior is particularly useful for caching scenarios where we don’t want the keys to persist in memory unnecessarily once they are no longer used elsewhere.

**3. No Impact on Values**:

- The values in the `WeakHashMap` are **strong references**, meaning they won’t be garbage collected unless they are no longer referenced by any object.

---

## 354. Explain Internal working of concurrent hashmap?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

A **`ConcurrentHashMap`** is a thread-safe map introduced in Java 5, designed for high concurrency, which allows multiple threads to read and write to the map concurrently without blocking each other.

Unlike a regular `HashMap` that is not synchronized and prone to data inconsistency when accessed concurrently, `ConcurrentHashMap` provides an efficient way to handle concurrent operations.

---

## 355. You have a list of student names in a college. How can you convert this list into a set? What happens with the duplicate names?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 356. What Happens to Duplicate Names?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

When converting the list to a set:

1. **Duplicate names are automatically removed** because a `Set` does not allow duplicate elements.
2. Only one instance of each name will remain in the set, ensuring all elements in the set are unique.

For example, if the list contains:`["Alice", "Bob", "Alice", "Charlie", "Bob"]`,the resulting set will contain:`["Alice", "Bob", "Charlie"]`.

This behavior is particularly useful when the goal is to eliminate duplicates from a collection.

---

## 357. Explain deep copy with examples.

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

A **deep copy** refers to creating an entirely new copy of an object, including its nested or referenced objects.

In a deep copy, changes made to the copied object do not affect the original object and vice versa. This is because the deep copy creates new instances for all referenced objects as well.

---

## 358. Find the next greatest element for each element in an array?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 359. What is the difference between Postgres and MySQL database?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 360. What are the Features of Java 8?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 361. What are the Features of Java 17?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 362. What is the difference between these two Singleton and immutability?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 363. How to break singleton design pattern?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 364. What is data engine?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

A data engine, often referred to as a database engine or storage engine, is the underlying software component that a database management system (DBMS) uses to create, read, update, and delete (CRUD) data from a database. It is responsible for managing how data is stored, retrieved, and manipulated.

---

## 365. What will happen if we exchange @Repository and @Service annotations in spring boot project?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

What Happens if Exchanged?

1. **Functionality**: The primary functionality of the application may still work because both annotations make the classes Spring-managed beans. However, the specific roles and behaviors associated with each annotation will be lost.
2. **Exception Translation**: If you annotate a DAO class with `@Service` instead of `@Repository`, you will lose the automatic exception translation feature provided by `@Repository`.
3. **Semantics**: The code will become semantically incorrect, making it harder for other developers to understand the intended design and architecture of the application.
4. **Best Practices**: Violating best practices and conventions can lead to maintenance challenges and potential bugs in the future.

---

## 366. What is functional interface?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 367. What is default size of HashMap?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 368. What is load factor?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

The default initial capacity of a `HashMap` in Java is 16, with a default load factor of 0.75. This configuration helps balance memory usage and performance, providing a good trade-off between space and time complexity for most use cases.

---

## 369. What happens if size increases beyond load factor?

*Source: [`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*

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

---

## 370. What is Polymorphism in Java?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Polymorphism in Java is one of the four fundamental OOP (Object-Oriented Programming) concepts (along with inheritance, encapsulation, and abstraction).

The term literally means “many forms,” and that’s exactly what it allows: the ability of an object, method, or function to behave differently based on the context.

In simple terms, Polymorphism lets you perform the same action in different ways.

---

## 371. Explain Method Overriding.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Method Overriding means providing a new implementation for a method in the subclass that is already defined in the parent class.

This enables runtime polymorphism — the ability to call the overridden method based on the actual object type, not the reference type.

---

## 372. Can we override the static method?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**No, static methods cannot be overridden in Java.**

In Java:

- Static methods belong to the class, not to instances.
- Method overriding is a concept that applies to instance methods, resolved at runtime using the actual object type.
- Static methods are resolved at compile-time using the reference type, not the object.

If a subclass defines a static method with the **same signature** as a static method in the parent class, it’s not overriding — it’s called **method hiding**.

---

## 373. Why are strings immutable in Java?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

In Java, `String` is immutable, meaning once a `String` object is created, it cannot be changed.

Any operation that appears to modify a string (like `concat()`, `substring()`, `replace()`, etc.) actually creates a new string object.

Here are the core reasons why:

---

## 374. How to create an Immutable class in Java?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

I have already written a detailed article on the same. This would be one of the best article you’ll find on this topic:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/0meNk/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

---

## 375. Suppose you’ve a list of objects. How to change this list of objects to immutable?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

If you have a `List<Object>` and you want to make sure no one can modify it, below are the recommended ways:

---

## 376. How do you achieve deep cloning?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Deep cloning in Java means creating a completely independent copy of an object, including all objects referenced by it (and their references too), so that changes in the cloned object do not affect the original one at all.

There are multiple ways to achieve deep cloning:

---

## 377. What is the contract between equals and hashcode method?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

> This questions was also asked in Collabera Interview (Question - 3). So, this is an important question.
> 

Java defines a strict contract between `equals()` and `hashCode()` to ensure consistent behavior when objects are stored in hash-based collections like `HashMap`, `HashSet`, or `Hashtable`.

The Contract goes like:

1. If two objects are equal (i.e., `a.equals(b)` returns `true`), then their hash codes must also be equal (`a.hashCode() == b.hashCode()`).
2. If two objects have the same hash code, they are not necessarily equal. (`a.hashCode() == b.hashCode()` does not imply `a.equals(b)`).
3. If `equals()` is overridden, you must override `hashCode()` to maintain the contract.
4. Both `equals()` and `hashCode()` should return the same result unless the object is modified.

---

## 378. Is it possible to insert a duplicate key in a HashMap?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 379. Can you have null as a key in HashMap?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 380. What are the advantages and disadvantages of using Hibernate?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Below are the advantages and disadvantages of using Hibernate:

---

## 381. How to enhance the performance of Hibernate queries?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Below are a list of practical ways to boost Hibernate performance:

---

## 382. What is a dialect in Hibernate?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

In Hibernate, a dialect is basically a bridge between Hibernate and your database.

A dialect is a class in Hibernate that tells it how to generate SQL for a particular type of database (e.g., MySQL, Oracle, PostgreSQL, etc.).

---

## 383. How to implement HTTPS?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

To implement HTTPS in your web application, you’re essentially enabling secure communication over HTTP by using SSL/TLS certificates.

Here’s a step-by-step guide to implement HTTPS:

---

## 384. What are the types of IOC containers?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

In Spring, there are two main types of IoC (Inversion of Control) containers, both of which are part of the Spring Framework and responsible for managing the lifecycle and dependencies of beans.

They are:

---

## 385. Why dependency injection is useful?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Dependency Injection (DI) is useful because it makes your code loosely coupled, easier to maintain, testable, and flexible.

---

## 386. Explain @Controller annotation.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The `@Controller` annotation in Spring is used to mark a Java class as a web controller, which means it’s ready to handle HTTP requests in a Spring MVC web application.

---

## 387. Explain @RequestMapping annotation.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The `@RequestMapping` annotation in Spring is used to map web requests to specific handler methods in controller classes.

It tells Spring which URL path, HTTP method, and optionally headers, parameters, and content types a method should respond to.

---

## 388. How to create a thread? What is the most recommended way to create a thread?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

There are multiple ways to create a thread, but some methods are more efficient and easier to manage than others.

---

## 389. What is a deadlock and How can it be avoided?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

A deadlock is a situation where two or more threads are blocked forever, each waiting for the other to release a lock.

**Think of it like this:**

- Thread A has Lock 1, and wants Lock 2.
- Thread B has Lock 2, and wants Lock 1.
- Both are stuck. No one moves. This is deadlock.

---

## 390. Explain different states of a thread.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Below are main states of threads, and understanding them is key to mastering multithreading:

---

## 391. Once a thread is terminated, can we restart a thread?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

No, once a thread is terminated, it cannot be restarted.

In Java, a thread goes through several states:

```
NEW → RUNNABLE → RUNNING → TERMINATED
```

Once it reaches TERMINATED, it’s dead. The thread object can’t be started again using `.start()` — doing so throws an exception.

---

## 392. What are the types of Exceptions in Java?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Java exceptions fall into two main categories under the `Throwable` class:

```
Throwable
├── Exception         --> Recoverable issues
│   ├── Checked       --> Must handle (compile-time)
│   └── Unchecked     --> Runtime exceptions (optional to handle)
└── Error             --> Unrecoverable issues (like JVM crash)
```

---

## 393. Explain try-with-resource in Java.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

`try-with-resources` is a try block that automatically closes resources (like files, streams, DB connections) once you're done using them.

---

## 394. What is Dependency Injection and How does SpringBoot support it?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Dependency Injection is a design pattern used to implement Inversion of Control (IoC).

It allows a class to receive its dependencies from external sources, rather than creating them itself.

This makes your code:

- Loosely coupled
- Easier to test
- More maintainable

---

## 395. What is Circular Dependency and How does SpringBoot handle it?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

A circular dependency occurs when two or more beans depend on each other, either directly or indirectly, in such a way that it creates a loop.

This leads to a situation where Spring cannot resolve the dependencies and inject them properly.

Circular dependencies can be problematic because they create an infinite loop of dependency resolution, causing the Spring context to fail to initialize.

**For example:**

- Bean A depends on Bean B.
- Bean B depends on Bean A.

This circular reference makes it impossible for Spring to figure out which bean should be created first.

---

## 396. What are some best practices for tuning performance of your SpringBoot application?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Tuning the performance of a Spring Boot application is crucial to ensure it handles high loads efficiently, minimizes resource consumption, and delivers faster responses. Here are some best practices you can follow:

---

## 397. How would you divide your monolithic application into a microservice application?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Dividing a monolithic application into microservices is a complex task that needs strategy, patience, and a deep understanding of the current system.

Here’s how we can go about it step by step:

---

## 398. Define APIs and Contracts

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Microservices need to talk to each other via APIs:

- Define REST, GraphQL, or gRPC contracts.
- Use OpenAPI/Swagger for documentation.
- Ensure backward compatibility for smooth migration.

---

## 399. Write a program to find the list of unique words from a sentence?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 400. If the userService is up but returns HTTP 500 for some IDs, will the fallback be triggered?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
@FeignClient(name = "userService", fallback = UserFallback.class)
public interface UserClient {
    @GetMapping("/user/{id}")
    User getUser(@PathVariable String id);
}
```

---

## 401. What issues might arise under concurrent access?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 402. Why might “LazyService initialized” not print during application startup?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
@Service
@Lazy
public class LazyService {
    public LazyService() {
        System.out.println("LazyService initialized");
    }
}
```

---

## 403. Are withdraw() and deposit() methods transactional?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 404. What happens when an exception is thrown?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
@KafkaListener(topics = "orders")
public void listen(String message) {
    throw new RuntimeException("Processing failed");
}
```

---

## 405. Why might this Dockerfile fail during build?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
FROM openjdk:17
COPY target/app.jar app.jar
CMD ["java", "-jar", "app.jar"]
```

---

## 406. Why does “Attempting…” print only once?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
RetryTemplate template = new RetryTemplate();
template.execute(context -> {
    System.out.println("Attempting...");
    throw new RuntimeException("Failure");
});
```

---

## 407. Why might this call hang longer than expected?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
RestTemplate restTemplate = new RestTemplateBuilder()
    .setConnectTimeout(Duration.ofSeconds(1))
    .build();

restTemplate.getForObject("http://slow-service.com", String.class);
```

---

## 408. Which thread runs this?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
@GetMapping("/async")
public CompletableFuture<String> go() {
    return CompletableFuture.supplyAsync(() -> Thread.currentThread().getName());
}
```

---

## 409. Implement a Trie (Prefix Tree) with three methods:

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

- `insert(word)`
- `search(word)`
- `startsWith(prefix)`

---

## 410. What will be the output of the following code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 411. Why does the following never terminate?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 412. What will be the output?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(List.of(10, 5, 20));
        System.out.println(pq.poll());
    }
}
```

---

## 413. Will transactions work in this code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 414. Why does this code always return the same prototype bean?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 415. What happens if the fallback method itself fails in @CircuitBreaker?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

```
@CircuitBreaker(name = "myService", fallbackMethod = "fallback")
public String callService() {
    throw new RuntimeException("Service Down");
}
public String fallback(Throwable t) {
    throw new RuntimeException("Fallback Failed!");
}
```

---

## 416. What will be the output of below code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 417. What will the below code print?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 418. Will the below code compile?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 419. What will happen in the below code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 420. Can you count word occurrences?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 421. What will the output of below code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 422. What will be the output of the following code, and how does lazy evaluation impact performance?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer:**

```
Filtering: A
Filtering: B
Filtering: C
C
```

- **Lazy Evaluation**: `findFirst()` short-circuits the stream. As soon as `"C"` is found, no further elements are processed.
- **Performance Improvement**: If the stream had a large dataset, this optimization prevents unnecessary filtering operations.
- **Edge Case**: If the stream didn't contain `"C"`, no output would be printed.

---

## 423. What will be the output of this code? What happens if we swap peek() and limit()?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer:**

```
1122334455
```

- **Lazy Execution**: `peek(System.out::print)` executes before `limit(5)`.
- **Effect of Swapping**: If `limit(5)` comes before `peek(System.out::print)`, only 5 numbers will be printed once, reducing redundant operations.
- **Performance Tip**: Avoid unnecessary `peek()` calls before filtering or limiting a stream.

---

## 424. What will be the output of this code? What is the performance issue here?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer:**

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

---

## 425. What will be the output, and how does nullsLast() change behavior?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer:**

```
[null, Apple, Banana, Mango]
```

- `nullsFirst()` moves `null` values to the beginning.
- **Changing to `nullsLast()` would push `null` values to the end:**

```
[Apple, Banana, Mango, null]
```

- **Edge Case**: If there were multiple `null` values, sorting order would remain unchanged for them.

---

## 426. What will be the output of this code?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer:**

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

---

## 427. What happens if we try to use a stream twice?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer (Expected Error):**

```
Exception in thread "main" java.lang.IllegalStateException: stream has already been operated upon or closed
```

- Streams cannot be reused once a terminal operation is performed.
- **Fix:** Convert the stream into a list (`List<String> list = stream.collect(Collectors.toList());`) before reusing it.

---

## 428. What happens when two elements map to the same key?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

**Answer (Expected Error):**

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

---

## 429. Write a query to find the 3rd highest salary from an Employee table without using LIMIT.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

```
SELECT Salary
FROM (
    SELECT Salary,
           DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) AS RankedSalaries
WHERE rnk = 3;
```

**Explanation:**

- `DENSE_RANK()` creates a ranking of salaries in descending order.
- The subquery assigns a rank to each salary.
- The outer query filters for the 3rd highest salary.

---

## 430. Write a query to find the second-highest salary in each department from the Employee table.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

```
SELECT Department, Salary AS SecondHighestSalary
FROM (
    SELECT Department, Salary,
           DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS rnk
    FROM Employee
) AS RankedSalaries
WHERE rnk = 2;
```

**Explanation:**

- `DENSE_RANK()` assigns the same rank to equal values, ensuring correct handling of ties.

---

## 431. Write a query to remove duplicates from a table without using DISTINCT.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

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

**Explanation:**

- `ROW_NUMBER()` assigns a unique rank to duplicates.
- Rows with `rn > 1` are deleted, keeping the first occurrence.

---

## 432. Write a query to find employees who logged in for 3 consecutive days.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

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

**Explanation:**

- `LAG()` checks the previous two login dates.
- If they form a consecutive sequence, they are included in the result.

---

## 433. Write a query to calculate the cumulative sum of sales, resetting when the value becomes negative.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

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

**Explanation:**

- `CASE` creates a reset flag when the value is negative.
- `SUM()` partitions the data based on the reset flag.

---

## 434. Write a query to find the median value in a table.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

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

**Explanation:**

- `RANK()` ensures ties are handled correctly.
- `FLOOR` and `CEIL` select the middle values when the count is even.

---

## 435. Write a query to calculate a running total of sales for each month using a window function.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

```
SELECT SaleID, Month,
       SUM(SaleAmount) OVER (PARTITION BY Month ORDER BY SaleID) AS RunningTotal
FROM Sales;
```

**Explanation:**

- `SUM()` creates a running total within each month.
- `PARTITION BY` resets the total at the start of each new month.

---

## 436. Write a query to find the department with the highest total salary using window functions.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

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

**Explanation:**

- The total salary is calculated for each department.
- `RANK()` assigns a rank based on total salary.
- The highest-ranked department is returned.

---

## 437. Write a query to find missing values in a sequential column of IDs.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

```
SELECT t1.ID + 1 AS MissingID
FROM table t1
LEFT JOIN table t2 ON t1.ID + 1 = t2.ID
WHERE t2.ID IS NULL;
```

**Explanation:**

- The query checks for missing `ID` values using a `LEFT JOIN`.

---

## 438. Write a query to find overlapping date ranges from a Bookings table.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

**Answer:**

```
SELECT t1.*, t2.*
FROM Bookings t1
JOIN Bookings t2
ON t1.BookingID != t2.BookingID
AND t1.StartDate <= t2.EndDate
AND t1.EndDate >= t2.StartDate;
```

**Explanation:**

- The query checks if one booking’s date range overlaps with another’s using a `JOIN`.

---

## 439. What do you understand by Stream not storing elements?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

When we say “Stream does not store elements” in Java, it means: Streams don’t hold or contain data.

Instead, they operate on data from a source (like a collection, array, or I/O channel) and process elements on demand — i.e., lazily.

---

## 440. What is Parallel Stream?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

A Parallel Stream is a special kind of Java Stream that splits the data processing across multiple threads to perform operations in parallel, rather than sequentially.

It uses multiple CPU cores to process elements concurrently, which can significantly improve performance on large datasets — if used correctly.

---

## 441. What Predicate does Filter() accepts?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The `filter()` method in Java Streams accepts a `Predicate<T>` functional interface, where `T` is the type of elements in the stream.

It’s a functional interface with this method:

```
@FunctionalInterface
public interface Predicate<T> {
    boolean test(T t);
}
```

So, it takes an input of type `T` and returns a `boolean`. In the context of `filter()`, it tells the stream whether to keep or discard an element.

---

## 442. Suppose we have a method in a super class throws file not found exception. Now it’s sub class with same method overrides and throw IO Exception, will it work fine or error?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Here:

- Superclass method: throws `FileNotFoundException`
- Subclass method (overriding): throws `IOException`

So, when overriding a method, the subclass cannot declare a broader (more general) checked exception than the method in the superclass.

It can throw a narrower exception (i.e., subclass of the original), but not a broader one.

So:

- `FileNotFoundException` is a subclass of `IOException`.
- That means `IOException` is broader than `FileNotFoundException`.

---

## 443. In a class, we are overriding hashcode method and explicitly returning 0 every time. How will it impact the application?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 444. What do you understand by concurrency?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

In Java, concurrency refers to the ability to run multiple tasks simultaneously or overlapping in time in such a way that it makes optimal use of available resources (like CPU cores).

Java provides several mechanisms to manage concurrency, from low-level thread management to high-level abstractions like the Executor framework.

Let’s dive deeper into how concurrency is achieved in Java and the tools it offers to handle concurrent tasks.

---

## 445. What do you understand by Facade design pattern?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The Facade Design Pattern is a structural design pattern that provides a simplified interface to a complex subsystem.

It acts like a front-facing interface that hides all the inner workings of a system and exposes only what is necessary to the client.

Think of it like a hotel reception — you don’t need to know how room booking, housekeeping, and dining work internally. You just go to the reception (facade), and they take care of everything behind the scenes.

---

## 446. What is Atomic Integer class?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

`AtomicInteger` is a class in `java.util.concurrent.atomic` package that provides lock-free, thread-safe operations on a single `int` value.

In multithreaded environments, when multiple threads try to read-modify-write a shared integer (e.g., incrementing a counter), race conditions can occur. `AtomicInteger` solves this problem without using synchronization (i.e., no `synchronized` block or method).

It uses low-level atomic CPU instructions like compare-and-swap (CAS) under the hood for high performance.

---

## 447. Suppose you have to design a system like Uber, so how will you go about it?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

We can start with some high level design like below:

---

## 448. What are the best principles to follow while coding?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

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

---

## 449. Explain the internal working of ConcurrentHashMap.

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

`ConcurrentHashMap` is a thread-safe collection designed for high concurrency with better performance than `Hashtable` or `Collections.synchronizedMap`.

---

## 450. What are One-to-One, One-to-Many, Many-to-One, and Many-to-Many relationships in DB design?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Below are the details of the relationships in DB design:

---

## 451. How do you ensure safe concurrent updates in real-time systems?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Real-time systems demand high throughput, low latency, and consistency under concurrency.

Here’s how we handle it:

---

## 452. Suppose you have a DB server in multiple time zones. How will you handle time zones for queries that are supposed to run at a specific time?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

To handle time zones effectively in a database server with multiple time zones, ensuring queries run at specific times, we can follow these strategies:

---

## 453. Can you set a Default time zone for an entire application?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Yes, you can set a default time zone for an entire application to ensure consistent time handling across different parts of your application.

---

## 454. What is Inversion of Control?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

Inversion of Control (IoC) is a design principle in software engineering where the control of object creation, configuration, and management is transferred from the application code to an external system or framework.

This principle helps decouple components, making the system more modular, flexible, and testable.

In a traditional application, the flow of control is straightforward: you, the developer, call methods and manage object creation and their dependencies directly.

With IoC, the control is inverted. Instead of the application managing the creation and life cycle of its objects, an external component (such as a framework or container) takes responsibility for it.

---

## 455. What do you understand by error: “Application Context is not loading in runtime”?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The error “Application Context is not loading in runtime” typically occurs in Spring-based applications, especially when using Spring Framework for dependency injection and other aspects of application context management.

This error can happen due to various reasons, often related to issues during the application startup.

---

## 456. Suppose with the previous error you also get the error message: Unsatisfied dependency. What could be the reason for it?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

The error **“Unsatisfied dependency”** along with **“Application Context is not loading in runtime”** typically occurs when Spring is unable to inject the required dependencies into a bean during the application context initialization.

This error can happen for several reasons:

---

## 457. What is a Stream in Java?

*Source: [`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*

A Stream in Java is a sequence of elements that supports functional-style operations for processing data.

It was introduced in Java 8 as part of the java.util.stream package and allows for concise, readable, and efficient manipulation of collections (like `List`, `Set`, etc.).

---

## 458. What is Garbage Collector in Java?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

> This question was also asked in the TCS Interview (Question 6). So, this is an important question.
> 

The Garbage Collector in Java is an automatic memory management feature that helps in reclaiming memory used by objects that are no longer referenced in the program.

It is part of the Java runtime environment and is responsible for cleaning up memory by deleting objects that are no longer reachable.

---

## 459. What is the daemon thread?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

A daemon thread is a background thread that runs in support of user threads.

It is terminated automatically by the Java Virtual Machine (JVM) when all user (non-daemon) threads have finished execution.

You must call `setDaemon(true)` before starting the thread.

---

## 460. What is the Contract Between equals() and hashCode() in Java?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Java defines a strict contract between `equals()` and `hashCode()` to ensure consistent behavior when objects are stored in hash-based collections like `HashMap`, `HashSet`, or `Hashtable`.

The Contract goes like:

1. If two objects are equal (i.e., `a.equals(b)` returns `true`), then their hash codes must also be equal (`a.hashCode() == b.hashCode()`).
2. If two objects have the same hash code, they are not necessarily equal. (`a.hashCode() == b.hashCode()` does not imply `a.equals(b)`).
3. If `equals()` is overridden, you must override `hashCode()` to maintain the contract.
4. Both `equals()` and `hashCode()` should return the same result unless the object is modified.

---

## 461. How can you make an object a key in a HashMap?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

To use a custom object as a key in a `HashMap`, you must override `equals()` and `hashCode()` properly.

---

## 462. Explain Singleton design pattern.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Singleton ensures that only one instance of a class is created throughout the application and provides a global access point to that instance.

---

## 463. How to stop Cloneable in a Singleton design pattern.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

To prevent someone from breaking Singleton design pattern by cloning the object using the `Cloneable` interface, we must override the `clone()` method.

---

## 464. Explain Chain of Responsibility design pattern.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The Chain of Responsibility is a behavioral design pattern where a request is passed along a chain of handlers, and each handler decides whether to process it or pass it to the next one.

---

## 465. Explain SOLID principles.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

SOLID is an acronym for five core object-oriented design principles that help make software more maintainable, scalable, testable, and robust.

These principles promote clean architecture and are especially useful when working on large systems with evolving requirements.

They were introduced by Robert C. Martin and are considered best practices for designing well-structured, loosely coupled systems in OOP.

---

## 466. What are Default methods?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Default methods were introduced in Java 8 to allow interfaces to have method implementations without breaking existing code.

They help in evolving interfaces over time while maintaining backward compatibility.

---

## 467. How do microservices communicate with each other?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

> This question was also asked in Accenture Interview (Question 15). So, this is an important question.
> 

Microservices communicate using different mechanisms depending on the system’s architecture, performance needs, and reliability requirements.

These mechanisms can be broadly categorized into synchronous and asynchronous communication.

---

## 468. If I make a variable static, will it take part in the serialization process?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

No, static variables do not take part in the serialization process.

- Serialization is the process of converting an object’s state into a byte stream so it can be persisted or transferred.
- Static variables belong to the class, not to any specific instance.
- Since serialization is all about saving the state of an object instance, and static variables are not part of the object’s state, they are ignored during serialization.

---

## 469. Explain Internal working of Hashset.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

`HashSet` is a collection class in Java that stores unique elements. Internally, it uses a `HashMap` to store its elements.

It does not maintain insertion order and allows only one null element.

---

## 470. How can you make a HashMap synchronised?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

By default, `HashMap` is not synchronized, meaning:

- It is not safe to use in multi-threaded environments where multiple threads access and modify it concurrently.
- This can lead to data inconsistency, race conditions, or even infinite loops during iteration (due to structural changes).

---

## 471. What is Collections Class?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The `Collections` class in Java is a utility class that belongs to the `java.util` package.

- It cannot be instantiated.
- It provides static methods to operate on or return collections such as List, Set, and Map.
- Think of it as a helper toolbox for collection-related operations like sorting, searching, shuffling, synchronizing, etc.

---

## 472. Explain any three microservice design patterns.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Below are three commonly used microservice design patterns:

---

## 473. Explain Circuit Breaker Design Pattern.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

> This question was asked in both first and second rounds at Capgemini Interview, TCS Interview and CGI Interview. So, this is an important question.
> 

In a microservices architecture, a Circuit Breaker is a design pattern used to detect failures in a system and prevent them from propagating to other parts of the system.

It helps in improving the system’s resilience by allowing the system to recover from failures gracefully.

The main goal is to prevent a system from repeatedly making calls to a service that is failing and causing additional load or cascading failures.

---

## 474. Explain Bounded Context in Microservices.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Bounded Context is a core concept from Domain-Driven Design (DDD). It refers to a well-defined boundary within which a particular domain model is applicable and consistent.

In a microservices architecture, each microservice is treated as a Bounded Context, meaning it owns its data, business logic, and responsibilities, without overlapping with other services.

---

## 475. Explain API Gateway.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

I have already written a detailed article with additional interview questions on API Gateways. I recommend you to please go through the it:

[**API Gateway with Spring Boot: Deep Dive with Interview QuestionsA Comprehensive Guide**medium.com](https://archive.ph/o/ckOOF/https://medium.com/coding-odyssey/api-gateway-with-spring-boot-deep-dive-with-interview-questions-1a65954ad5f3)

---

## 476. Suppose we have multiple microservices and we jump from one microservice to another. How the other microservices maintain sessions?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In a microservices architecture, traditional server-side session handling (like `HttpSession`) doesn’t scale well across multiple services.

So instead of maintaining state on the server, microservices use stateless authentication, usually through JWT (JSON Web Tokens).

---

## 477. What is Event Sourcing?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Event Sourcing is a design pattern where state changes in an application are captured as a sequence of immutable events, instead of storing only the latest state in a database.

---

## 478. How to scale your microservices application?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

> This question was also asked in the TCS Interview. So, this is an important question.
> 

Scaling a microservices application involves handling increased load efficiently while maintaining performance, reliability, and cost-effectiveness.

Below are key strategies to scale a microservices-based application:

---

## 479. What is the default message size in Kafka?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The default maximum message size in Apache Kafka is: *1 MB.*

This is enforced through two main configurations:

- On the **broker side**: `message.max.bytes`
- On the **producer side**: `max.request.size`

---

## 480. What parameters are to be configured for a flow of message from Producer to Broker to Consumer in Kafka?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

To ensure a smooth flow of messages from Producer ➝ Broker ➝ Consumer in Apache Kafka, each component must be properly configured.

These configurations help manage message size, reliability, batching, buffering, and performance.

---

## 481. If message is beyond the default size, what happens in Kafka?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

When a message sent to Kafka exceeds the configured size limits, the system will reject the message, and an error will be thrown — either by the producer, broker, or consumer, depending on where the limit is violated.

---

## 482. What Happens When a Limit is Exceeded?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

**Case 1: Message too large on Producer**

- Kafka producer throws an exception:**`RecordTooLargeException`**
- **Reason**: The message (or batch) exceeds `max.request.size`.

**Case 2: Message rejected by Broker**

- Producer receives a **`RecordTooLargeException`** from the broker.
- **Reason:** The broker’s `message.max.bytes` is smaller than the producer’s message size.

**Case 3: Consumer can’t fetch large messages**

- The consumer fails to receive the message if its `fetch.message.max.bytes` or `max.partition.fetch.bytes` is too low.
- You may see partial fetches or missing records.

---

## 483. What is replication factor in Kafka? Give its use cases.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Kafka, the replication factor defines how many copies of each partition are maintained across different brokers in a Kafka cluster.

**For example:**If a topic has 3 partitions and replication factor = 2, Kafka will store 2 copies of each partition (one leader + one follower), across different brokers.

---

## 484. What is fault tolerance? Is it possible to implement fault tolerance using replication factor.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Fault tolerance refers to a system’s ability to continue operating correctly even when some of its components fail.In distributed systems like Kafka, fault tolerance ensures that the system remains available and consistent despite broker failures, hardware crashes, or network issues.

---

## 485. How to change server in Spring Boot?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

To Change Server from Tomcat to Jetty or Undertow:

---

## 486. Explain some REST Methods.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Below are some of the common REST (or HTTP) methods:

---

## 487. Explain PATCH Method.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The PATCH method is used to partially modify an existing resource on the server. Instead of sending the entire resource like `PUT`, you send only the fields you want to update.

---

## 488. What are some of the features of Java 8?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Java 8 was a major release and brought a ton of powerful features that modernized the language. Below are some of the most important features:

---

## 489. Explain Intermediate Operations.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Intermediate operations are the transformations applied to a stream before the final result is obtained. They don’t produce a final result on their own — they just prepare the data.

They’re always followed by a terminal operation like `collect()`, `forEach()`, or `count()`.

---

## 490. What are Default methods and How to implement it in functional interface?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java 8 and later, default methods allow you to add method implementations inside interfaces without affecting the classes that already implement them.

Before Java 8, interfaces could only have abstract methods (i.e., no body). But with default methods, you can now have concrete methods (with body) in interfaces.

---

## 491. What is Transient Keyword?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java, the `transient` keyword is used to mark a variable as non-serializable — meaning, it will not be saved when an object is serialized.

In other words, transient variables are not saved when an object is serialized to a stream and are ignored when the object is later deserialized.

---

## 492. What is an Externalizable Interface?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The `Externalizable` interface is part of Java’s serialization mechanism. It gives complete control over the serialization process, unlike the `Serializable` interface where the JVM automatically serializes all non-transient fields.

When you implement `Externalizable`, you decide how the object is saved and restored by implementing two methods:

- `writeExternal(ObjectOutput out)`
- `readExternal(ObjectInput in)`

---

## 493. What is the internal working of the filter method?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

The `filter()` method is an intermediate operation in the Java Stream API that returns a new stream consisting of the elements that match a given predicate (condition).

**Example:**

```
list.stream()
    .filter(e -> e % 2 == 0)
    .forEach(System.out::println);
```

---

## 494. Explain CyclicBarrier and CountDownLatch.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

`CyclicBarrier` and `CountDownLatch` are synchronization aids in Java's `java.util.concurrent` package, but they serve different purposes.

---

## 495. What is CompletableFuture?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

`CompletableFuture` is a powerful feature introduced in Java 8 (`java.util.concurrent`) that represents a future result of an asynchronous computation.

It provides a flexible way to write non-blocking, asynchronous code using functional programming constructs.

---

## 496. Write a program to reverse an integer array without any inbuilt functions.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

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

---

## 497. What will happen if we insert the same key in the hashmap?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

If you insert the same key into a `HashMap` in Java, it will overwrite the existing value associated with that key.

---

## 498. What is an IdentityHashMap?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

An IdentityHashMap is a specialized implementation of `Map` that compares keys using reference equality (`==`) instead of object equality (`equals()`).

This means that two keys are considered equal only if they are the same object in memory (i.e., they have the same reference), even if `equals()` returns `true` for them.

---

## 499. Write a program to find out the middle element of the linkedlist.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

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

---

## 500. What are rules for Instance variable?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Instance variables in Java are non-static fields that belong to an object (instance of a class). They are declared inside a class but outside any method, constructor, or block.

---

## 501. In the main method, if we declare a variable and not initialize it. What will it print?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java, local variables (including those declared inside the `main` method) do not get default values and must be explicitly initialized before use.

If you declare a variable in the `main` method and try to print it without initializing it, you will get a compilation error.

---

## 502. How to create a spring boot project from scratch?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

I have already written a detailed article on the same. I would recommend you to go through this:

[**Create a Spring Boot Rest API Project From ScratchFor Beginners**medium.com](https://archive.ph/o/0GR7C/https://medium.com/coding-odyssey/create-a-spring-boot-rest-api-project-from-scratch-937737b490f7)

---

## 503. What is the security used in current your project?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

We use **OAuth 2.0 with JWT** for authentication and authorization.

The authentication is handled by an Identity Provider (IdP), and once a user is authenticated, they receive an access token (JWT), which is used to access protected resources.

We have implemented Spring Security along with the OAuth2 Resource Server to validate JWTs. The system is stateless, and we use role-based access control (RBAC) to manage permissions.

---

## 504. Why OAuth2 + JWT?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

- Stateless authentication (no session storage required)
- Scalable (ideal for microservices)
- Secure (signed and encrypted tokens prevent tampering)
- Interoperability (works with third-party IdPs like Google, Okta, Keycloak)

---

## 505. How is JWT Validated in Spring Boot?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

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

---

## 506. How do the requests flow from the controller in OAuth2 + JWT Authentication?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

When a request is made to a secured endpoint in the Spring Boot application, the flow follows these steps:

---

## 507. What is the Response if a GET Call Finds No Entity?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

If a GET request does not find any entity, the response should follow RESTful best practices:

---

## 508. What are some of the features of Java 8 in brief?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Java 8 introduced several major features that significantly enhanced the language.

---

## 509. How to get current timestamp in java 8?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java 8, you can get the current timestamp using the `java.time` package, which provides a better alternative to `java.util.Date`.

---

## 510. Write a program to remove duplicate elements from list using stream API.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

There are 2 cases to remove duplicate elements from a list:

---

## 511. How to setup a database connection for rest API project?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Again, You can refer to the below article. I have created and established a new connection to DB from scratch.

[**Create a Spring Boot Rest API Project From ScratchFor Beginners**medium.com](https://archive.ph/o/0GR7C/https://medium.com/coding-odyssey/create-a-spring-boot-rest-api-project-from-scratch-937737b490f7)

---

## 512. Explain EntityManagerFactory.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java Persistence API (JPA), `EntityManagerFactory` is a crucial component for managing entity managers and interacting with the database efficiently.

- It is a factory class that creates `EntityManager` instances.
- It is heavyweight and should be created only once per persistence unit.
- It manages the persistence unit, including the database connection, configurations, and entity mappings.

---

## 513. Explain @Transactional annotation.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Spring, the `@Transactional` annotation is used for transaction management in database operations.

It ensures that a method executes within a single transaction, meaning that either all changes are committed or none are applied (rollback).

- It is a declarative transaction management annotation in Spring.
- It ensures ACID (Atomicity, Consistency, Isolation, Durability) compliance in database operations.
- It automatically rolls back the transaction if an unchecked exception (`RuntimeException` or `Error`) occurs.
- It is applied at the service layer (not recommended for DAO or controller layers).

---

## 514. How to Connect to Two Different Databases in the Same Spring Boot Project?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Spring Boot, you can configure multiple data sources to connect to two different databases within the same project. This is useful when you need to access two independent databases for different purposes.

We will configure two data sources:

1. **Primary Database** (`MySQL`)
2. **Secondary Database** (`PostgreSQL`)

---

## 515. How to manage the performance of APIs?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Below are some key strategies to optimize and manage API performance effectively:

---

## 516. Implement Caching

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

- Use Redis or In-Memory Cache for frequent API responses.
- Reduces unnecessary DB hits and improves response time.

**Example (Using Spring Boot & Redis):**

```
@Cacheable(value = "employees", key = "#id")
public Employee getEmployeeById(Long id) {
    return employeeRepository.findById(id).orElse(null);
}
```

---

## 517. How is the load balancer implemented in Azure DevOps?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

A Load Balancer ensures that incoming traffic is distributed evenly across multiple instances of an application, improving availability, reliability, and scalability.

In Azure DevOps, you can implement a Load Balancer using Azure Load Balancer, Azure Application Gateway, or Azure Front Door.

---

## 518. If I have a variable of datatype CLOB in Oracle DB, what will be it’s corresponding datatype in postgres?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

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

---

## 519. Explain Generics and its use cases in brief.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Generics in Java allow us to create classes, interfaces, and methods that operate on parameterized types. This provides compile-time type safety and code reusability.

Generics enable a type (class or method) to operate on different data types while maintaining type safety.

---

## 520. What do you understand by code reusability?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

Code reusability means writing code in a way that it can be used multiple times without modification.

Instead of duplicating logic across different parts of a program, reusable code is structured so that it can be called whenever needed, making development more efficient, maintainable, and scalable.

For example, using functions/methods, classes, inheritance, interfaces, generics, and design patterns all contribute to reusability.

---

## 521. How to implement multi threading?

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java, multithreading is implemented using the `Thread` class or the `Runnable` interface. It allows concurrent execution of multiple tasks, improving performance and responsiveness.

---

## 522. Explain ExecutorService.

*Source: [`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*

In Java, ExecutorService is part of the `java.util.concurrent` package and provides a better way to manage multiple threads efficiently.

Instead of manually creating and managing threads, ExecutorService handles thread creation, execution, and reuse, improving performance and resource management.

ExecutorService:

- **Manages thread pools** instead of creating new threads every time
- **Improves performance** by reusing threads
- **Prevents excessive thread creation**, avoiding memory issues
- **Provides control** over thread execution, scheduling, and termination

---

## 523. How can you make your code more flexible (scalable)?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

To ensure our code remains flexible and scalable, we follow key principles such as SOLID, design patterns, dependency injection, and modular architecture.

---

## 524. Implement Open/Closed Principle

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 525. Implement Asynchronous Processing for Scalability

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 526. How can you identify that the written code is most optimal code?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

We can identify if the written code is optimal by evaluating the following factors:

---

## 527. What is ConcurrentHashMap and what are it’s use cases?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

`ConcurrentHashMap` is a thread-safe, high-performance implementation of `Map` from the `java.util.concurrent` package.

It allows multiple threads to read and write simultaneously without locking the entire map, making it more efficient than `Collections.synchronizedMap()`.

---

## 528. What is Java Vert.x? What are it’s advantages and disadvantages?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Vert.x is a reactive, event-driven, and non-blocking framework for building high-performance applications on the JVM (Java Virtual Machine).

It is similar to Node.js but supports multiple languages like Java, Kotlin, Groovy, Scala, and JavaScript.

It follows the reactive programming paradigm and uses a verticle-based concurrency model instead of traditional threads.

---

## 529. Is it possible to use batch jobs using Java Vert.x?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Yes, it is possible to use batch jobs in Java Vert.x.

Vert.x is primarily an event-driven, non-blocking framework, but we can still implement batch jobs using different approaches.

---

## 530. If your batch jobs consumes an endpoint and during the batch run, there is a timeout error. So, how will you retry/reprocess the remaining records?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

When a batch job consumes an external API/endpoint and encounters a timeout error, it’s important to retry or reprocess the failed records efficiently.

Below are different approaches to handle this situation:

---

## 531. Implement Retry Mechanism (Exponential Backoff)

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Before marking a record as failed, retry the request a few times with increasing delay (**exponential backoff**) to avoid overwhelming the endpoint.

---

## 532. How to create a new REST API?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Steps to create a basic REST API for managing users:

---

## 533. How do you deploy your microservices to the containers?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

To deploy microservices into containers, we typically follow these steps:

---

## 534. How do you ensure that your endpoints work with different data formats like json, xml etc?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

To make your REST API endpoints support different data formats like JSON and XML, we need to configure content negotiation properly.

---

## 535. How do you convert your JSON to XML format and vice versa?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

There are multiple ways to convert JSON to XML and vice versa in Java. The most common approach is using Jackson (for JSON processing) and org.json (for direct conversion).

---

## 536. What DB tools you can use to measure performance?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

To measure database performance, you can use both built-in database tools and third-party monitoring tools.

---

## 537. How would you handle logging in a REST API application?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

When it comes to logging in a REST API application, it’s essential for debugging, monitoring, and scaling applications.

---

## 538. What are the different endpoints of actuators.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Spring Boot Actuator provides several built-in endpoints that help monitor and manage your application.

Below are the key Actuator endpoints:

---

## 539. Explain @CrossOrigin annotation.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The `@CrossOrigin` annotation in Spring Boot is used to enable Cross-Origin Resource Sharing (CORS) for REST APIs.

CORS is a security feature in web browsers that prevents unauthorized requests from different origins.

By default, browsers block cross-origin requests for security reasons, and `@CrossOrigin` helps bypass this restriction in Spring applications.

---

## 540. What is Decomposition design pattern in microservices?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In microservices architecture, decomposition is the process of breaking down a monolithic application into smaller, independent services.

The Decomposition Design Pattern ensures that each service is:

- **Loosely coupled** → Independent, reducing dependencies on other services.
- **Scalable** → Can handle increased load efficiently.
- **Manageable** → Easier to develop, deploy, and maintain.

There are two primary approaches to decomposition:

1. Decomposition by Business Capability.
2. Decomposition by Subdomain (Domain-Driven Design — DDD).

---

## 541. How microservices health is checked?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In microservices, health checks ensure that services are running properly and can handle requests.

This is done using health check endpoints, Kubernetes probes, service discovery tools, and monitoring dashboards.

---

## 542. What are different cascading types in JPA?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In JPA, cascade types define how operations (persist, merge, remove, etc.) on a parent entity should affect related child entities.

---

## 543. Why search with primary keys are faster?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Searching with primary keys is significantly faster compared to other types of queries because of the following reasons:

---

## 544. Explain EXISTS and how it is used.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

`EXISTS` is a logical operator in SQL used in `WHERE` clauses to check if a subquery returns any rows. It returns TRUE if the subquery produces at least one row and FALSE if it returns zero rows.

---

## 545. What is the max limit of varchar and what are the differences between Byte and Char in Database?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The maximum size of `VARCHAR` depends on the database system:

**MySQL Limitation**:

- The total row size cannot exceed 65,535 bytes, including all columns.
- UTF-8 encoding can use up to 4 bytes per character, so `VARCHAR(10)` may take up to 40 bytes.

---

## 546. How static works in Inheritance?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In Java, `static` members (methods and variables) have special behavior in inheritance.

Here’s how they work:

---

## 547. Can we change the scope of an overridden method?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Yes, we can change the scope (access modifier) of an overridden method, but only to a wider (more permissive) scope. We cannot reduce the visibility.

---

## 548. Explain Thread lifecycle.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The Thread Lifecycle in Java represents the different states a thread goes through during its execution.

There are six main states in a thread’s lifecycle, and each state transitions based on various events that occur during the thread’s execution.

---

## 549. Can we write default and static methods in a functional interface? If yes, will lambda expressions be allowed to use with it?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Yes, we can write both default and static methods in a functional interface.

However, a functional interface is defined as an interface that has exactly one abstract method. The presence of default or static methods does not break this rule because they are not considered abstract methods.

Lambda expressions are still allowed because they target only the single abstract method (SAM) in the interface.

---

## 550. Can we use an int variable declared outside inside the filter() method in Stream API to check a condition?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Yes, we can use an external `int` variable inside the `filter()` method of the Stream API, but there are certain restrictions.

---

## 551. Explain Object Cloning in Java.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Object cloning is the process of creating an exact copy of an existing object in Java.

It allows you to duplicate an object without manually copying each field. Java provides the `clone()` method for this purpose, defined in the `Object` class.

---

## 552. What are the rules for method overriding in Java?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 553. Explain working of Optional.of() method?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The `Optional.of()` method in Java, introduced in Java 8, is used to create an `Optional` instance that contains a non-null value.

It helps prevent `NullPointerException` by ensuring that the value is present.

---

## 554. Explain Lazy loading in Stream.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Lazy loading in Java Streams means that elements are not processed immediately when a Stream is created. Instead, operations on the Stream are executed only when a terminal operation is invoked.

Java Streams use a pipeline execution model where intermediate operations build a sequence of transformations without performing them until a terminal operation is encountered.

This lazy nature allows Java to optimize performance by deferring computation until absolutely necessary.

---

## 555. Explain Terminal Operations in Streams.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In Java Streams, **terminal operations** are operations that trigger the actual processing of the stream and produce a result or a side-effect. These operations are what cause the **stream pipeline to execute**. Until a terminal operation is invoked, no processing happens, even if intermediate operations are defined.

---

## 556. What are the use cases of FlatMap()?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The `flatMap()` function in Java Streams is used to transform and flatten data structures.

It comes in handy when working with elements in a stream that are collections or even other streams themselves.

It allows you to take each element, apply a function that returns a new stream, and then flatten all those streams into a single stream.

Below are some of the key use cases of `flatMap():`

---

## 557. Explain Factory design pattern.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The Factory Design Pattern is a creational design pattern that provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.

It helps in the process of object creation by delegating the responsibility of creating objects to a specific factory class, rather than directly creating them in client code.

This pattern promotes loose coupling and enhances flexibility, as it abstracts the instantiation process.

---

## 558. Describe the collision resolution mechanism in HashMap and How Java 8 improved it?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

A **collision** in a `HashMap` occurs when two different keys produce the same **bucket index** in the underlying array after applying hashing and modulo-based bucket assignment.

Java’s `HashMap` uses **chaining** as the primary collision resolution technique, meaning that multiple key-value pairs that map to the same bucket are stored within a **linked list**.

---

## 559. What is String interning and how does it affect comparisons?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

String interning is a process where Java stores a single instance of each unique string literal in a special memory area called the String Pool, which resides within the heap.

This allows **efficient memory usage** and **faster string comparisons** using `==`.

When a `String` is interned, Java ensures that all identical string values share the same memory reference in the String Pool.

---

## 560. Describe thread-safety in StringBuffer and how it’s thread safety compares to String and StringBuilder?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 561. Explain Qualifier annotation.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

> This question was also asked in Barclays Interview and Capgemini Interview. So, this is an important question.
> 

The `@Qualifier` annotation in Spring is used to resolve ambiguity when multiple beans of the same type are present in the application context.

It helps Spring to choose which bean to inject when there are multiple candidates for autowiring.

---

## 562. How to handle exception in Spring Boot application?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Exception handling in a Spring Boot application can be managed in an organized way using several key approaches:

---

## 563. How to implement logging mechanism in Spring Boot application?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Spring Boot provides built-in support for logging using **SLF4J** with **Logback** as the default logging framework. Below are some other ways as well:

---

## 564. When to Choose REST?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

- Microservices, mobile applications, IoT, and web applications.
- Public APIs (e.g., Google Maps, GitHub).
- When you need lightweight communication with minimal overhead.
- Scenarios requiring high performance and scalability.

---

## 565. When to Choose SOAP?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

- Enterprise applications that require high security and transactional support (e.g., banking, healthcare, insurance).
- When ACID-compliant transactions are needed (e.g., financial operations).
- When using legacy systems that already rely on SOAP-based services.
- Environments requiring protocol flexibility (not limited to HTTP).

---

## 566. What are the roles of HTTP methods in RESTful APIs?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Below are the HTTP methods used in RESTful APIs:

---

## 567. Explain statelessness in RESTful APIs.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In RESTful APIs, statelessness means that each client request must be self-contained, carrying all the necessary information for processing.

The server does not store client-specific session data between requests, making each request independent.

This adheres to the REST architectural constraints as defined by **Roy Fielding**.

---

## 568. How to secure REST APIs?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Below are some of the best practices to secure your API:

---

## 569. Implement Authentication & Authorization

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 570. Explain HATEOAS and its role in REST API?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

HATEOAS (Hypermedia as the Engine of Application State) is a key constraint of RESTful APIs, where API responses include hyperlinks (hypermedia) that dynamically guide clients on available actions.

This means that instead of hardcoding API endpoints in the client, the client discovers actions through the API response. This makes the system more flexible, loosely coupled, and self-descriptive.

HATEOAS was introduced as part of REST constraints by **Roy Fielding** in his dissertation.

---

## 571. Explain Joins in SQL?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 572. What is aggregation?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

**Aggregation** is a relationship between two classes where one class contains a reference to another class, but both can exist independently.

It represents a **“Has-A” relationship** with weak ownership.

- It is a form of **association**.
- The contained object **can exist independently** of the container.
- It is implemented using **instance variables** in Java.

---

## 573. Why Use Aggregation?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

- **Code Reusability**: The `Address` class can be used in other classes (e.g., `Company` or `Customer`).
- **Maintainability**: Changes to `Address` don’t require modifications in `Employee`.

---

## 574. How heap memory is divided in Java?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In Java, **heap memory** is where objects are stored at runtime. It is divided into different regions to optimize **garbage collection (GC) and memory management**.

---

## 575. Explain System.gc()? Can we use this in production environment?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The `System.gc()` method is a **request** to the JVM to run the garbage collector, but it **does not guarantee** that GC will actually run. It simply **suggests** that the JVM perform garbage collection.

---

## 576. Can We Use System.gc() in Production?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

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

---

## 577. What types of memories are present in Java Memory Model along with their use cases?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The **Java Memory Model (JMM)** defines how Java threads interact with memory and ensures consistency across different hardware and JVM implementations.

Java memory is divided into several types, each serving a specific purpose.

---

## 578. In which section of memory are primitive data types are stored?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Primitive data types (`int`, `char`, `float`, `double`, etc.) are stored differently depending on how they are declared:

---

## 579. What do you mean by memory reference?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

A **memory reference** in Java refers to the address in memory where an object is stored.

Instead of storing actual objects in variables, Java stores references (pointers) to the memory location where the object resides in **heap memory**.

- **References are stored in stack memory**, while objects reside in **heap memory**.
- Java passes a copy of the reference (pass-by-value), meaning modifications affect the object but not the reference itself.
- If no variable holds a reference to an object, it becomes eligible for **garbage collection**.
- **Primitives do not have memory references**; they are stored directly in stack or heap.

---

## 580. Why do we store cookies?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Cookies are small pieces of data stored on a user’s browser by websites. They help websites remember information about users to improve **functionality, performance, personalization, and tracking**.

---

## 581. What do you understand by recursive program?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

A **recursive program** is a program that calls itself within its own execution. In simple terms, **recursion** is a technique where a function **calls itself** to solve a smaller version of the same problem until a base condition is met.

---

## 582. Explain ConcurrentHashMaps. Is it possible for two threads to read or modify a ConcurrentHashMap at the same time?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

A **ConcurrentHashMap** in Java is a thread-safe, high-performance alternative to `HashMap`, designed for concurrent operations.

It belongs to the **java.util.concurrent** package and allows multiple threads to access and modify the map without explicit synchronization.

---

## 583. Can Two Threads Read or Modify a ConcurrentHashMap Simultaneously?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

1. **Two or more threads can read a `ConcurrentHashMap` simultaneously** because read operations do **not** require locking.
2. **Multiple threads can modify different segments of the map at the same time.** Writes are synchronized at the bucket level, meaning:
- If two threads modify **different keys**, they can do so **concurrently**.
- If two threads modify **the same key**, one thread will block until the operation is completed due to internal locks or CAS.

3. **Iteration using `keySet()`, `values()`, or `entrySet()` is weakly consistent** and does **not throw `ConcurrentModificationException`**, unlike `HashMap`.

---

## 584. What do you understand by prototype design pattern? Explain with example and code.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

The **Prototype Design Pattern** is a **creational design pattern** that allows you to **clone existing objects** instead of creating new ones from scratch. This improves performance, especially when object creation is costly.

---

## 585. Explain some annotations in Rest API?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

In **Spring Boot REST APIs**, annotations are used to define **endpoints, request handling, and response processing**.

Here are some of the most commonly used annotations:

---

## 586. Briefly explain some of the new features of Java 8?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Java 8 brought **major enhancements** to the language, making it more functional and efficient. Below are some of the most important features:

---

## 587. Suppose if we don’t override hash code in a hashing collection, then what will be the impact?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

If we **don’t override the `hashCode()` method** in a class used as a key in a **hashing-based collection** (like `HashMap`, `HashSet`, or `HashTable`), it can lead to **unexpected behavior and performance issues**.

---

## 588. Suppose if we don’t override equals method in a hashing collection, then what will be the impact?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

If two objects are considered equal by `equals()`, they must return the same hash code from `hashCode()`.

If we **don’t override the `equals()` method** in a class used as a key in a **hashing-based collection** (like `HashMap`, `HashSet`, or `HashTable`), it can lead to **incorrect behavior, data duplication, and failed lookups**.

---

## 589. How would you detect a deadlock in a running program?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

Deadlocks occur when two or more threads **block each other indefinitely** while waiting for resources held by the other.

---

## 590. Explain Immutable class in Java.

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

> This is a very important question and has been asked multiple times in my interview experiences.
> 

This is the best article you’ll find on Immutable classes., specifically written for this question. I highly recommend it:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/cwO7L/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

---

## 591. Suppose an arraylist reaches it’s threshold, how will it expand itself? What is it’s default size?

*Source: [`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*

When an `ArrayList` reaches its **current capacity**, it automatically **expands** by increasing its size by **50%**. The process follows these steps:

1. **Check if more elements can be added** → If not, **expansion is triggered**.
2. **New array is created** with about **50% more capacity** than the current one.
3. **Existing elements are copied** to the new array.
4. **Reference is updated** to point to the new, larger array.

This ensures that `ArrayList` dynamically grows as needed, but frequent resizing can be costly in terms of performance.

---

## 592. Why Do Deserialization Failures Occur?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 593. Explain use cases of Kafka.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 594. How many types of request and response are generated by Rest API? (Media Types)

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In REST APIs, request and response data are exchanged in different **media types**, which define how data is formatted and transmitted. The most commonly used media types are:

---

## 595. In Hibernate, explain internal workings of lazy loading and eager loading?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Hibernate, **lazy loading** and **eager loading** control how associated entities are fetched from the database.

---

## 596. Suppose you’ve a Java class (with nothing else), now define some techniques that work based on eager loading vs lazy loading?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

**Techniques for Eager loading vs lazy loading** using pure **Java** concepts without Hibernate.

---

## 597. What are the advantages of JPA?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

JPA is a specification for ORM (Object-Relational Mapping) in Java, making database interactions easier by abstracting SQL complexities. It is commonly used with Hibernate, EclipseLink, or OpenJPA.

---

## 598. Explain microservices design pattern?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Below are the microservice design patterns:

---

## 599. How do you create SpringBoot application from command line interface?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

To create a Spring Boot application from the command line, you can use **Spring Initializr** or **Spring CLI**.

---

## 600. How do spring boot application initializes?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

The initialization of a Spring Boot application follows these steps:

1. **Entry Point**: The application starts with a `main()` method in a class annotated with `@SpringBootApplication`.
2. **SpringApplication.run()**: This method initializes the Spring context, applies auto-configuration, and starts the embedded server (if it’s a web app).
3. **ApplicationContext Initialization**: The Spring IoC container is created, and beans are loaded based on component scanning and configuration classes.
4. **Auto-Configuration**: Spring Boot automatically configures beans and components based on the application’s dependencies and environment settings.
5. **Bean Initialization**: Beans are instantiated and injected into other beans as needed, with lifecycle methods like `@PostConstruct` being invoked.
6. **Embedded Web Server (if Web App)**: For web applications, the embedded server (Tomcat, Jetty, etc.) is started to serve HTTP requests.
7. **CommandLineRunner / ApplicationRunner** (Optional): If defined, these interfaces run custom logic after the application context is initialized.

Once all these steps are completed, the application is fully initialized and ready to serve requests or execute background tasks.

---

## 601. Write a program to implement comparator interface in Java.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

To implement the `Comparator` interface in Java, you need to define the comparison logic for the objects of a class. The `Comparator` interface has a single method, `compare()`, which compares two objects.

---

## 602. What is exception handling and why do we need it?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Exception handling is a mechanism in Java that allows us to handle runtime errors gracefully, ensuring that the program doesn’t crash unexpectedly.

It helps in identifying, catching, and managing errors so that we can provide a proper response instead of abrupt termination.

---

## 603. Explain Internal working of HashMap. Also, explain features and use cases of HashMap.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

I have answered this in detail in my HashMap article. I recommend reading this, as HashMap is a very important topic (especially for Junior roles) and it’s very important to understand it completely.

[**HashMap: Deep Dive and Interview QuestionsDive Into HashMaps with Interview Prep**medium.com](https://archive.ph/o/0hnBY/https://medium.com/coding-odyssey/hashmap-deep-dive-and-interview-questions-6cf251baf61a)

---

## 604. If we want to create our own HashMap class, can we do it without extending the HashMap class or implementing the Map interface? What do you need to do?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

It is possible to create your own `HashMap` class without extending the `HashMap` class or implementing the `Map` interface.

You would just need to implement the basic functionality of a `HashMap`, like hashing, handling collisions, resizing, and storing key-value pairs manually.

---

## 605. What is static keyword?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

The `static` keyword in Java is mainly used for memory management. It is used to indicate that a particular variable, method, or inner class belongs to the class itself, rather than to instances of the class. This means you don't need to create an object of the class to access the static member.

The users can apply static keywords with variables, methods, blocks, and nested classes.

---

## 606. Explain Singleton class and how to create a Singleton class.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

**A Singleton class** is a design pattern in software development that ensures a class has only one instance and provides a global point of access to that instance.

This pattern is useful when you want to control access to shared resources, like a configuration manager, logging service, or database connection.

---

## 607. What is an Immutable class and how to create it?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

This is the best article you’ll find on Immutable classes., specifically written for this question. I highly recommend it:

[**Immutable Class in Java: Deep Dive with Interview QuestionsA Deep Dive Into What, Why, and How with Code Breakdown**medium.com](https://archive.ph/o/0hnBY/https://medium.com/coding-odyssey/immutable-class-in-java-deep-dive-2aa2d80bf92c)

---

## 608. How is the string immutable?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Java, a `String` is immutable, meaning once a `String` object is created, its state (the sequence of characters it holds) cannot be changed.

This immutability is a key characteristic of the `String` class and is achieved through several design decisions in Java.

---

## 609. What is Spring Boot? Explain some annotations.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Spring Boot is a framework that simplifies the process of setting up, developing, and deploying Spring-based applications.

It is built on top of the Spring Framework and offers a set of conventions, auto-configuration options, and embedded servers that eliminate the need for much of the boilerplate code that comes with traditional Spring development.

Spring Boot makes it easier to develop stand-alone, production-ready applications that you can “just run” with minimal configuration.

Key features of **Spring Boot** include:

- **Auto-configuration**: Spring Boot can automatically configure many of the components in your application based on the libraries present in the classpath.
- **Standalone**: It eliminates the need for a web.xml or complex configuration setup and runs applications as stand-alone Java applications with an embedded server (e.g., Tomcat, Jetty).
- **Production-ready**: Spring Boot provides out-of-the-box support for features like health checks, metrics, and application monitoring.

---

## 610. What are Microservices?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Microservices is an architectural style that structures an application as a collection of small, independent services, each focused on a specific business function.

These services can be developed, deployed, and scaled independently, communicating through lightweight protocols like HTTP or messaging systems.

---

## 611. How is authentication done in your microservices project?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In a microservices architecture, authentication is often handled centrally to ensure that the authentication process is consistent across services. There are several approaches to achieving this, but the most common methods are:

---

## 612. In how many ways autowiring can be done?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Spring, **autowiring** is a mechanism that allows Spring to automatically inject dependencies into a bean without needing to explicitly define them in the configuration.

There are **four types of autowiring** that can be done in Spring:

---

## 613. In how many ways dependency injection be done?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Spring, **Dependency Injection (DI)** is a fundamental concept where an object’s dependencies are provided rather than the object creating them itself.

There are three main ways to perform dependency injection in Spring:

---

## 614. How to handle multiple beans at the same time in Spring Boot?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Spring Boot provides several mechanisms to handle multiple beans of the same type:

---

## 615. How do we create custom annotations in Spring Boot? Explain with an example.

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Here’s how you can create and use custom annotations in Spring Boot:

---

## 616. Define the Annotation

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 617. Implement the Annotation’s Behavior Using AOP

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 618. What is caching in Spring Boot?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 619. How inter service communication occurs in microservices?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 620. How can we customize specific auto configuration in spring boot?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

We can customize the defaults configurations using the following approaches:

---

## 621. What are the different scopes present in Spring Boot?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

> This question was asked in TCS Interview (Question 7) as well. So, this is an important question.
> 

In Spring, **bean scopes** determine the lifecycle and visibility of beans in the Spring container.

Below are the main **bean scopes** available in Spring:

---

## 622. How can we create a custom scope?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

We can create custom scopes for managing beans or dependencies like in the below example:

---

## 623. Define a Custom Scope Annotation

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 624. Implement the Custom Scope

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 625. What is the Saga design pattern?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 626. What is idempotency in microservices?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Idempotency in microservices refers to the property of an operation where performing it multiple times produces the same result as performing it once.

In other words, if a client sends the same request repeatedly — intentionally or due to retries — the state of the system remains consistent, and there are no unintended side effects.

**For example:**

- **GET** requests are naturally idempotent because retrieving the same resource multiple times doesn’t change its state.
- **PUT** requests can be idempotent if they always overwrite a resource with the same data, ensuring the state doesn’t change further with repeated requests.
- **POST** requests are typically not idempotent because they create new resources with every request unless explicitly designed to be so (e.g., by using unique identifiers).

Idempotency is crucial in distributed systems and microservices to handle failures, retries, and duplicate requests gracefully. It ensures consistency and reliability, even in the presence of network issues or system crashes.

---

## 627. What is the super class of all Java classes? What are some of the methods in it?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 628. Suppose you only have a class A. How can you prove that it follows OOPS principles?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 629. What collection would you use to remove duplicates from list and maintain insertion order?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 630. What is a volatile keyword in Java?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

The `volatile` keyword in Java ensures that a variable's value is always directly read from and written to the main memory, guaranteeing visibility across threads.

It prevents threads from caching the value, ensuring they see the most recent updates made by other threads.

- **Visibility Guarantee:** Ensures that updates to a `volatile` variable are immediately visible to all threads.
- **No Atomicity Guarantee:** It does not make operations like `count++` atomic. For atomic operations, synchronization is needed.

**Example:**

```
private volatile boolean flag = false;
```

Use `volatile` for variables shared between threads where visibility of changes is critical.

---

## 631. What is a transient keyword in Java?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

**20. What are the differences between == and .equals() method?***This question was asked in [Wipro Interview (Question 11)](https://archive.ph/o/pN9yq/https://medium.com/coding-odyssey/wipro-java-developer-interview-acdcc666e553) as well. So, this is an important question.*

---

## 632. What is an index and how do you create an index in SQL?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

An **index** in SQL is a database object that improves the speed of data retrieval operations on a table at the cost of additional space and maintenance time.

It helps to quickly locate and access data without having to search every row in the table.

---

## 633. How indexing works internally?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Internally, indexes in SQL are typically implemented using **B-trees (Balanced Trees)** or **Hash Tables**, depending on the type of index. Here’s how indexing works in general:

---

## 634. What are variable length arguments in Java?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Variable-length arguments (**varargs**) allow you to pass a variable number of arguments to a method. Use `...` after the data type in the method signature.

---

## 635. Can we replace arguments in main method with variable length arguments?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Yes, we can replace the arguments in the `main` method with variable-length arguments in Java.

The `main` method signature:

```
public static void main(String[] args)
```

can be replaced with:

```
public static void main(String... args)
```

---

## 636. There are two variables: int i = 9 and int i = 09, is there a difference between the two? Is int i = 09 a valid statement?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Java, there is a difference between `int i = 9;` and `int i = 09;`.

---

## 637. What is a Base class?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

A **base class** (also known as a **superclass** or **parent class**) in object-oriented programming is a class that provides common functionality or attributes that can be inherited by other classes (called **derived classes** or **subclasses**).

The base class acts as the foundation for creating more specialized classes.

---

## 638. What is rehashing?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Rehashing is the process of resizing a `HashMap` and redistributing its entries when the load factor threshold is exceeded.

The default load factor is 0.75, and the initial capacity is 16. This helps maintain efficient retrieval and insertion operations.

- **When:** Rehashing occurs when the number of elements exceeds `capacity × load factor`.
- **What happens:** The capacity is doubled, and all elements are rehashed into the new bucket array.
- **Time Complexity:** The rehashing process takes **O(n)** for resizing, but ensures average **O(1)** complexity for subsequent operations.

---

## 639. What are the criteria for Hashmap keys?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Java, `HashMap` keys must satisfy below criteria to function correctly. These criteria ensure the keys are handled efficiently during storage and retrieval.

---

## 640. What is fail-fast and fail-safe in collections?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Java, the behavior of iterators when a collection is structurally modified during iteration is categorized into **fail-fast** and **fail-safe**.

---

## 641. You have a string builder as a hashmap key, now you appended the string builder. What will be value of the string builder with the get object?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

If you use a `StringBuilder` as a `HashMap` key and modify (append) the `StringBuilder` after adding it to the map, you may not be able to retrieve the value associated with that key. This is because the `hashCode` of `StringBuilder` depends on its current state, and modifying it changes the `hashCode`.

---

## 642. There are two variables, storing exchange rates of currency. Now, what data type will you use for these variables and which method will you use to equate them?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

When dealing with exchange rates of currencies, it’s essential to ensure precision due to the potential for financial inaccuracies caused by floating-point arithmetic.

---

## 643. What is Marker interface in Java? Can we create a custom Marker interface?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

- A **marker interface** is an interface with no methods or fields (essentially empty).
- It is used to indicate or “mark” a class for a specific capability, behavior, or property.

---

## 644. Custom Marker Interface?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Yes, you can create your own marker interface. It can be used to signal a specific behavior or functionality in your application.

---

## 645. What is a Circuit breaker pattern?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

> This is a very important question that came up in both my first and second rounds at Capgemini.
> 

In a microservices architecture, a **Circuit Breaker** is a design pattern used to detect failures in a system and prevent them from propagating to other parts of the system. It helps in improving the system’s resilience by allowing the system to recover from failures gracefully. The main goal is to prevent a system from repeatedly making calls to a service that is failing and causing additional load or cascading failures.

---

## 646. How do you do fault isolation?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Fault isolation is the process of identifying, diagnosing, and containing errors or faults in a system to prevent them from affecting other parts of the system.

It ensures that failures are handled gracefully and do not propagate or impact other services or components.

Here’s how fault isolation can be achieved:

---

## 647. What is an Immutable class and How to create an Immutable class in Java?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 648. Is there any collection in Java that supports key-value pairs and keeps the keys in sorted order?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

Yes, in Java, we have the **TreeMap** that supports key-value pairs and ensures that the keys are always sorted.

It uses a **red-black tree** under the hood, which ensures that the keys are sorted in their **natural order** (if the key class implements `Comparable`) or according to a **custom comparator** that you can provide during the TreeMap's creation.

Key operations like `put()`, `get()`, and `remove()` have a time complexity of **O(log n)** because of the red-black tree structure.

Additionally, TreeMap offers methods like `firstKey()`, `lastKey()`, `higherKey()`, and `lowerKey()` to efficiently navigate through the sorted keys.

---

## 649. What happens when you try to insert the above discussed employee object in Treemap?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 650. What are the bean scopes available in Spring?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

In Spring, **bean scopes** determine the lifecycle and visibility of beans in the Spring container.

Below are the main **bean scopes** available in Spring:

---

## 651. What is lazy loading?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

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

---

## 652. What is cascading?

*Source: [`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*

**Cascading** refers to the automatic propagation of certain operations (like persist, delete, or update) from one entity to its related entities.

This means that when an operation is performed on a parent entity, it can automatically affect the child entities that are associated with it, depending on the cascade configuration.

When dealing with relationships between entities, you may have operations like saving, updating, or deleting an entity. By configuring **cascading**, you can specify that these operations should automatically be performed on related entities as well.

For example, if you have a `Parent` entity and a `Child` entity, and you delete the `Parent`, you might want to automatically delete all the associated `Child` entities as well. Cascading lets you do this without explicitly deleting each child entity.

---

## 653. What is an Interface?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 654. What is an Abstract Class?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 655. Usecase of Abstract Class?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

- Use an abstract class when classes share common behavior and fields, but you also want to enforce certain methods to be implemented by subclasses.
- If you need multiple inheritance, interfaces are a better choice since Java doesn’t support multiple inheritance with classes.

---

## 656. Explain Exception Handling in Java.

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 657. What is a Finally Block?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

The **`finally` block** is a special block of code in Java associated with exception handling. The finally block always executes when the try block exits.

It is used to execute crucial cleanup code, such as releasing resources, closing files, or clearing buffers, irrespective of whether an exception is thrown or not.

---

## 658. What Happens if the finally Block Contains return?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 659. What are Collections in Java?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

In Java, **Collections** refer to a framework that provides a unified architecture for storing and manipulating a group of objects.

It includes a set of interfaces, classes, and algorithms to manage data efficiently.

Collections are an essential part of Java, allowing developers to manage data like lists, sets, maps, and queues with built-in methods for operations like adding, removing, sorting, and searching.

---

## 660. What is the default server port in Spring Boot?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

In Spring Boot, the default server port is **8080**.

When you run a Spring Boot application, by default, it starts an embedded web server (like Tomcat) and listens on port **8080**.

You can change this default port by modifying the `application.properties` or `application.yml` configuration file in your project.

---

## 661. What is a comparable interface? Explain the difference between comparable vs comparator.

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 662. How are you managing exceptions in your Spring Boot project (Explanation of Global Exception Handling)?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

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

---

## 663. What is Deep Cloning? Difference between Shallow Cloning and Deep Cloning.

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

Deep cloning is when an object and all the objects it refers to are cloned. This means that not only the object itself is copied, but also all the nested objects (or objects referenced by the original object).

In deep cloning, the new object has its own copies of the nested objects, and changes to the cloned object or any of its nested objects won’t affect the original object.

---

## 664. Mention some of the Java 8 features. Don’t explain.

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

Below are some of the important Java 8 features:

1. **Lambda Expressions**: Introduced functional programming with concise syntax.
2. **Functional Interfaces**: Interfaces with a single abstract method, like `Predicate`, `Function`, and `Consumer`.
3. **Streams API**: Enables functional-style operations on collections with methods like `filter()`, `map()`, and `collect()`.
4. **Default and Static Methods**: Allows interfaces to have method implementations.
5. **Optional Class**: Helps handle null values and avoid `NullPointerException`.
6. **Date and Time API**: Introduces modern date-time handling with `LocalDate`, `LocalTime`, and more.
7. **Method References**: Simplifies lambdas by directly referencing methods (e.g., `ClassName::methodName`).
8. **Collectors Utility**: Provides utilities to transform and group data in streams.

---

## 665. What is a Consumer?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

A **Consumer** is a functional interface introduced in Java 8 as part of the `java.util.function` package. It represents an operation that accepts a single input argument and performs an action on it but does not return any result.

---

## 666. How to create a Thread in Java. Explain the thread life cycle.

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

There are two primary ways to create a thread in Java:

---

## 667. What is a deadlock and how to avoid it?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

A **deadlock** occurs in a multi-threaded environment when two or more threads are blocked forever, waiting for each other to release resources. It usually happens when multiple threads hold some resources and attempt to acquire resources held by others, creating a circular dependency.

---

## 668. What are S.O.L.I.D principles in Java?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

The S.O.L.I.D principles are a set of five design principles that promote good software design, improve maintainability, and make the code more robust and flexible.

These principles form the foundation of **object-oriented programming** and are widely used in Java.

---

## 669. How do you decide if you have to choose a Set or List?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

**Choose Set when:**

- You need to ensure uniqueness.
- Performance for lookups is critical.

**Choose List when:**

- You need to maintain order.
- You require duplicates.
- You need to access elements by index.

---

## 670. How do you monitor health of your Spring Boot application?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

To monitor the health of a Spring Boot application, I would use **Spring Boot Actuator**, which provides production-ready features like health checks, metrics, and other useful endpoints.

---

## 671. When to use application.properties file vs application.yaml file?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

Both `application.properties` and `application.yaml` are configuration files used in Spring Boot to configure the application’s properties. They serve the same purpose, but the format and the way they’re structured differ.

- **`application.properties`**: A traditional, simple key-value pair format.
- **`application.yaml` (or `application.yml`)**: A hierarchical data format, typically used for more complex configurations, where readability and structured data are important.

---

## 672. What is an API gateway?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

An **API Gateway** is a server that acts as an entry point for client requests to access various services in a microservices architecture.

It functions as a reverse proxy, routing client requests to the appropriate microservices, aggregating the results, and providing a unified response. API Gateways help centralize common functionality like authentication, load balancing, rate limiting, and logging, reducing the complexity of managing multiple services directly.

---

## 673. What is a stored procedure?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

A **stored procedure** is a precompiled collection of one or more SQL statements that are stored in a database.

Stored procedures can be executed by the database engine to perform specific tasks such as querying, inserting, updating, or deleting data.

These procedures are written in SQL (or a procedural extension of SQL like PL/SQL in Oracle or T-SQL in SQL Server), and they are stored directly in the database for repeated use.

---

## 674. What is a trigger?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

A **trigger** is a special type of stored procedure in a database that automatically executes in response to certain events, such as an `INSERT`, `UPDATE`, or `DELETE` operation on a table or view.

Below are some of it’s key points:

---

## 675. Can we have more than one primary key in a table?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

No, a table can have **only one primary key**.

The primary key in a table is a unique identifier for each record. While a table can have multiple **unique keys** or **unique constraints**, there can only be **one primary key**. The primary key enforces both **uniqueness** and **not null** constraints on the column(s) it is defined on.

However, a primary key can consist of **multiple columns** — this is called a **composite primary key**. But even in this case, there is still only one primary key for the table, which involves multiple columns.

---

## 676. What is the purpose of JOIN and UNION?

*Source: [`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

JOIN and UNION are both used to combine data from multiple tables in SQL, but they serve different purposes and work in distinct ways.

---

## Question bank (no recorded answers)

Prompts collected from the notes that have no written answer yet:

- Difference between RSocket vs HTTP/2? — *[`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*
- The waiter comes back and says, “Sorry, the item is out of stock”? — *[`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*
- Or “Please wait, the chef is still preparing your dish”? — *[`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*
- Or worse, “Kitchen’s on fire — no food today”? — *[`03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md`](../03-medium-series/deep-dive/medium-interview-company-questions-deep-dive-serie.md)*
- List<?>: Useful for read-only methods that accept any list type. — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What are generics and why are they useful? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What is type erasure? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What is the difference between <? extends T> and <? super T>? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- Can you use primitive types with generics? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- How do bounded type parameters improve type safety? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What’s the difference between List<Object> and List<?>? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- Why can’t we create a generic array in Java (e.g., T[] array = new T[10];)? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What is PECS in Generics? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- What Is Type Inference? — *[`03-medium-series/other-part-1/medium-interview-questions-part-1.md`](../03-medium-series/other-part-1/medium-interview-questions-part-1.md)*
- Q3 — How does Garbage Collection prevent a Java application from going out of memory? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Q4 — Is Java “pass-by-reference” or “pass-by-value”? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Q7 — Is it possible to override or overload a static method in Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Q8 — What’s the most reliable way to test whether two double values are equal? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Q9 — Will the finally block be executed if the try or catch block executes a return statement? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between Spring MVC and Spring WebFlux? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between primitive and non-primitive data types? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between compile-time and run-time polymorphism? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between an abstract class and an interface in Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between throw and throws? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between checked and unchecked exceptions? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between Iterator and ListIterator? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between Comparable and Comparator? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between compile-time and runtime errors? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are JDK, JRE, and JVM? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain Abstraction and Encapsulation? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Inheritance, Aggregation, and Association? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a try-with resource in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain different Java 8 features? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain the JVM memory model? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain Garbage Collection? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are exceptions and what is exception handling? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain Autoboxing and Unboxing? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Typecasting? Explain with Parent-Child inheritance example. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why is the Java platform independent? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How many ways can we create objects in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Collections framework? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain static, this, and super keyword? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain finally, finalize and final keyword? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Serialization? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain the Internal working of a HashMap? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Concurrent HashMap? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the default size of ArrayList and HashMap? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Marker Interfaces and Functional Interfaces? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain Classloading in java and types of classloaders? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How can we create a custom Exception? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Covariant return type? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Threading? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Daemon threads? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between start() and run() ? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Volatile keyword? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between Synchronized method and block? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between sleep(), wait () , yeild() ? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you mean by Deadlock? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain Join()? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are ThreadLocal and Threadpool? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the immutable class? How can you make a class immutable? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Singleton? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between classNotFound and NoClassDefinitionFound? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Consumer, Predicate, Supplier? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between map() and flatMap() ? (answer) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How are you financed? (especially important for startups) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you like about working here? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How can I best prepare for this role before starting? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Could you describe a typical work week? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How big are teams? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What would my immediate responsibilities be? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Will there be opportunities to choose, what projects I work on? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What does the career path look like for this role? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does your company promote personal growth? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Do you feel there are any skills currently lacking on the team? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the biggest change the company has gone through in the last year? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What’s the style of leadership? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the rhythm of work here? Is there a particular time of year, when it’s all hands on deck and we’re pulling long hours, or is it fairly consistent throughout the year? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What type of background and experience are you looking for in this position? What would your ideal candidate be like? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Is there anything that stands out to you that makes you think I might not be the right fit for this position? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the timeline for making a decision on this position? When should I get back in touch with you? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between static and non-static methods, variables And explain their memory architecture as well? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you understand by using of final keyword with classes and variables as well, give the case where you will prefer to use the final keyword? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is typecasting? Suppose there is a data which is of type double then how can you show that double in int data type? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the main advantages of polymorphism? And what is the alternate of polymorphism? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is constructor chaining in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Explain constructor with the help of inheritance? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- ‘Super’ keyword is used to access superclass properties, but what when you are not allowed to use super then how can you access the property of superclass, if yes then how? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Suppose you have 11th, 12th class books in your beg, now how will you use inheritance to show the relationship between them? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why java compiler needs main method static only? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you understand by anonymous word? And what is the impact of anonymous array and object in java? Explain memory structure with or without anonymous? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why java requires inner class? What do you understand by static inner classes in java? And where will you use a static and non-static class? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- An abstraction is hiding information in java, how java showing abstraction and write a program where you have to show abstraction and do the same program without abstraction? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are different ways to create an object in java? And what do you understand by object creation in java? Where the memory will be allocated when the object is created in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- JVM is compiler in java to run your program, explain steps from writing your code to execute on the machine? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is heap memory allocation in java? Explain the difference between stack and heap memory allocation in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How JVM knows about your program and what is the cycle of code execution in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between public, private and protected modifiers and explain why do you need all these modifiers in your code? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What will be the result If java set the main method to private? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is command line argument and how can you give order to java program to execute a file reading operation by command line argument? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Where do you need super constructor and suppose you don’t have super constructor then is there any way to execute superclass constructor, if yes then explain? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- The interface is about 100% abstraction, what do you understand by 100% abstraction and how can you achieve 100% abstraction in java? Write the same program from both interface and abstract class, now as you can write the same code with abstract class then why do you need an interface in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is multilevel inheritance in java? And does java support multiple inheritances, explain your thoughts? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Java is object-oriented language, explain both object and oriented word? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you understand by design patterns in oops, if you have to design your own patterns then what are the parameters you will consider most? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Write some basic programs like: <1>. Palindrome,< 2>. String reverse, <3>. Patterns of stars in all possible ways, <4>.Find out minimum and maximum numbers in a given array, <5>. You are given city name and person name blank array of fixed-sized, write a program to get the city name of a person. You have to take city name and person name at run time, <6>. Write matrix multiplication program in java, <7>. How will you break an array in an equal part? Consider all possible cases, <8>. Write a program using switch case where you have to ask day name from the user and then you will print the first three letters of that day in the capital letter as a response to the user,<9>. Ask the user to give a string as input then show repeated letters with count as a response, <10>. Convert any given number into binary format, <11>. Read context from a file and replace every small letter into capital and every capital letter into the small letter and then print the modified file as the response of program,<12>. Write a program where the program will ask the user about name, age, address and college name, then you will print the detail in order but if user repeats the same name again then show available data of the user. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you understand by the break and continue keyword in an iteration? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Write all possible syntax of for loop? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between while and for loop? And explain the cases where which one suits better? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you understand by variable scope? Is it required to initialize the local variable explain why so? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is an interpreter in java? And the difference between compilation and interpretation in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you get by mean of return type in java? And suppose you have to return int data but return type of method is double, explain will it work or not? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Whether you can override superclass methods or variables? Explain it? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is object chaining in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between parameters and arguments in java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Write a singleton class in java? And where, why you will prefer singleton in any case? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Whether java is procedural language or functional language explain it? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the parameters that make java different from other language give some practical examples where java suits better than any other language? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why exception handling is introduced in java? List down all the causes behind this? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between try, catch and finally? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the volatile keyword in Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is synchronization in Java and when do we use it? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is serialization and why is it used? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- If a Student object has normal, static, and transient fields — which ones get serialized? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is serialVersionUID and why is it important in serialization? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What kind of keys and values does a HashMap accept? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why use Map.Entry when we can directly iterate over the Map? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we use both primitive and object types as keys or values in a Map? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a Set in Java and how is it different from a List? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the two types of stream operations in Java 8? (Hint: Intermediate & Terminal) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is flatMap in Java Streams and how is it different from map? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you used map() and flatMap() in your real project? Share an example. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can you explain how your frequency map logic works under the hood? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are stereotype annotations in Spring Boot? (@Component, @Service, @Controller, etc.) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens if we put @Service on a controller class and @Controller on a service? Will the server start? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- If annotations are swapped incorrectly, will Postman requests still work? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How can we access a property defined in application.properties inside a class? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens if we use @Value but forget to define the key in the properties file? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What if both key and value are missing from application.properties? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we provide a default value using @Value? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens if the property is missing? Will the app crash or use default? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the @Primary annotation in Spring? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is tight coupling in Java? (e.g., “I always want a Car object, no matter what.”) — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What does @Autowired do, and how does it work behind the scenes? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens if we create an object using new even though we’ve used @Autowired? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- If we manually instantiate the same object in 10 classes using new, what are we losing? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the concepts related to Object Oriented Programming? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How many ways can an object be created in Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How many objects will be created using a string literal? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why does Java have two ways of creating strings (literal vs new keyword)? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What makes a class mutable or immutable? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you heard about Marker Interfaces? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What’s the difference between throw and throws? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we use only a try block without catch or finally? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we have multiple catch blocks? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the purpose of the finally block? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What’s the difference between abstract class and interface? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- When should we use an interface and when should we use an abstract class? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the main interfaces/classes in the Collection framework? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the contract of equals() and hashCode()? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Internal working of HashMap? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- On what basis does HashMap decide where to store an element? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Is hashing based on key, value, or both? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- If we insert the same key in HashMap, what happens to the previous value? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What’s the difference between Comparable and Comparator? When to use each? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Fail-Fast and Fail-Safe iterators? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why does Fail-Safe not throw exceptions? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to make an ArrayList read-only? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What’s the difference between Collection and Stream? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- If Stream modifies the data using filter/map, isn’t that a modification? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the new features in Java 8? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are intermediate and terminal operations in streams? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you used filter() and map()? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to declare a list of integers in Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to reverse a list using Java 8 Stream API? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to sort a list using Java 8? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Do we have an intermediate method in Java 8 to sort a list? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to find even numbers from a list? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to square elements in a list and filter those greater than 25? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the SOLID principles? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Factory Design Pattern? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Singleton? How to break Singleton? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to create a thread using Thread and Runnable? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Which method is overridden in Runnable? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens when a thread is started? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is event-driven architecture? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Producer-Consumer problem? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you worked with Kafka or RabbitMQ? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the use of API Gateway? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is message-driven architecture? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What do you mean by normalization? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between TRUNCATE, DROP, and DELETE? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What does @EnableJpaRepositories do in Spring Boot? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you worked with any profilers? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Is a profiler a tool or a code snippet? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you used any performance/load testing tools like JMeter? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens in Jenkins when image creation is triggered? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you check logs in UAT/Release environment using tools like Dynatrace? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does a Spring Boot application start? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What annotations are used in the Spring Boot main class? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you used GraphQL or Spring Security? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Have you implemented JWT or OAuth2? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the features of Java?Object-oriented, platform-independent, secure, robust, multithreaded, and architecture-neutral. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between JDK, JRE, and JVM?JDK = development tools + JRE, JRE = JVM + libraries, JVM = executes bytecode. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why is Java platform-independent?Bytecode runs on any platform with JVM. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between == and .equals()?== checks reference, .equals() checks content. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is autoboxing and unboxing?Automatic conversion between primitives and wrapper classes. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How is memory managed in Java?Through stack, heap, and garbage collection. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the role of the main method in Java?Entry point of any standalone Java application. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a constructor? How is it different from a method?Initializes objects; no return type and same name as class. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we overload constructors?Yes, by using different parameters. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between break, continue, and return?break exits loop, continue skips iteration, return exits method. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are enhanced for-loops?A simpler syntax for iterating over collections or arrays. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between primitive and wrapper classes?Primitive is basic type; wrapper wraps it into an object. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are static variables and methods?Belong to the class, not to instances. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between String, StringBuilder, and StringBuffer?String is immutable, StringBuilder is mutable and fast, StringBuffer is thread-safe. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Why are Strings immutable in Java?For security, thread-safety, and caching. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does String interning work?Stores unique string literals in a pool for reuse. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between Array and ArrayList?Array has fixed size; ArrayList is resizable. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are generics in Java?Enable type safety and reusability. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- When to use HashMap vs TreeMap vs LinkedHashMap?HashMap for fast access, TreeMap for sorted keys, LinkedHashMap for insertion order. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between fail-fast and fail-safe iterators?Fail-fast throws ConcurrentModificationException, fail-safe doesn’t. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is method overloading and overriding?Overloading = same method name, different params; overriding = subclass version of superclass method. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is runtime polymorphism?Method overriding resolved at runtime. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the super keyword?Refers to parent class methods/constructors. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between this and super?this refers to current class, super to parent class. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is an abstract class vs interface?Abstract class can have state; interfaces are contracts. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can we have default methods in interfaces? Why?Yes, to provide backward-compatible enhancements. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the diamond problem and how does Java solve it?Ambiguity in multiple inheritance; solved via interfaces and default methods. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between checked and unchecked exceptions?Checked = compile-time, Unchecked = runtime. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is finally block? When is it not executed?Executes always, except when JVM exits or System.exit() is called. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can a try block exist without a catch?Yes, if finally block is present. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does throw and throws work?throw is for actual exception, throws declares potential exceptions. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a thread in Java?A lightweight process for multitasking. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between Runnable and Thread?Runnable decouples task from thread; Thread is more heavyweight. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are thread states?New, Runnable, Running, Blocked, Waiting, Timed Waiting, Terminated. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a thread-safe class? Is HashMap thread-safe?Safe for use by multiple threads; HashMap is not. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does synchronized work?Locks an object/method to ensure mutual exclusion. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is volatile keyword?Ensures visibility of changes across threads. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between wait() and sleep()?wait() releases lock; sleep() doesn't. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is thread starvation and deadlock?Starvation: thread waits indefinitely; Deadlock: two threads wait on each other. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Callable and Future?Callable returns a value; Future holds result. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the use of ExecutorService?Manages thread pools and asynchronous task execution. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is ForkJoinPool and when to use it?For parallel processing using divide-and-conquer. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is ReentrantLock and how is it better than synchronized?More flexible locking with try-lock and fairness options. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are atomic variables?Variables like AtomicInteger support lock-free thread-safe operations. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a functional interface?Interface with a single abstract method. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the @FunctionalInterface annotation?Marks interface as functional for compiler validation. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are method references?Shorthand for calling existing methods. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Java Streams?API for processing data in a functional style. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between map() and flatMap()?map() transforms, flatMap() flattens nested streams. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is lazy evaluation in Streams?Execution deferred until terminal operation is called. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a terminal operation?Operation that triggers Stream processing (e.g., collect, forEach). — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Optional in Java?A container to avoid null checks. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to avoid NullPointerException using Optional?Use ifPresent, orElse, map. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between old Date API and java.time API?New API is immutable and thread-safe. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are the different memory areas allocated by JVM?Heap, stack, method area, code cache, metaspace. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does garbage collection work in Java?Automatically removes unreachable objects. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are strong, weak, soft, and phantom references?Reference types that affect GC behavior differently. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a memory leak in Java?When unused objects are unintentionally retained. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you analyze and fix OutOfMemoryError?Heap dump analysis and optimizing memory usage. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Java profilers?Tools like JVisualVM, YourKit to monitor performance. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is a Singleton Pattern? How to implement it?One instance per JVM; use private constructor + static instance >>> private constructor and a thread-safe, lazy-loaded static accessor >>> Use ENUM for more robustness — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Builder Pattern?Constructs complex objects step-by-step. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Observer Pattern?One-to-many dependency for event notification. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between Strategy and State pattern?Strategy = interchangeable behaviors; State = internal state changes. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Java Reflection API?Inspect or modify classes/methods/fields at runtime. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Annotation? How are custom annotations created?Metadata for code; use @interface. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How does Serialization work in Java?Converts object to byte stream. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the transient keyword?Prevents serialization of fields. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are best practices for exception handling?Use specific exceptions, never swallow, log properly. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to prevent memory leaks in Java applications?Avoid static references, use WeakReference, close resources. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you secure a Java application? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to write immutable classes? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Just-In-Time (JIT) Compiler?Improves performance by compiling bytecode to native code. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are JVM tuning parameters?Flags to optimize memory and GC (Xmx, XX:+UseG1GC, etc.). — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to analyze GC logs?Use tools like GCViewer to detect frequency, pause time. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the Java Platform Module System (JPMS)?Modularizes JDK and large apps since Java 9. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between modular and non-modular applications?Modular uses module-info.java, non-modular doesn’t. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Records in Java?Immutable data carriers with concise syntax. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can Records implement interfaces? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are Sealed Classes?Restrict which classes can extend them. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do they help in type safety?Enforce control over class hierarchy. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What are virtual threads in Java?Lightweight threads introduced in Java 21. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Difference between platform and virtual threads?Virtual threads use less memory and context-switch overhead. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What problems do virtual threads solve?Scalability in high-concurrency apps. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you handle concurrency in microservices using Java? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you implement caching in Java?Use libraries like Caffeine, Ehcache, or Redis. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is circuit breaker pattern and how is it used in Java?Prevents cascading failures; use Resilience4j or Hystrix. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you use Java with Kafka or RabbitMQ?Through official client libraries for pub/sub and messaging. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you implement idempotency in Java APIs?Use unique request IDs or tokens and database checks. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is the difference between Unit and Integration testing?Unit tests individual components; Integration tests system parts together. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is Mockito? How to mock dependencies?A mocking framework to simulate dependencies. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How to write parameterized tests in JUnit?Use @ParameterizedTest with @ValueSource or @CsvSource. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What is test coverage and how do you measure it?% of code exercised by tests; use Jacoco or Cobertura(legacy, not updated from long time), Codecov. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- What happens when System.gc() is called? — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- Can you write a thread-safe singleton?Yes, using enum or synchronized block. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you design a rate limiter in Java?Use token bucket or leaky bucket algorithms. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How do you handle 10M+ records in Java efficiently?Use batching, streaming, and paging. — *[`03-medium-series/other-part-2/medium-interview-questions-part-2.md`](../03-medium-series/other-part-2/medium-interview-questions-part-2.md)*
- How would you use the Stream API to filter out all even numbers from a list of integers? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you sort a stream of objects based on a specific attribute? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What is Spring Bean LifeCycle? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What's the main difference between HashTable and Hashmap? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Difference between Callable and Runnable? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Difference Primary key and Unique key? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Difference Prepared Statement and Statement? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How does Garbage Collection work in Java? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are WeakReference and SoftReference in Java? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Explain the differences between ArrayList and LinkedList. When to use which? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are the key differences between Monolithic and Microservices Architecture? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How does Spring Boot make application development easier? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What is Circuit Breaker Pattern? How is it implemented using Resilience4j? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How does Spring Cloud handle service discovery? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you secure REST APIs in Spring Boot? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Can you walk me through a complex project you worked on? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you handle production issues in a microservices system? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are the biggest performance challenges you’ve faced? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Have you worked with DevOps tools (Docker, Kubernetes, Jenkins)? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you ensure high availability in microservices? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are your strengths and weaknesses? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you handle tight deadlines and pressure? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Where do you see yourself in 5 years? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How does Spring Boot handle dependency injection? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How would you debug memory leaks in a Java application? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What strategies can be used to optimize API response times? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are the database optimization techniques? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you mentor junior developers? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you manage conflicts within a development team? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What is your approach to conducting code reviews? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What’s the expected traffic/load? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Is it a global product or regional? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What are the latency and availability expectations? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- Are there specific compliance or data residency requirements? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How will you handle database scaling? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What caching strategies will you use? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How will you ensure fault tolerance? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How do you manage consistency vs. availability? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What happens if Kafka goes down? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How will you know if the system is down? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What metrics will you track? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- How will you troubleshoot latency issues? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- “How does Spring Dependency Injection work internally?” — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- “What’s the difference between HashMap and ConcurrentHashMap?” — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What problem were you solving? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What architecture did you choose and why? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What challenges did you face and how did you resolve them? — *[`03-medium-series/part-1/medium-interview-company-questions-part-1.md`](../03-medium-series/part-1/medium-interview-company-questions-part-1.md)*
- What is the Hierarchy of exception? — *[`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*
- What is a REST API, and how does it differ from SOAP?(SOAP vs REST)? — *[`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*
- What is the difference between 2NF and 3NF in database normalization? — *[`03-medium-series/part-2/medium-interview-company-questions-part-2.md`](../03-medium-series/part-2/medium-interview-company-questions-part-2.md)*
- What are the differences between Abstract class vs Interface. Also, Explain when to use what? — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- Design a microservice to handle uploading large files (e.g., 100MB+) with high concurrency. — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- If 3 out of 5 calls fail, what happens? — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- How can you implement per-user rate limiting in a distributed microservices environment? — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- How do you implement rollback in a Saga pattern using orchestration? — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- Design an algorithm to serialize and deserialize a binary tree. You must ensure that the tree can be reconstructed exactly from the serialized string. — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- Implement a regular expression matching with support for '.' and ''. — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- When to use LinkedList over an ArrayList? — *[`03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md`](../03-medium-series/part-3/medium-interview-company-questions-part-3-by-shiva.md)*
- How have you implemented the Authorization? — *[`03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md`](../03-medium-series/part-4/medium-interview-company-questions-part-4-by-shiva.md)*
- Write a query to find duplicate records in a table. — *[`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*
- Write a query to find top 5 employees details having salary greater than average salary of all employees in the company. — *[`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*
- How String and StringBuffer handle memory differently? — *[`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*
- What are the differences between REST vs SOAP? When to choose one over another? — *[`03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md`](../03-medium-series/part-5/medium-interview-company-questions-part-5-by-shiva.md)*
- What are the use cases of Array list and Linked list? — *[`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*
- Can String or String builder or primitive integer or wrapper class be a hashmap key? — *[`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*
- How long does Heap memory and Stack Memory stay in Java? — *[`03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md`](../03-medium-series/part-6/medium-interview-company-questions-part-6-by-shiva.md)*
- When to use Interface vs Abstract class? — *[`03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md`](../03-medium-series/part-7/medium-interview-company-questions-part-7-by-shiva.md)*

