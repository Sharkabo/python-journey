# Unit 12: Loop Control (Break & Continue)

## 1. Break - Stop the Loop
The `break` statement immediately exits a loop, even if the loop condition is still true.

**Syntax:**
```python
for item in list:
    if condition:
        break
    # Do something
```

**Example:**
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints: 0, 1, 2, 3, 4 (stops at 5)
```

---

## 2. Continue - Skip to Next Iteration (Optional)
The `continue` statement skips the rest of the current iteration and moves to the next one.

**Syntax:**
```python
for item in list:
    if condition:
        continue
    # Do something
```

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:  # If even
        continue
    print(num)  # Only prints odd: 1, 3, 5
```

---

## Spiral Learning Note
We learned loops in Units 06 and 10. Now we can control them more precisely! `break` and `continue` are essential for handling user input and filtering data.
