# Unit 13c: Doubly Linked Lists

## 1. Doubly Linked Node
Each node has references to both the next and previous nodes, allowing bidirectional traversal.

**Syntax:**
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

**Example:**
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def traverse_backwards(self):
        current = self.head
        while current and current.next:
            current = current.next
        
        while current:
            print(current.data)
            current = current.prev

# Usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.traverse_backwards()  # 3, 2, 1
```

---

## Spiral Learning Note
Doubly linked lists can traverse both directions. Used in browser history, undo/redo systems, and music playlists. Next you'll learn tree data structures.
