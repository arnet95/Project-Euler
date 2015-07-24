#def f(lst):




l = []
for a in [3, 2]:
    for b in range(a, 1, -1):
        for c in range(b, 1, -1):
            for d in range(c, 1, -1):
                for e in range(d, 0, -1):
                    for f in range(e, 0, -1):
                        for g in range(min(f, 2), -1, -1):
                            for h in range(min(g, 2), -1, -1):
                                for i in range(min(h, 2), -1, -1):
                                    for j in range(min(i, 2), -1, -1):
                                        if a + b + c + d + e + f + g + h + i + j == 18:
                                            l.append([a, b, c, d, e, f, g, h, i, j])

#for i in l:
print l
