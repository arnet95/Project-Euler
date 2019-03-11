from math import factorial

choose_mem = {}

def choose(n, k):
    if (n, k) in choose_mem:
        return choose_mem[(n, k)]
    elif n < k:
        return 0
    else:
        k = min(k, n-k)
        result = 1
        for i in xrange(1, k+1):
            result *= (n-i+1)
            result //= i
        choose_mem[(n, k)] = result
        return result

def p(n, alphabetsize):
    result = 0
    for i in xrange(2, n+1):
        for j in xrange(1, alphabetsize):
            for k in xrange(j+1, alphabetsize+1):
                for s in xrange(i-1):
                    result += choose(alphabetsize-k, s)*choose(k-j-1, i-s-2)*choose(k-i+s, n-i)
    return result

def main(alphabetsize):
    return max(p(n, alphabetsize) for n in xrange(1, alphabetsize+1))

print main(26)
