def solutions(p):
    if gcd(15, p-1) == 1:
        return [p-1]
    else:
        #Needs improvement
        return [n for n in xrange(p) if (pow(n, 15, p) == p-1)]

def S(N, m):
    result = 0
    for p in primes(m+1):
        for sol in solutions(p):
            result += p*((n-sol)//p)
