#Project Euler 301: Nim

def main(n):
    c = 0
    for i in xrange(1, n+1):
        if i ^ 2*i == 3*i:
            c += 1
    return c

print main(2**30)

#From Wikipedia, we can find that the X(a, b, c) = 0 if and only if a xor b xor c = 0.
#So this means we can loop through all numbers, and checking if (i ^ 2*i) ^ 3*i == 0.
#Since we have a ^ b == 0 for positive a and b if and only if a == b, we can instead
#check whether i ^ 2*i == 3*i, which is less computationally expensive.
#This finishes in about 3 seconds using pypy.
