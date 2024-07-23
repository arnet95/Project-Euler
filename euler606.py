from itertools import product
from eulertools import primes
from math import isqrt, log2


#Playing around with functions from Problem 548,
#one discovers that k has 252 gozinta chains iff k = p^3q^3 for distinct primes p, q

def semiprimes(N):
    s = set([])
    print(len(primes(N)))
    for p, q in product(primes(N), primes(N)):
        if p != q:
            if p*q <= N:
                s.add(p*q)
    return s

def S(N):
    return sum(k**3 for k in semiprimes(N))

print(S(10**6))