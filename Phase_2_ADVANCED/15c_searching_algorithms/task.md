# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Implement Binary Search
Create function `binary_search(arr, target)` that:
- Searches sorted array using divide-and-conquer
- Returns index if found, -1 if not
- Time complexity: O(log n)
- Track number of comparisons

## Step 2: Implement Linear Search (for comparison)
Create function `linear_search(arr, target)` that:
- Searches array sequentially
- Returns index if found, -1 if not
- Time complexity: O(n)
- Track number of comparisons

## Step 3: Visualize Binary Search Steps
Modify binary_search to print:
- Current search range at each step
- Middle element being checked
- Decision made (go left/right/found)

## Step 4: Compare Performance
Test both algorithms on the same data:
- Search for element near the end
- Count comparisons for each
- Show the efficiency difference

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

Binary Search for 25 (with visualization):
Range [0, 14], mid=7, value=15, target > mid
Range [8, 14], mid=11, value=23, target > mid
Range [12, 14], mid=13, value=27, target < mid
Range [12, 12], mid=12, value=25, FOUND!
Result: index 12, comparisons: 4

Linear Search for 25:
Result: index 12, comparisons: 13

Performance: Binary search used 69% fewer comparisons!
For 1 million items: Binary ~20 comparisons vs Linear ~1,000,000
```
