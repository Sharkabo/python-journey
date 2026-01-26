# Unit 15a: Algorithm Complexity

## 1. Big O Notation
Big O notation describes how an algorithm's runtime grows as input size increases. It helps you choose efficient algorithms.

**Syntax:**
```python
# O(1) - Constant time
# O(n) - Linear time
# O(n²) - Quadratic time
# O(log n) - Logarithmic time
```

**Example:**
```python
# O(1) - Constant
def get_first(arr):
    return arr[0]  # Always one operation

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # n iterations
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # n iterations
        for j in range(n-i-1):  # n iterations
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# O(log n) - Logarithmic
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## Spiral Learning Note
Understanding time complexity helps you write efficient code. O(1) is fastest, O(n²) is slow for large data. Next you'll learn sorting algorithms and their complexities.
