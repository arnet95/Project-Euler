#Euler 187
from time import time
from eulertools import primes

t_start = time()
a = primes(5*(10**7))
l = []

for i in a:
    for j in a:
        x = i*j
        if x < 10**8:
            l.append(x)
        else:
            break

print len(set(l))

t_finish = time()
print t_finish-t_start
