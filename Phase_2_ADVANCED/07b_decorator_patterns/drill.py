# Drills - Decorator Patterns
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a timing decorator for performance measurement
import time
from functools import wraps
from typing import Any, Callable

def timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"It took {duration:.6f} to complete")
        return result
    return wrapper

# Drill 2: Create a retry decorator with max_attempts parameter
def retry(max_attempts: int):
    def decorater(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = max_attempts
            result = None
            while attempts > 0:
                try:
                    result = func(*args, **kwargs)
                    break
                except Exception as e:
                    attempts -= 1
                    if attempts > 0:
                        time.sleep(1)
                    else: 
                        raise e
            return result
        return wrapper
    return decorater

# Drill 3: Create a logging decorator that shows function name and args
def logger(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        arg_str = "/".join(str(a) for a in args)
        result: Any = func(*args, **kwargs)
        print(f"Function: {func_name}– Arguments: {arg_str}")
        return result
    return wrapper

# Drill 4: Use @lru_cache for memoization
from functools import lru_cache
@lru_cache(maxsize= 128)
def multiply_by_2(num: int) -> int:
    return num * 2

# Drill 5: Create an authentication decorator (check if user is logged in)
def auth(identify):
    def decorater(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if identify == 'admin':
                result: Any = func(*args, **kwargs)
            else:
                result = None
            return result
        return wrapper
    return decorater
# Drill 6: Create a rate limiting decorator
def rate_limiting(max_calls: int, period: float):
    def decorater(func: Callable):
        calls: int = 0
        last_reset = time.perf_counter()
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal calls, last_reset
            now = time.perf_counter()
            if now - last_reset > period:
                calls = 0
                last_reset = now
            if calls < max_calls:
                calls += 1
                result: Any = func(*args, **kwargs)
            else:
                result = None
                print('Sorry, too many request')
            return result
        return wrapper
    return decorater

# Drill 7: Create a validation decorator for function arguments
def validate_args(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if not args and not kwargs:
            result = None
        else:
            result: Any = func(*args, **kwargs)
        return result
    return wrapper

# Drill 8: Create a caching decorator that stores results
def caching(func: Callable):
    _cache: dict[tuple, Any] = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in _cache:
            _cache[key]= func(*args, **kwargs)
        return _cache[key]
    return wrapper