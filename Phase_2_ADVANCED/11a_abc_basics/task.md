# Task Description

Open `answer.py` in this folder and complete the following objectives:

## Step 1: Create an Abstract Payment Class
Import ABC and abstractmethod, then create an abstract `Payment` class that:
- Inherits from ABC
- Has abstract method `process_payment(self, amount: float) -> bool`
- Has abstract method `get_payment_type(self) -> str`

## Step 2: Create Concrete Implementations
Create two concrete classes that inherit from Payment:
- `CreditCardPayment` - implements both abstract methods
- `PayPalPayment` - implements both abstract methods

## Step 3: Test Instantiation Rules
Try to instantiate the abstract Payment class directly (it should fail).
Then successfully instantiate the concrete classes.

## Step 4: Use Polymorphism
Create a function `process_order(payment: Payment, amount: float)` that:
- Accepts any Payment subclass
- Calls the payment methods polymorphically
- Works with both CreditCard and PayPal payments

---

**Expected Output:**
When you run the code, the terminal should show:
```text
Cannot instantiate abstract class!
Error: Can't instantiate abstract class Payment

Credit Card Payment:
Payment type: Credit Card
Processing $99.99 via Credit Card: Success

PayPal Payment:
Payment type: PayPal
Processing $49.99 via PayPal: Success

Polymorphism test:
Processing order with Credit Card
Payment type: Credit Card
Processing $150.00 via Credit Card: Success

Processing order with PayPal
Payment type: PayPal
Processing $75.00 via PayPal: Success
```
