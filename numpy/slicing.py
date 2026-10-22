import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #print elements from index 1 but does not include element at index 5

print(arr[4:]) #print elements from index 4 to the end of the array

print(arr[:4]) #print elements from the beginning of the array to index 4 but does not include element at index 4


#NEGATIVE SLICING
# Negative slicing means beginning from the end, -1 refers to the last item, -2
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

#STEP
# You can define the step of the slicing, which allows you to skip elements in the array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:5:2])
print(arr[::2]) #print every other element from the array
print(arr[1::2]) #print every other element from the array starting from index 1
print(arr[::])  # print the whole array
print(arr[::-1]) #print the array in reverse order

# slicing 2-d and 3-d arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 2])