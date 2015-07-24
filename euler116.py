#Project Euler 116: Red, green or blue tiles

red_mem = {}
def reds(n, bool):
    if (n, bool) in red_mem:
        return red_mem[(n, bool)]
    elif n < 2:
        red_mem[(n, bool)] = 1*bool
        return 1*bool
    else:
        a = reds(n-1, bool) + reds(n-2, True)
        red_mem[(n, bool)] = a
        return a

green_mem = {}
def greens(n, bool):
    if (n, bool) in green_mem:
        return green_mem[(n, bool)]
    elif n < 3:
        green_mem[(n, bool)] = 1*bool
        return 1*bool
    else:
        a = greens(n-1, bool) + greens(n-3, True)
        green_mem[(n, bool)] = a
        return a

blue_mem = {}
def blues(n, bool):
    if (n, bool) in blue_mem:
        return blue_mem[(n, bool)]
    elif n < 4:
        blue_mem[(n, bool)] = 1*bool
        return 1*bool
    else:
        a = blues(n-1, bool) + blues(n-4, True)
        blue_mem[(n, bool)] = a
        return a

def f(n):
    return reds(n, False) + greens(n, False) + blues(n, False)

print f(50)
