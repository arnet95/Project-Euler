from eulertools import modinv, primes

def x(p):
    return pow(2, pow(2, p, p-1), p)

def f(p):
    return (-x(p)*modinv(p, 2**p)) % (2**p)

def g(p):
    return f(p) % p
    p2mod = pow(2, p)
    p22mod = pow(2, pow(2, p, p-1), p)
    p2 = 2**p
    a = ((p2mod - p22mod)*modinv(p, p2)) % p
    b = (-p2*(((p2 - p22mod)*modinv(p, p2))  // p2)) % p
    print(p, (a+b) % p, f(p) % p)
    return (a + b) % p
    b = f(p) % p
    return a
    return f(p) % p
    return (-pow(2, pow(2, p, p-1), p))*(modinv(p, 2**p) % p) % p

def G(N):
    return sum(g(p) for p in primes(N)[1:])

for p in primes(30)[1:]:
    print(p, g(p), 2*2**p > x(p)*modinv(p, 2**p), 2**p)
#print(G(30))
