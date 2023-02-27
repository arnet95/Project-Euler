from itertools import combinations

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def f(s, comb, i):
    new_comb = [comb[0]]
    for j in range(1, len(comb)):
        new_comb.append(comb[j] - comb[j-1])
    result = 0
    for c in new_comb:
        result += int(s[:c])
        if result > i:
            return False
        s = s[c:]
    result += int(s)
    return result == i

def T(N):
    #Precompute combinations and remove
    combs = [[]]
    for str_length in range(1, 14):
        l = [combinations(range(1, str_length), j) for j in range(1, str_length)]

        combs.append(l)


    result = 0
    for i in range(1, isqrt(N)+1):
        n = i**2
        s = str(n)
        l = len(s)
        if any(any(f(s, comb, i) for comb in combinations(range(1, l), j)) for j in range(1, l)):
            print(n)
            result += n
    return result

print(T(10**12))
