# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Fibonacci Generator
Create a generator function `fibonacci(n)` that:
- Uses `yield` to generate Fibonacci numbers
- Generates the first `n` Fibonacci numbers
- Example: fibonacci(10) should yield: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

## Step 2: Create an Infinite Generator
Create a generator `count_up(start=0)` that:
- Counts up infinitely from the start number
- Uses `yield` and a while True loop
- Never stops (user must manually stop iteration)

## Step 3: Create a Generator Expression
Create a generator expression that:
- Generates squares of numbers from 1 to 10
- Compare memory usage concept with list comprehension (mentioned in comment)

## Step 4: Chain Generators Together
Create a function `even_squares(n)` that:
- Uses your count_up() generator
- Filters for even numbers only
- Squares them
- Returns first n results

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Fibonacci sequence (first 10):
0 1 1 2 3 5 8 13 21 34

Infinite counter (first 5):
0 1 2 3 4

Generator expression (squares of 1-10):
1 4 9 16 25 36 49 64 81 100

Even squares (first 5):
0 4 16 36 64
```
