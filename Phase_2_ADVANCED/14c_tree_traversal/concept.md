# Unit 14c: Tree Traversal

## 1. DFS Traversal
Depth-First Search (DFS) has three main traversal orders: inorder, preorder, and postorder.

**Syntax:**
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
```

**Example:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    """Left -> Root -> Right"""
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    """Root -> Left -> Right"""
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    """Left -> Right -> Root"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# Create tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder:  ", end="")
inorder(root)    # 4 2 5 1 3

print("\nPreorder: ", end="")
preorder(root)   # 1 2 4 5 3

print("\nPostorder:", end="")
postorder(root)  # 4 5 2 3 1
```

---

## Spiral Learning Note
Different traversal orders serve different purposes: inorder gives sorted order for BST, preorder is used for copying trees, postorder is used for deletion. This completes Phase 2 data structures.
