#Project Euler 116: Red, green or blue tiles
import time

mem = {}
def f(n, used, k):
    if (n, used, k) in mem:
        return mem[(n, used, k)]
    elif n < k:
        a = used
    else:
        a = f(n-1, used, k) + f(n-k, True, k)
    mem[(n, used, k)] = a
    return a

def main(n):
    return f(n, False, 2) + f(n, False, 3) + f(n, False, 4)

t0 = time.time()
print main(50)
print time.time() - t0
#We let f(n, used, k) represent
