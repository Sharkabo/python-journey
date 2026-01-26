# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create Exception with Context Data
Create an `InsufficientFundsError` exception that:
- Takes `balance`, `requested_amount`, and `account_id` as parameters
- Stores all three in instance attributes
- Has a custom `__str__()` method that formats a helpful message

## Step 2: Use Exception Context in Application
Create a `BankAccount` class with:
- Balance attribute
- `withdraw(amount)` method that raises InsufficientFundsError with context
- Include account ID in the exception

## Step 3: Handle Exception and Use Context Data
Catch the exception and:
- Display all context information
- Calculate how much more is needed
- Show user-friendly error message

## Step 4: Chain Exceptions
Demonstrate exception chaining using `raise ... from`:
- Wrap a lower-level exception (ValueError) in a higher-level exception
- Show how both exceptions appear in the traceback

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Account 12345: Withdrawal successful! Balance: $50.00

Withdrawal failed!
Error: Insufficient funds in account 12345
Balance: $50.00
Requested: $75.00
Shortfall: $25.00

Exception Chaining:
Caught application error: Invalid transaction
Original cause: negative numbers not allowed
```
