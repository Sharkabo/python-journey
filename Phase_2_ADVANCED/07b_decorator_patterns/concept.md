# Unit 07b: Common Decorator Patterns

## 1. Timing Decorator
Measure how long a function takes to execute.

**Syntax:**
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper
```

**Example:**
```python
@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done"

slow_function()  # slow_function took 2.0021s
```

---

## 2. Cache Decorator (Optional)
Store results of expensive function calls using Python's built-in `@lru_cache`.

**Syntax:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(arg):
    # Expensive computation
    return result
```

**Example:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Fast! Results are cached
print(fibonacci(100))  # Instant (from cache)
```

---

## Spiral Learning Note
You learned basic decorators and arguments. Now you know common patterns like timing and caching. Next you'll learn lambda and functional programming.
