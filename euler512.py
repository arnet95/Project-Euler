#Project Euler 512: Sums of totients of powers
from eulertools import primes
from math import log

def totient_gen(n):
    phis = [2*i-1 for i in xrange(1, n/2+1)]
    odd_primes = primes(n+1)[1:]
    for p in odd_primes:
        for i in xrange(p, n, 2*p):
            phis[i//2] /= p
            phis[i//2] *= (p-1)
    return phis

def main(n):
    odd_totients = totient_gen(n)
    return sum(odd_totients)

print main(5*10**7)

#Through some calculations, we get that g(n) is given by the sum of
#odd totients up to, and including n.
#We use a sieve to compute the sum.
