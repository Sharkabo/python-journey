# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Function Using *args
Create a function `sum_all(*args: int) -> int` that:
- Accepts any number of integer arguments
- Returns the sum of all arguments
- Use *args to collect variadic arguments

## Step 2: Create a Function Using **kwargs
Create a function `create_user(**kwargs: str) -> dict[str, str]` that:
- Accepts any number of keyword arguments
- Returns a dictionary with all the key-value pairs
- Print each key-value pair inside the function

## Step 3: Combine *args and **kwargs
Create a function `flexible_function(required: str, *args: int, **kwargs: str) -> None` that:
- Takes one required parameter
- Accepts additional positional arguments via *args
- Accepts additional keyword arguments via **kwargs
- Prints all parameters in a formatted way

## Step 4: Use *args to Unpack
Create a function `calculate_stats(numbers: list[int]) -> tuple[int, int, float]` that returns (min, max, average).
Then call `sum_all()` by unpacking the list using the `*` operator.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Sum: 15
Sum with unpacking: 21

User data:
name: Alice
age: 25
email: alice@example.com
User dict: {'name': 'Alice', 'age': '25', 'email': 'alice@example.com'}

Flexible function called:
Required: Hello
Args: (1, 2, 3)
Kwargs: {'city': 'NYC', 'country': 'USA'}

Stats: min=1, max=9, avg=5.0
Sum of stats list: 45
```
