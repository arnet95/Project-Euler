#Project Euler 485: Maximum number of divisors
from eulertools import dynamic_sigma
import time

def S(u, k):
    l = dynamic_sigma(0, u+1)
    s = 0
    curr_max = max(l[1:k+1])
    curr_index = k - l[1:k+1].index(curr_max) - 1
    for i in xrange(1, u - k + 2):
        s += curr_max
        curr_val = l[i + k]
        if curr_index == (k - 1):
            curr_max = max(l[i+1:i+k+1])
            curr_index = k - l[i+1:i+k+1].index(curr_max) - 1
        elif curr_val > curr_max:
            curr_max = curr_val
            curr_index = 1
        else:
            curr_index += 1
    return s

t = time.time()
print S(10**8, 10**5)
print time.time() - t
