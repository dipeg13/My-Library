import math
import numpy
import matplotlib.pyplot as plt

def weights_calculation(a,b,n):
    A = numpy.zeros((n+1,n+1))
    index = numpy.zeros(n+1)
    h = (b-a)/n
    for i in range(n+1):
        index[i] = a + i * h
    for i in range(n+1):
        for j in range(n+1):
            A[i][j] = index[j]**i
    B = numpy.zeros(n+1)
    for i in range(n+1):
        B[i] = (b**(i+1) - a**(i+1))/(i+1)
    return numpy.linalg.solve(A, B)

def main():
    integral = 0
    """Define your funcrion"""
    f = lambda x: x
    a = float(input("Give a: "))
    b = float(input("Give b: "))
    n = int(input("Give the degree of the method: "))
    N = int(input("Give N: "))
    t = numpy.linspace(a,b,N)
    for i in range(N-1):
        summ = 0
        weights = weights_calculation(t[i],t[i+1],n)
        h = (t[i+1] - t[i])/n
        for j in range(len(weights)):
            summ+= weights[j] *f(t[i] + j* h)
        integral += summ

    """
    In case you want to see what you calculate, deactivate the comments here:
    y = [f(t[i]) for i in range(len(t)) ]
    plt.plot(t,y)
    plt.tight_layout()
    plt.fill_between(t,y)
    plt.show()
    """
    return integral

print(main())
                    
        
    
