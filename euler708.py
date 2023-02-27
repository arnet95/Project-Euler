from eulertools import primes
from bisect import bisect

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
    if x < 10**7:
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

def pi_ext(k, N):
    if k == 1:
        return pi(N)

print(pi(10**14//2))