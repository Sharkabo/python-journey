# Task Description

**Scenario: The Strictly Typed Inventory System**

You are building the core backend for a high-reliability e-commerce platform. The previous system caused millions of dollars in losses because simple type errors (like treating a price strings as numbers) crashed the checkout process. Your CTO has mandated that the new system must use **Type Hints** for everything.

**Your Goal:**
Build a robust `Inventory` system that manages `Product` items. You must use strict type hints for all classes, methods, and list collections to ensure the code is transparent and self-documenting.

**Objectives:**
1.  Create a `Product` class with typed attributes for `name` (str), `price` (float), and `stock` (int).
2.  Add a generic type hint list `items: list[Product]` to the `Inventory` class to ensure it *only* stores Product objects.
3.  Implement a method `add_product(product: Product) -> None` that enforces adding valid Product instances.
4.  Implement `get_total_value() -> float` to calculate the total value of all stock.
5.  Create a strict protocol or base structure if needed, but primarily focus on ensuring that if another developer tries to add a `string` or `int` to your inventory, a static type checker would scream at them (and it should be visually obvious in the code).

**Success Condition:**
Your code should gracefully handle creating products, adding them to an inventory, and calculating the total value, with every single variable and function signature explicitly typed.
