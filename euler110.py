from eulertools import primes
from math import log
from Queue import *

prime_list = primes(10**6)

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

def decreasing(t):
    return all(t[i] >= t[i+1] for i in xrange(len(t)-1))

def d(exp):
    return prod([2*r+1 for r in exp])

def priority(t):
    return sum(t[i]*log(prime_list[i]) for i in xrange(len(t)))

def get_new_candidates(t):
    l = []
    for i in xrange(len(t)):
        cand = t[:i] + (t[i]+1, ) + t[i+1:]
        if decreasing(cand):
            l.append(t[:i] + (t[i]+1, ) + t[i+1:])
    l.append(t + (1, ))
    return l

def F(limit):
    guesses = PriorityQueue()
    guesses.put((priority((1, )), (1,)))
    items_in_queue = set([(1, )])
    current_guess = ()
    largest_f = d(current_guess)
    while largest_f < limit:
        candidate = guesses.get()
        if d(candidate[1]) > largest_f:
            current_guess = candidate[1]
            largest_f = d(candidate[1])
        for new_cand in get_new_candidates(current_guess):
            if new_cand not in items_in_queue:
                guesses.put((priority(new_cand), new_cand))
                items_in_queue.add(new_cand)
    return current_guess

def main(n):
    t = F(2*n)
    result = 1
    for i in xrange(len(t)):
        result *= prime_list[i]**t[i]
    return result

print main(4*10**6)
