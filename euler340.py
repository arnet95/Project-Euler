#Project Euler 340: Crazy Function

#Important result
#F(b - na - m) = (4 + 3n)(a - c) + b - m
def S(a, b, c):
    m, q = b%a, b/a
    s = (m + 1) * ((a - c) * (4 + 3 *q ) + b)
    s += a * (a - c) * (4 * q + 3 * (q * (q - 1)/2)) + a * b * q
    s -= ((a * (a-1))/2) * q + ((m + 1) * m)/2
    return s

print S(21**7, 7**21, 12**7)
