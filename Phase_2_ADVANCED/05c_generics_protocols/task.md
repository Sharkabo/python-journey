# Task Description

**Scenario: The Universal Package Handler**

You are designing a logistics system for a shipping company. They ship *everything*—books, electronics, fragile glass. You need a system that can handle any type of item (`Generic`) but also ensures that every item has a specific capability, like reporting its weight (`Protocol`).

**Your Goal:**
Build a **Generic** container class that can hold any item type, but enforce that items must follow a specific **Protocol**.

**Objectives:**
1.  **Define a Protocol:** Create a `Weighable` protocol. It must require a method `get_weight(self) -> float`.
2.  **Define Items:** Create two classes, `Book` and `Laptop`, that implement `Weighable`.
    - `Book` weight might be 0.5.
    - `Laptop` weight might be 2.0.
3.  **Create a Generic Class:** Create a class `ShippingContainer[T]` where `T` is a TypeVar.
    - It should hold a list of items of type `T`.
    - It should have a method `add_item(item: T)`.
    - It should have a method `total_weight() -> float` that sums up the weights of all items.
4.  **The Twist:** The `ShippingContainer` should be type-hinted so that `T` is *bound* to `Weighable` (syntax: `T = TypeVar("T", bound=Weighable)`). This ensures you can't put a non-weighable object in it!

**Success Condition:**
1.  Create a `ShippingContainer` for Books. Add a Book. Print total weight.
2.  Create a `ShippingContainer` for Laptops. Add a Laptop. Print total weight.
3.  (Mental Check): If you tried to add a string "Hello" to the container, your IDE (static type checker) should theoretically flag it as an error because "Hello" doesn't have `get_weight()`.
