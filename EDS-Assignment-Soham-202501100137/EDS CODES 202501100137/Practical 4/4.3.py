print("TUPLE OPERATIONS")

numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)

print("Length:", len(numbers))

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

print("Sliced Tuple:", numbers[1:4])

print("Count of 20:", numbers.count(20))

print("Index of 30:", numbers.index(30))

new_tuple = numbers + (60, 70)
print("After Concatenation:", new_tuple)

repeat_tuple = numbers * 2
print("After Repetition:", repeat_tuple)

print("Is 40 present?", 40 in numbers)

print("Tuple Elements:")
for item in numbers:
    print(item)

nested_tuple = ((1, 2), (3, 4))
print("Nested Tuple:", nested_tuple)

num_list = list(numbers)
print("Tuple converted to List:", num_list)

new_numbers = tuple(num_list)
print("List converted back to Tuple:", new_numbers)