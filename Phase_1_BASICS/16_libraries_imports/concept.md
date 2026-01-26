# Unit 16: Libraries & Imports

## 1. Using Modules
Python comes with batteries included! You don't have to write everything yourself. We use `import` to load ready-made tools.

**Syntax:**
```python
import module_name

result = module_name.function()
```

**Example:**
```python
import random

number = random.randint(1, 10)  # Random number 1-10
print(number)

coin = random.choice(["heads", "tails"])
print(coin)
```

---

## Spiral Learning Note
Remember Unit 02 (Math) and guessing games? Now we can make games fun with REAL random numbers instead of a fixed secret number!
