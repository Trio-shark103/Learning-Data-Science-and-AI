# import numpy 


# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)
# object ndarray is array()function of numpy module. It is used to create an array.
import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))  # Output: <class 'numpy.ndarray'>

# to create an ndarray we can pass a tuple, list or array to the array() function. 
# The array() function takes a sequence-like object as input and returns an ndarray object.

arb = np.array((1, 2, 3, 4, 5))
print(arb)