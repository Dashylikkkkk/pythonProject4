import math
import random

sum = 0
t = 1000000
for i in range(t):
    x = random.random()
    y = random.random()
    sum += math.sqrt(x ** 2 + y ** 2)
pi = sum * 4 / t
print(pi)

