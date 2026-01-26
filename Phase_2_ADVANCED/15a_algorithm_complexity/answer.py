# Complete your task here (goals are defined in task.md)
import time

# Step 1: Implement O(n) Linear Search


# Step 2: Implement O(n²) Bubble Sort


#Step 3: Compare Performance


# Step 4: Demonstrate Big O Differences
if __name__ == "__main__":
    print("Linear Search O(n):")
    arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    result, comparisons = linear_search(arr1, 50)
    print(f"Found 50 at index {result}")
    print(f"Comparisons: {comparisons}")
    print()
    
    result, comparisons = linear_search(arr1, 99)
    print(f"Not found 99")
    print(f"Comparisons: {comparisons}")
    print()
    
    print("Bubble Sort O(n²):")
    arr2 = [64, 34, 25, 12, 22]
    print(f"Original: {arr2}")
    sorted_arr, comparisons = bubble_sort_demo(arr2.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Comparisons: {comparisons}")
    print()
    
    print("Performance Comparison:")
    small_arr = list(range(10, 0, -1))
    
    start = time.time()
    linear_search(small_arr, 1)
    linear_time = time.time() - start
    
    start = time.time()
    bubble_sort_demo(small_arr.copy())
    bubble_time = time.time() - start
    
    print(f"Small array (n=10):")
    print(f"  Linear search: {linear_time:.4f} seconds")
    print(f"  Bubble sort: {bubble_time:.4f} seconds")
    print()
    print("The difference grows with larger n!")
