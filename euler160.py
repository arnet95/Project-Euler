#Project Euler 160: Factorial trailing digits
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
    return sum(b*((p**i-1)/(p-1)) for i, b in enumerate(convert_to(p, n)))

def main(n):
    prime_list = primes(n)
    l = [g(p, n) for p in prime_list]
    l[0] -= l[2]
    l[2] = 0
    return 2

print len(primes(10**12))
