from eulertools import primes

def g(p, q, r):
    return 2*p*q*r - p*q - p*r - q*r

result = 0
ps = primes(5000)
pc = len(ps)
for i in range(pc):
    p = ps[i]
    for j in range(i+1, pc):
        q = ps[j]
        for k in range(j+1, pc):
            r = ps[k]
            result += g(p, q, r)
print(result)