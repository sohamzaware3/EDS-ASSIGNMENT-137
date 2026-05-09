marks = list(map(float, input("Enter subject marks separated by space: ").split()))

total = sum(marks)

percentage = total / len(marks)

print("Total Marks =", total)
print("Percentage =", percentage, "%")