from typing import Protocol, TypeVar, Generic

class Weighable(Protocol):
    def get_weight(self) -> float:
        ...

T = TypeVar ("T", bound = Weighable)

class Book:
    def __init__(self, weight: float = 0.5) -> None:
        self._weight = weight

    def get_weight(self) -> float:
        '''Acquire book's weight'''
        return self._weight

class Laptop:
    def __init__(self, weight: float = 2.0) -> None:
        self._weight = weight

    def get_weight(self) -> float:
        '''Acquire laptop's weight'''
        return self._weight

class ShippingContainer(Generic [T]):
    def __init__(self) -> None:
        self._items: list [T] = []

    def add_item(self, item: T) -> None:
        self._items.append(item)
    
    def total_weight(self) -> float:
        return sum (item.get_weight() for item in self._items)