from itertools import product
from eulertools import primes

def compl_mult(t1, t2):
    return (t1[0]*t2[0] - t1[1]*t2[1], t1[0]*t2[1] + t1[1]*t2[0])

def gen_facs(n):
    l = [[] for _ in xrange(n+1)]
    for p in primes(n+1):
        k = 1
        while p**k <= n:
            for i in xrange(p**k, n+1, p**k):
                l[i].append(p)
            k += 1
    return l

l = gen_facs(2*(5**10))

def get_facs(n):
    d = {}
    for i in l[n]:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def combine_facs(fac1, fac2):
    d = {}
    for p in fac1:
        d[p] = fac1[p]
    for p in fac2:
        if p in d:
            d[p] += fac2[p]
        else:
            d[p] = fac2[p]
    return d

mem = {}
def prime_divs(p):
    if p in mem:
        return mem[p]
    for i in xrange(1, p):
        for j in xrange(1, i):
            if p == i**2+j**2:
                mem[p] = (i, j)
                return (i, j)

def f(z, r):
    print z
    result = 0
    curr_prod = (1, 0)
    prime_facs = combine_facs(get_facs(r+z), get_facs(r-z))
    curr_primes = prime_facs.keys()
    if 2 in curr_primes:
        for i in xrange(prime_facs[2]):
            curr_prod = compl_mult(curr_prod, (1, 1))
        curr_primes.remove(2)
    mod3_primes = [p for p in curr_primes if p % 4 == 3]
    if all([prime_facs[p] % 2 == 0 for p in mod3_primes]):
        for p in mod3_primes:
            curr_prod = compl_mult(curr_prod, (p**(prime_facs[p]//2), 0))
        mod1_primes = sorted([p for p in curr_primes if p % 4 == 1])
        length = len(mod1_primes)
        l = [range(prime_facs[p]+1) for p in mod1_primes]
        for picker in product(*l):
            new_prod = curr_prod
            for i in xrange(length):
                p = mod1_primes[i]
                div = prime_divs(p)
                conj_div = (div[0], -div[1])
                pick = picker[i]
                for j in xrange(pick):
                    new_prod = compl_mult(new_prod, div)
                for j in xrange(prime_facs[p] - pick):
                    new_prod = compl_mult(new_prod, conj_div)
            result += 4*(abs(new_prod[0])+abs(new_prod[1])+z)
    return result

def S(r):
    if r % 2 == 0:
        return 2*S(r//2)
    else:
        return 2*(sum(f(z, r) for z in xrange(1, r)) + r) + f(0, r)

print S(10**10)
