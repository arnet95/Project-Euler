#Project Euler 1: Multiples of 3 and 5

#Most efficient way, based on the sum of arithmetic sequences:
def efficient(n):
    n = n - 1
    return 3*((n/3)*(n/3+1))/2 + 5*(n/5*(n/5+1))/2 - 15*(n/15*(n/15+1))/2

#Expression comprehension:
def comprehension(n):
    sum(i for i in xrange(1, n) if i%3 == 0 or i%5 == 0)

#Verbose way:
def verbose(n):
    s = 0
    for i in xrange(1, n):
        if i%3 == 0 or i%5 == 0:
            s += i
    print s

print efficient(1000)
