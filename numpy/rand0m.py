from numpy import random

# x = random.randint(100, size=(3, 5)) # generates a 2d with 3 rows and 5 columns of random integers between 0 and 100
y = random.rand(5)
# z = random.rand(3, 5, 3)
b = random.choice([3, 5, 7, 9])
# print(x)
print(b)
print(y)
# print(z)    

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)