# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Repository ABC
Create an abstract `Repository` class that defines a storage interface:
- Abstract method `save(self, item: dict) -> bool`
- Abstract method `find(self, id: int) -> dict | None`
- Abstract method `delete(self, id: int) -> bool`

## Step 2: Implement In-Memory Repository
Create `InMemoryRepository(Repository)` that:
- Uses a dictionary to store items in memory
- Implements all three abstract methods
- Stores items by ID

## Step 3: Implement File Repository
Create `FileRepository(Repository)` that:
- Uses JSON file for persistence
- Implements all three abstract methods
- Reads/writes to 'data.json'
- Import `json` module

## Step 4: Demonstrate Repository Pattern
Create a function `manage_users(repo: Repository)` that:
- Works with any Repository implementation
- Performs save, find, and delete operations
- Test with both InMemory and File repositories

---

**Expected Output:**
When you run the code, the terminal should show:
```text
=== Testing InMemoryRepository ===
Saved user: True
Found user: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
Deleted user: True
User not found after deletion: None

=== Testing FileRepository ===
Saved user: True
Found user: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
Deleted user: True
User not found after deletion: None

Repository pattern works with both implementations!
```
