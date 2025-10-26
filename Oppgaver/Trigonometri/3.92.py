# 3.93

# Forklar hva programmet gjør :

# Kjør programmet

from pylab import *

delta_x = 1E-8

def f(x):
    return sin(x)

def derivert(a, delta_x):
    return (f( a + delta_x) - f(a)) / delta_x

print(derivert(pi/3, delta_x))
