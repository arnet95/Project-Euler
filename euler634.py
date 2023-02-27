from math import sqrt, isqrt
from eulertools import primes


def is_square(n):
    return isqrt(n)**2 == n

def squarefree(n):
    for p in primes(n+1):
        if n % (p**2) == 0:
            return False
    return True

def F(n):
    s = set([])
    
    for b in range(2, int(n**(1/3.))+1):
        for a in range(2, int(sqrt((n // (b**3))))+1):
            if a**2*b**3 in s:
                print(is_square(b))
            else:
                s.add(a**2*b**3)
    return len(s)
print(F(3*10**6))
