# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Countdown Iterator
Create a `Countdown` class that:
- Takes a starting number in `__init__`
- Implements `__iter__()` that returns self
- Implements `__next__()` that counts down and raises StopIteration at 0

## Step 2: Test Your Iterator with for Loop
Use a for loop to iterate through Countdown(5) and print each number.

## Step 3: Test Your Iterator with next()
Create an iterator and manually call `next()` on it 3 times to see the countdown.

## Step 4: Handle StopIteration
Use a try/except block to catch StopIteration when manually calling next() beyond the limit.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Countdown from 5:
5
4
3
2
1

Manual countdown from 3:
3
2
1
Countdown finished! (StopIteration caught)
```
