# Take user input for the number
num = int(input("Enter a number: "))

# Calculate the number of digits in the number
num_digits = len(str(num))

# Initialize a variable to store the sum of the nth powers of digits
sum_armstrong = 0
temp = num

# Check if the number is an Armstrong number
while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** num_digits
    temp //= 10

if num == sum_armstrong:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
