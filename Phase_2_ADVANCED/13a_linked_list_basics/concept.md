# Unit 13a: Linked List Basics

## 1. What is a Linked List?
A sequence of nodes where each node contains data and a reference to the next node. Unlike arrays, linked lists don't need contiguous memory.

**Syntax:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

**Example:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
```

---

## Spiral Learning Note
Linked lists are a fundamental data structure. Each node points to the next, allowing dynamic size. Next you'll learn linked list operations like insert and delete.
