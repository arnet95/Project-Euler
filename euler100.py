#Euler 100

def f():
    l = []
    n = 0
    x = 0
    while n < 2*(10**12):
        l.append(x)
        n += 1
        x = n**2-n
    return l

print len(f())
