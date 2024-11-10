import numpy as np
import math
import matplotlib.pyplot as plt

x = np.array([0, 4, 10, 15, 21, 29, 36, 51])
y = np.array([5, 41, 106, 145, 205, 285, 350, 3510])

def done(x, y):
    n = len(x)
    a = (n * sum(x*y) - sum(x)*sum(y)) / (n * sum(x**2) - sum(x)**2) 
    b = (sum(y)*sum(x**2)-sum(x)*sum(x*y)) / (n*sum(x**2)-sum(x)**2)

    return a, b
(a, b) = done(x, y)
eq = a*x+b

plt.plot(x, eq, label="linear regression for y = a*x+b", marker="o")
plt.grid(True)
plt.legend()
plt.show()