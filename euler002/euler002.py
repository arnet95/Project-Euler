#Project Euler 2: Even Fibonacci numbers

xp, xpp = 2, 1
s = 0

while xpp < 4000000:
    if xpp % 2 == 0:
        s += xpp
    xp, xpp = xp + xpp, xp

print s