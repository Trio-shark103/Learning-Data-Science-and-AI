import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)


arr1 = np.array([1, 2, 3, 4, 5])

x = arr1.copy()
y = arr1.view()

print(x.base)
print(y.base)