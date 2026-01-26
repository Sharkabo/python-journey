# Complete your task here (goals are defined in task.md)
import math

# Step 1: Implement Binary Search


# Step 2: Implement Linear Search (for comparison)


# Step 3: Visualize Binary Search Steps (integrated in Step 1)

# Step 4: Compare Performance
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    target = 25
    
    print(f"Array: {arr}")
    print()
    
    print(f"Binary Search for {target} (with visualization):")
    bin_idx, bin_comps = binary_search(arr, target)
    print(f"Result: index {bin_idx}, comparisons: {bin_comps}")
    print()
    
    print(f"Linear Search for {target}:")
    lin_idx, lin_comps = linear_search(arr, target)
    print(f"Result: index {lin_idx}, comparisons: {lin_comps}")
    print()
    
    # Performance comparison
    if bin_comps < lin_comps:
        reduction = ((lin_comps - bin_comps) / lin_comps) * 100
        print(f"Performance: Binary search used {reduction:.0f}% fewer comparisons!")
    
    # Theoretical comparison for larger data
    n = 1_000_000
    binary_max = math.ceil(math.log2(n))
    print(f"For 1 million items: Binary ~{binary_max} comparisons vs Linear ~{n:,}")
