from eulertools import primes
from bisect import bisect_left, insort_left

def twicemedian(l):
    if len(l) % 2 == 0:
        return l[len(l)//2] + l[len(l)//2-1]
    else:
        return 2*l[len(l)//2]

n, k = 10**7, 10**5
prime_list = primes(18*10**7)[:10**7]
S = [0] + [pow(prime_list[i], i+1, 10007) for i in xrange(n)]
S2 = [0] + [S[i] + S[(i//10000) + 1] for i in xrange(1, n+1)]


result = 0
L = sorted(S2[1:k+1])
for i in xrange(1, n-k+1):
    print i
    result += twicemedian(L)
    del L[bisect_left(L, S2[i])]
    insort_left(L, S2[i+k])
result += twicemedian(L)
print result/2.
