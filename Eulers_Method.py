import math
import matplotlib.pyplot as plt
import numpy

def euler():
    """
    Define your function here
    """
    f = lambda t,y: (y*math.log(y))/t
    a = float(input("Give a: "))
    b = float(input("Give b: "))
    N = int(input("Give N: "))
    h = (b-a)/N
    t = numpy.linspace(a,b,N)
    y0 = float(input("Give y_0: "))
    y = [y0]
    for i in range(len(t)-1):
        y.append(y[i]+h*f(t[i],y[i]))
    plt.plot(t,y)
    plt.show()

euler()
