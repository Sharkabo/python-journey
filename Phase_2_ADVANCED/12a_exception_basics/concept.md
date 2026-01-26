# Unit 12a: Custom Exceptions

## 1. Creating Custom Exceptions
Create custom exception classes by inheriting from `Exception` to make error handling more specific.

**Syntax:**
```python
class CustomExceptionName(Exception):
    pass
```

**Example:**
```python
class ValidationError(Exception):
    pass

class NotFoundError(Exception):
    pass

class User:
    def __init__(self, age):
        if age < 0:
            raise ValidationError("Age cannot be negative")
        if age > 150:
            raise ValidationError("Age is unrealistic")
        self.age = age

try:
    user = User(-5)
except ValidationError as e:
    print(e)  # Age cannot be negative
```

---

## Spiral Learning Note
Custom exceptions make error handling more specific and clear. Next you'll learn patterns for adding data to exceptions.
