# Complete your task here (goals are defined in task.md)

# Step 1: Use Lambda with map()


# Step 2: Use Lambda with filter()


# Step 3: Use Lambda with sorted()


# Step 4: Combine map() and filter()


# Test your code
if __name__ == "__main__":
    # Test Step 1
    numbers1 = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers1))
    print(f"Original: {numbers1}")
    print(f"Squared: {squared}")
    print()
    
    # Test Step 2
    numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
    evens = list(filter(lambda x: x % 2 == 0, numbers2))
    print(f"Original: {numbers2}")
    print(f"Even only: {evens}")
    print()
    
    # Test Step 3
    students = [
        {"name": "Alice", "grade": 95},
        {"name": "Bob", "grade": 82},
        {"name": "Charlie", "grade": 88}
    ]
    sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
    print("Students sorted by grade:")
    for student in sorted_students:
        print(f"{student['name']}: {student['grade']}")
    print()
    
    # Test Step 4
    numbers3 = [3, 7, 2, 9, 4, 8, 1, 6]
    filtered = list(filter(lambda x: x > 5, numbers3))
    result = list(map(lambda x: x ** 2, filtered))
    print(f"Numbers: {numbers3}")
    print(f"Filtered (>5): {filtered}")
    print(f"Squared: {result}")
