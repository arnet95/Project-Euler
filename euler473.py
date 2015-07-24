#Project Euler 473: Phigital number base
from math import sqrt, log
phi = (1 + sqrt(5))/2
#n_max =

f_cache = {0: 0, 1: 1}
def f(n):
    if n in f_cache:
        return f_cache[n]
    elif n < 0:
        tmp = f(n+2) - f(n+1)
    else:
        tmp = f(n-1) + f(n-2)
    f_cache[n] = tmp
    return tmp

def phi_pow(n):
    return [f(n), f(n-1)]

def phi_sum(n):
    """Returns phi^(n-1) + phi^(-n)"""
    return [f(n-1) + f(-n), f(n-2) + f(-n-1)]

l = [0]
#for i in xrange(1, )
