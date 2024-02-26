try:
    # Input student details
    while True:
        name = input("Enter student name: ")
        if name.isalpha():# name contain only an alphabates no numbers
            break
        else:
            print("Invalid name. Please enter a valid name.")

    while True:
        roll_number = input("Enter roll number: ")
        if roll_number.isdigit():
            roll_number = int(roll_number)
            break
        else:
            print("Invalid roll number. Please enter a valid roll number.")

    # Input scores for 5 subjects
    subjects = ['English', 'Hindi', 'Maths', 'Science', 'Social Science']
    scores = []
    for subject in subjects:
        while True:
            score = input(f"Enter score for {subject}: ")
            if score.isdigit() and 1 <= int(score) <= 100:
                scores.append(int(score))
                break
            else:
                print("Invalid score. Please enter a score between 1 and 100.")

    # Calculate percentage
    total_marks = sum(scores)
    percentage = round((total_marks / (len(subjects) * 100)) * 100, 2)

    # Determine result
    result = "Pass" if percentage >= 36 else "Fail"

    # Display student details, scores, percentage, and result
    print("\n------------------------------")
    print(f"Roll no.: {roll_number}")
    print(f"Name: {name}")
    print("------------------------------")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {scores[i]}")
    print("------------------------------")
    print(f"Percentage: {percentage}%")
    print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter valid values.")
