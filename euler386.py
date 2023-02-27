from eulertools import primes
from math import prod
from itertools import product

def exponents_gen(n):
    factorisations = [[] for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            factorisations[i].append(1)
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                factorisations[i][-1] += 1
            k += 1
    return factorisations

def N(exponents):
    if len(exponents) <= 1:
        return 1
    degrees = {}
    for t in product(*[range(e+1) for e in exponents]):
        degree = sum(t)
        if degree in degrees:
            degrees[degree] += 1
        else:
            degrees[degree] = 1
    return max(degrees.values())

def sum_N(L):
    d = {}
    for l in exponents_gen(L):
        t = tuple(sorted(l))
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    d[()] -= 1
    return sum(d[t]*N(t) for t in d)
    print(len(d))

print(sum_N(10**8))