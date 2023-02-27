def F(n):
    return len(bin(n)[3:].rstrip("1"))

def S(N):
    result = 0
    k = 1
    while 2**k <= N:
        result += 2**(k-1)*(k-1)
        result -= (k-1)
        for j in range(k-1):
            result -= j*2**(k-j-2)
        k += 1
    result += (N - 2**(k-1) + 1)*(k-1)  
    j = 0
    while 2**j-1 + 2**(k-1) <= N:
        count = (N - 2**(k-1) - (2**j-1))//(2**(j+1)) + 1
        result -= j*count
        j += 1
    return result

print(S(10**16))
