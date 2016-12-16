from math import sqrt

#The equation in question is the Pell equation.
#The function solve implements the Chakravala method to solve the equation:
#https://en.wikipedia.org/wiki/Chakravala_method
#Then it's just a matter of finding the relevant answer to the question

def solve(D):
    a, b = int(sqrt(D)), 1
    k = a**2 - D
    while k != 1:
        m = 0
        while ((b*m + a) % k) != 0:
            m += 1
        old_dist = abs(m**2 - D)
        while True:
            m += abs(k)
            new_dist = abs(m**2 - D)
            if new_dist > old_dist:
                m -= abs(k)
                break
            old_dist = new_dist
        a, b, k = (a*m + D*b) / abs(k), (a + b*m) / abs(k), (m**2 - D) / k
    return a

def main(n):
    return max([n for n in xrange(1, 1001) if sqrt(n) % 1 != 0], key=solve)

print main(1000)
