import sys

sys.setrecursionlimit(10**4)


mem = {(0, 1, 0): 9, (1, 1, 0): 8, (0, 1, 1): 0, (1, 1, 1): 1}

def D2(d, k, m):
#    print(d, k, m)
    if (d, k, m) in mem:
        return mem[(d, k, m)]
    else:
        if m > k or k <= 0 or m < 0:
            result = 0
        else:
            result = D2(d, k-1, m-1) + 9*D2(d, k-1, m)
        mem[(d, k, m)] = result
        return result

def D1(d, k):
    return sum(D2(d, k, m) for m in range((k//2) + 1, k+1))

def D(N):
    return sum(D1(0, k) + 9*D1(1, k) for k in range(1, N+1))

print(D(4))
print(D(10))
print(D(2022) % (10**9 + 7))
