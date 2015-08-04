#Project Euler 211: Divisor Square Sum
from math import sqrt
from eulertools import dynamic_sigma
import time

def is_square(n):
    #Turns out to be good enough in this case
    return sqrt(n) % 1 == 0

def main(n):
    s = 1
    l = dynamic_sigma(2, n)
    for i in xrange(2, len(l)):
        if is_square(l[i]):
            s += i
    return s

t = time.time()
print main(64*10**6)
print time.time() - t
#Quite slow, use PyPy
