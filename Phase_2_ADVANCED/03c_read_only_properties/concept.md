# Unit 03c: Read-Only Properties

## 1. Read-Only Properties
You can create read-only properties by defining only the getter without a setter.

**Syntax:**
```python
class ClassName:
    @property
    def read_only_value(self):
        return self._value  # No setter defined
```

**Example:**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Read-only property (computed)"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)    # 78.53975
circle.radius = 10    # OK, has setter
print(circle.area)    # 314.159 (automatically updated)
# circle.area = 100   # AttributeError: can't set attribute
```

---

## 2. Property Deleter (Optional)
You can define a deleter for properties using `@property_name.deleter`.

**Syntax:**
```python
@property_name.deleter
def property_name(self):
    # Cleanup code
    self._value = None
```

**Example:**
```python
class User:
    def __init__(self, username):
        self._email = None
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value
    
    @email.deleter
    def email(self):
        print(f"Deleting email: {self._email}")
        self._email = None

user = User("alice")
user.email = "alice@example.com"
del user.email  # Deleting email: alice@example.com
```

---

## Spiral Learning Note
You learned `@property` in Unit 03b. Now you understand read-only properties and deleters. Next you'll learn magic methods that power properties behind the scenes.
