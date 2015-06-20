#Euler 179
from eulertools import primes



def f(n):
    primes_list = primes(n)
    mod_primes_list = primes_list[1:]
    possibilities = [2, 3]
    for i in xrange(4, n):
        if i in mod_primes_list