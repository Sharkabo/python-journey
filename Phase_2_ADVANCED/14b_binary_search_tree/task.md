# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create BST Class with Insert
Create a `BinarySearchTree` class that:
- Uses TreeNode from previous exercise
- Has `insert(value)` method that maintains BST property
- Smaller values go left, larger values go right

## Step 2: Implement Search
Add method `search(value)` that:
- Returns True if value exists in tree
- Returns False if not found
- Uses BST property for efficient search

## Step 3: Implement Find Min and Max
Add methods:
- `find_min()` - returns the smallest value in the tree
- `find_max()` - returns the largest value in the tree

## Step 4: Test Your BST
Insert values, search for them, and find min/max.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Inserting: 50, 30, 70, 20, 40, 60, 80

Search for 40: True
Search for 25: False
Search for 70: True
Search for 100: False

Minimum value: 20
Maximum value: 80

Tree follows BST property: left < root < right
```
