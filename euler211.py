#Project Euler 211: Divisor Square Sum
from math import sqrt
from eulertools import dynamic_sigma
import time

def is_square2(n):
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def is_square(n):
    if sqrt(n) % 1 == 0:
        if abs(sqrt(n)**2 - n) < 1E-8:
            return is_square2(n)
    return False

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
