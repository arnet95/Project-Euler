from eulertools import primes
from sys import setrecursionlimit

phi_mem = {}
def pi(x):
    prime_list = [1] + primes(int(x**0.5)+1)
    def phi(x, a):
        if (x, a) in phi_mem:
            return phi_mem[(x, a)]
        elif a == 1:
            return (x + 1) // 2
        else:
            t = phi(x, a-1) - phi(x // prime_list[a], a-1)
            phi_mem[(x, a)] = t
            return t
    return phi(x, len(prime_list) - 1) + len(prime_list) - 2

setrecursionlimit(10**4)
def S(n):
    mem = {1: 0, 2: 1, 3: 2, 4: 3, 5: 5}
    if n in mem:
        return mem[n]
    else:
        return pi(n) + pi(n-2) - 1 + max((n//2 + 1) - 2, 0) + (n // 2 - 2)*(n // 2 - 1) - (n//2 - 2)*(n % 2 == 0)

F_mem = {0: 0, 1: 1}
def F(n):
    if n in F_mem:
        return F_mem[n]
    else:
        tmp = F(n-1) + F(n-2)
        F_mem[n] = tmp
        return tmp

def main(n):
    return sum(S(F(k)) for k in xrange(3, n+1))

print main(44)
