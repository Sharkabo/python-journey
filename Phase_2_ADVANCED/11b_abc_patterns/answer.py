# Complete your task here (goals are defined in task.md)
from abc import ABC, abstractmethod
import json
import os

# Step 1: Create a Repository ABC


# Step 2: Implement In-Memory Repository


# Step 3: Implement File Repository


# Step 4: Demonstrate Repository Pattern


# Test your code
if __name__ == "__main__":
    # Test InMemoryRepository
    print("=== Testing InMemoryRepository ===")
    manage_users(InMemoryRepository())
    print()
    
    # Test FileRepository
    print("=== Testing FileRepository ===")
    manage_users(FileRepository())
    print()
    
    print("Repository pattern works with both implementations!")
    
    # Cleanup
    if os.path.exists('data.json'):
        os.remove('data.json')
