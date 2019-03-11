from math import log

def legendre(p, n):
    if n == 0:
        return 0
    return sum(n // (p**k) for k in xrange(1, int(log(n)/log(p)) + 1))

def order(p, n):
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count

def v(p, n, k):
    return legendre(p, n) - (legendre(p, k) + legendre(p, n-k))


def f(n):
    count = 0
    for i in xrange(n+1):
        a, b = 12 - v(2, n, i), 12 - v(5, n, i)
    return count

print f(2*10**5)
