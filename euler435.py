from eulertools import crt
from fractions import gcd

def pisano_period(n):
    a = (1, 1)
    count = 1
    while a != (0, 1):
        a = (a[1] % n, a[0] + a[1] % n)
        count += 1
    return count

def lcm(n, m):
    return (n*m)//gcd(n, m)

fib_mem = {0: 0, 1: 1}
def fib(n):
    if n in fib_mem:
        return fib_mem[n]
    else:
        result = fib(n-1) + fib(n-2)
        fib_mem[n] = result
        return result

def G(n, x, p, k):
    m = p**k
    if gcd(x, p) == 1:
        period = lcm((p-1)*p**(k-1), pisano_period(m))
        return ((n//period)*(sum((fib(i)*pow(x, i, m)) for i in xrange(period)) % m) + sum((fib(i)*pow(x, i, m)) for i in xrange((n % period) + 1))) % m
    else:
        return sum(fib(i)*pow(x, i, m) for i in xrange(k)) % m



def main():
    l = [(2, 11), (3, 6), (5, 3), (7, 2), (11, 1), (13, 1)]
    result = (0, 1)
    for base, exp in l:
        M = base**exp
        temp_result = 0
        for x in xrange(0, 101):
            temp_result += G(10**15, x, base, exp)
            temp_result %= M
        if result == (0, 1):
            result = (temp_result, M)
        else:
            result = (crt(temp_result, result[0], base**exp, result[1]), result[1]*M)
    return result[0]

print main()
