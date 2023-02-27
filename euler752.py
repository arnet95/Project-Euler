from eulertools import primes
from fractions import gcd
from itertools import product

def gen_primefacs(n):
    """Generates a list of a list of prime factors for all numbers <= n"""
    prime_facs = [[] for i in xrange(n+1)]
    for prime in primes(n+1):
        k = 1
        while prime**k <= n:
            for i in xrange(prime**k, n+1, prime**k):
                prime_facs[i].append(prime)
            k += 1
    return prime_facs

def lcm(n, m):
    if n == 0 and m == 0:
        return 0
    return (n*m)//gcd(n, m)

def dynamic_divisors(n):
	divs = [[], [1]] + [[1, i] for i in xrange(2, n+1)]
	for i in xrange(2, int(n**0.5) + 1):
		divs[i*i].append(i)
		divs[i*i].sort()
		for d in xrange(i*(i+1), n+1, i):
			divs[d].append(i)
			divs[d].append(d//i)
			divs[d].sort()
	return divs

divisor_list = dynamic_divisors(10**6)

def matrix_mult(m1, m2):
    """Only needed for 2x2-matrices in this case"""
    a, b, c, d = m1
    e, f, g, h = m2
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]

def matrix_exp(matrix, power, modulus):
    #The matrix
    #(a b)
    #(c d)
    #is represented as [a, b, c, d]
    if power == 0:
        return [1, 0, 0, 1]
    elif power % 2 == 1:
        return [i % modulus for i in matrix_mult(matrix, matrix_exp(matrix, power-1, modulus))]
    else:
        new_matrix = matrix_exp(matrix, power // 2, modulus)
        return [i % modulus for i in matrix_mult(new_matrix, new_matrix)]

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

memoization = {2: 0, 3: 0}

def g(factorisation):
    prime_factors = set(factorisation)
    x = prod(factorisation)
    result = 1
    for p in prime_factors:
        k = factorisation.count(p)
        if p not in memoization:
            divisors = sorted(list(set([prod(t) for t in product(divisor_list[p], divisor_list[p+1], divisor_list[p-1], divisor_list[p-1])])))
            curr = [1, 7 % x, 1, 1]
            for div1, div2 in zip(divisors[:-1], divisors[1:]):
                curr = [i % x for i in matrix_mult(curr, matrix_exp([1, 7 % x, 1, 1], div2-div1, x))]
                if curr == [1, 0, 0, 1]:
                    memoization[p] = div2
                    break
        result = lcm(result, memoization[p]*p**(k-1))
    return result

def G(N):
    return sum(g(factorisation) for factorisation in gen_primefacs(N)[2:])

print(G(10**6))
