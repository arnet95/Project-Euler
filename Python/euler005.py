#Project Euler 5: Smallest multiple

from eulertools import primes
from math import log


def f(n):
    """This function returns the smallest positive number
    which is evenly divisble by all the numbers from 1 to n"""
    product = 1
    for i in primes(n+1):
        #For each prime less than or equal to n,
        #find the largest power of that prime less than or equal to n
        #Multiply all these prime powers together. It will give the right result.
        target = log(n)/log(i)
        k = 1
        while k < target:
            k += 1
        product *= i**(k-1)
    return product

print f(20)
