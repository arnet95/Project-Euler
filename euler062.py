#Project Euler 62: Cubic permutations
from __future__ import division

def final(n, goal):
    lower_limit = 10 ** ((n-1)/3)
    upper_limit = 10 ** (n/3)
    l = []
    for x in xrange(int(lower_limit), int(upper_limit)+1):
        s = ''.join(sorted(str(x**3)))
        if s == goal:
            l.append(x)
    return l

def f(target):
    n = 1
    while True:
        lower_limit = 10 ** ((n-1)/3)
        upper_limit = 10 ** (n/3)
        d = {}
        for x in xrange(int(lower_limit), int(upper_limit)+1):
            s = ''.join(sorted(str(x**3)))
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        min_cube = 10**(4*n)
        test = False
        for key in d:
            if d[key] == target:
                min_cube = min(min_cube, min(final(n, key))**3)
                test = True
        if test:
            return min_cube
        n += 1

print f(5)
