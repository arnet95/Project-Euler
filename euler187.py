#Euler 187
from time import time
from eulertools import primes



def f(n):

    a = primes(5*(10**7))
    l = []

    for i in a:
        for j in a:
            x = i*j
            if x < 10**8:
                l.append(x)
            else:
                break

    return len(set(l))


print f(1)
