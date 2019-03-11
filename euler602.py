modulus = 10**9+7

mem = {}
def c(n, k):
    if (n, k) in mem:
        return mem[(n, k)]
    elif n == k or k == 1:
        mem[(n, k)] = 1
        return 1
    else:
        result = (n-k+1)*c(n-1, k-1) + k*c(n-1, k)
        result %= modulus
        mem[(n, k)] = result
        return result

print c(1000000, 400000)
