from eulertools import primes, isqrt, prod

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

N = 10**8
mobius_list = mobius_gen(isqrt(10**16)//2)

def sqfcount(n):
    count = 0
    for k in range(1, isqrt(n)+1):
        count += (n//(k**2))*mobius_list[k]
    return count

prime_list = primes(10**8)

results = {}
k = 1

result = 0
i = 0
while prime_list[i]**2 <= N:
    result += sqfcount(N//(prime_list[i]**2))
    i += 1

print(result)


#while prod(prime_list[:k])**2 <= N:
#    result = 0
#    i = 0
#    while prod(prime_list[i:i+k])**2 <= N:

#    k += 1#
print(sqfcount(2**50))