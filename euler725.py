

def ds(n):
    return sum(int(c) for c in str(n))


def S1(n):
    result = 0
    for i in range(n):
        for k in range(10**n):
            s = str(k)
            s = "0"*(n - len(s)) + s
            if ds(k) == 2*int(s[i]):
                result += k
    return result

def S2(n):
    result = 0
    for d in range(1, 10):
        for i in range(0, n-1):
            for j in range(i+1, n):
                result += d*(10**i + 10**j)
    return result

def S2_new(n):
    result = 0
    for d in range(1, 10):
        for i in range(n-1):
            result += d*(10**i*(n-i-1) + 10**(i+1)*(10**(n-i-1) - 1)//9)
    return result

def S(n):
    return S1(n) - S2(n)

#print(S(3))
#print(S(7))
print(S2(200) - S2_new(200))
print(S2_new(2020))