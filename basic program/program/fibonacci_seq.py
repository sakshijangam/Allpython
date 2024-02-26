# Take user input for the number of terms
terms = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci sequence
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence up to", terms, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(a, end=" ")
        nth_term = a + b
        # Update values for the next iteration
        a = b
        b = nth_term
        count += 1
