#Project Euler 119: Digit power sum


def f(n):
    candidates = [1 for i in xrange(30*n+1)]
    count = 0
    while True:
        
