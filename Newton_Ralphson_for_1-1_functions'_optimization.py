import math
import numpy as np
import matplotlib.pyplot as plt

#define function f
def f(x):
    return x**4 - 10 * x**3 + 1

#define first derivative of f
def f_1(x):
    return 4 * x**3 - 30 * x**2

#define second derivative of f
def f_2(x):
     return 12 * x**2 - 60 * x

def NR_1D(x_0, tolerance):
    counter = 0
    while abs(f_1(x_0)) > tolerance:
        x_0 += -1 * (f_1(x_0)/f_2(x_0))
    return x_0

t = np.linspace(-1000, 1000, 1000000)
f_val = f(t)

f_min = NR_1D(1, .01)
plt.plot(t, f_val, f_min, f(f_min), 'o', 'r')
plt.show()
