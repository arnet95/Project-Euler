from eulertools import primes, isqrt

def is_square(n):
    return isqrt(n)**2 == n

def f(p):
    b = 1
    while not is_square(4*p - 27*b**2):
        b += 1
    a = isqrt(4*p-27*b**2)
    if a % 3 != 1:
        return -a
    return a

def F(p):
    if p % 3 == 1:
        return (p-1)*(f(p)+p-8)
    else:
        return (p-1)*(p-2)

def main(N):
    return sum(F(p) for p in primes(N))

print(main(6*10**6))