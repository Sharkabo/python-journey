# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Simple Decorator
Create a decorator `log_call` that:
- Prints "Calling [function_name]" before the function executes
- Calls the original function
- Prints "Finished [function_name]" after the function executes
- Returns the result of the original function

## Step 2: Apply Your Decorator
Create two simple functions:
- `greet()` that prints "Hello!"
- `add(a, b)` that returns a + b  
Apply the decorator to both using the `@log_call` syntax.

## Step 3: Understand How Decorators Work
Without using @ syntax, manually decorate a function `say_goodbye()` by calling:
```python
say_goodbye = log_call(say_goodbye)
```

## Step 4: Test All Decorated Functions
Call all three decorated functions and observe the logging behavior.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Calling greet
Hello!
Finished greet

Calling add
Finished add
Result: 8

Calling say_goodbye
Goodbye!
Finished say_goodbye
```
