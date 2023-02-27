def F(s):
    d = {(0, False): (1, 0)}
    for i in range(len(s)):
        new_d = {}
        for ds, flag in d:
            count, sum = d[(ds, flag)]
            if flag:
                for next_digit in range(10):
                    val = next_digit*10**(len(s)-i-1)
                    new_ds = ds + next_digit
                    if (new_ds, True) in new_d:
                        old_count, old_sum = new_d[(new_ds, True)]
                        new_d[(new_ds, True)] = (old_count + count, old_sum + sum + val*count)
                    else:
                        new_d[(new_ds, True)] = (count, sum + val*count)
            else:
                for next_digit in range(int(s[i])):
                    #flag is now true
                    val = next_digit*10**(len(s)-i-1)
                    new_ds = ds + next_digit
                    if (new_ds, True) in new_d:
                        old_count, old_sum = new_d[(new_ds, True)]
                        new_d[(new_ds, True)] = (old_count + count, old_sum + sum + val*count)
                    else:
                        new_d[(new_ds, True)] = (count, sum + val*count)
                next_digit = int(s[i])
                val = next_digit*10**(len(s)-i-1)
                new_ds = ds + next_digit
                if (new_ds, False) in new_d:
                    old_count, old_sum = new_d[(new_ds, False)]
                    new_d[(new_ds, False)] = (old_count + count, old_sum + sum + val*count)
                else:
                    new_d[(new_ds, False)] = (count, sum + val*count)
        d = new_d.copy()
        print(d)
    #print(d)
    result = 0
    for t in d:
        if t[0] != 0:
            result += d[t][1]/t[0]
    return result


print("%.12e" %F("1234567890123456789"))