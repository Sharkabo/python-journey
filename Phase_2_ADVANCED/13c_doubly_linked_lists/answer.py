# Complete your task here (goals are defined in task.md)

# Step 1: Create a Doubly Linked Node


# Step 2: Create a Doubly Linked List


# Step 3: Implement Backward Traversal


# Step 4: Test Bidirectional Traversal
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    
    dll.display()
    dll.display_reverse()
    print()
    
    print("Adding more elements...")
    dll.append(50)
    dll.append(60)
    
    dll.display()
    dll.display_reverse()
