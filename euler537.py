from eulertools import primes

def f(n, L):
    if n == 0:
        return [[]]
    results = []
    for i in range(1, min(n, L)+1):
        for lst in f(n-i, i):
            results.append([i] + lst)
    return results

print(len(f(10, 10)))
print(len(f(50, 50)))