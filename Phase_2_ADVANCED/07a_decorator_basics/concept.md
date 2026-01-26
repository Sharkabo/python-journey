# Unit 07a: Decorator Basics

## 1. What are Decorators?
A decorator is a function that modifies or enhances another function without changing its code. They use the `@` symbol.

**Syntax:**
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

**Example:**
```python
def log_decorator(func):
    def wrapper():
        print(f"Calling: {func.__name__}")
        result = func()
        print(f"Completed: {func.__name__}")
        return result
    return wrapper

@log_decorator
def fetch_data():
    print("Fetching data...")
    return {"users": 100}

data = fetch_data()
# Output:
# Calling: fetch_data
# Fetching data...
# Completed: fetch_data
```

---

## 2. Multiple Decorators (Optional)
You can stack multiple decorators on one function.

**Syntax:**
```python
@decorator1
@decorator2
def function():
    pass
```

**Example:**
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())  # "HELLO WORLD"
```

---

## Spiral Learning Note
Unit 06 taught that functions can take functions as parameters. Now you use that to modify functions with decorators. Next you'll learn decorators with arguments.
