#Realize that P can be recursively described by
#P(1) = 1
#P(2) = 2
#P(2k+1) = P(2k)
#P(4k+2) = 4P(k)
#P(4k) = 4P(k)-2

#Then, through some computations, we have that
#S(4k+3) = 5 + 16S(k) - 4k

#Then, it simply remains to implement and memoize these functions.

mem_P = {1:1, 2:2}
def P(n):
    if n in mem_P:
        return mem_P[n]
    else:
        if n % 2 == 1:
            res = P(n-1)
        elif n % 4 == 2:
            res = 4*P(n//4)
        else:
            res = 4*P(n//4)-2
        mem_P[n] = res
        return res

mem_S = {i:sum(P(i) for i in xrange(1, i+1)) for i in xrange(1, 10)}
def S(n):
    if n in mem_S:
        return mem_S[n]
    elif n % 4 == 3:
        res = 5 + 16*S(n//4) - 4*(n//4)
    else:
        res = P(n) + S(n-1)
    mem_S[n] = res
    return res

print S(10**18) % 987654321
