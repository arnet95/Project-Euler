#Project Euler 225: Tribonacci non-divisors

T_cache = {1: 1, 2: 1, 3: 1}
def T(n):
    if n in T_cache:
        return T_cache[n]
    else:
        tmp = T(n-1) + T(n-2) + T(n-3)
        T_cache[n] = tmp
        return tmp

def divides(m):
    i = 2
    while True:
        if T(i) % m == 0:
            return True
        if T(i) % m == 1:
            if T(i+1) % m == 1:
                if T(i+2) % m == 1:
                    return False
        i += 1

def main(n):
    l = range(27, 27*(2*n), 54)
    i = 29
    while i <= l[-1]:
        if i not in l:
            if not divides(i):
                l = sorted(list(set(l + range(i, i*2*n, 2*i))))[:n]
        i += 2
    return l[-1]

print main(124)
