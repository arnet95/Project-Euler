#Project Euler 5: Smallest multiple

from fractions import gcd

def lcm(a, b):
    return (a*b)//gcd(a, b)

lcm_list = lambda n: reduce(lcm, range(1, n+1))

print lcm_list(20)
