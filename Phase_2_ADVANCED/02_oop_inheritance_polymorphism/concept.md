# Unit 02: Inheritance and Polymorphism

## 1. What is Inheritance?
Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and creates hierarchical relationships.

**Syntax:**
```python
class ParentClass:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def parent_method(self):
        return "This is from parent"

class ChildClass(ParentClass):  # Inherit from ParentClass
    def child_method(self):
        return "This is from child"
```

**Example:**
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):  # Override parent method
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"

dog = Dog("Buddy", 3)
print(dog.make_sound())  # Woof!
print(dog.fetch())       # Buddy is fetching the ball
```

---

## 2. Using super() (Optional)
The `super()` function allows you to call methods from the parent class.

**Syntax:**
```python
class ChildClass(ParentClass):
    def __init__(self, child_param, parent_param):
        super().__init__(parent_param)  # Call parent's __init__
        self.child_param = child_param
```

**Example:**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

manager = Manager("Alice", 80000, "Engineering")
print(f"{manager.name} - {manager.department}")
```

---

## Spiral Learning Note
In Unit 01, you learned to create classes. Inheritance builds on this by allowing classes to share and extend functionality. Next you'll learn Encapsulation to protect data in classes.
