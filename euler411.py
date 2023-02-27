def S(n):
    s = set([])
    x = 1
    y = 1
    for i in range(2*n+1):
        x = (x * 2) % n
        y = (y * 3) % n
        s.add((x, y))
    return len(s)

for k in range(1, 31):
    print(k, k**5, S(k**5))