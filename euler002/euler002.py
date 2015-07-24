#Project Euler 2: Even Fibonacci numbers
import time

def while_loop(n):
    xp, xpp = 2, 1
    s = 0
    while xpp < n:
        if xpp % 2 == 0:
            s += xpp
        xp, xpp = xp + xpp, xp

    return s

def unmemoized(n):
    def unmemoized_fib(n):
        return n if n < 3 else unmemoized_fib(n-1) + unmemoized_fib(n-2)
    s = 0
    c = 1
    while True:
        a = unmemoized_fib(c)
        if a >= n:
            return s
        if a % 2 == 0:
            s += a
        c += 1

def memoized(n):
    mem = {1: 1, 2: 2}
    def memoized_fib(n):
        if n in mem:
            return mem[n]
        else:
            tmp = memoized_fib(n-1) + memoized_fib(n-2)
            mem[n] = tmp
            return tmp
    s = 0
    c = 1
    while True:
        a = memoized_fib(c)
        if a >= n:
            return s
        if a % 2 == 0:
            s += a
        c += 1

print "Result:", while_loop(4000000)


#Timing

t1 = time.time()
unmemoized(4000000)
t2 = time.time()
for i in xrange(10000):
    while_loop(4000000)
t3 = time.time()
for i in xrange(10000):
    memoized(4000000)
t4 = time.time()

print "Timing"
print "One run of unmemoized:", t2 - t1
print "10000 runs of while_loop:", t3 - t2
print "10000 runs of memoized:", t4 - t3

#Not very surprisingly, the unmemoized version is tremendously slow.
#Also, the while loop is about 6 times as fast as the memoized recursive version.
