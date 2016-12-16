from eulertools import modinv, primes

main = lambda n: sum(modinv(10, p) for p in [3] + primes(n)[3:])
print main(10**7)

#Through a straightforward computation, one can find out that the divisibility
#multiplier is the modular inverse of 10 modulo the given prime p.
#Importing functions for prime generation and computing the modular inverse
#gives us the right answer fairly quickly.
