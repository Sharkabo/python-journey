# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Implement O(n) Linear Search
Create function `linear_search(arr, target)` that:
- Searches through array sequentially  
- Returns index if found, -1 if not
- Time complexity: O(n)

## Step 2: Implement O(n²) Bubble Sort
Create function `bubble_sort_demo(arr)` that:
- Uses nested loops to sort
- Counts comparisons made
- Time complexity: O(n²)

## Step 3: Compare Performance
Create function `measure_time(func, *args)` that:
- Measures execution time of a function
- Returns elapsed time in seconds
- Use `time` module

## Step 4: Demonstrate Big O Differences
Test with different input sizes and show how:
- O(n) scales linearly
- O(n²) scales quadratically
- Compare actual run times

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Linear Search O(n):
Found 50 at index 4
Comparisons: 5

Not found 99
Comparisons: 10

Bubble Sort O(n²):
Original: [64, 34, 25, 12, 22]
Sorted: [12, 22, 25, 34, 64]
Comparisons: 10

Performance Comparison:
Small array (n=10):
  Linear search: 0.0001 seconds
  Bubble sort: 0.0002 seconds

The difference grows with larger n!
```
