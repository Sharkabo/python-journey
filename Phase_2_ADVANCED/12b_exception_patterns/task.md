# Task Description

**Scenario: The Smart API Error Handler**

On the backend of a web API, exceptions happen all the time (Not Found, validation errors, permission denied). You want to centralize how these are handled. Instead of just passing a string message, your exceptions should carry "metadata" like standard HTTP error codes (404, 403, 500) so the API knows what to send back to the frontend.

**Your Goal:**
Create a "Rich" exception class that carries both a message and an error code, and build a central handler that processes them.

**Objectives:**
1.  Create `AppError(Exception` that accepts `message` and `code`. Store them as attributes.
2.  Create subclasses:
    - `NotFoundError` (defaults code to 404).
    - `NotAuthorizedError` (defaults code to 403).
3.  Create a "fake database" function `get_user(user_id)`:
    - Raise `NotFoundError(f"User {user_id} missing")` if user_id is 999.
    - Raise `NotAuthorizedError("You are banned")` if user_id is 666.
    - Return a user dict otherwise.
4.  **The Handler:** Write a `process_request(user_id)` function that wraps the call in a `try...except`.
    - It should catch `AppError` (the base class).
    - It should print a JSON-like formatted error: `{"error": "User 999 missing", "code": 404}`.

**Success Condition:**
Calling `process_request(999)` should output the structured 404 error. Calling `process_request(666)` should output the 403 error. The handler code should only have ONE except block that handles both cases dynamically.
