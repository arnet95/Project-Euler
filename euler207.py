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
