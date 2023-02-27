def choose2(n):
    return (n*(n-1))//2

def T(N, m):
    if 2*m >= N + 2:
        return N-m+1
    else:
        return choose2(N) - choose2(m) + 1

print(T(3, 2), T(8, 4))
