# Unit 05b: Advanced Types (Optional, Union, Collections)

## 1. Dictionary and Collection Type Hints
Dictionaries require type hints for both keys and values.

**Syntax:**
```python
# Dictionary with string keys and int values
ages: dict[str, int] = {"Alice": 25, "Bob": 30}

# Set of strings
unique_names: set[str] = {"Alice", "Bob", "Charlie"}

# Tuple with specific types
user: tuple[str, int, float] = ("Alice", 25, 5.8)
```

**Example:**
```python
def count_items(items: list[str]) -> dict[str, int]:
    """Count how many times each item appears"""
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

fruits = ["apple", "banana", "apple", "orange"]
result = count_items(fruits)
print(result)  # {'apple': 2, 'banana': 1, 'orange': 1}
```

---

## 2. Optional and Union Types (Optional)
`Optional` means a value can be the specified type OR `None`. `Union` means one of several types.

**Syntax:**
```python
from typing import Optional

# Variable can be str or None
name: Optional[str] = "Alice"
name = None  # Valid

# Or use | operator (Python 3.10+)
name: str | None = "Alice"

# Union for multiple types
user_id: int | str = 123
```

**Example:**
```python
def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return None if not found"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

result = find_user(1)
if result is not None:
    print(f"Found: {result}")
```

---

## Spiral Learning Note
Unit 05a taught basic type hints. Now you handle complex collections and optional values. Next you'll apply type hints to classes.
