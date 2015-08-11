#Project Euler 77: Prime summations
from eulertools import primes

mem = {}
def f(n, max_allowed):
    if (n, max_allowed) in mem:
        return mem[(n, max_allowed)]
    if max_allowed == 2 or n < 3:
        tmp = n%2 == 0
    elif n == max_allowed:
        tmp = 1 + f(n, max_allowed - 1)
    else:
        tmp = sum(f(n-i, min(i, n-i)) for i in primes(max_allowed+1))
    mem[(n, max_allowed)] = tmp
    return tmp

def main(target):
    n = 0
    while True:
        if f(n, n-1) > target:
            return n
        n += 1

print main(5000)
