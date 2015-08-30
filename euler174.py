
n = 10**6
d = {i:0 for i in xrange(n+1)}

hole_size = 1 #Hole size
while hole_size < n // 4:
    k = 0
    while 4*k*(hole_size+k) <= n:
        d[4*k*(hole_size+k)] += 1
        k += 1
    hole_size += 1

def N(n):
    return d.values().count(n)

print sum(N(i) for i in xrange(1, 11))
