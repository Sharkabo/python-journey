# Unit 11: Function Return Values

## 1. What is Return?
Functions can **give back** values using `return`. Think of it like a vending machine: you put in money (parameters), and it returns a snack (return value).

**Syntax:**
```python
def function_name(parameter):
    result = parameter * 2
    return result
```

**Example:**
```python
def add_five(number):
    return number + 5

result = add_five(10)
print(result)  # Prints: 15
```

---

## 2. Using Return Values (Optional)
The power of `return` is that we can store the result and use it later!

**Syntax:**
```python
def function_name():
    if condition:
        return value1
    else:
        return value2
```

**Example:**
```python
def calculate_tax(price):
    return price * 0.1

item_price = 100
tax = calculate_tax(item_price)
total = item_price + tax
print(f"Total: ${total}")  # Total: $110.0
```

---

## Spiral Learning Note
Functions from Unit 07 just performed actions. Now they can **produce values** that we can use in calculations, store in variables, or pass to other functions!
