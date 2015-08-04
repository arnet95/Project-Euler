from math import sqrt
from itertools import combinations
from eulertools import primes

def f(n):
    prime_list = primes(n)
    count = 0
    for i in xrange(2,n+1):
        if i in prime_list:
            count += i-1
        else:
            factors = []
            for p in prime_list:
                if p > i/2.0:
                    break
                if i%p == 0:
                    factors.append(p)
            count += pie(i, factors)
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
