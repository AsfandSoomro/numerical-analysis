"""
    This is a simple Bisection Method demonstration python program made by AsfandSoomro on 2/5/2022.
"""

from time import sleep
from math import sin, cos, pi, exp


# Function of x
def f(x):
    equation = x*x*x*x - 9 # Equation (Change Here)
    return equation


# Starting values for x (Change Here)
x1 = 1
x2 = 2

x3 = 0  # It will store the bisected value at each iteration
tmp = 0

if f(x1) == 0:
    print(str(x1) + " is the root")
    exit(0)
if f(x2) == 0:
    print(str(x2) + " is the root")
    exit(0)

for i in range(500):
    x3 = (x1 + x2) / 2  # Bisection Formula

    if f(x3) == 0:  # If it reaches the exact root value then exit loop
        print(str(x3) + " is the root")
        break
    if tmp == x3:  # If it reaches the most accurate value which is not 0 then exit loop
        break

    if f(x1)*f(x3) < 0:  # Check the condition 1
        x2 = x3
    elif f(x2)*f(x3) < 0:  # Check the condition 2
        x1 = x3

    tmp = x3  # Temporary storing previous value of x3 to keep track

    print("[" + str(x1) + ", " + str(x2) + "]" + " --- f(" + str(x3) + ") = " + str(f(x3)))
    print()

    sleep(0.5)  # Wait after each computation (good for eye)
