from math import sqrt
from itertools import combinations

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

primes = rwh_primes1(1000000)


def f(n):
    count = 0
    for i in xrange(2,n+1):
        if i in primes:
            count += i-1
        else:
            factors = []
            for p in primes:
                if p > i/2.0:
                    break
                if i%p == 0:
                    factors.append(p)
            count += pie(i, factors)
        if i%10000 == 0:
            print i
    return count


def pie(n, l):
    temp = 0
    for i in xrange(len(l)):
        temp_l = combinations(l, i+1)
        key_val = (-1)**(i)
        for comb in temp_l:
            a = 1
            for elem in comb:
                a *= elem
            temp += key_val * (n/a)
    return n - temp

print f(10**6)