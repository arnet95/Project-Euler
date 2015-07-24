#Project Euler 479: Roots on the Rise
m = 1000000007
from eulertools import modinv

def S(n):
    s = 0
    for k in xrange(1, n+1):
        a = k**2
        s += (1 - a) * (1 - pow(1 - a, n, m)) * modinv(a, m)
        s %= m
    return s

print S(10**6)
