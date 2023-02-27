from eulertools import primes
from bisect import bisect_right

def S(N):
    result = 0
    cubefulls = [1]
    for p in primes(int(N**(1/3))+1):
        new_cubefulls = []
        pk = p**3
        bisect_idx = bisect_right(cubefulls, N//pk)
        result += sum(N//d for d in cubefulls[bisect_idx:])
        cubefulls = cubefulls[:bisect_idx]
        while pk <= N:
            bisect_idx = bisect_right(cubefulls, N//pk)
            for i in cubefulls[:bisect_idx]:
                new_cubefulls.append(i*pk)
            pk *= p
        cubefulls += new_cubefulls
        cubefulls.sort()
    result += sum(N//d for d in cubefulls)
    return result

print(S(10**18))
