#Project Euler 191: Prize Strings

mem = {}

def f(l, a, n):
    if (l, a, n) in mem:
        return mem[(l, a, n)]
    elif n == 0:
        b = 1 * (l < 2 and a < 3)
        mem[(l, a, n)] = b
        return b
    elif l == 2 or a == 3:
        mem[(l, a, n)] = 0
        return 0
    else:
        b = f(l+1, 0, n-1) + f(l, a+1, n-1) + f(l, 0, n-1)
        mem[(l, a, n)] = b
        return b

def main(n):
    return f(0, 0, n)

print main(30)
