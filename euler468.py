from eulertools import primes

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

def sbsum(fac, n, mod):
    prime_list = sorted(fac.keys())
    result = 1*(prime_list[0]-1)
    curr_prod = 1
    length = len(prime_list)
    for i in xrange(length-1):
        curr_prod *= pow(prime_list[i], fac[prime_list[i]], mod)
        curr_prod %= mod
        result += (curr_prod * (prime_list[i+1]-prime_list[i]))
        result %= mod
    curr_prod *= pow(prime_list[length-1], fac[prime_list[length-1]], mod)
    curr_prod %= mod
    result += (curr_prod * ((n+1) - prime_list[length-1]))
    result %= mod
    return result

def prod(fac):
    result = 1
    for p in fac:
        result *= p**fac[p]
    return result

def F(n, mod):
    factorisations = prime_factors_gen(n)
    result = n
    current_factorisation = {}
    for k in xrange(1, n//2+1):
        print k
        for p in factorisations[n-k+1]:
            if p in current_factorisation:
                current_factorisation[p] += factorisations[n-k+1][p]
            else:
                current_factorisation[p] = factorisations[n-k+1][p]
        for p in factorisations[k]:
            if current_factorisation[p] == factorisations[k][p]:
                del current_factorisation[p]
            else:
                current_factorisation[p] -= factorisations[k][p]
        result += sbsum(current_factorisation, n, mod)
        result %= mod
    return (2*result) % mod

print F(111111, 1000000993)
