# Unit 19: File Writing

## 1. Writing to Files
To save data, we use Write mode (`"w"`). **WARNING:** `"w"` overwrites the whole file!

**Syntax:**
```python
with open("filename.txt", "w") as f:
    f.write("text to save")
```

**Example:**
```python
with open("output.txt", "w") as f:
    f.write("This is saved forever.")

# Append mode (adds to end)
with open("output.txt", "a") as f:
    f.write("\nNew line added.")
```

---

## Spiral Learning Note
Now we can save our "ToDo List" (Unit 05) or game high scores so they're still there tomorrow.
