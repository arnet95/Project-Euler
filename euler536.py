from eulertools import primes

for m in range(1, 1000001):
    if all(pow(a, m+4, m) == a for a in range(2, m)):
        l = [p for p in primes(m+1) if m % p == 0]
        res = 1
        for i in l:
            res *= i
        print(m, [p for p in primes(m+1) if m % p == 0], m == res)
