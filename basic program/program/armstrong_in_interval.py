# Take user input for the interval
lower = int(input("Enter lower bound of the interval: "))
upper = int(input("Enter upper bound of the interval: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

# Iterate through each number in the interval
for num in range(lower, upper + 1):
    # Count the number of digits in the number
    num_digits = len(str(num))
    # Initialize sum
    sum = 0
    temp = num

    # Calculate sum of nth power of each digit
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10

    # Check if the number is Armstrong or not
    if num == sum:
        print(num)
