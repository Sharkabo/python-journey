# Task Description

**Scenario: The Unclosed Connection leak**

Your team's server keeps crashing because it runs out of "file handles" or "database connections". It turns out developers are opening connections but forgetting to close them when errors occur. You need to enforce a pattern that makes it *impossible* to forget cleanup.

**Your Goal:**
Simulate a resource that *must* be closed (like a file), and use the `with` statement to ensure it closes even if the program crashes halfway through.

**Objectives:**
1.  Use Python's built-in `open()` function as the simplest context manager.
2.  Create a file `"crash_test.txt"`.
3.  Write a block of code using `with open(...)` to write to the file.
4.  Inside the `with` block, deliberately raise an exception (e.g., `raise ValueError("Oops!")`).
5.  Wrap the whole thing in a `try...except` block to catch the error.
6.  After the error is caught, verify if the file is closed. (Hint: `file_object.closed` returns True/False).

**Success Condition:**
You should see: "Error occurred: Oops!", followed by "File is closed: True". The file MUST be closed even though the code inside the `with` block crashed before it finished.
