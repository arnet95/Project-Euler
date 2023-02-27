from eulertools import primes, prod, isqrt
from itertools import product


def f(lst, par):
    N = prod(lst)
    num_primes = len(lst)

    #First, populate small products
    small_products = []
    for t in product([0,1], repeat=par):
        factors = [lst[i] if t[i] else 1 for i in range(par)]
        small_products.append(prod(factors))
    small_products.sort()
    small_products = [n for n in small_products if n**2 <= N]
    print("Hello")
    max_psr = 0
    for t in product([0,1], repeat=num_primes-par):
        factors = [lst[i] if t[i-par] else 1 for i in range(par, num_primes)]
        n = prod(factors)
        if n**2 <= N:
            low = 0
            high = len(small_products)-1
            if (n*small_products[high])**2 <= N:
                max_psr = max(max_psr, n*small_products[high])
            else:
                while low + 1 < high:
                    mid = (low + high)//2
                    if (small_products[mid]*n)**2 > N:
                        high = mid - 1
                    else:
                        low = mid + 1
                while (n*small_products[low])**2 > N:
                    low -= 1
                max_psr = max(max_psr, n*small_products[low])
    print(N-max_psr**2)
    return max_psr

print(f(primes(190), 21) % (10**16))
