# Unit 15c: Searching Algorithms

## 1. Binary Search
Binary search works on sorted arrays with O(log n) time complexity. Much faster than linear search for large datasets.

**Syntax:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check mid element
    return -1  # Not found
```

**Example:**
```python
def binary_search(arr, target):
    """Search for target in sorted array. Returns index or -1."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Found!
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# Usage (array must be sorted!)
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))   # 3
print(binary_search(arr, 6))   # -1 (not found)
print(binary_search(arr, 15))  # 7

# Comparison with linear search
def linear_search(arr, target):
    """O(n) time complexity"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

---

## Spiral Learning Note
Binary search is O(log n), while linear search is O(n). For 1 million items, binary search takes ~20 comparisons vs 1 million for linear! This completes algorithms. Next is the capstone project combining everything.
