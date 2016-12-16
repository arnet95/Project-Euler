#Euler 187
from eulertools import primes

#This is a fairly straightforward solution, with basically no thinking done.
#The method is to generate all semiprimes in a structured way such that one
#does not generate many semiprimes bigger than the desired limit.

def f(n):
    prime_list = primes(n // 2)
    semiprimes = set([])
    for factor1 in prime_list:
        for factor2 in prime_list:
            x = factor1 * factor2
            if x < n:
                semiprimes.add(x)
            else:
                break
    return len(semiprimes)

print f(10**8)
