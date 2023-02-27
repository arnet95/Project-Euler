from random import randint

def g(m, n):
    return (m ^ n) + m + n

def G(N):
    return 2*sum((k | i) for k in range(N+1) for i in range(N-k+1))
    return sum((k ^ (n-k)) for k in range(N+1) for n in range(N-k+1)) + (N*(N+1)*(N+2))//3



n = 11
print(sum(sum(n | i for i in range(n+1)) for n in range(8, 16)))
for i in range(20):
    print(i, 9 | i)


print(G(10**2))
