# Complete your task here (goals are defined in task.md)

# Step 1: Create a Node Class


# Step 2: Create a LinkedList Class


# Step 3: Implement Size Tracking


# Step 4: Test Your Linked List
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    
    ll.display()
    print(f"Size: {ll.get_size()}")
    print()
    
    print("Adding more elements...")
    ll.append(50)
    ll.append(60)
    
    ll.display()
    print(f"Size: {ll.get_size()}")
