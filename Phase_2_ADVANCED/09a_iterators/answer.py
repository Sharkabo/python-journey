from typing import Any

class FibonacciIterator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count: int = 0
        self.a, self.b = 0, 1
    
    def __iter__(self)-> Any:
        return self
    
    def __next__(self)-> Any:
        if self.count < self.limit:
            self.count += 1
            result: int = self.a
            self.a, self.b = self.b, (self.a + self.b)
            return result
        else:
            raise StopIteration