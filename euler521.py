from eulertools import primes
import sys
prime_list = primes(10**6+1)

sys.setrecursionlimit(10**5)
def CSeq(n, i):
    pi = prime_list[i]
    if n < pi:
        return (0, 0)
    elif pi <= n and n < pi**2:
        return (1, pi)
    elif pi == 2:
        return (n // 2, (n // 2)*(n // 2 + 1))
    else:
        k = n // pi
        csum = 0
        ssum = 0
        for j in xrange(i):
            c, s = CSeq(k, j)
            csum += c
            ssum += s
        return (k - csum, pi*(tri(k) - ssum))

tri = lambda n: n*(n+1)//2

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def S(n):
    new_prime_list = primes(isqrt(n)+1)
    Pindex = len(new_prime_list)
    result = (tri(n) - 1)
    for i in xrange(Pindex):
        c, s = CSeq(n, i)
        result += (prime_list[i]*c - s)
    return result

print S(10**12)
