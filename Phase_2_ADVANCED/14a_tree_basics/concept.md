# Unit 14a: Tree Basics

## 1. Tree Structure
A tree is a hierarchical data structure with a root node and child nodes. Binary trees have at most two children per node.

**Syntax:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

**Example:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

# Create a simple tree
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Print root and children
print(root.data)        # 1
print(root.left.data)   # 2
print(root.right.data)  # 3
```

---

## Spiral Learning Note
Trees organize data hierarchically. Each node can have children. Essential for file systems, organization charts, and algorithms. Next you'll learn Binary Search Trees (BST).
