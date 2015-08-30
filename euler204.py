#Project Euler 204: Generalised Hamming Numbers
from eulertools import primes
from math import log

def f(type_n, limit):
    prime_list = primes(type_n+1)
    l = [1]
    for prime in prime_list:
        for elem in l:
            if prime > limit // elem:
                break
            for i in xrange(1, int(log(limit//elem, prime))+1):
                l.append(elem*prime**i)
        l.sort()
    return len(set(l))

print f(100, 10**9)
