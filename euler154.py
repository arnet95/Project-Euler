from math import log

limit = 200000

def legendre(p, n):
    if n == 0:
        return 0
    count = 0
    power = p
    while power <= n:
        count += (n//power)
        power *= p
    return count

vp2 = [legendre(2, i) for i in range(limit + 1)]
upbound2 = vp2[limit] - 12
vp5 = [legendre(5, i) for i in range(limit + 1)]
upbound5 = vp5[limit] - 12

count = 0
for a in range(0, limit+1):
    for b in range(0, (limit-a)+1):
        c = limit - (a + b)
        if (upbound2 >= vp2[a] + vp2[b] + vp2[c]) and (upbound5 >= vp5[a] + vp5[b] + vp5[c]):
            count += 1
print(count)
