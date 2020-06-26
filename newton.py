import math
import matplotlib.pyplot as plt
import numpy
import sys

def newton():
    """
    Define your function
    """
    f = lambda x: x**3 - x**2 - 1
    """
    Define the derivative of your function
    """
    df = lambda x: 3*x**2 - 2*x
    x = float(input("Give the initial guess of the solution: "))
    flag = False
    step = 0
    many_steps = False
    while abs(f(x)) > sys.float_info.epsilon and not flag and not many_steps:
        if df(x) == 0:
            flag = True
        elif step>10**6:
            many_steps = True
        else:
            x = x -(f(x)/df(x))
        step+=1
    if flag:return "Houston, we have a problem! Zero derivate! No solution found!"
    elif many_steps:return "That took a long time, didn't it? Anyways, your approximation is: "+str(x)
    else:return str(x)
            

print(newton())
    
