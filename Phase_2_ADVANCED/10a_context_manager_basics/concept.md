# Unit 10a: Context Manager Basics

## 1. The with Statement
The `with` statement ensures resources are properly cleaned up, even if errors occur.

**Syntax:**
```python
with expression as variable:
    # Use the resource
    pass
# Resource automatically cleaned up
```

**Example:**
```python
# Without with (easy to forget to close!)
file = open('data.txt', 'r')
content = file.read()
file.close()

# With with statement (automatically closes)
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed here!
```

---

## 2. How It Works (Optional)
The `with` statement calls `__enter__()` and `__exit__()` methods.

**Syntax:**
```python
# Internally, Python does:
obj = expression
obj.__enter__()
try:
    # Your code
finally:
    obj.__exit__()
```

**Example:**
```python
# Multiple context managers
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
# Both files automatically closed
```

---

## Spiral Learning Note
The `with` statement ensures cleanup. Next you'll learn to create custom context managers and use the @contextmanager decorator.
