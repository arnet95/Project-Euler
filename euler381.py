from eulertools import primes
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main(n):
    return sum((-1 + 15*modinv((p-4)*(p-3)*(p-2)*(p-1), p))%p for p in primes(n)[2:])

print main(10**8)