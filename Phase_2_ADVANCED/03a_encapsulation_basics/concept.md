# Unit 03a: Encapsulation Basics

## 1. What is Encapsulation?
Encapsulation is bundling data and methods together while controlling access to that data. It's about hiding internal details and only exposing what's necessary.

**Syntax:**
```python
class ClassName:
    def __init__(self):
        self.public_attr = "accessible"      # Public
        self._protected_attr = "internal"    # Protected (convention)
        self.__private_attr = "hidden"       # Private (name mangled)
```

**Example:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self.__balance = balance        # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(account.owner)          # Alice (public, OK)
print(account.get_balance())  # 1000 (access through method)
# print(account.__balance)    # AttributeError (private)
```

---

## 2. Name Mangling (Optional)
When you use double underscores `__`, Python applies name mangling to make attributes harder to access from outside.

**Syntax:**
```python
# Python internally renames __private to _ClassName__private
obj._ClassName__private  # Can still access (not recommended!)
```

**Example:**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    
    def get_price(self):
        return self.__price

laptop = Product("Gaming Laptop", 1000)
print(laptop.get_price())  # 1000 (controlled access)
```

---

## Spiral Learning Note
Unit 01 taught you to create classes. Unit 02 taught inheritance. Now you control access to attributes. Next you'll learn the `@property` decorator for elegant encapsulation.
