# Unit 14b: Binary Search Tree

## 1. BST Insert
A Binary Search Tree (BST) maintains sorted order: left children are smaller, right children are larger.

**Syntax:**
```python
class BST:
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
```

**Example:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_recursive(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert_recursive(node.right, data)
            else:
                node.right = TreeNode(data)
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

# Usage
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.search(3))  # True
print(bst.search(10)) # False
```

---

## Spiral Learning Note
BST maintains sorted order enabling O(log n) search time. Next you'll learn tree traversal algorithms (inorder, preorder, postorder).
