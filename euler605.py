n = 10**8+7
k = 10**4+7
m = (k-2) % n
modulus = 10**8
print (pow(2, n-2-m, modulus)*(n + (m+1)*(pow(2, n, modulus)-1))*(pow(2, n, modulus) - 1)**2) % modulus
