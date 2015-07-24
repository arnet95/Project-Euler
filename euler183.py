#Project Euler 183: Maximum product of parts
from math import e, ceil, log
from fractions import gcd


def reduced(n):
    while (n % 2) == 0:
        n = n // 2
    while (n % 5) == 0:
        n = n // 5
    return -1 if n == 1 else 1

def d(N):
    low = int(N/e)
    high = low + 1
    k = high if (low * (log(N) - log(low))) < (high * (log(N) - log(high))) else low
    k = k/(gcd(k, N))
    return reduced(k)*N

def main(n):
    return sum(d(i) for i in xrange(5, n+1))

print main(10000)
