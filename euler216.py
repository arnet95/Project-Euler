from eulertools import primes

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

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main(n):
    l = [True for _ in xrange(n+1)]
    limit = isqrt(2*n**2)
    for p in primes(limit+1)[1:]:
        if is_square((p+1)//2, p):
            a, b = find_square_roots((p+1)//2, p)
            for i in xrange(a, n+1, p):
                if 2*i**2 - 1 > p:
                    l[i] = False
            for i in xrange(b, n+1, p):
                if 2*i**2 - 1 > p:
                    l[i] = False
    return sum(l) - 2

print main(50*10**6)
