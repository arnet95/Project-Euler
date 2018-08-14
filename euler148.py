def base_convert(n, base):
    l = []
    while n > 0:
        l.append(n % base)
        n //= base
    return l[::-1]

def prod(l):
    result = 1
    for i in l:
        result *= i
    return result

def count(n):
    result = 1
    while n > 0:
        result *= ((n % 7) + 1)
        n //= 7
    return result

def main(n):
    return sum(count(i) for i in xrange(n))

print main(10**9)
