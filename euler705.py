from eulertools import primes

def G(N):
    s = ""
    for p in primes(N):
        s += str(p)
    return s

def F(N):
    d = {(0, )*9: 1}
    for c in G(N):
        digit = int(c)
        new_d = {}
        for i in range(1, digit+1):
            if digit % i == 0:
                pass
