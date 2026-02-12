# Task Description

**Scenario: The Flaky Network API**

You are integrating a third-party Weather API that is notoriously unstable. About 50% of the time, it fails with a "Connection Error". Your application crashes whenever this happens. You need a way to automatically retry the request a few times before giving up.

**Your Goal:**
Create a robust `@retry` decorator that accepts an argument for the number of attempts. It should attempt to run the function, and if it fails (raises an Exception), it should try again until it runs out of attempts.

**Objectives:**
1.  Create a decorator factory `retry(max_attempts)` that takes an integer argument.
2.  The decorator should wrap a function (e.g., `fetch_weather()`).
3.  Inside the wrapper, use a loop to call the function.
    - If it succeeds, return the result immediately.
    - If it raises an exception, catch it, print "Retrying...", and loop again.
    - If it fails after `max_attempts`, let the exception crash the program (propagate it).
4.  Simulate a flaky function that uses `random.random()` to raise an Exception 70% of the time and succeeds 30% of the time.

**Success Condition:**
Decorate your simulated flaky function with `@retry(max_attempts=5)`. When you call it, you should see it fail a few times and then (hopefully) succeed, or fail 5 times and raise the error.
