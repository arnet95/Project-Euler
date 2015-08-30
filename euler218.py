#Project Euler 218: Perfect right-angled triangles
from fractions import gcd



def f(limit):
    perfect = 0
    superperfect = 0

    for r in xrange(2, int(limit**0.5)):
        for s in xrange((r%2) + 1, r, 2):
            if gcd(r, s) == 1:
                n, m = r**2 - s**2, 2*r*s
                n, m = min(n, m), max(n, m)
                area = (m**2 - n**2) * m * n
                perfect += 1
                if area % 6 == 0 and area % 28 == 0:
                    superperfect += 1
    print perfect, superperfect
    return perfect - superperfect

print f(10**8)
