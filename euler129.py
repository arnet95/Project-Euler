#Project Euler 129: Repunit divisibility
from fractions import gcd

def A(n):
    rem = 1
    counter = 1
    old = 1
    while rem != 0:
        old *= 10
        old %= n
        rem += old
        rem %= n
        counter += 1
    return counter


def main(n):
    i = n+1 #Since A(n) <= n
    while True:
        if gcd(i, 10) == 1:
            if A(i) > n:
                return i
        i += 2


print main(10**6)
