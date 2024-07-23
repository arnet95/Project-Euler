n = 10


s = set([])
for _ in range(n):
    a = 1
    while a in s:
        a += 1
    s.add(a)
    b = 1
    while b in s or (a ^ b) in s:
        b += 1
    s.add(b)
    s.add(a ^ b)

print(s)

print(sum(s))