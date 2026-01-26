# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Implement Merge Function
Create function `merge(left, right)` that:
- Takes two sorted arrays
- Merges them into one sorted array
- Returns the merged result

## Step 2: Implement Merge Sort
Create function `merge_sort(arr)` that:
- Recursively divides array in half
- Calls merge() to combine sorted halves
- Time complexity: O(n log n)

## Step 3: Add Step Counter
Modify merge_sort to count:
- Number of divisions
- Number of merges
- Show the recursive process

## Step 4: Compare with Bubble Sort
Sort the same array with both:
- Merge sort O(n log n)
- Bubble sort O(n²) (from previous exercise)
- Compare the number of operations

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Original array: [38, 27, 43, 3, 9, 82, 10]

Merge Sort:
Sorted: [3, 9, 10, 27, 38, 43, 82]
Divisions: 6
Merges: 6

Comparison with Bubble Sort (same array):
Merge Sort operations: ~24
Bubble Sort operations: ~49

Merge sort is much more efficient!
O(n log n) vs O(n²)
```
