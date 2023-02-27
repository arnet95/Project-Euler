from math import gcd

def g(n):
    if n % 2 == 1:
        return -n
    print(n, sum((-1)**i*gcd(n, i**2) for i in range(1, n+1)))
    return sum((-1)**i*gcd(n, i**2) for i in range(1, n+1))

def G(N):
    return sum(g(n) for n in range(1, N+1))

print(G(200))