#Euler 179
from eulertools import primes
from math import sqrt



def f(n):
    primes_list = primes(n)
    squares_list = [i**2 for i in xrange(1, int(sqrt(n)) + 1)]
    candidates = range(1, n)

f(10**7)