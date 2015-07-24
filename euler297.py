#Project Euler 297: Zeckendorf Representation
import time

fib_cache = {0: 1, 1: 1, 2: 2}
def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        tmp = fib(n-1) + fib(n-2)
        fib_cache[n] = tmp
        return tmp

S_cache = {1: 0, 2: 1, 3: 2, 5: 5}
def S(n):
    if n in S_cache:
        return S_cache[n]
    else:
        i = 1
        while fib(i) <= n:
            i += 1
        i -= 1
        f = fib(i)
        if f == n:
            return 2 * S(fib(i-2)) + S(fib(i-3)) + fib(i-3) + fib(i-2)
        else:
            m = n - 1 - f
            return S(f) + 1 + m + S(m+1)

def main(n):
    i = 1
    while fib(i) <= n:
        S_cache[fib(i)] = S(fib(i))
        i += 1
    return S(n)

print main(10**17)
