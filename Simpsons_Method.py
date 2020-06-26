import math
import matplotlib.pyplot as plt
import numpy

def Simpson():
    summ = 0
    f = lambda x: math.log(x)
    a = float(input("Give a: "))
    b = float(input("Give b: "))
    N = int(input("Give N: "))
    t = numpy.linspace(a,b,N)
    for i in range(len(t)-1):
        h = (t[i+1] - t[i])/2
        x0 = t[i]
        x1 = t[i] + h
        x2 = t[i] + 2*h
        summ+= (h/3)*(f(x0)+4*f(x1)+f(x2))
    """
    In case you want to see what you calculate, deactivate the comments here:
    y = [f(t[i]) for i in range(len(t)) ]
    plt.plot(t,y)
    plt.tight_layout()
    plt.fill_between(t,y)
    plt.show()
    """
    return summ
print(Simpson())
