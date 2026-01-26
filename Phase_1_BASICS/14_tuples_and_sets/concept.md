# Unit 14: Tuples & Sets

## 1. Tuples - Immutable Lists
Tuples are like lists, but they **cannot be changed** after creation. Use parentheses `()` instead of brackets.

**Syntax:**
```python
tuple_name = (item1, item2, item3)
# Access like lists
first_item = tuple_name[0]
```

**Example:**
```python
point = (3, 4)
x, y = point  # Unpacking
print(f"X: {x}, Y: {y}")  # X: 3, Y: 4
```

---

## 2. Sets - Unique Collections (Optional)
Sets store **unique** values only (no duplicates). Use curly braces `{}`.

**Syntax:**
```python
set_name = {item1, item2, item3}
set_name.add(new_item)
set_name.remove(item)
```

**Example:**
```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3} - duplicates removed!

if 1 in unique_numbers:
    print("Found it!")
```

---

## Spiral Learning Note
Lists (Unit 05) are flexible. Tuples are for fixed data. Sets are for unique collections. Choose the right tool for the job!
