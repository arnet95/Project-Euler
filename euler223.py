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

def is_square(n, p):
    return pow(n, (p-1) // 2, p) == 1

def exp_in_fp2(l, exponent, k, p):
    if exponent == 0:
        return (1, 0)
    elif exponent == 1:
        return l
    elif exponent % 2 == 0:
        x, y = l
        return exp_in_fp2(((x**2+y**2*k) % p , (2*x*y) % p), exponent//2, k, p)
    else:
        x, y = l
        z, w = exp_in_fp2(((x**2+y**2*k) % p , (2*x*y) % p), (exponent-1)//2, k, p)
        return ((x*z+y*w*k) % p, (x*w+y*z) % p)

def find_square_roots(n, p):
    """Implementing Cipolli's algorithm"""
    a = 1
    while is_square((a**2-n) % p, p):
        a += 1
    result = exp_in_fp2((a, 1), (p+1)//2, (a**2-n) % p, p)
    return result[0], p - result[0]

def prod(fac):
    result = 1
    for p in fac:
        result *= (p**fac[p])
    return result

def f(perimeter):
    climit = perimeter // 2
    count = 0
    cfactorisations = [{} for _ in xrange(climit+1)]
    #Fill in cfactorisations
    for sol in xrange(1, climit+1, 2):
        cfactorisations[sol][2] = 1
    for p in primes(climit+1)[1:]:
        if is_square(p-1, p):
            a, b = find_square_roots(p-1, p)
            for sol in range(a, climit+1, p) + range(b, climit+1, p):
                k = 0
                N = sol**2 + 1
                while N % p == 0:
                    N //= p
                    k += 1
                cfactorisations[sol][p] = k
    for c in xrange(1, climit+1):
        if (c**2+1) != prod(cfactorisations[c]):
            cfactorisations[c][(c**2+1)//prod(cfactorisations[c])] = 1
    print "Completed factorisations"
    for c in xrange(1, climit+1):
        print c
        new_count = 0
        curr_prod = (1, 0)
        prime_facs = cfactorisations[c]
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
                    if a >= 0 and b >= 0:
                        if a <= b:
                            if c <= k*(a + b):
                                if k*a + k*b + c <= perimeter:
                                    new_count += 1
        count += new_count
    return count

print f(25*10**6)
