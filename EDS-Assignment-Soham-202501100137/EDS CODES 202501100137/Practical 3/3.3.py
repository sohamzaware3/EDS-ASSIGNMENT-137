numbers = [10, 20, 30, 40]

print("Original List:", numbers)

numbers.append(50)
print("After Append:", numbers)

numbers.insert(2, 25)
print("After Insert:", numbers)

numbers.remove(30)
print("After Remove:", numbers)

numbers.pop()
print("After Pop:", numbers)

numbers.sort()
print("After Sort:", numbers)

numbers.reverse()
print("After Reverse:", numbers)

print("Length of List:", len(numbers))

print("Index of 20:", numbers.index(20))

print("Sliced List:", numbers[1:3])


# Creating dictionary
student = {
    "name": "Shashank",
    "age": 20,
    "course": "Python"
}

print("Original Dictionary:", student)

student["marks"] = 85
print("After Adding:", student)

student["age"] = 21
print("After Updating:", student)

student.pop("course")
print("After Removing:", student)

print("Student Name:", student["name"])

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Length:", len(student))