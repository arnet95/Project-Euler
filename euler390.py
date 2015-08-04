#Project Euler 390: Triangles with non rational sides and integral area

#By Heron's formula, the problem is related to finding all e,d such that
#e^2 + d^2 + (2ed)^2 is a perfect square

def is_square(n):
    return n**0.5 % 1 == 0

def f(n):
    s = 0
    for d in xrange(1, int(n**0.5)+1):
        if d % 2 == 0:
            for e in xrange(d, n//(2*d)+1):
                a = e**2 + d**2 + (2*e*d)**2
                if is_square(a):
                    if a**0.5 <= n:
                        s += int(a**0.5)
        else:
            for e in xrange(d+1, n//(2*d)+1, 2):
                a = e**2 + d**2 + (2*e*d)**2
                if is_square(a):
                    if a**0.5 <= n:
                        s += int(a**0.5)
    return s

print f(10**6)
