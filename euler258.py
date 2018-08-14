

def matrix_multiplication(A, B, modulus):
    """Assume that A, B are both nxn-matrices"""
    length = len(A)
    C = []
    for i in xrange(length):
        l = [sum(A[i][k] * B[k][j] for k in xrange(length)) % modulus for j in xrange(length)]
        C.append(l)
    return C

def exp_by_squaring(M, exponent, modulus):
    print exponent
    if exponent == 1:
        return M
    elif exponent % 2 == 0:
        return exp_by_squaring(matrix_multiplication(M, M, modulus), exponent // 2, modulus)
    else:
        result = exp_by_squaring(matrix_multiplication(M, M, modulus), (exponent-1) // 2, modulus)
        return matrix_multiplication(M, result, modulus)


def main():
    M = []
    M.append([0]*1998 + [1, 1])
    for i in xrange(1999):
        new_l = [0]*2000
        new_l[i] = 1
        M.append(new_l)

    return sum(exp_by_squaring(M, 10**18, 20092010)[-1]) % 20092010

print main()
