# Pareto Distribution
# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# It has two parameter:

# a - shape parameter.

# size - The shape of the returned array.

from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()
