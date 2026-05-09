import numpy as np

data = np.array([
    [85, 78, 92],
    [88, 76, 95],
    [90, 89, 91]
])

print("Original Dataset:\n", data)

print("\nMATRIX OPERATIONS")

print("\nAddition:")
print(data + 5)

print("\nSubtraction:")
print(data - 2)

print("\nMultiplication:")
print(data * 2)

print("\nTranspose:")
print(data.T)

print("\nMatrix Multiplication:")
print(np.dot(data, data.T))

print("\nSTACKING OPERATIONS")

extra_data = np.array([
    [80, 81, 82],
    [83, 84, 85],
    [86, 87, 88]
])

h_stack = np.hstack((data, extra_data))
print("\nHorizontal Stack:\n", h_stack)

v_stack = np.vstack((data, extra_data))
print("\nVertical Stack:\n", v_stack)

print("\nCUSTOM SEQUENCE")

seq = np.arange(1, 21, 2)
print("Arithmetic Sequence:", seq)

line_seq = np.linspace(0, 10, 5)
print("Linspace Sequence:", line_seq)

print("\nARITHMETIC OPERATIONS")

print("Addition:\n", data + 10)
print("Subtraction:\n", data - 5)
print("Multiplication:\n", data * 2)
print("Division:\n", data / 2)

print("\nSTATISTICAL OPERATIONS")

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))

print("\nMATHEMATICAL OPERATIONS")

print("Square Root:\n", np.sqrt(data))
print("Square:\n", np.square(data))
print("Log Values:\n", np.log(data))

print("\nBITWISE OPERATIONS")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Bitwise AND:", np.bitwise_and(a, b))
print("Bitwise OR:", np.bitwise_or(a, b))
print("Bitwise XOR:", np.bitwise_xor(a, b))

print("\nCOPY AND VIEW")

copy_array = data.copy()
view_array = data.view()

print("Copied Array:\n", copy_array)
print("Viewed Array:\n", view_array)

print("\nSEARCHING")

print("Position of 95:")
print(np.where(data == 95))

print("\nSORTING")

print("Sorted Data:\n", np.sort(data))

print("\nCOUNTING")

print("Count of elements > 85:")
print(np.count_nonzero(data > 85))

print("\nBROADCASTING")

broadcast_array = np.array([1, 2, 3])

print(data + broadcast_array)