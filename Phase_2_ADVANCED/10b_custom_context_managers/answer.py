# Complete your task here (goals are defined in task.md)
import time

# Step 1: Create a Timer Context Manager Class


# Step 2: Use Your Timer Context Manager


# Step 3: Store the Elapsed Time


# Step 4: Handle Exceptions in Context Manager


# Test your code
if __name__ == "__main__":
    # Test Step 2: Basic timing
    with Timer():
        total = sum(range(1000000))
    
    with Timer():
        time.sleep(1)
    
    # Test Step 3: Access elapsed time
    with Timer() as t:
        time.sleep(1)
    print(f"Elapsed time stored: {t.elapsed:.4f} seconds")
    print()
    
    # Test Step 4: Exception handling
    print("Testing exception handling:")
    try:
        with Timer():
            x = 1 / 0  # This will raise an exception
    except ZeroDivisionError:
        print("Exception caught outside: Division by zero!")
    print("Timer still recorded time even with exception!")
