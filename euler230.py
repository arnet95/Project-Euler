#Project Euler 230: Fibonacci Words

Fib_cache = {}
def Fib(n):
    if n in Fib_cache:
        return Fib_cache[n]
    else:
        tmp = Fib(n-1) + Fib(n-2)
        Fib_cache[n] = tmp
        return tmp

def E(A, B, n, x):
    if n == 1:
        return A[x - 1]
    elif n == 2:
        return B[x - 1]
    elif x <= Fib(n - 2):
        return E(A, B, n-2, x)
    else:
        return E(A, B, n-1, x - Fib(n-2))

def D(A, B, x):
    n = 1
    while x >= Fib(n):
        n += 1
    return E(A, B, n, x)

def main(A, B, n):
    Fib_cache[1] = len(A)
    Fib_cache[2] = len(B)
    s = 0
    for i in xrange(n):
        x = D(A, B, ((127 + 19*i) * (7**i)))
        s += (10**i) * int(x)
    return s

A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

print main(A, B, 18)

#This solution builds on two main ideas. The first is that the lengths of the elements
#in the sequences form a Fibonacci sequence with seed values = len(A) and len(B).
#The second is that given a position in a string, we can relate that to a
#position with a lower numerical value in a shorter string, so the solution can
#be described recursively fairly easily.
