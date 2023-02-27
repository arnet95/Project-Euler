from eulertools import primes
#from math import isqrt

def prime_factors_gen(n):
    factorisations = [{} for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            factorisations[i][p] = 1
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                factorisations[i][p] += 1
            k += 1
    return factorisations

def f(L):
    facs = prime_factors_gen(int(L**0.5)+1)
    power = 2
    result = 0
    while 2**power <= L:
        for q in primes(int(L**(1/power))+1):
            limit = L//(q**power)
            l = [1]
            for p in primes(q-1):
                new_l = []
                pk = p
                while pk <= limit:
                    i = 0
                    while l[i]*pk <= limit:
                        new_l.append(l[i]*pk)
                        i += 1
                    pk *= p
                l = sorted(new_l)
            


        power += 3
    q = 2, 5, 8