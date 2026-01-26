# Unit 06: Loops & Repetition

## 1. The For Loop
Loops allow us to repeat code without copying and pasting. The `for` loop is great for going through a List.

**Syntax:**
```python
for item in list_name:
    # Do something with item
```

**Example:**
```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello " + name)
# Prints "Hello Alice", "Hello Bob", "Hello Charlie"
```

---

## 2. Using Ranges (Optional)
If you just want to repeat code a specific number of times, use `range()`.

**Syntax:**
```python
for i in range(number):
    # Code to repeat
```

**Example:**
```python
for i in range(3):
    print("Repeat!")
# Prints "Repeat!" three times
```

---

## Spiral Learning Note
Loops let us process Lists (Unit 05) automatically. We can also use `if` (Unit 04) inside a loop to filter items!
