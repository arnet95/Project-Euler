from eulertools import totient_gen

def H(n):
    totients = totient_gen(n)
    return 3 * n * (n+1) - 6 * sum(totients[1:])

print H(10**8)
