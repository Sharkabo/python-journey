# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create Context Manager with @contextmanager
Import `contextmanager` from contextlib and create a `temporary_file()` context manager that:
- Opens a temp file in write mode (yield the file handle)
- Automatically closes and deletes the file after use
- Uses try/finally to ensure cleanup

## Step 2: Use suppress() from contextlib
Import `suppress` and use it to:
- Ignore FileNotFoundError when trying to delete a non-existent file
- Show that code continues even if error occurs

## Step 3: Create a Nested Context Manager
Use `@contextmanager` to create `change_directory(path)` that:
- Saves current directory
- Changes to new directory (yield)
- Restores original directory in finally block
- Import `os` module

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Writing to temporary file...
Temp file created and used successfully
Temp file cleaned up!

Trying to delete non-existent file...
File doesn't exist, but no error raised!
Code continues normally.

Current dir: /Users/ianchen/development/python_projects/python-journey/PHASE_2_ADVANCED_PYTHON/10c_contextlib_patterns
Changed to: /tmp
Working in: /tmp
Restored to: /Users/ianchen/development/python_projects/python-journey/PHASE_2_ADVANCED_PYTHON/10c_contextlib_patterns
```
