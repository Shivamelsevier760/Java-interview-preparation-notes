# Medium interview company questions Deep Dive Series 1 by Shivam Srivastava

# **HTTP Status Codes: Deep Dive with Interview Questions**

**I**magine you’re in a restaurant. You place an order, the waiter nods, and in a few minutes, he returns with your food.

Great. That’s how things should work.

But what if:

- The waiter comes back and says, “Sorry, the item is out of stock”?
- Or “Please wait, the chef is still preparing your dish”?
- Or worse, “Kitchen’s on fire — no food today”?

That’s *exactly* what HTTP status codes are — messages from the server (waiter) telling the client (you) what happened to your request.

Whether you’re building an API or just browsing the internet, **HTTP status codes** play a vital role in communication between client and server.

They help browsers, APIs, mobile apps, and even you — the developer — understand what’s happening behind the scenes.

Let’s dive in.

# **Basics:**

HTTP status codes are 3-digit responses issued by a server to indicate the result of a client’s request.

They follow this format:

```
HTTP/1.1 200 OK
```

- `HTTP/1.1` → Protocol version
- `200` → Status code
- `OK` → Status message

Think of these codes as the **tone of response**:

- “Everything’s fine”
- “You’re asking for something weird”
- “Oops, something broke”
- “Go away, you’re asking too much”

# **Classification:**

All status codes fall into five categories, based on the first digit:

## **1xx — Informational Responses**

These are rarely seen in REST APIs, but they’re important in HTTP communication.

- **100 Continue**: Client can continue with the request.
- **101 Switching Protocols**: Server is switching protocols (e.g., from HTTP to WebSocket).
- Browsers usually hide 1xx codes from users.

## **2xx — Success**

The client did everything right. The server did its job. Everyone’s happy.

- **200 OK**: The request was successful.
- **201 Created**: Resource was successfully created.
- **204 No Content**: Request was successful but there’s no content to return.
- **206 Partial Content** — Returned when using range requests (download resumes, video streaming).
- ***Tip: Use 201 when creating resources in APIs to clearly indicate success.***

## **3xx — Redirection**

The resource you requested isn’t here — but it might be somewhere else.

- **301 Moved Permanently** — The resource has moved. Update your links.
- **302 Found** — Temporarily moved.
- **304 Not Modified** — You already have the latest version. No need to re-download.
- Used extensively in caching, SEO, and browser redirects.

## **4xx — Client Errors**

These errors are your fault (as a client). The server is saying: *“What you asked doesn’t make sense.”*

- **400 Bad Request** — Malformed syntax, invalid JSON, or parameters.
- **401 Unauthorized** — You need to log in (but didn’t).
- **403 Forbidden** — You’re not allowed, even if you’re logged in.
- **404 Not Found** — The resource doesn’t exist.
- **409 Conflict** — Duplicate entries or version mismatches.
- **422 Unprocessable Entity** — Valid syntax, but semantically invalid (e.g., missing required fields). 422 is not part of core RFC 2616 (HTTP/1.1), but introduced in WebDAV extension
- **401 vs 403***: 401 means “You’re not authenticated.” 403 means “You’re authenticated, but not authorized.”*

## **5xx — Server Errors**

Now it’s the server’s fault. The client did everything right, but the server crashed, timed out, or misbehaved.

- **500 Internal Server Error** — Generic server failure.
- **502 Bad Gateway** — Invalid response from upstream service.
- **503 Service Unavailable** — Server is down or overloaded.
- **504 Gateway Timeout** — Server took too long to respond.
- ***503** is commonly used during deployments or maintenance windows.*

## **Status Code Use in REST APIs**

**Example 1: Creating a User**

```
POST /users
201 Created
Location: /users/123
```

**Example 2: Fetching a Deleted Item**

```
GET /products/99
404 Not Found
```

**Example 3: Sending Invalid Input**

```
POST /orders
400 Bad Request
{
  "error": "Missing field: quantity"
}
```

**Example 4: Rate Limiting**

```
429 Too Many Requests
Retry-After: 60
```

# **Custom Status Codes:**

HTTP does not officially support truly custom status codes (like `799`, `699`, etc.) because clients, proxies, and browsers are expected to recognize and interpret only the standard ones defined in the HTTP specification.

However, you can define custom error messages within the body of a response using standard status codes like `400`, `422`, `403`, etc., to convey application-specific errors.

**For example:**

```
{
  "status": 422,
  "error": "Validation Error",
  "message": "Email is invalid"
}
```

# **Best Practices**

- **Be precise**: Don’t return 200 OK for everything. Use 201, 204, 400, 404, etc., as appropriate.
- **Return meaningful messages** in the response body for 4xx and 5xx errors.
- **Don’t expose sensitive info** in error messages (especially 500 series).
- **Use 422 for validation errors**, instead of 400.
- **Log all 5xx errors server-side for debugging**.
- **For APIs, consider including `error_code` and `message` fields** in responses:

```
{
  "error_code": "USER_NOT_FOUND",
  "message": "No user exists with the given ID."
}
```

# **Advanced Usage:**

## **Redirection & Versioning (Microservices)**

In large applications or **microservices architectures**, resource locations may change over time, making **301 Moved Permanently** and **302 Found** particularly useful.

- **301 Moved Permanently**: Use for API version updates.

```
HTTP/1.1 301 Moved Permanently
Location: /api/v2/resource
```

- **302 Found**: Temporary redirection for maintenance. 302 can be problematic if misunderstood — it doesn’t always preserve method (GET/POST confusion).

## **Concurrency Conflict (409 Conflict)**

In distributed systems or microservices, race conditions and conflicts are common when multiple clients are interacting with the same resources. **409 Conflict** can be used to handle these scenarios.

Imagine two clients updating the same resource:

**Client 1: Updates a record at `/api/resource/123`**

```
PUT /api/resource/123
{
  "name": "New Name"
}
```

**Client 2: Simultaneously tries to update the same record**

```
PUT /api/resource/123
{
  "name": "Another Name"
}
```

- If Client 1’s update is successful first, Client 2 gets a 409 Conflict.

```
HTTP/1.1 409 Conflict
```

## **Optimizing with Caching (304 Not Modified)**

- **304 Not Modified** is a lightweight response that tells the client that the cached version of the resource is still valid, so it doesn’t need to download the entire content again.

```
HTTP/1.1 304 Not Modified
```

- Use ETags and Last-Modified headers in conjunction with 304 Not Modified to optimize caching. This reduces the load on the server and speeds up response times.

```
ETag: "12345" Last-Modified: Thu, 01 Jan 2025 00:00:00 GMT
```

> An “ETag” (Entity Tag) is a unique identifier for a specific version of a resource. It’s used to determine if a cached version of a resource is still valid. If the ETag returned by the server matches the one stored in the client’s cache, the server doesn’t need to send the full resource again, saving bandwidth and improving performance.
> 

## **Rate Limiting (429 Too Many Requests)**

- The **429 Too Many Requests** status code indicates that the user has sent too many requests in a given amount of time.
- Implement exponential backoff or token bucket algorithms to throttle requests in a fair and controlled manner.
- Additionally, use the `Retry-After` header to indicate when the client can try again.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 3600  # Retry after 1 hour
```

# **Interview Questions:**

## **1. When to use `422 Unprocessable Entity` instead of `400 Bad Request`?**

**When to use:**

![](https://d78n4vzgjyhqm4.archive.ph/g6cDf/08898709aa1435bc3baf3013c54110d020c87caf.webp)

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

## **2. A client sends a `PUT` request to update a resource. The server responds with `204 No Content`. Why is this better than `200 OK`?**

Below are some of the reasons why `204 No Content` better than `200 OK` for a successful `PUT` update:

- The update is successful and there’s nothing more the client needs to know.
- It avoids sending a redundant or empty response body.
- Helps optimize performance, especially in high-traffic APIs.

## **Example:**

```
@PutMapping("/users/{id}")
public ResponseEntity<Void> updateUser(@PathVariable Long id, @RequestBody UserDto dto) {
    userService.update(id, dto);
    return ResponseEntity.noContent().build();  // Returns HTTP 204
}
```

- `204` signals that the client doesn't need to refresh or reprocess any data — the server accepted the update silently.
- If the updated resource is returned (say, with new computed fields), then `200 OK` with a body makes sense:

```
return ResponseEntity.ok(updatedUserDto);  // HTTP 200 with body
```

- But in cases where the client already has the latest state and no server-generated metadata needs to be returned — 204 is ideal.

## **3. What’s the difference between `301 Moved Permanently` and `308 Permanent Redirect` in HTTP/1.1 and HTTP/2?**

Both `301` and `308` are used to indicate permanent redirects, but they behave differently when it comes to preserving the HTTP method and body.

![](https://d78n4vzgjyhqm4.archive.ph/g6cDf/abeb4b13d84a4084acafe1d23ac0f9009c08e89c.webp)

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

## **4. If a server receives a `PATCH` request but lacks support for the method, which status code should it return: `405`, `501`, or `400`?**

Firstly, let’s understand what each of the given status codes indicate:

- **405 Method Not Allowed**: Server understands the method but doesn’t allow it for the resource
- **501 Not Implemented**: Server doesn’t support the method at all
- **400 Bad Request**: Incorrect when the syntax is valid

So, if a server receives a `PATCH` request but lacks support for the method, it should **return 501 (Not Implemented)** if method is unknown.

- **Use `405` only if the method is supported but not allowed on that specific endpoint.**

## **5. You’re building an API Gateway. How do you differentiate between `502 Bad Gateway`, `503 Service Unavailable`, and `504 Gateway Timeout`?**

When building an API Gateway, understanding the differences between **502 Bad Gateway**, **503 Service Unavailable**, and **504 Gateway Timeout** is crucial for debugging and managing API traffic. Here’s a breakdown:

## **1. 502 Bad Gateway**

- **What it means**: The gateway or proxy server received an invalid response from the upstream server. This typically happens when the upstream server crashes, returns a malformed response (such as HTML instead of JSON), or isn’t functioning as expected.
- **When to use**: This error should be thrown when the server the API Gateway is communicating with returns an unexpected or faulty response, like a crash or corrupted data.
- **Example Scenario**: The downstream microservice crashes or returns an unexpected response (like HTML instead of JSON).

**Example situation**: Your backend service crashed, and the API Gateway cannot parse the error correctly, resulting in a 502 error.

## **2. 503 Service Unavailable**

- **What it means**: The upstream service is **down** or **overloaded**, and cannot process the request. This could be due to maintenance or temporary capacity issues.
- **When to use**: This error occurs when the server cannot process requests because it is either overloaded or temporarily offline for maintenance.
- **Example Scenario**: The API Gateway is unable to reach the service because the service is under heavy load or undergoing scheduled maintenance.

**Example situation**: The backend service is temporarily unavailable for maintenance, so the API Gateway returns a 503 error to the client.

## **3. 504 Gateway Timeout**

- **What it means**: The gateway times out while waiting for a response from the upstream server. This can happen when the upstream server is too slow to respond within the expected time frame.
- **When to use**: This error happens when the API Gateway successfully reaches the upstream service, but the service takes too long to respond.
- **Example Scenario**: The backend service is slow to respond, or there is a network issue causing a delay, resulting in the gateway timing out.

**Example situation**: The backend service is taking too long to process a request, and the API Gateway times out, returning a 504 error.

## **Example:**

In Spring Cloud Gateway, you might configure retry mechanisms to handle 502 Bad Gateway and 504 Gateway Timeout errors. Here’s how you can configure retries in the `application.yml`:

```
spring:
  cloud:
    gateway:
      default-filters:
        - name: Retry
          args:
            retries: 3
            statuses: BAD_GATEWAY, GATEWAY_TIMEOUT
```

In this case:

- **502 (Bad Gateway)**: Happens when the upstream service gives an invalid response, like crashing or sending incorrect data.
- **503 (Service Unavailable)**: Happens when the upstream service is down or overloaded.
- **504 (Gateway Timeout)**: Happens when the gateway times out waiting for the upstream service.

## **6. What are the risks of always returning `200 OK` in your API, even for errors?**

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

## **7. You’re implementing rate limiting. Why is `429 Too Many Requests` more appropriate than `503 Service Unavailable`?**

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

## **8. Can a `304 Not Modified` response include a body? If not, why?**

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

## **9. A client sends invalid credentials. What’s the difference between `401 Unauthorized` and `403 Forbidden`?**

![](https://d78n4vzgjyhqm4.archive.ph/g6cDf/365e5bbac5459196161c7cd2db91f07ab71fa23f.webp)

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

## **10. Why should you avoid using `302 Found` for API redirects involving POST requests?**

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

# **Final Thoughts**

HTTP status codes aren’t just numbers — they’re part of your API’s language.

Using the right code improves clarity, prevents bugs, and shows attention to detail. Mastering them helps you build better APIs and stand out in interviews.

Also, If I missed anything or if you have any suggestions, let me know — I’ll update it.

# **API Gateway with Spring Boot: Deep Dive with Interview Questions**

Imagine you’re traveling for a long-awaited vacation. You arrive at the airport, but before boarding your flight, you need to go through the check-in counter.

Why?

Because the check-in counter acts as a **single point of entry**, handling multiple responsibilities like Identity Verification, Baggage Handling, Security Checks, Load Management, Upgrades & Special Services etc.

Now, imagine an airport without a check-in system — people rushing straight to planes, incorrect luggage on flights, security risks, and complete chaos.

That’s exactly what happens in a **microservices system without an API Gateway** — uncontrolled access, security issues, and inefficient communication.

**API Gateway** is a crucial component in modern application architecture, especially in microservices, cloud computing, and distributed systems.

Now, let’s dive into **why API Gateways are essential**, how they work, and how to implement one using Spring Boot.

# **Definition**

An **API Gateway** is a server that acts as an entry point for **client requests** and routes them to the appropriate backend services.

It provides functionalities like **authentication, rate limiting, caching, request transformation, and security** to ensure efficient and secure communication between clients and services.

Think of it as the front door to a system of microservices, handling all incoming API requests.

# **Need**

- Clients directly interact with multiple microservices.
- Each microservice needs to implement security, rate limiting, and monitoring.
- Load balancing, request validation, and caching are handled separately by each service.
- Inconsistent APIs, leading to poor developer experience.
- Performance overhead due to multiple client-service interactions the appropriate service.

**Features**
1. **Request Routing** — Determines which backend service should process the request.
2. **Authentication & Authorization** — Supports JWT, OAuth, API keys, and other security mechanisms.
3. **Rate Limiting & Throttling** — Restricts API consumption per user/IP.
4. **Logging & Analytics** — Tracks API performance and usage.
5. **Caching** — Stores responses for faster retrieval.
6. **Load Balancing** — Distributes traffic among multiple instances of a microservice.
7. **Circuit Breaker & Failover** — Prevents cascading failures by blocking requests to failing services.
8. **Response Transformation** — Converts responses to required formats.

1. 1. **Request Routing** — Determines which backend service should process the request.
2. 2. **Authentication & Authorization** — Supports JWT, OAuth, API keys, and other security mechanisms.
3. 3. **Rate Limiting & Throttling** — Restricts API consumption per user/IP.
4. 4. **Logging & Analytics** — Tracks API performance and usage.
5. 5. **Caching** — Stores responses for faster retrieval.
6. 6. **Load Balancing** — Distributes traffic among multiple instances of a microservice.
7. 7. **Circuit Breaker & Failover** — Prevents cascading failures by blocking requests to failing services.
8. 8. **Response Transformation** — Converts responses to required formats.

# **Advantages**

- **Single entry point** for all microservices.
- **Centralized security** (authentication, authorization, encryption).
- **Request aggregation** (combine multiple API calls into one).
- **Load balancing & failover** for high availability.
- **Caching & rate limiting** for better performance.
- **Logging & monitoring** for API analytics.

# **Disadvantages**

- **Single point of failure** — If the gateway crashes, the whole API layer fails.
- **Increased latency** — Extra processing (authentication, routing, logging).
- **Complex setup & maintenance** — Needs security, caching, and scaling.
- **Scaling challenges** — Needs distributed architecture for high traffic.

# **Use Cases**

- **Microservices Architecture** — Simplifies inter-service communication.
- **Multi-Client Applications** — Web, mobile, IoT devices consuming APIs.
- **Security-Critical APIs** — Financial services, healthcare, banking APIs.
- **Legacy to Cloud Migration** — Wrapping legacy APIs with a secure gateway.

**API Gateway Architecture: Basic Flow**
1. **Client Sends Request** → (Browser, Mobile App, Postman, etc.)
2. **API Gateway Intercepts the Request** → Checks authentication, authorization, rate limiting.
3. **Gateway Routes the Request** → Sends it to the appropriate microservice.
4. **Microservice Processes the Request** → Retrieves or processes data.
5. **Response is Sent Back to Gateway** → The API Gateway may modify or cache it.
6. **Gateway Returns Response to Client**.

1. 1. **Client Sends Request** → (Browser, Mobile App, Postman, etc.)
2. 2. **API Gateway Intercepts the Request** → Checks authentication, authorization, rate limiting.
3. 3. **Gateway Routes the Request** → Sends it to the appropriate microservice.
4. 4. **Microservice Processes the Request** → Retrieves or processes data.
5. 5. **Response is Sent Back to Gateway** → The API Gateway may modify or cache it.
6. 6. **Gateway Returns Response to Client**.

![](https://dd7gsaj1cdqm6w.archive.ph/E0bhA/902914b396887354108ef7fe03239105a2d256f6.webp)

# **Implementing a simple API Gateway in Spring Boot**

Follow the below steps to implement a simple API gateway in a Spring Boot, Microservices project. Once implemented, we can focus on the advanced processes:

## **Step 1: Add Dependencies**

```
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>

</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

## **Step 2: Configure Routes in `application.yml`**

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: http://localhost:8081/
          predicates:
            - Path=/users/**
        - id: order-service
          uri: http://localhost:8082/
          predicates:
            - Path=/orders/**
```

## **Step 3: Implement API Gateway Filter**

```
@Component
public class CustomFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        ServerHttpRequest request = exchange.getRequest().mutate()
            .header("X-Custom-Header", "Gateway-Processed")
            .build();
        return chain.filter(exchange.mutate().request(request).build());
    }

    @Override
    public int getOrder() {
        return -1;  // Lower values have higher priority
    }
}
```

## **Step 4: Enable API Gateway in Main Class**

```
@SpringBootApplication
public class ApiGatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }
}
```

This configuration routes requests to `user-service` and `order-service`, adding a custom header for tracking purposes.

# **Implement JWT Authentication in API Gateway**

## **Step 1: Add JWT Dependencies**

```
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.11.2</version>
</dependency>
```

## **Step 2: Implement a JWT Filter**

```
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;

@Slf4j
@Component
public class JwtAuthenticationFilter implements GlobalFilter, Ordered {

    private static final String BEARER_PREFIX = "Bearer ";

    @Value("${jwt.secret}")  //Load secret from application properties
    private String secretKey;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        ServerHttpRequest request = exchange.getRequest();

        //Check if Authorization header exists
        if (!request.getHeaders().containsKey(HttpHeaders.AUTHORIZATION)) {
            log.warn("Missing Authorization Header");
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }

        String authHeader = request.getHeaders().getFirst(HttpHeaders.AUTHORIZATION);

        //Validate Bearer token format
        if (authHeader == null || !authHeader.startsWith(BEARER_PREFIX)) {
            log.warn("Invalid Token Format");
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }

        String token = authHeader.substring(BEARER_PREFIX.length());

        //Validate JWT token
        if (!validateJwtToken(token)) {
            log.warn("Invalid Token");
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }

        //Proceed with valid token
        return chain.filter(exchange);
    }

    private boolean validateJwtToken(String token) {
        try {
            SecretKey key = Keys.hmacShaKeyFor(secretKey.getBytes(StandardCharsets.UTF_8));

            Claims claims = Jwts.parserBuilder()
                .setSigningKey(key)
                .build()
                .parseClaimsJws(token)
                .getBody();

            log.info("Token Validated: {}", claims.getSubject());
            return true;
        } catch (Exception e) {
            log.error("JWT Validation Failed: {}", e.getMessage());
            return false;
        }
    }

    @Override
    public int getOrder() {
        return -1; // Higher priority execution
    }
}
```

**Benefit:** Now, all requests passing through the API Gateway must include a **valid JWT token**.

# **Add Rate Limiting with Spring Cloud Gateway**

To prevent API abuse, let’s **limit requests per second per user**.

## **Step 1: Add Rate Limiting Dependencies**

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis-reactive</artifactId>
</dependency>
```

Uses Redis to track request counts. ****Ensure Redis is running, or the Gateway will fail.

## **Step 2: Configure Rate Limiting in `application.yml`**

```
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: http://localhost:8081/
          predicates:
            - Path=/users/**
          filters:
            - name: RequestRateLimiter
              args:
                redis-rate-limiter.replenishRate: 5
                redis-rate-limiter.burstCapacity: 10
                redis-rate-limiter.requestedTokens: 1
            - name: Retry
              args:
                retries: 3
                statuses: 429
```

**Benefit:** Users are now limited to **5 requests per second**, protecting backend services.

# **Implement Circuit Breaker to Prevent Failures**

Circuit breakers prevent cascading failures if a **microservice crashes**.

## **Step 1: Add Resilience4j Dependencies**

```
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-circuitbreaker-reactor-resilience4j</artifactId>
</dependency>
```

## **Step 2: Configure Circuit Breaker in `application.yml`**

```
spring:
  cloud:
    gateway:
      routes:
        - id: order-service
          uri: http://localhost:8082/
          predicates:
            - Path=/orders/**
          filters:
            - name: CircuitBreaker
              args:
                name: orderServiceCircuitBreaker
                fallbackUri: forward:/fallback/orders
```

## **Step 3: Create a Fallback Controller**

```
@RestController
@RequestMapping("/fallback")
public class FallbackController {
    @GetMapping("/orders")
    public ResponseEntity<String> orderFallback() {
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE)
                .body("Order Service is currently unavailable. Please try again later.");
    }
}
```

**Benefit:** If `order-service` fails, clients get a **graceful fallback response** instead of errors.

**API Gateway vs. Service Mesh vs. Backend-for-Frontend (BFF)**

![](https://dd7gsaj1cdqm6w.archive.ph/E0bhA/3f292e6aab0d2052f3cefa9da0c66df5f46220cd.webp)

# **Interview Questions**

Below are some of the interview questions related to API gateway:

## **1. How can you dynamically route requests to different backend services at runtime in Spring Cloud Gateway?**

**Answer:**Dynamic routing allows API Gateway to determine the backend service at runtime, instead of hardcoding routes in `application.yml`.

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

## **2. How do you handle request aggregation in API Gateway when multiple microservices must be queried?**

**Answer:**Request aggregation is essential when an API requires data from multiple microservices.

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

## **3. How do you implement dynamic rate limiting per user using API Gateway?**

**Answer:**

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

## **4. What is a shadow deployment in API Gateway, and how can you implement it?**

**Answer:**Shadow deployment allows testing a new version of an API without impacting live traffic.

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

## **5. How would you implement multi-tenancy in API Gateway?**

**Answer:**For multi-tenancy, API Gateway must route requests dynamically based on tenant ID.

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

## **6. How can API Gateway enforce zero-trust security principles?**

**Answer:**

- **Mutual TLS (mTLS):** Enforce authentication **for both client & server**.
- **OAuth2/JWT-based authentication:** No implicit trust, every request must be validated.
- **Dynamic access control:** API Gateway should **verify user permissions** for each request.
- **Runtime anomaly detection:** Detect **unusual request patterns** in real time.

## **7. How does API Gateway handle caching, and what problems can arise?**

**Answer:**API Gateway can cache responses using a **distributed cache** (e.g., Redis).

**Problems:**

- **Stale data**: Need cache invalidation strategies.
- **Incorrect granularity**: Caching too much or too little.
- **Security risk**: Caching sensitive data (avoid caching auth tokens).

## **8. How can API Gateway track request tracing across microservices?**

**Answer:**Use distributed tracing (Zipkin, OpenTelemetry):

- Inject trace ID in request headers:

```
String traceId = UUID.randomUUID().toString();
ServerHttpRequest request = exchange.getRequest().mutate()
    .header("X-Trace-ID", traceId)
    .build();
```

## **9. How would you prevent replay attacks in API Gateway?**

**Answer:**

- Use a nonce (one-time token) for each request.
- Reject duplicate requests within a time window using Redis.

## **10. How do you implement blue-green deployments in API Gateway?**

**Answer:**Use **weighted routing**:

```
routes:
  - id: blue-service
    uri: http://blue-version
    weight: 90
  - id: green-service
    uri: http://green-version
    weight: 10
```

# **Final Thoughts**

API Gateways are indispensable in modern cloud and microservices architectures. They are critical for security, scalability, and deployment efficiency.

So, it’s better to learn about them and try to build one from scratch.

Also, If I missed anything or if you have any suggestions, let me know — I’ll update it.

# **Create a Spring Boot Rest API Project From Scratch**

# **1. Create a New Project in IntelliJ IDEA**

Instead of using Spring Initializr, we’ll manually create a project to understand the structure better.

- Open IntelliJ IDEA.
- Select **“Java” or “Spring”** under **“New Project.”**
- Choose **“Maven”** as the build system (as shown in the screenshot).
- Set the project name and location.
- Select the JDK (like **OpenJDK 23.0.2**).
- Keep the sample code and onboarding tips checked (or uncheck if you prefer a clean start).
- Hit **Create** to generate the project.

![](https://dd78vagm60f6ph.archive.ph/DpxgH/b1c88298e313baf3b40396a7857afeaa0b66e1c2.webp)

I’ve seen a lot of tutorials using Spring Initializr. While it’s not wrong, you’re unlikely to use Spring Initializr in a real company project.

It’s better to understand how dependencies and configurations work instead of relying on auto-generated code.

# **2. Define the Project Structure**

Once the project is created, define a clean and organized structure. A typical Spring Boot project follows this pattern:

![](https://dd78vagm60f6ph.archive.ph/DpxgH/2b48b45258f251ac05d1213eb9d7fbb75fae8601.webp)

## **1. Controller Layer (`controller`):**

- Contains all the REST endpoints.
- Uses `@RestController` to handle HTTP requests and responses.
- **Example:** `UserController.java` manages routes like `/api/users`.

## **2. Service Layer (`service`)**

- Contains business logic.
- Uses `@Service` to define reusable business functions.
- **Example:** `UserService.java` handles data processing and complex logic.

## **3. Repository Layer (`repository`)**

- Handles data access using Spring Data JPA.
- Uses `@Repository` to abstract database operations.
- **Example:** `UserRepository.java` extends `JpaRepository`.

## **4. Model Layer (`model`)**

- Contains entity classes that map to database tables.
- Uses `@Entity` to define JPA entities.
- **Example:** `User.java` maps to the `user` table.

## **5. Main Class**

- `@SpringBootApplication` initializes the Spring Boot context.
- **Example:** `SpringBootRestApplication.java` is the entry point of the app.

## **6. Resources**

- `application.properties` – Configures the app (database URL, logging, etc.).
- `schema.sql` – (Optional) Initializes database schema if needed.

## **7. Test Layer (`test`)**

- Holds unit and integration tests.
- Follows the same package structure as `main`.

# **3. Create/Update SpringBootRestApplication.java file**

```
package com.example.springbootrest;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringBootRestApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootRestApplication.class, args);
    }
}
```

## **How to Run:**

1. Open a terminal or use the built-in terminal in your IDE.
2. Run the following command:

```
mvn spring-boot:run
```

orIf you’re using an IDE like **IntelliJ** or **Eclipse**, just **right-click** on `SpringBootRestApplication.java` → **Run**.

## **Expected Output:**

- You should see the following log message when the application starts successfully:

```
Started SpringBootRestApplication in XX.YYY seconds
```

## **Verify:**

Open your browser and go to: [http://localhost:8080](https://archive.ph/o/DpxgH/localhost:8080/)

If the setup is correct, the app will start without any errors.

# **4. Update pom.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.4</version>
        <relativePath/>
    </parent>

    <groupId>org.example</groupId>
    <artifactId>spring-boot-rest</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Spring Boot Starter Web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Spring Boot Starter Data JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <!-- Postgres Driver -->

        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.5.5</version>
            <scope>runtime</scope>
        </dependency>

        <!-- Lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.30</version>
            <scope>provided</scope>
        </dependency>

        <!-- Spring Boot Starter Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.1.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

## **Explanation of Dependencies:**

1. **Spring Boot Starter Web** — For creating RESTful APIs.
2. **Spring Boot Starter Data JPA** — For database access using Spring Data.
3. **PostgreSQL Driver** — For connecting to a PostgreSQL database.
4. **Lombok** — To reduce boilerplate code (like getters, setters, constructors).
5. **Spring Boot Starter Test** — For writing unit tests.

## **Update Dependencies:**

If any dependencies are missing or outdated, run:

```
mvn clean install
```

This will download all dependencies and update the project.

# **5. Create the Necessary Classes**

Let’s create the essential components step-by-step.

## **Model:**

Create an entity class to define the table structure:

```
package com.example.springbootrest.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false, unique = true)
    private String email;
}
```

## **Repository:**

Create a repository interface to interact with the database:

```
package com.example.springbootrest.repository;

import com.example.springbootrest.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
```

## **Service:**

Create a service class to handle the business logic:

```
package com.example.springbootrest.service;

import com.example.springbootrest.model.User;
import com.example.springbootrest.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

@Autowired
private UserRepository userRepository;

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public User updateUser(Long id, User updatedUser) {
        return userRepository.findById(id)
                .map(user -> {
                    user.setName(updatedUser.getName());
                    user.setEmail(updatedUser.getEmail());
                    return userRepository.save(user);
                }).orElseThrow(() -> new RuntimeException("User not found with id " + id));
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

## **Controller:**

Create a controller class to handle the HTTP endpoints:

```
package com.example.springbootrest.controller;

import com.example.springbootrest.model.User;
import com.example.springbootrest.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public Optional<User> getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
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

# **6. Connect to an SQL Database**

## **1. `application.properties`**

Add the following configuration to the `src/main/resources/application.properties` file:

```
# Server Configuration
server.port=8080

# PostgreSQL Configuration
spring.datasource.url=jdbc:postgresql://localhost:5433/springbootrest
spring.datasource.username=springuser
spring.datasource.password=password
spring.datasource.driver-class-name=org.postgresql.Driver

# Hibernate Configuration
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

1. `server.port=8080` – Sets the port where the app will run.
2. `spring.datasource.url` – JDBC URL for PostgreSQL connection.
3. `spring.datasource.username` – PostgreSQL username.
4. `spring.datasource.password` – PostgreSQL password.
5. `spring.datasource.driver-class-name` – PostgreSQL driver class.
6. `spring.jpa.database-platform` – Hibernate dialect for PostgreSQL.
7. `spring.jpa.hibernate.ddl-auto=update` – Automatically updates schema based on entity definitions.
8. `spring.jpa.show-sql=true` – Logs generated SQL queries to the console.

## **2. `schema.sql`**

Create a `schema.sql` file in `src/main/resources`: `src/main/resources/schema.sql`

```
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

## **Initialize the Database:**

1. Ensure that PostgreSQL is running.
2. Create a database using:

```
CREATE DATABASE springbootrest;
```

3. Start the Spring Boot application:

```
mvn spring-boot:run
```

## **What Happens:**

- Spring Boot will create the `users` table if it doesn’t exist.
- Any schema update will be handled automatically by `spring.jpa.hibernate.ddl-auto=update`.
- SQL queries will be logged in the console.

# **7. Test with Postman and Database**

Now that the project is set up, you can test the endpoints using Postman:

1. Open Postman.
2. Create a new request.
3. Test each endpoint (GET, POST, PUT, DELETE).

**Example:**

## **1. POST Request — Create a New User**

- **Method:** `POST`
- **URL:** [`http://localhost:8080/api/users`](https://archive.ph/o/DpxgH/localhost:8080/api/users)
- **Body:** (Set to `raw` → `JSON`)

![](https://dd78vagm60f6ph.archive.ph/DpxgH/97045fbf15d3ce8f868d7a7b2839d3446b55e945.webp)

Now, we see the status 200, so it means it is added successfully.

With the GET call, we should be able to verify if this:

## **2. GET Request — Fetch All Users**

- **Method:** `GET`
- **URL:** [`http://localhost:8080/api/users`](https://archive.ph/o/DpxgH/localhost:8080/api/users)
- **Expected Response:**

![](https://dd78vagm60f6ph.archive.ph/DpxgH/50c1a944877106d780805367f3f48aff34b5f717.webp)

Also, can be verified from DB, that the user is added:

![](https://dd78vagm60f6ph.archive.ph/DpxgH/c9348237bd50f3e29ff264e4f53873f85900c19c.webp)

# **RSocket with Spring Boot: Deep Dive with Interview Questions**

Imagine you walk into a coffee shop and place an order for a cappuccino.

In a traditional setup (like HTTP request-response), you stand at the counter waiting until your coffee is ready before leaving. If the barista is busy, you’re stuck waiting, wasting time.

Now, imagine a more efficient system: you place your order, get a token, and sit at a table. The barista prepares your coffee and notifies you when it’s ready. You only return when needed, freeing you to do other things in the meantime.

This is how **RSocket improves communication** — instead of waiting for responses (blocking calls), it allows asynchronous, event-driven interactions between services, making applications more responsive and efficient.

# **Definition**

RSocket is a reactive, binary protocol designed for efficient and high-performance communication over various transport layers such as TCP, WebSockets, Aeron, and HTTP/2.

RSocket was developed by Netflix and is now a part of the RSocket.io initiative.

Unlike REST and gRPC, RSocket is not tied to HTTP and supports asynchronous, event-driven architectures with built-in backpressure, multiplexing, and low-latency messaging.

# **Features**

- **Transport-Agnostic** — Works over TCP, WebSockets, HTTP/2, etc.
- **Full-Duplex Communication** — Supports bidirectional streaming.
- **Multiplexing** — Multiple logical streams over one connection.
- **Built-in Backpressure** — Prevents overwhelming services.
- **Low Latency & Lightweight** — Uses binary encoding.
- **Multiple Interaction Models** — Request-response, streaming, fire-and-forget, and channel.
- **Session Resumption** — Restores dropped connections without re-establishing.
- **Reactive-Friendly** — Works with Project Reactor and RxJava.

# **Use Cases**

- **Microservices Communication** — Efficient, low-latency service-to-service calls.
- **Streaming Data** — Real-time stock updates, chat apps, video streaming.
- **IoT & Edge Computing** — Saves bandwidth, improves efficiency.
- **Bidirectional APIs** — Ideal for APIs needing real-time updates.
- **Gaming & Multiplayer Apps** — Fast event-driven updates.
- **Serverless & Cloud-Native Apps** — Real-time event triggers.
- **Database Change Notifications** — Efficient event streaming.
- **GraphQL Subscriptions** — Better than WebSockets for real-time queries.
- **Mobile Apps** — Reduces battery drain compared to polling.
- **ML Model Serving** — Streams inference results in real-time.

# **Advantages**

- **Asynchronous & Non-blocking** — Works seamlessly with reactive programming.
- **Lightweight & Multiplexing Support** — Allows multiple streams over a single connection.
- **Built-in Backpressure Handling** — Prevents overwhelming downstream services.
- **Supports Multiple Interaction Models** — Unlike WebSockets, RSocket provides request-response, streaming, and fire-and-forget.

# **Disadvantages**

- **Not as widely adopted** as REST or gRPC, leading to limited community support.
- **Requires a reactive paradigm**, which has a learning curve for developers unfamiliar with Project Reactor or RxJava.
- **Debugging can be harder** due to binary encoding, making it less human-readable than JSON-based REST APIs.

# **RSocket Communication Models**

RSocket supports four interaction models, making it more flexible than WebSockets or traditional HTTP-based protocols:

## **1. Request-Response (Unary Communication)**

- The client sends a request and receives a single response.
- Similar to traditional REST APIs.
- **Example use case**: Fetching user details from a database.

```
@MessageMapping("request-response")
public Mono<String> requestResponse(@Payload String request) {
    return Mono.just("Response for: " + request);
}
```

## **2. Fire-and-Forget (No Response Needed)**

- The client sends a message without waiting for a response.
- Useful for logging, telemetry, or event notifications.

```
@MessageMapping("fire-and-forget")
public Mono<Void> fireAndForget(@Payload String message) {
    log.info("Received Fire-and-Forget Message: {}", message);
    return Mono.empty();  // No response sent back
}
```

## **3. Request-Stream (Streaming Response)**

- The client sends one request and receives a stream of responses.
- Ideal for real-time stock prices, logs, or event streaming.

```
@MessageMapping("request-stream")
public Flux<String> requestStream(@Payload String request) {
    return Flux.interval(Duration.ofSeconds(1)) // Stream emits values every second
               .map(i -> "Stream response " + i)
               .take(5); // Limit the number of responses
}
```

## **4. Channel (Bidirectional Streaming)**

- Both the client and server continuously exchange messages.
- Useful for chat applications, collaborative tools, or IoT communication.

```
@MessageMapping("channel")
public Flux<String> channel(@Payload Flux<String> requests) {
    return requests.map(request -> {
        log.info("Received from client: {}", request);
        return "Echo: " + request;
    });
}
```

**Comparison with WebSockets & gRPC**

![](https://dgprwqcp7lz2wh.archive.ph/cF0Us/265a8912a99c4287acf79d2cb9c877a4cd1b7486.webp)

# **Security Considerations**

RSocket supports **multiple security mechanisms**:

- **TLS (Transport Layer Security)** — Ensures encrypted communication.
- **JWT Authentication** — Token-based authentication for securing requests.
- **OAuth2 Integration** — Works with Spring Security for token validation.
- **Custom Authentication** — Can embed security metadata in RSocket frames.

# **Performance Benchmarks**

RSocket is optimized for high-performance messaging:

- Lower latency than REST and gRPC due to binary encoding and persistent connections.
- Efficient multiplexing reduces the number of connections needed.
- Handles millions of concurrent connections with minimal resource usage.

# **Deployment and Scaling**

a) **Containerizaztion —** RSocket services can be containerized and deployed in Kubernetes.

b) **Horizontal Scaling** — Since RSocket uses persistent connections, use round-robin DNS or Kubernetes service discovery. Use Horizontal Pod Autoscaler (HPA) to scale instances dynamically.

**c) Service Mesh Integration** — Tools like Istio and Linkerd can help with traffic control, retries, and observability.

**d) RSocket Load Balancing Strategies** — Load balancers can distribute RSocket connections for high availability. Use sticky sessions or connection pooling for better efficiency.

- **Client-Side Load Balancing**: Use multiple RSocket connections and distribute them.
- **Server-Side Load Balancing**: Use Kubernetes Headless Services with round-robin or Eureka Service Discovery.

**e) Connection Pooling**: Use `RSocketRequester.builder().setupRoute()` for warm connections.

## **Spring Boot RSocket Configuration (application.yml)**

This configuration enables an RSocket server on port 7000 using TCP transport.

```
spring:
  rsocket:
    server:
      port: 7000
      transport: tcp
```

# **Error Handling & Observability**

RSocket provides built-in error handling mechanisms:

**Common RSocket errors:**

- `INVALID_SETUP` – Incorrect handshake.
- `CONNECTION_ERROR` – Network failure.
- `APPLICATION_ERROR` – Server-side issue.

**Example:**

```
.requestResponse(Mono.just("Hello"))
.doOnError(error -> System.err.println("Error: " + error.getMessage()))
.onErrorReturn("Fallback response")
.subscribe(System.out::println);
```

# **Logging & Metrics**

- **Prometheus & Grafana** — Monitor RSocket performance metrics.
- **Zipkin or Jaeger** — Distributed tracing for debugging.
- **Enable Debug Logging in RSocke**t

```
logging.level.io.rsocket=DEBUG
```

**Implementation in Spring Boot
1. Add Dependencies**

```jsx
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-rsocket</artifactId>
</dependency>
<dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.4.0</version>
</dependency>
```

**2. RSocket Controller**

```jsx
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Controller;
import reactor.core.publisher.Mono;

@Controller
public class RSocketController {
    @MessageMapping("request-response")
    public Mono<String> requestResponse(@Payload String request) {
        return Mono.just("Response for: " + request);
    }
    @MessageMapping("fire-and-forget")
    public void fireAndForget(@Payload String message) {
        System.out.println("Received: " + message);
    }
    @MessageMapping("request-stream")
    public Flux<String> requestStream(@Payload String request) {
        return Flux.interval(Duration.ofSeconds(1))
                   .map(i -> "Stream response " + i)
                   .take(5);
    }
}
```

**3. RSocket Client**

```jsx
import org.springframework.messaging.rsocket.RSocketRequester;
import reactor.core.publisher.Mono;

public class RSocketClient {
    public static void main(String[] args) {
       RSocketRequester requester = RSocketRequester.builder()
                                    .connectTcp("localhost", 7000)
                                    .retryWhen(Retry.backoff(5, Duration.ofSeconds(2)))
                                    .doOnError(error -> System.err.println("Connection failed: " + error.getMessage()))
                                    .block();
        // Request-Response
        requester.route("request-response")
            .data("Hello RSocket")
            .retrieveMono(String.class)
            .doOnError(error -> System.err.println("Request failed: " + error.getMessage()))
            .subscribe(System.out::println);
        // Fire-and-Forget
        requester.route("fire-and-forget")
            .data("Logging this message")
            .send()
            .subscribe();
    }
}
```

# **Tricky Interview Questions:**

## **1. How would you implement error handling in an RSocket service? What happens if the client or server disconnects during a request-response interaction?**

RSocket provides built-in error handling mechanisms and allows developers to implement custom handling to ensure resilience.

## **1. Built-in Error Codes in RSocket**

RSocket defines standard error codes that can be handled at the client or server side:

- **INVALID_SETUP** → Handshake issue (e.g., incorrect authentication or setup payload).
- **CONNECTION_ERROR** → Network failure or client-server disconnect.
- **APPLICATION_ERROR** → Business logic failure on the server.
- **REJECTED_SETUP** → Server rejects the setup due to authentication or protocol mismatch.
- **REJECTED_RESUME** → Occurs when a client attempts to resume a connection, but the server does not have a matching session (e.g., due to session expiration or loss).

## **2. Handling Errors in a Request-Response Interaction**

Since RSocket is reactive, we use onErrorResume(), doOnError(), or onErrorReturn() to gracefully handle failures.

## **Example: Handling Errors on the Client**

If the server fails to respond, we catch errors and provide a fallback response:

```
requester.route("request-response")
    .data("Hello RSocket")
    .retrieveMono(String.class)
    .onErrorResume(error -> {
        System.err.println("Request failed: " + error.getMessage());
        return Mono.just("Fallback response");
    })
    .subscribe(System.out::println);
```

- `onErrorResume()` → Handles the error and provides an alternative response dynamically.

## **Example: Handling Errors on the Server**

The server can catch exceptions and return meaningful error messages instead of crashing:

```
@MessageMapping("request-response")
public Mono<String> requestResponse(@Payload String request) {
    return Mono.just(request)
        .flatMap(data -> {
            if (data.equalsIgnoreCase("fail")) {
                return Mono.error(new RuntimeException("Simulated server error"));
            }
            return Mono.just("Response for: " + request);
        })
        .onErrorResume(e -> Mono.just("Error occurred: " + e.getMessage()));
}
```

- `flatMap()` → Ensures proper error propagation.
- `onErrorResume()` → Handles the error gracefully and returns a meaningful message.

## **3. Handling Client or Server Disconnections**

When the client or server disconnects, RSocket provides reconnection strategies to ensure robustness.

## **Client-Side Reconnection**

If the client disconnects due to network issues, use retryWhen() for exponential backoff retries:

```
RSocketRequester requester = RSocketRequester.builder()
    .connectTcp("localhost", 7000)
    .retryWhen(Retry.backoff(5, Duration.ofSeconds(2)))  // Retry up to 5 times with increasing delays
    .doOnError(error -> System.err.println("Connection failed: " + error.getMessage()))
    .block();
```

- **retryWhen()** → Retries the connection using an exponential backoff strategy to prevent overloading the server.

## **Server-Side Handling for Client Disconnections**

Use RSocket lifecycle callbacks to detect when a client disconnects:

```
@EventListener
public void handleRSocketDisconnect(RSocketRequester requester) {
    requester.rsocket()
        .onClose()
        .doFinally(signal -> log.info("Client disconnected, cleaning up resources"))
        .subscribe();
}
```

- **onClose()** → Triggers cleanup when a client disconnects.

## **4. Using Keep-Alive to Detect Broken Connections**

RSocket supports keep-alive heartbeats to detect when a client or server is unreachable.

## **Server-Side Keep-Alive Configuration (`application.yml`)**

```
spring:
  rsocket:
    server:
      transport: tcp
      keepalive:
        interval: 20s   # Ping every 20 seconds
        max-life: 60s   # Disconnect if no response in 60 seconds
```

- **interval** → How often the server sends keep-alive pings.
- **max-life** → How long the server waits before considering the client unresponsive.

## **Client-Side Keep-Alive Configuration**

```
RSocketRequester.builder()
    .setupMetadata("client-id", MetadataCodec.defaultMetadata())
    .keepAlive(Duration.ofSeconds(20), Duration.ofSeconds(60))
    .connectTcp("localhost", 7000);
```

- Ensures bidirectional keep-alive monitoring to detect failures.

## **2. What are some common challenges you face when using RSocket in a microservices architecture?**

RSocket is great for low-latency, reactive, and bi-directional communication, but it comes with some challenges when integrating it into a microservices architecture. Let me break them down one by one.

## **1. Service Discovery & Load Balancing**

Unlike REST, which is stateless, RSocket uses persistent connections, making traditional load balancing (e.g., round-robin DNS, HTTP-based ALBs) ineffective.

**Problem**:

- If a client connects to a failed server, it must retry another node.
- Standard HTTP-based load balancers don’t work well with long-lived RSocket connections.

**Solution**:

We need sticky load balancing or a broker-based architecture. Here’s an example using Spring Cloud LoadBalancer for RSocket clients:

```
@Bean
public RSocketRequester rSocketRequester(RSocketRequester.Builder builder, LoadBalancerExchangeFilterFunction lb) {
    return builder
        .rsocketConnector(connector -> connector.loadBalance(lb)) // Correct Load Balancer
        .connectTcp("localhost", 7000)
        .block();
}
```

This helps dynamically discover healthy instances instead of relying on static IPs.

## **2. Connection Management & Backpressure Handling**

RSocket supports unlimited concurrent streams, but without proper backpressure, the server may get overwhelmed.

**Problem**:

If a client sends too many requests, the server may run out of memory or crash.

**Solution**:

We use RSocket’s `request(n)` mechanism to limit data flow based on client capacity.

```
requester.route("stream-data")
    .data("Start Streaming")
    .retrieveFlux(String.class)
    .doOnRequest(n -> System.out.println("Requesting " + n + " items")) // Explicit backpressure
    .subscribe(System.out::println);
```

This ensures controlled data flow and prevents overloading the microservice.

## **3. Authentication & Security**

Unlike HTTP, which has OAuth, JWT, and API gateways, RSocket needs manual security implementation.

**Problem**:

- No built-in API gateway support like Kong or Apigee.
- JWT authentication isn’t natively enforced.

**Solution**:

We secure RSocket using Spring Security with JWT tokens:

```
@Configuration
public class RSocketSecurityConfig {
    @Bean
    public RSocketSecurity rSocketSecurity(RSocketSecurity security) {
        return security
            .authorizePayload(auth -> auth.anyRequest().authenticated()) // Securing RSocket payloads
            .jwt(Customizer.withDefaults()); // JWT Authentication
    }
}
```

This ensures only authenticated clients can communicate using RSocket.

## **4. Debugging & Observability Issues**

Since RSocket is fully reactive, traditional tools like Postman, cURL, or logging middleware don’t work well.

## **Problem:**

- No easy way to log request-response interactions.
- Hard to trace RSocket requests in distributed microservices.

## **Solution:**

Use Micrometer + Prometheus for metrics and OpenTelemetry for distributed tracing.

```
@Bean
public MeterRegistryCustomizer<MeterRegistry> metricsConfig() {
    return registry -> registry.config().commonTags("application", "rsocket-service");
}
```

For detailed logging, use Logging Interceptors:

```
import io.rsocket.plugins.InterceptorRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.publisher.Hooks;
import reactor.util.Loggers;

import javax.annotation.PostConstruct;
@Configuration
public class RSocketLoggingConfig {
    private static final Logger logger = LoggerFactory.getLogger(RSocketLoggingConfig.class);
    @PostConstruct
    public void enableReactorDebug() {
        Hooks.onEachOperator(Loggers::enableLogger); // Enables detailed RSocket logs
    }
    @Bean
    public RSocketConnectorCustomizer loggingInterceptor() {
        return connector -> connector.interceptors((InterceptorRegistry registry) ->
            registry.forRequester(frame -> {
                logger.info("Sending request: {}", frame);
                return frame;
            }).forResponder(frame -> {
                logger.info("Received response: {}", frame);
                return frame;
            })
        );
    }
}
```

This enables real-time monitoring and tracing of RSocket services.

## **5. Handling Client or Server Failures**

RSocket supports session resumption, but it needs explicit handling when a server crashes.

**Problem:**

- If the server goes down, clients need to reconnect manually.
- Stateless REST APIs auto-retry, but RSocket needs resumability.

**Solution:**

Enable resumption in RSocket client to reconnect automatically:

```
import io.rsocket.core.Resume;
import io.rsocket.frame.decoder.PayloadDecoder;
import io.rsocket.transport.netty.client.TcpClientTransport;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.rsocket.RSocketRequester;
import reactor.util.retry.Retry;

import java.time.Duration;
@Configuration
public class RSocketClientConfig {
    @Bean
    public RSocketRequester rSocketRequester(RSocketRequester.Builder builder) {
        return builder
            .rsocketConnector(connector -> connector
                .resume(new Resume()
                    .store(new InMemoryResumableFramesStore("client")) // Stores unacknowledged frames
                    .retry(Retry.fixedDelay(3, Duration.ofSeconds(5))) // Retries 3 times with 5s delay
                )
                .payloadDecoder(PayloadDecoder.ZERO_COPY) // Optimized payload decoding
            )
            .transport(TcpClientTransport.create("localhost", 7000)) // Connects to server
            .block();
    }
}
```

This allows clients to resume from the last state instead of restarting the entire session.

## **3. Explain the concept of backpressure in RSocket. How does it handle it differently compared to other protocols like HTTP/2?**

Backpressure is a flow-control mechanism that ensures a fast producer does not overwhelm a slow consumer. It helps maintain system stability and prevents memory overflows when handling large amounts of data.

In traditional request-response models like HTTP/1.1, the server sends data as fast as possible, assuming the client can handle it. Since HTTP/1.1 lacks built-in backpressure, this can overwhelm the consumer.

In contrast, reactive systems (like RSocket) use the Reactive Streams specification, where consumers can request data at their own pace, ensuring a controlled and efficient data flow.

## **How Does RSocket Handle Backpressure?**

RSocket is fully reactive and natively supports backpressure through the Reactive Streams specification.

Unlike protocols like HTTP/2, where flow control is handled at the transport level, RSocket decouples transport flow control from application logic, allowing fine-grained control over data flow.

While RSocket runs over TCP, it does not rely on TCP’s backpressure alone; instead, it implements reactive backpressure at the application level for optimal performance.

## **RSocket’s Backpressure Handling:**

1. **Demand-Based Flow Control** (`request(n)`)
- The client explicitly requests `n` items from the server.
- The server only sends what is requested, ensuring controlled data flow.

```
requester.route("stream-data")
    .data("Start Streaming")
    .retrieveFlux(String.class)
    .doOnRequest(n -> System.out.println("Requesting " + n + " items")) // Explicit backpressure
    .subscribe(System.out::println);
```

- **Advantage**: The client never gets overloaded with more data than it can handle.

**2. Backpressure Propagation**

- If the client stops requesting, the server pauses sending data.
- This ensures that resources are used efficiently, avoiding memory overflows.

**3. Resumable Sessions** (if enabled)

- If a client disconnects temporarily, RSocket remembers its last requested position and resumes from there when it reconnects.
- If session resumption is enabled, RSocket remembers the last acknowledged request. This allows a client to resume from where it left off after a temporary disconnection. However, the server must be explicitly configured with a resumable session store, such as `InMemoryResumableFramesStore`.

## **Difference between RSocket vs HTTP/2?**

![](https://dgprwqcp7lz2wh.archive.ph/cF0Us/7cd54eed3e3716283404ba21420eaf9e473b042e.webp)

## **4. If you need to deploy an RSocket service in Kubernetes, how would you scale it efficiently to handle a large number of connections?**

To deploy and scale an RSocket service efficiently in Kubernetes (K8s) while handling a large number of connections, you need to address key concerns like load balancing, connection persistence, scaling strategies, and resource optimization.

Here’s how you can achieve this:

## **1. Choose the Right Load Balancing Strategy**

Unlike HTTP-based services, RSocket uses persistent connections, meaning traditional round-robin load balancing (via Kubernetes Services) does not work well.

Instead, we should use:

## **Sticky Load Balancing (Session-Aware Load Balancing)**

Since RSocket maintains long-lived connections, you should ensure a client consistently connects to the same server instance to avoid breaking session state.

**Solution:** Use a TCP-aware load balancer that supports consistent hashing to route a connection to the same pod.

**Options:**

- Envoy with TCP Proxy Mode
- Nginx with Hash-based Load Balancing
- Ingress with Stateful Sessions (e.g., Traefik, Linkerd)

**Example for Nginx-based sticky load balancing:**

```
upstream rsocket_servers {
    hash $remote_addr consistent;  # Ensures clients reconnect to the same instance
    server rsocket-pod-1:7000;
    server rsocket-pod-2:7000;
}
```

**Alternative**: If using Spring Boot RSocket, consider Spring Cloud Gateway with RSocket Routing.

## **2. Horizontal Pod Autoscaling (HPA) for Efficient Scaling**

Since RSocket connections are stateful, scaling needs to consider connection load, CPU, and memory usage rather than simple request counts.

## **Scale Based on Concurrent Connections**

- Use Custom Metrics (via Prometheus + K8s HPA) to scale based on active connections per pod.

**Example HPA configuration for RSocket service:**

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: rsocket-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: rsocket-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: External
      external:
        metricName: rsocket_active_connections
        target:
          type: AverageValue
          averageValue: 500  # Scale when a pod has more than 500 active connections
```

You can use Prometheus + Custom Exporter to track active RSocket connections per pod.

## **Scale Based on CPU and Memory Usage**

- If CPU/Memory spikes due to large data streams, use CPU-based HPA scaling:

```
- type: Resource
  resource:
    name: cpu
    target:
      type: Utilization
      averageUtilization: 75
```

## **3. Connection Distribution: Using RSocket Load Balancer**

## **Client-Side Load Balancing (Best Approach for RSocket)**

Since RSocket maintains long-lived connections, traditional server-side load balancing is inefficient. Instead, use client-side load balancing, where the client chooses an available node dynamically.

**Spring Cloud RSocket Load Balancer Example:**

```
RSocketRequester.builder()
    .rsocketConnector(connector -> connector.reconnect(Retry.fixedDelay(5, Duration.ofSeconds(2))))
    .transport(TcpClientTransport.create("rsocket-service", 7000));
```

**Alternative:** Use Service Discovery (Eureka, Consul, Kubernetes DNS) to Fetch Available RSocket Nodes**.**

## **4. Resilience: Handling Connection Failures Gracefully**

Since RSocket services maintain persistent connections, pods can restart or scale up/down dynamically, causing disconnections. Use the following techniques:

## **a) Reconnect Automatically Using Retry Mechanisms**

```
RSocketRequester.builder()
    .rsocketConnector(connector -> connector.reconnect(Retry.fixedDelay(5, Duration.ofSeconds(2))))
    .transport(TcpClientTransport.create("rsocket-service", 7000));
```

## **b) Enable Resumable Sessions to Prevent Data Loss**

Enable resumable sessions to avoid losing in-flight data:

```
RSocketRequester.builder()
    .rsocketConnector(connector -> connector.resume(resumeStrategy()))
    .transport(TcpClientTransport.create("rsocket-service", 7000));
```

## **c) Use Circuit Breakers (Resilience4J) to Prevent Failures**

```
CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("rsocketCircuitBreaker");
RSocketRequester.builder()
    .rsocketConnector(connector -> connector.addRequesterPlugin(CircuitBreakerOperator.of(circuitBreaker)))
    .transport(TcpClientTransport.create("rsocket-service", 7000));
```

## **5. Optimize Resource Usage for High Throughput**

## **Tune TCP Settings for High Connection Load**

- Set higher ulimit for file descriptors (`ulimit -n 100000`) to handle thousands of open connections.
- Increase Kubernetes pod `max open connections` limit to avoid connection drops.

## **Optimize RSocket Frame Size & Keep-Alive Intervals**

- Reduce frame size to avoid TCP fragmentation.
- Tune keep-alive interval to avoid unnecessary reconnections.

**Example (Spring Boot RSocket config in `application.yml`):**

```
spring:
  rsocket:
    server:
      transport: tcp
      port: 7000
      keep-alive-interval: 30s
      max-frame-length: 1048576  # 1MB frame size
```

## **Final Kubernetes Deployment YAML for RSocket Service**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rsocket-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rsocket
  template:
    metadata:
      labels:
        app: rsocket
    spec:
      containers:
      - name: rsocket-container
        image: my-rsocket-app:latest
        ports:
        - containerPort: 7000
        env:
        - name: RSOCKET_PORT
          value: "7000"
        - name: SPRING_RSOCKET_KEEP_ALIVE_INTERVAL
          value: "30s"
        resources:
          requests:
            cpu: "250m"
            memory: "512Mi"
          limits:
            cpu: "1000m"
            memory: "2Gi"
```

## **5. How does RSocket handle retries if a request fails?**

RSocket enables resilient communication by allowing client-side retries, resumable sessions, and circuit breakers to handle failures efficiently.

## **1. Client-Side Retries (Best Practice)**

RSocket does not provide built-in retries but supports retries using Reactor’s retry utilities (`Retry.fixedDelay`, `Retry.backoff`).

**Example: Retrying a Request with Fixed Delay**

```
RSocketRequester requester = RSocketRequester.builder()
    .rsocketConnector(connector -> connector.reconnect(Retry.fixedDelay(5, Duration.ofSeconds(2)))) // Handles reconnections
    .transport(TcpClientTransport.create("localhost", 7000));

Mono<String> response = requester.route("fetch.data")
    .retrieveMono(String.class)
    .retryWhen(Retry.fixedDelay(3, Duration.ofSeconds(1))); // Retries request 3 times with 1s delay
```

**How It Works:**

- If the request fails due to network issues, timeouts, or transient server errors, the client retries up to 3 times with a 1-second delay.
- If all retries fail, the error propagates to the caller.

**Exponential Backoff for Smarter Retries**

```
.retryWhen(Retry.backoff(3, Duration.ofMillis(500))
    .maxBackoff(Duration.ofSeconds(5))
    .jitter(0.5)
    .filter(throwable -> throwable instanceof TimeoutException)) // Only retry on timeouts
```

**Why Use Backoff:**

- Prevents retry storms when a service is down.
- Reduces server overload by introducing randomized retry delays (jitter).

## **2. Resumable Sessions (Avoiding Data Loss on Disconnects)**

If a connection drops mid-stream, RSocket can resume the session instead of restarting the entire request flow.This is useful for mobile networks, cloud environments, or unstable connections.

**Enable Resumable Sessions:**

```
RSocketRequester.builder()
    .rsocketConnector(connector ->
        connector.resume(Resume.builder().build()) // Enables resumability
    )
    .transport(TcpClientTransport.create("localhost", 7000));
```

**How It Works:**

- If the connection is lost, the client automatically resumes from where it left off.
- Ideal for streaming scenarios (e.g., real-time updates, chat apps).

## **3. Handling Retries at the Server Side**

If a request fails on the server, the retry logic should be applied inside the message handler rather than using interceptors.

**Example: Retrying Server Processing Logic**

```
@MessageMapping("fetch.data")
public Mono<String> fetchData() {
    return Mono.fromSupplier(() -> someUnstableServiceCall())
        .retryWhen(Retry.fixedDelay(3, Duration.ofSeconds(1))); // Retries failed processing 3 times
}
```

**Why Use This:**

- Handles temporary failures (e.g., database unavailability, slow network).
- Ensures faster recovery without needing client intervention.

## **4. Circuit Breakers for Fail-Safe Retries**

If a service is persistently failing, blindly retrying can make things worse. Circuit breakers prevent cascading failures.

**Example: Using Resilience4J Circuit Breaker**

```
CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("rsocketCircuitBreaker");

RSocketRequester requester = RSocketRequester.builder()
    .rsocketConnector(connector -> connector.addRequesterPlugin(CircuitBreakerOperator.of(circuitBreaker)))
    .transport(TcpClientTransport.create("localhost", 7000));
Mono<String> response = requester.route("fetch.data")
    .retrieveMono(String.class)
    .transformDeferred(CircuitBreakerOperator.of(circuitBreaker)) // Apply circuit breaker
    .onErrorResume(ex -> Mono.just("Fallback Response"));
```

**How It Works:**

- Opens the circuit if too many failures happen in a short time.
- Rejects new requests temporarily until the system stabilizes.
- Automatically resets after a cool-down period.

## **6. Can RSocket work in a serverless environment (AWS Lambda, Google Cloud Functions)?**

Yes, RSocket can work in a serverless environment (AWS Lambda, Google Cloud Functions), but there are several challenges due to the nature of serverless architectures.

## **Challenges:**

Unlike traditional long-lived servers, serverless functions are:1. **Stateless** → They start and stop on demand, making it difficult to maintain persistent RSocket connections.2. **Cold Starts** → There is a delay when the function is invoked after being idle, which affects real-time interactions.3. **Limited Execution Time** → Some serverless platforms impose timeouts (e.g., AWS Lambda has a max timeout of 15 minutes), which may disrupt long-lived streams.

## **How to Make RSocket Work in Serverless:**

You can still use RSocket in a serverless-friendly way by adopting the following approaches:

## **1. Client-Initiated Connections (Fire and Forget)**

Instead of keeping a persistent connection from the serverless function, let the client initiate requests and use `fireAndForget()` or `requestResponse()` modes.

**Example: AWS Lambda as an RSocket Server**

```
@MessageMapping("process.data")
public Mono<Void> processData(String data) {
    return Mono.fromRunnable(() -> {
        // Serverless function processing logic
        System.out.println("Processing: " + data);
    });
}
```

**Why It Works?**

- Lambda receives a request, processes it, and exits quickly (aligning with stateless serverless behavior).

## **2. Using AWS API Gateway as a WebSocket Proxy**

Since RSocket works best over WebSockets, you can deploy it in AWS Lambda via API Gateway WebSocket support.

**Architecture:**

- Client ↔ AWS API Gateway (WebSockets) ↔ AWS Lambda
- API Gateway acts as a WebSocket bridge, forwarding messages to a Lambda function.

**Example: AWS Lambda Handler for WebSockets**

```
public class RSocketLambdaHandler implements RequestHandler<Map<String, Object>, APIGatewayProxyResponseEvent> {
    @Override
    public APIGatewayProxyResponseEvent handleRequest(Map<String, Object> event, Context context) {
        String body = event.get("body").toString();
        // Handle RSocket message
        System.out.println("Received: " + body);
        return new APIGatewayProxyResponseEvent().withStatusCode(200);
    }
}
```

**Why It Works:**

- API Gateway keeps the WebSocket connection alive, while Lambda processes messages only when needed.
- No need for long-lived connections inside Lambda.

## **3. Using an Always-On RSocket Server with Serverless Clients**

Instead of running RSocket on Lambda itself, deploy an always-on RSocket server (e.g., AWS Fargate, GCP Cloud Run) and let serverless functions connect to it on demand.

**Architecture:**

- RSocket Server: Runs in AWS Fargate (ECS) or Google Cloud Run (autoscalable).
- Serverless Clients: AWS Lambda or Google Cloud Functions connect to the RSocket server only when needed.

**Example: Lambda as an RSocket Client (Request-Response Mode)**

```
RSocketRequester requester = RSocketRequester.builder()
    .transport(WebsocketClientTransport.create("rsocket-server-url"));

public String fetchData() {
    return requester.route("fetch.data")
        .retrieveMono(String.class)
        .block(); // Blocking call since Lambda is short-lived
}
```

**Why It Works:**

- The server stays always-on, while serverless functions invoke it only when needed.
- Best for low-latency use cases.

#