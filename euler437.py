from eulertools import primes

def prime_factors_gen(n):
	phis = [[] for _ in xrange(n+1)]
	for p in primes(n+1):
		for i in xrange(p, n+1, p):
			phis[i].append(p)
	return phis

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

def is_prim_root(n, p):
    """Naive method"""
    return True

def main(prime_list):
    candidates = [p for p in prime_list if is_square(5, p)]
    count = 1
    successes = 5 #5 is a bit special, but it works
    for cand in candidates:
        a, b = find_square_roots(5, cand)
        if is_prim_root((1+a)*((cand+1)//2) % cand, cand):
            count += 1
            successes += cand
        else:
            if is_prim_root((1+b)*((cand+1)//2) % cand, cand):
                count += 1
                successes += cand
    return count, successes

#print main(primes(10**8)[1:])
print len(prime_factors_gen(10**8))
