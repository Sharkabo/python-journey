# Complete your task here (goals are defined in task.md)

# Global counters for tracking operations
divisions = 0
merges = 0

# Step 1: Implement Merge Function


# Step 2: Implement Merge Sort


# Step 3: Add Step Counter (integrated in Steps 1 & 2)

# Step 4: Compare with Bubble Sort
def bubble_sort_operations(arr):
    """Bubble sort that counts operations"""
    n = len(arr)
    operations = 0
    for i in range(n):
        for j in range(n - i - 1):
            operations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, operations


# Test your code
if __name__ == "__main__":
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {test_arr}")
    print()
    
    # Reset counters
    divisions = 0
    merges = 0
    
    print("Merge Sort:")
    sorted_arr = merge_sort(test_arr.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Divisions: {divisions}")
    print(f"Merges: {merges}")
    print()
    
    # Compare with bubble sort
    print("Comparison with Bubble Sort (same array):")
    _, bubble_ops = bubble_sort_operations(test_arr.copy())
    merge_ops = divisions + merges
    
    print(f"Merge Sort operations: ~{merge_ops}")
    print(f"Bubble Sort operations: ~{bubble_ops}")
    print()
    print("Merge sort is much more efficient!")
    print("O(n log n) vs O(n²)")
