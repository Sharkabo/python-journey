# Complete your task here (goals are defined in task.md)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 1: Create BST Class with Insert


# Step 2: Implement Search


# Step 3: Implement Find Min and Max


# Step 4: Test Your BST
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting: {', '.join(map(str, values))}")
    for val in values:
        bst.insert(val)
    print()
    
    # Test search
    print(f"Search for 40: {bst.search(40)}")
    print(f"Search for 25: {bst.search(25)}")
    print(f"Search for 70: {bst.search(70)}")
    print(f"Search for 100: {bst.search(100)}")
    print()
    
    # Test min/max
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    print()
    
    print("Tree follows BST property: left < root < right")
