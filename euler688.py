tri = lambda k: (k*(k+1))//2

def S(N):
    result = 0
    k = 1
    while tri(k) <= N:
        j = (N - (tri(k) - 1))//k
        result += k*tri(j)
        result += (j+1)*(N - ((tri(k)-1) + j*k))
        k += 1
    return result

print(S(10**16) % (10**9+7))
