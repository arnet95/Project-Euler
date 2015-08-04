#Project Euler 78: Coin partitions

def g(k):
    return (k*(3*k-1))/2


mem = {0: 1, 1: 1}
def p(n):
    if n in mem:
        return mem[n]
    else:
        s = 0
        #Positives
        k, flip = 1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k += 1
            flip *= -1
        #Negatives
        k, flip = -1, 1
        while g(k) <= n:
            s += flip*p(n - g(k))
            k -= 1
            flip *= -1
        mem[n] = s
        return s

def main():
    n = 1
    while True:
        if (p(n) % 1000000) == 0:
            return n
        n += 1

print main()
