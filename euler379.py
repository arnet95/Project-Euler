from eulertools import primes
from fractions import gcd

lcm = lambda x, y: (x*y)//gcd(x, y)

def f_test(n):
    return sum(lcm(x, y) == n for x in xrange(1, n+1) for y in xrange(x, n+1))

def g_test(n):
    return sum(f_test(i) for i in xrange(1, n+1))

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

def f(prime_fac):
    return prod([k+1 for k in prime_fac.values()])

def prime_factors_gen(n):
    factorisations = [{} for _ in xrange(n+1)]
    for p in primes(n+1):
        for i in xrange(p, n+1, p):
            factorisations[i][p] = 1
        k = 2
        while p**k <= n:
            for i in xrange(p**k, n+1, p**k):
                factorisations[i][p] += 1
            k += 1
    return factorisations

from eulertools import dynamic_sigma

sigmas = dynamic_sigma(0, 100)

def f(n):
    s = sigmas[n]
    return (s*(s+1))//2

#def test(n):
factorisations = prime_factors_gen(100)
for i in xrange(1, 101):
    print i, f_test(i) - f(i)

def g(n):
    factorisations = prime_factors_gen(n)
    return sum(f(factorisations[i]) for i in xrange(1, n+1))

#print g(10**6)
#test()
