from fractions import gcd
from itertools import product

#By rewriting the equations, we get that fn(x, y, z) = 0 iff x^n + y^n = z^n.
#By Fermat's Last Theorem, this can only happen if n = 1, 2, -1, -2.
#We then generate all fractions satisfying the conditions, and check if
#the equation holds for any of the n's.

#Using fractions from the Python library was very slow, so we use our own
#variant instead, which uses tuples of integers.

#This is very slow for normal Python, but very fast with PyPy (for some reason).

def eq_check(n, x, y, z):
    a, b = x
    c, d = y
    e, f = z
    return (a*d*f)**n + (b*c*f)**n == (b*d*e)**n

def shorten(a, b):
    g = gcd(a, b)
    return (a // g, b // g)

def rational_sum(x, y, z):
    a, b = x
    c, d = y
    e, f = z
    return shorten(a*d*f+b*c*f+b*d*e, b*d*f)

def test_fractions(x, y, z):
    x1, y1, z1 = (x[1], x[0]), (y[1], y[0]), (z[1], z[0])
    if eq_check(1, x, y, z):
        return True
    elif eq_check(2, x, y, z):
        return True
    elif eq_check(1, x1, y1, z1):
        return True
    elif eq_check(2, x1, y1, z1):
        return True
    else:
        return False

def main(k):
    results = set([])
    l = [(a, b) for a in xrange(1, k) for b in xrange(a+1, k+1) if gcd(a, b) == 1]
    for x, y, z in product(l, repeat=3):
        if test_fractions(x, y, z):
            results.add(rational_sum(x, y, z))
    result = (0, 1)
    for a, b in results:
        g, h = result
        result = shorten(a*h + b*g, b*h)
    return result[0] + result[1]

print main(35)
