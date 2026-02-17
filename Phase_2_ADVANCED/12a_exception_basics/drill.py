# Drills - Custom Exceptions
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a custom ValidationError exception
class BannedUserError(Exception):
    pass

# Drill 2: Raise your custom exception
class User:
    def __init__(self, name: str, is_banned: bool) -> None:
        self.name = name
        if is_banned:
            raise BannedUserError('Your account is being banned')
        self.banned = is_banned

# Drill 3: Catch your custom exception
try:
    user = User("test", False)
except BannedUserError as e:
    print(e)

# Drill 4: Create a custom exception for invalid age
class InvalidAge(Exception):
    pass

# Drill 5: Use custom exceptions in a class
class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        if age < 18:
            raise InvalidAge('You are under 18, not allow to use this service')

try:
    Minion = Student('Lobo', 4)
except InvalidAge as e:
    print(e)