from itertools import product
from eulertools import primes

def mods(a, n):
    if n <= 0:
        return "negative modulus"
    a = a % n
    if (2 * a > n):
        a -= n
    return a

def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n))/n

def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return(w0 - z0 * u0 + z1 * u1,
           w1 - z0 * u1 - z1 * u0)

def ggcd(w, z):
    while z != (0,0):
        w, z = z, grem(w, z)
    return w

def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1"
    k = p/4
    j = 2
    while True:
        a = pow(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1

def sq2(p):
    a = root4(p)
    return ggcd((p,0),(a,1))

def compl_mult(t1, t2):
    return (t1[0]*t2[0] - t1[1]*t2[1], t1[0]*t2[1] + t1[1]*t2[0])

mem = {}
def prime_divs(p):
    if p in mem:
        return mem[p]
    else:
        result = sq2(p)
        mem[p] = result
        return result

def factors_of_even_gen(n):
    factorisations = [{} for _ in xrange(0, n+1, 2)]
    for i in xrange(2, n+1, 2):
        factorisations[i//2][2] = 1
    k = 2
    while 2**k <= n:
        for i in xrange(2**k, n+1, 2**k):
            factorisations[i//2][2] += 1
        k += 1
    for p in primes(n+1)[1:]:
        print p
        for i in xrange(2*p, n+1, 2*p):
            factorisations[i//2][p] = 1
        k = 2
        while p**k <= n:
            for i in xrange(2*p**k, n+1, 2*p**k):
                factorisations[i//2][p] += 1
            k += 1
    return factorisations

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

def f(perimeter):
    climit = perimeter // 2
    count = 0
    factorisations = factors_of_even_gen(climit+1)
    for c in xrange(3, climit+1, 2):
        print c
        new_count = 0
        curr_prod = (1, 0)
        prime_facs = combine_facs(factorisations[(c-1)//2], factorisations[(c+1)//2])
        curr_primes = prime_facs.keys()
        if 2 in curr_primes:
            for i in xrange(prime_facs[2]):
                curr_prod = compl_mult(curr_prod, (1, 1))
            curr_primes.remove(2)
        mod3_primes = [p for p in curr_primes if p % 4 == 3]
        if all([prime_facs[p] % 2 == 0 for p in mod3_primes]):
            k = 1
            for p in mod3_primes:
                k *= p**(prime_facs[p]//2)
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
                for z in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    a, b = compl_mult(new_prod, z)
                    if a > 0 and b >= a:
                        if c <= k*(a + b):
                            if k*a + k*b + c <= perimeter:
                                new_count += 1
        count += new_count
    return count

print f(75*10**6)
