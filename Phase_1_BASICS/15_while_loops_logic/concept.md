# Unit 15: While Loops

## 1. The While Loop
`for` loops run a set number of times. `while` loops run **as long as** a condition is True.

**Syntax:**
```python
while condition:
    # Code to repeat
    # Must change the condition eventually!
```

**Example:**
```python
count = 0
while count < 3:
    print("Run")
    count = count + 1
# Prints "Run" three times
```

---

## 2. Infinite Loops Warning (Optional)
If the condition NEVER becomes False, the loop runs forever. Always ensure something changes inside the loop!

---

## Spiral Learning Note
This is perfect for "Game Loops" where we don't know how many guesses the user needs. Use `while` instead of `for` for uncertain repetitions.
