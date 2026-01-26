# Complete your task here (goals are defined in task.md)

# Step 1: Create a Custom Exception


# Step 2: Raise Your Custom Exception


# Step 3: Handle Your Custom Exception


# Step 4: Create an Exception Hierarchy


# Test your code
if __name__ == "__main__":
    # Test valid age
    try:
        result = validate_age(25)
        print(f"Validation passed: 25")
    except ValidationError as e:
        print(f"Validation Error: {e}")
    print()
    
    # Test negative age
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        if hasattr(e, 'field_name') and e.field_name:
            print(f"Field: {e.field_name}")
    print()
    
    # Test age too high
    try:
        validate_age(200)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        if hasattr(e, 'field_name') and e.field_name:
            print(f"Field: {e.field_name}")
    print()
    
    # Test exception hierarchy
    print("Exception Hierarchy:")
    try:
        raise DatabaseError("Database connection failed")
    except AppError as e:
        print(f"Caught AppError: {e}")
    
    try:
        raise NetworkError("Network timeout occurred")
    except AppError as e:
        print(f"Caught AppError: {e}")
    
    print("\nBoth caught by base exception type!")
