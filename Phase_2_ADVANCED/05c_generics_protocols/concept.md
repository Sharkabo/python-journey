# Unit 05c: Generics and Protocols

## 1. Generics (TypeVars)
Generics allow you to write flexible components that work with multiple types while maintaining type safety. Use `TypeVar` to create a placeholder type.

**Syntax:**
```python
from typing import TypeVar

T = TypeVar("T")  # Define a generic type variable

def get_first(items: list[T]) -> T:
    return items[0]
```

**Example:**
```python
from typing import TypeVar

T = TypeVar("T")

class Stack:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

box = Stack()
box.push(10)      # T becomes int
# box.push("hi")  # Type Checker Error!
```

---

## 2. Protocols (Structural Subtyping)
Protocols define "duck typing" rules. An object follows a protocol if it has the required methods, even if it doesn't inherit from a specific class.

**Syntax:**
```python
from typing import Protocol

class CanFly(Protocol):
    def fly(self) -> None:
        ...  # Empty body
```

**Example:**
```python
from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> str:
        ...

class Bird:
    def fly(self) -> str:
        return "Flap flap"

class Airplane:
    def fly(self) -> str:
        return "Whoosh"

def make_it_fly(obj: Flyer):
    print(obj.fly())

make_it_fly(Bird())      # Works!
make_it_fly(Airplane())  # Works!
```

---

## Spiral Learning Note
You moved from basic types to Generics (flexible types) and Protocols (structural types). These are advanced tools for building large, robust systems. Next you'll learn about `*args` and `**kwargs`.
