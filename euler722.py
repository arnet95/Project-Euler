def E(k, n):
    #Returns E_k(1 - 1/n)
    result = 0
    rd = 1
    for d in range(1, 10**8):
        rd *= (n/(n-1))
        result += d**k/(rd - 1)
    return result

print("{:.12e}".format(E(1, 16)))
print("{:.12e}".format(E(3, 2**8)))
print("{:.12e}".format(E(7, 2**15)))