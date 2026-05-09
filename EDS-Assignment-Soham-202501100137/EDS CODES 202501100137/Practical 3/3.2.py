num = list(map(int,input("Enter list elements seperated by space: ").split()))
key = int(input("Enter number of search: "))
position=-1
for i in range(len(num)):
    if (num[i]==key):
        position=i
        break

if position != -1:
    print("Element found at position:",position)
else:
    print("Element not found")