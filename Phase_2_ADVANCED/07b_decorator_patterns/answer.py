from typing import Any, Callable
from functools import wraps
import time

def timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end-start
        print(f'Duration: {duration:.3f}')
        return result
    return wrapper

def memoize(func: Callable):
    _cache: dict[tuple, Any] = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

@memoize
@timer
def fib(num):
    '''Fibonacci sequence'''
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

fib(35)