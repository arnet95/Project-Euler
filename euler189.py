from itertools import product
from random import randint


l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
#, 4, 5, 5, 6, 6, 7, 7, 8]

print sum(l)

previous = {(0,): 1, (1,): 1, (2,): 1}

def acceptable_rows(a, b):
    if len(a) == len(b):
        for i in xrange(len(a)):
            if a[i] == b[i]:
                return False
        return True
    else:
        for i in xrange(len(b)):
            if i == 0:
                if a[i] == b[i]:
                    return False
            elif i == len(b)-1:
                if a[i-1] == b[i]:
                    return False
            else:
                if a[i] == b[i] or a[i] == b[i-1]:
                    return False
        return True

for i in xrange(1, len(l)):
    new = {}
    for tup in product([0, 1, 2], repeat = l[i]):
        new[tup] = 0
    for tup in product([0, 1, 2], repeat = l[i]):
        for tup2 in previous:
            if acceptable_rows(tup2, tup):
                new[tup] += previous[tup2]
    previous = new.copy()

print sum(previous.values())
