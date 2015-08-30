#Project Euler 78: Coin partitions

g = lambda k: (k*(3*k-1)) // 2

mem = {0: 1, 1: 1}
def p(n):
    if n in mem:
        return mem[n]
    else:
        s = 0
        #Positive k's
        k, flip = 1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k += 1
            flip *= -1
        #Negative k's
        k, flip = -1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k -= 1
            flip *= -1
        mem[n] = s
        return s

def main():
    n = 1
    while (p(n) % 1000000) != 0:
        n += 1
    return n

print main()

#This problem is strongly related to Problem 76, in that p(n) is the same as
#the number of different ways n can be written as a sum of at least two
#positive integers + 1. However, using the formula from problem 76 is too slow
#for this problem, so we need to use a smarter formula. We implement p(n) by
#Euler's pentagonal number theorem:
#(https://en.wikipedia.org/wiki/Partition_(number_theory)#Recurrence_formula)
#Then we simply try all values of n until we find one which is divisible by 10**6.
