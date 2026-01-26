# Unit 09b: Generators

## 1. What are Generators?
Generators are a simpler way to create iterators. Instead of writing `__iter__` and `__next__`, you just use the `yield` keyword in a function.

**Syntax:**
```python
def generator_function():
    yield value1
    yield value2
```

**Example:**
```python
def count_up_to(max_num):
    num = 1
    while num <= max_num:
        yield num  # Pause here and return num
        num += 1   # Resume here on next call

for n in count_up_to(5):
    print(n)  # 1, 2, 3, 4, 5

# Manual iteration
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

---

## 2. Generator Expressions (Optional)
Even shorter syntax for simple generators.

**Syntax:**
```python
generator = (expression for item in iterable)
```

**Example:**
```python
# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))

# List comprehension (creates entire list)
squares_list = [x**2 for x in range(10)]

# Generators use less memory!
for square in squares_gen:
    print(square)
```

---

## Spiral Learning Note
Unit 09a taught the iterator protocol. Generators make it simple with `yield`. Next you'll learn context managers which also use generators.
