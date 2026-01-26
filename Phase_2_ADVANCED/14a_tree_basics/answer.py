# Complete your task here (goals are defined in task.md)

# Step 1: Create a TreeNode Class


# Step 2: Build a Binary Tree Manually


# Step 3: Implement Simple Traversal


# Step 4: Count Nodes


# Test your code
if __name__ == "__main__":
    # Build tree:
    #       1
    #      / \
    #     2   3
    #    /   /
    #   5   4
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.right.left = TreeNode(4)
    
    print("Tree Structure:")
    print_tree(root)
    print()
    
    total = count_nodes(root)
    print(f"Total nodes: {total}")
    
    # Alternative visualization
    print("\nAlternative view:")
    print_tree(root)
