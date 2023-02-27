def left_pad(s, length):
    if len(s) < length:
        return "0"*(length - len(s)) + s
    return s

def F(R, M, modulus):
    result = 0
    num_digits = len(str(M))
    for a in range(num_digits):
        print(a)
        init_dict = [0]*10
        for m in range(M+1):
            init_dict[int(left_pad(str(m), num_digits)[a])] += 1
        print(a)
        d = init_dict[:]
        for r in range(1, R):
            new_d = [0]*10
            for i in range(10):
                for j in range(10):
                    new_prod = (i*j) % 10
                    new_d[new_prod] += d[i]*init_dict[j]

            d = [new_d[i] % modulus for i in range(10)]
        result += 10**(num_digits-a-1)*sum(i*d[i] for i in range(10))
    return result % modulus

print(F(234567, 765432, 10**9+9))