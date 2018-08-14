from eulertools import primes

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def S(n):
    l = [True] * (5*n)
    low = ((n-2)*(n-3))//2 + 1
    high = ((n+2)*(n+3))//2
    for p in primes(isqrt(high)+1):
        if low % p == 0:
            for i in xrange(low, high+1, p):
                l[i-low] = False
        else:
            for i in xrange( ((low //p)+1)*p, high+1, p):
                l[i-low] = False
    prevrowlow = ((n-2)*(n-1))//2 + 1
    prevrowhigh = ((n-1)*n)//2
    nthrowlow = ((n-1)*n)//2 + 1
    nthrowhigh = (n*(n+1))//2
    nextrowlow = (n*(n+1))//2 + 1
    nextrowhigh = ((n+1)*(n+2))//2
    return [i+low for i in xrange(5*n) if l[i]]

S(5678027)
