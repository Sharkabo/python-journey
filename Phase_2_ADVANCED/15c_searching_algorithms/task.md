# Task Description

**Scenario: The Timestamp Locator**

You have a log file with 1 million lines, sorted by timestamp (integer Unix time). You need to find the exact line for a specific timestamp. Scanning 1 million lines (`O(n)`) is too slow. You need to use **Binary Search** (`O(log n)`).

**Your Goal:**
Implement Binary Search to find a target number in a sorted list.

**Objectives:**
1.  Create a sorted list of numbers: `timestamps = [100, 200, 300, ... 10000]` (you can just use `list(range(0, 10000, 10))`).
2.  Implement `binary_search(data, target) -> index`:
    - Use `left` and `right` pointers.
    - Loop while `left <= right`.
    - Calculate `mid`.
    - Check if `data[mid] == target`.
    - Adjust `left` or `right` to cut the search space in half.
3.  Return the index if found, or `-1` if not.

**Success Condition:**
Search for a number that exists (e.g., 500). It should return the correct index.
Search for a number that doesn't exist (e.g., 505). It should return -1.
Add a print statement inside the loop: "Checking index X". You should see it find the answer in very few steps (e.g., < 10 steps for 1000 items), proving it's efficient.
