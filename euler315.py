#Project Euler 315: Digital root clocks
from eulertools import primes

def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

zero =  [1, 1, 1, 1, 1, 1, 0]
one =   [0, 1, 1, 0, 0, 0, 0]
two =   [1, 1, 0, 1, 1, 0, 1]
three = [1, 1, 1, 1, 0, 0, 1]
four =  [0, 1, 1, 0, 0, 1, 1]
five =  [1, 0, 1, 1, 0, 1, 1]
six =   [1, 0, 1, 1, 1, 1, 1]
seven = [1, 1, 1, 0, 0, 1, 0]
eight = [1, 1, 1, 1, 1, 1, 1]
nine =  [1, 1, 1, 1, 0, 1, 1]
digits = [zero, one, two, three, four, five, six, seven, eight, nine]

sam_transitions = [sum(digit) for digit in digits]
max_transitions = [[sum(a != b for a, b in zip(i, j)) for i in digits] for j in digits]

def sam_trans(n):
    s = 0
    while n:
        s += sam_transitions[n%10]
        n = n // 10
    return s

def sam_num(n):
    if n in sam_mem:
        return sam_mem[n]
    elif n < 10:
        return 2*sam_trans(n)
    else:
        return 2*sam_trans(n) + sam_num(digit_sum(n))

sam_mem = {}
for i in xrange(65):
    sam_mem[i] = sam_num(i)

def max_trans(n):
    s = 0
    m = digit_sum(n)
    while m:
        s += max_transitions[m%10][n%10]
        n, m = n/10, m/10
    return s + sam_trans(n)

def max_sub(n):
    if n in max_mem:
        return max_mem[n]
    elif n < 10:
        return sam_trans(n)
    else:
        return max_trans(n) + max_sub(digit_sum(n))

def max_num(n):
    return sam_trans(n) + max_sub(n)

max_mem = {}
for i in xrange(65):
    max_mem[i] = max_sub(i)

def main(l):
    return sum(sam_num(i) - max_num(i) for i in l)

print main(primes(2*10**7)[664579:])
