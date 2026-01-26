# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Implement Inorder Traversal
Create function `inorder(node)` that:
- Traverses: Left -> Root -> Right
- Returns list of values in sorted order (for BST)
- Uses recursion

## Step 2: Implement Preorder Traversal
Create function `preorder(node)` that:
- Traverses: Root -> Left -> Right
- Returns list of values
- Useful for copying tree structure

## Step 3: Implement Postorder Traversal
Create function `postorder(node)` that:
- Traverses: Left -> Right -> Root
- Returns list of values
- Useful for deleting tree (children before parent)

## Step 4: Compare All Three Traversals
Use the same tree and show results of all three traversals side-by-side.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Tree structure:
    50
  30    70
20  40 60  80

Inorder (Left-Root-Right): [20, 30, 40, 50, 60, 70, 80]
Sorted for BST!

Preorder (Root-Left-Right): [50, 30, 20, 40, 70, 60, 80]
Good for copying structure!

Postorder (Left-Right-Root): [20, 40, 30, 60, 80, 70, 50]
Good for deletion!
```
