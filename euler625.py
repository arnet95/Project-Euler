from eulertools import isqrt
from math import log

def tri(n):
    return n*(n+1)//2

mem = {}
sieve = []
max_n = 0
current_L = 0

def totientsumgen(n, L, cache, sieve):
    if n <= L:
        return sieve[n]
    if n in cache:
        return cache[n]
    result = tri(n)
    for g in xrange(2, isqrt(n)+1):
        result -= totientsumgen(n//g, L, cache, sieve)
    for z in xrange(1, isqrt(n)+1):
        if (n // z) != z:
            result -= ((n//z) - (n//(z+1)))*totientsumgen(z, L, cache, sieve)
    cache[n] = result
    return result

def totientsum(n):
    if n in mem:
        return mem[n]
    global max_n, sieve, current_L
    if n > max_n:
        L = int((n/(log(log(n))))**(2/3.))
        sieve = range(L+1)
        for p in xrange(2, L+1):
            if p == sieve[p]:
                for k in xrange(p, L+1, p):
                    sieve[k] = (sieve[k]*(p-1))//p
            sieve[p] = sieve[p] + sieve[p-1]
        max_n = n
        current_L = L
    return totientsumgen(n, current_L, mem, sieve)

def G(N):
    result = 0
    for j in xrange(1, isqrt(N)+1):
        result += j*totientsum(N//j)
    for z in xrange(1, isqrt(N)+1):
        if z != (N//z):
            result += (tri((N//z)) - tri(N//(z+1)))*totientsum(z)
    return result

print G(10**11) % 998244353
