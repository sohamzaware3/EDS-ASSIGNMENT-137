marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for course {i}: "))
    marks.append(mark)

if all(mark >= 40 for mark in marks):

    total = sum(marks)
    percentage = total / 5

    print("Student Passed")
    print("Percentage =", percentage)

    if percentage > 75:
        print("Grade: Distinction")

    elif percentage >= 60 and percentage < 75:
        print("Grade: First Division")

    elif percentage >= 50 and percentage < 60:
        print("Grade: Second Division")

    elif percentage >= 40 and percentage < 50:
        print("Grade: Third Division")

else:
    print("Student Failed")