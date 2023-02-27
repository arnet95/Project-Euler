f=lambda m,n:n and n%2*m^f(2*m,n//2)

def modified_sieve(L):
    l = [True]*(L+1)
    i = 2
    while f(i, i) <= L:
        #if l[i]:
        print(i)
        k = 1
        while i*2**k <= L:
            k += 1
        for j in range(i, 2**k):
            idx = f(i, j)
            if idx <= L:
                l[idx] = False
        i += 1

    return [i for i in range(2, L+1) if l[i]]

xor_primes = modified_sieve(10**8)
print(xor_primes[4999999])