#Project Euler 183: Maximum product of parts
from __future__ import division
from math import e, ceil, log

def reduced(n):
    while n%2 == 0:
        n = n/2
    while n%5 == 0:
        n = n/5
    return -1 if n == 1 else 1

def d(N):
    minimum = N/e
    low = int(minimum)
    high = low + 1
    k = high if (low * log(N/low)) < (high * log(N/high)) else low
    return reduced(k)*N

def main(upper):
    return sum(d(n) for n in xrange(5, upper+1))

print main(100)
