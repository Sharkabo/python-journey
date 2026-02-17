# Drills - Abstract Base Classes
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Import ABC and abstractmethod
from abc import ABC, abstractmethod
from typing import Any

# Drill 2: Create an abstract Shape class with abstract area() method
class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def area(self) -> Any:
        pass

# Drill 3: Create Rectangle subclass implementing area()
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self) -> Any:
        return self.length * self.width

# Drill 4: Create Circle subclass implementing area()
from math import pi

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
    
    def area(self) -> Any:
        return pi * self.radius ** 2

# Drill 5: Create an abstract Animal class with speak() method
class Animal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def speak(self) -> Any:
        pass
