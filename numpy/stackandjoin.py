# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))

# print(arr)


# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr3 = np.concatenate((arr1, arr2), axis=1)

# print(arr3)


# # using stack to combine arrays along a new axis
# #stack is used to combine arrays along a new axis, while concatenate is used to combine arrays along an existing axis.
# arr4 = np.array([1, 2, 3, 4])

# arr5 = np.array([4, 5, 6, 7])

# arr = np.stack((arr4, arr5), axis=1)

# print(arr)



# #hstack is used to combine arrays horizontally (column-wise), while vstack is used to combine arrays vertically (row-wise).
# arr6 = np.array([1, 2, 3])  

# arr7 = np.array([4, 5, 6])

# arr8 = np.array([7, 8, 9])

# arr = np.hstack((arr6, arr7, arr8))

# arrv = np.vstack((arr6, arr7, arr8))

# print(arr)
# print(arrv)



#stacking arrays along a new axis using dstack (depth-wise stacking-height)