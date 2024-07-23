from math import gcd, isqrt
from eulertools import primes

def mobius_gen(n):
    mobius_list = [1 for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            mobius_list[i] *= (-1)
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                mobius_list[i] = 0
            k += 1
    return mobius_list


def D2(n):
    return 2*sum(n//i for i in range(1, isqrt(n)+1)) - isqrt(n)**2

mobius = mobius_gen(isqrt(10**15))
def h(n):
    result = 0
    for k in range(1, isqrt(n)+1):
        result += mobius[k]*D2(n//k**2)
    return result

def F(N):
    result = 0
    g = 1
    while g**2 <= N:
        if g < 1000:
            print(g)
        else:
            if g % 10000 == 0:
                print(g)
        result += g*h(N//(g**2))
        g += 1
    return result


print(F(10**15))