from eulertools import primes

def prime_factors_gen(n):
	phis = [[2] for _ in xrange(n//2+1)]
	for p in primes(n//2+1)[1:]:
		for i in xrange(2*p, n+1, 2*p):
			phis[i//2].append(p)
	return phis

prime_factors = prime_factors_gen(10**8)

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
	l = prime_factors[(p-1)//2]
	return all([pow(n, (p-1)//pi, p) != 1 for pi in l])



def main(n):
	candidates = [p for p in primes(n)[1:] if is_square(5, p)]
	count = 1
	successes = 5 #Since 3 is a prim fib root mod 5, we add this.
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

print main(10**8)
#print len(prime_factors_gen(10**8))
