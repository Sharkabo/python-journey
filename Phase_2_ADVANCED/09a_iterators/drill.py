# Drills - Iterators
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Counter iterator class with __iter__ and __next__
from typing import Any

class Counter:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num
        self.num: int = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.num >= self.max_num:
            raise StopIteration
        self.num += 1
        return self.num

# Drill 2: Create a Reverse iterator for a list
class Reverse_interator:
    def __init__(self, input_list: list) -> None:
        self.input_list = input_list
        self.index = len(self.input_list) - 1

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self.index >= 0:
            result: Any = self.input_list[self.index]
            self.index -= 1
            return result
        else:
            raise StopIteration
        
# Drill 3: Use iter() and next() functions on a list
num_list: list[int] = [1, 2, 3, 4]
iterator = iter(num_list)
print(next(iterator))
print(next(iterator))

# Drill 4: Create a Range iterator (like Python's range())
class MyRange:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# Drill 5: Create a Fibonacci iterator
class Fibonacci_iterator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count: int = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self.count < self.limit:
            self.count += 1
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
        else:
            raise StopIteration

# Drill 6: Create an iterator for reading file lines
class FileLineIterator:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(self.filename, "r", encoding= 'utf-8')
    
    def __iter__(self):
        return self
    
    def __next__(self)-> Any:
        line = self.file.readline()
        if line == "":
            self.file.close()
            raise StopIteration
        return line.strip()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()