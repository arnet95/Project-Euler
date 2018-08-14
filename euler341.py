l = [(1, 1, 1), (2, 3, 2)]

i = 4
j = 2
j_index = 1

while i < 10**12:
    a, b, c = l[j_index]
    l.append((i, i+(c-1), j+1))
    i += c
    j += 1
    if j >= b:
        j_index += 1

print len(l)
