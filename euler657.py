from eulertools import modinv


def I(alpha, n, mod):
    result = (-1)**(alpha+1) +(-1)**alpha*alpha*(n+1)
    current_coeff = alpha
    for i in xrange(2, alpha):
        print i
        current_coeff *= (alpha-i+1)
        current_coeff *= modinv(i, mod)
        current_coeff %= mod
        result += (-1)**(alpha-i+1)*current_coeff*(pow(i, n+1, mod)-1)*modinv(i-1, mod)
        result %= mod
    return result

print I(10**7, 10**12, 10**9+7)
