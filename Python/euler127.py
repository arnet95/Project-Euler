#Project Euler 127: abc-hits
from eulertools import primes
from fractions import gcd

def rad(n):
    """Creates list of radicals up to n"""
    l = [1]*(n+1)
    for prime in primes(n+1):
        for i in xrange(prime, n+1, prime):
            l[i] *= prime
    return l

def main(n):
    s = 0
    radicals = rad(n)
    for c in xrange(3, n):
        if radicals[c] < c:
            if c % 2 == 0:
                for a in xrange(1, c//2+1, 2):
                    if radicals[a]*radicals[c-a]*radicals[c] < c:
                        if gcd(a, c) == 1 and gcd(a, c-a) == 1:
                            s += c
            else:
                for a in xrange(1, c//2+1):
                    if radicals[a]*radicals[c-a]*radicals[c] < c:
                        if gcd(a, c) == 1 and gcd(a, c-a) == 1:
                            s += c
    return s

print main(120000)

#There are two main ideas needed in order to solve this problem.
#Firstly, since a, b, and c are all relatively prime, we have
#rad(abc) = rad(a)rad(b)rad(c).
#Secondly, we can precompute the radicals in order to decrease computation time later.
#Now, it's just a matter of generating all triples satisfying the four conditions.
