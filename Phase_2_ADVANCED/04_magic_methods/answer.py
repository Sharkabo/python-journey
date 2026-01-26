# Complete your task here (goals list refer to task.md)

# Goal 1: Create a Product Class
class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        if isinstance(price, (int, float)) and isinstance(quantity, int):
            self.price = price
            self.quantity = quantity
        else:
            raise ValueError('Price and quantity must be numeric')

# Goal 2: Implement String Representations
    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"
    
    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

# Goal 3: Implement Comparison Methods
    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price
    
# Goal 4: Implement Arithmetic
    def __add__(self, other) -> Product:
        if not isinstance(other, Product):
            return NotImplemented
        if self.name == other.name:
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError('They are two different kinds of product, so can\'t add up')

# Goal 5: Test Your Implementation

