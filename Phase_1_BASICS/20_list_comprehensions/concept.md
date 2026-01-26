# Unit 20: List Comprehensions

## 1. What is List Comprehension?
List comprehension is a **shortcut** to create lists using a single line of code. It's a more "Pythonic" way to transform data.

**Syntax:**
```python
new_list = [expression for item in iterable]
```

**Example:**
```python
# Traditional way
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)

# List comprehension way
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

---

## 2. Adding Conditions (Optional)
You can filter items using `if` inside the comprehension.

**Syntax:**
```python
new_list = [expression for item in iterable if condition]
```

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # [2, 4, 6]
```

---

## Spiral Learning Note
List comprehensions combine loops (Unit 06), conditions (Unit 04), and list operations (Unit 05) into one elegant line!
