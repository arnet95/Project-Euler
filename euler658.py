from eulertools import modinv

def S(k, n, mod):
    result = 0
    if k % 2 == 0:
        result +=  (n+1)*(2 + (k-2)//2)
    else:
        result += 1 - (n+1)*(k-1)//2
    result %= mod
    sgn = sign(k)
    current_h = sgn*k
    current_coeff = k+1
    for i in xrange(k-1, 1, -1):
        print i
        s = (pow(i, n+1, mod) - 1)*modinv(i-1, mod)
        result += s*sign(-i+1)*current_h
        current_coeff *= (i+1)
        current_coeff *= modinv(k-i+1, mod)
        current_coeff %= mod
        current_h = sgn*current_coeff - sign(i) - 2*current_h
        current_h %= mod
        result %= mod
    return result


print S(10**7, 10**12, 10**9+7)
