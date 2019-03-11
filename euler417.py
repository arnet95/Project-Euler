from eulertools import primes
from fractions import gcd

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


def lcm(a, b):
    return (a*b)//gcd(a, b)

lcm_list = lambda l: 0 if l == [] else reduce(lcm, l)

prime_factors_list = prime_factors_gen(10**8)

mem = {}
def order10(p, k):
    if (p, k) in mem:
        return mem[(p, k)]
    N = p**k
    totient = p**(k-1)*(p-1)
    prime_factors = prime_factors_list[p**(k-1)*(p-1)]
    for prime in prime_factors:
        for i in xrange(prime_factors[prime]):
            totient //= prime
            if pow(10, totient, N) != 1:
                totient *= prime
                break
    mem[(p, k)] = totient
    return totient

result = 0
for n in xrange(3, 10**6+1):
    result += lcm_list([order10(p, prime_factors_list[n][p]) for p in prime_factors_list[n] if p != 2 and p != 5])
print result
