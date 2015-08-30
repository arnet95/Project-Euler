#Project Euler 139: Pythagorean tiles
from fractions import gcd

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main(limit_perimeter):
    counter = 1
    for m in xrange(2, isqrt(limit_perimeter // 4) + 2):
        for n in xrange((m%2) + 1, m, 2):
            if gcd(m, n) == 1:
                primitive_length = 2*m*(m+n)
                for k in xrange(1, limit_perimeter//primitive_length + 1):
                    a, b, c = (k*(m**2-n**2), k*2*m*n, k*(m**2+n**2))
                    if c % isqrt(c*c - 2*a*b) == 0:
                        counter += 1
    return counter

print main(10**8)

#Quite bad!!!! +2 mins in pypy
