# Complete your task here (goals are defined in task.md)

# Step 1: Create a Function Using *args


# Step 2: Create a Function Using **kwargs


# Step 3: Combine *args and **kwargs


# Step 4: Use *args to Unpack


# Test your code
if __name__ == "__main__":
    # Test Step 1
    result = sum_all(1, 2, 3, 4, 5)
    print(f"Sum: {result}")
    
    # Test Step 4 (unpacking)
    numbers = [1, 2, 3, 4, 5, 6]
    unpacked_sum = sum_all(*numbers)
    print(f"Sum with unpacking: {unpacked_sum}")
    print()
    
    # Test Step 2
    print("User data:")
    user = create_user(name="Alice", age="25", email="alice@example.com")
    print(f"User dict: {user}")
    print()
    
    # Test Step 3
    print("Flexible function called:")
    flexible_function("Hello", 1, 2, 3, city="NYC", country="USA")
    print()
    
    # Test Step 4 (stats)
    stats_list = [1, 3, 5, 7, 9]
    min_val, max_val, avg_val = calculate_stats(stats_list)
    print(f"Stats: min={min_val}, max={max_val}, avg={avg_val}")
    sum_stats = sum_all(*stats_list)
    print(f"Sum of stats list: {sum_stats}")
