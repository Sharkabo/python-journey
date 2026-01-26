# Drills - Read-Only Properties
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Person class with read-only 'id' property
class Person:
    def __init__(self, id) -> None:
        self._id = id
    
    @property
    def id(self) -> int:
        return self._id

# Drill 2: Create a Book class with read-only ISBN property
class Book:
    def __init__(self, isbn) -> None:
        self._isbn = isbn

    @property
    def isbn(self) -> int:
        return self._isbn
# Drill 3: Create a Student with computed full_name from first and last names
class Student:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.isalpha():
           self._first_name = value.capitalize()
        else:
           raise ValueError('First name should contain only alphabets')
        
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.isalpha():
           self._last_name = value.capitalize()
        else:
           raise ValueError('Last name should contain only alphabets')
    
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

# Drill 4: Create a Car with computed 'age' from current year and manufacture year
import datetime

class Car:
    def __init__(self, manufacture_year) -> None:
        self.manufacture_year = manufacture_year
    
    @property
    def manufacture_year(self) -> int:
        return self._manufacture_year
    
    @manufacture_year.setter
    def manufacture_year(self, value: int) -> None:
        try:
            val = int(value)
        except ValueError:
            raise ValueError('Manufacture year should be numeric')
        
        current_year = datetime.date.today().year
        if val > current_year:
            raise ValueError('We don\'t deal with future setup')
        else:
            self._manufacture_year = val
        
    @property
    def age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.manufacture_year

# Drill 5: Create a Product with read-only id and editable name/price
class Product:
    def __init__(self, id, name, price) -> None:
        self._id = id
        self.name = name
        self.price = price
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        try:
            val = float(value)
        except ValueError:
            raise ValueError('Price should be numeric')
        
        if val > 0:
            self._price = val
        else:
            raise ValueError('Price should be greater than zero')
        
# Drill 6: Create Animal parent class with sound property
class Animal:
    def __init__(self, sound) -> None:
        self.sound = sound
    
    @property
    def sound(self) -> str:
        return self._sound
    
    @sound.setter
    def sound(self, value: str) -> None:
        if value.isalpha():
            self._sound = value
        else:
            raise ValueError('Sound should contain only Alphabets')

# Drill 7: Create Dog subclass that overrides sound property
class Dog(Animal):
    def __init__(self, sound) -> None:
        super().__init__(sound)

    @property
    def sound(self) -> str:
        return f"{self._sound.upper()}! (Woof! Woof!)"
    
    @sound.setter
    def sound(self, value: str) -> None:
        assert Animal.sound.fset is not None
        Animal.sound.fset(self,value)

# Drill 8: Create Account with read-only account_number
class Account:
    def __init__(self, account_number) -> None:
        self._account_number = account_number
    
    @property
    def account_number(self) -> int:
        return self._account_number

# Drill 9: Create Employee class with annual_salary property and computed read-only monthly_salary property (annual_salary / 12)
class Employee:
    def __init__(self, annual_salary) -> None:
        self.annual_salary = annual_salary
    
    @property
    def annual_salary(self) -> float:
        return self._annual_salary
    
    @annual_salary.setter
    def annual_salary(self, value: float) -> None:
        try: 
            val = float(value)
        except ValueError:
            raise ValueError('Salary must be numeric')
        
        if val > 0:
            self._annual_salary = val
        else:
            raise ValueError('Salary should be greater than zero')
    
    @property
    def monthly_salary(self) -> float:
        return round (self.annual_salary / 12, 2)
    
# Drill 10: Create Circle class with radius property and computed read-only diameter property (radius * 2)
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        try: 
            val = float(value)
        except ValueError:
            raise ValueError('Radius must be numeric')

        if val > 0:
            self._radius = val
        else:
            raise ValueError('Radius should be greater than zero')

    @property
    def diameter(self) -> float:
        return round(self.radius *2, 2)