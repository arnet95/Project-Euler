#Project Euler 347: Largest integer divisible by two primes
from eulertools import primes

def gen_distinct_primefacs(n):
    """Generates a list of a list of prime factors for all numbers <= n"""
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

#We go through the list of prime factors, and if it is of length 2, and we
#store it in a dictionary with the keys (p, q) where p and q are distinct primes.
#Since we go through the list in order, the final value for the key (p, q) will
#be the largest number <= n which is only divisible by both p and q. The result
#is then the sum of all the values in our dictionary.
