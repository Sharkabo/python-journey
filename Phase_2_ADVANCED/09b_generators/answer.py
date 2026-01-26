# Complete your task here (goals are defined in task.md)

# Step 1: Create a Fibonacci Generator


# Step 2: Create an Infinite Generator


# Step 3: Create a Generator Expression


# Step 4: Chain Generators Together


# Test your code
if __name__ == "__main__":
    # Test Step 1: Fibonacci
    print("Fibonacci sequence (first 10):")
    fib_nums = list(fibonacci(10))
    print(" ".join(map(str, fib_nums)))
    print()
    
    # Test Step 2: Infinite counter (take only 5)
    print("Infinite counter (first 5):")
    counter = count_up(0)
    for _ in range(5):
        print(next(counter), end=" ")
    print("\n")
    
    # Test Step 3: Generator expression
    print("Generator expression (squares of 1-10):")
    # Generator expression uses () instead of []
    # squares_gen = (x**2 for x in range(1, 11))
    # More memory efficient than list comprehension: [x**2 for x in range(1, 11)]
    squares_gen = (x**2 for x in range(1, 11))
    print(" ".join(map(str, squares_gen)))
    print()
    
    # Test Step 4: Chain generators
    print("Even squares (first 5):")
    even_sq = list(even_squares(5))
    print(" ".join(map(str, even_sq)))
