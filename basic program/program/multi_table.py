# Take user input for the number
num = int(input("Enter a number: "))

# Display the multiplication table
print("Multiplication table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
