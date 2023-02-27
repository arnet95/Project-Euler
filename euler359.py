def tri(n):
    return n*(n+1)//2

def even(s):
    return s % 2 == 0

def odd(s):
    return s % 2 == 1

def P(f, r):
    s = f + r
    upper = s - (s % 2)
    lower = upper - 2
    if odd(f) and f > 1:
        return tri(lower + odd(s)) + (2*even(s) - 1)*(f//2)
    else:
        return tri(upper - even(s)) + (2*even(s) - 1)*(f//2)

def main():
    result = 0
    count = 0
    for a1 in range(28):
        for a2 in range(13):
            f = 2**a1*3**a2
            r = 2**(27-a1)*3**(12-a2)
            result += P(f, r)
    return result % (10**8)

print(main())