# Complete your task here (goals list refer to task.md)

# Goal 1: Create a Product Class with Read-Only ID
class Product:
    def __init__(self, id, name, price) -> None:
        self._id = id
        self.name = name
        self.price = price
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value.capitalize()

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
            raise ValueError('Price has to be greater than zero')
    
    @property
    def info(self) -> str:
        return f'– Product ID: {self._id}\n– Product Name: {self.name}\n– Product Price: {self.price}'

# Goal 2: Add Child Class with Property Override
class DiscountedProduct(Product):
    
    @Product.price.getter
    def price(self) -> float:
        return self._price * 0.8
    
    @price.setter
    def price(self, value: float) -> None:
        assert Product.price.fset is not None
        Product.price.fset(self, value)