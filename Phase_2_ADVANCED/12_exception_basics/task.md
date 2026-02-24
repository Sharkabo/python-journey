# Task Description

**Scenario: The Strict Password Policy**

You are building the user registration system for a banking app. A generic "Invalid Password" error is not helpful—users need to know *why* their password failed (Too short? No numbers? No symbols?). You need to create a validation system that throws specific, granular errors.

**Your Goal:**
Create a custom exception hierarchy to handle different password validation failures distinctively.

**Objectives:**
1.  Create a base custom exception `PasswordValidationError(Exception)`.
2.  Create subclass exceptions:
    - `PasswordTooShortError`
    - `PasswordMissingDigitError`
    - `PasswordMissingSymbolError`
3.  Write a function `validate_password(password: str)`.
    - Raise `PasswordTooShortError` if length < 8.
    - Raise `PasswordMissingDigitError` if no numbers are found.
    - Raise `PasswordMissingSymbolError` if no special chars are found.
4.  Write a loop that asks the user for input and uses a `try...except` block to catch each specific error and print a specific helpful message for each one.

**Success Condition:**
When you provide a weak password "apple", it should specifically say "Password is too short". If you provide "applebanana", it should say "Missing a digit". If you provide "applebanana1", it should say "Missing a symbol". Only "applebanana1!" should pass.
