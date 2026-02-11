# Drills - Basic Type Hints
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create variables with type annotations: name (str), age (int), height (float), is_student (bool)
name: str
age: int
height: float
is_student: bool

# Drill 2: Create a function add_numbers(a: int, b: int) -> int that returns the sum
def add_numbers(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError('Both input must be integer')

# Drill 3: Create a function greet(name: str) -> str that returns "Hello, {name}!"
def greet(name: str) -> str:
    return f"Hello, {name.capitalize()}!"

# Drill 4: Create a function get_even_numbers(numbers: list[int]) -> list[int] that filters even numbers
def get_even_numbers(numbers: list[int]) -> list[int]:
   list_evens = [num for num in numbers if num % 2 == 0]
   return list_evens

# Drill 5: Create a function get_user_info() -> tuple[str, int] that returns a tuple with name and age
def get_user_info() -> tuple[str, int]:
    return ("Alice", 25)

# Drill 6: Create a function print_message(msg: str) -> None that prints the message
def print_message(msg: str) -> None:
    print(f'{msg}')

# Drill 7: Create a Person class with __init__(self, name: str, age: int) and get_info(self) -> str method
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def get_info(self) -> str:
        return f"Name:{self.name} Age: {self.age}"

# Drill 8: Create a function uppercase_names(names: list[str]) -> list[str] that converts names to uppercase
def uppercase_names(names: list[str]) -> list[str]:
    uppercase_list = [name.upper() for name in names]
    return uppercase_list

# Drill 9: Create a function divide_with_remainder(a: int, b: int) -> tuple[int, int] that returns (quotient, remainder)
def divide_with_remainder(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        raise ValueError('Can\'t divided by zero')
    
    # Floor division
    quotient = a // b
    remainder = a % b
    return (quotient, remainder)

# Drill 10: Create a function create_profile(name: str, age: int, hobbies: list[str]) -> str with formatted output
def create_profile(name: str, age: int, hobbies: list[str]) -> str:
    return f'Name: {name} Age: {age} Hobbies: {hobbies}'