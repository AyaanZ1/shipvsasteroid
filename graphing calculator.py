import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
def quadratic(x,a,b,c):
    return a*x**2 + b*x + c
def linear(x,a,b):
    return a*x + b
def exponential(x,a,b):
    return a*(b**x)
def absolute(x,a,b):
    return a*np.abs(x) + b

type = input("Type of function: ")
if type == "quadratic":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = np.linspace(-10,10,100)
    y = quadratic(x,a,b,c)
    plt.plot(x,y)
    plt.grid()
    plt.show()
elif type == "linear":
    a = float(input("a: "))
    b = float(input("b: "))
    x = np.linspace(-10,10,100)
    y = linear(x,a,b)
    plt.plot(x,y)
    plt.grid()
    plt.show()
elif type == "exponential":
    a = float(input("a: "))
    b = float(input("b: "))
    x = np.linspace(-10,10,100)
    y = exponential(x,a,b)
    plt.plot(x,y)
    plt.grid()
    plt.show()
elif type == "absolute":
    a = float(input("a: "))
    b = float(input("b: "))
    x = np.linspace(-10,10,100)
    y = absolute(x,a,b)
    plt.plot(x,y)
    plt.grid()
    plt.show()

