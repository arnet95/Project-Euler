#Project Euler 234: Semidivisible numbers
from eulertools import primes

counter = 0

def f(p1, p2, n=None):
    s1 = range(p1**2 + p1, min(n+1, p2**2+1), p1)
    s2 = range(min(n-(n%p2), p2**2 - p2) , p1**2 - 1, - p2)
    s = 0
    count = 0
    for c in s1:
        if c not in s2:
            s += c
    for c in s2:
        if c not in s1:
            s += c
    return s

n = 999966663333
prime_list = primes(1000004)
print sum(f(prime_list[i], prime_list[i+1], n) for i in xrange(len(prime_list) - 1))
