from eulertools import primes

def six_powers(n):
    l = [1]
    for p in primes(n**(1/6) + 1):
        new_l = []
        k = 6
        while p**k <= n:
            i = 0
            while l[i]*p**k <= n:
                i += 1
                new_l.append(l[i]*p**k)
            k += 6
        l.sort()


def f(n):
    ps = primes(2*10**6)
    

