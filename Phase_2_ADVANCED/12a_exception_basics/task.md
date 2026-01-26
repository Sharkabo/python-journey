# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Custom Exception
Create a custom exception class `ValidationError` that:
- Inherits from Exception
- Takes a message parameter
- Optionally takes a `field_name` parameter
- Stores both in instance attributes

## Step 2: Raise Your Custom Exception
Create a function `validate_age(age: int)` that:
- Raises ValidationError if age < 0
- Raises ValidationError if age > 150
- Returns True if valid

## Step 3: Handle Your Custom Exception
Use try/except to catch ValidationError and:
- Print the error message
- Access the field_name if provided
- Show graceful error handling

## Step 4: Create an Exception Hierarchy
Create a base `AppError` exception and two specific exceptions:
- `DatabaseError(AppError)` for database issues
- `NetworkError(AppError)` for network issues
Show catching both with a single except block.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Validation passed: 25

Validation Error: Age cannot be negative
Field: age

Validation Error: Age cannot exceed 150 years
Field: age

Exception Hierarchy:
Caught AppError: Database connection failed
Caught AppError: Network timeout occurred

Both caught by base exception type!
```
