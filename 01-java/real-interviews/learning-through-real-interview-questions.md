# Learning through real interview questions

### ✅ **Best Practices for Writing Good APIs**

1. **Use DTOs (Data Transfer Objects)**
    - Avoid exposing database entity classes directly.
    - Protects internal structure and prevents tight coupling between layers.
2. **Version Your APIs (v1, v2, ...)**
    - Ensure backward compatibility.
    - Avoid breaking changes for existing clients.
3. **Use Meaningful Status Codes**
    - Don’t rely only on `200 OK` or `500 Internal Server Error`.
    - Examples:
        - `201 Created` → When a resource is created.
        - `204 No Content` → When there's no content to return.
        - `400 Bad Request` → For invalid inputs.
        - `404 Not Found` → Resource doesn’t exist.
        - `409 Conflict` → Conflict in data or request.
4. **Implement Idempotency in POST APIs**
    - Prevent duplicate processing on retries.
    - Use unique request identifiers or tokens.
5. **Centralized Validation & Exception Handling**
    - Handle exceptions uniformly (`@ControllerAdvice` in Spring Boot).
    - Avoid exposing stack traces or sensitive internal errors to clients.
6. **Logging with Context**
    - Include contextual information like `requestId` and `userId`.
    - Helps in debugging, especially in distributed systems.
    

**7 Security by Default**

- Use secure authentication methods like JWT or OAuth2.
- Avoid passing sensitive data in URL parameters.