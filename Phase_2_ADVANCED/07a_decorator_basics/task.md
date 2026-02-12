# Task Description

**Scenario: Verified Access Only**

Your company is building an internal dashboard with sensitive commands like `delete_database()` and `grant_access()`. Junior developers keep accidentally calling these functions. You need a way to secure them without rewriting the logic inside every single function.

**Your Goal:**
Implement an `@admin_required` decorator that acts as a security gate. It should intercept function calls and check for a global permission flag before allowing the function to execute.

**Objectives:**
1.  Define a global variable `CURRENT_USER_ROLE` (set it to "guest" initially).
2.  Create a decorator `admin_required` that wraps any function.
3.  Inside the wrapper, check if `CURRENT_USER_ROLE` is "admin".
    - If yes: Execute the decorated function and return its result.
    - If no: Print "Access Denied" and return `None` (do *not* run the function).
4.  Apply this decorator to a sensitive function like `nuke_system()`.

**Success Condition:**
1.  With `CURRENT_USER_ROLE = "guest"`, calling `nuke_system()` prints "Access Denied".
2.  Change `CURRENT_USER_ROLE` to "admin".
3.  Calling `nuke_system()` now successfully prints "System Destroyed!".
