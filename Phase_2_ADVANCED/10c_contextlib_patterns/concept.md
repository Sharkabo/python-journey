# Unit 10c: Contextlib Patterns

## 1. @contextmanager Decorator
Simpler syntax for context managers using generators.

**Syntax:**
```python
from contextlib import contextmanager

@contextmanager
def context_name():
    # Setup code (like __enter__)
    try:
        yield resource  # Provide resource to with block
    finally:
        # Cleanup code (like __exit__)
        pass
```

**Example:**
```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager('data.txt', 'w') as f:
    f.write("Easy!")
# File automatically closed
```

---

## Spiral Learning Note
Unit 10b taught creating context managers with classes. The @contextmanager decorator uses generators (Unit 09b) for simpler syntax. Preferred for simple cases.
