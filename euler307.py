def p(k, n):
    mem = {i: 1. for i in xrange(k % 2, k+1, 2)}
    for counter in xrange(1, k+1):
        new_mem = {}
        if (k - counter) % 2 == 0:
            num_twos = (k - counter) // 2
            num_zeros = n - num_twos
            new_mem[0] = (num_zeros / float(n))*mem[1]
        for num_ones in xrange(2 - ((k - counter) % 2), k - counter + 1, 2):
            num_twos = (k - counter - num_ones) // 2
            num_zeros = n - num_ones - num_twos
            a = (num_zeros / float(n))*mem[num_ones+1]
            b = (num_ones / float(n))*mem[num_ones-1]
            new_mem[num_ones] = a + b
        mem = new_mem
    return round(1 - mem[0], 10)

print p(20000, 1000000)
