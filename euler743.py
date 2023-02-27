from eulertools import modinv

def A(k, m, modulus):
    f_value = 1
    result = pow(2, k*m, modulus)
    for i in range(1, k//2+1):
        if i % 10**6 == 0:
            print(i)
        a = modinv(i, modulus)
        f_value *= (k-2*i+2)*(k-2*i+1)*a**2
        f_value %= modulus
        result += (f_value*pow(2, (k-2*i)*m, modulus))
        result %= modulus
    return result



print(A(3, 3, 10**9+7))
print(A(4, 5, 10**9+7))
print(A(10**8, 10**8, 10**9+7))
