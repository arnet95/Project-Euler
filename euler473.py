from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

mem = {-1: 1, 0: 0, 1: 1}
def fib(n):
    if n in mem:
        return mem[n]
    result = fib(n-1) + fib(n-2)
    mem[n] = result
    return result

def h(r):
    return fib(2*r+5) + fib(2*r-1)


def main(L):
    result = 1
    d = {2: [1]}
    r = 1
    while h(r) <= L:
        d[h(r)] = [2*r, 2*r+3]
        r += 1
    for subset in powerset(d.keys()):
        if sum(subset) <= L:
            l = []
            for i in subset:
                l += d[i]
            l.sort()
            if all(l[i+1] - l[i] > 1 for i in xrange(len(l)-1)):
                result += sum(subset)
    return result

print main(10**10)


#print 1 + 2 + sum(l) + 2*l[0] + sum(l[3:]) + l[1] + l[4] + 4*2 + sum(l[1:])
