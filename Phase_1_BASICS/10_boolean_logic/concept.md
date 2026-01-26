# Unit 10: Boolean Logic & Operators

## 1. Boolean Values and Comparisons
In Python, `True` and `False` are special values that represent yes/no, on/off.

**Syntax:**
```python
# Comparison operators return True or False
>   # Greater than
<   # Less than
==  # Equal to
!=  # Not equal to
>=  # Greater than or equal to
<=  # Less than or equal to
```

**Example:**
```python
age = 20
print(age > 18)   # True
print(age == 20)  # True
print(age != 25)  # True
```

---

## 2. Logical Operators (Optional)
We can combine multiple conditions using `and`, `or`, and `not`.

**Syntax:**
```python
and  # Both conditions must be True
or   # At least one condition must be True
not  # Reverses True/False
```

**Example:**
```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive!")

if not has_license:
    print("You need a license!")
```

---

## Spiral Learning Note
We used `if` statements in Unit 04, but now we can create more complex conditions! This is essential for real-world decision-making in programs.
