# Unit 07b: Decorators with Arguments

## 1. Decorators with Function Arguments
Decorators need to handle function parameters using *args and **kwargs.

**Syntax:**
```python
from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Code before
        result = func(*args, **kwargs)
        # Code after
        return result
    return wrapper
```

**Example:**
```python
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def greet(name):
    return f"Hello, {name}"

@log_decorator
def add(a, b):
    return a + b

print(greet("Alice"))  # Calling greet \n Hello, Alice
print(add(5, 3))       # Calling add \n 8
```

---

## 2. Using functools.wraps (Optional)
Always use `@wraps(func)` to preserve function metadata.

**Syntax:**
```python
from functools import wraps

def decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Example:**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello"""
    return f"Hello, {name}"

print(greet.__name__)  # "greet" ✓
print(greet.__doc__)   # "Say hello" ✓
```

---

## Spiral Learning Note
Unit 07a taught basic decorators. Now you handle function arguments with *args/**kwargs and preserve metadata with @wraps. Next you'll learn common decorator patterns.
