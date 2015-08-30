#Project Euler 297: Zeckendorf Representation
import time

fib_cache = {0: 1, 1: 1}
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
            return S(f) + m + 1 + S(m+1)

def main(n):
    i = 1
    while fib(i) <= n:
        S_cache[fib(i)] = S(fib(i))
        i += 1
    return S(n)

print main(10**17)

#There is one essential property of the Zeckendorf representation we need,
#which is that using a greedy algorithm is enough to find a number's Zeckendorf
#representation. (Meaning that we can always take the largest Fibonacci number
#not exceeding n as the first number in the Zeckendorf representation.)

#What this means, is that z(n) = 1 + z(f(n)) where f(n) is the largest Fibonacci
#number not exceeding n. If we let S(n) = sum(z(k) for k in xrange(1, n)), we can
#use this to write S(n) recursively. If n is a Fibonacci number, (say fib(i)), we
#have S(fib(i)) = 
