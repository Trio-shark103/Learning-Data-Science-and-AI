import numpy as np 
# a dimension in arrays is one level of array depth(nested arrays)

# 0-dimension arrays /scalar arrays
arr = np.array(42)
print (arr)

# 1- Dimension arrays
ard = np.array([1, 2, 3, 4, 5])
print(ard)

# 2-Dimension arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# 3-Dimension arrays
# contains 2 arrays, each array has 2 arrays, and each of those arrays has 3 values
# use to represent a 3D matrix or a cube of data and 3rd order tensor. It is used in deep learning and computer vision applications.

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)


# how to check the dimensions of an array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# create an array with 5 dimensions and verify it
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)