try:
    N = int(input("Enter the height/steps of Pascal's triangle: "))

    for i in range(N):
        # Print spaces to align triangle to the right
        for _ in range(N - i - 1):
            print(" ", end=" ")

        # Calculate and print elements in current row
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)

        print()  # Move to the next line for the next row

except ValueError:
    print("Invalid input. Please enter an integer.")
