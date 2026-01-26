# Unit 10b: Custom Context Managers

## 1. Creating Context Managers
Create custom context managers by implementing `__enter__()` and `__exit__()` methods.

**Syntax:**
```python
class ContextManagerClass:
    def __enter__(self):
        # Setup code
        return self  # or resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup code
        return False  # Don't suppress exceptions
```

**Example:**
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager('data.txt', 'w') as f:
    f.write("Hello!")
# File automatically closed
```

---

## 2. Timer Context Manager (Optional)
A practical example for timing code execution.

**Example:**
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        elapsed = time.time() - self.start
        print(f"Took {elapsed:.2f}s")

with Timer():
    time.sleep(2)
# Prints: Took 2.00s
```

---

## Spiral Learning Note
Unit 10a taught the `with` statement. Now you create custom context managers. Next you'll learn the @contextmanager decorator for simpler syntax.
