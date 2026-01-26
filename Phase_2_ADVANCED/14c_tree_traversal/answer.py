# Complete your task here (goals are defined in task.md)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 1: Implement Inorder Traversal


# Step 2: Implement Preorder Traversal


# Step 3: Implement Postorder Traversal


# Step 4: Compare All Three Traversals
if __name__ == "__main__":
    # Build BST:
    #       50
    #      /  \
    #    30    70
    #   / \   / \
    #  20 40 60 80
    
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)
    
    print("Tree structure:")
    print("    50")
    print("  30    70")
    print("20  40 60  80")
    print()
    
    in_result = inorder(root)
    print(f"Inorder (Left-Root-Right): {in_result}")
    print("Sorted for BST!")
    print()
    
    pre_result = preorder(root)
    print(f"Preorder (Root-Left-Right): {pre_result}")
    print("Good for copying structure!")
    print()
    
    post_result = postorder(root)
    print(f"Postorder (Left-Right-Root): {post_result}")
    print("Good for deletion!")
