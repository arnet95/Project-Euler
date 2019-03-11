from eulertools import isqrt

mem = {}

def totientsum(n):
    if n in mem:
        return mem[n]
    result = n*(n+1)//2
    for g in xrange(2, isqrt(n)+1):
        result -= totientsum(n//g)
    for z in xrange(1, isqrt(n)+1):
        if (n // z) != z:
            result -= ((n//z) - (n//(z+1)))*totientsum(z)
    mem[n] = result
    return result

def f(n):
    result = 0
    k = 1
    while 2**k <= n:
        result += (totientsum(n//(2**k))-1)
        k += 1
    return result

print f(10**11) % (10**9+7)
