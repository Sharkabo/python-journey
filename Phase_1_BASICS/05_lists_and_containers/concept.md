# Unit 05: Lists & Containers

## 1. Creating and Using Lists
Variables hold one thing. **Lists** hold many things in order. We use square brackets `[]` to create a list.

**Syntax:**
```python
list_name = [item1, item2, item3]
# Access items by index (starts at 0)
first_item = list_name[0]
```

**Example:**
```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])  # Prints: Apple
print(fruits[1])  # Prints: Banana
```

---

## 2. Adding Items to Lists (Optional)
Use `.append()` to add items to the end of a list.

**Syntax:**
```python
list_name.append(new_item)
```

**Example:**
```python
fruits.append("Orange")
print(fruits)  # ["Apple", "Banana", "Cherry", "Orange"]
```

---

## Spiral Learning Note
Lists are powerful variable containers. We can store user inputs (Unit 03) into a list to save a history of what they typed!
