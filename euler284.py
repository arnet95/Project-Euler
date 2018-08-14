from eulertools import modinv

def crt(remainders, moduli):
    s = remainders[0]
    prod = moduli[0]
    for a, m in zip(remainders, moduli)[1:]:
        s = s + ((a-s)*modinv(prod, m) % m)*prod
        prod *= m
    return s

def base_convert(n, base):
    l = []
    while n > 0:
        l.append(n % base)
        n //= base
    return l[::-1]

def format_base14(l):
    s = ""
    for i in l:
        s += "0123456789abcd"[i]
    return s

def main(n):
    result = 1 #Counting 1
    m1, m2 = 1, 1
    for i in xrange(1, n+1):
        print i
        m1 *= 2
        m2 *= 7
        solutions = [crt([1, 0] , [m1, m2]), crt([0, 1] , [m1, m2])]
        for solution in solutions:
            if solution >= (m1*m2)//14:
                result += sum(base_convert(solution, 14))
    return format_base14(base_convert(result, 14))

print main(10**4)
