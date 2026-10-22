# shuffle and permutation
# Shuffle changes the order of elements in an original array in place, while permutation returns a new array with the elements permuted.
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(random.permutation(arr))  # Output: [3 5 1 4 2] (example output, actual output may vary)
print(arr)