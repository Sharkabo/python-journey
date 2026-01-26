# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Timing Decorator
Create a decorator `timing` that:
- Records the start time before function execution
- Executes the function
- Records the end time after execution
- Prints how long the function took to run (in seconds)
- Import `time` module

## Step 2: Apply Timing Decorator
Create and decorate two functions:
- `fast_function()` that calculates sum(range(100))
- `slow_function()` that uses `time.sleep(1)` to simulate slow operation

## Step 3: Use @lru_cache for Memoization
Import `lru_cache` from functools.
Create a recursive `fibonacci(n)` function and decorate it with `@lru_cache(maxsize=128)`.
Test by calculating fibonacci(35) - it should be very fast due to caching.

## Step 4: Compare Cached vs Uncached Performance
Create an uncached version of fibonacci and time both:
- Cached fibonacci(35)
- Uncached fibonacci(35)
Observe the massive performance difference.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
fast_function took 0.0000 seconds
Result: 4950

slow_function took 1.0012 seconds
Simulated slow operation complete!

Fibonacci (cached) of 35: 9227465
fibonacci took 0.0000 seconds

Fibonacci (uncached) of 35: 9227465
fibonacci_uncached took 2.4567 seconds

Performance improvement: 61417x faster with caching!
```
