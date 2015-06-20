from eulertools import primes
from math import log10, ceil

def prime_pair(p1, p2):
    x = pow(10, int(ceil(log10(p1))))
    n = 1
    while True:
        test = n*x + p1
        if test % p2 == 0:
            return test
        n = n + 1

def main(n):
    prime_list = primes(n)[2:]
    s = 0
    for i in xrange(len(prime_list)-1):
        p1 = prime_list[i]
        p2 = prime_list[i+1]
        s += prime_pair(p1, p2)
    return s

print main(10000004)