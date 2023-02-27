from scipy.stats import gamma
from math import log


def f(N):
    limit = 0.75
    guess = 1
    while gamma.cdf(guess, N) < limit:
        guess *= 2
    low = guess/2
    high = guess
    while abs(low - high) > 1e-6:
        mid = (low + high)/2
        if gamma.cdf(mid, N) < limit:
            low = mid
        else:
            high = mid
    return (low + high)/(2*log(10))

print("%.2f" % f(10**7))

#print(gamma.cdf(4350000*log(10), 10**7))