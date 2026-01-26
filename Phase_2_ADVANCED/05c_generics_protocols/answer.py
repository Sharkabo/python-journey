# Complete your task here (goals are defined in task.md)

# Step 1: Create a Typed Product Class


# Step 2: Create a Typed Inventory Class


# Step 3: Create a Typed Method with Inheritance


# Step 4: Test Your Classes
if __name__ == "__main__":
    # Create products
    laptop = Product("Laptop", 999.99, 5)
    mouse = Product("Mouse", 49.99, 0)
    
    print(f"Product: {laptop.name}")
    print(f"In stock: {laptop.is_in_stock()}")
    print(f"Price: ${laptop.price}")
    print()
    
    print(f"Product: {mouse.name}")
    print(f"In stock: {mouse.is_in_stock()}")
    print()
    
    # Create inventory
    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(mouse)
    
    total = inventory.get_total_value()
    print(f"Total inventory value: ${total:.2f}")
    print()
    
    # Create discounted product
    keyboard = DiscountedProduct("Keyboard", 79.99, 10, 0.20)
    print(f"Discounted Product: {keyboard.name}")
    print(f"Original price: ${keyboard.price}")
    print(f"Final price: ${keyboard.get_final_price():.2f}")
