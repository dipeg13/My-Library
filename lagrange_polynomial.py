import math
import matplotlib.pyplot as plt
import numpy

def lagrange_basis(l,j,x):
    pi = 1
    for i in range(len(l)):
        if i!=j:
            pi*= (x-l[i])/(l[j]-l[i])
    return pi

def lagrange_polynomial(l,x):
    sum = 0
    lx = []
    for i in range(len(l)): lx.append(l[i][0])
    for j in range(len(l)):
        sum+=l[j][1] * lagrange_basis(lx,j,x)
    return sum

"""
l = [ [x_0,y_0] , ... , [x_k,y_k] ]
"""

def define_list():
    l = []
    n = int(input("Define the numebers of points: "))
    for i in range(n):
        x = float(input("Give x: "))
        y = float(input("Give y: "))
        l.append([x,y])
    return l

def main():
    a = float(input("Give a: "))
    b = float(input("Give b: "))
    N = int(input("Give N: "))
    x = numpy.linspace(a,b,N)
    l = define_list()
    y = []
    for i in range(N):
        y.append(lagrange_polynomial(l,x[i]))
    plt.plot(x,y)
    plt.show()

main()
