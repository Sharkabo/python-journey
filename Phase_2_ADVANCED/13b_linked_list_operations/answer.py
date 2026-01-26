# Complete your task here (goals are defined in task.md)

# Copy your Node and LinkedList from 13a, then add these operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Step 1: Add Insert at Beginning
    
    
    # Step 2: Add Insert at Position
    
    
    # Step 3: Add Delete Method


# Step 4: Test All Operations
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    print("Initial list:")
    ll.display()
    print()
    
    ll.insert_at_beginning(5)
    print("After insert at beginning (5):")
    ll.display()
    print()
    
    ll.insert_at_position(15, 2)
    print("After insert at position 2 (15):")
    ll.display()
    print()
    
    result = ll.delete(15)
    print(f"Delete 15: {result}")
    print("After deletion:")
    ll.display()
    print()
    
    result = ll.delete(999)
    print(f"Delete 999 (not found): {result}")
    print("Final list:")
    ll.display()
