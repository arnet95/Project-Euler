#Project Euler 293: Pseudo-Fortunate Numbers

from eulertools import primes
from math import log

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

def prod(l):
    res = 1
    for i in l:
        res *= i
    return res

def pseudoFortunate(n):
    m = 3
    while True:
        if isprime(n+m):
            return m
        m += 2

def f(n):
    l = []
    i = 2
    while i < n:
        l.append(i)
        i *= 2
    prime_list = primes(1000)
    i = 1
    while prod(prime_list[:i]) < n:
        i += 1
    result = l
    for p in prime_list[1:i-1]:
        new = []
        for elem in l:
            if (n // elem) >= p:
                for i in xrange(1, int(log(n//elem, p))+1):
                    new.append(elem*p**i)
        result += new
        l = new
    return sum(set(pseudoFortunate(i) for i in result))

print f(10**9)
