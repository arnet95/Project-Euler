def A(m, n):
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2*n + 3
    elif m == 3:
        return 2**(n + 3) - 3
    elif m == 4:
        return tetration(2, n+3, 14**8) - 3
    elif m == 5:
        if n == 0:
            return 65533
        return A(4, A(m, n-1))


def tetration(b, n, modulus):
    result = b
    for i in xrange(n-1):
        result = pow(b, result, modulus)
    return result

def main(n):
    return sum(A(i, i) for i in xrange(n)) % 14**8
