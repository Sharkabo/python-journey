# Task Description

**Scenario: The Atomic Bank Transaction**

You are building a banking system. When transferring money, two things happen:
1. Deduct $100 from Alice.
2. Add $100 to Bob.

If step 2 fails (e.g., Bob's account is invalid), you MUST undo step 1. You can't leave Alice with $100 less and Bob with nothing. This is called an "Atomic Transaction"—either everything happens, or nothing happens.

**Your Goal:**
Create a custom Context Manager class `AtomicTransaction` that automatically "rolls back" changes if an error occurs inside the `with` block.

**Objectives:**
1.  Create a dictionary `accounts = {"Alice": 1000, "Bob": 500}`.
2.  Create a class `AtomicTransaction`.
    - `__init__`: Save a backup (copy) of the `accounts` dictionary.
    - `__enter__`: Return the current `accounts` dictionary to be modified.
    - `__exit__`: Check if an exception occurred (`exc_type` is not None).
        - If an error happened: RESTORE `accounts` from the backup. Print "Rollback!".
        - If no error: Do nothing (changes are permanent).
3.  Test it: Use `with AtomicTransaction() as db:` to modify accounts, then raise an error.
4.  Print `accounts` afterwards. It should be back to original values!

**Success Condition:**
"Alice" should still have 1000, not 900. The failed transaction should satisfy the ACID property of Atomicity.
