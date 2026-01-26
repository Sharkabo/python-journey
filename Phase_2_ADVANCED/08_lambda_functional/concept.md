# Unit 08: Lambda and Functional Programming

## 1. What is a Lambda Function?
A lambda function is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only ONE expression.

**Syntax:**
```python
lambda arguments: expression
```

**Example:**
```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(5, 3))          # 8
print(add_lambda(5, 3))   # 8

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

---

## 2. map(), filter(), and sorted() with Lambda (Optional)
Use lambda with built-in functions for quick data transformations.

**Syntax:**
```python
map(lambda x: expression, iterable)
filter(lambda x: condition, iterable)
sorted(iterable, key=lambda x: expression)
```

**Example:**
```python
# filter - Select even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# sorted - Sort by length
words = ['apple', 'banana', 'kiwi']
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)  # ['kiwi', 'apple', 'banana']
```

---

## Spiral Learning Note
You know list comprehensions from Phase 1. Lambda extends functional programming concepts. Next you'll learn iterators and generators.
