#Project Euler 231: The prime factorisation of binomial coefficients
from eulertools import primes
from math import log

def convert_to(b, n):
    k = int(log(n)/log(b))
    l = [0]*(k+1)
    while n > 0:
        l[k] = n/(b**k)
        n = n % (b**k)
        k -= 1
    return l

def g(p, n):
    return sum(b*((p**i-1)//(p-1)) for i, b in enumerate(convert_to(p, n)))

def f(n):
    s = 0
    for p in primes(n):
        if p > n/2:
            s += p
        else:
            s += p*g(p, n)
    return s


def main(m, n):
    return f(m) - f(n) - f(m-n)

print main(20000000, 15000000)
