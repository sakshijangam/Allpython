#a menu driven program that checks whether two lists have the same values
while True:
    print("Menu:")
    print("1. Check using Dictionary")
    print("2. Check using Set")
    print("3. check using list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        list1 = input("Enter the first list of 5 elements separated by space: ").split()
        list2 = input("Enter the second list of 5 elements separated by space: ").split()

        if len(list1) != 5 or len(list2) != 5:
            print("Please enter exactly 5 elements in each list.")
            continue

        dict1 = {}
        dict2 = {}

        for num in list1:
            dict1[num] = dict1.get(num, 0) + 1

        for num in list2:
            dict2[num] = dict2.get(num, 0) + 1

        if dict1 == dict2:
            print("Yes")
        else:
            print("No")

    elif choice == '2':
        list1 = set(input("Enter the first list of 5 elements separated by space: ").split())
        list2 = set(input("Enter the second list of 5 elements separated by space: ").split())

        if len(list1) != 5 or len(list2) != 5:
            print("Please enter exactly 5 elements in each list.")
            continue

        if list1 == list2:
            print("Yes")
        else:
            print("No")
    elif choice == '3':
        list1 = list(input("Enter the first list of 5 elements separated by space: ").split())
        list2 = list(input("Enter the second list of 5 elements separated by space: ").split())

        if len(list1) != 5 or len(list2) != 5:
            print("Please enter exactly 5 elements in each list.")
            continue

        if list1 == list2:
            print("Yes")
        else:
            print("No")
    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")
