from itertools import product
from eulertools import primes, modinv

modulus = 10**9+7

def prod(l, mod):
    result = 1
    for i in l:
        result *= i
        result %= mod
    return result

def R(prime_fac):
    return prod([(1 + pow(prime, prime_fac[prime], modulus)) for prime in prime_fac], modulus) - prod([pow(prime, prime_fac[prime], modulus) for prime in prime_fac], modulus)

def prime_factors_gen(n):
    factorisations = [{} for _ in xrange(n+1)]
    for p in primes(n+1):
        for i in xrange(p, n+1, p):
            factorisations[i][p] = 1
        k = 2
        while p**k <= n:
            for i in xrange(p**k, n+1, p**k):
                factorisations[i][p] += 1
            k += 1
    return factorisations

def main(n):
    factorisations = prime_factors_gen(n)
    result = 0
    current_rval = 1
    prime_factorisation = {p: 0 for p in primes(n+1)}
    for k in xrange(1, n//2+1):
        print k
        numerator_change = 1
        denominator_change = 1
        change_dictionary = {}
        for p in factorisations[n-k+1]:
            change_dictionary[p] = factorisations[n-k+1][p]
        for p in factorisations[k]:
            if p in change_dictionary:
                change_dictionary[p] -= factorisations[k][p]
            else:
                change_dictionary[p] = -factorisations[k][p]
        for p in change_dictionary:
            if prime_factorisation[p] + change_dictionary[p] != 0:
                numerator_change *= (1 + pow(p, prime_factorisation[p] + change_dictionary[p], modulus))
            if prime_factorisation[p] != 0:
                denominator_change *= (1 + pow(p, prime_factorisation[p], modulus))
            prime_factorisation[p] += change_dictionary[p]
            numerator_change %= modulus
            denominator_change %= modulus
        current_rval *= numerator_change
        current_rval *= modinv(denominator_change, modulus)
        current_rval %= modulus
        if k < n//2:
            result += 2*current_rval
        else:
            result += current_rval
        result %= modulus
    return (result - pow(2, n, modulus) + 2) % modulus

print main(10**7)
