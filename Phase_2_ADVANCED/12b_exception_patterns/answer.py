# Complete your task here (goals are defined in task.md)

# Step 1: Create Exception with Context Data


# Step 2: Use Exception Context in Application


# Step 3: Handle Exception and Use Context Data


# Step 4: Chain Exceptions


# Test your code
if __name__ == "__main__":
    # Test successful withdrawal
    account = BankAccount(balance=100.00, account_id="12345")
    try:
        account.withdraw(50.00)
        print(f"Account {account.account_id}: Withdrawal successful! Balance: ${account.balance:.2f}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    print()
    
    # Test insufficient funds
    print("Withdrawal failed!")
    try:
        account.withdraw(75.00)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        print(f"Balance: ${e.balance:.2f}")
        print(f"Requested: ${e.requested_amount:.2f}")
        shortfall = e.requested_amount - e.balance
        print(f"Shortfall: ${shortfall:.2f}")
    print()
    
    # Test exception chaining
    print("Exception Chaining:")
    try:
        try:
            # Low-level error
            value = int("-5")
            if value < 0:
                raise ValueError("negative numbers not allowed")
        except ValueError as e:
            # Chain with high-level error
            raise RuntimeError("Invalid transaction") from e
    except RuntimeError as e:
        print(f"Caught application error: {e}")
        if e.__cause__:
            print(f"Original cause: {e.__cause__}")
