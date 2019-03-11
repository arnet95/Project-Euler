from eulertools import primes, modinv

modulus = 10**9 + 7

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

factorisations = prime_factors_gen(20000)

def D(n):
    print n
    prod_dict = {}
    curr_dict = {}
    for k in xrange(1, n//2+1):
        for p in factorisations[n-k+1]:
            if p in curr_dict:
                curr_dict[p] += factorisations[n-k+1][p]
            else:
                curr_dict[p] = factorisations[n-k+1][p]
        for p in factorisations[k]:
            if curr_dict[p] > factorisations[k][p]:
                curr_dict[p] -= factorisations[k][p]
            else:
                del curr_dict[p]
        for p in curr_dict:
            if 2*k == n:
                multiplier = 1
            else:
                multiplier = 2
            if p in prod_dict:
                prod_dict[p] += multiplier*curr_dict[p]
            else:
                prod_dict[p] = multiplier*curr_dict[p]
    result = 1
    for p in prod_dict:
        result *= (pow(p, prod_dict[p]+1, modulus) - 1)
        result *= modinv(p-1, modulus)
        result %= modulus
    return result

def S(n):
    return sum(D(k) for k in xrange(1, n+1)) % modulus

print S(20000)
