from fractions import *
from eulertools import primes

def legendre(p, n):
    if n == 0:
        return 0
    count = 0
    power = p
    while power <= n:
        count += (n//power)
        power *= p
    return count

def all_pfs(n, ps):
    for p in ps:
        while n % p == 0:
            n //= p
    return n == 1

def check(f, ps):
    num = f.numerator
    den = f.denominator
    return all_pfs(num, ps) and all_pfs(den, ps)

def C(facs):
    d = {Fraction(1): 1}
    m = max(facs.values())
    prime_list = primes(m+1)
    ps = sorted(facs.keys(), key=lambda x: -facs[x])
    for i in range(len(ps)):
        p = ps[i]
        k = facs[p]
        new_d = {}
        for j in range(k+1):
            for f in d:
                new_f = f*Fraction(j+1, k-j+1)
                if new_f in new_d:
                    new_d[new_f] += d[f]
                else:
                    new_d[new_f] = d[f]
        if i + 1 < len(ps):
            l = [p for p in prime_list if p <= facs[ps[i+1]]+1]
            d = {f: new_d[f] for f in new_d if check(f, l)}
        else:
            d = {f: new_d[f] for f in new_d}
    return d[Fraction(1)]//2

facs = {p: legendre(p, 100) for p in primes(100)}
print(C(facs))