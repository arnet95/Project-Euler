from eulertools import primes, isqrt

def mobius_gen(n):
    mobius_list = [1 for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            mobius_list[i] *= (-1)
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                mobius_list[i] = 0
            k += 1
    return mobius_list

def sqcount(n):
    mobius_list = mobius_gen(isqrt(n))
    count = 0
    for k in range(1, isqrt(n)+1):
        count += (n//(k**2))*mobius_list[k]
    return count

def S(N):
    return sum(k**2*sqcount(N//(k**2)) for k in range(1, isqrt(N)+1))

print(S(10))
print(S(100))
print(S(10**14) % (10**9+7))
