#Project Euler 78: Coin partitions

g = lambda k: (k*(3*k-1)) // 2

mem = {0: 1, 1: 1}
def p(n):
    if n in mem:
        return mem[n]
    else:
        s = 0
        #Positive k's
        k, flip = 1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k += 1
            flip *= -1
        #Negative k's
        k, flip = -1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k -= 1
            flip *= -1
        mem[n] = s
        return s

def main():
    n = 1
    while (p(n) % 1000000) != 0:
        n += 1
    return n

print main()
