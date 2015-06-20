def max_num(N):
    n = 1
    while True:
        if (2*n**3+3*n**2+n)/6 >= N:
            return n-1
        n += 1

def all_sums(i, N):
    result = []
    n = 1
    while True:
        s = sum(i**2 for i in xrange(n, n+i))
        if s >= N:
            return result
        result.append(s)
        n += 1

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main(N):
    max_n = max_num(N)
    sums = []
    for k in xrange(2, max_n+1):
        sums += all_sums(k, N)
    result = 0
    for s in set(sums):
        if is_palindrome(s):
            result += s
    return result

print main(10**8)