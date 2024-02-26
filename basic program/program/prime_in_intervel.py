# Take user input for the interval
lower = int(input("Enter lower bound of the interval: "))
upper = int(input("Enter upper bound of the interval: "))

print("Prime numbers between", lower, "and", upper, "are:")

# Iterate through each number in the interval
for num in range(lower, upper + 1):
    # Prime numbers are greater than 1
    if num > 1:
        # Check for factors
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
