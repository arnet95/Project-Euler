#Euler 122
from math import log

def convert_to(b, n):
    k = int(log(n)/log(b))
    l = [0]*(k+1)
    while n > 0:
        l[k] = n/(b**k)
        n = n % (b**k)
        k -= 1
    return l


binary = {}
for i in xrange(1, 201):
    b = convert_to(2, i)
    binary[i] = len(b) - 1 + sum(b[:-1])


def f(available, n, target):
    if target in available:
        return n
    elif n >= binary[target]:
        return binary[target]
    else:
        a = []
        for i in available:
            for j in available:
                if i + j not in available:
                    available.append(i + j)
                    a = f(available, n + 1, target)
        return min(a)



print f([1], 0, 2)
