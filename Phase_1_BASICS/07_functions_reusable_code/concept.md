# Unit 07: Functions

## 1. Defining Functions
Functions are like mini-programs or "recipes" you write once and use many times. We use `def` to define them.

**Syntax:**
```python
def function_name():
    # Code to run
```

**Example:**
```python
def greet():
    print("Hello!")

greet()  # Prints: Hello!
```

---

## 2. Function Parameters (Optional)
You can pass data into functions to make them more flexible.

**Syntax:**
```python
def function_name(parameter):
    # Use parameter here
```

**Example:**
```python
def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Child")

check_age(20)  # Prints: Adult
check_age(10)  # Prints: Child
```

---

## Spiral Learning Note
Functions wrap up your logic involving Variables (Unit 01), Math (Unit 02), Decisions (Unit 04), and Loops (Unit 06) into reusable blocks.
