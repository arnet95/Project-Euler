from eulertools import primes, isqrt

N = 2**50

prime_list = primes(isqrt(N)+1)

mem = {}
def psqfeq(n, i):
    pi = prime_list[i]
    if i == 0:
        return n // 4
    elif n < 4*pi**2:
        return n // (pi**2)
    else:
        k = n // (pi**2)
        return k - sum(psqfeq(k, j) for j in xrange(i))

print N - sum(psqfeq(N, i) for i in xrange(len(prime_list)))
