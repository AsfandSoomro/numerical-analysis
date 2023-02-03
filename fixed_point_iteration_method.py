"""
    This is a Fixed-Point Iterative Method demonstration python program made by AsfandSoomro on 2/16/2022.
"""

from time import sleep
from math import pi

from sympy import diff, symbols, sin, cos, asin, acos  # Third-Party Module

x0 = 2.0  # Initial value of x (Change Here)


# Function of x
def f(x):
    equation = x*x - 2  # Equation (Change Here)
    return equation


# Another Function of x (made from f(x))
def g(x):
    equation = 2/x  # Another Equation (Change Here)
    return equation


# Derivative of function (g(x) at value r)
def g_dash(r):
    x = symbols('x')
    deriv = diff(g(x), x)  # Derivative of g(x)
    return deriv.subs(x, r)  # Returns g'(r), r = any value


x_next = x0  # Variable to store next computed value of x (xn+1)
tmp = 0

if abs(g_dash(x_next)) > 1:
    print("g'(x0) => " + str(abs(g_dash(x_next))) + " > 1 - Error")
    exit(0)

for i in range(100):
    if f(x_next) == 0:
        print("Found the exact root:", x_next)
        break
    if tmp == x_next:  # If it reaches the most accurate value which is not 0 then exit loop
        break

    tmp = x_next  # Temporary storing the value of x

    print("x" + str(i) + " = " + str(x_next) + " - " + "f(x" + str(i) + ") = " + str(f(x_next)))

    x_next = g(x_next)  # Computing new value of x with Fixed-Point Iterative formula

    sleep(0.5)  # As always "good for visualization"
