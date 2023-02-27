from eulertools import primes
from math import prod
from itertools import product
from math import factorial
from bisect import bisect_left, bisect_right

def legendre(p, n):
    if n == 0:
        return 0
    count = 0
    power = p
    while power <= n:
        count += (n//power)
        power *= p
    return count

def S(f, L, H):
    prime_factors = {}
    ps = primes(f+1)
    for p in ps:
        prime_factors[p] = legendre(p, f)
    num_divisors = prod([val+1 for val in prime_factors.values()])

    lambda_small_divs = [1]
    count = 1
    i = 0
    while count**2 < num_divisors:
        count *= (prime_factors[ps[i]] + 1)
        new_divs = []
        for j in range(1, prime_factors[ps[i]] + 1):
            lambda_k = (-ps[i])**j
            for lambda_div in lambda_small_divs:
                new_divs.append(lambda_div*lambda_k)
        lambda_small_divs += new_divs
        i += 1
    lambda_small_divs.sort(key=abs)
    lambda_small_divs = [i for i in lambda_small_divs if abs(i) <= H]

    lambda_big_divs = [1]
    while i < len(ps):
        new_divs = []
        for j in range(1, prime_factors[ps[i]] + 1):
            lambda_k = (-ps[i])**j
            for lambda_div in lambda_big_divs:
                new_divs.append(lambda_div*lambda_k)
        lambda_big_divs += new_divs
        i += 1
    lambda_big_divs.sort(key=abs)
    lambda_big_divs = [i for i in lambda_big_divs if abs(i) <= H]

    result = 0
    low = len(lambda_small_divs)
    high = len(lambda_small_divs)
    interval_sum = 0
    for big_d in lambda_big_divs:
        new_low = bisect_left(lambda_small_divs, L/abs(big_d), key=abs)
        new_high = bisect_right(lambda_small_divs, H/abs(big_d), key=abs)
        interval_sum += sum(lambda_small_divs[new_low:low])
        interval_sum -= sum(lambda_small_divs[new_high:high])
        low, high = new_low, new_high
        result += big_d*interval_sum
    return result

print(S(70, 10**20, 10**60) % (10**9 + 7))