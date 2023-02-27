from fractions import *
from math import copysign

sign = lambda x: copysign(1, x)

def I(r):
    l = []
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            if x**2 + y**2 < r**2:
                l.append((x, y))
    return l

def slope_from_origin(x,y):
    if x == 0:
        return "Inf"
    else:
        return Fraction(y, x)


def test(l):
    d = {}
    for x, y in l:
        t = (slope_from_origin(x, y), y >= 0)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    return len(d.keys())

print(test(I(3)))
print(test(I(5)))
print(test(I(105)))