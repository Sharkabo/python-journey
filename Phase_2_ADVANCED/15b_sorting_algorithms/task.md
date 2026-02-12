# Task Description

**Scenario: Sorting the E-Commerce Catalog**

You have a list of `Product` objects (name, price). You need to sort them by price. While Python's `sort()` is great, understanding **Merge Sort** is critical for interviews and understanding divide-and-conquer algorithms.

**Your Goal:**
Implement **Merge Sort** from scratch to sort a list of custom objects based on a specific attribute.

**Objectives:**
1.  Create a `Product` class `(name, price)`.
2.  Create a list of 5 unsorted products.
3.  Implement `merge_sort(products) -> list`:
    - **Base Case:** If list len <= 1, return it.
    - **Divide:** Split list in half.
    - **Conquer:** Recursively call `merge_sort` on left and right halves.
    - **Merge:** Write a `merge(left, right)` helper function that compares `left[0].price` vs `right[0].price` and combines them into a sorted list.
4.  Print the list before and after.

**Success Condition:**
The output list must be sorted by Price ascending.
You must NOT use `list.sort()` or `sorted()`. You must write the recursive logic yourself.
