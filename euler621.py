from eulertools import primes, isqrt

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
    if n == 1:
        return 1, p-1
    """Implementing Cipolli's algorithm"""
    a = 1
    while is_square((a**2-n) % p, p):
        a += 1
    result = exp_in_fp2((a, 1), (p+1)//2, (a**2-n) % p, p)
    return result[0], p - result[0]

def power(p, n):
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count

def G(n):
    count = 0
    prime_list = primes(isqrt(4*n+1)+1)
    N = 8*n+3
    l = [1 for _ in xrange((isqrt(8*n+3)-1)//2+1)]
    products = [2 for _ in xrange((isqrt(8*n+3)-1)//2+1)]
    for p in prime_list[1:]:
        L = N % p
        if L == 0:
            sol = ((-1)*(p+1)//2) % p
            for i in xrange(sol, len(l), p):
                exp = power(p, N-(2*i+1)**2)
                products[i] *= p**exp
                if p % 4 == 1:
                    l[i]*= (exp+1)
                else:
                    if exp % 2 != 0:
                        l[i] = 0
        if is_square(L, p):
            l1, l2 = find_square_roots(L, p)
            sol1 = ((-1 + l1)*(p+1)//2) % p
            sol2 = ((-1 + l2)*(p+1)//2) % p
            for i in range(sol1, len(l), p) + range(sol2, len(l), p):
                exp = power(p, N-(2*i+1)**2)
                products[i] *= p**exp
                if p % 4 == 1:
                    l[i]*= (exp+1)
                else:
                    if exp % 2 != 0:
                        l[i] = 0
    for k in xrange((isqrt(8*n+3)-1)//2+1):
        if N - (2*k+1)**2 != products[k]:
            p = (N - (2*k+1)**2)//products[k]
            if p % 4 == 3:
                l[k] = 0
            else:
                l[k] *= 2
    return sum(l)
print G(17526*10**9)
