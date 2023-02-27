def Hhelp(N, k):

    """Return True iff the current player can force a win"""
    if N == 0:
        return False
    elif 2*k >= N:
        return True
    else:
        return any(not Hhelp(N-i, i) for i in range(1, 2*k+1))

def H(N):
    return min(i for i in range(1, N+1) if not Hhelp(N-i, i))


fib_mem = {0: 1, 1: 1}
def fib(n):
    if n in fib_mem:
        return fib_mem[n]
    else:
        result = fib(n-1) + fib(n-2)
        fib_mem[n] = result
        return result

G_fib_mem = {1: 1, 2: 3}
def G_fib(i):
    if i in G_fib_mem:
        return G_fib_mem[i]
    else:
        result = G_fib(i-1) + G_fib(i-2) - fib(i-2) + fib(i)
        G_fib_mem[i] = result
        return result

print(fib(79), G_fib(79))
