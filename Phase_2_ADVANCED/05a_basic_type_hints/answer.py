# Complete your task here (goals are defined in task.md)

# Step 1: Create Typed Variables


# Step 2: Create a Typed Function


# Step 3: Create a Function with List Type Hints


# Step 4: Create a Function Returning Tuple


# Test your code
if __name__ == "__main__":
    # Test Step 1
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Is Student: {is_student}")
    
    # Test Step 2
    bmi = calculate_bmi(70.0, 1.75)
    print(f"BMI: {bmi:.2f}")
    
    # Test Step 3
    grades = [85.5, 92.0, 88.5, 84.0]
    avg = get_average_grade(grades)
    print(f"Average Grade: {avg:.2f}")
    
    # Test Step 4
    info1 = get_user_info("Bob", 17)
    print(f"User Info: {info1}")
    
    info2 = get_user_info("Alice", 25)
    print(f"User Info: {info2}")
