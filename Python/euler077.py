#Project Euler 77: Prime summations
from eulertools import primes

def isprime(n):
    if n == 2 or n == 3:
        return True
    if pow(2, n-1, n) == 1:
        if pow(3, n-1, n) == 1:
            for i in xrange(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
    return False

mem = {}
def f(n, max_allowed):
    if (n, max_allowed) in mem:
        return mem[(n, max_allowed)]
    if max_allowed == 2 or n < 3:
        tmp = n%2 == 0
    elif n == max_allowed:
        tmp = isprime(n) + f(n, max_allowed - 1)
    else:
        tmp = sum(f(n-i, min(i, n-i)) for i in primes(max_allowed+1))
    mem[(n, max_allowed)] = tmp
    return tmp

def main(target):
    n = 0
    while f(n, n-1) <= target:
        n += 1
    return n

print main(5000)

#This is a fairly simple change to the code from Problem 76, but the main idea
#is the same. The base case is changed to reflect that 2 is the smallest prime number.
#The first recursive clause checks whether n is prime, otherwise it would not be a sum.
#The second recursive clause now loops over the primes up to max_allowed, rather
#than all the integers up to max_allowed, but the rest of the code for f is the same.
#Then we simply add a main function to loop until we find what we are looking for.
