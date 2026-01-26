# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create Typed Variables
Create variables with type hints for:
- A person's name (string)
- Their age (integer)
- Their height in meters (float)
- Whether they are a student (boolean)

## Step 2: Create a Typed Function
Create a function `calculate_bmi(weight: float, height: float) -> float` that:
- Takes weight in kg and height in meters
- Returns the BMI (weight / height²)
- Includes proper type hints for parameters and return value

## Step 3: Create a Function with List Type Hints
Create a function `get_average_grade(grades: list[float]) -> float` that:
- Takes a list of grade scores
- Returns the average grade
- Uses proper collection type hints

## Step 4: Create a Function Returning Tuple
Create a function `get_user_info(name: str, age: int) -> tuple[str, int, bool]` that:
- Takes name and age as parameters
- Returns a tuple with: (name, age, is_adult)
- is_adult should be True if age >= 18

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
