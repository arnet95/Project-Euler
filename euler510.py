#http://mathworld.wolfram.com/TangentCircles.html

from fractions import gcd

def S(L):
    result = 0
    a = 1
    while a**4+2*a**3+a**2 <= L:
        b = 1
        while a**2*(a+b)**2 <= L and a >= b:
            s = (a*b)**2 + (a*(a+b))**2 + (b*(a+b))**2
            if gcd(a, b) == 1:
                k = 1
                while a**2*(a+b)**2*k <= L:
                    result += k*s
                    k += 1
            b += 1
        a += 1
    return result

print S(10**9)
