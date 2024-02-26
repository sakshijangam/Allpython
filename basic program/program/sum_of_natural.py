# Take user input for the number
num = int(input("Enter a positive integer: "))

# Check if the number is positive
if num < 0:
    print("Please enter a positive integer")
else:
    # Initialize sum
    sum = 0
    # Calculate sum of natural numbers
    for i in range(1, num + 1):
        sum += i
    print("The sum of natural numbers up to", num, "is", sum)
