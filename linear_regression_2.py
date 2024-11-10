import numpy as np
import math
import matplotlib.pyplot as plt

x = np.array([0, 4, 10, 15, 21, 29, 36, 51])
y = np.array([5, 41, 106, 145, 205, 285, 350, 3510])

def done(x, y):
    def exp_log(y):
        new_y = []
        for i in y:
            new_y.append(math.log(i))
        return new_y

    new_y = exp_log(y)

    def linear_regression(x, new_y):
        n = len(x)
        b = (n * sum(x * new_y) - sum(x) * sum(new_y)) / (n * sum(x**2) - sum(x)**2)
        ln_a = (sum(new_y) - b * sum(x)) / n
        return ln_a, b

    ln_a, b = linear_regression(x, new_y)
    
    a = math.exp(ln_a)
    return a, b

a, b = done(x, y)
print("a =", a)
print("b =", b)

y_values = []
for i in x:
    exp_eq = a * math.exp(b * i)
    y_values.append(exp_eq)

plt.plot(x, y_values, label='Експоненціальна модель', color='skyblue')
plt.scatter(x, y, color='blue', label='Дані', marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Експоненціальна регресія')
plt.legend()
plt.grid(True)
plt.show()