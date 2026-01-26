# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Use Lambda with map()
Create a list of numbers and use `map()` with a lambda function to:
- Square each number
- Convert the result to a list

## Step 2: Use Lambda with filter()
Use `filter()` with a lambda to:
- Filter only even numbers from a list
- Convert the result to a list

## Step 3: Use Lambda with sorted()
Create a list of dictionaries representing students with 'name' and 'grade' keys.
Use `sorted()` with a lambda to sort by grade (highest first).

## Step 4: Combine map() and filter()
Given a list of numbers, use:
1. `filter()` to get only numbers > 5
2. `map()` to square the filtered numbers
3. Chain them together

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]

Original: [1, 2, 3, 4, 5, 6, 7, 8]
Even only: [2, 4, 6, 8]

Students sorted by grade:
Alice: 95
Charlie: 88
Bob: 82

Numbers: [3, 7, 2, 9, 4, 8, 1, 6]
Filtered (>5): [7, 9, 8, 6]
Squared: [49, 81, 64, 36]
```
