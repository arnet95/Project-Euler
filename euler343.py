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

def main(n):
    prime_list = primes(n+2)
    l = [(1, k**3+1) for k in xrange(n+1)]
    for p in prime_list:
        remainders = set([])
        if p == 2:
            remainders.add(1)
        elif p == 3:
            remainders.add(2)
        else:
            if is_square(p-3, p):
                a, b = find_square_roots(p-3, p)
                remainders.add((1+a)*((p+1)//2) % p)
                remainders.add((1+b)*((p+1)//2) % p)
            remainders.add(p-1)
        for rem in remainders:
            for i in xrange(rem, n+1, p):
                a, b = l[i]
                while b % p == 0:
                    b //= p
                l[i] = (p, b)
    result = 0
    for i in l[1:]:
        result += max(i) - 1
    return result

print main(100)
print main(2*10**6)
