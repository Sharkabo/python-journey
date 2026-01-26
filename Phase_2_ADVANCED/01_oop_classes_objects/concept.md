# Unit 01: Classes and Objects (OOP Basics)

## 1. What is Object-Oriented Programming?
Object-Oriented Programming (OOP) organizes data and the methods that operate on that data together into "objects".

**Syntax:**
```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
    
    def method_name(self):
        # Method content
        pass
```

**Example:**
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

# Create objects
book1 = Book("Python Basics", "John Smith", 200)
print(book1.get_info())  # Python Basics by John Smith, 200 pages
```

---

## 2. Understanding `self` (Optional)
`self` represents the object instance itself and allows methods to access the object's attributes.

**Syntax:**
```python
class ClassName:
    def __init__(self, param):
        self.attribute = param  # self.attribute is the object's attribute
    
    def method(self):
        # self lets us access the object's attributes
        return self.attribute
```

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

person1 = Person("Alice", 25)
person1.introduce()  # Hi, I'm Alice and I'm 25 years old
```

---

## Spiral Learning Note
You already know functions (Phase 1 Unit 07) and dictionaries (Phase 1 Unit 13). OOP combines these: data + functions = objects. Next you'll learn about Inheritance, which allows classes to be reused.
