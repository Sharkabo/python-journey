# Unit 09: String Methods & Formatting

## 1. Common String Methods
Strings (text) have built-in "tools" called **methods** that help us manipulate them.

**Syntax:**
```python
text.upper()      # Convert to uppercase
text.lower()      # Convert to lowercase
text.strip()      # Remove whitespace from ends
text.replace(old, new)  # Replace text
```

**Example:**
```python
text = "  Hello World  "
print(text.upper())   # "  HELLO WORLD  "
print(text.strip())   # "Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "
```

---

## 2. F-Strings (Modern Formatting) (Optional)
F-strings let us insert variables directly into text using `f""` and `{}`.

**Syntax:**
```python
f"Text {variable} more text"
```

**Example:**
```python
name = "Ian"
age = 20
print(f"My name is {name} and I am {age} years old")
# Prints: My name is Ian and I am 20 years old
```

---

## Spiral Learning Note
We learned about strings in Unit 01, but now we can manipulate them! This is crucial for processing user input (Unit 03) and working with files later.
