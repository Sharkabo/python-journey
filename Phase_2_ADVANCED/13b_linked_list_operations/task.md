# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Add Insert at Beginning
Add method `insert_at_beginning(data)` to your LinkedList class that:
- Creates a new node
- Sets its next to current head
- Updates head to the new node

## Step 2: Add Insert at Position
Add method `insert_at_position(data, position)` that:
- Inserts a node at the specified position (0-indexed)
- Handles edge cases (beginning, middle, end)

## Step 3: Add Delete Method
Add method `delete(data)` that:
- Finds and removes the first node with matching data
- Returns True if deleted, False if not found
- Handles head deletion correctly

## Step 4: Test All Operations
Test insert at beginning, insert at position, and delete operations.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Initial list:
10 -> 20 -> 30 -> None

After insert at beginning (5):
5 -> 10 -> 20 -> 30 -> None

After insert at position 2 (15):
5 -> 10 -> 15 -> 20 -> 30 -> None

Delete 15: True
After deletion:
5 -> 10 -> 20 -> 30 -> None

Delete 999 (not found): False
Final list:
5 -> 10 -> 20 -> 30 -> None
```
