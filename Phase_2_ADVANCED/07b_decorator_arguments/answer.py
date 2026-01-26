# Complete your task here (goals are defined in task.md)
from functools import wraps

# Step 1: Create a Decorator with *args and **kwargs


# Step 2: Use @wraps (already imported above, apply in Step 1)

# Step 3: Decorate Functions with Different Signatures


# Step 4: Verify Metadata is Preserved
if __name__ == "__main__":
    # Test no arguments
    say_hello()
    print()
    
    # Test positional arguments
    greet("Alice", 25)
    print()
    
    # Test keyword arguments
    create_profile(name="Bob", email="bob@example.com")
    print()
    
    # Verify metadata preservation
    print(f"Function name: {greet.__name__}")
    print(f"Function docstring: {greet.__doc__}")
