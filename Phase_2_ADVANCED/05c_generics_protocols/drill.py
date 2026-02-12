# Drills - Generics and Protocols
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Define a generic TypeVar 'T'
from typing import TypeVar

T = TypeVar("T")

# Drill 2: Define a function 'echo' that accepts and returns the same generic type T
def echo(item: T) -> T:
    return item

# Drill 3: Define a generic function 'first' that returns the first item of a List[T]
def first(items: list[T]) -> T:
    return items[0]

# Drill 4: Define a generic class 'Box' that holds an item of type T
from typing import Generic

class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item

# Drill 5: Define a Protocol 'Flyer' with a 'fly(self) -> None' method
from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> None:
        ...
# Drill 6: Create a class 'Bird' that satisfies the 'Flyer' protocol
class Bird():
    def fly(self) -> None:
        print('I think I nailed it. Hahaha')