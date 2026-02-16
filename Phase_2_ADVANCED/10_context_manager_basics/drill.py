# Drills - Context Manager Basics
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Use 'with' statement to open and read a file
def readfile(filename: str):
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# Drill 2: Explain what __enter__ and __exit__ do

# Ans: 
# These two methods construct so called with statement context manager protocol. 
# Enter method is for object initialization.
# Exit insure no matter what the resources can be free.

# Drill 3: Use with statement for multiple file operations
from typing import Any

def read_multiple_files(filelist: list)-> Any:
    for filename in filelist:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                yield line.strip()

# Drill 4: Handle exceptions inside a with block
class Reader:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def handle_exception(self)-> Any:
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                for line in file:
                    yield line.strip()
        except Exception as e:
            print(f'{e}')

# Drill 5: Compare with vs manual file.open() and file.close()
# Main difference is with statement can automatically 
# free ram resources without causing system to failed.