#Project Euler 346: Strong Repunits
from math import sqrt

def f(n):
    l = [1]
    for b in xrange(2, int(sqrt(n)) + 1):
        s = 1 + b + b**2
        i = 3
        while s < n:
            l.append(s)
            s += b**i
            i += 1
    return sum(list(set(l)))

print f(10**12)
