# Drills - @property Decorator
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Rectangle class with _width and _height, use @property for getters
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    @property
    def height(self) -> float:
        return self._height
    
    @property
    def width(self) -> float:
        return self._width
    
    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Height has to be greater than 0')
        self._height = value
    
    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Width has to be greater than 0')
        self._width = value

# Drill 2: Add a computed 'area' property that returns width * height
    @property
    def area(self) -> float:
        return self._height * self._width
    
# Drill 3: Create a Circle class with _radius property and area calculation
import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Radius must be greater than 0')
        self._radius = value
    
    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

# Drill 4: Add setters to Circle.radius that validate radius > 0


# Drill 5: Create a Person class with first_name, last_name, and full_name property
class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, user_input) -> None:
        self._first_name = user_input
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, user_input) -> None:
        self._last_name = user_input
    
    @property
    def full_name(self) -> str:
        return (f'{self.first_name} {self.last_name}')

# Drill 6: Create a Product class with price property and setter that validates price >= 0
class Product:
    def __init__(self, price) -> None:
        self.price = price
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value) -> None:
        if value <= 0:
            raise ValueError('Price should be greater than zero')
        self._price = value

# Drill 7: Create a Temperature class with celsius property and fahrenheit conversion
class Temperature:
    def __init__(self, celsius) -> None:
        self.celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value) -> None:
        try:
            val = float(value)
            if val < -273.15:
                raise ValueError("Temperature cannot be below Absolute Zero (-273.15°C)")
            self._celsius = val
        except ValueError as e:
            if "Absolute Zero" in str(e):
                raise
            raise ValueError('Please input number and number only')

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

# Drill 8: Create a BankAccount with balance property (read-only, no setter)
class BankAccount:
    def __init__(self, balance) -> None:
        try:
            self._balance = float(balance)
        except ValueError:
            raise ValueError('Initial balance must be a number')
    
    @property
    def balance(self) -> float:
        return self._balance

# Drill 9: Create a Book class with _pub_year and computed 'age' property
import datetime

class Book:
    def __init__(self, pub_year) -> None:
        self.pub_year = pub_year
    
    @property
    def pub_year(self) -> int:
        return self._pub_year
    
    @pub_year.setter
    def pub_year(self, value: int) -> None:
        try:
            val = int(value)
            if val > datetime.date.today().year:
                raise ValueError('Books from the future are not supported yet!')
            self._pub_year = val
        except ValueError:
            raise ValueError('Published year must be a number')
    
    @property
    def age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.pub_year

# Drill 10: Create a Square class with side property (both getter and setter)
class Square:
    def __init__(self, side) -> None:
        self.side = side
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, value) -> None:
        try:
            val = float(value)
            self._side = val
        except ValueError:
            raise ValueError('Side must be number and number only')
    
    @property
    def area(self) -> float:
        return self.side **2
