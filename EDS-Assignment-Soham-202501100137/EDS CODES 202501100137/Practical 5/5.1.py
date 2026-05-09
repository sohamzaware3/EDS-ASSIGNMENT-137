import numpy as np

print("NUMPY OPERATIONS")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)

print("Subtraction:", arr2 - arr1)

print("Multiplication:", arr1 * arr2)

print("Division:", arr2 / arr1)

print("Scalar Addition:", arr1 + 5)
print("Scalar Multiplication:", arr1 * 2)

print("Shape of Array:", arr1.shape)

print("Dimensions:", arr1.ndim)

print("Data Type:", arr1.dtype)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr3)

reshaped = arr3.reshape(3, 2)
print("Reshaped Array:\n", reshaped)

print("First Element:", arr1[0])

print("Sliced Array:", arr1[1:4])

print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))

print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))

print("Standard Deviation:", np.std(arr1))

print("Square Root:", np.sqrt(arr1))

print("Sorted Array:", np.sort(arr2))

zeros = np.zeros((2, 3))
print("Zeros Array:\n", zeros)

ones = np.ones((2, 2))
print("Ones Array:\n", ones)

identity = np.eye(3)
print("Identity Matrix:\n", identity)

random_arr = np.random.rand(3, 3)
print("Random Array:\n", random_arr)

print("Transpose:\n", arr3.T)

print("Flatten Array:", arr3.flatten())