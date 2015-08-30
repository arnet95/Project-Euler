#Project Euler 119: Digit power sum
from math import log

def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

def f(limit):
    powers = [4, 3] + [2 for _ in xrange(4, 11)]
    logs = [log(i) for i in xrange(2, 11)]
    count = 0
    while count < limit:
        i = min(range(2, len(powers) + 1), key=lambda n: powers[n-2]*logs[n-2])
        (base, power) = (i, powers[i-2])
        n = base**power
        if digit_sum(n) == base:
            count += 1
            print count, base, power, n
        powers[i-2] += 1
        logs[i-2] += log(i)
        if powers[-1] > 2:
            powers.append(2)

    print l


f(30)
