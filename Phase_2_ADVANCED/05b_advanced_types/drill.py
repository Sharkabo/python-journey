# Drills - Advanced Type Hints
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a function that returns Optional[str] (find user by ID)
def find_user(id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(id)

# Drill 2: Create a function with Union[int, str] parameter
def find_grade(grade: int | str) -> int | str:
    return grade

# Drill 3: Create a function with dict[str, int] return type
def find_seat() -> dict[str, int]:
    test_score: dict[str, int] = {}
    return test_score

# Drill 4: Create a function with list[str] parameter and return type
def list_names(names: list[str]) -> list[str]:
    return names

# Drill 5: Create a function with set[int] return type
def try_hint_set() -> set[int]:
    empty_set = set()
    return empty_set

# Drill 6: Create a function with tuple[str, int, float] return type
def try_hint_tuple() -> tuple[str, int, float]:
    testing_tuple = ('what', 1, 0.1)
    return testing_tuple

# Drill 7: Create a function with Optional[dict[str, list[int]]] return
def try_hint_dict() -> dict[str, list[int]] | None:
    data = {"scores": [90, 80, 70]}
    return data

# Drill 8: Create a function accepting Union[list[int], set[int]]
def try_union(data: list[int] | set[int]):
    return sum(data)