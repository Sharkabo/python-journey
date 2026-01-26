# Complete your task here (goals are defined in task.md)
import time
from functools import wraps, lru_cache

# Step 1: Create a Timing Decorator


# Step 2: Apply Timing Decorator


# Step 3: Use @lru_cache for Memoization


# Step 4: Compare Cached vs Uncached Performance (create uncached version)


# Test your code
if __name__ == "__main__":
    # Test fast function
    result = fast_function()
    print(f"Result: {result}")
    print()
    
    # Test slow function
    slow_function()
    print()
    
    # Test cached fibonacci
    fib_result = fibonacci(35)
    print(f"Fibonacci (cached) of 35: {fib_result}")
    print()
    
    # Test uncached fibonacci and compare
    start = time.time()
    fib_uncached_result = fibonacci_uncached(35)
    uncached_time = time.time() - start
    print(f"Fibonacci (uncached) of 35: {fib_uncached_result}")
    print(f"fibonacci_uncached took {uncached_time:.4f} seconds")
    print()
    
    # Note: To see timing for cached fibonacci, call it again
    # The first call will be slower (building cache)
    start_cached = time.time()
    fibonacci(35)
    cached_time = time.time() - start_cached
    
    if cached_time > 0:
        speedup = uncached_time / cached_time
        print(f"Performance improvement: {speedup:.0f}x faster with caching!")
