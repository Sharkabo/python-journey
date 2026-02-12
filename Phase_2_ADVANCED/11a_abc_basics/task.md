# Task Description

**Scenario: The Universal Payment Gateway**

You are building an e-commerce platform that supports multiple payment providers (Stripe, PayPal, Crypto). You need to ensure that every new payment method added in the future follows the *exact same structure* so the checkout code doesn't break. You can't trust developers to "just remember" to add a `process_payment` method. You need to enforce it.

**Your Goal:**
Create an Abstract Base Class (ABC) `PaymentGateway` that acts as a strict contract for all payment processors.

**Objectives:**
1.  Define an abstract class `PaymentGateway` inheriting from `ABC`.
2.  Define abstract methods:
    - `connect(api_key: str)`: Connects to the service.
    - `process_payment(amount: float) -> bool`: Processes a charge.
3.  Implement a concrete class `PayPalGateway` that inherits from your ABC.
    - Implement the methods with simple print statements simulating the actions.
4.  Implement a concrete class `StripeGateway` that inherits from your ABC.
5.  **The Test:** Try to instantiate a class `IncompleteGateway` that inherits from `PaymentGateway` but *forgets* to implement `process_payment`.

**Success Condition:**
1.  `PayPalGateway` and `StripeGateway` should work perfectly.
2.  Trying to create an instance of `IncompleteGateway` MUST raise a `TypeError` immediately (Python prevents it from existing). This proves your contract is working.
