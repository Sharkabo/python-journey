# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Read a File Using with Statement
Create a file 'sample.txt' with some content, then:
- Use `with open()` to read the file safely
- Print the contents
- Verify the file auto-closes after the with block

## Step 2: Write to a File Using with Statement
Use `with open()` in write mode to:
- Create/overwrite 'output.txt'
- Write 3 lines of text
- Verify auto-close behavior

## Step 3: Demonstrate the Advantage
Show what happens without `with`:
- Open a file normally (without with)
- Read it
- Manually close it
- Comment on why `with` is better

---

**Expected Output:**
When you run the code, the terminal should show:
```text
File contents:
Hello, this is a sample file.
It has multiple lines.
Context managers are useful!

File closed after with block: True

Writing to output.txt...
Write complete! File auto-closed: True

Manual file handling (without with):
Same content read
Manual close required - with statement is safer!
```
