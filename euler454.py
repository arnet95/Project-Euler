def F(L):
    result = 0
    for k in xrange(1, L):
        result += len([n for n in xrange(k+1, L) if (n**2 % k == 0) and (n + ((n**2)//k) <= L)])
    return result

print F(1000)
