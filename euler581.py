from eulertools import isqrt, primes, modinv
from itertools import chain, combinations
from fractions import gcd

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

def isPsmooth(n, P):
    result = n
    for p in P:
        while result % p == 0:
            result //= p
        if result == 1:
            return True
    return False
    #return result == 1

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def cfrac_sqrt(n):
    k = isqrt(n)
    res = [k]
    a, b, c = 0, 1, k
    while a != 2*k:
        t = n - c * c
        b = t // gcd(b, t)
        a = (c + k) // b
        c = k - (c + k) % b
        res.append(a)
    return res

def pell(n):
    cf = cfrac_sqrt(n)
    e = cf[1:]
    i, le = -1, len(e)
    a, b = 1, cf[0]
    c, d = 0, 1
    while (b*b - n*d*d) != 1:
        i = (i + 1) % le
        a, b = b, e[i] * b + a
        c, d = d, e[i] * d + c
    xi, yi = b, d
    while True:
        yield xi, yi
        xi, yi = b*xi+n*d*yi, d*xi+b*yi


def pell1(n):
    cf = cf_gen(n)
    a, b = 1, cf.next()
    c, d = 0, 1
    while (b*b - n*d*d) != 1:
        an = cf.next()
        a, b = b, an * b + a
        c, d = d, an * d + c
    return b, d

def solve(D):
    a, b = isqrt(D), 1
    k = a**2 - D
    while k != 1:
        absk = abs(k)
        #Finding
        if a % k == 0:
            m = absk
        else:
            m = ((absk - a)*modinv(b, absk)) % absk
        old_dist = abs(m**2 - D)
        new_dist = abs(m**2 - D)
        while new_dist <= old_dist:
            m += absk
            old_dist = new_dist
            new_dist = abs(m**2 - D)
        m -= absk
        a, b, k = (a*m + D*b) // absk, (a + b*m) // absk, (m**2 - D) // k
    return a, b

def Psmoothpairs(P):
    nterms = max(3, (max(P) + 1)//2)
    s = set([])
    count = 0
    squarefrees = [prod(l) for l in powerset(P) if prod(l) != 2]
    for q in squarefrees:
        count += 1
        print count
        D = 2*q
        sol_gen = pell(D)
        for i in xrange(nterms):
            x, y = sol_gen.next()
            if isPsmooth(y, P):
                s.add((x-1)//2)
            else:
                if i == 0:
                    break
    print len(s)
    return sum(s)

def main(n):
    return Psmoothpairs(primes(n+1))

#print main(5)
print main(47)
