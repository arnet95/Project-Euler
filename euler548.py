from itertools import product
from eulertools import primes
from math import isqrt, log2

g_mem = {(): 1}
def g(tup):
    #Assume that t is in descending order
    if tup in g_mem:
        return g_mem[tup]
    else:
        result = 0
        for t in product(*[range(i+1) for i in tup]):
            if t != tup:
                result += g(tuple(sorted([i for i in t if i != 0], reverse=True)))
        g_mem[tup] = result
        return result

def factorise(n):
    if n == 1:
        return {}
    d = {}
    if n < 4:
        ps = []
    else:
        ps = primes(isqrt(n))

    for p in ps:
        if n % p == 0:
            count = 0
            while n % p == 0:
                n //= p
                count += 1
            d[p] = count
        if n == 1:
            return d
    d[n] = 1
    return d

def gen_help(i, L, lim, ps):
    results = [()]
    k = 1
    while ps[i]**k <= L and k <= lim:
        sub_results = gen_help(i+1, L//(ps[i]**k), k, ps)
        for sub in sub_results:
            results.append((k, ) + sub)
        k += 1
    return results


def gen_prime_signatures(N):
    ps = primes(100)
    return gen_help(0, N, int(log2(N))+2, ps)

def f(N):
    result = 0
    for prime_sig in gen_prime_signatures(N):
        if prime_sig == ():
            result += 1
        else:
            gchains = g(prime_sig)
            if gchains <= N:
                fac = factorise(gchains)
                if tuple(sorted(fac.values(), reverse=True)) == prime_sig:
                    result += gchains
                    print(gchains, prime_sig)
    return result

#print(f(10**16))