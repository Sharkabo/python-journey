# Task Description

**Scenario: The Slow Fibonacci Sequence**

You are optimizing a calculation engine. You have a recursive function that calculates Fibonacci numbers, but it is incredibly slow for larger numbers (like `fib(35)`). You need to analyze *why* it's slow (timing) and then *fix* it (caching) without changing the algorithm itself.

**Your Goal:**
Build a "Decorator Toolkit" containing two powerful tools: `@timer` and `@memoize`.

**Objectives:**
1.  **The Timer:** Create a `@timer` decorator that measures execution time. It should record the start time, run the function, record the end time, and print: `"Function X took 0.0024 seconds"`.
2.  **The Cache (Memoize):** Create a `@memoize` decorator. It should store the results of expensive function calls in a dictionary `cache = {}`.
    - Before running the function, check if the arguments are already in `cache`.
    - If yes, return the stored value (Instant!).
    - If no, run the function, store the result in `cache`, and then return it.
3.  Apply `@timer` to a slow recursive Fibonacci function. Observe the slowness.
4.  Stack `@memoize` on top of (or below) `@timer`.

**Success Condition:**
Calculate `fib(35)` without memoization (should take a few seconds).
Calculate `fib(35)` WITH memoization (should be nearly instant, 0.0000s).
Prove the speedup using your own `@timer` decorator.
