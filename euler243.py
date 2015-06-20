#Euler 243
from __future__ import division
from eulertools import primes
prime_list = primes(10**6)

target = 15499/94744

def get_resilience(p, k):
    resilience = 1
    d = 1
    for a, b in zip(p, k):
        resilience *= (a-1)*(a**(b-1))
        d *= a**b
    resilience = resilience/(d-1)
    return d, resilience, resilience < target, target

#print get_resilience(prime_list[:9] + [prime_list[10]])
print get_resilience(prime_list[:10], [1 for i in xrange(10)])
print get_resilience(prime_list[:9], [2, 2, 1, 1, 1, 1, 1, 1, 1])

print prime_list[:9]

"""1338557220"""