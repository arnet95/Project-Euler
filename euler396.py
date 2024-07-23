def base_convert(n, base):
    l = []
    while n > 0:
        l.append(n % base)
        n //= base
    return l

def update(g, curr_base):
    i = 0
    while g[i] == 0:
        i += 1
    for j in range(i):
        g[j] = curr_base - 1
    g[i] -= 1
    while g != [] and g[-1] == 0:
        g.pop()

def G(n):
    g = base_convert(n, 2)
    curr_base = 2
    count = 1
    while g != []:
        if g[0] != 0:
            curr_base += g[0]
            g[0] = 0
            while g != [] and g[-1] == 0:
                g.pop()
        else:
            print(g)
            #print(g, curr_base)
            curr_base += 1
            update(g, curr_base)
    return curr_base - 2
        



print(G(15))