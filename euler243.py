#Euler 243
from __future__ import division
from eulertools import primes
from fractions import *

prime_list = primes(10**6)

target_num = 4
target_den = 10

n = 1
frac_num = 1
frac_den = 1
i = 0
while True:
    if frac_num * n * target_den < frac_den * (n - 1) * target_num:
        print n
        break
    else:
        p = prime_list[i]
        n *= p
        frac_num *= (p - 1)
        frac_den *= p
