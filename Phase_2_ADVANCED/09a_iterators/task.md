# Task Description

**Scenario: The Infinite Sequence Generator**

You are building a simulation that needs an endless stream of Fibonacci numbers to model population growth. You can't pre-calculate a list because you don't know how many numbers you'll need—maybe 50, maybe 5000. You need an object that generates the *next* number only when asked.

**Your Goal:**
Build a custom Iterator class `FibonacciIterator` that calculates the next number in the sequence on-the-fly.

**Objectives:**
1.  Create a class `FibonacciIterator`.
2.  Implement `__init__(self, max_count)` to limit the sequence (optional safety stop).
3.  Implement `__iter__(self)` to return `self`.
4.  Implement `__next__(self)`:
    - It should calculate the next Fibonacci number (0, 1, 1, 2, 3, 5...).
    - It should update its internal state (`a`, `b` = `b`, `a + b`).
    - It should `raise StopIteration` if it exceeds `max_count`.
5.  Use a `for` loop to iterate through your class and print the first 10 numbers.

**Success Condition:**
You should be able to run `for num in FibonacciIterator(10): print(num)` and see the sequence print out line by line. The memory usage should be tiny because it never stores the full list.
