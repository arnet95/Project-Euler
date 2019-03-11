from eulertools import primes, modinv

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

def exponent(p, n):
    exp = 0
    while n % p == 0:
        n //= p
        exp += 1
    return exp


def main(L):
    P = [(0, 4*i**2+1) for i in xrange(L+1)]
    for p in primes(2*L+1)[2:]:
        print p
        r = (p-1)*modinv(4, p) % p
        if is_square(r, p):
            a, b = find_square_roots((p-1)*modinv(4, p) % p, p)
            for i in xrange(a, L+1, p):
                n, m = P[i]
                while m % p == 0:
                    m //= p
                P[i] = (p, m)
            for i in xrange(b, L+1, p):
                n, m = P[i]
                while m % p == 0:
                    m //= p
                P[i] = (p, m)
    result = 0
    for i in xrange(1, L+1):
        result += max(P[i][0], P[i][1])
    return result % 10**18

print main(10**7)
