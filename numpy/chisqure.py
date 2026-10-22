# Chi Square Distribution
# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).

# size - The shape of the returned array.

from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.chisquare(df=1, size=1000), kind="kde")

# plt.show()


# Rayleigh Distribution
# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2, 3))

print(x)
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()

#Similarity Between Rayleigh and Chi Square Distribution
#At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions.