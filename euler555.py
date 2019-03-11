from eulertools import isqrt
def create_divisors(limit):
    divisors = [[], [1]] + [[i, 1] for i in xrange(2, limit+1)]
    for i in xrange(2, isqrt(limit) + 1):
        divisors[i*i].append(i)
        for d in xrange(i*(i+1), limit+1, i):
            divisors[d].append(i)
            divisors[d].append(d//i)
    return divisors

def SF(m, k, s):
    if s % (k-s) != 0:
        return 0
    else:
        return (k-s)*(m+1-s) + ((k-s-1)*(k-s) // 2)

def S(p, m):
    divisor_list = create_divisors(m)
    result = 0
    for s in xrange(1, p+1):
        for d in divisor_list[s]:
            k = d + s
            if s < k <= p:
                result += SF(m, k, s)
    return result

def main(N):
    return S(N, N)

print main(10**6)
