# Spring Boot & Microservices — Interview Q&A

> Auto-extracted from the notes in [`02-microservices/`](../02-microservices/) by [`scripts/extract_qa.mjs`](../scripts/extract_qa.mjs).
> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.

**48 answered questions** · **29 question prompts without recorded answers**

---

## 1. What are the main challenges in implementing microservices?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

The main challenges I've encountered in microservices implementation include:

**Network Complexity & Latency:** Think of an e-commerce platform like Amazon. In a monolith, when you add an item to cart, everything happens in one application. But with microservices, the Cart Service needs to talk to Inventory Service, Product Service, and User Service over the network. Each network call adds latency and potential failure points.

**Distributed Data Management:** Imagine you're processing an order - you need to update inventory, create an order record, and charge the customer. In a monolith, this is one database transaction. With microservices, each service has its own database, so maintaining consistency becomes complex. You can't just rollback everything if one step fails.

**Service Discovery & Communication:** It's like managing a large shopping mall. Services need to find each other dynamically. If the Payment Service moves to a different server, how does the Order Service find it? You need service registries and load balancers.

**Monitoring & Debugging:** When a customer complains their order failed, in a monolith you check one log file. With microservices, that single request might have traveled through 8 different services. Tracing the issue becomes like detective work across multiple systems.

**Operational Complexity:** Instead of deploying one application, you're now deploying 20+ services. Each needs its own CI/CD pipeline, monitoring, scaling policies, and maintenance windows.

---

## 2. Explain the importance of containerization in microservices.

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Containerization is like having standardized shipping containers for global trade - it solves the fundamental problem of "it works on my machine."

**Key Benefits:**

**Environment Consistency:** Imagine you're running an e-commerce platform with 15 microservices:

- User Service (Python/Django)
- Product Service (Node.js)
- Payment Service (Java/Spring Boot)
- Inventory Service (Go)

Without containers, each service needs specific runtime versions, libraries, and configurations. Deploying to production becomes a nightmare of dependency conflicts.

With containers, each service bundles its runtime, dependencies, and configuration. Whether it runs on developer's laptop, staging, or production - it's identical.

**Resource Isolation:** Think of a busy shopping mall during Black Friday. Without containers, if the Search Service suddenly uses 90% CPU (due to high traffic), it could slow down the Payment Service running on the same server.

Containers provide isolation - each service gets its allocated resources and can't affect others.

**Scalability:** During flash sales, your Product Service might need 10 instances while User Service needs only 2. Containers make it easy to:

- Scale services independently
- Deploy quickly (containers start in seconds)
- Move services between servers

**Development Velocity:** New developers can run the entire e-commerce platform locally with one command:

`docker-compose up`

No need to install 5 different runtimes, databases, and configure ports.

**Technology Diversity:** Your team can choose the best tool for each job - Python for ML recommendations, Go for high-performance APIs, Node.js for real-time features - all running seamlessly together.

---

## 3. How do you approach logging and monitoring in a microservices environment?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Logging and monitoring in microservices is like managing a large restaurant chain - you need visibility into every location while maintaining overall business health.

**Centralized Logging Approach:**

**Challenge:** In an e-commerce system, when a customer reports "my order failed," that single request might touch:

- API Gateway → User Service → Order Service → Inventory Service → Payment Service

Without proper logging, you'd need to check logs on 5 different servers.

**Solution - ELK Stack (Elasticsearch, Logstash, Kibana):**

**Structured Logging**

: Each service logs in JSON format with consistent fields

```jsx
{
  "timestamp": "2024-01-15T10:30:00Z",
  "service": "order-service",
  "traceId": "abc123",
  "level": "ERROR",
  "message": "Payment failed for order 12345",
  "userId": "user789"
}
```

- **Correlation IDs**: Every request gets a unique ID that follows it through all services
- **Centralized Collection**: All logs flow to Elasticsearch for searchable storage

Micrometer  Tracing

**Monitoring Strategy:**

**Application Metrics:**

- **Business Metrics**: Orders per minute, conversion rates, revenue
- **Technical Metrics**: Response times, error rates, throughput

**Infrastructure Metrics:**

- CPU, memory, disk usage per service
- Database connection pools
- Queue depths

**Practical Implementation:**

- **Prometheus + Grafana**: For metrics collection and visualization
- **Health Check Endpoints**: Each service exposes `/health` endpoint
- **Circuit Breaker Monitoring**: Track when services are failing and recovering

**Alerting Rules:**

- Order Service error rate > 5%
- Payment Service response time > 2 seconds
- Inventory Service down for > 1 minute

**Real Example:** When Black Friday traffic hits, dashboards show:

- Search Service CPU spiking → Auto-scale triggers
- Database connection pool full → Alert ops team
- Payment gateway latency increasing → Switch to backup provider

---

## 4. How would you implement data consistency across microservices?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Data consistency in microservices is like coordinating a complex restaurant order across different kitchen stations - everything needs to work together even though each station operates independently.

**The Challenge:** Imagine an e-commerce order process:

1. Order Service creates order
2. Inventory Service reserves items
3. Payment Service charges customer
4. Shipping Service creates shipment

If payment fails after inventory is reserved, you need to "undo" the reservation. But services can't participate in a traditional database transaction.

**Saga Pattern Implementation:**

**Choreography-Based Saga (Event-Driven):**

```jsx
Order Created → Inventory Reserved → Payment Processed → Shipping Created
  ↓              ↓                 ↓                  ↓
Events        Events            Events            Events
```

Each service publishes events and listens for others. If Payment fails, it publishes "Payment Failed" event, and Inventory Service automatically releases the reservation.

**Orchestration-Based Saga:** A central Order Orchestrator manages the entire flow:

```jsx
Orchestrator → Call Inventory Service
→ Call Payment Service  
→ Call Shipping Service
```

If any step fails, the orchestrator handles compensating actions.

**Practical Implementation:**

**Event Sourcing + CQRS:** Instead of storing current state, store events:

```jsx
OrderCreated(orderId: 123, items: [...])
InventoryReserved(orderId: 123, items: [...])
PaymentProcessed(orderId: 123, amount: 299.99)
```

**Eventual Consistency:** Accept that data might be temporarily inconsistent. Show customers:

- "Order Confirmed" immediately
- "Payment Processing"
- "Order Shipped" when everything is complete

**Compensation Patterns:** For each action, define a compensating action:

- Reserve Inventory ↔ Release Inventory
- Charge Payment ↔ Refund Payment
- Create Shipment ↔ Cancel Shipment

**Real-World Example:** Amazon may reserve inventory during checkout before full payment is confirmed, using eventual consistency for some backend processes. If payment later fails, the order is canceled and the inventory is released.

---

## 5. What design patterns have you used while implementing microservices?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

I've used several key patterns, and I'll explain them with e-commerce examples:

**API Gateway Pattern:** Think of this as the reception desk at a large office building. Instead of customers directly calling 15 different services, they go through one entry point.

**Implementation:**

- Single endpoint: `api.ecommerce.com`
- Routes `/orders/*` to Order Service
- Routes `/products/*` to Product Service
- Handles authentication, rate limiting, request/response transformation

**Circuit Breaker Pattern:** Like electrical circuit breakers in your house - when there's overload, they trip to prevent damage.

**Real Example:** If Payment Service is down, instead of timing out every request:

- Circuit opens after 5 consecutive failures
- Returns cached "Payment temporarily unavailable"
- Periodically tests if service is back up
- Closes circuit when service recovers

**Bulkhead Pattern:** Like compartments in a ship - if one floods, others remain safe.

**Implementation:** Separate thread pools for different operations:

- 10 threads for product searches
- 5 threads for payment processing
- 3 threads for user authentication

If product search overloads, payment processing still works.

**Saga Pattern:** Already covered in data consistency - manages distributed transactions.

**Event Sourcing Pattern:** Store events instead of current state:

```jsx
Instead of: User(id: 123, email: "new@email.com")
Store: UserCreated, EmailChanged, EmailVerified
```

**CQRS (Command Query Responsibility Segregation):** Separate read and write operations:

- Write: Order Service handles order creation
- Read: Separate reporting database optimized for dashboards

**Strangler Fig Pattern:** Gradually replace monolith like a strangler fig plant:

- Route new features to microservices
- Gradually move existing features
- Eventually remove monolith

**Database per Service:** Each microservice owns its data:

- Order Service → Orders Database
- User Service → Users Database
- No cross-database queries

---

## 6. How do you handle inter-service communication in microservices?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Inter-service communication is like managing communication in a large organization - you need different methods for different situations.

**Synchronous Communication (REST/HTTP):**

**When to Use:** Real-time operations where you need immediate response.

**E-commerce Example:** When user clicks "Add to Cart":

```jsx
Frontend → API Gateway → Cart Service → Product Service (get price)
→ User Service (validate user)
```

**Implementation:**

```jsx
// Cart Service calls Product Service
const productResponse = await fetch(`${PRODUCT_SERVICE_URL}/products/${productId}`);
const product = await productResponse.json();
```

**Pros:** Simple, immediate consistency **Cons:** Creates tight coupling, cascading failures

**Asynchronous Communication (Message Queues):**

**When to Use:** Operations that don't need immediate response or involve multiple services.

**E-commerce Example:** When order is placed:

```jsx
Order Service → Publishes "OrderCreated" event
→ Inventory Service (reduces stock)
→ Email Service (sends confirmation)  
→ Analytics Service (updates metrics)
```

**Implementation with RabbitMQ/Kafka:**

```jsx
// Publisher (Order Service)
await messageQueue.publish('order.created', {
  orderId: 123,
  userId: 456,
  items: [...]
});

// Subscriber (Inventory Service)
messageQueue.subscribe('order.created', async (orderEvent) => {
  await reduceInventory(orderEvent.items);
});
```

**gRPC for Internal Communication:**

**When to Use:** High-performance internal communication between services.

**Benefits:**

- Binary protocol (faster than JSON)
- Strong typing with Protocol Buffers
- Built-in load balancing

**Service Discovery:**

**Netflix Eureka/Consul:** Services register themselves and discover others:

```jsx
// Service registration
serviceRegistry.register({
  name: 'order-service',
  host: '192.168.1.10',
  port: 8080,
  health: '/health'
});

// Service discovery
const orderServiceUrl = await serviceRegistry.discover('order-service');
```

**Real-World Implementation Strategy:**

- **Critical path:** Synchronous (user registration, payment)
- **Background tasks:** Asynchronous (email notifications, analytics)
- **Internal APIs:** gRPC for performance
- **External APIs:** REST for simplicity

---

## 7. What are different deployment strategies for microservices?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Deployment strategies in microservices are like different ways to renovate a busy shopping mall - you need to keep business running while making improvements.

**Blue-Green Deployment:**

**Concept:** Maintain two identical production environments - Blue (current) and Green (new version).

**E-commerce Example:** You're updating the Order Service:

- Blue environment: Current Order Service v1.2 (handling live traffic)
- Green environment: New Order Service v1.3 (deployed but no traffic)
- Switch traffic from Blue to Green instantly
- Keep Blue as rollback option

**Implementation:**

```jsx
# Load balancer configuration
upstream order-service {
    server blue-order-service:8080;  # Current version
    # server green-order-service:8080;  # New version (commented out)
}
```

---

## 8. Compare Results

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- Use dashboards (Grafana, Google Analytics, custom BI)
- Decide which version performs better

---

## 9. How do you approach database design in a microservices architecture?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Database design in microservices is like organizing a large library system - each department needs its own specialized collection, but they still need to share information efficiently.

**Database per Service Pattern:**

**Principle:** Each microservice owns its data and database schema.

**E-commerce Example:**

```jsx
User Service → PostgreSQL (user profiles, authentication)
Order Service → MongoDB (order documents, flexible schema)
Inventory Service → MySQL (ACID transactions for stock)
Analytics Service → ClickHouse (time-series data)
```

**Benefits:**

- Services can evolve independently
- Choose optimal database for each use case
- No cross-service database dependencies

**Data Sharing Strategies:**

**API-Based Data Access:**

```jsx
// Order Service needs user email
const user = await userService.getUser(userId);
const order = {
  userId: userId,
  userEmail: user.email, // Cache locally
  items: items
};
```

**Event-Driven Data Synchronization:**

When user updates email:

```jsx
User Service → Publishes "UserEmailChanged" event
→ Order Service updates cached email
→ Notification Service updates email
```

**Data Consistency Patterns:**

**Eventual Consistency:** Accept temporary inconsistency for better performance.

**Example:**

- User changes address
- Order Service might show old address for few seconds
- Eventually syncs with new address

**Saga Pattern for Distributed Transactions:** Already covered - ensures data consistency across services.

**Shared Database Anti-Pattern:**

**What NOT to do:**

```jsx
Order Service ←→ Shared Database ←→ Inventory Service
```

**Problems:**

- Tight coupling between services
- Schema changes affect multiple services
- Difficult to scale independently

**CQRS Implementation:**

**Command Side (Write):**

**CQRS Implementation:**

**Command Side (Write):**

```jsx
Order Service → Orders Write Database (optimized for writes)
```

**Query Side (Read):**

```jsx
Order Reporting → Orders Read Database (optimized for reporting)
```

**Data synchronization via events.**

**`Practical Considerations:**

**Reference Data:** Some data is shared across services (countries, currencies):

- **Option 1:** Duplicate in each service
- **Option 2:** Shared reference data service
- **Option 3:** Configuration management

**Reporting and Analytics:** Create dedicated reporting databases:

```jsx
All Services → Event Stream → Data Warehouse → Analytics
```

---

## 10. How do you implement service versioning in a microservices architecture?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Service versioning in microservices is like managing different versions of mobile apps - you need to support old versions while introducing new features.

**URL-Based Versioning:**

**Implementation:**

```jsx
/api/v1/orders  → Order Service v1
/api/v2/orders  → Order Service v2
```

**E-commerce Example:**

- v1: Returns basic order info
- v2: Adds tracking information and estimated delivery

**Code Example:**

```jsx
// API Gateway routing
app.use('/api/v1/orders', orderServiceV1Router);
app.use('/api/v2/orders', orderServiceV2Router);

// Controller
async function getOrder(req, res) {
  const order = await orderService.getOrder(req.params.id);
  
  if (req.baseUrl.includes('v2')) {
    // v2 includes tracking info
    order.tracking = await trackingService.getTracking(order.id);
  }
  
  res.json(order);
}
```

**Header-Based Versioning:**

**Implementation:**

```jsx
// Client request
fetch('/api/orders', {
  headers: {
    'Accept': 'application/vnd.ecommerce.v2+json'
  }
});

// Service handling
app.use((req, res, next) => {
  const acceptHeader = req.headers.accept;
  req.apiVersion = acceptHeader.includes('v2') ? 'v2' : 'v1';
  next();
});
```

**Contract-First Approach:**

**API Contract Definition (OpenAPI):**

```jsx
# orders-api-v2.yaml
paths:
  /orders/{id}:
    get:
      summary: Get order details
      parameters:
        - name: include_tracking
          in: query
          schema:
            type: boolean
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderV2'
```

**Backward Compatibility Strategies:**

**Additive Changes (Safe):**

- Add new optional fields
- Add new endpoints
- Add new query parameters

**Breaking Changes (Requires new version):**

- Remove fields
- Change field types
- Change endpoint behavior

**Deprecation Strategy:**

**Phased Approach:**

1. **Announce deprecation:** v1 will be deprecated in 6 months
2. **Support both versions:** Run v1 and v2 in parallel
3. **Monitor usage:** Track which clients use v1
4. **Migrate clients:** Work with teams to upgrade
5. **Retire old version:** Turn off v1 after migration

**Service Evolution Patterns:**

**Expand and Contract:**

```jsx
Phase 1: Add new field (both versions supported)
Phase 2: Migrate clients to use new field  
Phase 3: Remove old field
```

**Adapter Pattern:**

```jsx
class OrderV1Adapter {
  adapt(orderV2) {
    return {
      id: orderV2.id,
      total: orderV2.total,
      // Convert v2 format to v1 format
      items: orderV2.lineItems.map(item => ({
        productId: item.product.id,
        quantity: item.qty
      }))
    };
  }
}
```

**Consumer-Driven Contracts:**

**Testing Approach:**

```jsx
// Consumer (Frontend) defines contract
const orderContract = {
  request: {
    method: 'GET',
    path: '/orders/123'
  },
  response: {
    status: 200,
    body: {
      id: '123',
      total: 299.99,
      status: 'confirmed'
    }
  }
};

// Provider (Order Service) must satisfy contract
```

---

## 11. Describe approaches to handle authentication and authorization across microservices.

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Authentication and authorization in microservices is like managing security in a large office building - you need one entry point for identity verification, but different access levels for different departments.

**JWT (JSON Web Token) Approach:**

**Flow:**

1. User logs in → Authentication Service issues JWT
2. JWT contains user info and permissions
3. Each microservice validates JWT independently

**E-commerce Example:**

```jsx
// JWT payload
{
  "userId": "12345",
  "email": "user@example.com",
  "roles": ["customer", "premium"],
  "permissions": ["view_orders", "create_orders"],
  "exp": 1640995200
}

// Order Service validates JWT
const jwt = require('jsonwebtoken');

function validateJWT(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

// Check permissions
function requirePermission(permission) {
  return (req, res, next) => {
    if (req.user.permissions.includes(permission)) {
      next();
    } else {
      res.status(403).json({ error: 'Insufficient permissions' });
    }
  };
}

// Usage
app.get('/orders', validateJWT, requirePermission('view_orders'), getOrders);
```

**OAuth 2.0 with API Gateway:**

**Architecture:**

```jsx
Client → API Gateway (OAuth validation) → Microservices
```

**Implementation:**

```jsx
// API Gateway middleware
async function validateOAuth(req, res, next) {
  const token = req.headers.authorization;
  
  // Validate with OAuth server
  const userInfo = await oauthServer.introspect(token);
  
  if (userInfo.active) {
    req.user = userInfo;
    next();
  } else {
    res.status(401).json({ error: 'Invalid token' });
  }
}
```

**Service-to-Service Authentication:**

**Mutual TLS (mTLS):** Each service has certificates for secure communication.

**Service Account Tokens:**

```jsx
// Order Service calling Inventory Service
const serviceToken = await getServiceAccountToken();

const response = await fetch('http://inventory-service/check-stock', {
  headers: {
    'Authorization': `Bearer ${serviceToken}`,
    'X-Service-Name': 'order-service'
  }
});
```

**Role-Based Access Control (RBAC):**

**E-commerce Roles:**

```jsx
const roles = {
  customer: ['view_orders', 'create_orders', 'view_products'],
  admin: ['*'], // All permissions
  support: ['view_orders', 'update_order_status'],
  warehouse: ['view_inventory', 'update_inventory']
};

// Permission checking
function hasPermission(userRoles, requiredPermission) {
  return userRoles.some(role => 
    roles[role].includes(requiredPermission) || 
    roles[role].includes('*')
  );
}
```

**Fine-Grained Authorization:**

**Attribute-Based Access Control (ABAC):**

```jsx
// Policy: Users can only view their own orders
function canViewOrder(user, orderId) {
  return user.id === order.userId || user.roles.includes('admin');
}

// Policy: Premium users can access expedited shipping
function canAccessExpedited(user) {
  return user.subscription === 'premium';
}
```

**Session Management:**

**Distributed Session Store:**

```jsx
// Redis-based session store
const session = await redis.get(`session:${sessionId}`);

if (session) {
  req.user = JSON.parse(session);
  // Extend session expiry
  await redis.expire(`session:${sessionId}`, 3600);
}
```

**Security Best Practices:**

**Token Rotation:**

```jsx
// Refresh token mechanism
app.post('/refresh-token', async (req, res) => {
  const refreshToken = req.body.refreshToken;
  
  if (await validateRefreshToken(refreshToken)) {
    const newAccessToken = generateAccessToken(user);
    const newRefreshToken = generateRefreshToken(user);
    
    res.json({
      accessToken: newAccessToken,
      refreshToken: newRefreshToken
    });
  }
});
```

**Rate Limiting by User:**

```jsx
// Per-user rate limiting
const rateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: (req) => {
    return req.user.subscription === 'premium' ? 1000 : 100;
  },
  keyGenerator: (req) => req.user.id
});
```

**Audit Logging:**

```jsx
// Track all access attempts
function auditLog(req, res, next) {
  console.log({
    timestamp: new Date().toISOString(),
    userId: req.user?.id,
    action: `${req.method} ${req.path}`,
    ip: req.ip,
    userAgent: req.headers['user-agent']
  });
  next();
}
```

This comprehensive approach ensures secure, scalable authentication and authorization across your microservices architecture while maintaining good user experience and operational efficiency.

---

## 12. Question 1: What are the main drawbacks of using synchronized methods?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Using `synchronized` methods in Java is the simplest way to handle thread-safety, but it comes with some important drawbacks:

1. **No Flexibility**:
    
    `synchronized` is a blocking mechanism with no built-in support for advanced control like try-lock or timed lock attempts. You can't try acquiring a lock without getting stuck.
    
2. **Can't Interrupt**:
    
    If a thread is waiting for a lock via `synchronized`, it cannot be interrupted. This limits responsiveness in multi-threaded applications.
    
3. **No Fairness or Priority Handling**:
    
    There's no way to control the order in which threads acquire the lock—leading to potential starvation.
    
4. **Coarse-Grained Locking**:
    
    It can sometimes lead to unnecessary locking if the scope is too wide (e.g., locking an entire method).
    
5. **No Condition Support**:
    
    You can't use multiple condition variables or fine-grained signaling like `await()`, `signal()`, or `signalAll()` which are useful in complex thread coordination.
    

---

---

## 13. Question 2: How does ReentrantLock improve performance and flexibility?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

`ReentrantLock` from `java.util.concurrent.locks` improves over `synchronized` in several ways:

1. **Try and Timeout**:
    
    You can attempt to acquire the lock using `tryLock()` or `tryLock(timeout)` — improving responsiveness and avoiding deadlock.
    
2. **Interruptibility**:
    
    Threads waiting on a `ReentrantLock` can be interrupted using `lockInterruptibly()`.
    
3. **Fairness**:
    
    It supports **fair locking**, meaning threads acquire the lock in the order they requested it (FIFO), avoiding starvation.
    
4. **Multiple Conditions**:
    
    Supports multiple `Condition` objects for more granular signaling between threads, improving complex thread interactions.
    
5. **Explicit Locking**:
    
    Since locking and unlocking are explicit (`lock()` / `unlock()`), developers have more control over synchronization scope.
    

---

---

## 14. How would you design an API Gateway to handle dynamic routing and security policies?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

To design a robust **API Gateway** with **dynamic routing** and **security policy enforcement**, I'd follow a microservices-friendly and scalable approach:

---

## 15. What are the challenges of handling pagination in REST APIs for massive datasets?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

When handling **pagination at scale**, especially with **millions of records**, several challenges arise:

---

## 16. How would you manage API timeouts and retries in a distributed system?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

In a distributed system, **timeouts and retries** are critical for reliability and resilience. Here's how I approach them:

---

## 17. What’s the best way to implement WebSockets in a fintech application?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

WebSockets are great for **real-time updates** like trades, balances, or FX rates in fintech. Here's how I’d implement them securely and at scale:

---

## 18. How would you enforce idempotency in payment APIs?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Idempotency is crucial in fintech to **avoid duplicate payments** during retries. Here's how I enforce it:

---

## 19. Design a high-throughput, low-latency order-matching system for a stock exchange

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

A **stock exchange order-matching engine** must be ultra-fast and highly reliable. Here’s a breakdown of how I’d approach it:

---

---

## 20. How would you ensure data integrity in a multi-region database setup?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Multi-region databases are essential for global availability, but they introduce complexity in maintaining consistency. Here's how I'd ensure **data integrity**:

---

---

## 21. Write Fencing & Versioning:

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- Use **optimistic locking / version numbers** to prevent stale writes.
- Enforce **linearizability** in critical paths (e.g., balance updates, orders).

---

---

## 22. Want to go next level?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

You can offer to sketch out:

- **Order-matching pseudocode using TreeMap in Java**
- A **multi-region write-safe schema design** (e.g., user wallet or payment ledger)
- Or even talk about **Paxos vs Raft** if asked about consensus protocols

---

Let me know if you want diagrams, code samples, or to simulate a real interview whiteboard session.

---

## 23. Explain Leader Election. How would you implement it in a microservices-based system?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

**Leader Election** is the process of designating one node (service instance) as the **"coordinator" or "primary"**, responsible for certain tasks (e.g., scheduling, resource locking, background jobs) while others stay passive or standby.

---

---

## 24. What are the trade-offs between CQRS and traditional CRUD systems?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

CQRS (Command Query Responsibility Segregation) **separates read and write models**, while traditional CRUD merges them in a single model.

---

---

## 25. How does a Distributed Message Queue like Kafka handle backpressure?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Backpressure happens when **producers push faster than consumers can process**. Kafka handles it via **built-in flow control + buffering**.

---

---

## 26. What is a Deadlock?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Occurs when two or more threads hold locks and wait for each other in a **circular dependency**, causing all to freeze.

---

---

## 27. Why a Hash Map?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

1. **Flexibility**:
    - **Hash Maps** provide **O(1)** average-time complexity for **insertion**, **deletion**, and **lookup** operations.
    - You can use **hash maps** to implement complex data structures:
        - **Sets**: By using the hash map's keys, you can simulate sets.
        - **Stacks/Queues**: Using keys for indices, you can implement a stack or queue with custom logic.
        - **Graphs**: You can represent a graph by using hash maps to store adjacency lists.
2. **Real-World Use Cases**:
    - **Caching**: A hash map is ideal for implementing **LRU (Least Recently Used)** caches where you store recently accessed data.
    - **Counting and Frequency**: You can use hash maps for counting occurrences of elements in a stream, such as counting words in a document or tracking elements in an inventory system.
    - **Mapping**: Any problem involving a **key-value pair** is perfectly suited for a hash map, including database indexing, configuration settings, and managing users with unique identifiers.
3. **Adaptability**:
    - With a **HashMap**, you can build other abstract data structures and adapt to various problem types (e.g., adjacency lists for graphs, frequency counters, etc.).

---

---

## 28. Why Remove Checked Exceptions?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

1. **Excessive Boilerplate**:
    - Java forces developers to handle checked exceptions, leading to unnecessary `try-catch` blocks and the need to declare exceptions in method signatures, which can clutter the code.
2. **Readability**:
    - Checked exceptions often obscure the logic of the program and make it harder to follow. Unchecked exceptions, on the other hand, allow the developer to focus on the actual business logic.
3. **Overuse**:
    - Developers sometimes overuse checked exceptions for cases that could be handled more cleanly with runtime exceptions or other error-handling approaches.
4. **Alternative Approaches**:
    - Languages like **Scala** and **Kotlin** (which runs on the JVM) don’t enforce checked exceptions and offer more flexible error-handling strategies, leading to cleaner code.
    - Java has introduced alternatives like **`Optional`**, **`CompletableFuture`**, and **`Result`**, which can make error handling more graceful and functional.

---

---

## 29. What is a Circuit Breaker?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- A circuit breaker acts like an electrical circuit breaker in the physical world. It detects failures in a system, "opens" (stops sending requests to a failing service), and prevents further strain on the service, giving it time to recover.
- Once the service becomes healthy again, the circuit breaker "closes" and starts accepting requests.

**The typical behavior of a circuit breaker involves three states:**

1. **Closed**: The circuit is closed by default, meaning requests are flowing to the service. The circuit breaker monitors the service for failures.
2. **Open**: If the failure threshold is reached (e.g., multiple failed requests), the circuit breaker opens, and no further requests are sent to the service until it's deemed healthy again.
3. **Half-Open**: After a configured recovery time, the circuit breaker allows a limited number of requests to go through to test if the service has recovered. If the requests succeed, the circuit breaker closes. If they fail, it remains open.

---

## 30. Why Use Circuit Breakers?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- **Prevent System Collapse**: When one service fails, it can trigger a cascade of failures across other services. Circuit breakers prevent this by isolating the failing service.
- **Improve Resilience**: They allow the system to gracefully degrade by providing **fallback mechanisms** (e.g., returning cached data or default responses).
- **Manage Dependencies**: Services can avoid overloading a downstream service that is experiencing issues.

---

## 31. How It Works:

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- **Sending Messages**: A verticle can send a message to the event bus using `eventBus.send(address, message)`. The message can be any serializable object.
- **Receiving Messages**: A verticle can register a handler to receive messages from an address using `eventBus.consumer(address, handler)` for subscription-based communication.
- **Example**:
    
    ```java
    // Sending a message to an address
    vertx.eventBus().send("my.address", "Hello!");
    
    // Receiving the message on a different verticle
    vertx.eventBus().consumer("my.address", message -> {
        System.out.println("Received message: " + message.body());
    });
    
    ```

---

## 32. How would you use Vert.x reactive programming to handle high-concurrency tasks?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

**Interview-Ready Answer:**

> “Vert.x uses a reactive, non-blocking model that allows handling high-concurrency tasks on a small number of threads through its event loop and Reactive APIs like RxJava, Mutiny, or Reactor.
> 

Here's how I would use Vert.x for high-concurrency:

🔹 **Verticles & Event Loop**:

I would split my logic into **verticles**—each component runs on a dedicated event loop. Since Vert.x uses very few threads (e.g., 2 * number of CPU cores), I’d avoid blocking calls and offload those to worker verticles.

🔹 **Reactive Programming**:

Using **Vert.x RxJava** or **Mutiny** extensions, I can compose async calls like DB queries, HTTP calls, and file reads using `flatMap`, `zip`, or `onItem().transform()`—this makes my code composable and clean.

🔹 **Backpressure-aware**:

Reactive streams like `Flowable` (RxJava) help control backpressure when dealing with large streaming data like live feeds or telemetry.

🔹 **Real Example**:

```java
eventBus.consumer("process.data", message -> {
    myReactiveService.processData(message.body())
        .subscribe(result -> {
            message.reply(result);
        }, err -> {
            message.fail(500, err.getMessage());
        });
});

```

By avoiding thread-per-request and using **reactive chains**, Vert.x handles **tens of thousands** of concurrent events efficiently on minimal threads.”

---

---

## 33. Explain how Vert.x handles non-blocking I/O and why it’s beneficial.

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

**Interview-Ready Answer:**

> “Vert.x is built on top of Netty, which is a high-performance NIO (Non-blocking I/O) framework. It uses a single-threaded event loop model where each thread handles multiple connections without blocking.
> 

🔸 **How It Works**:

- Incoming requests/events are queued in the **event loop**.
- Instead of blocking the thread waiting for I/O (e.g., DB, file, HTTP), Vert.x uses **callbacks** or **futures/promises** to resume execution when the operation completes.

🔸 **Why It’s Beneficial**:

1. **Massive concurrency**: You don’t need 1 thread per connection. One thread can handle thousands of sockets.
2. **Scalability**: Reduced context switching and memory overhead lead to better performance under high load.
3. **Resilience**: Since threads are never blocked, the system remains responsive even under peak load.

🔸 **Example**:

```java
webClient.get(8080, "localhost", "/data")
    .send()
    .onSuccess(response -> {
        // non-blocking response processing
    });

```

In summary, **non-blocking I/O** in Vert.x means **fewer threads, better throughput**, and **cost-efficient scaling**—making it ideal for microservices and real-time apps.”

---

---

## 34. How would you implement a distributed task scheduler using Vert.x and Redis?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

**Interview-Ready Answer:**

> “To implement a distributed task scheduler using Vert.x and Redis, I’d combine Vert.x’s Timer APIs with Redis locks to ensure only one instance processes a scheduled job in a cluster.
>

---

## 35. How would you design a rate-limiting mechanism for a public API?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “To protect a public API from abuse and ensure fair usage, I’d design a rate-limiting system using a distributed in-memory store like Redis, implementing an algorithm like Token Bucket or Leaky Bucket.”
> 

---

---

## 36. Why Redis?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

- **Distributed**: Works across multiple nodes/services.
- **Fast**: Sub-millisecond reads/writes.
- **Atomic**: Use Lua scripts for consistent updates.

---

---

## 37. What’s the difference between synchronous and asynchronous APIs?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “The difference lies in how the request is handled and when the client receives the response.”
> 

---

---

## 38. How would you design a payment gateway to handle high traffic?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “Designing a payment gateway for high traffic involves availability, idempotency, security, and low latency. I'd break it down into modular, resilient microservices with asynchronous processing and strong consistency where required.”
> 

---

---

## 39. Explain the role of message queues like Kafka or RabbitMQ in a distributed system.

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “Message queues like Kafka or RabbitMQ decouple producers and consumers in a distributed system, improving scalability, resilience, and asynchronous processing.”
> 

---

---

## 40. How would you troubleshoot a failing API in production?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “When an API fails in production, I follow a layered debugging approach — starting from monitoring, isolating the failure, and then deep-diving into logs, metrics, and dependencies.”
> 

---

---

## 41. How does event-driven architecture work with Kafka?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “In an event-driven architecture with Kafka, services communicate by publishing and consuming events instead of making direct API calls. This leads to loose coupling, scalability, and async workflows.”
> 

---

---

## 42. Redis vs. Memcached: Which one do you pick for caching, and why?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “I’d pick Redis for most real-world systems due to its rich data structures, persistence options, and pub/sub support.”
> 

---

---

## 43. How do you monitor and troubleshoot issues in a microservices architecture?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

> “Monitoring in microservices is all about observability — logs, metrics, and traces. I use a combination of centralized tools and standardized practices.”
> 

---

---

## 44. Where Have I Used Immutable Objects?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

1. **In multi-threaded applications**:
    - **Example**: In a multi-threaded environment, I used immutable objects to represent shared data that would be read by multiple threads but not modified by them. For instance, an immutable `Person` object could be used to ensure thread-safety without the need for synchronization when shared between threads.
2. **In Java Collections**:
    - **Example**: I have often used immutable objects as keys in `HashMap` and `HashSet` because their state remains constant, ensuring consistent behavior in these hash-based collections. I used immutable classes to represent data that should not change after it's inserted into the collection.
3. **In functional programming**:
    - **Example**: While working with functional programming paradigms in Java, I used immutable objects to represent values that could not be changed once created. This was particularly useful when implementing things like value objects and working with streams.
4. **In financial systems**:
    - **Example**: In a financial application, I used immutable objects to represent entities like `Transaction` or `Account`, where the values of certain fields should not be altered after creation to ensure the integrity of the data.
5. **In caching**:
    - **Example**: In a caching layer, I used immutable objects for cache entries to ensure that once an object is put in the cache, its state doesn't change. This ensured the consistency of the cache across various components in the system.

---

In summary, immutable objects are a great way to enforce consistency, avoid bugs related to state changes, and improve thread safety in Java applications. They are useful in various scenarios like multi-threading, functional programming, and when designing stable data models.

---

## 45. Which One Fits Better in Which Situation?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

1. **When to Use `String`:**
    - When the string's value doesn’t change.
    - For string literals, constants, or when you don’t need to modify the string after it is created.
    - When immutability is important (e.g., hashmaps with `String` keys, string constants in Java).
    - Example: `String str = "Hello";`
2. **When to Use `StringBuilder`:**
    - When you need to build or modify strings in a single-threaded environment, especially in loops or when performing a lot of concatenation.
    - Best for performance when dealing with string concatenation in scenarios where thread safety is not a concern.
    - Example: Building an HTML document or CSV string in a loop.
3. **When to Use `StringBuffer`:**
    - When you need a mutable string in a multi-threaded environment and thread safety is a concern.
    - Suitable for cases where multiple threads are modifying the string, such as when different threads are working on parts of a string concurrently.
    - Example: Logging systems where multiple threads are concurrently appending logs.

---

---

## 46. What is the synchronized keyword in Java?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

In Java, the `synchronized` keyword is used to ensure that only one thread can access a particular block of code or method at a time, providing **mutual exclusion** and ensuring **thread safety**. When a method or block is marked as `synchronized`, the thread holds a **lock** on the object or class it is synchronized on, preventing other threads from entering the synchronized section of code until the lock is released.

---

## 47. How does the synchronized keyword affect performance?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

Yes, using the `synchronized` keyword can affect performance, and here's how:

---

## 48. How to mitigate performance issues with synchronized?

*Source: [`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

1. **Reduce Lock Contention**: Minimize the scope of synchronized code to reduce the amount of time each thread holds the lock. Use synchronized blocks instead of synchronizing entire methods when possible.
2. **Use Fine-Grained Locks**: Instead of synchronizing on a large shared object, use multiple locks for smaller, independent sections of code. This allows multiple threads to access different parts of the code concurrently.
3. **Use `java.util.concurrent` Classes**: Java provides concurrency utilities like `ReentrantLock`, `ReadWriteLock`, `Semaphore`, and `Atomic variables` in the `java.util.concurrent` package, which provide more advanced and flexible control over thread synchronization. These can sometimes offer better performance compared to the basic `synchronized` keyword.
4. **Avoid Locking on Heavy Resources**: If possible, avoid synchronizing methods that perform I/O or network operations, as these tend to be slow operations. You can use separate locks for different resources to avoid bottlenecks.
5. **Minimize Shared Data**: Reduce the amount of shared data between threads, as synchronization is mostly required to access shared mutable state. Using immutable objects can reduce the need for synchronization.

---

---

## Question bank (no recorded answers)

Prompts collected from the notes that have no written answer yet:

- If Java didn’t have the synchronized keyword, how would you implement thread safety? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- How would you store a billion records in memory while ensuring efficient search operations? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Explain Java’s ClassLoader in a way that a 10-year-old could understand. — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- What exactly happens inside the JVM when a NullPointerException is thrown? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Design a Traffic Management System for a City with Self-Driving Cars — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- If You Had to Reduce API Response Time by 50% in a Large-Scale System, Where Would You Start? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- How would you design a video streaming platform that adapts in real-time to network conditions? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Can you sort an array faster than O(n log n)? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- You have an infinite stream of numbers. How would you efficiently find the median at any point? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- If you could only use one data structure for every problem, which one would it be and why? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- How would you explain recursion to someone who has never coded before? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- If you could remove one feature from Java, what would it be and why? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Tell me something interesting about technology that isn’t on your resume. — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- How would you debug a memory leak in a production Java application? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Explain CAP theorem and its relevance to distributed systems. — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Explain circuit breakers and how you’d implement them using Hystrix in a microservices architecture. — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- How does the Vert.x Event Bus work for inter-component communication? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- What’s the difference between Vert.x and traditional blocking frameworks like Spring Boot? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Why Use Message Queues? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- When to Use Which? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Bulkhead pattern (to isolate thread pools)? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Distributed tracing with Sleuth + Zipkin? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Rate limiting combined with circuit breaking? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Why Two Heaps?: — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Is it global or region-specific? All users or one client? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Is a downstream service (like payment gateway, auth provider) failing? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Is the container or pod crashing (OOMKilled, high CPU)? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Is DB under heavy load or locked up? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*
- Any recent config changes or new deployments? — *[`02-microservices/microservices-interview-questions-for-3-years-exp.md`](../02-microservices/microservices-interview-questions-for-3-years-exp.md)*

