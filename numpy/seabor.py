import matplotlib.pyplot as plt
import seaborn as sns



#plotting a displot histogram
# sns.displot([0, 1, 2, 3, 4, 5])


# plotting a displot kde(curve)
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
 

# plt.show()

#Normal distribution plot / Gaussian distribution plot

# Use the random.normal() method to get a Normal Data Distribution.

# It has three parameters:

# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

from numpy import random
w = random.normal(size=(1000),)
# w = random.normal(size=(1, 3))
# z = random.normal(size=(2, 3))
# y = random.normal(size=(1,3,5))
# x = random.normal(size=(2, 3,5))

# print('this is for w')
# print(w)
# print('this is for z')
# print(z)
# print('this is for y')
# print(y)
# print('this is for x')
# print(x)

# x = random.normal(loc=1, scale=2, size=(2, 3))

# print(w)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()