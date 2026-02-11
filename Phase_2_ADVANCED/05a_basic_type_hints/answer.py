name: str = 'Alice'
age: int = 25
height: float = 1.75
is_student: bool = True

def calculate_bmi(weight: float, height: float) -> float:
    if isinstance(weight, (int, float)) and isinstance(height, (int, float)):
        return weight / height ** 2
    else:
        raise ValueError('Weight and height must be numeric')

def get_average_grade(grades: list[float]) -> float:
    return sum(grades) / len(grades)

def get_user_info(name: str, age: int) -> tuple[str, int, bool]:
    is_adult = age >= 18
    return (name, age, is_adult)