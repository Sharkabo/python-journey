# Unit 13b: Linked List Operations

## 1. Insert Operation
Insert a node at a specific position in the linked list.

**Syntax:**
```python
def insert(self, position, data):
    new_node = Node(data)
    # Handle insertion logic
```

**Example:**
```python
class LinkedList:
    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Usage
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.insert(1, 2)  # Insert 2 at position 1
ll.delete(2)     # Delete node with data 2
```

---

## Spiral Learning Note
Insert, delete, and search are core linked list operations. Next you'll learn doubly linked lists with bidirectional traversal.
