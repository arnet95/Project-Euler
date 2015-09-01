#Project Euler 491: Double pandigital number divisible by 11

mem = {}

def f(s, tup):
    if (s, tup) in mem:
        return mem[(s, tup)]
    elif sum(tup) == 20:
        tmp = s == 0
        mem[(s, tup)] = tmp
        return tmp
    else:
        tmp = 0
        l = list(tup)
        mod = (-1 if sum(tup) % 2 == 1 else 1)
        for i in xrange(10):
            if l[i] != 2:
                l[i] += 1
                tmp += f((s + mod*i) % 11, tuple(l))
                l[i] -= 1
        mem[(s, tup)] = tmp
        return tmp

def main():
    return sum(f(i, ((0,) * i + (1, ) + (0,) * (9-i))) for i in xrange(1, 10))

print main()
print len(mem)
