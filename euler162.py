#Project Euler 162: Hexadecimal numbers


mem = {}
def f(n, one, zero, A):
    if (n, one, zero, A) in mem:
        return mem[(n, one, zero, A)]
    else:
        if n == 0:
            tmp = 1*(one and zero and A)
        else:
            tmp = f(n-1, True, zero, A) + f(n-1, one, True, A) + f(n-1, one, zero, True)
            tmp += 13*f(n-1, one, zero, A)
        mem[(n, one, zero, A)] = tmp
        return tmp

def g(n):
    result = f(n-1, True, False, False) + f(n-1, False, False, True)
    result += 13*f(n-1, False, False, False)
    return result

def main():
    s = 0
    for i in xrange(1, 17):
        s += g(i)
    return hex(s)[2:].upper()

print main()
