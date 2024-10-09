
# En numerisk ekvationslösare

import math

def f(x):
    return x**2-1

def derivative(f,x,h):
    första_derivatan = ( 1/(2*h) )*( f(x+h)-f(x-h) )
    return första_derivatan
    #return flyttal

print(derivative(f,math.pi, 0.001))

# 5b
        
def solve(f,x0,h):
    xn_1 = 0
    while True:
        xn_1 = x0 - (f(x0)/derivative(f,x0,h))
        if abs( x0 - xn_1 ) <= h:
            return xn_1
        x0 = xn_1

print(solve(f,4,0.01))

import d0009e_lab2_solveTest