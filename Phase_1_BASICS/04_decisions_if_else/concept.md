# Unit 04: Making Decisions (If/Else)

## 1. Conditions
We use `if` statements to run code ONLY if a condition is true.

**Syntax:**
```python
if condition:
    # Code to run if True
elif another_condition:
    # Code to run if first is False but this is True
else:
    # Code to run if all above are False
```

**Example:**
```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Study harder")
```

---

## 2. Comparison Operators (Optional)
Used to compare values in conditions.

**Syntax:**
```python
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

---

## Spiral Learning Note
We can now make our programs smart! We can take `input` (Unit 03), convert it to a number (Unit 02), and check its value using `if`.
