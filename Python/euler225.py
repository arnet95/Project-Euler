#Project Euler 225: Tribonacci non-divisors

T_cache = {1: 1, 2: 1, 3: 1}
def T(n):
    """Memoized Tribonacci function"""
    if n in T_cache:
        return T_cache[n]
    else:
        tmp = T(n-1) + T(n-2) + T(n-3)
        T_cache[n] = tmp
        return tmp

def divides(m):
    """Returns whether m divides any terms in the Tribonacci sequence"""
    i = 2
    while True:
        #If we ever find a divisor, return True
        if T(i) % m == 0:
            return True
        #Otherwise we do cycle detection. If we ever find the moduli (1, 1, 1)
        #later out in the sequence, we will never find a divisor, because we get a cycle.
        if T(i) % m == 1:
            if T(i+1) % m == 1:
                if T(i+2) % m == 1:
                    return False
        i += 1

def main(n):
    #We use that 27 is a known non-divisor, and so is also any multiple of 27.
    l = range(27, 27*(2*n), 54)
    i = 29
    while i <= l[-1]:
        if i not in l:
            if not divides(i):
                #Once we find a divisor, we add enough multiples of that number to the list.
                #We take the first n values of the sorted list, and move on.
                l = sorted(list(set(l + range(i, i*2*n, 2*i))))[:n]
        i += 2
    return l[-1]

print main(124)
