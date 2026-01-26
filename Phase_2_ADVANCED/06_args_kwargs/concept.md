# Unit 06: Args and Kwargs (*args, **kwargs)

## 1. What are *args and **kwargs?
`*args` and `**kwargs` allow functions to accept a variable number of arguments.

**Syntax:**
```python
def function(*args, **kwargs):
    # *args is a tuple of positional arguments
    # **kwargs is a dictionary of keyword arguments
    pass
```

**Example:**
```python
def add_numbers(*args):
    print(f"Received: {args}")  # Tuple
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)
print(result)  # 15

def create_profile(**kwargs):
    print(f"Received: {kwargs}")  # Dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=25, city="NYC")
```

---

## 2. Combining Parameters (Optional)
You can mix regular parameters, *args, and **kwargs. Order matters!

**Syntax:**
```python
def function(required, *args, default="value", **kwargs):
    # Function body
    pass
```

**Example:**
```python
def api_call(path, *middlewares, **options):
    print(f"Path: {path}")
    print(f"Middlewares: {middlewares}")
    print(f"Options: {options}")

api_call("/users", "auth", "logging", method="GET", cache=True)
# Path: /users
# Middlewares: ('auth', 'logging')
# Options: {'method': 'GET', 'cache': True}
```

---

## Spiral Learning Note
You know functions from Phase 1. `*args` and `**kwargs` make them flexible. Next you'll learn decorators that heavily use these concepts.
