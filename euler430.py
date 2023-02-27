from math import comb
from math import factorial

def flip_prob(n, N):
    return 1 - ((n-1)**2 + (N-n)**2)/N**2

def E(N, M):
    k = N**2
    coeff_2 = 2 + N**2
    coeff_1 = 4 + 4*N
    base_result = 0.5*N
    result = 0
    for n in range(1, N//2 + 1):
        #Assumes N is even
        #p = flip_prob(n, N)
        result += (4*n**2 - coeff_1*n + coeff_2)**M
    result /= k**M
    return result + base_result

def E(N, M):
    a = 4
    b = -(4 + 4*N)
    c = (2 + N**2)
    result = 0
    for i in range(0, M+1):
        ai = a**i
        for j in range(0, M-i+1):
            k = M-i-j
            tri_coeff = comb(i+j, j)*comb(M, k)
            result += tri_coeff*ai*b**j*c**k*sum(n**(2*i + j) for n in range(1, N+1))
    return result/(N**(2*M) * 2) + (N/2)


print(E(100, 10))
print(E(10**7, 4000))