from eulertools import primes
from math import log

def legendre(p, n):
    return sum(n // (p**k) for k in xrange(1, int(log(n)/log(p)) + 1))

def main(n, modulus):
    result = 1
    for p in primes(n):
        result *= (pow(p, 2*legendre(p, n), modulus) + 1)
        result %= modulus
    return result

print main(10**8, 1000000009)
