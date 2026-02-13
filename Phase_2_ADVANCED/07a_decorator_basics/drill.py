# Drills - Decorator Basics
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a simple decorator that prints "Before" and "After"
from typing import Any

def simple_log(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Before')
        result: Any = func(*args, **kwargs)
        print('After')
        return result
    return wrapper

# Drill 2: Apply the decorator using @ syntax to a function
@simple_log
def test() -> None:
    print("Test")

# Drill 3: Create a decorator that logs the function name
from typing import Callable
from functools import wraps

def name_log(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        print(f"Function name: {func_name}")
        result: Any = func(*args, **kwargs)
        return result
    return wrapper

# Drill 4: Create a timing decorator that measures execution time
import time

def timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        start = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"{func_name} took {duration} to complete.")
        return result
    return wrapper

# Drill 5: Stack two decorators on one function
@timer
@name_log
def try_stack_two() -> None:
    print('What a day~')

# Drill 6: Create a decorator that counts how many times a function is called
def call_counter(func: Callable):
    call_history: dict[str, int] = {}
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        call_history[func_name] = call_history.get(func_name, 0) +1
        result: Any = func(*args, **kwargs)
        return result
    return wrapper

# Drill 7: Create a decorator for a function with arguments
def arg_decorater(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        result: Any = func(*args, **kwargs)
        return result
    return wrapper

# Drill 8: Create a decorator that returns a modified result
def multiply_by_2(func: Callable):
    @wraps(func)
    def wrapper(*args: Any) -> float:
        result: float = func(*args)
        return result * 2
    return wrapper