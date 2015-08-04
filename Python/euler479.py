#Project Euler 479: Roots on the Rise
from eulertools import modinv

def S(n, m):
    s = 0
    for k in xrange(1, n+1):
        a = k**2
        s += (1 - a) * (1 - pow(1 - a, n, m)) * modinv(a, m)
        s %= m
    return s

print S(10**6, 1000000007)

#Firstly, we expand the equation into standard cubic form.
#Using Viete's formulas for the cubic and the formula for the geometric series,
#we get that S(n) = sum_{k=1}^n ((1-k^2)*(1-(1-k^2)^n))/(k^2)
#Finally, we use the modular inverse to do the modular division.
