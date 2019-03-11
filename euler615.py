from heapq import *
from eulertools import primes
from math import log

prime_list = primes(10**7)

def priority(t):
    return sum(t[i]*log(prime_list[i]) for i in xrange(len(t)))

def get_new_candidates(t):
    l = []
    for i in xrange(len(t)-1):
        if t[i] > 0:

            l.append(t[:i] + (t[i]-1, ) + (t[i+1]+1, ) + t[i+2:])
    l.append(t[:len(t)-1] + (t[len(t)-1]-1, ) + (1, ))
    return l

def f(n, m):
    #Returns the nth number with at least m prime factors
    heap = [(priority((i,)),(i,)) for i in xrange(m, m+n+2)]
    heapify(heap)
    count = 0
    log_largest = 0
    current_guess = 0
    items_in_queue = set([(i, ) for i in xrange(m, m + n + 2)])
    while count < n:
        candidate = heappop(heap)
        if candidate[0] > log_largest:
            current_guess = candidate[1]
            items_in_queue.remove(candidate[1])
            log_largest = candidate[0]
            count += 1
            print count
            for new_can in get_new_candidates(candidate[1]):
                if new_can not in items_in_queue:
                    s = priority(new_can)
                    if s > log_largest:
                        heappush(heap, (s, new_can))
                        items_in_queue.add(new_can)
    return current_guess

def prod(t, mod):
    print t
    result = 1
    for i in xrange(len(t)):
        result *= pow(prime_list[i], t[i], mod)
        result %= mod
    return result

print prod(f(10**6, 10**6), 123454321)
