# Unit 03b: The @property Decorator

## 1. The @property Decorator
The `@property` decorator allows you to define methods that can be accessed like attributes. This gives you control over how attributes are accessed and modified.

**Syntax:**
```python
class ClassName:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Getter method"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Setter method"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value
```

**Example:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.celsius = 30       # Calls setter with validation
```

---

## 2. Computed Properties (Optional)
Properties can compute values on the fly without storing them.

**Syntax:**
```python
@property
def computed_value(self):
    return self.value1 * self.value2  # Computed from other attributes
```

**Example:**
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 10)
print(rect.area)  # 50 (computed on the fly)
```

---

## Spiral Learning Note
Unit 03a taught encapsulation. Now you use `@property` for elegant access. Next you'll learn about read-only properties and magic methods.
