# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Timer Context Manager Class
Create a class `Timer` that:
- Has `__enter__(self)` that records start time and returns self
- Has `__exit__(self, exc_type, exc_val, exc_tb)` that calculates elapsed time
- Prints how long the code block took to execute
- Import `time` module

## Step 2: Use Your Timer Context Manager
Use your Timer with a `with` statement to time:
- A loop that sums numbers 0-1000000
- A time.sleep(1) operation

## Step 3: Store the Elapsed Time
Modify Timer to:
- Store elapsed time in `self.elapsed` attribute
- Allow accessing the time after the with block exits

## Step 4: Handle Exceptions in Context Manager
Test that your context manager still works even if an exception occurs inside the with block.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Code block took 0.0234 seconds

Sleep took 1.0012 seconds

Elapsed time stored: 1.0012 seconds

Testing exception handling:
Code block took 0.0001 seconds
Exception caught outside: Division by zero!
Timer still recorded time even with exception!
```
