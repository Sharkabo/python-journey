# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a TreeNode Class
Create a `TreeNode` class that has:
- `value` attribute
- `left` attribute (reference to left child)
- `right` attribute (reference to right child)

## Step 2: Build a Binary Tree Manually
Create a binary tree by:
- Creating individual TreeNode instances
- Manually linking them as parent-child relationships
- Build a tree with at least 3 levels

## Step 3: Implement Simple Traversal
Create a function `print_tree(node, level=0)` that:
- Prints the tree structure with indentation
- Shows the hierarchy visually
- Uses recursion

## Step 4: Count Nodes
Create a function `count_nodes(node)` that:
- Recursively counts all nodes in the tree
- Returns the total count

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Tree Structure:
    1
  2
      5
  3
    4

Tree looks clear and hierarchical with 5 nodes.
Total nodes: 5

Alternative view:
        1
    2
            5
        3
            4
```
