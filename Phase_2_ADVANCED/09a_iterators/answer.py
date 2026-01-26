# Complete your task here (goals are defined in task.md)

# Step 1: Create a Countdown Iterator


# Step 2: Test Your Iterator with for Loop


# Step 3: Test Your Iterator with next()


# Step 4: Handle StopIteration


# Test your code
if __name__ == "__main__":
    # Test Step 2: for loop
    print("Countdown from 5:")
    for num in Countdown(5):
        print(num)
    print()
    
    # Test Step 3 & 4: manual next() with StopIteration handling
    print("Manual countdown from 3:")
    countdown = Countdown(3)
    try:
        print(next(countdown))
        print(next(countdown))
        print(next(countdown))
        print(next(countdown))  # This will raise StopIteration
    except StopIteration:
        print("Countdown finished! (StopIteration caught)")
