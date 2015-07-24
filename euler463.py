#Project Euler 463: A weird recurrence relation
import time

f_mem = {1: 1, 3: 3}

def f(n):
    if n in f_mem:
        return f_mem[n]
    elif n % 2 == 0:
        tmp = f(n/2)
    elif n % 4 == 1:
        tmp = 2 * f(2 * (n/4) + 1) - f(n/4)
    else:
        tmp = 3 * f(2 * (n/4) + 1) - 2 * f(n/4)
    f_mem[n] = tmp
    return tmp

S_mem = {1:1, 2: 2, 3: 5}

def S(n):
    if n in S_mem:
        return S_mem[n]
    elif n % 4 == 0:
        tmp = S(n - 1) + f(n/4)
    elif n % 4 == 1:
        tmp = S(n - 2) + 2 * f(2*(n/4) + 1)
    elif n % 4 == 2:
        tmp = S(n - 3) + 3 * f(2*(n/4) + 1)
    else:
        tmp = 6 * S(2*(n/4) + 1) - 1 - 8 * S(n/4)
    S_mem[n] = tmp
    return tmp

t0 = time.time()
print "Result:", S(3**37)
t1 = time.time()
print "Time taken:", t1 - t0
print len(f_mem)
print len(S_mem)
