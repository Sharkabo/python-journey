# Complete your task here (goals are defined in task.md)
from abc import ABC, abstractmethod

# Step 1: Create an Abstract Payment Class


# Step 2: Create Concrete Implementations


# Step 3: Test Instantiation Rules


# Step 4: Use Polymorphism


# Test your code
if __name__ == "__main__":
    # Test Step 3: Try to instantiate abstract class
    print("Cannot instantiate abstract class!")
    try:
        payment = Payment()
    except TypeError as e:
        print(f"Error: {e}")
    print()
    
    # Test concrete implementations
    print("Credit Card Payment:")
    cc = CreditCardPayment()
    print(f"Payment type: {cc.get_payment_type()}")
    success = cc.process_payment(99.99)
    print(f"Processing $99.99 via Credit Card: {'Success' if success else 'Failed'}")
    print()
    
    print("PayPal Payment:")
    pp = PayPalPayment()
    print(f"Payment type: {pp.get_payment_type()}")
    success = pp.process_payment(49.99)
    print(f"Processing $49.99 via PayPal: {'Success' if success else 'Failed'}")
    print()
    
    # Test Step 4: Polymorphism
    print("Polymorphism test:")
    print("Processing order with Credit Card")
    process_order(CreditCardPayment(), 150.00)
    print()
    
    print("Processing order with PayPal")
    process_order(PayPalPayment(), 75.00)
