#Project Euler 381: (prime-k) factorial
from eulertools import primes, modinv

def S(p):
    return (3 * modinv((-8)%p, p)) % p

def main(n):
    return sum(S(p) for p in primes(n)[2:])

print main(10**8)

#Wilson's theorem and modular inverses are the key to solving this problem.
#Wilson's theorem states that for p prime, (p-1)! = -1 mod p. This means that
#we get the follow equalities:
#S(p) = ((p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)!) % p
# = (p-1)!(1 + 1/(p-1) + 1/(p-1)(p-2) + 1/(p-1)(p-2)(p-3) + 1/(p-1)(p-2)(p-3)(p-4)) % p
# (This is fine since division is well-defined in Z_p)
# = (p-1)!(( (p-1)(p-2)(p-3)(p-4) + (p-2)(p-3)(p-4) + (p-3)(p-4) + (p-4) + 1 ) / (p-1)(p-2)(p-3)(p-4) ) % p
# = (p-1)!( (p-1)(p-2)(p-4) + (p-2)(p-4) + (p-4) + 1    /(p-1)(p-2)(p-4)   ) % p
# = (p-1)!( (p^3 + 6p^2 + 8p - 3) / (p^3 - 7p^2 + 14p - 8)) % p
# = ((p-1)! %p) * ((p^3 + 6p^2 + 8p - 3) % p) * modinv((p^3 - 7p^2 + 14p - 8), p)
# = -1 * -3 * modinv((-8) % p, p) = (3 * modinv((-8)%p, p)) % p
