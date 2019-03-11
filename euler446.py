from itertools import product
from eulertools import primes, modinv

modulus = 10**9+7

def prod(l):
    result = 1
    for i in l:
        result *= i
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

pos_f = lambda x: x**2 + 2*x + 2
neg_f = lambda x: x**2 - 2*x + 2

def R(prime_fac):
    return prod([(1 + p**prime_fac[p]) for p in prime_fac]) - prod([p**prime_fac[p] for p in prime_fac])

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

def F(N):
    neg_factorisations = [{} for _ in xrange(N+1)]
    pos_factorisations = [{} for _ in xrange(N+1)]
    for i in xrange(2, N+1, 2):
        neg_factorisations[i][2] = 1
        pos_factorisations[i][2] = 1
    for p in primes(N+3)[1:]:
        if p % 4 == 1:
            #Then -1 is a quadratic residue
            m1, m2 = find_square_roots(p-1, p)
            pos_solutions = [m1 - 1, m2 - 1]
            neg_solutions = [m1 + 1, m2 + 1]
            k = 1
            while p**(k-1) <= N:
                for sol in pos_solutions:
                    for i in xrange(sol, N+1, p**k):
                        if p in pos_factorisations[i]:
                            pos_factorisations[i][p] += 1
                        else:
                            pos_factorisations[i][p] = 1
                for sol in neg_solutions:
                    for i in xrange(sol, N+1, p**k):
                        if p in neg_factorisations[i]:
                            neg_factorisations[i][p] += 1
                        else:
                            neg_factorisations[i][p] = 1
                pos_solutions = [(x - (pos_f(x)*modinv(2*x+2, p))) % p**(k+1) for x in pos_solutions]
                neg_solutions = [(x - (neg_f(x)*modinv(2*x-2, p))) % p**(k+1) for x in neg_solutions]
                k += 1
    result = 0
    for i in xrange(1, N+1):
        print i
        pos_factor_result = prod([p**pos_factorisations[i][p] for p in pos_factorisations[i]])
        neg_factor_result = prod([p**neg_factorisations[i][p] for p in neg_factorisations[i]])
        if pos_factor_result != pos_f(i):
            if pos_f(i)//pos_factor_result in pos_factorisations[i]:
                pos_factorisations[i][pos_f(i)//pos_factor_result] += 1
            else:
                pos_factorisations[i][pos_f(i)//pos_factor_result] = 1
        if neg_factor_result != neg_f(i):
            if neg_f(i)//neg_factor_result in neg_factorisations[i]:
                neg_factorisations[i][neg_f(i)//neg_factor_result] += 1
            else:
                neg_factorisations[i][neg_f(i)//neg_factor_result] = 1
        factorisation = {}
        for p in pos_factorisations[i]:
            factorisation[p] = pos_factorisations[i][p]
        for p in neg_factorisations[i]:
            if p in factorisation:
                factorisation[p] += neg_factorisations[i][p]
            else:
                factorisation[p] = neg_factorisations[i][p]
        result += R(factorisation)
    return result

print F(10**7) % modulus
