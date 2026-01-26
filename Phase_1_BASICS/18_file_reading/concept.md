# Unit 18: File Reading

## 1. Reading Files
We can read text files (like `.txt`). We use `with open(...)` because it automatically closes the file for us.

**Syntax:**
```python
with open("filename.txt", "r") as f:
    content = f.read()
```

**Example:**
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line)
```

---

## Spiral Learning Note
Variables (Unit 01) disappear when the program ends. Files allow data to survive!
