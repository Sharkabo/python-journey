# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create a Typed Product Class
Create a `Product` class with type hints:
- `__init__(self, name: str, price: float, stock: int)` 
- Properties: name, price, stock with proper type hints
- Method: `is_in_stock(self) -> bool` returns True if stock > 0

## Step 2: Create a Typed Inventory Class
Create an `Inventory` class that:
- Has `__init__(self)` initializing `items: list[Product]`
- Has `add_product(self, product: Product) -> None` to add a product
- Has `get_total_value(self) -> float` that returns total value (sum of price * stock)
- All methods have proper type hints

## Step 3: Create a Typed Method with Inheritance
Create a `DiscountedProduct(Product)` class that:
- Inherits from Product
- Adds `discount: float` parameter to `__init__`
- Overrides a method `get_final_price(self) -> float` with type hints
- Returns price after discount (price * (1 - discount))

## Step 4: Test Your Classes
Create instances and test:
- Create 2-3 Product instances
- Add them to Inventory
- Create a DiscountedProduct
- Print results with type-safe operations

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Product: Laptop
In stock: True
Price: $999.99

Product: Mouse
In stock: False

Total inventory value: $1049.98

Discounted Product: Keyboard
Original price: $79.99
Final price: $63.99
```
