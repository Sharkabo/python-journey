# Complete your task here (goals are defined in task.md)
from typing import Optional

# Step 1: Create a Function with Dict Type Hints


# Step 2: Create a Function with Optional Type


# Step 3: Create a Function with Union Type


# Step 4: Create a Function with Set Type Hints


# Test your code
if __name__ == "__main__":
    # Test Step 1
    text = "hello world hello python"
    word_counts = count_words(text)
    print(f"Word counts: {word_counts}")
    
    # Test Step 2
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    user = find_user(1, users)
    print(f"User found: {user}")
    
    not_found = find_user(99, users)
    print(f"User not found: {not_found}")
    
    # Test Step 3
    result1 = process_input(42)
    print(f"Process int: {result1}")
    
    result2 = process_input("hello")
    print(f"Process str: {result2}")
    
    # Test Step 4
    posts = [
        {"tags": ["python", "tutorial"]},
        {"tags": ["coding", "tips"]},
        {"tags": ["python", "beginner"]}
    ]
    tags = get_unique_tags(posts)
    print(f"Unique tags: {tags}")
