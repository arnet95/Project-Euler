from eulertools import isqrt

def small_factors(n):
    l = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            l.append(i)
        i += 1
    return l

def gen_divs(N):
    l = [[] for _ in range(N+1)]
    d = 1
    while d**2 <= N:
        for n in range(d**2, N+1, d):
            l[n].append(d)
        d += 1
    return l

def f(N):
    divisors = gen_divs(isqrt(N))
    count = 0
    s = set([])
    a = 1
    while a**2 <= N:
        for f in divisors[a]:
            r = (a + f) * (a + (a//f))
            if r <= N:
                s.add(r)
        a += 1
    return len(s)

print(f(10**14))