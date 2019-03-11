from eulertools import modinv

def reversed_base_expansion(n, b):
    l = []
    while n > 0:
        l.append(n % b)
        n //= b
    return l

def choose(n, k):
    if n < k:
        return 0
    k = min(k, n-k)
    result = 1
    for i in xrange(1, k+1):
        result *= (n-i+1)
        result *= modinv(i, 999999937)
        result %= 999999937
    return result

def bincoeffmod(n, k, p):
    if k == 0:
        return 1
    n_exp = reversed_base_expansion(n, p)
    k_exp = reversed_base_expansion(k, p)
    while len(k_exp) < len(n_exp):
        k_exp.append(0)
    res = 1
    for ni, ki in zip(n_exp, k_exp):
        res *= choose(ni, ki)
        res %= p
    return res

mem = {}
def f(i, n, m, d):
    if (i, n, m, d) in mem:
        return mem[(i, n, m, d)]
    elif i == 0:
        result = (-1)**m*bincoeffmod(n-d-1, m-1, 999999937)
        result %= 999999937
        mem[(i, n, m, d)] = result
        return result
    else:
        result = (-1)*f(i-1, n, m, d)*(m-i+1)*(n-d+i-1)*modinv(i, 999999937)*modinv(n-d-m+i, 999999937)
        result %= 999999937
        mem[(i, n, m, d)] = result
        return result

def C(n, m, d):
    result = 0
    for i in xrange(d+1):
        result += f(i, n, m, d)
        result %= 999999937
    return result

print C(10**13, 10**12, 10**4)
