# Drills - Magic Methods
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a class Person with name and age, implement __str__ to return "Name: {name}, Age: {age}"
class Person:
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

# Drill 2: Implement __repr__ for Person to return "Person(name='{name}', age={age})"
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age='{self.age})"

# Drill 3: Create a class Temperature with celsius attribute, implement __eq__ to compare temperatures


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

# Drill 4: Implement __lt__ and __gt__ for Temperature to enable comparisons
    def __lt__(self, other) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius < other.celsius
    
    def __gt__(self, other) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius > other.celsius

# Drill 5: Create a class ShoppingCart, implement __len__ to return number of items
class ShoppingCart:
    def __init__(self, item) -> None:
        self.item = item
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
# Drill 6: Implement __getitem__ for ShoppingCart to allow indexing like cart[0]
    def __getitem__(self, index):
        return self.items[index]

# Drill 7: Create a class Vector with x and y attributes, implement __add__ to add two vectors
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

# Drill 8: Implement __str__ for Vector to return "(x, y)"
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

# Drill 9: Create a class BookCollection, implement __contains__ to check if a book title exists
class BookCollection:
    def __init__(self, books: list) -> None:
        self.books = books
    
    def __contains__(self, book):
        return book in self.books

# Drill 10: Create any class and implement __call__ to make the object callable like a function
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __call__(self) -> None:
        print ('You did it!')