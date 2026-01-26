# Unit 15b: Sorting Algorithms

## 1. Merge Sort
Merge sort is a divide-and-conquer algorithm with O(n log n) time complexity. It's stable and efficient.

**Syntax:**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

**Example:**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

---

## Spiral Learning Note
Merge sort is O(n log n), much better than bubble sort's O(n²). It's stable (maintains order of equal elements) and efficient for large datasets. Next you'll learn searching algorithms.
