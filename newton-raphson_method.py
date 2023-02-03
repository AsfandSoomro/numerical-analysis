"""
    This is a Newtom-Raphson Method demonstration python program made by AsfandSoomro on 2/10/2022.
"""

from time import sleep
from math import pi

from sympy import diff, symbols, sin, cos  # Third-Party Module

x0 = 1.0  # Initial value of x (Change Here)


# Function of x
def f(x):
    equation = sin(x * pi/180) - x  # Equation (Change Here)
    return equation


# Derivative of function (f(x) at value r)
def f_dash(r):
    x = symbols('x')
    deriv = diff(f(x), x)  # Derivative of f(x)
    return deriv.subs(x, r)  # Returns f'(r), r = any value


x_next = x0  # Variable to store next computed value of x (xn+1)
tmp = 0

for i in range(100):
    if f(x_next) == 0:
        print("Found the exact root:", x_next)
        break
    if tmp == x_next:  # If it reaches the most accurate value which is not 0 then exit loop
        break
    if f_dash(x_next) == 0:  # When derivative of x_next (f'(x_next) == 0), terminate program as it can't be solved further
        print("f'(x" + str(i) + ") = 0 - Error")
        break

    tmp = x_next  # Temporary storing the value of x

    print("x" + str(i) + " = " + str(x_next) + " - " + "f(x" + str(i) + ") = " + str(f(x_next)))
    x_next = x_next - (f(x_next)/f_dash(x_next))  # Computing new value of x with Newton-Raphson formula

    sleep(0.5)  # As always "good for visualization"
