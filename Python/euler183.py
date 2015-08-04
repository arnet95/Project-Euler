#Project Euler 183: Maximum product of parts
from math import e, log
from fractions import gcd

def reduced(n):
    while (n % 2) == 0:
        n = n // 2
    while (n % 5) == 0:
        n = n // 5
    return -1 if n == 1 else 1

def d(N):
    #We have that the maximum point of (N/k)**k is at N/e,
    #which means that the two possible integer values for the maximum are at floor(N/e) and ceil(N/e)
    low = int(N/e)
    high = low + 1
    k = high if (low * (log(N) - log(low))) < (high * (log(N) - log(high))) else low
    k = k/(gcd(k, N))
    #When we have found the maximum point, we check whether N/k in its lowest possible terms is terminating or not.
    return reduced(k)*N

def main(n):
    return sum(d(i) for i in xrange(5, n+1))

print main(10000)
