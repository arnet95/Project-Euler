mem = {0: 0, 1: 1}
def fib(n):
    if n in mem:
        return mem[n]
    else:
        result = fib(n-1) + fib(n-2)
        mem[n] = result
        return result

def G(n):
    r = fib(n)
    if r % 2 == 0:
        return (r - 2)//2
    else:
        return (r - 1)//2

def tri(n):
    return n*(n+1)//2

def f(l):
    return sum(tri(s2) - tri(s1-1) for s1, s2 in l)

def h(tup):
    s1, s2 = tup
    return s2+1-s1

def Msum(n):
    result = 0
    l = [(1, 1)]
    l2 = [5]
    j = 5
    while fib(j) <= n:
        result += f(l)
        new_l = []
        new_l.append((1, G(l2[0])))
        for i in xrange(1, len(l)):
            new_l.append((l[i][1]+1, G(l2[i])))
        l2 = [i+1 for i in l2]
        if l[-1][1] == 2:
            new_l.append((1, 1))
            l2.append(5)
        j += 1
        l = new_l
    remaining = n - fib(j-1)
    i = 0
    while remaining > 0:
        if h(l[i]) <= remaining:
            remaining -= h(l[i])
            s1, s2 = l[i]
            result += tri(s2) - tri(s1-1)
        else:
            s1 = l[i][0]
            result += tri(s1-1+remaining) - tri(s1-1)
            remaining = 0
        i += 1
    return result

print Msum(10**18) % (10**8)
