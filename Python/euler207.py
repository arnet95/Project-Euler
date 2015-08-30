#Project Euler 207: Integer partition equations
from fractions import gcd

def isPowerOfTwo(n):
    while n % 2 == 0:
        n //= 2
    return n == 1

def main(a, b):
    perfect = 0
    total = 0
    c = 1
    while perfect * b >= total * a:
        if isPowerOfTwo(c+1):
            perfect += 1
        total += 1
        c += 1
    return c * (c - 1)

print main(1, 12345)

#Let x = 2**t. This lets us rephrase our equation as x**2 = x + k <==> x**2 - x - k = 0.
#If we write k = c(c+1) for all integers k (this is always possible), we can
#factor our quadratic polynomimal. We have x**2 - x - k = (x+c)(x-(c+1)), which
#has the positive solution x = c+1. So this has integer solutions only for
#those positive integers k, which can be written as c(c+1) for an integer c.
#Furthermore, this will yield an integer solution for t only when c+1 is a power
#of two. So we simply go through positive integer values for c, keeping track
#of the total number of partitions, and the number of perfect partitions.
#We keep going until we satisfy the given ratio. Then we return the last k.
