# Task Description

**Scenario: The Algorithm Race**

Your manager thinks "Code is code, it doesn't matter how you write it as long as it works." You need to prove them wrong. You need to demonstrate that for large datasets, an unnecessary nested loop (`O(n²)`) is catastrophic compared to a linear solution (`O(n)`).

**Your Goal:**
Write two functions that do the same thing (find duplicates) but with different complexities, and RACE them.

**Objectives:**
1.  Generate a list of 10,000 random integers between 1 and 100.
2.  **Function 1 (Bad):** `find_duplicates_quadratic(lst)`.
    - Use a nested loop: `for i in lst: for j in lst:` to check for duplicates.
    - This is `O(n²)`.
3.  **Function 2 (Good):** `find_duplicates_linear(lst)`.
    - Use a Set or Dictionary to track seen numbers: `if i in seen:`.
    - This is `O(n)`.
4.  Use `time.time()` to measure how long each one takes.

**Success Condition:**
Run the race.
The Linear solution should be instantaneous (0.00something seconds).
The Quadratic solution should take noticeably longer (maybe seconds or tens of seconds).
Print the winner and the time difference factor (e.g., "Linear was 500x faster").
