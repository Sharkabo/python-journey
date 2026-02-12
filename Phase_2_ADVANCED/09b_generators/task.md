# Task Description

**Scenario: The Massive Log File**

You have a 50GB server log file. You need to read it line-by-line to find error messages. If you try to open this file and read it into a list (`lines = file.readlines()`), your computer will run out of RAM and crash. You need a "Lazy" way to read it.

**Your Goal:**
Create a generator function that simulates reading a massive file line-by-line, yielding one line at a time.

**Objectives:**
1.  Create a generator function `stream_log_data(lines_count)`.
2.  Instead of reading a real file (to keep it simple), use a loop to generate simulated log lines like `"Log line 1"`, `"Log line 2"`, etc., up to `lines_count`.
3.  Use the `yield` keyword to return one line at a time to the caller.
4.  Pause the loop after each yield.
5.  Demonstrate usage: Use a `for` loop to consume your generator. Print `"Processing: Log line X"` for each item.

**Success Condition:**
Calling `stream_log_data(5)` should NOT return a list `['Log line 1', ...]`. It should return a *generator object*. Your `for` loop should receive the lines one by one. Prove it's lazy!
