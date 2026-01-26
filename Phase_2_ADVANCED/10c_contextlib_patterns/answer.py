# Complete your task here (goals are defined in task.md)
from contextlib import contextmanager, suppress
import os

# Step 1: Create Context Manager with @contextmanager


# Step 2: Use suppress() from contextlib (already imported above)


# Step 3: Create a Nested Context Manager


# Test your code
if __name__ == "__main__":
    # Test Step 1: Temporary file
    print("Writing to temporary file...")
    with temporary_file() as f:
        f.write("This is temporary data\n")
        print("Temp file created and used successfully")
    print("Temp file cleaned up!")
    print()
    
    # Test Step 2: suppress
    print("Trying to delete non-existent file...")
    with suppress(FileNotFoundError):
        os.remove("does_not_exist.txt")
    print("File doesn't exist, but no error raised!")
    print("Code continues normally.")
    print()
    
    # Test Step 3: change_directory
    original = os.getcwd()
    print(f"Current dir: {original}")
    
    with change_directory("/tmp"):
        print(f"Changed to: {os.getcwd()}")
        print(f"Working in: {os.getcwd()}")
    
    print(f"Restored to: {os.getcwd()}")
