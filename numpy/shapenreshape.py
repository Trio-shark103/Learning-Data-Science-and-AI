import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)

# Ans (2,4). where the 2 represents the number of rows and 4 represents the number of columns in the array.
# the shape attribute returns a tuple representing the dimensions of the array. In this case, the array has 2 elements for the first dimension and 4 elements for the second dimension, so the shape is (2, 4).`


# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)



# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)

# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(2, 3, 2)

# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


#flattening an array that is converting a multidimensional Array into a 1 Dimension array
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)

# print(newarr)