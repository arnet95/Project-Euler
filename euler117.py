#Project Euler 117: Red, green, and blue tiles

mem = {}

def f(n):
    if n in mem:
        return mem[n]
    elif n < 0:
        return 0
    elif n == 0:
        mem[n] = 1
        return 1
    else:
        tmp = f(n-1) + f(n-2) + f(n-3) + f(n-4)
        mem[n] = tmp
        return tmp

print f(50)
