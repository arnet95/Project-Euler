from eulertools import primes
from math import log
prime_list = primes(10**7)

l = [1] * 500500

min_next_log = [2*log(prime_list[i]) for i in xrange(len(l))]

switch = True
while switch:
    switch = False
    p_log = log(prime_list[len(l) - 1])
    min_i, min_val = 0, p_log + 1
    i = 0
    while l[i] != 1:
        if min_next_log[i] < min_val:
            min_i, min_val = i, min_next_log[i]
        i += 1
    if min_next_log[i] < min_val:
        min_i, min_val = i, min_next_log[i]
    if min_val < p_log:
        l[min_i] *= 2
        l[min_i] += 1
        l = l[:-1]
        min_next_log[min_i] = (l[min_i] + 1) * log(prime_list[min_i])
        switch = True

s = 1
for i in xrange(len(l)):
    s *= pow(prime_list[i], l[i], 500500507)
    s %= 500500507
print s
