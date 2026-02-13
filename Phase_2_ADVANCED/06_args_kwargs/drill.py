# Drills - Args and Kwargs
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a function multiply_all(*args) that multiplies all arguments together
def multiply_all(first: float, *others: float) -> float:
    result = first
    for num in others:
        result *= num
    return result

# Drill 2: Create a function print_info(**kwargs) that prints all key-value pairs
def print_info(**info) -> None:
    for key, value in info.items():
        print(f'{key}: {value}')

# Drill 3: Create a function greet(greeting, *names) that greets multiple people
def greet(greeting: str, *names: str) -> list[str]:
    results: list[str] = []
    for name in names:
        results.append(f"{greeting}, {name}")
    return results

# Drill 4: Create a function build_url(base, *paths, **params) that builds a URL
from typing import Any

def build_url(base: str, *paths: str, **params: Any) -> str:
    path_str = "/".join(paths)
    para_list: list[str] = []
    for key, value in params.items():
        para_list.append(f"{key}={value}")
    para_str = "&".join(map(str, para_list))
    
    if len(para_list) == 0:
        return f"{base}/{path_str}"
    else:
        return f"{base}/{path_str}?{para_str}"

# Drill 5: Unpack the list [1, 2, 3] to call a function add(a, b, c)
nums = [1, 2, 3]

def add(a: int, b: int, c: int) -> int:
    return a + b + c

result = add(*nums)

# Drill 6: Unpack the dictionary {'name': 'Bob', 'age': 30} to call a function
bob_info : dict[str, str | int] = {'name': 'Bob', 'age': 30}

def get_info(**source) -> list[str]:
    info_list: list[str] = []
    for key, value in source.items():
        info_list.append(f"{key}={value}")
    return info_list

get_info(**bob_info)

# Drill 7: Create a function that accepts (required, *args, default="value", **kwargs)
def display_syntax(necessary: str, *test_args: int, status: str = "Pending", **kwargs: Any) -> None:
    print('Nailed it, hahaha')

# Drill 8: Combine two lists using unpacking: [1, 2, 3] and [4, 5, 6]
def combine_two_lists(*source) -> list[int]:
    return list(source)

list_a: list[int] = [1, 2, 3]
list_b: list[int] = [4, 5, 6]

combine_two_lists(*list_a, *list_b)

# Drill 9: Combine two dictionaries using unpacking
def combine_two_dict(**source) -> dict[str, int]:
    result: dict [str, int] = {}
    for key, value in source.items():
        result [key] = value
    return result

# Drill 10: Create a wrapper function that logs any function call (use *args, **kwargs)
from typing import Callable
from functools import wraps

def logger(func:Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper