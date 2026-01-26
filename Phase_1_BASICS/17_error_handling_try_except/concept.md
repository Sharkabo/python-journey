# Unit 17: Error Handling (Try/Except)

## 1. Catching Errors
If a user enters text when you asked for a number, your program crashes. We can catch these errors to prevent crashes.

**Syntax:**
```python
try:
    # Dangerous code here
except ExceptionType:
    # Run this if error occurs
```

**Example:**
```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("That was not a number!")
```

---

## Spiral Learning Note
Remember Unit 03 (Input)? This fixes the biggest problem with `input()` — users typing the wrong thing.
