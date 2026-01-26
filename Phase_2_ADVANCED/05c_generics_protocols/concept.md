# Unit 05c: Type Hints for Classes

## 1. Type Hints for Classes
You can add type hints to class attributes and methods just like functions.

**Syntax:**
```python
class ClassName:
    # Class variable type hint
    class_var: int = 0
    
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
    
    def method(self) -> str:
        return "result"
```

**Example:**
```python
class User:
    def __init__(self, name: str, age: int, email: str):
        self.name: str = name
        self.age: int = age
        self.email: str = email
    
    def get_info(self) -> str:
        return f"{self.name}, {self.age} years old"
    
    def is_adult(self) -> bool:
        return self.age >= 18

user: User = User("Alice", 25, "alice@email.com")
print(user.get_info())
```

---

## 2. Type Hints with Inheritance (Optional)
Type hints work with inheritance to ensure subclasses follow parent class contracts.

**Syntax:**
```python
class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:  # Override with same type
        return "Woof!"
```

**Example:**
```python
def make_animal_speak(animal: Animal) -> str:
    return animal.speak()

dog: Dog = Dog()
cat: Cat = Cat()

print(make_animal_speak(dog))  # Works with any subclass
```

---

## Spiral Learning Note
You learned basic and advanced type hints. Now you apply them to classes. Next you'll learn `*args` and `**kwargs` which also use type hints.
