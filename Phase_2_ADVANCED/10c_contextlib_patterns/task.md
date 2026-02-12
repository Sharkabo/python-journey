# Task Description

**Scenario: The Temporary Configuration Switch**

You are writing tests for an application that behaves differently in "DEV" mode vs "PROD" mode. You need to switch the environment variable `APP_ENV` to "PROD" just for one specific test, and then *immediately* switch it back to "DEV" so you don't break other tests. Doing this manually with `os.environ` is tedious and error-prone.

**Your Goal:**
Create a clean, reusable `@contextmanager` that temporarily sets an environment variable and resets it when done.

**Objectives:**
1.  Import `contextmanager` from `contextlib` and `os`.
2.  Define a generator function `temporary_env_var(key, value)`.
3.  **Setup (`yield` before):** Save the old value of `os.environ[key]`. Set the new `value`. Yield.
4.  **Teardown (`yield` after):** In a `finally` block, restore the old value.
5.  Test it:
    - Set `os.environ["MODE"] = "DEFAULT"`.
    - Use `with temporary_env_var("MODE", "TESTING"):`.
    - Inside the block, print `os.environ["MODE"]` (should be "TESTING").
    - Outside the block, print `os.environ["MODE"]` (should be "DEFAULT").

**Success Condition:**
The environment variable must revert to its original value automatically, ensuring your test doesn't pollute the global environment.
