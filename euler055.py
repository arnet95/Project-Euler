def is_prob_lychrel(n):
    counter = 0
    while counter < 50:
        n = n + int(str(n)[::-1])
        counter += 1
        if str(n) == str(n)[::-1]:
            return False
    return True

print sum(is_prob_lychrel(n) for n in xrange(1, 10000))
