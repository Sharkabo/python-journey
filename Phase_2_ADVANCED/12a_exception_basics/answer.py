from typing import Any

class PasswordValidationError(Exception):
    pass

class PasswordTooShortError(PasswordValidationError):
    pass

class PasswordMissingDigitError(PasswordValidationError):
    pass

class PasswordMissingSymbolError(PasswordValidationError):
    pass

def validate_password(password: str) -> Any:
    if len(password) < 8:
        raise PasswordTooShortError('Password is too short')
    
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigitError('Password must contain number')
    
    if all(char.isalnum() for char in password):
        raise PasswordMissingSymbolError('Password must have at least one special character')
    
    return True

password: str = 'Test12345678'
try:
    if validate_password(password):
        print('Password accepted')
except PasswordTooShortError as e:
    print(e)
except PasswordMissingDigitError as e:
    print(e)
except PasswordMissingSymbolError as e:
    print(e)