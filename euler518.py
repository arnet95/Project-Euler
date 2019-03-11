from eulertools import primes, isqrt
from bisect import bisect_left

def search(l, x):
    i = bisect_left(l, x)
    if i != len(l) and l[i] == x:
        return True
    else:
        return False

def gen_divs(n):
    divs = [[], [1]] + [[i,1] for i in xrange(2, n+1)]
    for i in xrange(2, isqrt(n) + 1):
        divs[i*i].append(i)
        for d in xrange(i*(i+1), n+1, i):
            divs[d].append(i)
            divs[d].append(d//i)
    return divs

def get_divs_square(n):
    l = [1, n]
    for i in xrange(2, isqrt(n)+1):
        if n % i == 0:
            l.append(i)
            l.append(n // i)
    return list(set([i*j for i in l for j in l]))


def S(n):
    res = 0
    prime_list = primes(n)
    for b in prime_list[1:-1]:
        print b
        #Case a = 2
        if (b + 1) % 3 == 0:
            c = (((b+1)**2) // 3) - 1
            if search(prime_list, c):
                res += (2+b+c)
        divisors = get_divs_square(b+1)
        a_vals = [d-1 for d in divisors if d <= b and d % 2 == 0]
        for a in a_vals:
            c = ((b+1)**2 // (a+1)) - 1
            if c < n:
                if search(prime_list, a):
                    if search(prime_list, c):
                        res += (a+b+c)
    return res

print S(10**8)
