# Unit 05a: Basic Type Hints

## 1. What are Type Hints?
Type hints (type annotations) allow you to specify what types of values variables, function parameters, and return values should have.

**Syntax:**
```python
# Variable annotation
name: str = "Alice"
age: int = 25

# Function annotation
def greet(name: str) -> str:
    return f"Hello, {name}"
```

**Example:**
```python
def add_numbers(a: int, b: int) -> int:
    return a + b

def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

# Multiple return values (tuple)
def get_user_info() -> tuple[str, int]:
    return ("Alice", 25)

# No return value
def print_message(msg: str) -> None:
    print(msg)
```

---

## 2. Collection Type Hints (Optional)
Lists, dictionaries, and other collections can have type hints.

**Syntax:**
```python
# List of specific type
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob"]
```

**Example:**
```python
def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

scores: list[float] = [95.5, 87.3, 92.1]
```

---

## Spiral Learning Note
You've worked with classes and properties. Type hints make code clearer and help catch bugs. Next you'll learn advanced types like Optional and Union.
