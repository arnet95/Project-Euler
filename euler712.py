from eulertools import primes
from bisect import bisect
from sys import setrecursionlimit
from random import randint

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

phi_mem = {}
prime_list = [1] + primes(10**7)
def phi(x, a):
    if (x, a) in phi_mem:
        return phi_mem[(x, a)]
    elif a == 1:
        return (x + 1) // 2
    else:
        t = phi(x, a-1) - phi(x // prime_list[a], a-1)
        phi_mem[(x, a)] = t
        return t


pi_mem = {}
def pi(x):
    if x in pi_mem:
        return pi_mem[x]
    if x < 10**6:
        result = bisect(prime_list, x) - 1
        #result = len(primes(x))
        pi_mem[x] = result
        return result
    a = pi(int(x**(1/4)))
    b = pi(int(x**(1/2)))
    c = pi(int(x**(1/3)))
    s = phi(x, a) + (((b+a-2) * (b-a+1)) // 2)
    for i in range(a+1, b+1):
        w = x // prime_list[i]
        lim = pi(int(w**(1/2)))
        s -= pi(w)
        if i <= c:
            for j in range(i, lim+1):
                s = s - pi(w//prime_list[j]) + j - 1
    pi_mem[x] = s
    return s

def S_old(N):
    result = 0
    for p in primes(N+1):
        mid_result = 0
        k = 0
        while p**k <= N:
            l = k+1
            while p**l <= N:
                mid_result += (l-k)*((N//(p**k)) - (N//(p**(k+1))))*((N//(p**l)) - (N//(p**(l+1))))
                l += 1
            k += 1
        result += 2*mid_result
    return result

def S1(N, p):
    mid_result = 0
    k = 0
    while p**k <= N:
        l = k+1
        while p**l <= N:
            mid_result += (l-k)*((N//(p**k)) - (N//(p**(k+1))))*((N//(p**l)) - (N//(p**(l+1))))
            l += 1
        k += 1
    return 2*mid_result

def S(N):
    result = 0
    for p in primes((N//isqrt(N))+1):
        result += S1(N, p)
    print("Hello")
    for c in range(1, isqrt(N)):
        print(c)
        result += 2*(N-c)*c*(pi(N//c) - pi(N//(c+1)))
    return result

print(S(100))
print(S(10))
print(S(10**12)%(10**9+7))
