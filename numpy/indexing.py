import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2] + arr[3])


# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print('1st element on 1st row: ', arr[0, 0])
print('1st element on 2nd row: ', arr[1, 0])
print('5th element on 2nd row: ', arr[1, 4])


# to access elements from 3-D arrays we can use comma separated integers representing the dimension and the index of the element.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

# The 0 represents the 1st array,
# Ans : [[1, 2, 3], [4, 5, 6]]
# The 1 represents the 2nd array of that 1st array,
#  Ans : [4, 5, 6]
# The 2 represents the 3rd element of that 2nd array.
# Ans : 6



# NEGATIVE INDEXING
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element on 1st row: ', arr[0, -1]) #Ans : 5
print('Second last element on 1st row: ', arr[0, -2]) #Ans : 4
print('Last element on 2nd row: ', arr[1, -1]) #Ans : 10