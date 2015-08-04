from eulertools import primes, modinv

def main(n):
    return sum((-1 + 15*modinv((p-4)*(p-3)*(p-2)*(p-1), p))%p for p in primes(n)[2:])

print main(10**8)
#Wilson's formula
