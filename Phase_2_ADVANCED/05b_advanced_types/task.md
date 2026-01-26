# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Function with Dict Type Hints
Create a function `count_words(text: str) -> dict[str, int]` that:
- Takes a string of text
- Returns a dictionary where keys are words and values are their counts
- Use proper dict type hints

## Step 2: Create a Function with Optional Type
Create a function `find_user(user_id: int, users: dict[int, str]) -> Optional[str]` that:
- Takes a user_id and a dictionary of users
- Returns the username if found, None if not found
- Import and use `Optional` from typing

## Step 3: Create a Function with Union Type
Create a function `process_input(value: int | str) -> str` that:
- Accepts either an integer or string
- Returns a formatted string: "Number: X" if int, "Text: X" if str
- Use the `|` operator for Union type (Python 3.10+)

## Step 4: Create a Function with Set Type Hints
Create a function `get_unique_tags(posts: list[dict[str, list[str]]]) -> set[str]` that:
- Takes a list of post dictionaries (each has a 'tags' key with list of strings)
- Returns a set of all unique tags across all posts
- Use nested collection type hints

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Word counts: {'hello': 2, 'world': 1, 'python': 1}
User found: Alice
User not found: None
Process int: Number: 42
Process str: Text: hello
Unique tags: {'python', 'tutorial', 'coding', 'tips', 'beginner'}
```
