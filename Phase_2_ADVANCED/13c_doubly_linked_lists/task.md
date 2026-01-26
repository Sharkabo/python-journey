# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Doubly Linked Node
Create a `DNode` class that has:
- `data` attribute
- `next` attribute (reference to next node)
- `prev` attribute (reference to previous node)

## Step 2: Create a Doubly Linked List
Create a `DoublyLinkedList` class with:
- `head` and `tail` attributes
- `append(data)` method that updates both next and prev pointers
- Update both head and tail appropriately

## Step 3: Implement Backward Traversal
Add method `display_reverse()` that:
- Starts from tail
- Traverses backward using prev pointers
- Prints the list in reverse order

## Step 4: Test Bidirectional Traversal
Create a list, add elements, and traverse both forward and backward.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Forward: 10 <-> 20 <-> 30 <-> 40 <-> None
Backward: 40 <-> 30 <-> 20 <-> 10 <-> None

Adding more elements...
Forward: 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> 60 <-> None
Backward: 60 <-> 50 <-> 40 <-> 30 <-> 20 <-> 10 <-> None
```
