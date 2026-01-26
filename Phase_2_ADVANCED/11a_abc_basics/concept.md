# Unit 11a: ABC Basics

## 1. What are Abstract Base Classes?
ABCs (Abstract Base Classes) define an interface that subclasses must implement. They enforce that certain methods are implemented.

**Syntax:**
```python
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    @abstractmethod
    def required_method(self):
        pass
```

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # 15
```

---

## Spiral Learning Note
ABCs enforce interfaces using @abstractmethod. Subclasses must implement all abstract methods. Common in large projects for consistency.
