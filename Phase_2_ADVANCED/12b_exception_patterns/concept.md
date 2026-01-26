# Unit 12b: Exception Patterns

## 1. Exceptions with Data
Store extra data in custom exceptions for better debugging and error handling.

**Syntax:**
```python
class CustomError(Exception):
    def __init__(self, message, extra_data):
        self.extra_data = extra_data
        super().__init__(message)
```

**Example:**
```python
class APIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

class NotFoundError(APIError):
    def __init__(self, resource_type, resource_id):
        self.resource_type = resource_type
        self.resource_id = resource_id
        super().__init__(404, f"{resource_type} {resource_id} not found")

try:
    raise APIError(500, "Server Error")
except APIError as e:
    print(f"Status: {e.status_code}")
    print(f"Message: {e.message}")

try:
    raise NotFoundError("User", 123)
except NotFoundError as e:
    print(f"{e.status_code}: {e.message}")
    # 404: User 123 not found
```

---

## Spiral Learning Note
Unit 12a taught creating custom exceptions. Now you add data to them for better debugging. This pattern is common in web frameworks like FastAPI.
