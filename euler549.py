from eulertools import primes
from math import log

def legendre(p, n):
    return sum(n // (p**k) for k in xrange(1, int(log(n)/log(p)) + 1))

def s(p, r):
    if r <= p:
        return p*r
    else:
        x = p
        while legendre(p, x) < r:
            x += p
        return x

def S(n):
    prime_list = primes(n+1)
    l = [0, 0] + [1]*(n-1)
    for prime in prime_list:
        for k in xrange(1, int(log(n)/log(prime))+1):
            res = s(prime, k)
            for index in xrange(prime**k, n+1, prime**k):
                l[index] = max(l[index], res)
    return sum(l)

print S(10**8)
