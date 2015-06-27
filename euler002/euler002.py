#Project Euler 2: Even Fibonacci numbers

def while_loop(n):
    xp, xpp = 2, 1
    s = 0
    while xpp < n:
        if xpp % 2 == 0:
            s += xpp
        xp, xpp = xp + xpp, xp

    return s

print while_loop(4000000)
