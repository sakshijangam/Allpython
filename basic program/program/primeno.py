# Take user input for the number to check
num = int(input("Enter a number: "))

# Check if the number is prime
if num > 1:
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
