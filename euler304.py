from eulertools import primes

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def modified_prime_sieve(start, stop):
    """Returns a list of all primes p such that start <= p < stop"""
    l = [True for _ in xrange(start, stop)]
    prime_list = primes(isqrt(stop)+1)
    for p in prime_list:
        if start % p == 0:
            first = start
        else:
            first = (start//p)*p + p
        for i in xrange(first-start, stop-start, p):
            l[i] = False
    return [start+i for i in xrange(stop-start) if l[i]]

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

def fibonacci(n, mod):
    #Via matrix multiplication
    return matrix_exp([1, 1, 1, 0], n, mod)[1]

def main():
    mod = 1234567891011
    s = 0
    l = modified_prime_sieve(10**14, 10**14+5*10**6)[:100000]
    for i in l:
        s += fibonacci(i, mod)
        s %= mod
    return s

print main()
