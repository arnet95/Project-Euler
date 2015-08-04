#Project Euler 347: Largest integer divisible by two primes
from eulertools import primes

def gen_distinct_primefacs(n):
    prime_facs = [[] for i in xrange(n+1)]
    #[[]] * (n+1)
    for prime in primes(n+1):
        for i in xrange(prime, n+1, prime):
            prime_facs[i].append(prime)
    return prime_facs

def f(n):
    prime_factors = gen_distinct_primefacs(n)
    pairs = {}
    for i in xrange(n):
        p = prime_factors[i+1]
        if len(p) == 2:
            pairs[tuple(p)] = i
    return sum(pairs.values())

print f(10**7)
