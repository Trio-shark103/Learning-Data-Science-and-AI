import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr1.dtype)


arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2)
print(arr2.dtype)


arr3 = np.array([1, 2, 3, 4], dtype='i4')

print(arr3)
print(arr3.dtype)


arr3 = np.array([1.1, 2.1, 3.1])

newarr = arr3.astype('i')

print(newarr)
print(newarr.dtype)


arr4 = np.array([1.1, 2.1, 3.1])

newarr1= arr4.astype(int)

print(newarr1)
print(newarr1.dtype)


import numpy as np

arr7 = np.array([1, 0, 3])

newarr3 = arr7.astype(bool)

print(newarr3)
print(newarr3.dtype)