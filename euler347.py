#Project Euler 347: Largest integer divisible by two primes
from eulertools import primes

def gen_distinct_primefacs(n):
    prime_facs = [[] for i in xrange(n+1)]
    for prime in primes(n+1):
        for i in xrange(prime, n+1, prime):
            prime_facs[i].append(prime)
    return prime_facs

def S(n):
    prime_factors = gen_distinct_primefacs(n)
    pairs = {}
    for i in xrange(1, n+1):
        p = prime_factors[i]
        if len(p) == 2:
            pairs[tuple(p)] = i
    return sum(pairs.values())

print S(10**7)
