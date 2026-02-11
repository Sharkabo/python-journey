# Task Description

Open `answer.py` in this folder and complete the following objectives:

In this exercise, you'll practice adding **type hints** to variables and functions. Type hints help make your code more readable and catch potential bugs early. You won't be creating any classes - just simple variables and functions with proper type annotations.

## Step 1: Create Variables with Type Hints

Create four variables that represent information about a person. Each variable should have a type hint annotation:

- `name: str` - A person's name (use "Alice")
- `age: int` - Their age in years (use 25)
- `height: float` - Their height in meters (use 1.75)
- `is_student: bool` - Whether they are currently a student (use True)

Then, print each variable with a descriptive label.

## Step 2: Write a BMI Calculator Function

Create a function called `calculate_bmi` that calculates Body Mass Index:

- **Function signature**: `calculate_bmi(weight: float, height: float) -> float`
- **Parameters**: 
  - `weight` - person's weight in kilograms
  - `height` - person's height in meters
- **Returns**: The BMI value (formula: weight / height²)
- **Important**: Include type hints for both parameters and the return value

Test this function by calculating and printing the BMI for weight=70kg and height=1.75m.

## Step 3: Write an Average Grade Calculator Function

Create a function called `get_average_grade` that calculates the average from a list of grades:

- **Function signature**: `get_average_grade(grades: list[float]) -> float`
- **Parameter**: 
  - `grades` - a list of grade scores (floats)
- **Returns**: The average of all grades in the list
- **Important**: Use the modern `list[float]` type hint to specify this is a list of floats

Test this function with the grades: [85.5, 92.0, 85.5] and print the result.

## Step 4: Write a User Info Function That Returns a Tuple

Create a function called `get_user_info` that packages user information into a tuple:

- **Function signature**: `get_user_info(name: str, age: int) -> tuple[str, int, bool]`
- **Parameters**:
  - `name` - person's name (string)
  - `age` - person's age (integer)
- **Returns**: A tuple containing three values: `(name, age, is_adult)`
  - `is_adult` should be `True` if the person is 18 or older, `False` otherwise
- **Important**: The return type hint shows the tuple contains exactly 3 items: a string, an int, and a bool

Test this function twice:
1. Call it with name="Bob" and age=17
2. Call it with name="Alice" and age=25

Print both results.

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Name: Alice
Age: 25
Height: 1.75
Is Student: True
BMI: 22.86
Average Grade: 87.67
User Info: ('Bob', 17, False)
User Info: ('Alice', 25, True)
```
