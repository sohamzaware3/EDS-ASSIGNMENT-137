numbers = list(map(int, input("Enter list elements separated by space: ").split()))

search = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Number found at position:", i + 1)
        found = True
        break

if not found:
    print("Number not found in the list")