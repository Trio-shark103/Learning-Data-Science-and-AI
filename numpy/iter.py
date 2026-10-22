import numpy as np

arr = np.array([1, 2, 3])

arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr1):
  print(x)
 
# Using nditer with the 'buffered' flag and specifying the output data type as string ('S')
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  

for x in np.nditer(arr1[:, ::2]):
  print(x)
