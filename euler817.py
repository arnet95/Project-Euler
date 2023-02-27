from eulertools import isqrt

def base_convert(n, base):
    l = []
    while n > 0:
        l.append(n % base)
        n //= base
    return l[::-1]


def f(p, N):
    s = set([p - d for d in range(1, N+1)])
    result = 0

    #Last digit
    for x in range(1, (p+3)//2):
        if x % 10**6 == 0:
            print(x)
        k = pow(x, 2, p)
        if k >= p-N:
            s.remove(k)
            result += x
    #Second-to-last digit
    k = 0
    while len(s) > 0:
        print(len(s))
        low = isqrt(k*p**2 + (p-N)*p)

        high = isqrt(k*p**2 + (p+1)*(p-1)) + 1
        for n in range(low, high+1):
            for d in base_convert(n**2, p):
                if d >= p-N:
                    if d in s:
                        result += n
                        s.remove(d)
        

        k += 1

    return result

print(f(10**9+7, 10**5))