# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Decorator with *args and **kwargs
Create a decorator `smart_log` that:
- Accepts functions with any arguments using *args and **kwargs
- Prints the function name and its arguments
- Calls the original function with all arguments
- Returns the result

## Step 2: Use @wraps to Preserve Metadata
Import `wraps` from functools and apply it to your wrapper function.
This preserves the original function's name and docstring.

## Step 3: Decorate Functions with Different Signatures
Apply your decorator to:
- A function with no arguments: `say_hello()`
- A function with positional args: `greet(name, age)`
- A function with keyword args: `create_profile(name="", email="")`

## Step 4: Verify Metadata is Preserved
After decoration, print the `__name__` and `__doc__` of one decorated function to confirm @wraps worked.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Calling: say_hello, Args: (), Kwargs: {}
Hello!

Calling: greet, Args: ('Alice', 25), Kwargs: {}
Hello, Alice! You are 25 years old.

Calling: create_profile, Args: (), Kwargs: {'name': 'Bob', 'email': 'bob@example.com'}
Profile created for Bob (bob@example.com)

Function name: greet
Function docstring: Greet a person with their name and age
```
