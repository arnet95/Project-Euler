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
        if n % 1000000 == 0:
            print(n)
        result += (1 - 2*flip_prob(n, N))**M
    #result /= k**M
    return result + base_result




print(E(100, 10))
print(E(10**10, 4000))